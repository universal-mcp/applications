---
name: notion
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# Notion Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `retrieve_a_user` | Retrieves a user's details from the server using their unique identifier. |
| `list_all_users` | Retrieves a complete list of users from the API endpoint. |
| `retrieve_your_token_sbot_user` | Retrieves the current user's authentication token information from the SBOT service. |
| `retrieve_a_database` | Retrieves detailed information about a specific database using its unique identifier. |
| `update_a_database` | Updates a database entry with the specified ID using a PATCH request. |
| `query_a_database` | Executes a database query operation using a specified database ID and optional request parameters |
| `create_a_database` | Creates a new database on the server by sending a POST request to the database endpoint. |
| `create_a_page` | Creates a new page by sending a POST request to the API endpoint. |
| `retrieve_a_page` | Retrieves a specific page's data from a remote server using its unique identifier. |
| `update_page_properties` | Updates the properties of a page with the specified ID using the provided request body. |
| `retrieve_a_page_property_item` | Retrieves a specific property item from a Notion page using the page ID and property ID. |
| `retrieve_block_children` | Retrieves all child blocks for a specified parent block using its ID via the API. |
| `append_block_children` | Appends child elements to a specified block and returns the updated block data. |
| `retrieve_a_block` | Retrieves a specific block of data from the API using its unique identifier. |
| `delete_a_block` | Deletes a specified block by its ID and returns the server response. |
| `update_a_block` | Updates a specific block resource via a PATCH request to the API endpoint |
| `search` | Executes a search operation by sending a POST request to the search endpoint and returns the results |
| `retrieve_comments` | Retrieves comments from a remote server with optional block filtering and pagination support. |
| `add_comment_to_page` | Adds a comment to a page by making an HTTP POST request to the comments endpoint. |
