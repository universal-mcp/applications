# GoogleMailApp MCP Server

An MCP Server for the GoogleMailApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the GoogleMailApp API.


| Tool | Description |
|------|-------------|
| `send_email` | Sends an email using the Gmail API and returns a confirmation or error message. |
| `create_draft` | Creates a draft email message in Gmail using the Gmail API and returns a confirmation status. |
| `send_draft` | Sends an existing draft email using the Gmail API and returns a confirmation message. |
| `get_draft` | Retrieves and formats a specific draft email from Gmail by its ID |
| `list_drafts` | Retrieves and formats a list of email drafts from the user's Gmail mailbox with optional filtering and pagination. |
| `get_message` | Retrieves and formats a specific email message from Gmail API by its ID, including sender, recipient, date, subject, and full message body content. |
| `list_messages` | Retrieves and formats a list of messages from the user's Gmail mailbox with optional filtering and pagination support. |
| `list_labels` | Retrieves and formats a list of all labels (both system and user-created) from the user's Gmail account, organizing them by type and sorting them alphabetically. |
| `create_label` | Creates a new Gmail label with specified visibility settings and returns creation status details. |
| `get_profile` | Retrieves and formats the user's Gmail profile information including email address, message count, thread count, and history ID. |
| `update_drafts` | Updates an existing Gmail draft with new message content and metadata. |
| `trash_messsages` | Moves a message to the trash folder (acts like delete functionality). |
| `untrash_messages` | Moves a message out of the trash, effectively undoing a trash action and restoring the message to the user's mailbox. |
| `get_attachments` | Retrieves the actual file content of a specific attachment from a Gmail message |
| `update_labels` | Update an existing Gmail label's properties such as name, color, or visibility. |
| `delete_labels` | Delete a Gmail label by its ID. |
| `get_filters` | Fetch Gmail filter configuration and rules by filter ID |
| `delete_filters` | Remove Gmail filter and its associated automation rules |
| `list_filters` | Retrieve all Gmail filters and their automation settings |
| `create_filters` | Set up new Gmail filter with criteria and automated actions |
