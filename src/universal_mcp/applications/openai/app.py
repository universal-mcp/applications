import base64
from typing import Any, Literal

from openai import NOT_GIVEN, AsyncOpenAI, OpenAIError
from openai._types import FileTypes as OpenAiFileTypes
from openai.types import FilePurpose as OpenAiFilePurpose
from openai.types.audio import (
    Transcription,
    TranscriptionVerbose,
    Translation,
    TranslationVerbose,
)
from openai.types.audio.speech_model import SpeechModel as OpenAiSpeechModel
from openai.types.audio_model import AudioModel as OpenAiAudioModel
from openai.types.chat import ChatCompletionMessageParam
from openai.types.file_object import FileObject
from openai.types.image_model import ImageModel as OpenAiImageModel
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class OpenaiApp(APIApplication):
    """
    Application for interacting with the OpenAI API (api.openai.com)
    to generate chat completions, manage files, and create images.
    Requires an OpenAI API key configured via integration.
    Optionally, organization ID and project ID can also be configured.
    """

    def __init__(self, integration: Integration | None = None) -> None:
        super().__init__(name="openai", integration=integration)

    async def _get_client(self) -> AsyncOpenAI:
        """Initializes and returns the AsyncOpenAI client."""
        if not self.integration:
            raise ValueError("Integration not provided for OpenaiApp.")

        creds = self.integration.get_credentials()
        api_key = creds.get("api_key")
        organization = creds.get("organization")
        project = creds.get("project")

        return AsyncOpenAI(
            api_key=api_key,
            organization=organization,
            project=project,
        )

    async def create_chat_completion(
        self,
        messages: list[ChatCompletionMessageParam],
        model: str = "gpt-4o",  # Default model set to gpt-4o
        stream: bool = False,
        temperature: float | None = None,
        max_tokens: int | None = None,
        top_p: float | None = None,
        frequency_penalty: float | None = None,
        presence_penalty: float | None = None,
        stop: str | None | list[str] = None,
        user: str | None = None,
        # Add other common parameters as needed, or rely on
    ) -> dict[str, Any] | str:
        """
        Creates a model response for the given chat conversation.

        Args:
            messages: A list of messages comprising the conversation so far.
            model: ID of the model to use. Defaults to "gpt-4o".
                   Other examples include "gpt-4-turbo", "gpt-3.5-turbo",
                   "gpt-4o-mini", etc.
                   Ensure the model ID is valid for the OpenAI API.
            stream: If True, the response will be streamed and internally aggregated
                    into a single response object. Usage data will not be available in this mode.
                    If False (default), a single, complete response is requested.
            temperature: Sampling temperature to use, between 0 and 2.
            max_tokens: The maximum number of tokens to generate in the chat completion.
            top_p: An alternative to sampling with temperature, called nucleus sampling.
            frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency.
            presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far.
            stop: Up to 4 sequences where the API will stop generating further tokens.
            user: A unique identifier representing your end-user.

        Returns:
            A dictionary containing the chat completion response on success,
            or a string containing an error message on failure.
            If stream=True, usage data in the response will be None.

        Tags:
            chat, llm, important
        """
        try:
            client = await self._get_client()
            common_params = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "top_p": top_p,
                "frequency_penalty": frequency_penalty,
                "presence_penalty": presence_penalty,
                "stop": stop,
                "user": user,
            }
            common_params = {k: v for k, v in common_params.items() if v is not None}

            if not stream:
                response = await client.chat.completions.create(
                    stream=False, **common_params
                )
                return response.model_dump()
            else:
                stream_response = await client.chat.completions.create(
                    stream=True, **common_params
                )

                final_content_parts: list[str] = []
                final_role: str = "assistant"
                first_chunk_data: dict[str, Any] = {}
                finish_reason: str | None = None

                async for chunk in stream_response:
                    if not first_chunk_data and chunk.id:
                        first_chunk_data = {
                            "id": chunk.id,
                            "created": chunk.created,
                            "model": chunk.model,
                            "system_fingerprint": chunk.system_fingerprint,
                        }

                    if chunk.choices:
                        choice = chunk.choices[0]
                        if choice.delta:
                            if choice.delta.content:
                                final_content_parts.append(choice.delta.content)
                            if choice.delta.role:
                                final_role = choice.delta.role
                        if choice.finish_reason:
                            finish_reason = choice.finish_reason

                aggregated_choice = {
                    "message": {
                        "role": final_role,
                        "content": "".join(final_content_parts),
                    },
                    "finish_reason": finish_reason,
                    "index": 0,
                }

                response_dict = {
                    **first_chunk_data,
                    "object": "chat.completion",
                    "choices": [aggregated_choice],
                    "usage": None,
                }
                return response_dict

        except OpenAIError as e:
            return f"OpenAI API error creating chat completion for model {model}: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error creating chat completion for model {model}: {type(e).__name__} - {e}"

    async def upload_file(
        self, file: OpenAiFileTypes, purpose: OpenAiFilePurpose
    ) -> dict[str, Any] | str:
        """
        Upload a file that can be used across various OpenAI API endpoints.

        Args:
            file: The File object (not file name) or path to be uploaded.
                  Can be bytes, a PathLike object, or a file-like object.
            purpose: The intended purpose of the uploaded file (e.g., 'fine-tune', 'assistants').

        Returns:
            A dictionary containing the file object details on success,
            or a string containing an error message on failure.

        Tags:
            files, upload, storage
        """
        try:
            client = await self._get_client()
            response: FileObject = await client.files.create(file=file, purpose=purpose)
            return response.model_dump()
        except OpenAIError as e:
            return f"OpenAI API error uploading file: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error uploading file: {type(e).__name__} - {e}"

    async def list_files(
        self,
        purpose: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        order: Literal["asc", "desc"] | None = None,
    ) -> dict[str, Any] | str:
        """
        Lists the files that have been uploaded to your OpenAI account.

        Args:
            purpose: Only return files with the given purpose.
            limit: A limit on the number of objects to be returned.
            after: A cursor for use in pagination.
            order: Sort order by the `created_at` timestamp.

        Returns:
            A dictionary representing a page of file objects on success,
            or a string containing an error message on failure.

        Tags:
            files, list, storage
        """
        try:
            client = await self._get_client()
            params = {}
            if purpose:
                params["purpose"] = purpose
            if limit:
                params["limit"] = limit
            if after:
                params["after"] = after
            if order:
                params["order"] = order

            response_page = await client.files.list(**params)
            return response_page.model_dump()
        except OpenAIError as e:
            return f"OpenAI API error listing files: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error listing files: {type(e).__name__} - {e}"

    async def retrieve_file(self, file_id: str) -> dict[str, Any] | str:
        """
        Retrieves information about a specific file.

        Args:
            file_id: The ID of the file to retrieve.

        Returns:
            A dictionary containing the file object details on success,
            or a string containing an error message on failure.

        Tags:
            files, retrieve, storage
        """
        try:
            client = await self._get_client()
            response: FileObject = await client.files.retrieve(file_id=file_id)
            return response.model_dump()
        except OpenAIError as e:
            return (
                f"OpenAI API error retrieving file {file_id}: {type(e).__name__} - {e}"
            )
        except Exception as e:
            return f"Error retrieving file {file_id}: {type(e).__name__} - {e}"

    async def delete_file(self, file_id: str) -> dict[str, Any] | str:
        """
        Deletes a file.

        Args:
            file_id: The ID of the file to delete.

        Returns:
            A dictionary containing the deletion status on success,
            or a string containing an error message on failure.

        Tags:
            files, delete, storage
        """
        try:
            client = await self._get_client()
            response = await client.files.delete(file_id=file_id)
            return response.model_dump()
        except OpenAIError as e:
            return f"OpenAI API error deleting file {file_id}: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error deleting file {file_id}: {type(e).__name__} - {e}"

    async def retrieve_file_content(self, file_id: str) -> dict[str, Any] | str:
        """
        Retrieves the content of the specified file.
        Returns text content directly, or base64 encoded content in a dictionary for binary files.

        Args:
            file_id: The ID of the file whose content to retrieve.

        Returns:
            The file content as a string if text, a dictionary with base64 encoded
            content if binary, or an error message string on failure.

        Tags:
            files, content, download
        """
        try:
            client = await self._get_client()
            api_response = await client.files.content(file_id=file_id)

            http_response_headers = api_response.response.headers
            content_type = http_response_headers.get("Content-Type", "").lower()

            if (
                "text" in content_type
                or "json" in content_type
                or "xml" in content_type
                or "javascript" in content_type
                or "csv" in content_type
            ):
                return api_response.text  # Decoded text
            else:
                binary_content = api_response.content
                return {
                    "file_id": file_id,
                    "content_type": content_type,
                    "content_base64": base64.b64encode(binary_content).decode(),
                }
        except UnicodeDecodeError:
            client = await self._get_client()
            api_response = await client.files.content(file_id=file_id)
            binary_content = api_response.content
            content_type = api_response.response.headers.get("Content-Type", "").lower()
            return {
                "file_id": file_id,
                "content_type": content_type,
                "content_base64": base64.b64encode(binary_content).decode(),
                "warning": "Content could not be decoded as text, returned as base64.",
            }
        except OpenAIError as e:
            return f"OpenAI API error retrieving content for file {file_id}: {type(e).__name__} - {e}"
        except Exception as e:
            return (
                f"Error retrieving content for file {file_id}: {type(e).__name__} - {e}"
            )

    # --- Images Methods ---
    async def generate_image(
        self,
        prompt: str,
        model: str
        | OpenAiImageModel
        | None = "dall-e-3",  # Default model set to dall-e-3
        n: int | None = None,  # 1-10 for dall-e-2, 1 for dall-e-3
        quality: Literal["standard", "hd"] | None = None,  # For dall-e-3
        response_format: Literal["url", "b64_json"] | None = None,
        size: Literal["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"]
        | None = None,
        style: Literal["vivid", "natural"] | None = None,  # For dall-e-3
        user: str | None = None,
    ) -> dict[str, Any] | str:
        """
        Creates an image given a prompt.

        Args:
            prompt: A text description of the desired image(s).
            model: The model to use for image generation. Defaults to "dall-e-3".
                   The other primary option is "dall-e-2".
                   Ensure the model ID is valid for the OpenAI API.
            n: The number of images to generate. For "dall-e-3", only n=1 is supported.
               For "dall-e-2", n can be between 1 and 10.
               If model is "dall-e-3" and n is not 1, it may result in an API error.
            quality: The quality of the image ("standard" or "hd"). Only for "dall-e-3".
            response_format: The format in which the generated images are returned ("url" or "b64_json").
                             Defaults to "url" if not specified.
            size: The size of the generated images.
                  For "dall-e-2": "256x256", "512x512", or "1024x1024".
                  For "dall-e-3": "1024x1024", "1792x1024", or "1024x1792".
            style: The style of the generated images ("vivid" or "natural"). Only for "dall-e-3".
            user: A unique identifier representing your end-user.

        Returns:
            A dictionary containing the image generation response on success,
            or a string containing an error message on failure.

        Tags:
            images, generate, dalle, important
        """
        try:
            client = await self._get_client()

            effective_model = (
                model if model is not None else "dall-e-3"
            )  # Ensure effective_model is not None

            effective_params = {
                "prompt": prompt,
                "model": effective_model,
                "n": n,
                "quality": quality,
                "response_format": response_format,
                "size": size,
                "style": style,
                "user": user,
            }

            effective_params = {
                k: v for k, v in effective_params.items() if v is not None
            }

            response = await client.images.generate(**effective_params)
            return response.model_dump()
        except OpenAIError as e:
            return f"OpenAI API error generating image with model {model}: {type(e).__name__} - {e}"
        except Exception as e:
            return (
                f"Error generating image with model {model}: {type(e).__name__} - {e}"
            )

    async def create_image_edit(
        self,
        image: OpenAiFileTypes,
        prompt: str,
        mask: OpenAiFileTypes | None = None,
        model: str | OpenAiImageModel | None = "dall-e-2",
        n: int | None = None,
        response_format: Literal["url", "b64_json"] | None = None,
        size: Literal["256x256", "512x512", "1024x1024"] | None = None,
        user: str | None = None,
    ) -> dict[str, Any] | str:
        """
        Creates an edited or extended image given an original image and a prompt.

        Args:
            image: The image to edit. Must be a valid PNG file, less than 4MB, and square.
            prompt: A text description of the desired image(s).
            mask: An additional image whose fully transparent areas indicate where `image` should be edited.
            model: The model to use. Defaults to "dall-e-2", which is currently the only
                   model supported for image edits by the OpenAI API.
            n: The number of images to generate. Must be between 1 and 10.
            response_format: The format of the returned images ("url" or "b64_json"). Defaults to "url".
            size: The size of the generated images. Must be one of "256x256", "512x512", or "1024x1024".
            user: A unique identifier representing your end-user.

        Returns:
            A dictionary containing the image edit response on success,
            or a string containing an error message on failure.

        Tags:
            images, edit, dalle
        """
        try:
            client = await self._get_client()
            effective_model = model if model is not None else "dall-e-2"

            params = {
                "image": image,
                "prompt": prompt,
                "mask": mask,
                "model": effective_model,
                "n": n,
                "response_format": response_format,
                "size": size,
                "user": user,
            }
            params = {k: v for k, v in params.items() if v is not None}

            response = await client.images.edit(**params)
            return response.model_dump()
        except OpenAIError as e:
            return f"OpenAI API error creating image edit with model {effective_model}: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error creating image edit with model {effective_model}: {type(e).__name__} - {e}"

    async def create_image_variation(
        self,
        image: OpenAiFileTypes,
        model: str | OpenAiImageModel | None = "dall-e-2",
        n: int | None = None,
        response_format: Literal["url", "b64_json"] | None = None,
        size: Literal["256x256", "512x512", "1024x1024"] | None = None,
        user: str | None = None,
    ) -> dict[str, Any] | str:
        """
        Creates a variation of a given image.

        Args:
            image: The image to use as the basis for the variation(s). Must be a valid PNG file.
            model: The model to use. Defaults to "dall-e-2", which is currently the only
                   model supported for image variations by the OpenAI API.
            n: The number of images to generate. Must be between 1 and 10.
            response_format: The format of the returned images ("url" or "b64_json"). Defaults to "url".
            size: The size of the generated images. Must be one of "256x256", "512x512", or "1024x1024".
            user: A unique identifier representing your end-user.

        Returns:
            A dictionary containing the image variation response on success,
            or a string containing an error message on failure.

        Tags:
            images, variation, dalle
        """
        try:
            client = await self._get_client()
            effective_model = model if model is not None else "dall-e-2"

            params = {
                "image": image,
                "model": effective_model,
                "n": n,
                "response_format": response_format,
                "size": size,
                "user": user,
            }
            params = {k: v for k, v in params.items() if v is not None}

            response = await client.images.create_variation(**params)
            return response.model_dump()
        except OpenAIError as e:
            return f"OpenAI API error creating image variation with model {effective_model}: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error creating image variation with model {effective_model}: {type(e).__name__} - {e}"

    async def create_transcription(
        self,
        file: OpenAiFileTypes,
        model: str | OpenAiAudioModel = "gpt-4o-transcribe",
        language: str | None = None,
        prompt: str | None = None,
        response_format: Literal["json", "text", "srt", "verbose_json", "vtt"]
        | None = None,
        temperature: float | None = None,
        timestamp_granularities: list[Literal["word", "segment"]] | None = None,
        include: list[Literal["logprobs"]] | None = None,  # For gpt-4o models
        stream: bool = False,
    ) -> dict[str, Any] | str:
        """
        Transcribes audio into the input language.

        Args:
            file: The audio file object (not file name) to transcribe.
            model: ID of the model to use (e.g., "whisper-1", "gpt-4o-transcribe").
            language: The language of the input audio (ISO-639-1 format).
            prompt: Optional text to guide the model's style.
            response_format: The format of the transcript ("json", "text", "srt", "verbose_json", "vtt").
                             For "gpt-4o-transcribe" and "gpt-4o-mini-transcribe" with streaming,
                             this should effectively lead to a JSON-like final object.
            temperature: Sampling temperature between 0 and 1.
            timestamp_granularities: Granularities for timestamps ("word", "segment").
                                     Requires `response_format` to be "verbose_json".
            include: Additional information to include, e.g., ["logprobs"].
                     Only works with response_format="json" and gpt-4o models.
            stream: If True, streams the response. The method will aggregate the stream
                    into a final response object. Streaming is not supported for "whisper-1".

        Returns:
            A dictionary containing the transcription or a string, depending on `response_format`.
            If `stream` is True, an aggregated response dictionary.
            Returns an error message string on failure.

        Tags:
            audio, transcription, speech-to-text, important
        """
        try:
            client = await self._get_client()

            params = {
                "file": file,
                "model": model,
                "language": language if language is not None else NOT_GIVEN,
                "prompt": prompt if prompt is not None else NOT_GIVEN,
                "response_format": response_format
                if response_format is not None
                else NOT_GIVEN,
                "temperature": temperature if temperature is not None else NOT_GIVEN,
                "timestamp_granularities": timestamp_granularities
                if timestamp_granularities is not None
                else NOT_GIVEN,
                "include": include if include is not None else NOT_GIVEN,
            }

            if stream:
                stream_response = await client.audio.transcriptions.create(
                    **params, stream=True
                )

                final_transcription_value = None
                async for event in stream_response:
                    if hasattr(event, "value") and isinstance(
                        event.value, Transcription | TranscriptionVerbose
                    ):
                        if event.__class__.__name__ == "FinalTranscriptionEvent":
                            final_transcription_value = event.value
                            break

                if final_transcription_value:
                    return final_transcription_value.model_dump()
                else:
                    return {
                        "error": "Stream aggregation failed to find final transcription object."
                    }
            else:
                response = await client.audio.transcriptions.create(
                    **params, stream=False
                )
                if isinstance(response, Transcription | TranscriptionVerbose):
                    return response.model_dump()
                elif isinstance(response, str):
                    return response
                else:
                    return {
                        "error": "Unexpected_response_type_from_transcription_api",
                        "data": str(response),
                    }

        except OpenAIError as e:
            return f"OpenAI API error creating transcription: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error creating transcription: {type(e).__name__} - {e}"

    async def create_translation(
        self,
        file: OpenAiFileTypes,
        model: str | OpenAiAudioModel = "whisper-1",
        prompt: str | None = None,
        response_format: Literal["json", "text", "srt", "verbose_json", "vtt"]
        | None = None,
        temperature: float | None = None,
    ) -> dict[str, Any] | str:
        """
        Translates audio into English text.

        Args:
            file: The audio file object (not file name) to translate.
            model: ID of the model to use (currently, only "whisper-1" is supported).
            prompt: Optional text to guide the model's style (should be in English).
            response_format: The format of the translated text.
            temperature: Sampling temperature between 0 and 1.

        Returns:
            A dictionary containing the translation or a string, depending on `response_format`.
            Returns an error message string on failure.

        Tags:
            audio, translation, speech-to-text
        """
        try:
            client = await self._get_client()
            params = {
                "file": file,
                "model": model,
                "prompt": prompt if prompt is not None else NOT_GIVEN,
                "response_format": response_format
                if response_format is not None
                else NOT_GIVEN,
                "temperature": temperature if temperature is not None else NOT_GIVEN,
            }
            response = await client.audio.translations.create(**params)

            if isinstance(response, Translation | TranslationVerbose):
                return response.model_dump()
            elif isinstance(response, str):
                return response
            else:  # Should not happen
                return {
                    "error": "Unexpected_response_type_from_translation_api",
                    "data": str(response),
                }
        except OpenAIError as e:
            return f"OpenAI API error creating translation: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error creating translation: {type(e).__name__} - {e}"

    async def create_speech(
        self,
        input_text: str,
        voice: Literal[
            "alloy",
            "ash",
            "ballad",
            "coral",
            "echo",
            "fable",
            "onyx",
            "nova",
            "sage",
            "shimmer",
            "verse",
        ],
        model: str | OpenAiSpeechModel = "tts-1",
        response_format: Literal["mp3", "opus", "aac", "flac", "wav", "pcm"]
        | None = None,  # Defaults to "mp3"
        speed: float | None = None,
        instructions: str | None = None,  # For gpt-4o-mini-tts or newer models
    ) -> dict[str, Any] | str:
        """
        Generates audio from the input text.

        Args:
            input_text: The text to generate audio for (max 4096 characters).
            model: The TTS model to use (e.g., "tts-1", "tts-1-hd", "gpt-4o-mini-tts").
            voice: The voice to use for the audio.
            response_format: The format of the audio ("mp3", "opus", "aac", "flac", "wav", "pcm"). Defaults to "mp3".
            speed: Speed of the generated audio (0.25 to 4.0). Defaults to 1.0.
            instructions: Control voice with additional instructions (not for tts-1/tts-1-hd).


        Returns:
            A dictionary containing the base64 encoded audio content and content type,
            or an error message string on failure.

        Tags:
            audio, speech, text-to-speech, tts, important
        """
        try:
            client = await self._get_client()
            params = {
                "input": input_text,
                "model": model,
                "voice": voice,
                "response_format": response_format
                if response_format is not None
                else NOT_GIVEN,
                "speed": speed if speed is not None else NOT_GIVEN,
                "instructions": instructions if instructions is not None else NOT_GIVEN,
            }

            api_response = await client.audio.speech.create(**params)
            binary_content = api_response.content
            actual_content_type = api_response.response.headers.get(
                "Content-Type", "application/octet-stream"
            )

            if response_format and actual_content_type == "application/octet-stream":
                mime_map = {
                    "mp3": "audio/mpeg",
                    "opus": "audio/opus",
                    "aac": "audio/aac",
                    "flac": "audio/flac",
                    "wav": "audio/wav",
                    "pcm": "audio/L16",
                }
                actual_content_type = mime_map.get(response_format, actual_content_type)

            return {
                "model_used": str(model),
                "voice_used": voice,
                "content_type": actual_content_type,
                "content_base64": base64.b64encode(binary_content).decode(),
            }
        except OpenAIError as e:
            return f"OpenAI API error creating speech: {type(e).__name__} - {e}"
        except Exception as e:
            return f"Error creating speech: {type(e).__name__} - {e}"

    def list_tools(self) -> list[callable]:
        """Returns a list of methods exposed as tools."""
        return [
            self.create_chat_completion,
            self.upload_file,
            self.list_files,
            self.retrieve_file,
            self.delete_file,
            self.retrieve_file_content,
            self.generate_image,
            self.create_image_edit,
            self.create_image_variation,
            self.create_transcription,
            self.create_translation,
            self.create_speech,
        ]
