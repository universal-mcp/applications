# LinkedinApp MCP Server

An MCP Server for the LinkedinApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the LinkedinApp API.


| Tool | Description |
|------|-------------|
| `create_post` | Publishes a new text post to a specified LinkedIn author's feed (person or organization). It allows configuring visibility, distribution, and lifecycle state. Upon success, it returns the unique URN and URL for the new post, distinguishing this creation operation from the update or delete functions. |
| `get_authenticated_user_profile` | Retrieves the authenticated user's profile from the LinkedIn `/v2/userinfo` endpoint. Using credentials from the active integration, it returns a dictionary with basic user details like name and email. This function is for fetching user data, distinct from others that create, update, or delete posts. |
| `delete_post` | Deletes a LinkedIn post identified by its unique Uniform Resource Name (URN). This function sends a DELETE request to the API, permanently removing the content. Upon a successful HTTP 204 response, it returns a dictionary confirming the post's deletion status. |
| `update_post` | Modifies an existing LinkedIn post, identified by its URN, by performing a partial update. It selectively changes attributes like commentary or ad context, distinguishing it from `create_post` which creates new content. Returns a confirmation dictionary upon successful completion. |
