---
name: google-gemini
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# GoogleGemini Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `generate_text` | Generates text using the Google Gemini model based on a given prompt. This tool is suitable for various natural language processing tasks such as content generation, summarization, translation, and question answering. |
| `generate_image` | Generates an image based on a text prompt and an optional reference image using the Google Gemini model. This tool is ideal for creating visual content or modifying existing images based on natural language descriptions. It returns a dictionary containing the generated image data (base64 encoded), its MIME type, a suggested file name, and any accompanying text. |
| `analyze_image` | Analyzes one or more images based on a text prompt using the Google Gemini model. This tool is capable of describing images, answering questions about them, or performing visual reasoning. It accepts image URLs and a text prompt, returning a natural language response. |
| `generate_audio` | Generates audio from a given text prompt using the Google Gemini model's Text-to-Speech (TTS) capabilities. This tool is useful for converting text into spoken audio, which can be used for voiceovers, accessibility features, or interactive applications. It returns a dictionary containing the generated audio data (base64 encoded), its MIME type, and a suggested file name. |
| `generate_video` | Generates a video from a text prompt using Google Gemini's Veo model. This is a long-running operation that returns an operation ID. Use check_video_operation to monitor progress. |
| `generate_video_from_image` | Generates a video by animating a reference image as the first frame. This is a long-running operation that returns an operation ID. Use check_video_operation to monitor progress. |
| `generate_video_with_frames` | Generates a video by interpolating between a first frame and last frame. This is a long-running operation that returns an operation ID. Use check_video_operation to monitor progress. |
| `generate_video_with_reference_images` | Generates a video while preserving the appearance of a subject from reference images. This is a long-running operation that returns an operation ID. Use check_video_operation to monitor progress. |
| `extend_video` | Extends a previously generated Veo video by 7 seconds (can be repeated up to 20 times). This is a long-running operation that returns an operation ID. Use check_video_operation to monitor progress. |
| `check_video_operation` | Checks the status of a long-running video generation operation. |
