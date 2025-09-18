# GoogleMailApp MCP Server

An MCP Server for the GoogleMailApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the GoogleMailApp API.


| Tool | Description |
|------|-------------|
| `send_email` | Composes and immediately sends an email message via the Gmail API. It can function as a reply within an existing conversation if a `thread_id` is provided. This action is distinct from `send_draft`, which sends a previously saved draft message, or `create_draft`, which only saves an email. |
| `create_draft` | Saves a new email draft in Gmail with a specified recipient, subject, and body. An optional thread ID can create the draft as a reply within an existing conversation, distinguishing it from `send_email`, which sends immediately. |
| `send_draft` | Sends a pre-existing Gmail draft identified by its unique ID. It posts to the `/drafts/send` endpoint, converting a saved draft into a sent message. This function acts on drafts from `create_draft` and differs from `send_email`, which composes and sends an email in one step. |
| `get_draft` | Retrieves a specific Gmail draft by its unique ID. This function allows specifying the output format (e.g., full, raw) to control the response detail. Unlike `list_drafts`, it fetches a single, known draft rather than a collection of multiple drafts. |
| `list_drafts` | Fetches a list of email drafts, allowing filtering by a search query and limiting results. It can optionally include drafts from spam and trash, returning a collection of draft objects. This is distinct from `get_draft`, which retrieves only a single, specific draft by its ID. |
| `get_message_details` | Retrieves a specific email from Gmail by its ID. It parses the API response to extract and format key details—including sender, subject, body, and attachments—into a structured dictionary. This function provides detailed data for a single message, distinguishing it from `list_messages` which fetches multiple messages. |
| `list_messages` | Fetches a paginated list of detailed email messages using optional search queries. It concurrently retrieves full content (sender, subject, body) for each message, returning the results and a pagination token. This differs from `get_message_details`, which fetches only a single message. |
| `list_labels` | Fetches a complete list of all available labels from the user's Gmail account via the API. It retrieves both system-defined (e.g., INBOX) and user-created labels, returning their names and IDs, complementing management functions like `create_label` and `update_label`. |
| `create_label` | Creates a new Gmail label with a specified name, hardcoding its visibility to ensure it appears in both label and message lists. This function complements `update_label` and `delete_label` by adding new organizational tags to the user's account via the API. |
| `get_profile` | Retrieves the authenticated user's Gmail profile from the API. The profile includes the user's email address, total message and thread counts, and the mailbox's history ID, offering a high-level summary of the account's state. |
| `update_draft` | Replaces the entire content of a specific Gmail draft, identified by its ID, with a new message object. This allows complete modification of the recipient, subject, and body, serving as the primary "edit" function for drafts created via `create_draft`. |
| `trash_message` | Moves a specific Gmail message to the trash folder by its unique ID. This action performs a soft delete and is the direct counterpart to `untrash_message`, which restores a message. It requires both a user ID and the specific message ID to make the API call. |
| `untrash_message` | Restores a specific Gmail message from the trash to the user's mailbox, identified by its unique ID. It serves as the direct counterpart to `trash_message`, undoing the deletion action and making the message visible again in the user's account via an API call. |
| `get_attachment` | Fetches the raw, base64-encoded content of a specific email attachment using its unique ID. It requires the parent message and user IDs for a targeted API request, returning the file's size and data for download or processing, unlike functions that only list attachment metadata. |
| `update_label` | Updates an existing Gmail label's properties, such as its name, color, or visibility, using its unique ID. This modification function is distinct from `create_label` and `delete_label`, returning the full, updated label resource from the API upon successful completion. |
| `delete_label` | Permanently removes a specific Gmail label from a user's account, identified by its unique ID. This function performs an irreversible deletion via an API call, requiring both the `userId` and the label `id`. It is the destructive counterpart to `create_label` and `update_label`. |
| `get_filter` | Fetches a single Gmail filter's configuration by its unique ID for a specified user. It returns the filter’s criteria (e.g., sender) and actions (e.g., add label). This differs from `get_all_filters`, which retrieves a complete list of all filters for the user. |
| `delete_filter` | Permanently removes a specific Gmail filter, identified by its unique ID, from a user's account. This action deletes the filter's criteria and all associated automation rules, making it the destructive counterpart to `create_filter` and `get_filter`. |
| `get_all_filters` | Retrieves all configured email filters for a specified Gmail user ID. It fetches a list of a user's filters, including their matching criteria and automated actions, distinguishing it from `get_filter`, which retrieves only a single filter. |
| `create_filter` | Creates a new automated email filter in Gmail for a specified user. It requires defining matching criteria (e.g., sender, subject) and an action (e.g., add label). This function adds new rules, distinguishing it from `get_all_filters` and `delete_filter` which manage existing ones. |
