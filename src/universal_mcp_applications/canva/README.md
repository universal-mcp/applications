# Canva MCP Server

An MCP Server for the Canva API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Canva API.


| Tool | Description |
|------|-------------|
| `v1_apps_appid_jwks` | Retrieves the JSON Web Key Set (JWKS) containing public keys for verifying JWTs associated with the specified application. |
| `v1_assets_assetid1` | Retrieves the details of a specific asset using the provided assetId and returns the asset data. |
| `v1_assets_assetid3` | Updates an asset using the "POST" method at the "/v1/assets/{assetId}" endpoint and returns a status message. |
| `v1_assets_assetid` | Deletes an asset by its unique identifier and returns a success status upon completion. |
| `v1_assets_assetid2` | Updates specific properties of an asset identified by its ID and returns the operation status. |
| `v1_assets_upload` | Uploads an asset with provided metadata to the server and returns a success or error status. |
| `v1_asset_uploads` | Initiates an asset upload using the "POST" method at the "/v1/asset-uploads" path, accepting asset metadata in the header and handling responses for successful and failed uploads. |
| `v1_asset_uploads_jobid` | Retrieves the status and results of an asset upload job identified by the job ID. |
| `v1_autofills` | Triggers an autofill operation using the API at the "/v1/autofills" path, sending data via the POST method, and returns a response indicating success or failure. |
| `v1_autofills_jobid` | Retrieves autofill data for a job identified by the specified jobId using the GET method at the "/v1/autofills/{jobId}" endpoint. |
| `v1_brand_templates` | Retrieves a list of brand templates based on query parameters such as ownership and sorting options using the "GET" method at the "/v1/brand-templates" path. |
| `v1_brand_templates_brandtemplateid` | Retrieves metadata for a specific brand template using its unique identifier. |
| `v1_brand_templates_brandtemplateid_dataset` | Retrieves the dataset definition of a brand template, including data field names and types, allowing for the identification of autofillable fields. |
| `v1_comments` | Creates a new comment and returns a status message. |
| `v1_comments_commentid_replies` | Creates a new reply to a comment using the "POST" method. |
| `v1_designs_designid_comments_commentid` | Retrieves a specific comment from a design using the provided design ID and comment ID. |
| `v1_connect_keys` | Retrieves a list of connection keys associated with the current user or application. |
| `v1_designs` | Retrieves a list of designs based on query parameters, including query, continuation, ownership, and sort order, using the GET method at the "/v1/designs" endpoint. |
| `v1_designs1` | Creates a new design resource and returns the result of the operation. |
| `v1_designs_designid` | Retrieves a specific design by its ID using the GET method at the "/v1/designs/{designId}" endpoint. |
| `v1_imports` | Initiates a data import process with the provided metadata in the request header and returns an appropriate response. |
| `v1_imports_jobid` | Retrieves the status and details of a specific import job identified by its job ID. |
| `v1_exports` | Initiates an export process through the API and returns status codes for success or failure. |
| `v1_exports_exportid` | Retrieves export details by ID using the "GET" method at the path "/v1/exports/{exportId}" and returns a response. |
| `v1_folders_folderid1` | Retrieves information about a folder with the specified ID using the "GET" method at the "/v1/folders/{folderId}" endpoint. |
| `v1_folders_folderid` | Deletes a folder with the specified ID, including all of its contents, using the DELETE method and returns a status code indicating success or failure. |
| `v1_folders_folderid2` | Updates an existing folder using the specified `folderId` and returns a status message upon successful modification. |
| `v1_folders_folderid_items` | Retrieves a paginated list of items within a specified folder, filtered by type, using continuation tokens for pagination. |
| `v1_folders_move` | Moves folders to a new location using the "POST" method at the "/v1/folders/move" endpoint and returns status messages based on the operation's success or failure. |
| `v1_folders` | Creates a new folder in the system and returns a success or error status. |
| `v1_users_me` | Retrieves information about the currently authenticated user using the GET method at the "/v1/users/me" endpoint. |
| `v1_users_me_profile` | Retrieves the authenticated user's profile information. |
