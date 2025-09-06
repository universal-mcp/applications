# WhatsappApp MCP Server

An MCP Server for the WhatsappApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the WhatsappApp API.


| Tool | Description |
|------|-------------|
| `search_contacts` | Search WhatsApp contacts by name or phone number. |
| `list_messages` | Get WhatsApp messages matching specified criteria with optional context. |
| `list_chats` | Get WhatsApp chats matching specified criteria. |
| `get_chat` | Get WhatsApp chat metadata by JID. |
| `get_direct_chat_by_contact` | Get WhatsApp chat metadata by sender phone number. |
| `get_contact_chats` | Get all WhatsApp chats involving the contact. |
| `get_last_interaction` | Get most recent WhatsApp message involving the contact. |
| `get_message_context` | Get context around a specific WhatsApp message. |
| `send_message` | Send a WhatsApp message to a person or group. For group chats use the JID. |
| `send_file` | Send a file such as a picture, raw audio, video or document via WhatsApp to the specified recipient. For group messages use the JID. |
| `send_audio_message` | Send any audio file as a WhatsApp audio message to the specified recipient. For group messages use the JID. If it errors due to ffmpeg not being installed, use send_file instead. |
| `download_media` | Download media from a WhatsApp message and get the local file path. |
