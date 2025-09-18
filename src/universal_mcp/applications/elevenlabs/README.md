# ElevenlabsApp MCP Server

An MCP Server for the ElevenlabsApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ElevenlabsApp API.


| Tool | Description |
|------|-------------|
| `generate_speech_audio_url` | Converts a text string into speech using the ElevenLabs API. The function then saves the generated audio to a temporary MP3 file and returns a public URL to access it, rather than the raw audio bytes. |
| `speech_to_text` | Transcribes an audio file into text using the ElevenLabs API. It supports language specification and speaker diarization, providing the inverse operation to the audio-generating `text_to_speech` method. Note: The docstring indicates this is a placeholder for an undocumented endpoint. |
| `speech_to_speech` | Downloads an audio file from a URL and converts the speech into a specified target voice using the ElevenLabs API. This function transforms the speaker's voice in an existing recording and returns the new audio data as bytes, distinct from creating audio from text. |
