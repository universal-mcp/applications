import uuid
import wave
from typing import Annotated  # Added Literal for type hinting

from google import genai
from google.genai import types
from loguru import logger
from PIL import Image

from universal_mcp.applications.application import APIApplication
from universal_mcp.applications.file_system.app import FileSystemApp
from universal_mcp.integrations import Integration


class GoogleGeminiApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="google_gemini", integration=integration, **kwargs)
        self._genai_client = None

    @property
    def genai_client(self) -> genai.Client:
        if self._genai_client is not None:
            return self._genai_client
        credentials = self.integration.get_credentials()
        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )
        if not api_key:
            raise ValueError("API key not found in integration credentials")
        self._genai_client = genai.Client(api_key=api_key)
        return self._genai_client

    async def generate_text(
        self,
        prompt: Annotated[str, "The prompt to generate text from"],
        model: str = "gemini-2.5-flash",
    ) -> str:
        """Generates text using the Google Gemini model.

        Args:
            prompt (str): The prompt to generate text from.
            model (str, optional): The Gemini model to use for text generation. Defaults to "gemini-2.5-flash".

        Returns:
            str: The generated text response from the Gemini model.

        Raises:
            ValueError: If the API key is not found in the integration credentials.
            Exception: If the underlying client or API call fails.

        Example:
            response = app.generate_text("Tell me a joke.")
            
        Tags:
            important
        """
        response = self.genai_client.generate_content(prompt, model=model)
        return response.text

    async def generate_image(
        self,
        prompt: Annotated[str, "The prompt to generate image from"],
        image: Annotated[str, "The reference image path"] | None = None,
        model: str = "gemini-2.5-flash-image-preview",
    ) -> list:
        """
        Generates an image using the Google Gemini model and returns a list of results.
        Each result is a dict with either 'text' or 'image_bytes' (raw image data).

        Args:
            prompt (str): The prompt to generate image from.
            model (str, optional): The Gemini model to use for image generation. Defaults to "gemini-2.5-flash-image-preview".

        Returns:
            list: A list of dicts, each containing either 'text' or 'image_bytes'.
            
        Tags:
            important
        """
        # The Gemini API is synchronous, so run in a thread
        contents = [prompt]
        if image:
            image = Image.open(image)
            contents.append(image)
        response = self.genai_client.models.generate_content(
            model=model,
            contents=contents,
        )
        candidate = response.candidates[0]
        text = ""
        for part in candidate.content.parts:
            if part.text is not None:
                text += part.text
            elif part.inline_data is not None:
                # Return the raw image bytes
                image_bytes = part.inline_data.data
                upload_result = await FileSystemApp.write_file(
                    image_bytes, f"/tmp/{uuid.uuid4()}.png"
                )
                logger.info(f"Upload result: {upload_result['status']}")
                image_url = upload_result["data"]["url"]
                logger.info(f"Image URL: {image_url}")
                text += f"![Image]({image_url})"
        logger.info(f"Text: {text}")
        return {"text": text}

    async def generate_audio(
        self,
        prompt: Annotated[str, "The prompt to generate audio from"],
        model: str = "gemini-2.5-flash-preview-tts",
    ) -> str:
        """Generates audio using the Google Gemini model and returns the uploaded audio URL.

        Args:
            prompt (str): The prompt to generate audio from.
            model (str, optional): The Gemini model to use for audio generation. Defaults to "gemini-2.5-flash-preview-tts".

        Returns:
            str: The URL of the uploaded audio file.
            
        Tags:
            important
        """

        # Set up the wave file to save the output:
        def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
            with wave.open(filename, "wb") as wf:
                wf.setnchannels(channels)
                wf.setsampwidth(sample_width)
                wf.setframerate(rate)
                wf.writeframes(pcm)

        response = self.genai_client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name="Kore",
                        )
                    )
                ),
            ),
        )

        data = response.candidates[0].content.parts[0].inline_data.data

        file_name = "/tmp/audio.wav"
        wave_file(file_name, data)  # Saves the file to current directory
        # Upload the audio file directly
        upload_result = await FileSystemApp.move_file(
            file_name, f"/tmp/{uuid.uuid4()}.wav"
        )
        logger.info(f"Audio upload result: {upload_result['status']}")
        audio_url = upload_result["data"]["url"]
        logger.info(f"Audio URL: {audio_url}")

        return audio_url

    def list_tools(self):
        return [
            self.generate_text,
            self.generate_image,
            self.generate_audio,
        ]


async def test_google_gemini():
    app = GoogleGeminiApp()
    result = await app.generate_image(
        "A beautiful women potrait with red green hair color"
    )
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(test_google_gemini())
