# HttpToolsApp MCP Server

An MCP Server for the HttpToolsApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the HttpToolsApp API.


| Tool | Description |
|------|-------------|
| `http_get` | Executes an HTTP GET request to a given URL with optional headers and query parameters. It handles HTTP errors by raising an exception and processes the response, returning parsed JSON or a dictionary with the raw text and status details if JSON is unavailable. |
| `http_post` | Sends an HTTP POST request to a URL with an optional JSON body and headers. It returns the parsed JSON response or raw text if parsing fails and raises an exception for HTTP errors. It is used for creating new resources, unlike http_get which retrieves data. |
| `http_put` | Performs an HTTP PUT request to update or replace a resource at a specified URL. It accepts an optional JSON body and headers, raises an exception for error responses, and returns the parsed JSON response or a dictionary with the raw text and status details. |
| `http_delete` | Sends an HTTP DELETE request to a URL with optional headers and a JSON body. Raises an exception for HTTP error statuses and returns the parsed JSON response. If the response isn't JSON, it returns the text content, status code, and headers. |
| `http_patch` | Sends an HTTP PATCH request to apply partial modifications to a resource at a given URL. It accepts optional headers and a JSON body. It returns the parsed JSON response, or the raw text with status details if the response is not valid JSON. |
