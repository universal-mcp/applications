from pathlib import Path
from typing import Any, Literal

from fal_client import AsyncClient, AsyncRequestHandle, Status
from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration

Priority = Literal["normal", "low"]


class FalaiApp(APIApplication):
    """
    Application for interacting with the Fal AI platform.

    Provides tools to run, submit, check status, retrieve results, cancel jobs,
    upload files to the Fal CDN, and a specialized tool for generating images.

    Authentication is handled by the configured Integration provided by the
    Universal MCP server, fetching the necessary API key.
    """

    def __init__(self, integration: Integration, **kwargs) -> None:
        super().__init__(name="falai", integration=integration, **kwargs)
        self._fal_client = None

    @property
    def fal_client(self) -> AsyncClient:
        """
        A cached property that lazily initializes an `AsyncClient` instance. It retrieves the API key from the configured integration, providing a single, centralized authentication point for all methods that interact with the Fal AI API. Raises `NotAuthorizedError` if credentials are not found.
        """
        if self._fal_client is None:
            credentials = self.integration.get_credentials()
            logger.info(f"Credentials: {credentials}")
            api_key = (
                credentials.get("api_key")
                or credentials.get("API_KEY")
                or credentials.get("apiKey")
            )
            if not api_key:
                logger.error(
                    f"Integration {type(self.integration).__name__} returned credentials in unexpected format."
                )
                raise NotAuthorizedError(
                    "Integration returned empty or invalid API key."
                )
            self._fal_client = AsyncClient(key=api_key)
        return self._fal_client

    async def run(
        self,
        arguments: Any,
        application: str = "fal-ai/flux/dev",
        path: str = "",
        timeout: float | None = None,
        hint: str | None = None,
    ) -> Any:
        """
        Executes a Fal AI application synchronously, waiting for completion and returning the result directly. This method is suited for short-running tasks, unlike `submit` which queues a job for asynchronous processing and returns a request ID instead of the final output.

        Args:
            arguments: A dictionary of arguments for the application
            application: The name or ID of the Fal application (defaults to 'fal-ai/flux/dev')
            path: Optional subpath for the application endpoint
            timeout: Optional timeout in seconds for the request
            hint: Optional hint for runner selection

        Returns:
            The result of the application execution as a Python object (converted from JSON response)

        Raises:
            ToolError: Raised when the Fal API request fails, wrapping the original exception

        Tags:
            run, execute, ai, synchronous, fal, important
        """
        try:
            result = await self.fal_client.run(
                application=application,
                arguments=arguments,
                path=path,
                timeout=timeout,
                hint=hint,
            )
            return result
        except Exception as e:
            logger.error(
                f"Error running Fal application {application}: {e}", exc_info=True
            )
            raise ToolError(f"Failed to run Fal application {application}: {e}") from e

    async def submit(
        self,
        arguments: Any,
        application: str = "fal-ai/flux/dev",
        path: str = "",
        hint: str | None = None,
        webhook_url: str | None = None,
        priority: Priority | None = None,
    ) -> str:
        """
        Submits a job to the Fal AI queue for asynchronous processing, immediately returning a request ID. This contrasts with the `run` method, which waits for completion. The returned ID is used by `check_status`, `get_result`, and `cancel` to manage the job's lifecycle.

        Args:
            arguments: A dictionary of arguments for the application
            application: The name or ID of the Fal application, defaulting to 'fal-ai/flux/dev'
            path: Optional subpath for the application endpoint
            hint: Optional hint for runner selection
            webhook_url: Optional URL to receive a webhook when the request completes
            priority: Optional queue priority ('normal' or 'low')

        Returns:
            The request ID (str) of the submitted asynchronous job

        Raises:
            ToolError: Raised when the Fal API request fails, wrapping the original exception

        Tags:
            submit, async_job, start, ai, queue
        """
        try:
            handle: AsyncRequestHandle = await self.fal_client.submit(
                application=application,
                arguments=arguments,
                path=path,
                hint=hint,
                webhook_url=webhook_url,
                priority=priority,
            )
            request_id = handle.request_id
            return request_id
        except Exception as e:
            logger.error(
                f"Error submitting Fal application {application}: {e}", exc_info=True
            )
            raise ToolError(
                f"Failed to submit Fal application {application}: {e}"
            ) from e

    async def check_status(
        self,
        request_id: str,
        application: str = "fal-ai/flux/dev",
        with_logs: bool = False,
    ) -> Status:
        """
        Checks the execution state (e.g., Queued, InProgress) of an asynchronous Fal AI job using its request ID. It provides a non-blocking way to monitor jobs initiated via `submit` without fetching the final `result`, and can optionally include logs.

        Args:
            request_id: The unique identifier of the submitted request, obtained from a previous submit operation
            application: The name or ID of the Fal application (defaults to 'fal-ai/flux/dev')
            with_logs: Boolean flag to include execution logs in the status response (defaults to False)

        Returns:
            A Status object containing the current state of the request (Queued, InProgress, or Completed)

        Raises:
            ToolError: Raised when the Fal API request fails or when the provided request ID is invalid

        Tags:
            status, check, async_job, monitoring, ai
        """
        try:
            handle = self.fal_client.get_handle(
                application=application, request_id=request_id
            )
            status = await handle.status(with_logs=with_logs)
            return status
        except Exception as e:
            logger.error(
                f"Error getting status for Fal request_id {request_id}: {e}",
                exc_info=True,
            )
            raise ToolError(
                f"Failed to get status for Fal request_id {request_id}: {e}"
            ) from e

    async def get_result(
        self, request_id: str, application: str = "fal-ai/flux/dev"
    ) -> Any:
        """
        Retrieves the final result of an asynchronous job, identified by its `request_id`. This function waits for the job, initiated via `submit`, to complete. Unlike the non-blocking `check_status`, this method blocks execution to fetch and return the job's actual output upon completion.

        Args:
            request_id: The unique identifier of the submitted request
            application: The name or ID of the Fal application (defaults to 'fal-ai/flux/dev')

        Returns:
            The result of the application execution, converted from JSON response to Python data structures (dict/list)

        Raises:
            ToolError: When the Fal API request fails or the request does not complete successfully

        Tags:
            result, async-job, status, wait, ai
        """
        try:
            handle = self.fal_client.get_handle(
                application=application, request_id=request_id
            )
            result = await handle.get()
            return result
        except Exception as e:
            logger.error(
                f"Error getting result for Fal request_id {request_id}: {e}",
                exc_info=True,
            )
            raise ToolError(
                f"Failed to get result for Fal request_id {request_id}: {e}"
            ) from e

    async def cancel(
        self, request_id: str, application: str = "fal-ai/flux/dev"
    ) -> None:
        """
        Asynchronously cancels a running or queued Fal AI job using its `request_id`. This function complements the `submit` method, providing a way to terminate asynchronous tasks before completion. It raises a `ToolError` if the cancellation request fails.

        Args:
            request_id: The unique identifier of the submitted Fal AI request to cancel
            application: The name or ID of the Fal application (defaults to 'fal-ai/flux/dev')

        Returns:
            None. The function doesn't return any value.

        Raises:
            ToolError: Raised when the cancellation request fails due to API errors or if the request cannot be cancelled

        Tags:
            cancel, async_job, ai, fal, management
        """
        try:
            handle = self.fal_client.get_handle(
                application=application, request_id=request_id
            )
            await handle.cancel()
            return None
        except Exception as e:
            logger.error(
                f"Error cancelling Fal request_id {request_id}: {e}", exc_info=True
            )
            raise ToolError(f"Failed to cancel Fal request_id {request_id}: {e}") from e

    async def upload_file(self, path: str) -> str:
        """
        Asynchronously uploads a local file to the Fal Content Delivery Network (CDN), returning a public URL. This URL makes the file accessible for use as input in other Fal AI job execution methods like `run` or `submit`. A `ToolError` is raised if the upload fails.

        Args:
            path: The absolute or relative path to the local file

        Returns:
            A string containing the public URL of the uploaded file on the CDN

        Raises:
            ToolError: If the file is not found or if the upload operation fails

        Tags:
            upload, file, cdn, storage, async, important
        """
        try:
            file_url = await self.fal_client.upload_file(Path(path))
            return file_url
        except FileNotFoundError as e:
            logger.error(f"File not found for upload: {path}", exc_info=True)
            raise ToolError(f"File not found: {path}") from e
        except Exception as e:
            logger.error(f"Error uploading file {path} to Fal CDN: {e}", exc_info=True)
            raise ToolError(f"Failed to upload file {path}: {e}") from e

    async def run_image_generation(
        self,
        prompt: str,
        seed: int | None = 6252023,
        image_size: str | None = "landscape_4_3",
        num_images: int | None = 1,
        extra_arguments: dict[str, Any] | None = None,
        path: str = "",
        timeout: float | None = None,
        hint: str | None = None,
    ) -> Any:
        """
        A specialized wrapper for the `run` method that synchronously generates images using the 'fal-ai/flux/dev' model. It simplifies image creation with common parameters like `prompt` and `seed`, waits for the task to complete, and directly returns the result containing image URLs and metadata.

        Args:
            prompt: The text prompt used to guide the image generation
            seed: Random seed for reproducible image generation (default: 6252023)
            image_size: Dimensions of the generated image (default: 'landscape_4_3')
            num_images: Number of images to generate in one request (default: 1)
            extra_arguments: Additional arguments dictionary to pass to the application, can override defaults
            path: Subpath for the application endpoint (rarely used)
            timeout: Maximum time in seconds to wait for the request to complete
            hint: Hint string for runner selection

        Returns:
            A dictionary containing the generated image URLs and related metadata

        Raises:
            ToolError: When the image generation request fails or encounters an error

        Tags:
            generate, image, ai, async, important, flux, customizable, default
        """
        application = "fal-ai/flux/dev"
        arguments = {
            "prompt": prompt,
            "seed": seed,
            "image_size": image_size,
            "num_images": num_images,
        }
        if extra_arguments:
            arguments.update(extra_arguments)
            logger.debug(f"Merged extra_arguments. Final arguments: {arguments}")
        try:
            result = await self.run(
                application=application,
                arguments=arguments,
                path=path,
                timeout=timeout,
                hint=hint,
            )
            return result
        except Exception:
            raise

    def list_tools(self) -> list[callable]:
        return [
            self.run,
            self.submit,
            self.check_status,
            self.get_result,
            self.cancel,
            self.upload_file,
            self.run_image_generation,
        ]
