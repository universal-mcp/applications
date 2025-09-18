# OpenaiApp MCP Server

An MCP Server for the OpenaiApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the OpenaiApp API.


| Tool | Description |
|------|-------------|
| `create_chat_completion` | Generates a model response for a chat conversation. It supports both standard and streaming modes; if streaming, it internally aggregates response chunks into a single complete object, simplifying stream handling. Returns the completion data as a dictionary on success or an error string on failure. |
| `upload_file` | Uploads a file to the user's OpenAI account for use across various endpoints like 'assistants'. It accepts a file path or object and a purpose string, returning a dictionary with the created file object's details upon success. |
| `list_files` | Retrieves a paginated list of files uploaded to the OpenAI account. Allows filtering by purpose and controlling the output with limit, `after` cursor, and sort order parameters to efficiently navigate through the file collection. |
| `retrieve_file_metadata` | Retrieves the metadata (e.g., purpose, creation date) for a specific file from the OpenAI account using its ID. Unlike `retrieve_file_content`, this function does not download the file's contents. It returns a dictionary with file details on success or an error string on failure. |
| `delete_file` | Permanently deletes a file from the user's OpenAI account using its unique file ID. This action is irreversible. It returns a dictionary confirming the deletion on success or an error message string on failure. This is the 'delete' operation in the file management lifecycle. |
| `retrieve_file_content` | Retrieves a file's content from OpenAI using its ID. It returns plain text for common text formats (e.g., JSON, CSV). For binary or undecodable files, it returns a dictionary with base64-encoded data, differentiating it from `retrieve_file` which only fetches metadata. |
| `create_image` | Generates new images from a textual prompt using OpenAI's DALL-E models. It allows customization of parameters like image size, quality, style, and response format (URL or base64 JSON). Unlike other image functions in this class, it creates images entirely from scratch based on text. |
| `create_image_edit` | Modifies a source image using the DALL-E 2 model based on a text prompt. An optional mask can be supplied to specify the exact area for editing. This function is distinct from generating images from scratch (`generate_image`) or creating simple variations (`create_image_variation`). |
| `create_image_variation` | Generates one or more variations of a provided image using the OpenAI API, specifically the DALL-E 2 model. It allows customization of the number, size, and response format of the resulting images. Returns a dictionary with image data on success or an error string on failure. |
| `transcribe_audio` | Transcribes an audio file into text in its original language using models like Whisper or GPT-4o. It supports multiple response formats and internally aggregates streaming data into a final object. This differs from `create_translation`, which translates audio specifically into English text. |
| `create_translation` | Translates audio from any supported language into English text using OpenAI's API. Unlike `create_transcription`, which converts audio to text in its original language, this function's output is always English. It supports various response formats like JSON, text, or SRT for the translated content. |
| `create_speech` | Generates audio from input text using a specified TTS model and voice. This text-to-speech function allows customizing audio format and speed. On success, it returns a dictionary containing the base64-encoded audio content and its corresponding MIME type, or an error string on failure. |
