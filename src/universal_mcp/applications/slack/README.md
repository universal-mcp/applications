# SlackApp MCP Server

An MCP Server for the SlackApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the SlackApp API.


| Tool | Description |
|------|-------------|
| `chat_delete` | Deletes a specific message from a Slack channel. It identifies the message using its channel ID and timestamp (`ts`). This function is distinct from `chat_update` which modifies a message, and `chat_post_message` which sends a new one. |
| `chat_post_message` | Posts a new message to a specified Slack channel. It supports rich content formats like text, attachments, and blocks, along with options for threading and authorship. This function creates new messages, unlike `chat_update` which modifies existing ones or `chat_delete` which removes them. |
| `chat_update` | Updates a specific, existing message in a Slack channel, identified by its timestamp. It modifies content such as text, blocks, or attachments by calling the `chat.update` API endpoint, distinguishing it from functions that create (`chat_post_message`) or delete (`chat_delete`) messages. |
| `conversations_history` | Fetches the message history for a specific Slack conversation or channel. Supports filtering messages by timestamp and pagination using a cursor. This method retrieves messages *within* a conversation, unlike `conversations_list` which retrieves a list of available conversations. |
| `conversations_list` | Fetches a paginated list of channel-like conversations in a workspace. Allows filtering by type and excluding archived channels. This function lists available conversations, unlike `conversations_history` which retrieves the message history from within a specific conversation. |
| `reactions_add` | Adds a specific emoji reaction to a message in a Slack channel, identifying the message by its channel ID and timestamp. This method creates a new reaction, unlike `reactions_get` or `reactions_list` which retrieve existing reaction data for items or users. |
| `get_reactions_for_item` | Retrieves all reactions for a single item, such as a message, file, or file comment. This function targets reactions *on* a specific item, unlike `reactions_list` which gets reactions created *by* a user. |
| `get_user_reactions` | Retrieves a paginated list of items (e.g., messages, files) that a specific user has reacted to. Unlike `reactions_get`, which fetches all reactions for a single item, this function lists all items a given user has reacted to across Slack. |
| `search_messages` | Searches a Slack workspace for messages matching a specific query. It supports advanced control over results through pagination, sorting by relevance or timestamp, and an option to highlight search terms within the returned message content. |
| `team_info` | Fetches details for a Slack team, such as name and domain, by calling the `team.info` API endpoint. This function requires an authentication token and can optionally target a specific team by its ID, distinguishing it from user or channel-specific functions. |
| `get_user_info` | Fetches detailed profile information for a single Slack user, identified by their user ID. Unlike `users_list`, which retrieves all workspace members, this function targets an individual and can optionally include their locale information. It directly calls the `users.info` Slack API endpoint. |
| `users_list` | Fetches a paginated list of all users in a Slack workspace, including deactivated members. Unlike `users_info` which retrieves a single user's details, this function returns a collection and supports limiting results or including locale data through optional parameters. |
