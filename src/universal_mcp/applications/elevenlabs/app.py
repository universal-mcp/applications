import uuid
from io import BytesIO

import requests
from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError
from universal_mcp.integrations import Integration

from elevenlabs import ElevenLabs
from universal_mcp.applications.file_system.app import FileSystemApp


class ElevenlabsApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="elevenlabs", integration=integration, **kwargs)
        self.base_url = "https://api.elevenlabs.io"

    @property
    def client(self) -> ElevenLabs:
        """
        A property that lazily initializes and returns an authenticated `ElevenLabs` SDK client. On first access, it retrieves the API key from integration credentials and caches the instance, raising a `NotAuthorizedError` if credentials are not found.
        """
        if self._client is None:
            credentials = self.integration.get_credentials()
            if not credentials:
                raise NotAuthorizedError("No credentials found")
            api_key = (
                credentials.get("api_key")
                or credentials.get("API_KEY")
                or credentials.get("apiKey")
            )
            if not api_key:
                raise NotAuthorizedError("No api key found")
            self._client = ElevenLabs(api_key=api_key)
        return self._client

    # def get_voices(self):
    #     return self.client.voices.list_voices()

    async def generate_speech_audio_url(
        self,
        text: str,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",
        model_id: str = "eleven_multilingual_v2",
    ) -> bytes:
        """
        Converts a text string into speech using the ElevenLabs API. The function then saves the generated audio to a temporary MP3 file and returns a public URL to access it, rather than the raw audio bytes.

        Args:
            text (str): The text to convert to speech.
            voice_id (str): The ID of the voice to use.
            model_id (str, optional): The model to use. Defaults to "eleven_multilingual_v2".
            stability (float, optional): The stability of the voice.
            similarity_boost (float, optional): The similarity boost of the voice.

        Returns:
            bytes: The audio data.

        Tags:
            important
        """
        audio_generator = self.client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id=model_id,
            output_format="mp3_44100_128",
        )

        # Collect all audio chunks from the generator
        audio_data = b""
        for chunk in audio_generator:
            audio_data += chunk

        upload_result = await FileSystemApp.write_file(
            audio_data, f"/tmp/{uuid.uuid4()}.mp3"
        )
        return upload_result["data"]["url"]

    async def speech_to_text(
        self, audio_file_path: str, language_code: str = "eng", diarize: bool = True
    ) -> str:
        """
        Transcribes an audio file into text using the ElevenLabs API. It supports language specification and speaker diarization, providing the inverse operation to the audio-generating `text_to_speech` method. Note: The docstring indicates this is a placeholder for an undocumented endpoint.

        Args:
            audio_file_path (str): The path to the audio file.

        Returns:
            str: The transcribed text.

        Tags:
            important
        """
        transcription = self.client.speech_to_text.convert(
            file=audio_file_path,
            model_id="scribe_v1",  # Model to use, for now only "scribe_v1" is supported
            tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
            language_code=language_code,  # Language of the audio file. If set to None, the model will detect the language automatically.
            diarize=diarize,  # Whether to annotate who is speaking
        )
        return transcription

    async def speech_to_speech(
        self,
        audio_url: str,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",
        model_id: str = "eleven_multilingual_sts_v2",
    ) -> bytes:
        """
        Downloads an audio file from a URL and converts the speech into a specified target voice using the ElevenLabs API. This function transforms the speaker's voice in an existing recording and returns the new audio data as bytes, distinct from creating audio from text.

        Args:
            voice_id (str): The ID of the voice to use for the conversion.
            audio_file_path (str): The path to the audio file to transform.
            model_id (str, optional): The model to use. Defaults to "eleven_multilingual_sts_v2".

        Returns:
            bytes: The transformed audio data.

        Tags:
            important
        """
        response = requests.get(audio_url)
        audio_data = BytesIO(response.content)
        response = self.client.speech_to_speech.convert(
            voice_id=voice_id,
            audio=audio_data,
            model_id=model_id,
            output_format="mp3_44100_128",
        )
        return response.content

    def list_tools(self):
        return [
            self.generate_speech_audio_url,
            self.speech_to_text,
            self.speech_to_speech,
        ]


async def demo_text_to_speech():
    """
    A demonstration function that instantiates the `ElevenlabsApp` to test its `text_to_speech` method. It converts a sample string to audio and prints the resulting file URL to the console, serving as a basic usage example when the script is executed directly.
    """
    app = ElevenlabsApp()
    await app.generate_speech_audio_url("Hello, world!")


if __name__ == "__main__":
    import asyncio

    asyncio.run(demo_text_to_speech())
