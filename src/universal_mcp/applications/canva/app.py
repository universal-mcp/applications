from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class CanvaApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="canva", integration=integration, **kwargs)
        self.base_url = "https://api.canva.com/rest"

    def get_app_jwks(self, appId) -> dict[str, Any]:
        """
        Retrieves the JSON Web Key Set (JWKS) for a given application ID. The JWKS contains public keys essential for verifying the authenticity of JSON Web Tokens (JWTs) issued by the application, ensuring secure communication.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: OK

        Tags:
            app
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'")
        url = f"{self.base_url}/v1/apps/{appId}/jwks"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_asset(self, assetId) -> dict[str, Any]:
        """
        Fetches the details of a specific asset using its unique identifier. This function performs a GET request to retrieve asset data, distinguishing it from other functions that update (`v1_assets_assetid2`, `v1_assets_assetid3`) or delete (`v1_assets_assetid`) assets at the same endpoint.

        Args:
            assetId (string): assetId

        Returns:
            dict[str, Any]: OK

        Tags:
            asset
        """
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'")
        url = f"{self.base_url}/v1/assets/{assetId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_update_asset(self, assetId, name=None, tags=None) -> dict[str, Any]:
        """
        Updates an asset's name and tags by its ID using an HTTP POST request. This method is distinct from the PATCH-based update function (`v1_assets_assetid2`), which performs a similar action on the same `/v1/assets/{assetId}` endpoint.

        Args:
            assetId (string): assetId
            name (string): name Example: '<string>'.
            tags (array): tags
                Example:
                ```json
                {
                  "name": "<string>",
                  "tags": [
                    "<string>",
                    "<string>"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            asset
        """
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'")
        request_body = {
            "name": name,
            "tags": tags,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/assets/{assetId}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_asset(self, assetId) -> Any:
        """
        Deletes a specific Canva asset identified by its unique ID. This function sends an HTTP DELETE request to the `/v1/assets/{assetId}` endpoint to permanently remove the resource, returning the API's confirmation response upon successful completion.

        Args:
            assetId (string): assetId

        Returns:
            Any: OK

        Tags:
            asset
        """
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'")
        url = f"{self.base_url}/v1/assets/{assetId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def patch_asset(self, assetId, name=None, tags=None) -> dict[str, Any]:
        """
        Partially updates an asset by its ID using an HTTP PATCH request to modify specific fields like name or tags. Unlike `v1_assets_assetid3` which uses POST, this method applies incremental changes, returning the updated asset data upon completion.

        Args:
            assetId (string): assetId
            name (string): name Example: '<string>'.
            tags (array): tags
                Example:
                ```json
                {
                  "name": "<string>",
                  "tags": [
                    "<string>",
                    "<string>"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            asset
        """
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'")
        request_body = {
            "name": name,
            "tags": tags,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/assets/{assetId}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def upload_asset(self, request_body=None) -> dict[str, Any]:
        """
        Uploads an asset by sending its data to the `/v1/assets/upload` endpoint. This function performs a direct, synchronous upload, returning a confirmation. It differs from `v1_asset_uploads`, which initiates an asynchronous upload job tracked by an ID.

        Args:
            request_body (dict | None): Optional dictionary for arbitrary request body data.

        Returns:
            dict[str, Any]: OK

        Tags:
            asset
        """
        url = f"{self.base_url}/v1/assets/upload"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_asset_upload_job(self, request_body=None) -> dict[str, Any]:
        """
        Initiates an asynchronous asset upload by creating an upload job. This method returns details, like a job ID, for subsequent steps. It differs from `v1_assets_upload`, which targets a direct, synchronous upload endpoint.

        Args:
            request_body (dict | None): Optional dictionary for arbitrary request body data.

        Returns:
            dict[str, Any]: OK

        Tags:
            asset
        """
        url = f"{self.base_url}/v1/asset-uploads"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_asset_upload_job_status(self, jobId) -> dict[str, Any]:
        """
        Retrieves the status and results of an asynchronous asset upload job using its unique job ID. This allows for checking the outcome of an upload initiated by `v1_asset_uploads`, returning details on its completion and any resulting asset information.

        Args:
            jobId (string): jobId

        Returns:
            dict[str, Any]: OK

        Tags:
            asset
        """
        if jobId is None:
            raise ValueError("Missing required parameter 'jobId'")
        url = f"{self.base_url}/v1/asset-uploads/{jobId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_autofill_job(
        self, brand_template_id=None, data=None, preview=None, title=None
    ) -> dict[str, Any]:
        """
        Initiates an autofill job to create a new design by populating a brand template with provided data. It sends a POST request with the template ID, data, and title, returning the details of the newly created job.

        Args:
            brand_template_id (string): brand_template_id Example: '<string>'.
            data (object): data
            preview (string): preview Example: '<boolean>'.
            title (string): title
                Example:
                ```json
                {
                  "brand_template_id": "<string>",
                  "data": {
                    "ipsum_a5": {
                      "asset_id": "<string>",
                      "type": "image"
                    },
                    "laboris3": {
                      "asset_id": "<string>",
                      "type": "image"
                    }
                  },
                  "preview": "<boolean>",
                  "title": "<string>"
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            autofill
        """
        request_body = {
            "brand_template_id": brand_template_id,
            "data": data,
            "preview": preview,
            "title": title,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/autofills"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_autofill_job_status(self, jobId) -> dict[str, Any]:
        """
        Retrieves the status and results of an asynchronous autofill job by its unique `jobId`. This function is used to check the outcome of a template population operation initiated by the `v1_autofills` method.

        Args:
            jobId (string): jobId

        Returns:
            dict[str, Any]: OK

        Tags:
            autofill
        """
        if jobId is None:
            raise ValueError("Missing required parameter 'jobId'")
        url = f"{self.base_url}/v1/autofills/{jobId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_brand_templates(
        self, query=None, continuation=None, ownership=None, sort_by=None
    ) -> dict[str, Any]:
        """
        Searches for and retrieves a paginated list of brand templates. Results can be filtered by ownership and sorted by relevance, modification date, or title. A continuation token can be used to fetch subsequent pages of templates.

        Args:
            query (string): Lets you search the brand templates available to the user using a search term or terms. Example: '<string>'.
            continuation (string): If the success response contains a continuation token, the user has access to more
        brand templates you can list. You can use this token as a query parameter and retrieve
        more templates from the list, for example
        `/v1/brand-templates?continuation={continuation}`.
        To retrieve all the brand templates available to the user, you might need to make
        multiple requests. Example: '<string>'.
            ownership (string): Filter the brand templates to only show templates created by a particular user.
        Provide a Canva user ID and it will filter the list to only show brand templates
        created by that user. The 'owner' of a template is the user who created the design,
        and the owner can't be changed. Example: '<string>'.
            sort_by (string): Sort the list of brand templates. This can be one of the following:
        - `RELEVANCE`: (Default) Sort results using a relevance algorithm.
        - `MODIFIED_DESCENDING`: Sort results by the date last modified in descending order.
        - `MODIFIED_ASCENDING`: Sort results by the date last modified in ascending order.
        - `TITLE_DESCENDING`: Sort results by title in descending order.
        - `TITLE_ASCENDING`: Sort results by title in ascending order. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            brand_template, important
        """
        url = f"{self.base_url}/v1/brand-templates"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("continuation", continuation),
                ("ownership", ownership),
                ("sort_by", sort_by),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_brand_template_by_id(self, brandTemplateId) -> dict[str, Any]:
        """
        Retrieves the complete metadata for a specific brand template using its unique identifier. This is distinct from `v1_brand_templates`, which lists multiple templates, and `v1_brand_templates_brandtemplateid_dataset`, which gets only a template's dataset.

        Args:
            brandTemplateId (string): brandTemplateId

        Returns:
            dict[str, Any]: OK

        Tags:
            brand_template
        """
        if brandTemplateId is None:
            raise ValueError("Missing required parameter 'brandTemplateId'")
        url = f"{self.base_url}/v1/brand-templates/{brandTemplateId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_brand_template_dataset(self, brandTemplateId) -> dict[str, Any]:
        """
        Retrieves the dataset for a specific brand template by its ID. The dataset defines the names and types of autofillable fields, which is essential for programmatically populating the template with data.

        Args:
            brandTemplateId (string): brandTemplateId

        Returns:
            dict[str, Any]: OK

        Tags:
            brand_template
        """
        if brandTemplateId is None:
            raise ValueError("Missing required parameter 'brandTemplateId'")
        url = f"{self.base_url}/v1/brand-templates/{brandTemplateId}/dataset"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_comment(
        self, assignee_id=None, attached_to=None, message=None
    ) -> dict[str, Any]:
        """
        Creates a new top-level comment attached to a specific resource, such as a design. It allows for an optional assignee and a message body, sending a POST request to the `/v1/comments` endpoint and returning the details of the newly created comment.

        Args:
            assignee_id (string): assignee_id Example: '<string>'.
            attached_to (object): attached_to
            message (string): message
                Example:
                ```json
                {
                  "assignee_id": "<string>",
                  "attached_to": {
                    "design_id": "<string>",
                    "type": "design"
                  },
                  "message": "<string>"
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            comment
        """
        request_body = {
            "assignee_id": assignee_id,
            "attached_to": attached_to,
            "message": message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/comments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_comment_reply(
        self, commentId, attached_to=None, message=None
    ) -> dict[str, Any]:
        """
        Creates a reply to a specific comment, identified by `commentId`. It sends a POST request with the reply's message and attachment details to the `/v1/comments/{commentId}/replies` endpoint, adding a threaded response to an existing comment.

        Args:
            commentId (string): commentId
            attached_to (object): attached_to
            message (string): message
                Example:
                ```json
                {
                  "attached_to": {
                    "design_id": "<string>",
                    "type": "design"
                  },
                  "message": "<string>"
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            comment
        """
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'")
        request_body = {
            "attached_to": attached_to,
            "message": message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/comments/{commentId}/replies"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_design_comment(self, designId, commentId) -> dict[str, Any]:
        """
        Fetches a specific comment from a design using both the design and comment IDs. Unlike other functions that create comments or replies, this method exclusively retrieves the data for a single, existing comment by making a GET request to the API.

        Args:
            designId (string): designId
            commentId (string): commentId

        Returns:
            dict[str, Any]: OK

        Tags:
            comment
        """
        if designId is None:
            raise ValueError("Missing required parameter 'designId'")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'")
        url = f"{self.base_url}/v1/designs/{designId}/comments/{commentId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_connection_keys(self) -> dict[str, Any]:
        """
        Fetches a list of connection keys for the authenticated user or application from the `/v1/connect/keys` endpoint. These keys are used for establishing secure connections or integrations with the Canva API.

        Returns:
            dict[str, Any]: OK

        Tags:
            connect
        """
        url = f"{self.base_url}/v1/connect/keys"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_designs(
        self, query=None, continuation=None, ownership=None, sort_by=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of designs available to the user. Results can be filtered by a search query, ownership status, and sort order. It supports pagination for large datasets using a continuation token to fetch multiple designs.

        Args:
            query (string): Lets you search the user's designs, and designs shared with the user, using a search term or terms. Example: '<string>'.
            continuation (string): If the success response contains a continuation token, the list contains more designs
        you can list. You can use this token as a query parameter and retrieve more
        designs from the list, for example
        `/v1/designs?continuation={continuation}`. To retrieve all of a user's designs, you might need to make multiple requests. Example: '<string>'.
            ownership (string): Filter the list of designs based on the user's ownership of the designs.
        This can be one of the following: - `owned`: Designs owned by the user.
        - `shared`: Designs shared with the user.
        - `any`: Designs owned by and shared with the user. Example: '<string>'.
            sort_by (string): Sort the list of designs.
        This can be one of the following: - `relevance`: (Default) Sort results using a relevance algorithm.
        - `modified_descending`: Sort results by the date last modified in descending order.
        - `modified_ascending`: Sort results by the date last modified in ascending order.
        - `title_descending`: Sort results by title in descending order.
        - `title_ascending`: Sort results by title in ascending order. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            design, important
        """
        url = f"{self.base_url}/v1/designs"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("continuation", continuation),
                ("ownership", ownership),
                ("sort_by", sort_by),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_design(
        self, asset_id=None, design_type=None, title=None
    ) -> dict[str, Any]:
        """
        Creates a new design from an asset. This function sends a POST request to the `/v1/designs` endpoint with the asset ID, design type, and title, returning the data for the newly created design resource.

        Args:
            asset_id (string): asset_id Example: '<string>'.
            design_type (object): design_type
            title (string): title
                Example:
                ```json
                {
                  "asset_id": "<string>",
                  "design_type": {
                    "name": "doc",
                    "type": "preset"
                  },
                  "title": "<string>"
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            design
        """
        request_body = {
            "asset_id": asset_id,
            "design_type": design_type,
            "title": title,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/designs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_design(self, designId) -> dict[str, Any]:
        """
        Fetches the details for a single, specific design using its unique identifier. This function retrieves one design, distinguishing it from `v1_designs` which lists multiple designs and `v1_designs1` which creates a new design.

        Args:
            designId (string): designId

        Returns:
            dict[str, Any]: OK

        Tags:
            design
        """
        if designId is None:
            raise ValueError("Missing required parameter 'designId'")
        url = f"{self.base_url}/v1/designs/{designId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_design_import_job(self, request_body=None) -> dict[str, Any]:
        """
        Initiates a job to import a file (e.g., PDF, PPTX) for creating a new Canva design. This function sends a POST request to the `/v1/imports` endpoint and returns details of the created import job, including a job ID for status tracking.

        Args:
            request_body (dict | None): Optional dictionary for arbitrary request body data.

        Returns:
            dict[str, Any]: OK

        Tags:
            design_import
        """
        url = f"{self.base_url}/v1/imports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_design_import_status(self, jobId) -> dict[str, Any]:
        """
        Retrieves the status and results of a specific design import job using its unique `jobId`. This function checks the outcome of an import process initiated by the `v1_imports` method, returning details about the job's progress and final state.

        Args:
            jobId (string): jobId

        Returns:
            dict[str, Any]: OK

        Tags:
            design_import
        """
        if jobId is None:
            raise ValueError("Missing required parameter 'jobId'")
        url = f"{self.base_url}/v1/imports/{jobId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_design_export(self, design_id=None, format=None) -> dict[str, Any]:
        """
        Initiates an export job for a specified design based on its ID and format details (e.g., file type, quality). It returns the export job's details, including an ID used to track its status with `v1_exports_exportid`.

        Args:
            design_id (string): design_id Example: '<string>'.
            format (object): format
                Example:
                ```json
                {
                  "design_id": "<string>",
                  "format": {
                    "export_quality": "regular",
                    "pages": [
                      "<integer>",
                      "<integer>"
                    ],
                    "size": "letter",
                    "type": "pdf"
                  }
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            export
        """
        request_body = {
            "design_id": design_id,
            "format": format,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/exports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_export_job_status(self, exportId) -> dict[str, Any]:
        """
        Retrieves the status and results of a specific design export job using its unique ID. This is used to check on an export initiated by the `v1_exports` function and to obtain download links for the completed file.

        Args:
            exportId (string): exportId

        Returns:
            dict[str, Any]: OK

        Tags:
            export
        """
        if exportId is None:
            raise ValueError("Missing required parameter 'exportId'")
        url = f"{self.base_url}/v1/exports/{exportId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_folder_by_id(self, folderId) -> dict[str, Any]:
        """
        Retrieves detailed information for a specific folder using its unique ID. This GET operation fetches folder metadata, distinguishing it from functions that delete (`v1_folders_folderid`) or update (`v1_folders_folderid2`) the same folder resource.

        Args:
            folderId (string): folderId

        Returns:
            dict[str, Any]: OK

        Tags:
            folder
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        url = f"{self.base_url}/v1/folders/{folderId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_folder(self, folderId) -> Any:
        """
        Deletes a folder and all its contents using the folder's unique identifier. This function sends an HTTP DELETE request to the `/v1/folders/{folderId}` endpoint and returns a confirmation status upon successful deletion.

        Args:
            folderId (string): folderId

        Returns:
            Any: OK

        Tags:
            folder
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        url = f"{self.base_url}/v1/folders/{folderId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_folder(self, folderId, name=None) -> dict[str, Any]:
        """
        Updates a specific folder's properties, such as its name, using its unique ID. This function sends a PATCH request to the `/v1/folders/{folderId}` endpoint to apply partial modifications and returns the updated folder information upon success.

        Args:
            folderId (string): folderId
            name (string): name
                Example:
                ```json
                {
                  "name": "<string>"
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            folder
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/folders/{folderId}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_folder_items(
        self, folderId, continuation=None, item_types=None
    ) -> dict[str, Any]:
        """
        Lists items within a specific folder. Supports optional filtering by item type (asset, design, folder, template) and pagination using a continuation token to navigate through large result sets.

        Args:
            folderId (string): folderId
            continuation (string): If the success response contains a continuation token, the folder contains more items
        you can list. You can use this token as a query parameter and retrieve more
        items from the list, for example
        `/v1/folders/{folderId}/items?continuation={continuation}`. To retrieve all the items in a folder, you might need to make multiple requests. Example: '<string>'.
            item_types (string): Filter the folder items to only return specified types. The available types are:
        `asset`, `design`, `folder`, and `template`. To filter for more than one item type,
        provide a comma-delimited list. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            folder
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        url = f"{self.base_url}/v1/folders/{folderId}/items"
        query_params = {
            k: v
            for k, v in [("continuation", continuation), ("item_types", item_types)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def move_folder_item(
        self, from_folder_id=None, item_id=None, to_folder_id=None
    ) -> Any:
        """
        Moves an item, such as a design or another folder, from a source folder to a destination folder. It requires the unique IDs for the item, the source folder, and the target folder to perform the relocation, returning a status confirmation upon completion.

        Args:
            from_folder_id (string): from_folder_id Example: '<string>'.
            item_id (string): item_id Example: '<string>'.
            to_folder_id (string): to_folder_id
                Example:
                ```json
                {
                  "from_folder_id": "<string>",
                  "item_id": "<string>",
                  "to_folder_id": "<string>"
                }
                ```

        Returns:
            Any: OK

        Tags:
            folder
        """
        request_body = {
            "from_folder_id": from_folder_id,
            "item_id": item_id,
            "to_folder_id": to_folder_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/folders/move"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_folder(self, name=None, parent_folder_id=None) -> dict[str, Any]:
        """
        Creates a new folder, optionally assigning it a name and placing it within a specified parent folder. This function is distinct from others as it uses a POST request to the base `/v1/folders` endpoint, specifically for creation.

        Args:
            name (string): name Example: '<string>'.
            parent_folder_id (string): parent_folder_id
                Example:
                ```json
                {
                  "name": "<string>",
                  "parent_folder_id": "<string>"
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            folder
        """
        request_body = {
            "name": name,
            "parent_folder_id": parent_folder_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/folders"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_current_user(self) -> dict[str, Any]:
        """
        Retrieves core information for the currently authenticated user, such as ID and team details. This function is distinct from `v1_users_me_profile`, which fetches more specific profile data like the user's display name and profile picture.

        Returns:
            dict[str, Any]: OK

        Tags:
            user, important
        """
        url = f"{self.base_url}/v1/users/me"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_current_user_profile(self) -> dict[str, Any]:
        """
        Fetches detailed profile information for the currently authenticated user. This method is distinct from `v1_users_me`, which retrieves general user account information rather than specific profile details like display name or avatar.

        Returns:
            dict[str, Any]: OK

        Tags:
            user
        """
        url = f"{self.base_url}/v1/users/me/profile"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_app_jwks,
            self.get_asset,
            self.post_update_asset,
            self.delete_asset,
            self.patch_asset,
            self.upload_asset,
            self.create_asset_upload_job,
            self.get_asset_upload_job_status,
            self.create_autofill_job,
            self.get_autofill_job_status,
            self.list_brand_templates,
            self.get_brand_template_by_id,
            self.get_brand_template_dataset,
            self.create_comment,
            self.create_comment_reply,
            self.get_design_comment,
            self.get_connection_keys,
            self.list_designs,
            self.create_design,
            self.get_design,
            self.create_design_import_job,
            self.get_design_import_status,
            self.create_design_export,
            self.get_export_job_status,
            self.get_folder_by_id,
            self.delete_folder,
            self.update_folder,
            self.list_folder_items,
            self.move_folder_item,
            self.create_folder,
            self.get_current_user,
            self.get_current_user_profile,
        ]
