from typing import Any, Literal
from fal_client import AsyncClient, AsyncRequestHandle, Status
from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration

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

    async def get_fal_client(self) -> AsyncClient:
        """
        A cached property that lazily initializes an `AsyncClient` instance. It retrieves the API key from the configured integration, providing a single, centralized authentication point for all methods that interact with the Fal AI API. Raises `NotAuthorizedError` if credentials are not found.
        """
        if self._fal_client is None:
            credentials = await self.integration.get_credentials_async()
            logger.info(f"Credentials: {credentials}")
            api_key = credentials.get("api_key") or credentials.get("API_KEY") or credentials.get("apiKey")
            if not api_key:
                logger.error(f"Integration {type(self.integration).__name__} returned credentials in unexpected format.")
                raise NotAuthorizedError("Integration returned empty or invalid API key.")
            self._fal_client = AsyncClient(key=api_key)
        return self._fal_client

    async def generate_image(
        self,
        prompt: str,
        model: Literal[
            "fal-ai/flux/dev", "fal-ai/recraft-v3", "fal-ai/stable-diffusion-v35-large"
        ] = "fal-ai/flux/dev",
        image_size: Literal[
            "square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"
        ]
        | None = "landscape_4_3",
        num_images: int | None = 1,
        seed: int | None = None,
        safety_tolerance: str | None = None,
        extra_arguments: dict[str, Any] | None = None,
    ) -> Any:
        """
        Generates an image from a text prompt using specified Fal AI models.
        This tool supports state-of-the-art models like Flux, Recraft V3, and Stable Diffusion 3.5.

        Args:
            prompt: The text description of the image to generate.
            model: The model to use for generation. Options:
                   - 'fal-ai/flux/dev': High-quality, 12B param flow transformer.
                   - 'fal-ai/recraft-v3': SOTA model, great for text, vector art, and brand styles.
                   - 'fal-ai/stable-diffusion-v35-large': MMDiT model, excellent typography and complex prompts.
                   Defaults to 'fal-ai/flux/dev'.
            image_size: The size/aspect ratio of the generated image. Common values: 'landscape_4_3', 'square_hd'.
            num_images: Number of images to generate (default: 1).
            seed: Optional random seed for reproducibility.
            safety_tolerance: Optional safety filter level (if supported by model).
            extra_arguments: Additional model-specific parameters to pass in the request.

        Returns:
            A dictionary containing the generated image URLs and metadata.

        Tags:
            generate, image, text-to-image, ai, flux, recraft, stable-diffusion, important
        """
        arguments = {"prompt": prompt}

        # Common arguments that most models support
        if image_size:
            arguments["image_size"] = image_size
        if num_images:
            arguments["num_images"] = num_images
        if seed is not None:
            arguments["seed"] = seed
        if safety_tolerance:
            arguments["safety_tolerance"] = safety_tolerance

        if extra_arguments:
            arguments.update(extra_arguments)
            logger.debug(f"Merged extra_arguments. Final arguments: {arguments}")

        try:
            client = await self.get_fal_client()
            # The run method is equivalent to subscribe() in the JS SDK - it submits and waits for the result.
            result = await client.run(application=model, arguments=arguments)
            return result
        except Exception as e:
            logger.error(f"Error generating image with model {model}: {e}", exc_info=True)
            raise ToolError(f"Failed to generate image with {model}: {e}") from e

    async def submit_video_generation(
        self,
        image_url: str,
        prompt: str = "",
        model: Literal[
            "fal-ai/minimax-video/image-to-video",
            "fal-ai/luma-dream-machine/image-to-video",
            "fal-ai/kling-video/v1/standard/image-to-video",
        ] = "fal-ai/minimax-video/image-to-video",
        duration: Literal["5", "10"] | None = None,
        aspect_ratio: Literal["16:9", "9:16", "1:1"] | None = None,
        extra_arguments: dict[str, Any] | None = None,
    ) -> str:
        """
        Submits a video generation task using Fal AI models and returns a request ID.
        This is an asynchronous operation. Use `get_generation_status` and `get_generation_result` with the returned ID.

        Args:
            image_url: URL of the input image.
            prompt: Text prompt to guide the video generation.
            model: The video generation model to use.
            duration: Duration of the video in seconds (supported by some models like Kling).
            aspect_ratio: Aspect ratio of the generated video (supported by some models like Kling).
            extra_arguments: Additional model-specific parameters.

        Returns:
            The request ID (str) for the submitted task.

        Tags:
            submit, video, async, ai, minimax, luma, kling, important
        """
        arguments = {"image_url": image_url}
        if prompt:
            arguments["prompt"] = prompt
        
        if duration:
            arguments["duration"] = duration
        if aspect_ratio:
            arguments["aspect_ratio"] = aspect_ratio
            
        if extra_arguments:
            arguments.update(extra_arguments)
            logger.debug(f"Merged extra_arguments for video generation. Final arguments: {arguments}")
            
        try:
            client = await self.get_fal_client()
            handle = await client.submit(application=model, arguments=arguments)
            return handle.request_id
        except Exception as e:
            logger.error(f"Error submitting video generation with model {model}: {e}", exc_info=True)
            raise ToolError(f"Failed to submit video generation with {model}: {e}") from e

    async def get_generation_status(
        self,
        request_id: str,
        model: Literal[
            "fal-ai/minimax-video/image-to-video",
            "fal-ai/luma-dream-machine/image-to-video",
            "fal-ai/kling-video/v1/standard/image-to-video",
        ] = "fal-ai/minimax-video/image-to-video",
        with_logs: bool = False,
    ) -> Status:
        """
        Checks the status of a video generation task.

        Args:
            request_id: The ID of the request to check.
            model: The model used for the request (must match the submission).
            with_logs: Whether to include logs in the status.

        Returns:
            A Status object (Queued, InProgress, Completed, or Failed).
        
        Tags:
            check, status, video, async, important
        """
        try:
            client = await self.get_fal_client()
            handle = client.get_handle(application=model, request_id=request_id)
            return await handle.status(with_logs=with_logs)
        except Exception as e:
            logger.error(f"Error getting status for request {request_id}: {e}", exc_info=True)
            raise ToolError(f"Failed to get status for {request_id}: {e}") from e

    async def get_generation_result(
        self,
        request_id: str,
        model: Literal[
            "fal-ai/minimax-video/image-to-video",
            "fal-ai/luma-dream-machine/image-to-video",
            "fal-ai/kling-video/v1/standard/image-to-video",
            "fal-ai/kling-video/v2.6/pro/image-to-video",
        ] = "fal-ai/minimax-video/image-to-video",
    ) -> Any:
        """
        Retrieves the result of a completed video generation task.
        This method will block until the task is complete if it is not already.

        Args:
            request_id: The ID of the request.
            model: The model used for the request.

        Returns:
            The final result of the generation (video URL and metadata).

        Tags:
            result, get, video, async, important
        """
        try:
            client = await self.get_fal_client()
            handle = client.get_handle(application=model, request_id=request_id)
            return await handle.get()
        except Exception as e:
            logger.error(f"Error getting result for request {request_id}: {e}", exc_info=True)
            raise ToolError(f"Failed to get result for {request_id}: {e}") from e

    async def transcribe_audio(
        self,
        audio_url: str,
        model: Literal["fal-ai/whisper"] = "fal-ai/whisper",
        extra_arguments: dict[str, Any] | None = None,
    ) -> Any:
        """
        Converts speech to text from an audio file URL using Fal AI models.

        Args:
            audio_url: URL of the audio file to transcribe.
            model: The speech-to-text model to use. Options:
                   - 'fal-ai/whisper': Standard Whisper model.
                   Defaults to 'fal-ai/whisper'.
            extra_arguments: Additional model-specific parameters.

        Returns:
            A dictionary containing the transcription text and metadata.

        Tags:
            transcribe, audio, speech-to-text, ai, whisper  
        """
        arguments = {"audio_url": audio_url}

        if extra_arguments:
            arguments.update(extra_arguments)
            logger.debug(f"Merged extra_arguments for transcription. Final arguments: {arguments}")

        try:
            client = await self.get_fal_client()
            result = await client.run(application=model, arguments=arguments)
            return result
        except Exception as e:
            logger.error(f"Error transcribing audio with model {model}: {e}", exc_info=True)
            raise ToolError(f"Failed to transcribe audio with {model}: {e}") from e

    async def submit_start_end_video_generation(
        self,
        prompt: str,
        start_image_url: str,
        end_image_url: str,
        model: Literal[
            "fal-ai/kling-video/v2.6/pro/image-to-video",
        ] = "fal-ai/kling-video/v2.6/pro/image-to-video",
        duration: Literal["5", "10"] | None = None,
        extra_arguments: dict[str, Any] | None = None,
    ) -> str:
        """
        Submits a video generation task using start and end images.

        Args:
            prompt: Text prompt to guide the video generation.
            start_image_url: URL of the starting image.
            end_image_url: URL of the ending image.
            model: The video generation model to use. Defaults to 'fal-ai/kling-video/v2.6/pro/image-to-video'.
            duration: Duration of the video in seconds.
            extra_arguments: Additional model-specific parameters.

        Returns:
            The request ID (str) for the submitted task.

        Tags:
            submit, video, async, ai, minimax, luma, kling, important
        """
        arguments = {
            "prompt": prompt,
            "start_image_url": start_image_url,
            "end_image_url": end_image_url,
            "generate_audio": False,
        }

        if duration:
            arguments["duration"] = duration

        if extra_arguments:
            arguments.update(extra_arguments)
            arguments["generate_audio"] = False

        try:
            client = await self.get_fal_client()
            handle = await client.submit(application=model, arguments=arguments)
            return handle.request_id
        except Exception as e:
            logger.error(f"Error submitting video generation with model {model}: {e}", exc_info=True)
            raise ToolError(f"Failed to submit video generation with {model}: {e}") from e

    def list_tools(self):
        return [
            self.generate_image,
            self.submit_video_generation,
            self.submit_start_end_video_generation,
            self.get_generation_status,
            self.get_generation_result,
            self.transcribe_audio
        ]
