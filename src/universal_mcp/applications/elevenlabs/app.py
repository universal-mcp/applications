import base64
import uuid
import time
from io import BytesIO
from typing import Any, Dict, List, Optional
import requests

from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError
from universal_mcp.integrations import Integration
from elevenlabs.client import ElevenLabs
from elevenlabs import DialogueInput


class ElevenlabsApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="elevenlabs", integration=integration, **kwargs)
        self.base_url = "https://api.elevenlabs.io"
        self._client = None

    async def get_client(self) -> ElevenLabs:
        """
        A property that lazily initializes and returns an authenticated `ElevenLabs` SDK client. On first access, it retrieves the API key from integration credentials and caches the instance, raising a `NotAuthorizedError` if credentials are not found.
        """
        if self._client is None:
            credentials = await self.integration.get_credentials_async()
            if not credentials:
                raise NotAuthorizedError("No credentials found")
            api_key = credentials.get("api_key") or credentials.get("API_KEY") or credentials.get("apiKey")
            if not api_key:
                raise NotAuthorizedError("No api key found")
            self._client = ElevenLabs(api_key=api_key)
        return self._client

    # --- Text to Speech ---

    async def text_to_speech(
        self,
        text: str,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",
        model_id: str = "eleven_multilingual_v2",
    ) -> Dict[str, Any]:
        """
        Converts text to speech and returns the generated audio data.

        Args:
            text: The text to convert to speech.
            voice_id: The ID of the voice to use. Defaults to "21m00Tcm4TlvDq8ikWAM" (Rachel).
            model_id: The model to use. Defaults to "eleven_multilingual_v2".

        Returns:
            dict: A dictionary containing:
                - 'type' (str): "audio".
                - 'data' (str): The base64 encoded audio data.
                - 'mime_type' (str): "audio/mpeg".
                - 'file_name' (str): A suggested file name.

        Tags:
            text-to-speech, speech-synthesis, audio-generation, elevenlabs, important
        """
        client = await self.get_client()

        audio_generator = client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id=model_id,
            output_format="mp3_44100_128",
        )

        audio_data = b""
        for chunk in audio_generator:
            audio_data += chunk

        audio_base64 = base64.b64encode(audio_data).decode("utf-8")
        file_name = f"{uuid.uuid4()}.mp3"
        return {"type": "audio", "data": audio_base64, "mime_type": "audio/mpeg", "file_name": file_name}

    # --- Speech to Text ---

    async def speech_to_text(self, audio_file_path: str, language_code: str = "eng", diarize: bool = True) -> str:
        """
        Transcribes an audio file into text.

        Args:
            audio_file_path (str): The path to the audio file.
            language_code (str): Language code (ISO 639-1). Defaults to "eng".
            diarize (bool): Whether to distinguish speakers. Defaults to True.

        Returns:
            str: The transcribed text.

        Tags:
            speech-to-text, transcription, audio-processing, elevenlabs, important
        """
        client = await self.get_client()
        if audio_file_path.startswith(("http://", "https://")):
            response = requests.get(audio_file_path)
            response.raise_for_status()
            audio_data_io = BytesIO(response.content)
        else:
            with open(audio_file_path, "rb") as f:
                audio_data_io = BytesIO(f.read())
        transcription = client.speech_to_text.convert(
            file=audio_data_io, model_id="scribe_v1", tag_audio_events=True, language_code=language_code, diarize=diarize
        )
        return transcription.text

    # --- Speech to Speech ---

    async def speech_to_speech(
        self, audio_source: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM", model_id: str = "eleven_multilingual_sts_v2"
    ) -> Dict[str, Any]:
        """
        Converts speech from an audio source (URL or local path) to a different voice.

        Args:
            audio_source: URL or path of the source audio.
            voice_id: Target voice ID.
            model_id: Model ID. Defaults to "eleven_multilingual_sts_v2".

        Returns:
             dict: A dictionary containing:
                - 'type' (str): "audio".
                - 'data' (str): The base64 encoded audio data.
                - 'mime_type' (str): "audio/mpeg".
                - 'file_name' (str): A suggested file name.

        Tags:
            speech-to-speech, voice-conversion, audio-processing, elevenlabs, important
        """
        if audio_source.startswith(("http://", "https://")):
            response = requests.get(audio_source)
            response.raise_for_status()
            audio_data_io = BytesIO(response.content)
        else:
            with open(audio_source, "rb") as f:
                audio_data_io = BytesIO(f.read())

        client = await self.get_client()
        audio_stream = client.speech_to_speech.convert(
            voice_id=voice_id, audio=audio_data_io, model_id=model_id, output_format="mp3_44100_128"
        )

        output_data = b""
        for chunk in audio_stream:
            output_data += chunk

        audio_base64 = base64.b64encode(output_data).decode("utf-8")
        file_name = f"{uuid.uuid4()}.mp3"
        return {"type": "audio", "data": audio_base64, "mime_type": "audio/mpeg", "file_name": file_name}

    # --- History ---

    async def get_history_items(self, page_size: int = 100, start_after_history_item_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Returns a list of generated audio history items.

        Args:
            page_size: The number of items to return. Defaults to 100.
            start_after_history_item_id: The ID of the item to start after for pagination.

        Returns:
            dict: The history response containing a list of history items.

        Tags:
            history, audio-logs, elevenlabs
        """
        client = await self.get_client()
        return client.history.list(page_size=page_size, start_after_history_item_id=start_after_history_item_id).dict()

    async def get_history_item(self, history_item_id: str) -> Dict[str, Any]:
        """
        Retrieves a specific history item by ID.

        Args:
            history_item_id: The ID of the history item to retrieve.

        Returns:
            dict: The details of the history item.

        Tags:
            history, audio-logs, elevenlabs
        """
        client = await self.get_client()
        return client.history.get(history_item_id=history_item_id).dict()

    async def delete_history_item(self, history_item_id: str) -> Dict[str, Any]:
        """
        Deletes a history item by ID.

        Args:
            history_item_id: The ID of the history item to delete.

        Returns:
            dict: The deletion status.

        Tags:
            history, audio-logs, elevenlabs
        """
        client = await self.get_client()
        return client.history.delete(history_item_id=history_item_id)

    async def get_history_item_audio(self, history_item_id: str) -> Dict[str, Any]:
        """
        Gets the audio for a history item.

        Args:
            history_item_id: The ID of the history item.

        Returns:
             dict: A dictionary containing:
                - 'type' (str): "audio".
                - 'data' (str): The base64 encoded audio data.
                - 'mime_type' (str): "audio/mpeg".
                - 'file_name' (str): A suggested file name.

        Tags:
            history, audio-download, elevenlabs
        """
        client = await self.get_client()
        audio_generator = client.history.get_audio(history_item_id=history_item_id)
        audio_data = b""
        for chunk in audio_generator:
            audio_data += chunk

        audio_base64 = base64.b64encode(audio_data).decode("utf-8")
        file_name = f"{history_item_id}.mp3"
        return {"type": "audio", "data": audio_base64, "mime_type": "audio/mpeg", "file_name": file_name}

    # --- Voices ---

    async def get_voices(self) -> Dict[str, Any]:
        """
        Lists all available voices.

        Returns:
            dict: A dictionary containing the list of voices.

        Tags:
            voices, list-voices, elevenlabs
        """
        client = await self.get_client()
        return client.voices.get_all().dict()

    async def get_voice(self, voice_id: str) -> Dict[str, Any]:
        """
        Gets details of a specific voice.

        Args:
            voice_id: The ID of the voice to retrieve.

        Returns:
            dict: The voice details.

        Tags:
            voices, voice-details, elevenlabs
        """
        client = await self.get_client()
        return client.voices.get(voice_id=voice_id).dict()

    async def delete_voice(self, voice_id: str) -> Dict[str, Any]:
        """
        Deletes a voice by ID.

        Args:
            voice_id: The ID of the voice to delete.

        Returns:
            dict: The deletion status.

        Tags:
            voices, delete-voice, elevenlabs
        """
        client = await self.get_client()
        return client.voices.delete(voice_id=voice_id).dict()

    # --- Samples ---

    async def get_voice_samples(self, voice_id: str) -> List[Dict[str, Any]]:
        """
        Gets samples for a specific voice.

        Args:
            voice_id: The ID of the voice.

        Returns:
            list: A list of voice samples.

        Tags:
            samples, voice-samples, elevenlabs
        """
        voice = await self.get_voice(voice_id)
        # Check if voice is dict or object
        if hasattr(voice, "samples"):
            return [s.dict() for s in voice.samples]
        # Pydantic .dict() might return 'samples' as None if items are missing
        samples = voice.get("samples")
        if samples is None:
            return []
        return samples

    async def delete_sample(self, voice_id: str, sample_id: str) -> Dict[str, Any]:
        """
        Deletes a sample.

        Args:
            voice_id: The ID of the voice.
            sample_id: The ID of the sample to delete.

        Returns:
            dict: The deletion status.

        Tags:
            samples, delete-sample, elevenlabs
        """
        client = await self.get_client()
        return client.samples.delete(voice_id=voice_id, sample_id=sample_id).dict()

    # --- Text to Sound Effects ---

    async def convert_text_to_sound_effect(
        self, text: str, duration_seconds: Optional[float] = None, prompt_influence: float = 0.3
    ) -> Dict[str, Any]:
        """
        Converts text to sound effects.

        Args:
            text: A text description of the sound effect.
            duration_seconds: The duration of the sound effect in seconds.
            prompt_influence: The influence of the prompt on the generation (0.0 to 1.0). Defaults to 0.3.

        Returns:
             dict: A dictionary containing:
                - 'type' (str): "audio".
                - 'data' (str): The base64 encoded audio data.
                - 'mime_type' (str): "audio/mpeg".
                - 'file_name' (str): A suggested file name.

        Tags:
            sound-effects, audio-generation, elevenlabs
        """
        client = await self.get_client()
        audio_generator = client.text_to_sound_effects.convert(
            text=text, duration_seconds=duration_seconds, prompt_influence=prompt_influence
        )
        audio_data = b""
        for chunk in audio_generator:
            audio_data += chunk

        audio_base64 = base64.b64encode(audio_data).decode("utf-8")
        file_name = f"{uuid.uuid4()}.mp3"
        return {"type": "audio", "data": audio_base64, "mime_type": "audio/mpeg", "file_name": file_name}

    # --- Text to Dialogue ---

    async def convert_text_to_dialogue(
        self,
        dialogue_turns: List[Dict[str, str]],
        model_id: str = "eleven_v3",
        output_format: str = "mp3_44100_128",
    ) -> Dict[str, Any]:
        """
        Converts a list of text and voice ID pairs into speech (dialogue) and returns synthesized audio.

        Args:
            dialogue_turns: A list of dictionaries, each containing:
                - 'text' (str): The text to be spoken.
                - 'voice_id' (str): The ID of the voice to use.
            model_id: The model to use. Defaults to "eleven_v3".
            output_format: The output format. Defaults to "mp3_44100_128".

        Example:
            dialogue_turns = [
                {"text": "Hello there! How are you doing today?", "voice_id": "9BWtsMINqrJLrRacOk9x"},
                {"text": "I'm doing great, thanks for asking! And you?", "voice_id": "IKne3meq5aSn9XLyUdCD"},
                {"text": "I'm fantastic. Ready to test this dialogue feature.", "voice_id": "9BWtsMINqrJLrRacOk9x"}
            ]
        Returns:
             dict: A dictionary containing:
                - 'type' (str): "audio".
                - 'data' (str): The base64 encoded audio data.
                - 'mime_type' (str): "audio/mpeg".
                - 'file_name' (str): A suggested file name.

        Raises:
            ValueError: If the model ID is not supported.

        Tags:
            dialogue, conversational-ai, elevenlabs
        """
        client = await self.get_client()

        inputs = [DialogueInput(text=turn["text"], voice_id=turn["voice_id"]) for turn in dialogue_turns]

        audio_generator = client.text_to_dialogue.convert(
            inputs=inputs,
            model_id=model_id,
            output_format=output_format,
        )

        audio_data = b""
        for chunk in audio_generator:
            audio_data += chunk

        audio_base64 = base64.b64encode(audio_data).decode("utf-8")
        file_name = f"dialogue_{uuid.uuid4()}.mp3"
        return {"type": "audio", "data": audio_base64, "mime_type": "audio/mpeg", "file_name": file_name}

    async def remix_voice(
        self,
        voice_id: str,
        voice_description: str,
        text: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Remixes an existing voice to create a new one based on a description.

        Args:
            voice_id: The ID of the voice to remix.
            voice_description: A description of how to change the voice (e.g., "Make the voice have a higher pitch").
            text: Optional text for the voice to speak in the preview.

        Returns:
             dict: A dictionary containing:
                - 'type' (str): "audio".
                - 'data' (str): The base64 encoded audio data of the preview.
                - 'mime_type' (str): "audio/mpeg".
                - 'file_name' (str): A suggested file name.
                - 'generated_voice_id' (str): The ID of the generated voice preview.

        Tags:
            voice-remixing, voice-modification, elevenlabs
        """
        client = await self.get_client()

        response = client.text_to_voice.remix(
            voice_id=voice_id,
            voice_description=voice_description,
            text=text,
        )

        if not response.previews:
            raise ValueError("No previews generated")

        preview = response.previews[0]
        file_name = f"remix_{preview.generated_voice_id}.mp3"

        # preview.audio_base_64 is already a base64 string
        return {
            "type": "audio",
            "data": preview.audio_base_64,
            "mime_type": "audio/mpeg",
            "file_name": file_name,
            "generated_voice_id": preview.generated_voice_id,
        }

    # --- Forced Alignment ---

    async def align_audio(
        self,
        audio_file_path: str,
        text: str,
    ) -> Dict[str, Any]:
        """
        Aligns text to an audio file, returning timing information for characters and words.

        Args:
            audio_file_path: The path to the audio file (local path or URL).
            text: The transcript text corresponding to the audio.

        Returns:
            dict: The alignment result containing 'characters', 'words', and 'loss'.

        Tags:
            alignment, audio-sync, elevenlabs
        """
        client = await self.get_client()

        # Handle URL or local file
        if audio_file_path.startswith("http://") or audio_file_path.startswith("https://"):
            response = requests.get(audio_file_path)
            response.raise_for_status()
            audio_data = BytesIO(response.content)
        else:
            with open(audio_file_path, "rb") as f:
                audio_data = BytesIO(f.read())

        alignment = client.forced_alignment.create(file=audio_data, text=text)

        return alignment.dict()

    # --- Text to Music ---

    async def convert_text_to_music(self, prompt: str, music_length_ms: Optional[int] = None) -> Dict[str, Any]:
        """
        Generates music based on a text prompt.

        Args:
            prompt: A text description of the music to generate.
            music_length_ms: Optional duration of the music in milliseconds.

        Returns:
            dict: The generated audio data including 'type', 'data' (base64), 'mime_type', and 'file_name'.

        Tags:
            music-generation, audio-generation, elevenlabs
        """
        client = await self.get_client()

        # The SDK returns a sync iterator of bytes (since client is sync)
        audio_bytes = b""
        for chunk in client.music.compose(prompt=prompt, music_length_ms=music_length_ms):
            audio_bytes += chunk

        file_name = f"music_{uuid.uuid4()}.mp3"

        return {"type": "audio", "data": base64.b64encode(audio_bytes).decode("utf-8"), "mime_type": "audio/mpeg", "file_name": file_name}

    # --- Voice Cloning ---

    async def clone_voice(self, name: str, file_paths: List[str], description: Optional[str] = None) -> Dict[str, Any]:
        """
        Clones a voice from provided audio samples (URLs or local paths).

        Args:
            name: Name of the cloned voice.
            file_paths: List of absolute file paths or URLs to audio samples.
            description: Optional description of the voice.

        Returns:
            dict: Metadata of the created voice, including 'voice_id'.

        Tags:
            voice-cloning, instant-cloning, elevenlabs
        """
        client = await self.get_client()
        files_data = []

        for path in file_paths:
            if path.startswith("http"):
                response = requests.get(path)
                response.raise_for_status()
                files_data.append(BytesIO(response.content))
            else:
                # Read into memory so we can close the file handle immediately if needed,
                # though BytesIO is preferred for the SDK.
                with open(path, "rb") as f:
                    files_data.append(BytesIO(f.read()))

        # client.voices.ivc.create returns AddVoiceIvcResponseModel which has voice_id
        voice = client.voices.ivc.create(name=name, description=description, files=files_data)

        return {"voice_id": voice.voice_id, "name": name, "status": "created"}

    # --- Voice Design ---

    async def design_voice(self, voice_description: str, text: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Generates voice previews based on a text description.

        Args:
            voice_description: Description of the voice to generate (e.g., "A deep, resonant voice").
            text: Optional text for the voice to speak. If not provided, it will be automatically generated.

        Returns:
            list: A list of voice previews, each containing 'generated_voice_id', 'audio_base_64', and 'duration_secs'.

        Tags:
            voice-design, voice-generation, elevenlabs
        """
        client = await self.get_client()

        # design() returns VoiceDesignPreviewResponse
        # We need to access .previews which is a list of VoicePreviewResponseModel
        response = client.text_to_voice.design(
            voice_description=voice_description,
            text=text,
            # Using a default model that supports design
            model_id="eleven_multilingual_ttv_v2",
        )

        previews = []
        for preview in response.previews:
            previews.append(
                {
                    "generated_voice_id": preview.generated_voice_id,
                    "audio_base_64": preview.audio_base_64,
                    "duration_secs": preview.duration_secs,
                    "type": "audio",
                    "mime_type": "audio/mpeg",
                }
            )

        return previews

    # --- Audio Isolation ---

    async def isolate_audio(self, audio_source: str) -> Dict[str, Any]:
        """
        Removes background noise from audio.

        Args:
            audio_source: URL or path of the source audio.

        Returns:
            dict: A dictionary containing:
                - 'type' (str): "audio".
                - 'data' (str): The base64 encoded audio data.
                - 'mime_type' (str): "audio/mpeg".
                - 'file_name' (str): A suggested file name.

        Tags:
            audio-isolation, noise-removal, elevenlabs
        """
        if audio_source.startswith(("http://", "https://")):
            response = requests.get(audio_source)
            response.raise_for_status()
            audio_data_io = BytesIO(response.content)
        else:
            with open(audio_source, "rb") as f:
                audio_data_io = BytesIO(f.read())
        audio_data_io.name = "audio.mp3"

        client = await self.get_client()
        audio_generator = client.audio_isolation.convert(audio=audio_data_io)

        output_data = b""
        for chunk in audio_generator:
            output_data += chunk

        audio_base64 = base64.b64encode(output_data).decode("utf-8")
        file_name = f"{uuid.uuid4()}.mp3"
        return {"type": "audio", "data": audio_base64, "mime_type": "audio/mpeg", "file_name": file_name}

    # --- Dubbing ---

    async def dub_file(
        self,
        audio_source: str,
        target_lang: str,
        mode: str = "automatic",
        source_lang: Optional[str] = None,
        num_speakers: int = 0,
        watermark: bool = False,
    ) -> Dict[str, Any]:
        """
        Dubs an audio file into another language.

        Args:
            audio_source: URL or path of the source audio.
            target_lang: The target language code.
            mode: The dubbing mode. Defaults to "automatic".
            source_lang: Optional source language code.
            num_speakers: The number of speakers (0 for automatic detection). Defaults to 0.
            watermark: Whether to add a watermark. Defaults to False.

        Returns:
             dict: The dubbing project metadata.

        Tags:
            dubbing, translation, elevenlabs
        """
        if audio_source.startswith(("http://", "https://")):
            response = requests.get(audio_source)
            response.raise_for_status()
            audio_data_io = BytesIO(response.content)
        else:
            with open(audio_source, "rb") as f:
                audio_data_io = BytesIO(f.read())

        client = await self.get_client()
        return client.dubbing.create(
            file=audio_data_io, target_lang=target_lang, mode=mode, source_lang=source_lang, num_speakers=num_speakers, watermark=watermark
        ).dict()

    async def get_dubbing_project_metadata(self, dubbing_id: str) -> Dict[str, Any]:
        """
        Gets metadata for a dubbing project.

        Args:
            dubbing_id: The ID of the dubbing project.

        Returns:
            dict: The project metadata.

        Tags:
            dubbing, project-metadata, elevenlabs
        """
        client = await self.get_client()
        return client.dubbing.get(dubbing_id=dubbing_id).dict()

    async def get_dubbed_file(self, dubbing_id: str, language_code: str) -> Dict[str, Any]:
        """
        Downloads a dubbed file.

        Args:
            dubbing_id: The ID of the dubbing project.
            language_code: The language code of the dubbed file.

        Returns:
             dict: A dictionary containing:
                - 'type' (str): "audio".
                - 'data' (str): The base64 encoded audio data.
                - 'mime_type' (str): "audio/mpeg".
                - 'file_name' (str): A suggested file name.

        Tags:
            dubbing, file-download, elevenlabs
        """
        client = await self.get_client()
        audio_generator = client.dubbing.audio.get(dubbing_id=dubbing_id, language_code=language_code)

        output_data = b""
        for chunk in audio_generator:
            output_data += chunk

        audio_base64 = base64.b64encode(output_data).decode("utf-8")
        file_name = f"{dubbing_id}_{language_code}.mp3"
        return {"type": "audio", "data": audio_base64, "mime_type": "audio/mpeg", "file_name": file_name}

    # --- Models ---

    async def get_models(self) -> List[Dict[str, Any]]:
        """
        Lists available models.

        Returns:
            list: A list of available models and their details.

        Tags:
            models, list-models, elevenlabs
        """
        client = await self.get_client()
        return [model.dict() for model in client.models.list()]

    # --- User ---

    async def get_user_info(self) -> Dict[str, Any]:
        """
        Gets user information.

        Returns:
            dict: The user information.

        Tags:
            user, profile, elevenlabs
        """
        client = await self.get_client()
        return client.user.get().dict()

    async def get_user_subscription(self) -> Dict[str, Any]:
        """
        Gets user subscription details.

        Returns:
            dict: The subscription details.

        Tags:
            user, subscription, elevenlabs
        """
        client = await self.get_client()
        return client.user.subscription.get().dict()

    # --- Usage ---

    async def get_usage(self, start_unix: Optional[int] = None, end_unix: Optional[int] = None) -> Dict[str, Any]:
        """
        Gets usage statistics. Defaults to the last 30 days if dates are not provided.

        Args:
            start_unix (Optional[int]): Start time in Unix timestamp.
            end_unix (Optional[int]): End time in Unix timestamp.

        Returns:
            dict: Usage statistics.

        Tags:
            usage, statistics, elevenlabs
        """
        client = await self.get_client()
        if end_unix is None:
            end_unix = int(time.time())
        if start_unix is None:
            start_unix = end_unix - 30 * 24 * 3600  # 30 days ago

        return client.usage.get(start_unix=start_unix, end_unix=end_unix).dict()

    # --- Tool Listing ---

    def list_tools(self):
        return [
            self.text_to_speech,
            self.speech_to_text,
            self.speech_to_speech,
            self.get_history_items,
            self.get_history_item,
            self.delete_history_item,
            self.get_history_item_audio,
            self.get_voices,
            self.get_voice,
            self.delete_voice,
            self.get_voice_samples,
            self.delete_sample,
            self.convert_text_to_sound_effect,
            self.convert_text_to_dialogue,
            self.remix_voice,
            self.convert_text_to_music,
            self.clone_voice,
            self.design_voice,
            self.align_audio,
            self.isolate_audio,
            self.dub_file,
            self.get_dubbing_project_metadata,
            self.get_dubbed_file,
            self.get_models,
            self.get_user_info,
            self.get_user_subscription,
            self.get_usage,
        ]
