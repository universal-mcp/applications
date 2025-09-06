# Figma MCP Server

An MCP Server for the Figma API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Figma API.


| Tool | Description |
|------|-------------|
| `get_file` | Retrieves a specified file's data (including versions, geometry, and plugin information) from the API using a unique file identifier. |
| `get_file_nodes` | Retrieves nodes related to a file identified by the "file_key" using the specified query parameters for filtering by "ids", "version", "depth", "geometry", and "plugin_data". |
| `get_images` | Retrieves an image specified by the `file_key` using the GET method, allowing optional query parameters for customization such as formatting, scaling, and SVG options. |
| `get_image_fills` | Retrieves images associated with a file identified by the `{file_key}` using the `/v1/files/{file_key}/images` API endpoint. |
| `get_team_projects` | Retrieves a list of projects associated with a specific team identified by the team_id parameter. |
| `get_project_files` | Retrieves files from a specified project, optionally including branch data, using the provided project identifier. |
| `get_file_versions` | Retrieves a list of file versions using the "GET" method, filtering by file key and optional query parameters for pagination and sorting. |
| `get_comments` | Retrieves comments associated with a specified file and optionally returns them in Markdown format based on the query parameter. |
| `post_comment` | Creates a new comment on a file specified by the file_key and returns an appropriate status code. |
| `delete_comment` | Deletes a specified comment from a file identified by its file key and comment ID. |
| `get_comment_reactions` | Retrieves reactions for a specific comment in a file using the provided file key and comment ID. |
| `post_comment_reaction` | Adds a reaction to a specific comment on a file identified by the file key and comment ID using the "POST" method at the "/v1/files/{file_key}/comments/{comment_id}/reactions" endpoint. |
| `delete_comment_reaction` | Removes a reaction emoji from a comment on a file using the specified emoji parameter. |
| `get_me` | Retrieves the authenticated user's profile data. |
| `get_team_components` | Retrieves a list of components for a specified team with pagination support using page_size, after, and before parameters. |
| `get_file_components` | Retrieves a list of components associated with a file identified by the specified file key using the API endpoint "/v1/files/{file_key}/components". |
| `get_component` | Retrieves component information for a specific key using the API endpoint at "/v1/components/{key}" with the GET method. |
| `get_team_component_sets` | Retrieves a paginated list of component sets associated with a specific team ID, supporting pagination via page size, after, and before query parameters. |
| `get_file_component_sets` | Retrieves the component sets associated with a file identified by a specific file key using the "GET" method at the "/v1/files/{file_key}/component_sets" endpoint. |
| `get_component_set` | Retrieves a component set by its unique key identifier and returns the associated component data. |
| `get_team_styles` | Retrieves paginated style resources associated with a specific team using query parameters for pagination control. |
| `get_file_styles` | Retrieves styles information for a specific file identified by the file key using the API endpoint "/v1/files/{file_key}/styles" with the GET method. |
| `get_style` | Retrieves a style object associated with the specified key using the "GET" method at the "/v1/styles/{key}" endpoint. |
| `post_webhook` | Registers a new webhook to receive HTTP callbacks for specified events, returning success or error status codes. |
| `get_webhook` | Retrieves information about a specific webhook by its ID using the "GET" method at the path "/v2/webhooks/{webhook_id}". |
| `put_webhook` | Updates an existing webhook's configuration using the provided webhook ID and returns an HTTP status code indicating success or failure. |
| `delete_webhook` | Deletes a webhook identified by its `webhook_id`, permanently removing it to manage and optimize webhook configurations. |
| `get_team_webhooks` | Retrieves a list of webhooks for a specified team using the "GET" method, with the team identified by the `team_id` path parameter. |
| `get_webhook_requests` | Retrieves a list of requests for a specific webhook identified by `{webhook_id}` using the "GET" method. |
| `get_activity_logs` | Retrieves a list of activity logs filtered by specified events, time range, and other parameters, returning the results in a specified order with a limited number of entries. |
| `get_payments` | Retrieves payment information based on specified parameters, including plugin payment token, user ID, community file ID, plugin ID, and widget ID, using the "/v1/payments" API endpoint with a GET request. |
| `get_local_variables` | Retrieves local variables for a file specified by the "file_key" using the "GET" method. |
| `get_published_variables` | Retrieves the published variables for a file identified by the `{file_key}` using the `GET` method. |
| `post_variables` | Creates variables for a specific file identified by its file_key and returns an appropriate status code based on the operation's outcome. |
| `get_dev_resources` | Retrieves development resources associated with a specific file, identified by its file_key, with optional filtering by node IDs. |
| `post_dev_resources` | Creates developer resources via the API and returns a status response. |
| `put_dev_resources` | Replaces a specific developer resource at the specified path with updated data, returning a status code for success or error conditions. |
| `delete_dev_resource` | Deletes a specific development resource associated with a file using the provided file key and development resource ID. |
