# OutlookApp MCP Server

An MCP Server for the OutlookApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the OutlookApp API.


| Tool | Description |
|------|-------------|
| `users_message_reply` | Replies to a specific message for a user using the POST method, accepting JSON content in the request body and returning status codes indicating success or error. |
| `user_send_mail` | Sends an email on behalf of the specified user, accepting the email details as JSON in the request body and returning a 204 No Content response on success. |
| `user_get_mail_folder` | Retrieves a specific mail folder for a specified user using optional query parameters to include hidden folders or select/expand properties. |
| `user_list_message` | Retrieves a list of messages for a user, allowing optional filtering and sorting of results based on parameters such as includeHiddenMessages, search, filter, top, skip, orderby, select, and expand. |
| `user_get_message` | Retrieves a specific message for a user, optionally including hidden messages, selecting specific fields, or expanding related data. |
| `user_delete_message` | Deletes a specific message for a given user using the DELETE method and optional If-Match header for conditional requests. |
| `user_message_list_attachment` | Retrieves attachments associated with a specified user's message, supporting filtering, pagination, and field selection via query parameters. |
| `get_user_id` | Retrieves the current user. |
| `get_from_url` | Makes a GET request to a full @odata.nextLink or @odata.deltaLink URL. |
