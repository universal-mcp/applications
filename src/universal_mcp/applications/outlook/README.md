# OutlookApp MCP Server

An MCP Server for the OutlookApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the OutlookApp API.


| Tool | Description |
|------|-------------|
| `reply_to_message` | Replies to an email using its message ID, with either a simple comment or a full message object including attachments. Unlike `send_mail`, which creates a new email, this function targets an existing message. It defaults to the current user if no user ID is specified. |
| `send_mail` | Sends a new email on behalf of a specified or current user, using a dictionary for content like recipients and subject. Unlike `reply_to_message`, which replies to an existing message, this function composes and sends an entirely new email from scratch. |
| `get_mail_folder` | Retrieves a specific mail folder's metadata by its ID for a given user. The response can be customized to include hidden folders or select specific properties. Unlike `list_user_messages`, this function fetches folder details, not the emails contained within it. |
| `list_user_messages` | Retrieves a list of messages from a user's mailbox. This function supports powerful querying using optional parameters for filtering, searching, sorting, and pagination, unlike `get_user_message`, which fetches a single email by its ID. |
| `get_user_message` | Retrieves a specific email message by its ID for a given user, with options to select specific fields or expand related data. Unlike `list_user_messages`, which fetches a collection of emails with advanced filtering, this function is designed to retrieve a single, known message. |
| `user_delete_message` | Permanently deletes a specific email, identified by `message_id`, from a user's mailbox. If `user_id` is not provided, it defaults to the current authenticated user. Unlike retrieval functions such as `get_user_message`, this performs a destructive action to remove the specified email from Outlook. |
| `list_message_attachments` | Retrieves attachments for a specific email message, identified by its ID. Supports advanced querying for filtering, sorting, and pagination, allowing users to select specific fields to return in the result set, focusing only on attachments rather than the full message content. |
| `get_current_user_profile` | Fetches the `userPrincipalName` for the currently authenticated user from the `/me` endpoint. This internal helper is used by other methods to automatically obtain the user's ID for API calls when a `user_id` is not explicitly provided. |
| `get_next_page` | Executes a GET request for a full URL, typically the `@odata.nextLink` from a previous paginated API response. It simplifies retrieving subsequent pages of data from list functions by handling URL validation and parsing before fetching the results for the next page. |
