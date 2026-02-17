---
name: heygen
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# Heygen Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `get_v2_avatars` | Retrieves a list of avatar objects from the /v2/avatars API endpoint. |
| `list_avatar_groups` | Retrieves a list of avatar groups from the /v2/avatar_group.list API endpoint. |
| `list_avatars_in_group` | Retrieves a list of avatars from a specific avatar group. |
| `get_avatar_details` | Retrieves detailed information about a specific avatar by its ID. |
| `create_avatar_video` | Creates a new avatar video using the /v2/video/generate API endpoint. |
| `get_video_status` | Retrieves the status and details of a specific video by ID using the /v1/video_status.get endpoint. |
| `create_folder` | Creates a new folder under your account using the /v1/folders/create endpoint. |
| `list_folders` | Retrieves a paginated list of folders created under your account using the /v1/folders endpoint. |
| `update_folder` | Updates the name of an existing folder using the /v1/folders/{folder_id} endpoint. |
| `trash_folder` | Deletes (trashes) a specific folder by its unique folder ID using the /v1/folders/{folder_id}/trash endpoint. |
| `restore_folder` | Restores a previously deleted folder using the /v1/folders/{folder_id}/restore endpoint. |
