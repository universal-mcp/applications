---
name: ms-teams
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# MsTeams Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `get_me` | Get the currently signed-in user. |
| `get_user_chats` | Retrieves a collection of chats the authenticated user is participating in. Supports optional OData query parameters for advanced filtering, sorting, pagination, and field selection, enabling customized data retrieval from the Microsoft Graph API. |
| `create_chat` | Creates a new one-on-one or group chat in Microsoft Teams. This function provisions a new conversation using required parameters like chatType and members. |
| `get_chat_details` | Retrieves the properties and relationships of a specific chat conversation by its unique ID. |
| `update_chat_details` | Updates properties of a specific chat, such as its topic, using its unique ID. This function performs a partial update (PATCH). Currently, only the 'topic' property can be updated for group chats. |
| `list_chat_members` | Retrieves a collection of all members in a specific chat using its ID. Note: The Microsoft Graph API for getting chat members does NOT support OData query parameters like $top, $filter, etc. |
| `get_chat_member` | Retrieves detailed information for a specific member within a chat using their unique ID. Note: The Microsoft Graph API for this endpoint does NOT support OData query parameters. |
| `list_chat_messages` | Retrieves messages from a specific chat using its ID. |
| `get_chat_message` | Retrieves the full details of a single message from a specific chat using both chat and message IDs. Note: The Microsoft Graph API for this endpoint does NOT support OData query parameters like $select or $expand. |
| `send_chat_message` | Posts a new message to a specific Microsoft Teams chat using its unique ID. |
| `list_all_channels` | Retrieves the list of channels either in this team or shared with this team (incoming channels). Supported OData parameters: - $filter: Filter by property values. - $select: Select specific properties to return (recommended for performance). - $expand: Expand related entities. |
| `get_channel` | Retrieve the properties and relationships of a channel. Supported OData parameters: - $select: Select specific properties to return (recommended for performance). - $expand: Expand related entities. |
| `get_primary_channel` | Retrieve the default General channel of a team. Supported OData parameters: - $select: Select specific properties to return. - $expand: Expand related entities. |
| `send_channel_message` | Posts a new message to a specific channel in a team. |
| `reply_to_channel_message` | Sends a reply to an existing message in a channel. |
| `list_pinned_chat_messages` | Get a list of pinned messages in a chat. Supported OData parameters: - $expand: Expand related entities (e.g., 'message'). |
| `pin_chat_message` | Pin a message in a chat. |
| `unpin_chat_message` | Unpin a message from a chat. |
| `create_team` | Create a new team. Uses the 'standard' template by default. |
| `get_team` | Retrieve a specific team's details. Supported OData parameters: - $select: Select specific properties. - $expand: Expand related entities. |
| `list_joined_teams` | List the teams that the user is a direct member of. Note: This endpoint does not support OData query parameters. It returns a subset of properties (id, displayName, description, isArchived, tenantId) by default. |
