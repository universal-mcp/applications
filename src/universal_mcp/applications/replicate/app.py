import collections.abc
from pathlib import Path
from typing import Any

from loguru import logger

import replicate
from replicate.exceptions import ModelError as ReplicateModelError
from replicate.exceptions import ReplicateError as ReplicateAPIError
from replicate.prediction import Prediction
from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration


class ReplicateApp(APIApplication):
    """
    Application for interacting with the Replicate API.

    Provides tools to run models, manage predictions (submit, get status, retrieve results, cancel),
    upload files, and a specialized tool for generating images.

    Authentication is handled by the configured Integration provided by the
    Universal MCP server, fetching the necessary Replicate API token.
    """

    def __init__(self, integration: Integration, **kwargs) -> None:
        super().__init__(name="replicate", integration=integration, **kwargs)
        self._replicate_client: replicate.Client | None = None

    @property
    def replicate_client(self) -> replicate.Client:
        if self._replicate_client is None:
            credentials = self.integration.get_credentials()
            logger.info(
                f"ReplicateApp: Credentials from integration: {credentials}"
            )  # Be careful logging credentials
            api_key = (
                credentials.get("api_key")
                or credentials.get("API_KEY")
                or credentials.get("apiKey")
            )
            if not api_key:
                logger.error(
                    f"Integration {type(self.integration).__name__} returned credentials for Replicate in unexpected format or key is missing."
                )
                raise NotAuthorizedError(
                    "Integration returned empty or invalid API key/token for Replicate."
                )
            self._replicate_client = replicate.Client(api_token=api_key)
        return self._replicate_client

    async def run(
        self,
        model_ref: str,
        inputs: dict[str, Any],
        use_file_output: bool | None = True,
    ) -> Any:
        """
        Run a Replicate model and wait for its output. This is a blocking call from the user's perspective.
        If the model output is an iterator, this tool will collect all items into a list.

        Args:
            model_ref: The model identifier string (e.g., "owner/name" or "owner/name:version_id").
            inputs: A dictionary of inputs for the model.
            use_file_output: If True (default), file URLs in output are wrapped in FileOutput objects.

        Returns:
            The model's output. If the model streams output, a list of all streamed items is returned.

        Raises:
            ToolError: If the Replicate API request fails or the model encounters an error.

        Tags:
            run, execute, ai, synchronous, replicate, important
        """
        try:
            logger.info(
                f"Running Replicate model {model_ref} with inputs: {list(inputs.keys())}"
            )
            # Use async_run which handles polling and waiting
            result = await self.replicate_client.async_run(
                ref=model_ref,
                input=inputs,
                use_file_output=use_file_output,
            )
            if isinstance(result, collections.abc.AsyncIterator):
                logger.info(
                    f"Model {model_ref} returned an async iterator, collecting results."
                )
                collected_result = [item async for item in result]
                logger.info(
                    f"Collected {len(collected_result)} items from iterator for {model_ref}."
                )
                return collected_result
            logger.info(f"Model {model_ref} run completed successfully.")
            return result
        except ReplicateModelError as e:
            logger.error(
                f"Model error running Replicate model {model_ref}: {e.prediction.error}",
                exc_info=True,
            )
            raise ToolError(
                f"Model {model_ref} failed with error: {e.prediction.error}"
            ) from e
        except ReplicateAPIError as e:
            logger.error(
                f"API error running Replicate model {model_ref}: {e.detail}",
                exc_info=True,
            )
            raise ToolError(
                f"Failed to run Replicate model {model_ref}: {e.detail}"
            ) from e
        except Exception as e:
            logger.error(
                f"Unexpected error running Replicate model {model_ref}: {e}",
                exc_info=True,
            )
            raise ToolError(
                f"An unexpected error occurred while running model {model_ref}: {e}"
            ) from e

    async def submit_prediction(
        self,
        model_ref: str,
        inputs: dict[str, Any],
        webhook: str | None = None,
        webhook_events_filter: list[str] | None = None,
    ) -> str:
        """
        Submits a prediction request to Replicate for asynchronous processing.

        Args:
            model_ref: The model identifier string (e.g., "owner/name" or "owner/name:version_id").
            inputs: A dictionary of inputs for the model.
            webhook: URL to receive a POST request with prediction updates.
            webhook_events_filter: List of events to trigger webhooks (e.g., ["start", "output", "logs", "completed"]).

        Returns:
            The ID (str) of the created prediction.

        Raises:
            ToolError: If the Replicate API request fails.

        Tags:
            submit, async_job, start, ai, queue, replicate
        """
        try:
            logger.info(
                f"Submitting prediction for Replicate model {model_ref} with inputs: {list(inputs.keys())}"
            )
            # Ensure wait is False for async submission behavior
            # The version parameter in predictions.create can be a model_ref string
            prediction_params = {}
            if webhook:
                prediction_params["webhook"] = webhook
            if webhook_events_filter:
                prediction_params["webhook_events_filter"] = webhook_events_filter

            prediction = await self.replicate_client.predictions.async_create(
                version=model_ref,  # 'version' here means the model/version ref string
                input=inputs,
                wait=False,  # Explicitly set wait to False for non-blocking submission
                **prediction_params,
            )
            logger.info(f"Submitted prediction for {model_ref}, ID: {prediction.id}")
            return prediction.id
        except ReplicateAPIError as e:
            logger.error(
                f"API error submitting prediction for Replicate model {model_ref}: {e.detail}",
                exc_info=True,
            )
            raise ToolError(
                f"Failed to submit prediction for Replicate model {model_ref}: {e.detail}"
            ) from e
        except Exception as e:
            logger.error(
                f"Unexpected error submitting prediction for Replicate model {model_ref}: {e}",
                exc_info=True,
            )
            raise ToolError(
                f"An unexpected error occurred while submitting prediction for {model_ref}: {e}"
            ) from e

    async def get_prediction(self, prediction_id: str) -> Prediction:
        """
        Retrieves the current state and details of a Replicate prediction.

        Args:
            prediction_id: The unique ID of the prediction.

        Returns:
            A Replicate Prediction object containing status, logs, output (if ready), etc.

        Raises:
            ToolError: If the Replicate API request fails.

        Tags:
            status, check, async_job, monitoring, ai, replicate
        """
        try:
            logger.info(f"Getting status for Replicate prediction ID: {prediction_id}")
            prediction = await self.replicate_client.predictions.async_get(
                id=prediction_id
            )
            logger.info(f"Status for prediction {prediction_id}: {prediction.status}")
            return prediction
        except ReplicateAPIError as e:
            logger.error(
                f"API error getting status for Replicate prediction {prediction_id}: {e.detail}",
                exc_info=True,
            )
            raise ToolError(
                f"Failed to get status for Replicate prediction {prediction_id}: {e.detail}"
            ) from e
        except Exception as e:
            logger.error(
                f"Unexpected error getting status for Replicate prediction {prediction_id}: {e}",
                exc_info=True,
            )
            raise ToolError(
                f"An unexpected error occurred while getting status for prediction {prediction_id}: {e}"
            ) from e

    async def fetch_prediction_output(self, prediction_id: str) -> Any:
        """
        Retrieves the output of a completed Replicate prediction.
        If the prediction is not yet complete, this method will wait for it to finish.
        If the model output is an iterator, this tool will collect all items into a list.

        Args:
            prediction_id: The unique ID of the prediction.

        Returns:
            The output of the prediction. If the model streams output, a list of all streamed items is returned.

        Raises:
            ToolError: If the prediction fails, is canceled, or an API error occurs.

        Tags:
            result, fetch_output, async_job, wait, ai, replicate
        """
        try:
            logger.info(f"Fetching output for Replicate prediction ID: {prediction_id}")
            prediction = await self.replicate_client.predictions.async_get(
                id=prediction_id
            )

            if prediction.status not in ["succeeded", "failed", "canceled"]:
                logger.info(
                    f"Prediction {prediction_id} status is {prediction.status}. Waiting for completion..."
                )
                await (
                    prediction.async_wait()
                )  # This updates the prediction object in-place
                logger.info(
                    f"Prediction {prediction_id} finished with status: {prediction.status}"
                )

            if prediction.status == "failed":
                logger.error(f"Prediction {prediction_id} failed: {prediction.error}")
                raise ToolError(
                    f"Prediction {prediction_id} failed: {prediction.error}"
                )
            if prediction.status == "canceled":
                logger.warning(f"Prediction {prediction_id} was canceled.")
                raise ToolError(f"Prediction {prediction_id} was canceled.")
            if prediction.status != "succeeded":
                logger.error(
                    f"Prediction {prediction_id} did not succeed. Status: {prediction.status}"
                )
                raise ToolError(
                    f"Prediction {prediction_id} did not succeed. Status: {prediction.status}"
                )

            output = prediction.output
            logger.info(f"Successfully fetched output for prediction {prediction_id}.")
            return output
        except (
            ReplicateModelError
        ) as e:  # Should be caught by prediction.status == "failed" mostly
            logger.error(
                f"Model error fetching output for Replicate prediction {prediction_id}: {e.prediction.error}",
                exc_info=True,
            )
            raise ToolError(
                f"Prediction {prediction_id} (model) failed: {e.prediction.error}"
            ) from e
        except ReplicateAPIError as e:
            logger.error(
                f"API error fetching output for Replicate prediction {prediction_id}: {e.detail}",
                exc_info=True,
            )
            raise ToolError(
                f"Failed to fetch output for Replicate prediction {prediction_id}: {e.detail}"
            ) from e
        except Exception as e:
            logger.error(
                f"Unexpected error fetching output for Replicate prediction {prediction_id}: {e}",
                exc_info=True,
            )
            raise ToolError(
                f"An unexpected error occurred while fetching output for prediction {prediction_id}: {e}"
            ) from e

    async def cancel_prediction(self, prediction_id: str) -> None:
        """
        Cancels a running or queued Replicate prediction.

        Args:
            prediction_id: The unique ID of the prediction to cancel.

        Returns:
            None.

        Raises:
            ToolError: If the cancellation request fails.

        Tags:
            cancel, async_job, ai, replicate, management
        """
        try:
            logger.info(f"Cancelling Replicate prediction ID: {prediction_id}")
            prediction = await self.replicate_client.predictions.async_get(
                id=prediction_id
            )
            if prediction.status not in ["succeeded", "failed", "canceled"]:
                await prediction.async_cancel()
                logger.info(
                    f"Cancel request sent for prediction {prediction_id}. New status: {prediction.status}"
                )
            else:
                logger.warning(
                    f"Prediction {prediction_id} is already in a terminal state: {prediction.status}. Cannot cancel."
                )
            return None
        except ReplicateAPIError as e:
            logger.error(
                f"API error cancelling Replicate prediction {prediction_id}: {e.detail}",
                exc_info=True,
            )
            raise ToolError(
                f"Failed to cancel Replicate prediction {prediction_id}: {e.detail}"
            ) from e
        except Exception as e:
            logger.error(
                f"Unexpected error cancelling Replicate prediction {prediction_id}: {e}",
                exc_info=True,
            )
            raise ToolError(
                f"An unexpected error occurred while cancelling prediction {prediction_id}: {e}"
            ) from e

    async def upload_file(self, file_path: str) -> str:
        """
        Uploads a local file to Replicate and returns its public URL.
        Replicate uses these URLs for file inputs in models.

        Args:
            file_path: The absolute or relative path to the local file.

        Returns:
            A string containing the public URL of the uploaded file (e.g., "https://replicate.delivery/pbxt/...").

        Raises:
            ToolError: If the file is not found or if the upload operation fails.

        Tags:
            upload, file, storage, replicate, important
        """
        try:
            path_obj = Path(file_path)
            if not path_obj.exists():
                raise FileNotFoundError(f"File not found at path: {file_path}")

            logger.info(f"Uploading file to Replicate: {file_path}")
            # The `async_create` method in `replicate.file.Files` handles opening the file.
            uploaded_file_obj = await self.replicate_client.files.async_create(
                file=path_obj
            )
            file_url = uploaded_file_obj.urls["get"]
            logger.info(
                f"File {file_path} uploaded successfully to Replicate. URL: {file_url}"
            )
            return file_url
        except FileNotFoundError as e:
            logger.error(
                f"File not found for Replicate upload: {file_path}", exc_info=True
            )
            raise ToolError(f"File not found for Replicate upload: {file_path}") from e
        except ReplicateAPIError as e:
            logger.error(
                f"API error uploading file {file_path} to Replicate: {e.detail}",
                exc_info=True,
            )
            raise ToolError(
                f"Failed to upload file {file_path} to Replicate: {e.detail}"
            ) from e
        except Exception as e:
            logger.error(
                f"Unexpected error uploading file {file_path} to Replicate: {e}",
                exc_info=True,
            )
            raise ToolError(
                f"An unexpected error occurred while uploading file {file_path} to Replicate: {e}"
            ) from e

    async def generate_image(
        self,
        prompt: str,
        model_ref: str = "stability-ai/sdxl:c221b2b8ef527988fb59bf24a8b97c4561f1c671f73bd389f866bfb27c061316",
        negative_prompt: str | None = None,
        width: int | None = 1024,
        height: int | None = 1024,
        num_outputs: int | None = 1,
        seed: int | None = None,
        extra_arguments: dict[str, Any] | None = None,
    ) -> Any:
        """
        Generates images using a specified Replicate model (defaults to SDXL).
        This is a convenience wrapper around the `run` tool.

        Args:
            prompt: The text prompt for image generation.
            model_ref: The Replicate model identifier string.
                       Defaults to "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc".
            negative_prompt: Optional text to specify what not to include.
            width: Width of the generated image(s).
            height: Height of the generated image(s).
            num_outputs: Number of images to generate.
            seed: Optional random seed for reproducibility.
            extra_arguments: Dictionary of additional arguments specific to the model.

        Returns:
            The output from the image generation model, typically a list of image URLs.

        Raises:
            ToolError: If the image generation fails.

        Tags:
            generate, image, ai, replicate, sdxl, important, default
        """
        logger.info(
            f"Generating image with Replicate model {model_ref} for prompt: '{prompt[:30]}...'"
        )
        inputs = {
            "prompt": prompt,
        }
        if negative_prompt is not None:
            inputs["negative_prompt"] = negative_prompt
        if width is not None:
            inputs["width"] = width
        if height is not None:
            inputs["height"] = height
        if num_outputs is not None:
            inputs["num_outputs"] = num_outputs
        if seed is not None:
            inputs["seed"] = seed

        if extra_arguments:
            inputs.update(extra_arguments)
            logger.debug(
                f"Merged extra_arguments for image generation. Final input keys: {list(inputs.keys())}"
            )

        try:
            # Use the run method which handles waiting and iterator collection
            result = await self.run(model_ref=model_ref, inputs=inputs)
            logger.info(f"Image generation successful for model {model_ref}.")
            for index, item in enumerate(result):
                with open(f"output_{index}.png", "wb") as file:
                    file.write(item.read())
            return result
        except Exception as e:  # run method already wraps in ToolError
            logger.error(
                f"Error during generate_image call for model {model_ref}: {e}",
                exc_info=True,
            )
            # Re-raise if it's already ToolError, or wrap if it's something unexpected from this level
            if isinstance(e, ToolError):
                raise
            raise ToolError(
                f"Image generation failed for model {model_ref}: {e}"
            ) from e

    def list_tools(self) -> list[callable]:
        return [
            self.run,
            self.submit_prediction,
            self.get_prediction,
            self.fetch_prediction_output,
            self.cancel_prediction,
            self.upload_file,
            self.generate_image,
        ]
