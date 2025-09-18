# UnipileApp MCP Server

An MCP Server for the UnipileApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the UnipileApp API.


| Tool | Description |
|------|-------------|
| `list_all_chats` | Retrieves a paginated list of all chat conversations across linked accounts. Supports filtering by unread status, date range, account provider, and specific account IDs, distinguishing it from functions listing messages within a single chat. |
| `list_chat_messages` | Retrieves messages from a specific chat identified by `chat_id`. Supports pagination and filtering by date or sender. Unlike `list_all_messages`, which fetches from all chats, this function targets the contents of a single conversation. |
| `send_chat_message` | Sends a text message to a specific chat conversation using its `chat_id`. This function creates a new message via a POST request, distinguishing it from read-only functions like `list_chat_messages`. It returns the API's response, which typically confirms the successful creation of the message. |
| `retrieve_chat` | Retrieves a single chat's details using its Unipile or provider-specific ID. Requires an `account_id` when using a provider ID for context. This function is distinct from `list_all_chats`, which returns a collection, by targeting one specific conversation. |
| `list_all_messages` | Retrieves a paginated list of messages from all chats associated with the account(s). Unlike `list_chat_messages` which targets a specific conversation, this function provides a global message view, filterable by sender, account, and date range. |
| `list_all_accounts` | Retrieves a paginated list of all social media accounts linked to the Unipile service. This is crucial for obtaining the `account_id` required by other methods to specify which user account should perform an action, like sending a message or retrieving user-specific posts. |
| `retrieve_linked_account` | Retrieves details for a specific account linked to Unipile using its ID. It fetches metadata about the connection itself (e.g., a linked LinkedIn account), differentiating it from `retrieve_user_profile` which fetches a user's profile from the external platform. |
| `list_profile_posts` | Retrieves a paginated list of posts from a specific user or company profile using their provider ID. An authorizing `account_id` is required, and the `is_company` flag must specify the entity type, distinguishing this from `retrieve_post` which fetches a single post by its own ID. |
| `retrieve_own_profile` | Retrieves the profile details for the user associated with the specified Unipile account ID. This function targets the API's 'me' endpoint to fetch the authenticated user's profile, distinct from `retrieve_user_profile` which fetches profiles of other users by their public identifier. |
| `retrieve_user_profile` | Retrieves a specific LinkedIn user's profile using their public or internal ID, authorized via the provided `account_id`. Unlike `retrieve_own_profile`, which fetches the authenticated user's details, this function targets and returns data for any specified third-party user profile on the platform. |
| `retrieve_post` | Fetches a specific post's details by its unique ID, requiring an `account_id` for authorization. Unlike `list_profile_posts`, which retrieves a collection of posts from a user or company profile, this function targets one specific post and returns its full object. |
| `list_post_comments` | Fetches comments for a specific post using an `account_id` for authorization. Providing an optional `comment_id` retrieves threaded replies instead of top-level comments. This read-only operation contrasts with `create_post_comment`, which publishes new comments, and `list_content_reactions`, which retrieves 'likes'. |
| `create_post` | Publishes a new top-level post from a specified account, including text, user mentions, and an external link. This function creates original content, distinguishing it from `create_post_comment` which adds replies to existing posts. |
| `list_content_reactions` | Retrieves a paginated list of reactions for a given post or, optionally, a specific comment. This read-only operation uses the provided `account_id` for the request, distinguishing it from the `create_reaction` function which adds new reactions. |
| `create_post_comment` | Publishes a comment on a specified post. By providing an optional `comment_id`, it creates a threaded reply to an existing comment instead of a new top-level one. This function's dual capability distinguishes it from `list_post_comments`, which only retrieves comments and their replies. |
| `create_reaction` | Adds a specified reaction (e.g., 'like', 'love') to a LinkedIn post or, optionally, to a specific comment. This function performs a POST request to create the reaction, differentiating it from `list_content_reactions` which only retrieves existing ones. |
| `search` | Performs a comprehensive LinkedIn search for people, companies, posts, or jobs using granular filters like keywords and location. Alternatively, it can execute a search from a direct LinkedIn URL. Supports pagination and targets either the classic or Sales Navigator API. |
