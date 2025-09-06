from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class CanvaApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="canva", integration=integration, **kwargs)
        self.base_url = "https://api.canva.com/rest"

    def v1_apps_appid_jwks(self, appId) -> dict[str, Any]:
        """
        Retrieves the JSON Web Key Set (JWKS) containing public keys for verifying JWTs associated with the specified application.

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

    def v1_assets_assetid1(self, assetId) -> dict[str, Any]:
        """
        Retrieves the details of a specific asset using the provided assetId and returns the asset data.

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

    def v1_assets_assetid3(self, assetId, name=None, tags=None) -> dict[str, Any]:
        """
        Updates an asset using the "POST" method at the "/v1/assets/{assetId}" endpoint and returns a status message.

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

    def v1_assets_assetid(self, assetId) -> Any:
        """
        Deletes an asset by its unique identifier and returns a success status upon completion.

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

    def v1_assets_assetid2(self, assetId, name=None, tags=None) -> dict[str, Any]:
        """
        Updates specific properties of an asset identified by its ID and returns the operation status.

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

    def v1_assets_upload(self, request_body=None) -> dict[str, Any]:
        """
        Uploads an asset with provided metadata to the server and returns a success or error status.

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

    def v1_asset_uploads(self, request_body=None) -> dict[str, Any]:
        """
        Initiates an asset upload using the "POST" method at the "/v1/asset-uploads" path, accepting asset metadata in the header and handling responses for successful and failed uploads.

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

    def v1_asset_uploads_jobid(self, jobId) -> dict[str, Any]:
        """
        Retrieves the status and results of an asset upload job identified by the job ID.

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

    def v1_autofills(
        self, brand_template_id=None, data=None, preview=None, title=None
    ) -> dict[str, Any]:
        """
        Triggers an autofill operation using the API at the "/v1/autofills" path, sending data via the POST method, and returns a response indicating success or failure.

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

    def v1_autofills_jobid(self, jobId) -> dict[str, Any]:
        """
        Retrieves autofill data for a job identified by the specified jobId using the GET method at the "/v1/autofills/{jobId}" endpoint.

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

    def v1_brand_templates(
        self, query=None, continuation=None, ownership=None, sort_by=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of brand templates based on query parameters such as ownership and sorting options using the "GET" method at the "/v1/brand-templates" path.

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

    def v1_brand_templates_brandtemplateid(self, brandTemplateId) -> dict[str, Any]:
        """
        Retrieves metadata for a specific brand template using its unique identifier.

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

    def v1_brand_templates_brandtemplateid_dataset(
        self, brandTemplateId
    ) -> dict[str, Any]:
        """
        Retrieves the dataset definition of a brand template, including data field names and types, allowing for the identification of autofillable fields.

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

    def v1_comments(
        self, assignee_id=None, attached_to=None, message=None
    ) -> dict[str, Any]:
        """
        Creates a new comment and returns a status message.

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

    def v1_comments_commentid_replies(
        self, commentId, attached_to=None, message=None
    ) -> dict[str, Any]:
        """
        Creates a new reply to a comment using the "POST" method.

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

    def v1_designs_designid_comments_commentid(
        self, designId, commentId
    ) -> dict[str, Any]:
        """
        Retrieves a specific comment from a design using the provided design ID and comment ID.

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

    def v1_connect_keys(self) -> dict[str, Any]:
        """
        Retrieves a list of connection keys associated with the current user or application.

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

    def v1_designs(
        self, query=None, continuation=None, ownership=None, sort_by=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of designs based on query parameters, including query, continuation, ownership, and sort order, using the GET method at the "/v1/designs" endpoint.

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

    def v1_designs1(
        self, asset_id=None, design_type=None, title=None
    ) -> dict[str, Any]:
        """
        Creates a new design resource and returns the result of the operation.

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

    def v1_designs_designid(self, designId) -> dict[str, Any]:
        """
        Retrieves a specific design by its ID using the GET method at the "/v1/designs/{designId}" endpoint.

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

    def v1_imports(self, request_body=None) -> dict[str, Any]:
        """
        Initiates a data import process with the provided metadata in the request header and returns an appropriate response.

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

    def v1_imports_jobid(self, jobId) -> dict[str, Any]:
        """
        Retrieves the status and details of a specific import job identified by its job ID.

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

    def v1_exports(self, design_id=None, format=None) -> dict[str, Any]:
        """
        Initiates an export process through the API and returns status codes for success or failure.

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

    def v1_exports_exportid(self, exportId) -> dict[str, Any]:
        """
        Retrieves export details by ID using the "GET" method at the path "/v1/exports/{exportId}" and returns a response.

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

    def v1_folders_folderid1(self, folderId) -> dict[str, Any]:
        """
        Retrieves information about a folder with the specified ID using the "GET" method at the "/v1/folders/{folderId}" endpoint.

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

    def v1_folders_folderid(self, folderId) -> Any:
        """
        Deletes a folder with the specified ID, including all of its contents, using the DELETE method and returns a status code indicating success or failure.

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

    def v1_folders_folderid2(self, folderId, name=None) -> dict[str, Any]:
        """
        Updates an existing folder using the specified `folderId` and returns a status message upon successful modification.

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

    def v1_folders_folderid_items(
        self, folderId, continuation=None, item_types=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of items within a specified folder, filtered by type, using continuation tokens for pagination.

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

    def v1_folders_move(
        self, from_folder_id=None, item_id=None, to_folder_id=None
    ) -> Any:
        """
        Moves folders to a new location using the "POST" method at the "/v1/folders/move" endpoint and returns status messages based on the operation's success or failure.

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

    def v1_folders(self, name=None, parent_folder_id=None) -> dict[str, Any]:
        """
        Creates a new folder in the system and returns a success or error status.

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

    def v1_users_me(self) -> dict[str, Any]:
        """
        Retrieves information about the currently authenticated user using the GET method at the "/v1/users/me" endpoint.

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

    def v1_users_me_profile(self) -> dict[str, Any]:
        """
        Retrieves the authenticated user's profile information.

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
            self.v1_apps_appid_jwks,
            self.v1_assets_assetid1,
            self.v1_assets_assetid3,
            self.v1_assets_assetid,
            self.v1_assets_assetid2,
            self.v1_assets_upload,
            self.v1_asset_uploads,
            self.v1_asset_uploads_jobid,
            self.v1_autofills,
            self.v1_autofills_jobid,
            self.v1_brand_templates,
            self.v1_brand_templates_brandtemplateid,
            self.v1_brand_templates_brandtemplateid_dataset,
            self.v1_comments,
            self.v1_comments_commentid_replies,
            self.v1_designs_designid_comments_commentid,
            self.v1_connect_keys,
            self.v1_designs,
            self.v1_designs1,
            self.v1_designs_designid,
            self.v1_imports,
            self.v1_imports_jobid,
            self.v1_exports,
            self.v1_exports_exportid,
            self.v1_folders_folderid1,
            self.v1_folders_folderid,
            self.v1_folders_folderid2,
            self.v1_folders_folderid_items,
            self.v1_folders_move,
            self.v1_folders,
            self.v1_users_me,
            self.v1_users_me_profile,
        ]
