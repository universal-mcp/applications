# WhatsappApp MCP Server

An MCP Server for the WhatsappApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the WhatsappApp API.


| Tool | Description |
|------|-------------|
| `search_contacts` | Searches for WhatsApp contacts by name or phone number. This function takes a query string, handles user authentication, and calls the underlying API to find and return a list of matching contacts. It serves as the primary method to look up contact information within the application. |
| `search_messages` | Searches for and retrieves a paginated list of WhatsApp messages using various filters like date, sender, chat, or content query. It can optionally include surrounding contextual messages for each result, unlike `get_message_context` which targets a single message ID. |
| `search_chats` | Retrieves a paginated list of WhatsApp chats, allowing filtering by a search query and sorting by activity or name. Unlike `get_chat`, which fetches a single known chat, this function provides broad search and discovery capabilities across multiple user conversations. |
| `get_chat_by_jid` | Retrieves metadata for a specific WhatsApp chat (direct or group) using its unique JID. It can optionally include the most recent message. This precise JID-based lookup distinguishes it from `get_direct_chat_by_contact`, which uses a phone number, and `list_chats`, which performs a broader search. |
| `get_direct_chat_by_phone_number` | Retrieves metadata for a direct (one-on-one) WhatsApp chat using a contact's phone number. Unlike `get_chat` which requires a JID, this provides a simpler way to find direct conversations. Returns a dictionary containing the chat's details, such as its JID and name. |
| `list_chats_by_contact_jid` | Retrieves a paginated list of all WhatsApp chats, including direct messages and groups, that a specific contact participates in. The contact is identified by their unique JID. This differs from `get_direct_chat_by_contact` which only finds one-on-one chats. |
| `get_last_message_by_jid` | Retrieves the content of the most recent message involving a specific contact, identified by their JID. It authenticates the user and returns the message directly as a string, offering a quick way to view the last communication without fetching full message objects or chat histories. |
| `get_message_context` | Fetches the conversational context surrounding a specific WhatsApp message ID. It retrieves a configurable number of messages immediately preceding and following the target message. This provides a focused view of a dialogue, unlike `list_messages` which performs broader, filter-based searches. |
| `send_text_message` | Authenticates the user and sends a text message to a specified WhatsApp recipient. The recipient can be an individual (via phone number) or a group (via JID). It returns a dictionary indicating the operation's success status and a corresponding message. |
| `send_attachment` | Sends a media file (image, video, document, raw audio) as a standard attachment to a WhatsApp contact or group using their phone number or JID. Unlike `send_audio_message`, which creates a playable voice note, this function handles general file transfers. Returns a success status dictionary. |
| `send_voice_message` | Sends a local audio file as a playable WhatsApp voice message, converting it to the required format. Unlike `send_file` which sends audio as a document attachment, this function formats the audio as a voice note. It can be sent to an individual contact or a group chat. |
| `download_media_from_message` | Downloads media from a specific WhatsApp message, identified by its ID and chat JID. It saves the content to a local file and returns the file's path upon success. The function automatically handles user authentication before initiating the download. |
