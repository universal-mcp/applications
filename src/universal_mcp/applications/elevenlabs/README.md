---
name: elevenlabs
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# Elevenlabs Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `text_to_speech` | Converts text to speech and returns the generated audio data. |
| `speech_to_text` | Transcribes an audio file into text. |
| `speech_to_speech` | Converts speech from an audio source (URL or local path) to a different voice. |
| `get_history_items` | Returns a list of generated audio history items. |
| `get_history_item` | Retrieves a specific history item by ID. |
| `delete_history_item` | Deletes a history item by ID. |
| `get_history_item_audio` | Gets the audio for a history item. |
| `get_voices` | Lists all available voices. |
| `get_voice` | Gets details of a specific voice. |
| `delete_voice` | Deletes a voice by ID. |
| `get_voice_samples` | Gets samples for a specific voice. |
| `delete_sample` | Deletes a sample. |
| `convert_text_to_sound_effect` | Converts text to sound effects. |
| `convert_text_to_dialogue` | Converts a list of text and voice ID pairs into speech (dialogue) and returns synthesized audio. |
| `remix_voice` | Remixes an existing voice to create a new one based on a description. |
| `convert_text_to_music` | Generates music based on a text prompt. |
| `clone_voice` | Clones a voice from provided audio samples (URLs or local paths). |
| `design_voice` | Generates voice previews based on a text description. |
| `align_audio` | Aligns text to an audio file, returning timing information for characters and words. |
| `isolate_audio` | Removes background noise from audio. |
| `dub_file` | Dubs an audio file into another language. |
| `get_dubbing_project_metadata` | Gets metadata for a dubbing project. |
| `get_dubbed_file` | Downloads a dubbed file. |
| `get_models` | Lists available models. |
| `get_user_info` | Gets user information. |
| `get_user_subscription` | Gets user subscription details. |
| `get_usage` | Gets usage statistics. Defaults to the last 30 days if dates are not provided. |
