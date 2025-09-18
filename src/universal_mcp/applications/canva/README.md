# CanvaApp MCP Server

An MCP Server for the CanvaApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the CanvaApp API.


| Tool | Description |
|------|-------------|
| `get_app_jwks` | Retrieves the JSON Web Key Set (JWKS) for a given application ID. The JWKS contains public keys essential for verifying the authenticity of JSON Web Tokens (JWTs) issued by the application, ensuring secure communication. |
| `get_asset` | Fetches the details of a specific asset using its unique identifier. This function performs a GET request to retrieve asset data, distinguishing it from other functions that update (`v1_assets_assetid2`, `v1_assets_assetid3`) or delete (`v1_assets_assetid`) assets at the same endpoint. |
| `post_update_asset` | Updates an asset's name and tags by its ID using an HTTP POST request. This method is distinct from the PATCH-based update function (`v1_assets_assetid2`), which performs a similar action on the same `/v1/assets/{assetId}` endpoint. |
| `delete_asset` | Deletes a specific Canva asset identified by its unique ID. This function sends an HTTP DELETE request to the `/v1/assets/{assetId}` endpoint to permanently remove the resource, returning the API's confirmation response upon successful completion. |
| `patch_asset` | Partially updates an asset by its ID using an HTTP PATCH request to modify specific fields like name or tags. Unlike `v1_assets_assetid3` which uses POST, this method applies incremental changes, returning the updated asset data upon completion. |
| `upload_asset` | Uploads an asset by sending its data to the `/v1/assets/upload` endpoint. This function performs a direct, synchronous upload, returning a confirmation. It differs from `v1_asset_uploads`, which initiates an asynchronous upload job tracked by an ID. |
| `create_asset_upload_job` | Initiates an asynchronous asset upload by creating an upload job. This method returns details, like a job ID, for subsequent steps. It differs from `v1_assets_upload`, which targets a direct, synchronous upload endpoint. |
| `get_asset_upload_job_status` | Retrieves the status and results of an asynchronous asset upload job using its unique job ID. This allows for checking the outcome of an upload initiated by `v1_asset_uploads`, returning details on its completion and any resulting asset information. |
| `create_autofill_job` | Initiates an autofill job to create a new design by populating a brand template with provided data. It sends a POST request with the template ID, data, and title, returning the details of the newly created job. |
| `get_autofill_job_status` | Retrieves the status and results of an asynchronous autofill job by its unique `jobId`. This function is used to check the outcome of a template population operation initiated by the `v1_autofills` method. |
| `list_brand_templates` | Searches for and retrieves a paginated list of brand templates. Results can be filtered by ownership and sorted by relevance, modification date, or title. A continuation token can be used to fetch subsequent pages of templates. |
| `get_brand_template_by_id` | Retrieves the complete metadata for a specific brand template using its unique identifier. This is distinct from `v1_brand_templates`, which lists multiple templates, and `v1_brand_templates_brandtemplateid_dataset`, which gets only a template's dataset. |
| `get_brand_template_dataset` | Retrieves the dataset for a specific brand template by its ID. The dataset defines the names and types of autofillable fields, which is essential for programmatically populating the template with data. |
| `create_comment` | Creates a new top-level comment attached to a specific resource, such as a design. It allows for an optional assignee and a message body, sending a POST request to the `/v1/comments` endpoint and returning the details of the newly created comment. |
| `create_comment_reply` | Creates a reply to a specific comment, identified by `commentId`. It sends a POST request with the reply's message and attachment details to the `/v1/comments/{commentId}/replies` endpoint, adding a threaded response to an existing comment. |
| `get_design_comment` | Fetches a specific comment from a design using both the design and comment IDs. Unlike other functions that create comments or replies, this method exclusively retrieves the data for a single, existing comment by making a GET request to the API. |
| `get_connection_keys` | Fetches a list of connection keys for the authenticated user or application from the `/v1/connect/keys` endpoint. These keys are used for establishing secure connections or integrations with the Canva API. |
| `list_designs` | Retrieves a list of designs available to the user. Results can be filtered by a search query, ownership status, and sort order. It supports pagination for large datasets using a continuation token to fetch multiple designs. |
| `create_design` | Creates a new design from an asset. This function sends a POST request to the `/v1/designs` endpoint with the asset ID, design type, and title, returning the data for the newly created design resource. |
| `get_design` | Fetches the details for a single, specific design using its unique identifier. This function retrieves one design, distinguishing it from `v1_designs` which lists multiple designs and `v1_designs1` which creates a new design. |
| `create_design_import_job` | Initiates a job to import a file (e.g., PDF, PPTX) for creating a new Canva design. This function sends a POST request to the `/v1/imports` endpoint and returns details of the created import job, including a job ID for status tracking. |
| `get_design_import_status` | Retrieves the status and results of a specific design import job using its unique `jobId`. This function checks the outcome of an import process initiated by the `v1_imports` method, returning details about the job's progress and final state. |
| `create_design_export` | Initiates an export job for a specified design based on its ID and format details (e.g., file type, quality). It returns the export job's details, including an ID used to track its status with `v1_exports_exportid`. |
| `get_export_job_status` | Retrieves the status and results of a specific design export job using its unique ID. This is used to check on an export initiated by the `v1_exports` function and to obtain download links for the completed file. |
| `get_folder_by_id` | Retrieves detailed information for a specific folder using its unique ID. This GET operation fetches folder metadata, distinguishing it from functions that delete (`v1_folders_folderid`) or update (`v1_folders_folderid2`) the same folder resource. |
| `delete_folder` | Deletes a folder and all its contents using the folder's unique identifier. This function sends an HTTP DELETE request to the `/v1/folders/{folderId}` endpoint and returns a confirmation status upon successful deletion. |
| `update_folder` | Updates a specific folder's properties, such as its name, using its unique ID. This function sends a PATCH request to the `/v1/folders/{folderId}` endpoint to apply partial modifications and returns the updated folder information upon success. |
| `list_folder_items` | Lists items within a specific folder. Supports optional filtering by item type (asset, design, folder, template) and pagination using a continuation token to navigate through large result sets. |
| `move_folder_item` | Moves an item, such as a design or another folder, from a source folder to a destination folder. It requires the unique IDs for the item, the source folder, and the target folder to perform the relocation, returning a status confirmation upon completion. |
| `create_folder` | Creates a new folder, optionally assigning it a name and placing it within a specified parent folder. This function is distinct from others as it uses a POST request to the base `/v1/folders` endpoint, specifically for creation. |
| `get_current_user` | Retrieves core information for the currently authenticated user, such as ID and team details. This function is distinct from `v1_users_me_profile`, which fetches more specific profile data like the user's display name and profile picture. |
| `get_current_user_profile` | Fetches detailed profile information for the currently authenticated user. This method is distinct from `v1_users_me`, which retrieves general user account information rather than specific profile details like display name or avatar. |
