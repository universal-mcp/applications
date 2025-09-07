from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class BoxApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="box", integration=integration, **kwargs)
        self.base_url = "https://api.box.com/2.0"

    def get_authorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: str | None = None,
        state: str | None = None,
        scope: str | None = None,
    ) -> Any:
        """
        Authorize user

        Args:
            response_type (string): The type of response we'd like to receive. Example: 'code'.
            client_id (string): The Client ID of the application that is requesting to authenticate
        the user. To get the Client ID for your application, log in to your
        Box developer console and click the **Edit Application** link for
        the application you're working with. In the OAuth 2.0 Parameters section
        of the configuration page, find the item labelled `client_id`. The
        text of that item is your application's Client ID. Example: 'ly1nj6n11vionaie65emwzk575hnnmrk'.
            redirect_uri (string): The URI to which Box redirects the browser after the user has granted
        or denied the application permission. This URI match one of the redirect
        URIs in the configuration of your application. It must be a
        valid HTTPS URI and it needs to be able to handle the redirection to
        complete the next step in the OAuth 2.0 flow.
        Although this parameter is optional, it must be a part of the
        authorization URL if you configured multiple redirect URIs
        for the application in the developer console. A missing parameter causes
        a `redirect_uri_missing` error after the user grants application access. Example: 'http://example.com/auth/callback'.
            state (string): A custom string of your choice. Box will pass the same string to
        the redirect URL when authentication is complete. This parameter
        can be used to identify a user on redirect, as well as protect
        against hijacked sessions and other exploits. Example: 'my_state'.
            scope (string): A space-separated list of application scopes you'd like to
        authenticate the user for. This defaults to all the scopes configured
        for the application in its configuration page. Example: 'admin_readwrite'.

        Returns:
            Any: Does not return any data, but rather should be used in the browser.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Authorization, important
        """
        url = f"{self.base_url}/authorize"
        query_params = {
            k: v
            for k, v in [
                ("response_type", response_type),
                ("client_id", client_id),
                ("redirect_uri", redirect_uri),
                ("state", state),
                ("scope", scope),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_oauth_token(
        self,
        grant_type: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        refresh_token: str | None = None,
        assertion: str | None = None,
        subject_token: str | None = None,
        subject_token_type: str | None = None,
        actor_token: str | None = None,
        actor_token_type: str | None = None,
        scope: str | None = None,
        resource: str | None = None,
        box_subject_type: str | None = None,
        box_subject_id: str | None = None,
        box_shared_link: str | None = None,
    ) -> dict[str, Any]:
        """
        Request access token

        Args:
            grant_type (string): The type of request being made, either using a client-side obtained
        authorization code, a refresh token, a JWT assertion, client credentials
        grant or another access token for the purpose of downscoping a token. Example: 'authorization_code'.
            client_id (string): The Client ID of the application requesting an access token.

        Used in combination with `authorization_code`, `client_credentials`, or
        `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`. Example: 'ly1nj6n11vionaie65emwzk575hnnmrk'.
            client_secret (string): The client secret of the application requesting an access token.

        Used in combination with `authorization_code`, `client_credentials`, or
        `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`. Example: 'hOzsTeFlT6ko0dme22uGbQal04SBPYc1'.
            code (string): The client-side authorization code passed to your application by
        Box in the browser redirect after the user has successfully
        granted your application permission to make API calls on their
        behalf.

        Used in combination with `authorization_code` as the `grant_type`. Example: 'n22JPxrh18m4Y0wIZPIqYZK7VRrsMTWW'.
            refresh_token (string): A refresh token used to get a new access token with.

        Used in combination with `refresh_token` as the `grant_type`. Example: 'c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ'.
            assertion (string): A JWT assertion for which to request a new access token.

        Used in combination with `urn:ietf:params:oauth:grant-type:jwt-bearer`
        as the `grant_type`. Example: 'xxxxx.yyyyy.zzzzz'.
            subject_token (string): The token to exchange for a downscoped token. This can be a regular
        access token, a JWT assertion, or an app token.

        Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
        as the `grant_type`. Example: 'c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ'.
            subject_token_type (string): The type of `subject_token` passed in.

        Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
        as the `grant_type`. Example: 'urn:ietf:params:oauth:token-type:access_token'.
            actor_token (string): The token used to create an annotator token.
        This is a JWT assertion.

        Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
        as the `grant_type`. Example: 'c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ'.
            actor_token_type (string): The type of `actor_token` passed in.

        Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
        as the `grant_type`. Example: 'urn:ietf:params:oauth:token-type:id_token'.
            scope (string): The space-delimited list of scopes that you want apply to the
        new access token.

        The `subject_token` will need to have all of these scopes or
        the call will error with **401 Unauthorized**. Example: 'item_upload item_preview base_explorer'.
            resource (string): Full URL for the file that the token should be generated for. Example: 'https://api.box.com/2.0/files/123456'.
            box_subject_type (string): Used in combination with `client_credentials` as the `grant_type`. Example: 'enterprise'.
            box_subject_id (string): Used in combination with `client_credentials` as the `grant_type`.
        Value is determined by `box_subject_type`. If `user` use user ID and if
        `enterprise` use enterprise ID. Example: '123456789'.
            box_shared_link (string): Full URL of the shared link on the file or folder
        that the token should be generated for. Example: 'https://cloud.box.com/s/123456'.

        Returns:
            dict[str, Any]: Returns a new Access Token that can be used to make authenticated
        API calls by passing along the token in a authorization header as
        follows `Authorization: Bearer <Token>`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Authorization
        """
        request_body_data = None
        request_body_data = {
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "refresh_token": refresh_token,
            "assertion": assertion,
            "subject_token": subject_token,
            "subject_token_type": subject_token_type,
            "actor_token": actor_token,
            "actor_token_type": actor_token_type,
            "scope": scope,
            "resource": resource,
            "box_subject_type": box_subject_type,
            "box_subject_id": box_subject_id,
            "box_shared_link": box_shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/oauth2/token"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/x-www-form-urlencoded",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_oauth_token_refresh(
        self,
        grant_type: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        refresh_token: str | None = None,
    ) -> dict[str, Any]:
        """
        Refresh access token

        Args:
            grant_type (string): The type of request being made, in this case a refresh request. Example: 'refresh_token'.
            client_id (string): The client ID of the application requesting to refresh the token. Example: 'ly1nj6n11vionaie65emwzk575hnnmrk'.
            client_secret (string): The client secret of the application requesting to refresh the token. Example: 'hOzsTeFlT6ko0dme22uGbQal04SBPYc1'.
            refresh_token (string): The refresh token to refresh. Example: 'c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ'.

        Returns:
            dict[str, Any]: Returns a new Access Token that can be used to make authenticated
        API calls by passing along the token in a authorization header as
        follows `Authorization: Bearer <Token>`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Authorization
        """
        request_body_data = None
        request_body_data = {
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/oauth2/token#refresh"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/x-www-form-urlencoded",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_oauth_revoke(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        token: str | None = None,
    ) -> Any:
        """
        Revoke access token

        Args:
            client_id (string): The Client ID of the application requesting to revoke the
        access token. Example: 'ly1nj6n11vionaie65emwzk575hnnmrk'.
            client_secret (string): The client secret of the application requesting to revoke
        an access token. Example: 'hOzsTeFlT6ko0dme22uGbQal04SBPYc1'.
            token (string): The access token to revoke. Example: 'n22JPxrh18m4Y0wIZPIqYZK7VRrsMTWW'.

        Returns:
            Any: Returns an empty response when the token was successfully revoked.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Authorization
        """
        request_body_data = None
        request_body_data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "token": token,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/oauth2/revoke"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/x-www-form-urlencoded",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id(
        self, file_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get file information

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested.

        Additionally this field can be used to query any metadata
        applied to the file by specifying the `metadata` field as well
        as the scope and key of the template to retrieve, for example
        `?fields=metadata.enterprise_12345.contractTemplate`. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a file object.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_files_id(
        self,
        file_id: str,
        fields: list[str] | None = None,
        name: str | None = None,
        parent: Any | None = None,
    ) -> dict[str, Any]:
        """
        Restore file

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): An optional new name for the file. Example: 'Restored.docx'.
            parent (string): parent

        Returns:
            dict[str, Any]: Returns a file object when the file has been restored.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "parent": parent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_files_id(
        self,
        file_id: str,
        fields: list[str] | None = None,
        name: str | None = None,
        description: str | None = None,
        parent: Any | None = None,
        shared_link: Any | None = None,
        lock: dict[str, Any] | None = None,
        disposition_at: str | None = None,
        permissions: dict[str, Any] | None = None,
        collections: list[dict[str, Any]] | None = None,
        tags: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Update file

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): An optional different name for the file. This can be used to
        rename the file.

        File names must be unique within their parent folder. The name check is case-insensitive, so a file
        named `New File` cannot be created in a parent folder that already contains a folder named `new file`. Example: 'NewFile.txt'.
            description (string): The description for a file. This can be seen in the right-hand sidebar panel
        when viewing a file in the Box web app. Additionally, this index is used in
        the search index of the file, allowing users to find the file by the content
        in the description. Example: 'The latest reports. Automatically updated'.
            parent (string): parent
            shared_link (string): shared_link
            lock (object): Defines a lock on an item. This prevents the item from being
        moved, renamed, or otherwise changed by anyone other than the user
        who created the lock.

        Set this to `null` to remove the lock.
            disposition_at (string): The retention expiration timestamp for the given file. This
        date cannot be shortened once set on a file. Example: '2012-12-12T10:53:43-08:00'.
            permissions (object): Defines who can download a file.
            collections (array): An array of collections to make this file
        a member of. Currently
        we only support the `favorites` collection.

        To get the ID for a collection, use the
        [List all collections][1] endpoint.

        Passing an empty array `[]` or `null` will remove
        the file from all collections.

        [1]: e://get-collections
            tags (array): The tags for this item. These tags are shown in
        the Box web app and mobile apps next to an item.

        To add or remove a tag, retrieve the item's current tags,
        modify them, and then update this field.

        There is a limit of 100 tags per item, and 10,000
        unique tags per enterprise. Example: "['approved']".

        Returns:
            dict[str, Any]: Returns a file object.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "parent": parent,
            "shared_link": shared_link,
            "lock": lock,
            "disposition_at": disposition_at,
            "permissions": permissions,
            "collections": collections,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_files_id(self, file_id: str) -> Any:
        """
        Delete file

        Args:
            file_id (string): file_id

        Returns:
            Any: Returns an empty response when the file has been successfully
        deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_file_associations(
        self,
        file_id: str,
        limit: int | None = None,
        marker: str | None = None,
        application_type: str | None = None,
    ) -> dict[str, Any]:
        """
        List file app item associations

        Args:
            file_id (string): file_id
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            application_type (string): If given, only return app items for this application type Example: 'hubs'.

        Returns:
            dict[str, Any]: Returns a collection of app item objects. If there are no
        app items on this file, an empty collection will be returned.
        This list includes app items on ancestors of this File.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            App item associations
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/app_item_associations"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("marker", marker),
                ("application_type", application_type),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_content(
        self,
        file_id: str,
        version: str | None = None,
        access_token: str | None = None,
    ) -> Any:
        """
        Download file

        Args:
            file_id (string): file_id
            version (string): The file version to download Example: '4'.
            access_token (string): An optional access token that can be used to pre-authenticate this request, which means that a download link can be shared with a browser or a third party service without them needing to know how to handle the authentication.
        When using this parameter, please make sure that the access token is sufficiently scoped down to only allow read access to that file and no other files or folders. Example: 'c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ'.

        Returns:
            Any: Returns the requested file if the client has the **follow
        redirects** setting enabled to automatically
        follow HTTP `3xx` responses as redirects. If not, the request
        will return `302` instead.
        For details, see
        the [download file guide](g://downloads/file#download-url).

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Downloads
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/content"
        query_params = {
            k: v
            for k, v in [("version", version), ("access_token", access_token)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_files_id_content(
        self,
        file_id: str,
        fields: list[str] | None = None,
        attributes: dict[str, Any] | None = None,
        file: bytes | None = None,
    ) -> dict[str, Any]:
        """
        Upload file version

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            attributes (object): The additional attributes of the file being uploaded. Mainly the
        name and the parent folder. These attributes are part of the multi
        part request body and are in JSON format.

        <Message warning>

          The `attributes` part of the body must come **before** the
          `file` part. Requests that do not follow this format when
          uploading the file will receive a HTTP `400` error with a
          `metadata_after_file_contents` error code.

        </Message>
            file (file (e.g., open('path/to/file', 'rb'))): The content of the file to upload to Box.

        <Message warning>

          The `attributes` part of the body must come **before** the
          `file` part. Requests that do not follow this format when
          uploading the file will receive a HTTP `400` error with a
          `metadata_after_file_contents` error code.

        </Message>

        Returns:
            dict[str, Any]: Returns the new file object in a list.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        files_data = None
        request_body_data = {}
        files_data = {}
        if attributes is not None:
            request_body_data["attributes"] = attributes
        if file is not None:
            files_data["file"] = file
        files_data = {k: v for k, v in files_data.items() if v is not None}
        if not files_data:
            files_data = None
        url = f"{self.base_url}/files/{file_id}/content"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            files=files_data,
            params=query_params,
            content_type="multipart/form-data",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def options_files_content(
        self,
        name: str | None = None,
        size: int | None = None,
        parent: Any | None = None,
    ) -> dict[str, Any]:
        """
        Preflight check before upload

        Args:
            name (string): The name for the file Example: 'File.mp4'.
            size (integer): The size of the file in bytes Example: '1024'.
            parent (string): parent

        Returns:
            dict[str, Any]: If the check passed, the response will include a session URL that
        can be used to upload the file to.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "size": size,
            "parent": parent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/content"
        query_params = {}
        response = self._options(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_files_content(
        self,
        fields: list[str] | None = None,
        attributes: dict[str, Any] | None = None,
        file: bytes | None = None,
    ) -> dict[str, Any]:
        """
        Upload file

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            attributes (object): The additional attributes of the file being uploaded. Mainly the
        name and the parent folder. These attributes are part of the multi
        part request body and are in JSON format.

        <Message warning>

          The `attributes` part of the body must come **before** the
          `file` part. Requests that do not follow this format when
          uploading the file will receive a HTTP `400` error with a
          `metadata_after_file_contents` error code.

        </Message>
            file (file (e.g., open('path/to/file', 'rb'))): The content of the file to upload to Box.

        <Message warning>

          The `attributes` part of the body must come **before** the
          `file` part. Requests that do not follow this format when
          uploading the file will receive a HTTP `400` error with a
          `metadata_after_file_contents` error code.

        </Message>

        Returns:
            dict[str, Any]: Returns the new file object in a list.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads
        """
        request_body_data = None
        files_data = None
        request_body_data = {}
        files_data = {}
        if attributes is not None:
            request_body_data["attributes"] = attributes
        if file is not None:
            files_data["file"] = file
        files_data = {k: v for k, v in files_data.items() if v is not None}
        if not files_data:
            files_data = None
        url = f"{self.base_url}/files/content"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            files=files_data,
            params=query_params,
            content_type="multipart/form-data",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_files_upload_sessions(
        self,
        folder_id: str | None = None,
        file_size: int | None = None,
        file_name: str | None = None,
    ) -> dict[str, Any]:
        """
        Create upload session

        Args:
            folder_id (string): The ID of the folder to upload the new file to. Example: '0'.
            file_size (integer): The total number of bytes of the file to be uploaded Example: '104857600'.
            file_name (string): The name of new file Example: 'Project.mov'.

        Returns:
            dict[str, Any]: Returns a new upload session.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads (Chunked)
        """
        request_body_data = None
        request_body_data = {
            "folder_id": folder_id,
            "file_size": file_size,
            "file_name": file_name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/upload_sessions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_files_id_upload_sessions(
        self,
        file_id: str,
        file_size: int | None = None,
        file_name: str | None = None,
    ) -> dict[str, Any]:
        """
        Create upload session for existing file

        Args:
            file_id (string): file_id
            file_size (integer): The total number of bytes of the file to be uploaded Example: '104857600'.
            file_name (string): The optional new name of new file Example: 'Project.mov'.

        Returns:
            dict[str, Any]: Returns a new upload session.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads (Chunked)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "file_size": file_size,
            "file_name": file_name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}/upload_sessions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_upload_sessions_id(self, upload_session_id: str) -> dict[str, Any]:
        """
        Get upload session

        Args:
            upload_session_id (string): upload_session_id

        Returns:
            dict[str, Any]: Returns an upload session object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads (Chunked)
        """
        if upload_session_id is None:
            raise ValueError("Missing required parameter 'upload_session_id'.")
        url = f"{self.base_url}/files/upload_sessions/{upload_session_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_files_upload_sessions_id(
        self, upload_session_id: str, body_content: bytes | None = None
    ) -> dict[str, Any]:
        """
        Upload part of file

        Args:
            upload_session_id (string): upload_session_id
            body_content (bytes | None): Raw binary content for the request body.

        Returns:
            dict[str, Any]: Chunk has been uploaded successfully.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads (Chunked)
        """
        if upload_session_id is None:
            raise ValueError("Missing required parameter 'upload_session_id'.")
        request_body_data = None
        request_body_data = body_content
        url = f"{self.base_url}/files/upload_sessions/{upload_session_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/octet-stream",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_upload_session_by_id(self, upload_session_id: str) -> Any:
        """
        Remove upload session

        Args:
            upload_session_id (string): upload_session_id

        Returns:
            Any: A blank response is returned if the session was
        successfully aborted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads (Chunked)
        """
        if upload_session_id is None:
            raise ValueError("Missing required parameter 'upload_session_id'.")
        url = f"{self.base_url}/files/upload_sessions/{upload_session_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_upload_session_parts(
        self,
        upload_session_id: str,
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List parts

        Args:
            upload_session_id (string): upload_session_id
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list of parts that have been uploaded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads (Chunked)
        """
        if upload_session_id is None:
            raise ValueError("Missing required parameter 'upload_session_id'.")
        url = f"{self.base_url}/files/upload_sessions/{upload_session_id}/parts"
        query_params = {
            k: v for k, v in [("offset", offset), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def commit_upload_session(
        self, upload_session_id: str, parts: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Commit upload session

        Args:
            upload_session_id (string): upload_session_id
            parts (array): The list details for the uploaded parts

        Returns:
            dict[str, Any]: Returns the file object in a list.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uploads (Chunked)
        """
        if upload_session_id is None:
            raise ValueError("Missing required parameter 'upload_session_id'.")
        request_body_data = None
        request_body_data = {
            "parts": parts,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/upload_sessions/{upload_session_id}/commit"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_files_id_copy(
        self,
        file_id: str,
        fields: list[str] | None = None,
        name: str | None = None,
        version: str | None = None,
        parent: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        r"""
        Copy file

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): An optional new name for the copied file.

        There are some restrictions to the file name. Names containing
        non-printable ASCII characters, forward and backward slashes
        (`/`, `\`), and protected names like `.` and `..` are
        automatically sanitized by removing the non-allowed
        characters. Example: 'FileCopy.txt'.
            version (string): An optional ID of the specific file version to copy. Example: '0'.
            parent (object): The destination folder to copy the file to.

        Returns:
            dict[str, Any]: Returns a new file object representing the copied file.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "version": version,
            "parent": parent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}/copy"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_thumbnail_id(
        self,
        file_id: str,
        extension: str,
        min_height: int | None = None,
        min_width: int | None = None,
        max_height: int | None = None,
        max_width: int | None = None,
    ) -> Any:
        """
        Get file thumbnail

        Args:
            file_id (string): file_id
            extension (string): extension
            min_height (integer): The minimum height of the thumbnail Example: '32'.
            min_width (integer): The minimum width of the thumbnail Example: '32'.
            max_height (integer): The maximum height of the thumbnail Example: '320'.
            max_width (integer): The maximum width of the thumbnail Example: '320'.

        Returns:
            Any: When a thumbnail can be created the thumbnail data will be
        returned in the body of the response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        if extension is None:
            raise ValueError("Missing required parameter 'extension'.")
        url = f"{self.base_url}/files/{file_id}/thumbnail.{extension}"
        query_params = {
            k: v
            for k, v in [
                ("min_height", min_height),
                ("min_width", min_width),
                ("max_height", max_height),
                ("max_width", max_width),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_collaborations(
        self,
        file_id: str,
        fields: list[str] | None = None,
        limit: int | None = None,
        marker: str | None = None,
    ) -> dict[str, Any]:
        """
        List file collaborations

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.

        Returns:
            dict[str, Any]: Returns a collection of collaboration objects. If there are no
        collaborations on this file an empty collection will be returned.

        This list includes pending collaborations, for which the `status`
        is set to `pending`, indicating invitations that have been sent but not
        yet accepted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collaborations (List)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/collaborations"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("limit", limit), ("marker", marker)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_comments(
        self,
        file_id: str,
        fields: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """
        List file comments

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of comment objects. If there are no
        comments on this file an empty collection will be returned.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/comments"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("limit", limit), ("offset", offset)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_tasks(self, file_id: str) -> dict[str, Any]:
        """
        List tasks on file

        Args:
            file_id (string): file_id

        Returns:
            dict[str, Any]: Returns a list of tasks on a file.

        If there are no tasks on this file an empty collection is returned
        instead.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/tasks"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_trash(
        self, file_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get trashed file

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the file that was trashed,
        including information about when the it
        was moved to the trash.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/trash"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_files_id_trash(self, file_id: str) -> Any:
        """
        Permanently remove file

        Args:
            file_id (string): file_id

        Returns:
            Any: Returns an empty response when the file was
        permanently deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/trash"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_versions(
        self,
        file_id: str,
        fields: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """
        List all file versions

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.

        Returns:
            dict[str, Any]: Returns an array of past versions for this file.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File versions
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/versions"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("limit", limit), ("offset", offset)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_versions_id(
        self, file_id: str, file_version_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get file version

        Args:
            file_id (string): file_id
            file_version_id (string): file_version_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a specific version of a file.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File versions
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        if file_version_id is None:
            raise ValueError("Missing required parameter 'file_version_id'.")
        url = f"{self.base_url}/files/{file_id}/versions/{file_version_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_files_id_versions_id(self, file_id: str, file_version_id: str) -> Any:
        """
        Remove file version

        Args:
            file_id (string): file_id
            file_version_id (string): file_version_id

        Returns:
            Any: Returns an empty response when the file has been successfully
        deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File versions
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        if file_version_id is None:
            raise ValueError("Missing required parameter 'file_version_id'.")
        url = f"{self.base_url}/files/{file_id}/versions/{file_version_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_files_id_versions_id(
        self, file_id: str, file_version_id: str, trashed_at: str | None = None
    ) -> dict[str, Any]:
        """
        Restore file version

        Args:
            file_id (string): file_id
            file_version_id (string): file_version_id
            trashed_at (string): Set this to `null` to clear
        the date and restore the file.

        Returns:
            dict[str, Any]: Returns a restored file version object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File versions
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        if file_version_id is None:
            raise ValueError("Missing required parameter 'file_version_id'.")
        request_body_data = None
        request_body_data = {
            "trashed_at": trashed_at,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}/versions/{file_version_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_files_id_versions_current(
        self,
        file_id: str,
        fields: list[str] | None = None,
        id: str | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        """
        Promote file version

        Args:
            file_id (string): file_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            id (string): The file version ID Example: '11446498'.
            type (string): The type to promote Example: 'file_version'.

        Returns:
            dict[str, Any]: Returns a newly created file version object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File versions
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "type": type,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}/versions/current"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_metadata(self, file_id: str) -> dict[str, Any]:
        """
        List metadata instances on file

        Args:
            file_id (string): file_id

        Returns:
            dict[str, Any]: Returns all the metadata associated with a file.

        This API does not support pagination and will therefore always return
        all of the metadata associated to the file.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/metadata"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_file_security_classification_by_id(self, file_id: str) -> dict[str, Any]:
        """
        Get classification on file

        Args:
            file_id (string): file_id

        Returns:
            dict[str, Any]: Returns an instance of the `securityClassification` metadata
        template, which contains a `Box__Security__Classification__Key`
        field that lists all the classifications available to this
        enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications on files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_file_security_classification(
        self, file_id: str, Box__Security__Classification__Key: str | None = None
    ) -> dict[str, Any]:
        """
        Add classification to file

        Args:
            file_id (string): file_id
            Box__Security__Classification__Key (string): The name of the classification to apply to this file.

        To list the available classifications in an enterprise,
        use the classification API to retrieve the
        [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
        which lists all available classification keys. Example: 'Sensitive'.

        Returns:
            dict[str, Any]: Returns the classification template instance
        that was applied to the file.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications on files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "Box__Security__Classification__Key": Box__Security__Classification__Key,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_update_file_security_classification(
        self, file_id: str, items: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Update classification on file

        Args:
            file_id (string): file_id

        Returns:
            dict[str, Any]: Returns the updated classification metadata template instance.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications on files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json-patch+json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_file_metadata(self, file_id: str) -> Any:
        """
        Remove classification from file

        Args:
            file_id (string): file_id

        Returns:
            Any: Returns an empty response when the classification is
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications on files
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_metadata_id_id(
        self, file_id: str, scope: str, template_key: str
    ) -> dict[str, Any]:
        """
        Get metadata instance on file

        Args:
            file_id (string): file_id
            scope (string): scope
            template_key (string): template_key

        Returns:
            dict[str, Any]: An instance of the metadata template that includes
        additional "key:value" pairs defined by the user or
        an application.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        url = f"{self.base_url}/files/{file_id}/metadata/{scope}/{template_key}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_files_id_metadata_id_id(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        request_body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create metadata instance on file

        Args:
            file_id (string): file_id
            scope (string): scope
            template_key (string): template_key
            request_body (dict | None): Optional dictionary for an empty JSON request body (e.g., {}).

        Returns:
            dict[str, Any]: Returns the instance of the template that was applied to the file,
        including the data that was applied to the template.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        request_body_data = None
        request_body_data = request_body if request_body is not None else {}
        url = f"{self.base_url}/files/{file_id}/metadata/{scope}/{template_key}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_files_id_metadata_id_id(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        items: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Update metadata instance on file

        Args:
            file_id (string): file_id
            scope (string): scope
            template_key (string): template_key

        Returns:
            dict[str, Any]: Returns the updated metadata template instance, with the
        custom template data included.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/files/{file_id}/metadata/{scope}/{template_key}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json-patch+json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_files_id_metadata_id_id(
        self, file_id: str, scope: str, template_key: str
    ) -> Any:
        """
        Remove metadata instance from file

        Args:
            file_id (string): file_id
            scope (string): scope
            template_key (string): template_key

        Returns:
            Any: Returns an empty response when the metadata is
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        url = f"{self.base_url}/files/{file_id}/metadata/{scope}/{template_key}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_global_metadata(self, file_id: str) -> dict[str, Any]:
        """
        List Box Skill cards on file

        Args:
            file_id (string): file_id

        Returns:
            dict[str, Any]: Returns all the metadata associated with a file.

        This API does not support pagination and will therefore always return
        all of the metadata associated to the file.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Skills
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/metadata/global/boxSkillsCards"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_file_metadata_global_box_skills_cards(
        self, file_id: str, cards: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        Create Box Skill cards on file

        Args:
            file_id (string): file_id
            cards (array): A list of Box Skill cards to apply to this file.

        Returns:
            dict[str, Any]: Returns the instance of the template that was applied to the file,
        including the data that was applied to the template.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Skills
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "cards": cards,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}/metadata/global/boxSkillsCards"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_file_metadata(
        self, file_id: str, items: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Update Box Skill cards on file

        Args:
            file_id (string): file_id

        Returns:
            dict[str, Any]: Returns the updated metadata template, with the
        custom template data included.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Skills
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/files/{file_id}/metadata/global/boxSkillsCards"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json-patch+json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_file_global_box_skills_cards(self, file_id: str) -> Any:
        """
        Remove Box Skill cards from file

        Args:
            file_id (string): file_id

        Returns:
            Any: Returns an empty response when the cards are
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Skills
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/metadata/global/boxSkillsCards"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_watermark(self, file_id: str) -> dict[str, Any]:
        """
        Get watermark on file

        Args:
            file_id (string): file_id

        Returns:
            dict[str, Any]: Returns an object containing information about the
        watermark associated for to this file.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Watermarks (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/watermark"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_files_id_watermark(
        self, file_id: str, watermark: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Apply watermark to file

        Args:
            file_id (string): file_id
            watermark (object): The watermark to imprint on the file

        Returns:
            dict[str, Any]: Returns an updated watermark if a watermark already
        existed on this file.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Watermarks (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "watermark": watermark,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}/watermark"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_files_id_watermark(self, file_id: str) -> Any:
        """
        Remove watermark from file

        Args:
            file_id (string): file_id

        Returns:
            Any: Removes the watermark and returns an empty response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Watermarks (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}/watermark"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_file_requests_id(self, file_request_id: str) -> dict[str, Any]:
        """
        Get file request

        Args:
            file_request_id (string): file_request_id

        Returns:
            dict[str, Any]: Returns a file request object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File requests
        """
        if file_request_id is None:
            raise ValueError("Missing required parameter 'file_request_id'.")
        url = f"{self.base_url}/file_requests/{file_request_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_file_requests_id(
        self,
        file_request_id: str,
        title: str | None = None,
        description: str | None = None,
        status: str | None = None,
        is_email_required: bool | None = None,
        is_description_required: bool | None = None,
        expires_at: str | None = None,
    ) -> dict[str, Any]:
        """
        Update file request

        Args:
            file_request_id (string): file_request_id
            title (string): An optional new title for the file request. This can be
        used to change the title of the file request.

        This will default to the value on the existing file request. Example: 'Please upload required documents'.
            description (string): An optional new description for the file request. This can be
        used to change the description of the file request.

        This will default to the value on the existing file request. Example: 'Please upload required documents'.
            status (string): An optional new status of the file request.

        When the status is set to `inactive`, the file request
        will no longer accept new submissions, and any visitor
        to the file request URL will receive a `HTTP 404` status
        code.

        This will default to the value on the existing file request. Example: 'active'.
            is_email_required (boolean): Whether a file request submitter is required to provide
        their email address.

        When this setting is set to true, the Box UI will show
        an email field on the file request form.

        This will default to the value on the existing file request. Example: 'True'.
            is_description_required (boolean): Whether a file request submitter is required to provide
        a description of the files they are submitting.

        When this setting is set to true, the Box UI will show
        a description field on the file request form.

        This will default to the value on the existing file request. Example: 'True'.
            expires_at (string): The date after which a file request will no longer accept new
        submissions.

        After this date, the `status` will automatically be set to
        `inactive`.

        This will default to the value on the existing file request. Example: '2020-09-28T10:53:43-08:00'.

        Returns:
            dict[str, Any]: Returns the updated file request object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File requests
        """
        if file_request_id is None:
            raise ValueError("Missing required parameter 'file_request_id'.")
        request_body_data = None
        request_body_data = {
            "title": title,
            "description": description,
            "status": status,
            "is_email_required": is_email_required,
            "is_description_required": is_description_required,
            "expires_at": expires_at,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/file_requests/{file_request_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_file_requests_id(self, file_request_id: str) -> Any:
        """
        Delete file request

        Args:
            file_request_id (string): file_request_id

        Returns:
            Any: Returns an empty response when the file request has been successfully
        deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File requests
        """
        if file_request_id is None:
            raise ValueError("Missing required parameter 'file_request_id'.")
        url = f"{self.base_url}/file_requests/{file_request_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_file_requests_id_copy(
        self,
        file_request_id: str,
        title: str | None = None,
        description: str | None = None,
        status: str | None = None,
        is_email_required: bool | None = None,
        is_description_required: bool | None = None,
        expires_at: str | None = None,
        folder: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Copy file request

        Args:
            file_request_id (string): file_request_id
            title (string): An optional new title for the file request. This can be
        used to change the title of the file request.

        This will default to the value on the existing file request. Example: 'Please upload required documents'.
            description (string): An optional new description for the file request. This can be
        used to change the description of the file request.

        This will default to the value on the existing file request. Example: 'Please upload required documents'.
            status (string): An optional new status of the file request.

        When the status is set to `inactive`, the file request
        will no longer accept new submissions, and any visitor
        to the file request URL will receive a `HTTP 404` status
        code.

        This will default to the value on the existing file request. Example: 'active'.
            is_email_required (boolean): Whether a file request submitter is required to provide
        their email address.

        When this setting is set to true, the Box UI will show
        an email field on the file request form.

        This will default to the value on the existing file request. Example: 'True'.
            is_description_required (boolean): Whether a file request submitter is required to provide
        a description of the files they are submitting.

        When this setting is set to true, the Box UI will show
        a description field on the file request form.

        This will default to the value on the existing file request. Example: 'True'.
            expires_at (string): The date after which a file request will no longer accept new
        submissions.

        After this date, the `status` will automatically be set to
        `inactive`.

        This will default to the value on the existing file request. Example: '2020-09-28T10:53:43-08:00'.
            folder (object): The folder to associate the new file request to.

        Returns:
            dict[str, Any]: Returns updated file request object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File requests
        """
        if file_request_id is None:
            raise ValueError("Missing required parameter 'file_request_id'.")
        request_body_data = None
        request_body_data = {
            "title": title,
            "description": description,
            "status": status,
            "is_email_required": is_email_required,
            "is_description_required": is_description_required,
            "expires_at": expires_at,
            "folder": folder,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/file_requests/{file_request_id}/copy"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_id(
        self,
        folder_id: str,
        fields: list[str] | None = None,
        sort: str | None = None,
        direction: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Get folder information

        Args:
            folder_id (string): folder_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested.

        Additionally this field can be used to query any metadata
        applied to the file by specifying the `metadata` field as well
        as the scope and key of the template to retrieve, for example
        `?fields=metadata.enterprise_12345.contractTemplate`. Example: "['id', 'type', 'name']".
            sort (string): Defines the **second** attribute by which items
        are sorted.

        The folder type affects the way the items
        are sorted:

          * **Standard folder**:
          Items are always sorted by
          their `type` first, with
          folders listed before files,
          and files listed
          before web links.

          * **Root folder**:
          This parameter is not supported
          for marker-based pagination
          on the root folder

          (the folder with an `id` of `0`).

          * **Shared folder with parent path
          to the associated folder visible to
          the collaborator**:
          Items are always sorted by
          their `type` first, with
          folders listed before files,
          and files listed
          before web links. Example: 'id'.
            direction (string): The direction to sort results in. This can be either in alphabetical ascending
        (`ASC`) or descending (`DESC`) order. Example: 'ASC'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a folder, including the first 100 entries in the folder.
        If you used query parameters like
        `sort`, `direction`, `offset`, or `limit`
        the *folder items list* will be affected accordingly.

        To fetch more items within the folder, use the
        [Get items in a folder](e://get-folders-id-items)) endpoint.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}"
        query_params = {
            k: v
            for k, v in [
                ("fields", fields),
                ("sort", sort),
                ("direction", direction),
                ("offset", offset),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_folders_id(
        self,
        folder_id: str,
        fields: list[str] | None = None,
        name: str | None = None,
        parent: Any | None = None,
    ) -> dict[str, Any]:
        """
        Restore folder

        Args:
            folder_id (string): folder_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): An optional new name for the folder. Example: 'Restored Photos'.
            parent (string): parent

        Returns:
            dict[str, Any]: Returns a folder object when the folder has been restored.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "parent": parent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders/{folder_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_folders_id(
        self,
        folder_id: str,
        fields: list[str] | None = None,
        name: str | None = None,
        description: str | None = None,
        sync_state: str | None = None,
        can_non_owners_invite: bool | None = None,
        parent: Any | None = None,
        shared_link: Any | None = None,
        folder_upload_email: Any | None = None,
        tags: list[str] | None = None,
        is_collaboration_restricted_to_enterprise: bool | None = None,
        collections: list[dict[str, Any]] | None = None,
        can_non_owners_view_collaborators: bool | None = None,
    ) -> dict[str, Any]:
        r"""
        Update folder

        Args:
            folder_id (string): folder_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): The optional new name for this folder.

        The following restrictions to folder names apply: names containing
        non-printable ASCII characters, forward and backward slashes
        (`/`, `\`), names with trailing spaces, and names `.` and `..` are
        not allowed.

        Folder names must be unique within their parent folder. The name check is case-insensitive,
        so a folder named `New Folder` cannot be created in a parent folder that already contains
        a folder named `new folder`. Example: 'New Folder'.
            description (string): The optional description of this folder Example: 'Legal contracts for the new ACME deal'.
            sync_state (string): Specifies whether a folder should be synced to a
        user's device or not. This is used by Box Sync
        (discontinued) and is not used by Box Drive. Example: 'synced'.
            can_non_owners_invite (boolean): Specifies if users who are not the owner
        of the folder can invite new collaborators to the folder. Example: 'True'.
            parent (string): parent
            shared_link (string): shared_link
            folder_upload_email (string): folder_upload_email
            tags (array): The tags for this item. These tags are shown in
        the Box web app and mobile apps next to an item.

        To add or remove a tag, retrieve the item's current tags,
        modify them, and then update this field.

        There is a limit of 100 tags per item, and 10,000
        unique tags per enterprise. Example: "['approved']".
            is_collaboration_restricted_to_enterprise (boolean): Specifies if new invites to this folder are restricted to users
        within the enterprise. This does not affect existing
        collaborations. Example: 'True'.
            collections (array): An array of collections to make this folder
        a member of. Currently
        we only support the `favorites` collection.

        To get the ID for a collection, use the
        [List all collections][1] endpoint.

        Passing an empty array `[]` or `null` will remove
        the folder from all collections.

        [1]: e://get-collections
            can_non_owners_view_collaborators (boolean): Restricts collaborators who are not the owner of
        this folder from viewing other collaborations on
        this folder.

        It also restricts non-owners from inviting new
        collaborators.

        When setting this field to `false`, it is required
        to also set `can_non_owners_invite_collaborators` to
        `false` if it has not already been set. Example: 'True'.

        Returns:
            dict[str, Any]: Returns a folder object for the updated folder

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        If the user is moving folders with a large number of items in all of
        their descendants, the call will be run asynchronously. If the
        operation is not completed within 10 minutes, the user will receive
        a 200 OK response, and the operation will continue running.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "sync_state": sync_state,
            "can_non_owners_invite": can_non_owners_invite,
            "parent": parent,
            "shared_link": shared_link,
            "folder_upload_email": folder_upload_email,
            "tags": tags,
            "is_collaboration_restricted_to_enterprise": is_collaboration_restricted_to_enterprise,
            "collections": collections,
            "can_non_owners_view_collaborators": can_non_owners_view_collaborators,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders/{folder_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_folders_id(self, folder_id: str, recursive: bool | None = None) -> Any:
        """
        Delete folder

        Args:
            folder_id (string): folder_id
            recursive (boolean): Delete a folder that is not empty by recursively deleting the
        folder and all of its content. Example: 'True'.

        Returns:
            Any: Returns an empty response when the folder is successfully deleted
        or moved to the trash.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}"
        query_params = {k: v for k, v in [("recursive", recursive)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folder_app_item_associations(
        self,
        folder_id: str,
        limit: int | None = None,
        marker: str | None = None,
        application_type: str | None = None,
    ) -> dict[str, Any]:
        """
        List folder app item associations

        Args:
            folder_id (string): folder_id
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            application_type (string): If given, returns only app items for this application type Example: 'hubs'.

        Returns:
            dict[str, Any]: Returns a collection of app item objects. If there are no
        app items on this folder an empty collection will be returned.
        This list includes app items on ancestors of this folder.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            App item associations
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/app_item_associations"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("marker", marker),
                ("application_type", application_type),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_id_items(
        self,
        folder_id: str,
        fields: list[str] | None = None,
        usemarker: bool | None = None,
        marker: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        sort: str | None = None,
        direction: str | None = None,
    ) -> dict[str, Any]:
        """
        List items in folder

        Args:
            folder_id (string): folder_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested.

        Additionally this field can be used to query any metadata
        applied to the file by specifying the `metadata` field as well
        as the scope and key of the template to retrieve, for example
        `?fields=metadata.enterprise_12345.contractTemplate`. Example: "['id', 'type', 'name']".
            usemarker (boolean): Specifies whether to use marker-based pagination instead of
        offset-based pagination. Only one pagination method can
        be used at a time.

        By setting this value to true, the API will return a `marker` field
        that can be passed as a parameter to this endpoint to get the next
        page of the response. Example: 'True'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            sort (string): Defines the **second** attribute by which items
        are sorted.

        The folder type affects the way the items
        are sorted:

          * **Standard folder**:
          Items are always sorted by
          their `type` first, with
          folders listed before files,
          and files listed
          before web links.

          * **Root folder**:
          This parameter is not supported
          for marker-based pagination
          on the root folder

          (the folder with an `id` of `0`).

          * **Shared folder with parent path
          to the associated folder visible to
          the collaborator**:
          Items are always sorted by
          their `type` first, with
          folders listed before files,
          and files listed
          before web links. Example: 'id'.
            direction (string): The direction to sort results in. This can be either in alphabetical ascending
        (`ASC`) or descending (`DESC`) order. Example: 'ASC'.

        Returns:
            dict[str, Any]: Returns a collection of files, folders, and web links contained in a folder.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/items"
        query_params = {
            k: v
            for k, v in [
                ("fields", fields),
                ("usemarker", usemarker),
                ("marker", marker),
                ("offset", offset),
                ("limit", limit),
                ("sort", sort),
                ("direction", direction),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_folders(
        self,
        fields: list[str] | None = None,
        name: str | None = None,
        parent: dict[str, Any] | None = None,
        folder_upload_email: Any | None = None,
        sync_state: str | None = None,
    ) -> dict[str, Any]:
        r"""
        Create folder

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): The name for the new folder.

        The following restrictions to folder names apply: names containing
        non-printable ASCII characters, forward and backward slashes
        (`/`, `\`), names with trailing spaces, and names `.` and `..` are
        not allowed.

        Folder names must be unique within their parent folder. The name check is case-insensitive,
        so a folder named `New Folder` cannot be created in a parent folder that already contains
        a folder named `new folder`. Example: 'New Folder'.
            parent (object): The parent folder to create the new folder within.
            folder_upload_email (string): folder_upload_email
            sync_state (string): Specifies whether a folder should be synced to a
        user's device or not. This is used by Box Sync
        (discontinued) and is not used by Box Drive. Example: 'synced'.

        Returns:
            dict[str, Any]: Returns a folder object.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folders
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "parent": parent,
            "folder_upload_email": folder_upload_email,
            "sync_state": sync_state,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_folders_id_copy(
        self,
        folder_id: str,
        fields: list[str] | None = None,
        name: str | None = None,
        parent: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        r"""
        Copy folder

        Args:
            folder_id (string): folder_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): An optional new name for the copied folder.

        There are some restrictions to the file name. Names containing
        non-printable ASCII characters, forward and backward slashes
        (`/`, `\`), as well as names with trailing spaces are
        prohibited.

        Additionally, the names `.` and `..` are
        not allowed either. Example: 'New Folder'.
            parent (object): The destination folder to copy the folder to.

        Returns:
            dict[str, Any]: Returns a new folder object representing the copied folder.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "parent": parent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders/{folder_id}/copy"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_id_collaborations(
        self,
        folder_id: str,
        fields: list[str] | None = None,
        limit: int | None = None,
        marker: str | None = None,
    ) -> dict[str, Any]:
        """
        List folder collaborations

        Args:
            folder_id (string): folder_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.

        Returns:
            dict[str, Any]: Returns a collection of collaboration objects. If there are no
        collaborations on this folder an empty collection will be returned.

        This list includes pending collaborations, for which the `status`
        is set to `pending`, indicating invitations that have been sent but not
        yet accepted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collaborations (List)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/collaborations"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("limit", limit), ("marker", marker)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_id_trash(
        self, folder_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get trashed folder

        Args:
            folder_id (string): folder_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the folder that was trashed,
        including information about when the it
        was moved to the trash.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/trash"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_folders_id_trash(self, folder_id: str) -> Any:
        """
        Permanently remove folder

        Args:
            folder_id (string): folder_id

        Returns:
            Any: Returns an empty response when the folder was
        permanently deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/trash"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_id_metadata(self, folder_id: str) -> dict[str, Any]:
        """
        List metadata instances on folder

        Args:
            folder_id (string): folder_id

        Returns:
            dict[str, Any]: Returns all the metadata associated with a folder.

        This API does not support pagination and will therefore always return
        all of the metadata associated to the folder.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/metadata"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folder_security_classification(self, folder_id: str) -> dict[str, Any]:
        """
        Get classification on folder

        Args:
            folder_id (string): folder_id

        Returns:
            dict[str, Any]: Returns an instance of the `securityClassification` metadata
        template, which contains a `Box__Security__Classification__Key`
        field that lists all the classifications available to this
        enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications on folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_folder_metadata_security_classification(
        self, folder_id: str, Box__Security__Classification__Key: str | None = None
    ) -> dict[str, Any]:
        """
        Add classification to folder

        Args:
            folder_id (string): folder_id
            Box__Security__Classification__Key (string): The name of the classification to apply to this folder.

        To list the available classifications in an enterprise,
        use the classification API to retrieve the
        [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
        which lists all available classification keys. Example: 'Sensitive'.

        Returns:
            dict[str, Any]: Returns the classification template instance
        that was applied to the folder.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications on folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        request_body_data = {
            "Box__Security__Classification__Key": Box__Security__Classification__Key,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_folder_security_classification(
        self, folder_id: str, items: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Update classification on folder

        Args:
            folder_id (string): folder_id

        Returns:
            dict[str, Any]: Returns the updated classification metadata template instance.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications on folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json-patch+json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_security_classification_by_folder_id(self, folder_id: str) -> Any:
        """
        Remove classification from folder

        Args:
            folder_id (string): folder_id

        Returns:
            Any: Returns an empty response when the classification is
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications on folders
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_id_metadata_id_id(
        self, folder_id: str, scope: str, template_key: str
    ) -> dict[str, Any]:
        """
        Get metadata instance on folder

        Args:
            folder_id (string): folder_id
            scope (string): scope
            template_key (string): template_key

        Returns:
            dict[str, Any]: An instance of the metadata template that includes
        additional "key:value" pairs defined by the user or
        an application.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        url = f"{self.base_url}/folders/{folder_id}/metadata/{scope}/{template_key}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_folders_id_metadata_id_id(
        self,
        folder_id: str,
        scope: str,
        template_key: str,
        request_body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create metadata instance on folder

        Args:
            folder_id (string): folder_id
            scope (string): scope
            template_key (string): template_key
            request_body (dict | None): Optional dictionary for an empty JSON request body (e.g., {}).

        Returns:
            dict[str, Any]: Returns the instance of the template that was applied to the folder,
        including the data that was applied to the template.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        request_body_data = None
        request_body_data = request_body if request_body is not None else {}
        url = f"{self.base_url}/folders/{folder_id}/metadata/{scope}/{template_key}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_folders_id_metadata_id_id(
        self,
        folder_id: str,
        scope: str,
        template_key: str,
        items: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Update metadata instance on folder

        Args:
            folder_id (string): folder_id
            scope (string): scope
            template_key (string): template_key

        Returns:
            dict[str, Any]: Returns the updated metadata template instance, with the
        custom template data included.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/folders/{folder_id}/metadata/{scope}/{template_key}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json-patch+json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_folder_metadata(
        self, folder_id: str, scope: str, template_key: str
    ) -> Any:
        """
        Remove metadata instance from folder

        Args:
            folder_id (string): folder_id
            scope (string): scope
            template_key (string): template_key

        Returns:
            Any: Returns an empty response when the metadata is
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata instances (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        url = f"{self.base_url}/folders/{folder_id}/metadata/{scope}/{template_key}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_trash_items(
        self,
        fields: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
        usemarker: bool | None = None,
        marker: str | None = None,
        direction: str | None = None,
        sort: str | None = None,
    ) -> dict[str, Any]:
        """
        List trashed items

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            usemarker (boolean): Specifies whether to use marker-based pagination instead of
        offset-based pagination. Only one pagination method can
        be used at a time.

        By setting this value to true, the API will return a `marker` field
        that can be passed as a parameter to this endpoint to get the next
        page of the response. Example: 'True'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            direction (string): The direction to sort results in. This can be either in alphabetical ascending
        (`ASC`) or descending (`DESC`) order. Example: 'ASC'.
            sort (string): Defines the **second** attribute by which items
        are sorted.

        Items are always sorted by their `type` first, with
        folders listed before files, and files listed
        before web links.

        This parameter is not supported when using marker-based pagination. Example: 'name'.

        Returns:
            dict[str, Any]: Returns a list of items that have been deleted

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed items
        """
        url = f"{self.base_url}/folders/trash/items"
        query_params = {
            k: v
            for k, v in [
                ("fields", fields),
                ("limit", limit),
                ("offset", offset),
                ("usemarker", usemarker),
                ("marker", marker),
                ("direction", direction),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_id_watermark(self, folder_id: str) -> dict[str, Any]:
        """
        Get watermark for folder

        Args:
            folder_id (string): folder_id

        Returns:
            dict[str, Any]: Returns an object containing information about the
        watermark associated for to this folder.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Watermarks (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/watermark"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_folders_id_watermark(
        self, folder_id: str, watermark: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Apply watermark to folder

        Args:
            folder_id (string): folder_id
            watermark (object): The watermark to imprint on the folder

        Returns:
            dict[str, Any]: Returns an updated watermark if a watermark already
        existed on this folder.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Watermarks (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        request_body_data = {
            "watermark": watermark,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders/{folder_id}/watermark"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_folders_id_watermark(self, folder_id: str) -> Any:
        """
        Remove watermark from folder

        Args:
            folder_id (string): folder_id

        Returns:
            Any: An empty response will be returned when the watermark
        was successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Watermarks (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}/watermark"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folder_locks(self, folder_id: str) -> dict[str, Any]:
        """
        List folder locks

        Args:
            folder_id (string): The unique identifier that represent a folder.

        The ID for any folder can be determined
        by visiting this folder in the web application
        and copying the ID from the URL. For example,
        for the URL `https://*.app.box.com/folder/123`
        the `folder_id` is `123`.

        The root folder of a Box account is
        always represented by the ID `0`. Example: '12345'.

        Returns:
            dict[str, Any]: Returns details for all folder locks applied to the folder, including the
        lock type and user that applied the lock.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folder Locks
        """
        url = f"{self.base_url}/folder_locks"
        query_params = {k: v for k, v in [("folder_id", folder_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_folder_locks(
        self,
        locked_operations: dict[str, Any] | None = None,
        folder: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create folder lock

        Args:
            locked_operations (object): The operations to lock for the folder. If `locked_operations` is
        included in the request, both `move` and `delete` must also be
        included and both set to `true`.
            folder (object): The folder to apply the lock to.

        Returns:
            dict[str, Any]: Returns the instance of the folder lock that was applied to the folder,
        including the user that applied the lock and the operations set.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folder Locks
        """
        request_body_data = None
        request_body_data = {
            "locked_operations": locked_operations,
            "folder": folder,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folder_locks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_folder_locks_id(self, folder_lock_id: str) -> Any:
        """
        Delete folder lock

        Args:
            folder_lock_id (string): folder_lock_id

        Returns:
            Any: Returns an empty response when the folder lock is successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Folder Locks
        """
        if folder_lock_id is None:
            raise ValueError("Missing required parameter 'folder_lock_id'.")
        url = f"{self.base_url}/folder_locks/{folder_lock_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_metadata_templates(
        self,
        metadata_instance_id: str,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Find metadata template by instance ID

        Args:
            metadata_instance_id (string): The ID of an instance of the metadata template to find. Example: '01234500-12f1-1234-aa12-b1d234cb567e'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list containing the 1 metadata template that matches the
        instance ID.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata templates
        """
        url = f"{self.base_url}/metadata_templates"
        query_params = {
            k: v
            for k, v in [
                ("metadata_instance_id", metadata_instance_id),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_security_classification_schema(self) -> dict[str, Any]:
        """
        List all classifications

        Returns:
            dict[str, Any]: Returns the `securityClassification` metadata template, which contains
        a `Box__Security__Classification__Key` field that lists all the
        classifications available to this enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications
        """
        url = f"{self.base_url}/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def add_security_classification_schema(
        self, items: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Add classification

        Args:

        Returns:
            dict[str, Any]: Returns the updated `securityClassification` metadata template, which
        contains a `Box__Security__Classification__Key` field that lists all
        the classifications available to this enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#add"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_security_classification_schema(
        self, items: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Update classification

        Args:

        Returns:
            dict[str, Any]: Returns the updated `securityClassification` metadata template, which
        contains a `Box__Security__Classification__Key` field that lists all
        the classifications available to this enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#update"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json-patch+json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_schema_template(self, scope: str, template_key: str) -> dict[str, Any]:
        """
        Get metadata template by name

        Args:
            scope (string): scope
            template_key (string): template_key

        Returns:
            dict[str, Any]: Returns the metadata template matching the `scope`
        and `template` name.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata templates
        """
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        url = f"{self.base_url}/metadata_templates/{scope}/{template_key}/schema"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_schema_template(
        self,
        scope: str,
        template_key: str,
        items: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Update metadata template

        Args:
            scope (string): scope
            template_key (string): template_key

        Returns:
            dict[str, Any]: Returns the updated metadata template, with the
        custom template data included.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata templates
        """
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/metadata_templates/{scope}/{template_key}/schema"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json-patch+json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_metadata_template_schema(self, scope: str, template_key: str) -> Any:
        """
        Remove metadata template

        Args:
            scope (string): scope
            template_key (string): template_key

        Returns:
            Any: Returns an empty response when the metadata
        template is successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata templates
        """
        if scope is None:
            raise ValueError("Missing required parameter 'scope'.")
        if template_key is None:
            raise ValueError("Missing required parameter 'template_key'.")
        url = f"{self.base_url}/metadata_templates/{scope}/{template_key}/schema"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_metadata_templates_id(self, template_id: str) -> dict[str, Any]:
        """
        Get metadata template by ID

        Args:
            template_id (string): template_id

        Returns:
            dict[str, Any]: Returns the metadata template that matches the ID.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'.")
        url = f"{self.base_url}/metadata_templates/{template_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_metadata_templates_global(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List all global metadata templates

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns all of the metadata templates available to all enterprises
        and their corresponding schema.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata templates
        """
        url = f"{self.base_url}/metadata_templates/global"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_metadata_templates_enterprise(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List all metadata templates for enterprise

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns all of the metadata templates within an enterprise
        and their corresponding schema.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata templates
        """
        url = f"{self.base_url}/metadata_templates/enterprise"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_metadata_templates_schema(
        self,
        scope: str | None = None,
        templateKey: str | None = None,
        displayName: str | None = None,
        hidden: bool | None = None,
        fields: list[dict[str, Any]] | None = None,
        copyInstanceOnItemCopy: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create metadata template

        Args:
            scope (string): The scope of the metadata template to create. Applications can
        only create templates for use within the authenticated user's
        enterprise.

        This value needs to be set to `enterprise`, as `global` scopes can
        not be created by applications. Example: 'enterprise'.
            templateKey (string): A unique identifier for the template. This identifier needs to be
        unique across the enterprise for which the metadata template is
        being created.

        When not provided, the API will create a unique `templateKey`
        based on the value of the `displayName`. Example: 'productInfo'.
            displayName (string): The display name of the template. Example: 'Product Info'.
            hidden (boolean): Defines if this template is visible in the Box web app UI, or if
        it is purely intended for usage through the API. Example: 'True'.
            fields (array): An ordered list of template fields which are part of the template.
        Each field can be a regular text field, date field, number field,
        as well as a single or multi-select list.
            copyInstanceOnItemCopy (boolean): Whether or not to copy any metadata attached to a file or folder
        when it is copied. By default, metadata is not copied along with a
        file or folder when it is copied. Example: 'True'.

        Returns:
            dict[str, Any]: The schema representing the metadata template created.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata templates
        """
        request_body_data = None
        request_body_data = {
            "scope": scope,
            "templateKey": templateKey,
            "displayName": displayName,
            "hidden": hidden,
            "fields": fields,
            "copyInstanceOnItemCopy": copyInstanceOnItemCopy,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/metadata_templates/schema"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_metadata_template_classification(
        self,
        scope: str | None = None,
        templateKey: str | None = None,
        displayName: str | None = None,
        hidden: bool | None = None,
        copyInstanceOnItemCopy: bool | None = None,
        fields: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Add initial classifications

        Args:
            scope (string): The scope in which to create the classifications. This should
        be `enterprise` or `enterprise_{id}` where `id` is the unique
        ID of the enterprise. Example: 'enterprise'.
            templateKey (string): Defines the list of metadata templates. Example: 'securityClassification-6VMVochwUWo'.
            displayName (string): The name of the
        template as shown in web and mobile interfaces. Example: 'Classification'.
            hidden (boolean): Determines if the classification template is
        hidden or available on web and mobile
        devices. Example: 'False'.
            copyInstanceOnItemCopy (boolean): Determines if classifications are
        copied along when the file or folder is
        copied. Example: 'False'.
            fields (array): The classification template requires exactly
        one field, which holds
        all the valid classification values.

        Returns:
            dict[str, Any]: Returns a new `securityClassification` metadata template, which
        contains a `Box__Security__Classification__Key` field that lists all
        the classifications available to this enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Classifications
        """
        request_body_data = None
        request_body_data = {
            "scope": scope,
            "templateKey": templateKey,
            "displayName": displayName,
            "hidden": hidden,
            "copyInstanceOnItemCopy": copyInstanceOnItemCopy,
            "fields": fields,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/metadata_templates/schema#classifications"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_metadata_cascade_policies(
        self,
        folder_id: str,
        owner_enterprise_id: str | None = None,
        marker: str | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """
        List metadata cascade policies

        Args:
            folder_id (string): Specifies which folder to return policies for. This can not be used on the
        root folder with ID `0`. Example: '31232'.
            owner_enterprise_id (string): The ID of the enterprise ID for which to find metadata
        cascade policies. If not specified, it defaults to the
        current enterprise. Example: '31232'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list of metadata cascade policies

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata cascade policies
        """
        url = f"{self.base_url}/metadata_cascade_policies"
        query_params = {
            k: v
            for k, v in [
                ("folder_id", folder_id),
                ("owner_enterprise_id", owner_enterprise_id),
                ("marker", marker),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_metadata_cascade_policies(
        self,
        folder_id: str | None = None,
        scope: str | None = None,
        templateKey: str | None = None,
    ) -> dict[str, Any]:
        """
        Create metadata cascade policy

        Args:
            folder_id (string): The ID of the folder to apply the policy to. This folder will
        need to already have an instance of the targeted metadata
        template applied to it. Example: '1234567'.
            scope (string): The scope of the targeted metadata template. This template will
        need to already have an instance applied to the targeted folder. Example: 'enterprise'.
            templateKey (string): The key of the targeted metadata template. This template will
        need to already have an instance applied to the targeted folder.

        In many cases the template key is automatically derived
        of its display name, for example `Contract Template` would
        become `contractTemplate`. In some cases the creator of the
        template will have provided its own template key.

        Please [list the templates for an enterprise][list], or
        get all instances on a [file][file] or [folder][folder]
        to inspect a template's key.

        [list]: e://get-metadata-templates-enterprise
        [file]: e://get-files-id-metadata
        [folder]: e://get-folders-id-metadata Example: 'productInfo'.

        Returns:
            dict[str, Any]: Returns a new of metadata cascade policy

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata cascade policies
        """
        request_body_data = None
        request_body_data = {
            "folder_id": folder_id,
            "scope": scope,
            "templateKey": templateKey,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/metadata_cascade_policies"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_metadata_cascade_policy_by_id(
        self, metadata_cascade_policy_id: str
    ) -> dict[str, Any]:
        """
        Get metadata cascade policy

        Args:
            metadata_cascade_policy_id (string): metadata_cascade_policy_id

        Returns:
            dict[str, Any]: Returns a metadata cascade policy

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata cascade policies
        """
        if metadata_cascade_policy_id is None:
            raise ValueError("Missing required parameter 'metadata_cascade_policy_id'.")
        url = f"{self.base_url}/metadata_cascade_policies/{metadata_cascade_policy_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_metadata_cascade_policy(self, metadata_cascade_policy_id: str) -> Any:
        """
        Remove metadata cascade policy

        Args:
            metadata_cascade_policy_id (string): metadata_cascade_policy_id

        Returns:
            Any: Returns an empty response when the policy
        is successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata cascade policies
        """
        if metadata_cascade_policy_id is None:
            raise ValueError("Missing required parameter 'metadata_cascade_policy_id'.")
        url = f"{self.base_url}/metadata_cascade_policies/{metadata_cascade_policy_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def apply_metadata_cascade_policy_by_id(
        self, metadata_cascade_policy_id: str, conflict_resolution: str | None = None
    ) -> Any:
        """
        Force-apply metadata cascade policy to folder

        Args:
            metadata_cascade_policy_id (string): metadata_cascade_policy_id
            conflict_resolution (string): Describes the desired behavior when dealing with the conflict
        where a metadata template already has an instance applied
        to a child.

        * `none` will preserve the existing value on the file
        * `overwrite` will force-apply the templates values over
          any existing values. Example: 'none'.

        Returns:
            Any: Returns an empty response when the API call was successful. The metadata
        cascade operation will be performed asynchronously.

        The API call will return directly, before the cascade operation
        is complete. There is currently no API to check for the status of this
        operation.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Metadata cascade policies
        """
        if metadata_cascade_policy_id is None:
            raise ValueError("Missing required parameter 'metadata_cascade_policy_id'.")
        request_body_data = None
        request_body_data = {
            "conflict_resolution": conflict_resolution,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/metadata_cascade_policies/{metadata_cascade_policy_id}/apply"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def execute_metadata_query(
        self,
        from_: str | None = None,
        query: str | None = None,
        query_params: dict[str, Any] | None = None,
        ancestor_folder_id: str | None = None,
        order_by: list[dict[str, Any]] | None = None,
        limit: int | None = None,
        marker: str | None = None,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Query files/folders by metadata

        Args:
            from_ (string): Specifies the template used in the query. Must be in the form
        `scope.templateKey`. Not all templates can be used in this field,
        most notably the built-in, Box-provided classification templates
        can not be used in a query. Example: 'enterprise_123456.someTemplate'.
            query (string): The query to perform. A query is a logical expression that is very similar
        to a SQL `SELECT` statement. Values in the search query can be turned into
        parameters specified in the `query_param` arguments list to prevent having
        to manually insert search values into the query string.

        For example, a value of `:amount` would represent the `amount` value in
        `query_params` object. Example: 'value >= :amount'.
            query_params (object): Set of arguments corresponding to the parameters specified in the
        `query`. The type of each parameter used in the `query_params` must match
        the type of the corresponding metadata template field. Example: "{'amount': '100'}".
            ancestor_folder_id (string): The ID of the folder that you are restricting the query to. A
        value of zero will return results from all folders you have access
        to. A non-zero value will only return results found in the folder
        corresponding to the ID or in any of its subfolders. Example: '0'.
            order_by (array): A list of template fields and directions to sort the metadata query
        results by.

        The ordering `direction` must be the same for each item in the array.
            limit (integer): A value between 0 and 100 that indicates the maximum number of results
        to return for a single request. This only specifies a maximum
        boundary and will not guarantee the minimum number of results
        returned. Example: '50'.
            marker (string): Marker to use for requesting the next page. Example: 'AAAAAmVYB1FWec8GH6yWu2nwmanfMh07IyYInaa7DZDYjgO1H4KoLW29vPlLY173OKsci6h6xGh61gG73gnaxoS+o0BbI1/h6le6cikjlupVhASwJ2Cj0tOD9wlnrUMHHw3/ISf+uuACzrOMhN6d5fYrbidPzS6MdhJOejuYlvsg4tcBYzjauP3+VU51p77HFAIuObnJT0ff'.
            fields (array): By default, this endpoint returns only the most basic info about the items for
        which the query matches. This attribute can be used to specify a list of
        additional attributes to return for any item, including its metadata.

        This attribute takes a list of item fields, metadata template identifiers,
        or metadata template field identifiers.

        For example:

        * `created_by` will add the details of the user who created the item to
        the response.
        * `metadata.<scope>.<templateKey>` will return the mini-representation
        of the metadata instance identified by the `scope` and `templateKey`.
        * `metadata.<scope>.<templateKey>.<field>` will return all the mini-representation
        of the metadata instance identified by the `scope` and `templateKey` plus
        the field specified by the `field` name. Multiple fields for the same
        `scope` and `templateKey` can be defined. Example: "['extension', 'created_at', 'item_status', 'metadata.enterprise_1234.contracts', 'metadata.enterprise_1234.regions.location']".

        Returns:
            dict[str, Any]: Returns a list of files and folders that match this metadata query.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "from": from_,
            "query": query,
            "query_params": query_params,
            "ancestor_folder_id": ancestor_folder_id,
            "order_by": order_by,
            "limit": limit,
            "marker": marker,
            "fields": fields,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/metadata_queries/execute_read"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_comments_id(
        self, comment_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get comment

        Args:
            comment_id (string): comment_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a full comment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'.")
        url = f"{self.base_url}/comments/{comment_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_comments_id(
        self,
        comment_id: str,
        fields: list[str] | None = None,
        message: str | None = None,
    ) -> dict[str, Any]:
        """
        Update comment

        Args:
            comment_id (string): comment_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            message (string): The text of the comment to update Example: 'Review completed!'.

        Returns:
            dict[str, Any]: Returns the updated comment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'.")
        request_body_data = None
        request_body_data = {
            "message": message,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/comments/{comment_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_comments_id(self, comment_id: str) -> Any:
        """
        Remove comment

        Args:
            comment_id (string): comment_id

        Returns:
            Any: Returns an empty response when the comment has been deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'.")
        url = f"{self.base_url}/comments/{comment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_comments(
        self,
        fields: list[str] | None = None,
        message: str | None = None,
        tagged_message: str | None = None,
        item: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create comment

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            message (string): The text of the comment.

        To mention a user, use the `tagged_message`
        parameter instead. Example: 'Review completed!'.
            tagged_message (string): The text of the comment, including `@[user_id:name]`
        somewhere in the message to mention another user, which
        will send them an email notification, letting them know
        they have been mentioned.

        The `user_id` is the target user's ID, where the `name`
        can be any custom phrase. In the Box UI this name will
        link to the user's profile.

        If you are not mentioning another user, use `message`
        instead. Example: '@[1234:John] Review completed!'.
            item (object): The item to attach the comment to.

        Returns:
            dict[str, Any]: Returns the newly created comment object.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        request_body_data = None
        request_body_data = {
            "message": message,
            "tagged_message": tagged_message,
            "item": item,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/comments"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_collaborations_id(
        self, collaboration_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get collaboration

        Args:
            collaboration_id (string): collaboration_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a collaboration object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collaborations
        """
        if collaboration_id is None:
            raise ValueError("Missing required parameter 'collaboration_id'.")
        url = f"{self.base_url}/collaborations/{collaboration_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_collaborations_id(
        self,
        collaboration_id: str,
        role: str | None = None,
        status: str | None = None,
        expires_at: str | None = None,
        can_view_path: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update collaboration

        Args:
            collaboration_id (string): collaboration_id
            role (string): The level of access granted. Example: 'editor'.
            status (string): <!--alex ignore reject-->
        Set the status of a `pending` collaboration invitation,
        effectively accepting, or rejecting the invite. Example: 'accepted'.
            expires_at (string): Update the expiration date for the collaboration. At this date,
        the collaboration will be automatically removed from the item.

        This feature will only work if the **Automatically remove invited
        collaborators: Allow folder owners to extend the expiry date**
        setting has been enabled in the **Enterprise Settings**
        of the **Admin Console**. When the setting is not enabled,
        collaborations can not have an expiry date and a value for this
        field will be result in an error.

        Additionally, a collaboration can only be given an
        expiration if it was created after the **Automatically remove
        invited collaborator** setting was enabled. Example: '2019-08-29T23:59:00-07:00'.
            can_view_path (boolean): Determines if the invited users can see the entire parent path to
        the associated folder. The user will not gain privileges in any
        parent folder and therefore can not see content the user is not
        collaborated on.

        Be aware that this meaningfully increases the time required to load the
        invitee's **All Files** page. We recommend you limit the number of
        collaborations with `can_view_path` enabled to 1,000 per user.

        Only owner or co-owners can invite collaborators with a `can_view_path` of
        `true`.

        `can_view_path` can only be used for folder collaborations. Example: 'True'.

        Returns:
            dict[str, Any]: Returns an updated collaboration object unless the owner has changed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collaborations
        """
        if collaboration_id is None:
            raise ValueError("Missing required parameter 'collaboration_id'.")
        request_body_data = None
        request_body_data = {
            "role": role,
            "status": status,
            "expires_at": expires_at,
            "can_view_path": can_view_path,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/collaborations/{collaboration_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_collaborations_id(self, collaboration_id: str) -> Any:
        """
        Remove collaboration

        Args:
            collaboration_id (string): collaboration_id

        Returns:
            Any: A blank response is returned if the collaboration was
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collaborations
        """
        if collaboration_id is None:
            raise ValueError("Missing required parameter 'collaboration_id'.")
        url = f"{self.base_url}/collaborations/{collaboration_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_collaborations(
        self,
        status: str,
        fields: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List pending collaborations

        Args:
            status (string): The status of the collaborations to retrieve Example: 'pending'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of pending collaboration objects.

        If the user has no pending collaborations, the collection
        will be empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collaborations (List)
        """
        url = f"{self.base_url}/collaborations"
        query_params = {
            k: v
            for k, v in [
                ("status", status),
                ("fields", fields),
                ("offset", offset),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_collaborations(
        self,
        fields: list[str] | None = None,
        notify: bool | None = None,
        item: dict[str, Any] | None = None,
        accessible_by: dict[str, Any] | None = None,
        role: str | None = None,
        is_access_only: bool | None = None,
        can_view_path: bool | None = None,
        expires_at: str | None = None,
    ) -> dict[str, Any]:
        """
        Create collaboration

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            notify (boolean): Determines if users should receive email notification
        for the action performed. Example: 'True'.
            item (object): The item to attach the comment to.
            accessible_by (object): The user or group to give access to the item.
            role (string): The level of access granted. Example: 'editor'.
            is_access_only (boolean): If set to `true`, collaborators have access to
        shared items, but such items won't be visible in the
        All Files list. Additionally, collaborators won't
        see the the path to the root folder for the
        shared item. Example: 'True'.
            can_view_path (boolean): Determines if the invited users can see the entire parent path to
        the associated folder. The user will not gain privileges in any
        parent folder and therefore can not see content the user is not
        collaborated on.

        Be aware that this meaningfully increases the time required to load the
        invitee's **All Files** page. We recommend you limit the number of
        collaborations with `can_view_path` enabled to 1,000 per user.

        Only owner or co-owners can invite collaborators with a `can_view_path` of
        `true`.

        `can_view_path` can only be used for folder collaborations. Example: 'True'.
            expires_at (string): Set the expiration date for the collaboration. At this date, the
        collaboration will be automatically removed from the item.

        This feature will only work if the **Automatically remove invited
        collaborators: Allow folder owners to extend the expiry date**
        setting has been enabled in the **Enterprise Settings**
        of the **Admin Console**. When the setting is not enabled,
        collaborations can not have an expiry date and a value for this
        field will be result in an error. Example: '2019-08-29T23:59:00-07:00'.

        Returns:
            dict[str, Any]: Returns a new collaboration object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collaborations
        """
        request_body_data = None
        request_body_data = {
            "item": item,
            "accessible_by": accessible_by,
            "role": role,
            "is_access_only": is_access_only,
            "can_view_path": can_view_path,
            "expires_at": expires_at,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/collaborations"
        query_params = {
            k: v for k, v in [("fields", fields), ("notify", notify)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_search(
        self,
        query: str | None = None,
        scope: str | None = None,
        file_extensions: list[str] | None = None,
        created_at_range: list[str] | None = None,
        updated_at_range: list[str] | None = None,
        size_range: list[int] | None = None,
        owner_user_ids: list[str] | None = None,
        recent_updater_user_ids: list[str] | None = None,
        ancestor_folder_ids: list[str] | None = None,
        content_types: list[str] | None = None,
        type: str | None = None,
        trash_content: str | None = None,
        mdfilters: list[dict[str, Any]] | None = None,
        sort: str | None = None,
        direction: str | None = None,
        limit: int | None = None,
        include_recent_shared_links: bool | None = None,
        fields: list[str] | None = None,
        offset: int | None = None,
        deleted_user_ids: list[str] | None = None,
        deleted_at_range: list[str] | None = None,
    ) -> Any:
        """
        Search for content

        Args:
            query (string): The string to search for. This query is matched against item names,
        descriptions, text content of files, and various other fields of
        the different item types.

        This parameter supports a variety of operators to further refine
        the results returns.

        * `""` - by wrapping a query in double quotes only exact matches are
          returned by the API. Exact searches do not return search matches
          based on specific character sequences. Instead, they return
          matches based on phrases, that is, word sequences. For example:
          A search for `"Blue-Box"` may return search results including
          the sequence `"blue.box"`, `"Blue Box"`, and `"Blue-Box"`;
          any item containing the words `Blue` and `Box` consecutively, in
          the order specified.
        * `AND` - returns items that contain both the search terms. For
          example, a search for `marketing AND BoxWorks` returns items
          that have both `marketing` and `BoxWorks` within its text in any order.
          It does not return a result that only has `BoxWorks` in its text.
        * `OR` - returns items that contain either of the search terms. For
          example, a search for `marketing OR BoxWorks` returns a result that
          has either `marketing` or `BoxWorks` within its text. Using this
          operator is not necessary as we implicitly interpret multi-word
          queries as `OR` unless another supported boolean term is used.
        * `NOT` - returns items that do not contain the search term provided.
          For example, a search for `marketing AND NOT BoxWorks` returns a result
          that has only `marketing` within its text. Results containing
          `BoxWorks` are omitted.

        We do not support lower case (that is,
        `and`, `or`, and `not`) or mixed case (that is, `And`, `Or`, and `Not`)
        operators.

        This field is required unless the `mdfilters` parameter is defined. Example: 'sales'.
            scope (string): Limits the search results to either the files that the user has
        access to, or to files available to the entire enterprise.

        The scope defaults to `user_content`, which limits the search
        results to content that is available to the currently authenticated
        user.

        The `enterprise_content` can be requested by an admin through our
        support channels. Once this scope has been enabled for a user, it
        will allow that use to query for content across the entire
        enterprise and not only the content that they have access to. Example: 'user_content'.
            file_extensions (array): Limits the search results to any files that match any of the provided
        file extensions. This list is a comma-separated list of file extensions
        without the dots. Example: "['pdf', 'png', 'gif']".
            created_at_range (array): Limits the search results to any items created within
        a given date range.

        Date ranges are defined as comma separated RFC3339
        timestamps.

        If the the start date is omitted (`,2014-05-17T13:35:01-07:00`)
        anything created before the end date will be returned.

        If the end date is omitted (`2014-05-15T13:35:01-07:00,`) the
        current date will be used as the end date instead. Example: "['2014-05-15T13:35:01-07:00', '2014-05-17T13:35:01-07:00']".
            updated_at_range (array): Limits the search results to any items updated within
        a given date range.

        Date ranges are defined as comma separated RFC3339
        timestamps.

        If the start date is omitted (`,2014-05-17T13:35:01-07:00`)
        anything updated before the end date will be returned.

        If the end date is omitted (`2014-05-15T13:35:01-07:00,`) the
        current date will be used as the end date instead. Example: "['2014-05-15T13:35:01-07:00', '2014-05-17T13:35:01-07:00']".
            size_range (array): Limits the search results to any items with a size within
        a given file size range. This applied to files and folders.

        Size ranges are defined as comma separated list of a lower
        and upper byte size limit (inclusive).

        The upper and lower bound can be omitted to create open ranges. Example: '[1000000, 5000000]'.
            owner_user_ids (array): Limits the search results to any items that are owned
        by the given list of owners, defined as a list of comma separated
        user IDs.

        The items still need to be owned or shared with
        the currently authenticated user for them to show up in the search
        results. If the user does not have access to any files owned by any of
        the users an empty result set will be returned.

        To search across an entire enterprise, we recommend using the
        `enterprise_content` scope parameter which can be requested with our
        support team. Example: "['123422', '23532', '3241212']".
            recent_updater_user_ids (array): Limits the search results to any items that have been updated
        by the given list of users, defined as a list of comma separated
        user IDs.

        The items still need to be owned or shared with
        the currently authenticated user for them to show up in the search
        results. If the user does not have access to any files owned by any of
        the users an empty result set will be returned.

        This feature only searches back to the last 10 versions of an item. Example: "['123422', '23532', '3241212']".
            ancestor_folder_ids (array): Limits the search results to items within the given
        list of folders, defined as a comma separated lists
        of folder IDs.

        Search results will also include items within any subfolders
        of those ancestor folders.

        The folders still need to be owned or shared with
        the currently authenticated user. If the folder is not accessible by this
        user, or it does not exist, a `HTTP 404` error code will be returned
        instead.

        To search across an entire enterprise, we recommend using the
        `enterprise_content` scope parameter which can be requested with our
        support team. Example: "['4535234', '234123235', '2654345']".
            content_types (array): Limits the search results to any items that match the search query
        for a specific part of the file, for example the file description.

        Content types are defined as a comma separated lists
        of Box recognized content types. The allowed content types are as follows.

        * `name` - The name of the item, as defined by its `name` field.
        * `description` - The description of the item, as defined by its
          `description` field.
        * `file_content` - The actual content of the file.
        * `comments` - The content of any of the comments on a file or
           folder.
        * `tags` - Any tags that are applied to an item, as defined by its
           `tags` field. Example: "['name', 'description']".
            type (string): Limits the search results to any items of this type. This
        parameter only takes one value. By default the API returns
        items that match any of these types.

        * `file` - Limits the search results to files
        * `folder` - Limits the search results to folders
        * `web_link` - Limits the search results to web links, also known
           as bookmarks Example: 'file'.
            trash_content (string): Determines if the search should look in the trash for items.

        By default, this API only returns search results for items
        not currently in the trash (`non_trashed_only`).

        * `trashed_only` - Only searches for items currently in the trash
        * `non_trashed_only` - Only searches for items currently not in
          the trash
        * `all_items` - Searches for both trashed and non-trashed items. Example: 'non_trashed_only'.
            mdfilters (array): Limits the search results to any items for which the metadata matches the provided filter.
        This parameter is a list that specifies exactly **one** metadata template used to filter the search results.
        The parameter is required unless the `query` parameter is provided. Example: "[{'scope': 'enterprise', 'templateKey': 'contract', 'filters': [{'category': 'online'}, {'contractValue': 100000}]}]".
            sort (string): Defines the order in which search results are returned. This API
        defaults to returning items by relevance unless this parameter is
        explicitly specified.

        * `relevance` (default) returns the results sorted by relevance to the
        query search term. The relevance is based on the occurrence of the search
        term in the items name, description, content, and additional properties.
        * `modified_at` returns the results ordered in descending order by date
        at which the item was last modified. Example: 'modified_at'.
            direction (string): Defines the direction in which search results are ordered. This API
        defaults to returning items in descending (`DESC`) order unless this
        parameter is explicitly specified.

        When results are sorted by `relevance` the ordering is locked to returning
        items in descending order of relevance, and this parameter is ignored. Example: 'ASC'.
            limit (integer): Defines the maximum number of items to return as part of a page of
        results. Example: '100'.
            include_recent_shared_links (boolean): Defines whether the search results should include any items
        that the user recently accessed through a shared link.

        When this parameter has been set to true,
        the format of the response of this API changes to return
        a list of [Search Results with
        Shared Links](r://search_results_with_shared_links) Example: 'True'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            deleted_user_ids (array): Limits the search results to items that were deleted by the given
        list of users, defined as a list of comma separated user IDs.

        The `trash_content` parameter needs to be set to `trashed_only`.

        If searching in trash is not performed, an empty result set
        is returned. The items need to be owned or shared with
        the currently authenticated user for them to show up in the search
        results.

        If the user does not have access to any files owned by
        any of the users, an empty result set is returned.

        Data available from 2023-02-01 onwards. Example: "['123422', '23532', '3241212']".
            deleted_at_range (array): Limits the search results to any items deleted within a given
        date range.

        Date ranges are defined as comma separated RFC3339 timestamps.

        If the the start date is omitted (`2014-05-17T13:35:01-07:00`),
        anything deleted before the end date will be returned.

        If the end date is omitted (`2014-05-15T13:35:01-07:00`),
        the current date will be used as the end date instead.

        The `trash_content` parameter needs to be set to `trashed_only`.

        If searching in trash is not performed, then an empty result
        is returned.

        Data available from 2023-02-01 onwards. Example: "['2014-05-15T13:35:01-07:00', '2014-05-17T13:35:01-07:00']".

        Returns:
            Any: Returns a collection of search results. If there are no matching
        search results, the `entries` array will be empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Search
        """
        url = f"{self.base_url}/search"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("scope", scope),
                ("file_extensions", file_extensions),
                ("created_at_range", created_at_range),
                ("updated_at_range", updated_at_range),
                ("size_range", size_range),
                ("owner_user_ids", owner_user_ids),
                ("recent_updater_user_ids", recent_updater_user_ids),
                ("ancestor_folder_ids", ancestor_folder_ids),
                ("content_types", content_types),
                ("type", type),
                ("trash_content", trash_content),
                ("mdfilters", mdfilters),
                ("sort", sort),
                ("direction", direction),
                ("limit", limit),
                ("include_recent_shared_links", include_recent_shared_links),
                ("fields", fields),
                ("offset", offset),
                ("deleted_user_ids", deleted_user_ids),
                ("deleted_at_range", deleted_at_range),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_tasks(
        self,
        item: dict[str, Any] | None = None,
        action: str | None = None,
        message: str | None = None,
        due_at: str | None = None,
        completion_rule: str | None = None,
    ) -> dict[str, Any]:
        """
        Create task

        Args:
            item (object): The file to attach the task to.
            action (string): The action the task assignee will be prompted to do. Must be

        * `review` defines an approval task that can be approved or
        rejected
        * `complete` defines a general task which can be completed Example: 'review'.
            message (string): An optional message to include with the task. Example: 'Please review'.
            due_at (string): Defines when the task is due. Defaults to `null` if not
        provided. Example: '2012-12-12T10:53:43-08:00'.
            completion_rule (string): Defines which assignees need to complete this task before the task
        is considered completed.

        * `all_assignees` (default) requires all assignees to review or
        approve the the task in order for it to be considered completed.
        * `any_assignee` accepts any one assignee to review or
        approve the the task in order for it to be considered completed. Example: 'all_assignees'.

        Returns:
            dict[str, Any]: Returns the newly created task.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        request_body_data = None
        request_body_data = {
            "item": item,
            "action": action,
            "message": message,
            "due_at": due_at,
            "completion_rule": completion_rule,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/tasks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_tasks_id(self, task_id: str) -> dict[str, Any]:
        """
        Get task

        Args:
            task_id (string): task_id

        Returns:
            dict[str, Any]: Returns a task object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if task_id is None:
            raise ValueError("Missing required parameter 'task_id'.")
        url = f"{self.base_url}/tasks/{task_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_tasks_id(
        self,
        task_id: str,
        action: str | None = None,
        message: str | None = None,
        due_at: str | None = None,
        completion_rule: str | None = None,
    ) -> dict[str, Any]:
        """
        Update task

        Args:
            task_id (string): task_id
            action (string): The action the task assignee will be prompted to do. Must be

        * `review` defines an approval task that can be approved or
        rejected
        * `complete` defines a general task which can be completed Example: 'review'.
            message (string): The message included with the task. Example: 'Please review'.
            due_at (string): When the task is due at. Example: '2012-12-12T10:53:43-08:00'.
            completion_rule (string): Defines which assignees need to complete this task before the task
        is considered completed.

        * `all_assignees` (default) requires all assignees to review or
        approve the the task in order for it to be considered completed.
        * `any_assignee` accepts any one assignee to review or
        approve the the task in order for it to be considered completed. Example: 'all_assignees'.

        Returns:
            dict[str, Any]: Returns the updated task object

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if task_id is None:
            raise ValueError("Missing required parameter 'task_id'.")
        request_body_data = None
        request_body_data = {
            "action": action,
            "message": message,
            "due_at": due_at,
            "completion_rule": completion_rule,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/tasks/{task_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_tasks_id(self, task_id: str) -> Any:
        """
        Remove task

        Args:
            task_id (string): task_id

        Returns:
            Any: Returns an empty response when the task was successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if task_id is None:
            raise ValueError("Missing required parameter 'task_id'.")
        url = f"{self.base_url}/tasks/{task_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_tasks_id_assignments(self, task_id: str) -> dict[str, Any]:
        """
        List task assignments

        Args:
            task_id (string): task_id

        Returns:
            dict[str, Any]: Returns a collection of task assignment defining what task on
        a file has been assigned to which users and by who.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Task assignments
        """
        if task_id is None:
            raise ValueError("Missing required parameter 'task_id'.")
        url = f"{self.base_url}/tasks/{task_id}/assignments"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_task_assignments(
        self,
        task: dict[str, Any] | None = None,
        assign_to: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Assign task

        Args:
            task (object): The task to assign to a user.
            assign_to (object): The user to assign the task to.

        Returns:
            dict[str, Any]: Returns a new task assignment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Task assignments
        """
        request_body_data = None
        request_body_data = {
            "task": task,
            "assign_to": assign_to,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/task_assignments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_task_assignments_id(self, task_assignment_id: str) -> dict[str, Any]:
        """
        Get task assignment

        Args:
            task_assignment_id (string): task_assignment_id

        Returns:
            dict[str, Any]: Returns a task assignment, specifying who the task has been assigned to
        and by whom.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Task assignments
        """
        if task_assignment_id is None:
            raise ValueError("Missing required parameter 'task_assignment_id'.")
        url = f"{self.base_url}/task_assignments/{task_assignment_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_task_assignments_id(
        self,
        task_assignment_id: str,
        message: str | None = None,
        resolution_state: str | None = None,
    ) -> dict[str, Any]:
        """
        Update task assignment

        Args:
            task_assignment_id (string): task_assignment_id
            message (string): An optional message by the assignee that can be added to the task. Example: 'Looks good to me'.
            resolution_state (string): The state of the task assigned to the user.

        * For a task with an `action` value of `complete` this can be
        `incomplete` or `completed`.
        * For a task with an `action` of `review` this can be
        `incomplete`, `approved`, or `rejected`. Example: 'completed'.

        Returns:
            dict[str, Any]: Returns the updated task assignment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Task assignments
        """
        if task_assignment_id is None:
            raise ValueError("Missing required parameter 'task_assignment_id'.")
        request_body_data = None
        request_body_data = {
            "message": message,
            "resolution_state": resolution_state,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/task_assignments/{task_assignment_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_task_assignments_id(self, task_assignment_id: str) -> Any:
        """
        Unassign task

        Args:
            task_assignment_id (string): task_assignment_id

        Returns:
            Any: Returns an empty response when the task
        assignment was successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Task assignments
        """
        if task_assignment_id is None:
            raise ValueError("Missing required parameter 'task_assignment_id'.")
        url = f"{self.base_url}/task_assignments/{task_assignment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shared_items(self, fields: list[str] | None = None) -> dict[str, Any]:
        """
        Find file for shared link

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a full file resource if the shared link is valid and
        the user has access to it.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Files)
        """
        url = f"{self.base_url}/shared_items"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_id_get_shared_link(self, file_id: str, fields: str) -> dict[str, Any]:
        """
        Get shared link for file

        Args:
            file_id (string): file_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.

        Returns:
            dict[str, Any]: Returns the base representation of a file with the
        additional shared link information.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        url = f"{self.base_url}/files/{file_id}#get_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_files_id_add_shared_link(
        self, file_id: str, fields: str, shared_link: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Add shared link to file

        Args:
            file_id (string): file_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): The settings for the shared link to create on the file.
        Use an empty object (`{}`) to use the default settings for shared
        links.

        Returns:
            dict[str, Any]: Returns the base representation of a file with a new shared
        link attached.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}#add_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_file_shared_link(
        self, file_id: str, fields: str, shared_link: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Update shared link on file

        Args:
            file_id (string): file_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): The settings for the shared link to update.

        Returns:
            dict[str, Any]: Returns a basic representation of the file, with the updated shared
        link attached.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}#update_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def remove_shared_link_by_id(
        self, file_id: str, fields: str, shared_link: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Remove shared link from file

        Args:
            file_id (string): file_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): By setting this value to `null`, the shared link
        is removed from the file.

        Returns:
            dict[str, Any]: Returns a basic representation of a file, with the shared link removed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Files)
        """
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{file_id}#remove_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shared_items_folders(
        self, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Find folder for shared link

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a full folder resource if the shared link is valid and
        the user has access to it.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Folders)
        """
        url = f"{self.base_url}/shared_items#folders"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_folders_id_get_shared_link(
        self, folder_id: str, fields: str
    ) -> dict[str, Any]:
        """
        Get shared link for folder

        Args:
            folder_id (string): folder_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.

        Returns:
            dict[str, Any]: Returns the base representation of a folder with the
        additional shared link information.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/folders/{folder_id}#get_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_folders_id_add_shared_link(
        self, folder_id: str, fields: str, shared_link: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Add shared link to folder

        Args:
            folder_id (string): folder_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): The settings for the shared link to create on the folder.

        Use an empty object (`{}`) to use the default settings for shared
        links.

        Returns:
            dict[str, Any]: Returns the base representation of a folder with a new shared
        link attached.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders/{folder_id}#add_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_shared_linkfolder(
        self, folder_id: str, fields: str, shared_link: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Update shared link on folder

        Args:
            folder_id (string): folder_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): The settings for the shared link to update.

        Returns:
            dict[str, Any]: Returns a basic representation of the folder, with the updated shared
        link attached.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders/{folder_id}#update_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def remove_shared_link_by_folder_id(
        self, folder_id: str, fields: str, shared_link: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Remove shared link from folder

        Args:
            folder_id (string): folder_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): By setting this value to `null`, the shared link
        is removed from the folder.

        Returns:
            dict[str, Any]: Returns a basic representation of a folder, with the shared link removed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Folders)
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/folders/{folder_id}#remove_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_web_links(
        self,
        url: str | None = None,
        parent: dict[str, Any] | None = None,
        name: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        """
        Create web link

        Args:
            url (string): The URL that this web link links to. Must start with
        `"http://"` or `"https://"`. Example: 'https://box.com'.
            parent (object): The parent folder to create the web link within.
            name (string): Name of the web link. Defaults to the URL if not set. Example: 'Box Website'.
            description (string): Description of the web link. Example: 'Cloud Content Management'.

        Returns:
            dict[str, Any]: Returns the newly created web link object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Web links
        """
        request_body_data = None
        request_body_data = {
            "url": url,
            "parent": parent,
            "name": name,
            "description": description,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/web_links"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_web_links_id(self, web_link_id: str) -> dict[str, Any]:
        """
        Get web link

        Args:
            web_link_id (string): web_link_id

        Returns:
            dict[str, Any]: Returns the web link object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Web links
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        url = f"{self.base_url}/web_links/{web_link_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_web_links_id(
        self,
        web_link_id: str,
        fields: list[str] | None = None,
        name: str | None = None,
        parent: Any | None = None,
    ) -> dict[str, Any]:
        """
        Restore web link

        Args:
            web_link_id (string): web_link_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): An optional new name for the web link. Example: 'Restored.docx'.
            parent (string): parent

        Returns:
            dict[str, Any]: Returns a web link object when it has been restored.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed web links
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "parent": parent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/web_links/{web_link_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_web_links_id(
        self,
        web_link_id: str,
        url: str | None = None,
        parent: Any | None = None,
        name: str | None = None,
        description: str | None = None,
        shared_link: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update web link

        Args:
            web_link_id (string): web_link_id
            url (string): The new URL that the web link links to. Must start with
        `"http://"` or `"https://"`. Example: 'https://box.com'.
            parent (string): parent
            name (string): A new name for the web link. Defaults to the URL if not set. Example: 'Box Website'.
            description (string): A new description of the web link. Example: 'Cloud Content Management'.
            shared_link (object): The settings for the shared link to update.

        Returns:
            dict[str, Any]: Returns the updated web link object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Web links
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        request_body_data = None
        request_body_data = {
            "url": url,
            "parent": parent,
            "name": name,
            "description": description,
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/web_links/{web_link_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_web_links_id(self, web_link_id: str) -> Any:
        """
        Remove web link

        Args:
            web_link_id (string): web_link_id

        Returns:
            Any: An empty response will be returned when the web link
        was successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Web links
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        url = f"{self.base_url}/web_links/{web_link_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_web_links_id_trash(
        self, web_link_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get trashed web link

        Args:
            web_link_id (string): web_link_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the web link that was trashed,
        including information about when the it
        was moved to the trash.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed web links
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        url = f"{self.base_url}/web_links/{web_link_id}/trash"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_web_links_id_trash(self, web_link_id: str) -> Any:
        """
        Permanently remove web link

        Args:
            web_link_id (string): web_link_id

        Returns:
            Any: Returns an empty response when the web link was
        permanently deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trashed web links
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        url = f"{self.base_url}/web_links/{web_link_id}/trash"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shared_items_web_links(
        self, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Find web link for shared link

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a full web link resource if the shared link is valid and
        the user has access to it.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Web Links)
        """
        url = f"{self.base_url}/shared_items#web_links"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shared_link_by_id(self, web_link_id: str, fields: str) -> dict[str, Any]:
        """
        Get shared link for web link

        Args:
            web_link_id (string): web_link_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.

        Returns:
            dict[str, Any]: Returns the base representation of a web link with the
        additional shared link information.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Web Links)
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        url = f"{self.base_url}/web_links/{web_link_id}#get_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_web_link_shared_link(
        self,
        web_link_id: str,
        fields: str,
        shared_link: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Add shared link to web link

        Args:
            web_link_id (string): web_link_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): The settings for the shared link to create on the web link.

        Use an empty object (`{}`) to use the default settings for shared
        links.

        Returns:
            dict[str, Any]: Returns the base representation of a web link with a new shared
        link attached.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Web Links)
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/web_links/{web_link_id}#add_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_shared_link(
        self,
        web_link_id: str,
        fields: str,
        shared_link: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update shared link on web link

        Args:
            web_link_id (string): web_link_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): The settings for the shared link to update.

        Returns:
            dict[str, Any]: Returns a basic representation of the web link, with the updated shared
        link attached.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Web Links)
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/web_links/{web_link_id}#update_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def remove_shared_link_by_web_link_id(
        self,
        web_link_id: str,
        fields: str,
        shared_link: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Remove shared link from web link

        Args:
            web_link_id (string): web_link_id
            fields (string): Explicitly request the `shared_link` fields
        to be returned for this item. Example: 'shared_link'.
            shared_link (object): By setting this value to `null`, the shared link
        is removed from the web link.

        Returns:
            dict[str, Any]: Returns a basic representation of a web link, with the
        shared link removed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (Web Links)
        """
        if web_link_id is None:
            raise ValueError("Missing required parameter 'web_link_id'.")
        request_body_data = None
        request_body_data = {
            "shared_link": shared_link,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/web_links/{web_link_id}#remove_shared_link"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shared_items_app_items(self) -> dict[str, Any]:
        """
        Find app item for shared link

        Returns:
            dict[str, Any]: Returns a full app item resource if the shared link is valid and
        the user has access to it.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared links (App Items)
        """
        url = f"{self.base_url}/shared_items#app_items"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_users(
        self,
        filter_term: str | None = None,
        user_type: str | None = None,
        external_app_user_id: str | None = None,
        fields: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        usemarker: bool | None = None,
        marker: str | None = None,
    ) -> dict[str, Any]:
        """
        List enterprise users

        Args:
            filter_term (string): Limits the results to only users who's `name` or
        `login` start with the search term.

        For externally managed users, the search term needs
        to completely match the in order to find the user, and
        it will only return one user at a time. Example: 'john'.
            user_type (string): Limits the results to the kind of user specified.

        * `all` returns every kind of user for whom the
          `login` or `name` partially matches the
          `filter_term`. It will only return an external user
          if the login matches the `filter_term` completely,
          and in that case it will only return that user.
        * `managed` returns all managed and app users for whom
          the `login` or `name` partially matches the
          `filter_term`.
        * `external` returns all external users for whom the
          `login` matches the `filter_term` exactly. Example: 'managed'.
            external_app_user_id (string): Limits the results to app users with the given
        `external_app_user_id` value.

        When creating an app user, an
        `external_app_user_id` value can be set. This value can
        then be used in this endpoint to find any users that
        match that `external_app_user_id` value. Example: 'my-user-1234'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            usemarker (boolean): Specifies whether to use marker-based pagination instead of
        offset-based pagination. Only one pagination method can
        be used at a time.

        By setting this value to true, the API will return a `marker` field
        that can be passed as a parameter to this endpoint to get the next
        page of the response. Example: 'True'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.

        Returns:
            dict[str, Any]: Returns all of the users in the enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users, important
        """
        url = f"{self.base_url}/users"
        query_params = {
            k: v
            for k, v in [
                ("filter_term", filter_term),
                ("user_type", user_type),
                ("external_app_user_id", external_app_user_id),
                ("fields", fields),
                ("offset", offset),
                ("limit", limit),
                ("usemarker", usemarker),
                ("marker", marker),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_users(
        self,
        fields: list[str] | None = None,
        name: str | None = None,
        login: str | None = None,
        is_platform_access_only: bool | None = None,
        role: str | None = None,
        language: str | None = None,
        is_sync_enabled: bool | None = None,
        job_title: str | None = None,
        phone: str | None = None,
        address: str | None = None,
        space_amount: int | None = None,
        tracking_codes: list[dict[str, Any]] | None = None,
        can_see_managed_users: bool | None = None,
        timezone: str | None = None,
        is_external_collab_restricted: bool | None = None,
        is_exempt_from_device_limits: bool | None = None,
        is_exempt_from_login_verification: bool | None = None,
        status: str | None = None,
        external_app_user_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Create user

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): The name of the user Example: 'Aaron Levie'.
            login (string): The email address the user uses to log in

        Required, unless `is_platform_access_only`
        is set to `true`. Example: 'boss@box.com'.
            is_platform_access_only (boolean): Specifies that the user is an app user. Example: 'True'.
            role (string): The user’s enterprise role Example: 'user'.
            language (string): The language of the user, formatted in modified version of the
        [ISO 639-1](/guides/api-calls/language-codes) format. Example: 'en'.
            is_sync_enabled (boolean): Whether the user can use Box Sync Example: 'True'.
            job_title (string): The user’s job title Example: 'CEO'.
            phone (string): The user’s phone number Example: '6509241374'.
            address (string): The user’s address Example: '900 Jefferson Ave, Redwood City, CA 94063'.
            space_amount (integer): The user’s total available space in bytes. Set this to `-1` to
        indicate unlimited storage. Example: '11345156112'.
            tracking_codes (array): Tracking codes allow an admin to generate reports from the
        admin console and assign an attribute to a specific group
        of users. This setting must be enabled for an enterprise before it
        can be used.
            can_see_managed_users (boolean): Whether the user can see other enterprise users in their
        contact list Example: 'True'.
            timezone (string): The user's timezone Example: 'Africa/Bujumbura'.
            is_external_collab_restricted (boolean): Whether the user is allowed to collaborate with users outside
        their enterprise Example: 'True'.
            is_exempt_from_device_limits (boolean): Whether to exempt the user from enterprise device limits Example: 'True'.
            is_exempt_from_login_verification (boolean): Whether the user must use two-factor authentication Example: 'True'.
            status (string): The user's account status Example: 'active'.
            external_app_user_id (string): An external identifier for an app user, which can be used to look
        up the user. This can be used to tie user IDs from external
        identity providers to Box users. Example: 'my-user-1234'.

        Returns:
            dict[str, Any]: Returns a user object for the newly created user.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "login": login,
            "is_platform_access_only": is_platform_access_only,
            "role": role,
            "language": language,
            "is_sync_enabled": is_sync_enabled,
            "job_title": job_title,
            "phone": phone,
            "address": address,
            "space_amount": space_amount,
            "tracking_codes": tracking_codes,
            "can_see_managed_users": can_see_managed_users,
            "timezone": timezone,
            "is_external_collab_restricted": is_external_collab_restricted,
            "is_exempt_from_device_limits": is_exempt_from_device_limits,
            "is_exempt_from_login_verification": is_exempt_from_login_verification,
            "status": status,
            "external_app_user_id": external_app_user_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_users_me(self, fields: list[str] | None = None) -> dict[str, Any]:
        """
        Get current user

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a single user object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        url = f"{self.base_url}/users/me"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_users_terminate_sessions(
        self,
        user_ids: list[str] | None = None,
        user_logins: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Create jobs to terminate users session

        Args:
            user_ids (array): A list of user IDs Example: "['123456', '456789']".
            user_logins (array): A list of user logins Example: "['user@sample.com', 'user2@sample.com']".

        Returns:
            dict[str, Any]: Returns a message about the request status.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Session termination
        """
        request_body_data = None
        request_body_data = {
            "user_ids": user_ids,
            "user_logins": user_logins,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/terminate_sessions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_users_id(
        self, user_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get user

        Args:
            user_id (string): user_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a single user object.

        Not all available fields are returned by default. Use the
        [fields](#param-fields) query parameter to explicitly request
        any specific fields using the [fields](#get-users-id--request--fields)
        parameter.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/users/{user_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_users_id(
        self,
        user_id: str,
        fields: list[str] | None = None,
        enterprise: str | None = None,
        notify: bool | None = None,
        name: str | None = None,
        login: str | None = None,
        role: str | None = None,
        language: str | None = None,
        is_sync_enabled: bool | None = None,
        job_title: str | None = None,
        phone: str | None = None,
        address: str | None = None,
        tracking_codes: list[dict[str, Any]] | None = None,
        can_see_managed_users: bool | None = None,
        timezone: str | None = None,
        is_external_collab_restricted: bool | None = None,
        is_exempt_from_device_limits: bool | None = None,
        is_exempt_from_login_verification: bool | None = None,
        is_password_reset_required: bool | None = None,
        status: str | None = None,
        space_amount: int | None = None,
        notification_email: dict[str, Any] | None = None,
        external_app_user_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Update user

        Args:
            user_id (string): user_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            enterprise (string): Set this to `null` to roll the user out of the enterprise
        and make them a free user
            notify (boolean): Whether the user should receive an email when they
        are rolled out of an enterprise Example: 'True'.
            name (string): The name of the user Example: 'Aaron Levie'.
            login (string): The email address the user uses to log in

        Note: If the target user's email is not confirmed, then the
        primary login address cannot be changed. Example: 'somename@box.com'.
            role (string): The user’s enterprise role Example: 'user'.
            language (string): The language of the user, formatted in modified version of the
        [ISO 639-1](/guides/api-calls/language-codes) format. Example: 'en'.
            is_sync_enabled (boolean): Whether the user can use Box Sync Example: 'True'.
            job_title (string): The user’s job title Example: 'CEO'.
            phone (string): The user’s phone number Example: '6509241374'.
            address (string): The user’s address Example: '900 Jefferson Ave, Redwood City, CA 94063'.
            tracking_codes (array): Tracking codes allow an admin to generate reports from the
        admin console and assign an attribute to a specific group
        of users. This setting must be enabled for an enterprise before it
        can be used.
            can_see_managed_users (boolean): Whether the user can see other enterprise users in their
        contact list Example: 'True'.
            timezone (string): The user's timezone Example: 'Africa/Bujumbura'.
            is_external_collab_restricted (boolean): Whether the user is allowed to collaborate with users outside
        their enterprise Example: 'True'.
            is_exempt_from_device_limits (boolean): Whether to exempt the user from enterprise device limits Example: 'True'.
            is_exempt_from_login_verification (boolean): Whether the user must use two-factor authentication Example: 'True'.
            is_password_reset_required (boolean): Whether the user is required to reset their password Example: 'True'.
            status (string): The user's account status Example: 'active'.
            space_amount (integer): The user’s total available space in bytes. Set this to `-1` to
        indicate unlimited storage. Example: '11345156112'.
            notification_email (object): An alternate notification email address to which email
        notifications are sent. When it's confirmed, this will be
        the email address to which notifications are sent instead of
        to the primary email address.

        Set this value to `null` to remove the notification email.
            external_app_user_id (string): An external identifier for an app user, which can be used to look
        up the user. This can be used to tie user IDs from external
        identity providers to Box users.

        Note: In order to update this field, you need to request a token
        using the application that created the app user. Example: 'my-user-1234'.

        Returns:
            dict[str, Any]: Returns the updated user object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        request_body_data = None
        request_body_data = {
            "enterprise": enterprise,
            "notify": notify,
            "name": name,
            "login": login,
            "role": role,
            "language": language,
            "is_sync_enabled": is_sync_enabled,
            "job_title": job_title,
            "phone": phone,
            "address": address,
            "tracking_codes": tracking_codes,
            "can_see_managed_users": can_see_managed_users,
            "timezone": timezone,
            "is_external_collab_restricted": is_external_collab_restricted,
            "is_exempt_from_device_limits": is_exempt_from_device_limits,
            "is_exempt_from_login_verification": is_exempt_from_login_verification,
            "is_password_reset_required": is_password_reset_required,
            "status": status,
            "space_amount": space_amount,
            "notification_email": notification_email,
            "external_app_user_id": external_app_user_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/{user_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_users_id(
        self, user_id: str, notify: bool | None = None, force: bool | None = None
    ) -> Any:
        """
        Delete user

        Args:
            user_id (string): user_id
            notify (boolean): Whether the user will receive email notification of
        the deletion Example: 'True'.
            force (boolean): Whether the user should be deleted even if this user
        still own files Example: 'True'.

        Returns:
            Any: Removes the user and returns an empty response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/users/{user_id}"
        query_params = {
            k: v for k, v in [("notify", notify), ("force", force)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_users_id_avatar(self, user_id: str) -> Any:
        """
        Get user avatar

        Args:
            user_id (string): user_id

        Returns:
            Any: When an avatar can be found for the user the
        image data will be returned in the body of the
        response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User avatars
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/users/{user_id}/avatar"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_users_id_avatar(
        self, user_id: str, pic: bytes | None = None
    ) -> dict[str, Any]:
        """
        Add or update user avatar

        Args:
            user_id (string): user_id
            pic (file (e.g., open('path/to/file', 'rb'))): The image file to be uploaded to Box.
        Accepted file extensions are `.jpg` or `.png`.
        The maximum file size is 1MB.

        Returns:
            dict[str, Any]: * `ok`: Returns the `pic_urls` object with URLs to existing
        user avatars that were updated.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User avatars
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        request_body_data = None
        files_data = None
        request_body_data = {}
        files_data = {}
        if pic is not None:
            files_data["pic"] = pic
        files_data = {k: v for k, v in files_data.items() if v is not None}
        if not files_data:
            files_data = None
        url = f"{self.base_url}/users/{user_id}/avatar"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            files=files_data,
            params=query_params,
            content_type="multipart/form-data",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_users_id_avatar(self, user_id: str) -> Any:
        """
        Delete user avatar

        Args:
            user_id (string): user_id

        Returns:
            Any: * `no_content`: Removes the avatar and returns an empty response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User avatars
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/users/{user_id}/avatar"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_users_id_folders(
        self,
        user_id: str,
        fields: list[str] | None = None,
        notify: bool | None = None,
        owned_by: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Transfer owned folders

        Args:
            user_id (string): user_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            notify (boolean): Determines if users should receive email notification
        for the action performed. Example: 'True'.
            owned_by (object): The user who the folder will be transferred to

        Returns:
            dict[str, Any]: Returns the information for the newly created
        destination folder.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Transfer folders
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        request_body_data = None
        request_body_data = {
            "owned_by": owned_by,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/{user_id}/folders/0"
        query_params = {
            k: v for k, v in [("fields", fields), ("notify", notify)] if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_users_id_email_aliases(self, user_id: str) -> dict[str, Any]:
        """
        List user's email aliases

        Args:
            user_id (string): user_id

        Returns:
            dict[str, Any]: Returns a collection of email aliases.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email aliases
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/users/{user_id}/email_aliases"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_users_id_email_aliases(
        self, user_id: str, email: str | None = None
    ) -> dict[str, Any]:
        """
        Create email alias

        Args:
            user_id (string): user_id
            email (string): The email address to add to the account as an alias.

        Note: The domain of the email alias needs to be registered
         to your enterprise.
        See the [domain verification guide](
          https://support.box.com/hc/en-us/articles/4408619650579-Domain-Verification
          ) for steps to add a new domain. Example: 'alias@example.com'.

        Returns:
            dict[str, Any]: Returns the newly created email alias object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email aliases
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        request_body_data = None
        request_body_data = {
            "email": email,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/{user_id}/email_aliases"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_email_alias_by_id(self, user_id: str, email_alias_id: str) -> Any:
        """
        Remove email alias

        Args:
            user_id (string): user_id
            email_alias_id (string): email_alias_id

        Returns:
            Any: Removes the alias and returns an empty response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email aliases
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        if email_alias_id is None:
            raise ValueError("Missing required parameter 'email_alias_id'.")
        url = f"{self.base_url}/users/{user_id}/email_aliases/{email_alias_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_users_id_memberships(
        self, user_id: str, limit: int | None = None, offset: int | None = None
    ) -> dict[str, Any]:
        """
        List user's groups

        Args:
            user_id (string): user_id
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of membership objects. If there are no
        memberships, an empty collection will be returned.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Group memberships
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/users/{user_id}/memberships"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_invites(
        self,
        fields: list[str] | None = None,
        enterprise: dict[str, Any] | None = None,
        actionable_by: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create user invite

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            enterprise (object): The enterprise to invite the user to
            actionable_by (object): The user to invite

        Returns:
            dict[str, Any]: Returns a new invite object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Invites
        """
        request_body_data = None
        request_body_data = {
            "enterprise": enterprise,
            "actionable_by": actionable_by,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/invites"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_invites_id(
        self, invite_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get user invite status

        Args:
            invite_id (string): invite_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns an invite object

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Invites
        """
        if invite_id is None:
            raise ValueError("Missing required parameter 'invite_id'.")
        url = f"{self.base_url}/invites/{invite_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_groups(
        self,
        filter_term: str | None = None,
        fields: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """
        List groups for enterprise

        Args:
            filter_term (string): Limits the results to only groups whose `name` starts
        with the search term. Example: 'Engineering'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of group objects. If there are no groups, an
        empty collection will be returned.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Groups
        """
        url = f"{self.base_url}/groups"
        query_params = {
            k: v
            for k, v in [
                ("filter_term", filter_term),
                ("fields", fields),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_groups(
        self,
        fields: list[str] | None = None,
        name: str | None = None,
        provenance: str | None = None,
        external_sync_identifier: str | None = None,
        description: str | None = None,
        invitability_level: str | None = None,
        member_viewability_level: str | None = None,
    ) -> dict[str, Any]:
        """
        Create group

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): The name of the new group to be created. This name must be unique
        within the enterprise. Example: 'Customer Support'.
            provenance (string): Keeps track of which external source this group is
        coming, for example `Active Directory`, or `Okta`.

        Setting this will also prevent Box admins from editing
        the group name and its members directly via the Box
        web application.

        This is desirable for one-way syncing of groups. Example: 'Active Directory'.
            external_sync_identifier (string): An arbitrary identifier that can be used by
        external group sync tools to link this Box Group to
        an external group.

        Example values of this field
        could be an **Active Directory Object ID** or a **Google
        Group ID**.

        We recommend you use of this field in
        order to avoid issues when group names are updated in
        either Box or external systems. Example: 'AD:123456'.
            description (string): A human readable description of the group. Example: '"Customer Support Group - as imported from Active Directory"'.
            invitability_level (string): Specifies who can invite the group to collaborate
        on folders.

        When set to `admins_only` the enterprise admin, co-admins,
        and the group's admin can invite the group.

        When set to `admins_and_members` all the admins listed
        above and group members can invite the group.

        When set to `all_managed_users` all managed users in the
        enterprise can invite the group. Example: 'admins_only'.
            member_viewability_level (string): Specifies who can see the members of the group.

        * `admins_only` - the enterprise admin, co-admins, group's
          group admin
        * `admins_and_members` - all admins and group members
        * `all_managed_users` - all managed users in the
          enterprise Example: 'admins_only'.

        Returns:
            dict[str, Any]: Returns the new group object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Groups
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "provenance": provenance,
            "external_sync_identifier": external_sync_identifier,
            "description": description,
            "invitability_level": invitability_level,
            "member_viewability_level": member_viewability_level,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/groups"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_groups_terminate_sessions(
        self, group_ids: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Create jobs to terminate user group session

        Args:
            group_ids (array): A list of group IDs Example: "['123456', '456789']".

        Returns:
            dict[str, Any]: Returns a message about the request status.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Session termination
        """
        request_body_data = None
        request_body_data = {
            "group_ids": group_ids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/groups/terminate_sessions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_groups_id(
        self, group_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get group

        Args:
            group_id (string): group_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the group object

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Groups
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'.")
        url = f"{self.base_url}/groups/{group_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_groups_id(
        self,
        group_id: str,
        fields: list[str] | None = None,
        name: str | None = None,
        provenance: str | None = None,
        external_sync_identifier: str | None = None,
        description: str | None = None,
        invitability_level: str | None = None,
        member_viewability_level: str | None = None,
    ) -> dict[str, Any]:
        """
        Update group

        Args:
            group_id (string): group_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            name (string): The name of the new group to be created. Must be unique within the
        enterprise. Example: 'Customer Support'.
            provenance (string): Keeps track of which external source this group is
        coming, for example `Active Directory`, or `Okta`.

        Setting this will also prevent Box admins from editing
        the group name and its members directly via the Box
        web application.

        This is desirable for one-way syncing of groups. Example: 'Active Directory'.
            external_sync_identifier (string): An arbitrary identifier that can be used by
        external group sync tools to link this Box Group to
        an external group.

        Example values of this field
        could be an **Active Directory Object ID** or a **Google
        Group ID**.

        We recommend you use of this field in
        order to avoid issues when group names are updated in
        either Box or external systems. Example: 'AD:123456'.
            description (string): A human readable description of the group. Example: '"Customer Support Group - as imported from Active Directory"'.
            invitability_level (string): Specifies who can invite the group to collaborate
        on folders.

        When set to `admins_only` the enterprise admin, co-admins,
        and the group's admin can invite the group.

        When set to `admins_and_members` all the admins listed
        above and group members can invite the group.

        When set to `all_managed_users` all managed users in the
        enterprise can invite the group. Example: 'admins_only'.
            member_viewability_level (string): Specifies who can see the members of the group.

        * `admins_only` - the enterprise admin, co-admins, group's
          group admin
        * `admins_and_members` - all admins and group members
        * `all_managed_users` - all managed users in the
          enterprise Example: 'admins_only'.

        Returns:
            dict[str, Any]: Returns the updated group object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Groups
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "provenance": provenance,
            "external_sync_identifier": external_sync_identifier,
            "description": description,
            "invitability_level": invitability_level,
            "member_viewability_level": member_viewability_level,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/groups/{group_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_groups_id(self, group_id: str) -> Any:
        """
        Remove group

        Args:
            group_id (string): group_id

        Returns:
            Any: A blank response is returned if the group was
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Groups
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'.")
        url = f"{self.base_url}/groups/{group_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_groups_id_memberships(
        self, group_id: str, limit: int | None = None, offset: int | None = None
    ) -> dict[str, Any]:
        """
        List members of group

        Args:
            group_id (string): group_id
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of membership objects. If there are no
        memberships, an empty collection will be returned.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Group memberships
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'.")
        url = f"{self.base_url}/groups/{group_id}/memberships"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_groups_id_collaborations(
        self, group_id: str, limit: int | None = None, offset: int | None = None
    ) -> dict[str, Any]:
        """
        List group collaborations

        Args:
            group_id (string): group_id
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of collaboration objects. If there are no
        collaborations, an empty collection will be returned.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collaborations (List)
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'.")
        url = f"{self.base_url}/groups/{group_id}/collaborations"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_group_memberships(
        self,
        fields: list[str] | None = None,
        user: dict[str, Any] | None = None,
        group: dict[str, Any] | None = None,
        role: str | None = None,
        configurable_permissions: dict[str, bool] | None = None,
    ) -> dict[str, Any]:
        """
        Add user to group

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            user (object): The user to add to the group.
            group (object): The group to add the user to.
            role (string): The role of the user in the group. Example: 'member'.
            configurable_permissions (object): Custom configuration for the permissions an admin
        if a group will receive. This option has no effect
        on members with a role of `member`.

        Setting these permissions overwrites the default
        access levels of an admin.

        Specifying a value of `null` for this object will disable
        all configurable permissions. Specifying permissions will set
        them accordingly, omitted permissions will be enabled by default. Example: "{'can_run_reports': True}".

        Returns:
            dict[str, Any]: Returns a new group membership object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Group memberships
        """
        request_body_data = None
        request_body_data = {
            "user": user,
            "group": group,
            "role": role,
            "configurable_permissions": configurable_permissions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/group_memberships"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_group_memberships_id(
        self, group_membership_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get group membership

        Args:
            group_membership_id (string): group_membership_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the group membership object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Group memberships
        """
        if group_membership_id is None:
            raise ValueError("Missing required parameter 'group_membership_id'.")
        url = f"{self.base_url}/group_memberships/{group_membership_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_group_memberships_id(
        self,
        group_membership_id: str,
        fields: list[str] | None = None,
        role: str | None = None,
        configurable_permissions: dict[str, bool] | None = None,
    ) -> dict[str, Any]:
        """
        Update group membership

        Args:
            group_membership_id (string): group_membership_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            role (string): The role of the user in the group. Example: 'member'.
            configurable_permissions (object): Custom configuration for the permissions an admin
        if a group will receive. This option has no effect
        on members with a role of `member`.

        Setting these permissions overwrites the default
        access levels of an admin.

        Specifying a value of `null` for this object will disable
        all configurable permissions. Specifying permissions will set
        them accordingly, omitted permissions will be enabled by default. Example: "{'can_run_reports': True}".

        Returns:
            dict[str, Any]: Returns a new group membership object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Group memberships
        """
        if group_membership_id is None:
            raise ValueError("Missing required parameter 'group_membership_id'.")
        request_body_data = None
        request_body_data = {
            "role": role,
            "configurable_permissions": configurable_permissions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/group_memberships/{group_membership_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_group_memberships_id(self, group_membership_id: str) -> Any:
        """
        Remove user from group

        Args:
            group_membership_id (string): group_membership_id

        Returns:
            Any: A blank response is returned if the membership was
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Group memberships
        """
        if group_membership_id is None:
            raise ValueError("Missing required parameter 'group_membership_id'.")
        url = f"{self.base_url}/group_memberships/{group_membership_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_webhooks(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List all webhooks

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list of webhooks.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Webhooks
        """
        url = f"{self.base_url}/webhooks"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_webhooks(
        self,
        target: dict[str, Any] | None = None,
        address: str | None = None,
        triggers: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Create webhook

        Args:
            target (object): The item that will trigger the webhook
            address (string): The URL that is notified by this webhook Example: 'https://example.com/webhooks'.
            triggers (array): An array of event names that this webhook is
        to be triggered for Example: "['FILE.UPLOADED']".

        Returns:
            dict[str, Any]: Returns the new webhook object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Webhooks
        """
        request_body_data = None
        request_body_data = {
            "target": target,
            "address": address,
            "triggers": triggers,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/webhooks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_webhooks_id(self, webhook_id: str) -> dict[str, Any]:
        """
        Get webhook

        Args:
            webhook_id (string): webhook_id

        Returns:
            dict[str, Any]: Returns a webhook object

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'.")
        url = f"{self.base_url}/webhooks/{webhook_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_webhooks_id(
        self,
        webhook_id: str,
        target: dict[str, Any] | None = None,
        address: str | None = None,
        triggers: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Update webhook

        Args:
            webhook_id (string): webhook_id
            target (object): The item that will trigger the webhook
            address (string): The URL that is notified by this webhook Example: 'https://example.com/webhooks'.
            triggers (array): An array of event names that this webhook is
        to be triggered for Example: "['FILE.UPLOADED']".

        Returns:
            dict[str, Any]: Returns the new webhook object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'.")
        request_body_data = None
        request_body_data = {
            "target": target,
            "address": address,
            "triggers": triggers,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/webhooks/{webhook_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_webhooks_id(self, webhook_id: str) -> Any:
        """
        Remove webhook

        Args:
            webhook_id (string): webhook_id

        Returns:
            Any: An empty response will be returned when the webhook
        was successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'.")
        url = f"{self.base_url}/webhooks/{webhook_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_skill_invocations_id(
        self,
        skill_id: str,
        status: str | None = None,
        metadata: dict[str, Any] | None = None,
        file: dict[str, Any] | None = None,
        file_version: dict[str, Any] | None = None,
        usage: dict[str, Any] | None = None,
    ) -> Any:
        """
        Update all Box Skill cards on file

        Args:
            skill_id (string): skill_id
            status (string): Defines the status of this invocation. Set this to `success` when setting Skill cards. Example: 'success'.
            metadata (object): The metadata to set for this skill. This is a list of
        Box Skills cards. These cards will overwrite any existing Box
        skill cards on the file.
            file (object): The file to assign the cards to.
            file_version (object): The optional file version to assign the cards to.
            usage (object): A descriptor that defines what items are affected by this call.

        Set this to the default values when setting a card to a `success`
        state, and leave it out in most other situations.

        Returns:
            Any: Returns an empty response when the card has been successfully updated.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Skills
        """
        if skill_id is None:
            raise ValueError("Missing required parameter 'skill_id'.")
        request_body_data = None
        request_body_data = {
            "status": status,
            "metadata": metadata,
            "file": file,
            "file_version": file_version,
            "usage": usage,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/skill_invocations/{skill_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def options_events(self) -> dict[str, Any]:
        """
        Get events long poll endpoint

        Returns:
            dict[str, Any]: Returns a paginated array of servers that can be used
        instead of the regular endpoints for long-polling events.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Events
        """
        request_body_data = None
        url = f"{self.base_url}/events"
        query_params = {}
        response = self._options(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_events(
        self,
        stream_type: str | None = None,
        stream_position: str | None = None,
        limit: int | None = None,
        event_type: list[str] | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
    ) -> dict[str, Any]:
        """
        List user and enterprise events

        Args:
            stream_type (string): Defines the type of events that are returned

        * `all` returns everything for a user and is the default
        * `changes` returns events that may cause file tree changes
          such as file updates or collaborations.
        * `sync` is similar to `changes` but only applies to synced folders
        * `admin_logs` returns all events for an entire enterprise and
          requires the user making the API call to have admin permissions. This
          stream type is for programmatically pulling from a 1 year history of
          events across all users within the enterprise and within a
          `created_after` and `created_before` time frame. The complete history
          of events will be returned in chronological order based on the event
          time, but latency will be much higher than `admin_logs_streaming`.
        * `admin_logs_streaming` returns all events for an entire enterprise and
          requires the user making the API call to have admin permissions. This
          stream type is for polling for recent events across all users within
          the enterprise. Latency will be much lower than `admin_logs`, but
          events will not be returned in chronological order and may
          contain duplicates. Example: 'all'.
            stream_position (string): The location in the event stream to start receiving events from.

        * `now` will return an empty list events and
        the latest stream position for initialization.
        * `0` or `null` will return all events. Example: '1348790499819'.
            limit (integer): Limits the number of events returned

        Note: Sometimes, the events less than the limit requested can be returned
        even when there may be more events remaining. This is primarily done in
        the case where a number of events have already been retrieved and these
        retrieved events are returned rather than delaying for an unknown amount
        of time to see if there are any more results. Example: '50'.
            event_type (array): A comma-separated list of events to filter by. This can only be used when
        requesting the events with a `stream_type` of `admin_logs` or
        `adming_logs_streaming`. For any other `stream_type` this value will be
        ignored. Example: "['ACCESS_GRANTED']".
            created_after (string): The lower bound date and time to return events for. This can only be used
        when requesting the events with a `stream_type` of `admin_logs`. For any
        other `stream_type` this value will be ignored. Example: '2012-12-12T10:53:43-08:00'.
            created_before (string): The upper bound date and time to return events for. This can only be used
        when requesting the events with a `stream_type` of `admin_logs`. For any
        other `stream_type` this value will be ignored. Example: '2013-12-12T10:53:43-08:00'.

        Returns:
            dict[str, Any]: Returns a list of event objects.

        Events objects are returned in pages, with each page (chunk)
        including a list of event objects. The response includes a
        `chunk_size` parameter indicating how many events were returned in this
        chunk, as well as the next `stream_position` that can be
        queried.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Events
        """
        url = f"{self.base_url}/events"
        query_params = {
            k: v
            for k, v in [
                ("stream_type", stream_type),
                ("stream_position", stream_position),
                ("limit", limit),
                ("event_type", event_type),
                ("created_after", created_after),
                ("created_before", created_before),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_collections(
        self,
        fields: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List all collections

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns all collections for the given user

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collections
        """
        url = f"{self.base_url}/collections"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("offset", offset), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_collections_id_items(
        self,
        collection_id: str,
        fields: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List collection items

        Args:
            collection_id (string): collection_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            offset (integer): The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response. Example: '1000'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns an array of items in the collection.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collections
        """
        if collection_id is None:
            raise ValueError("Missing required parameter 'collection_id'.")
        url = f"{self.base_url}/collections/{collection_id}/items"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("offset", offset), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_collections_id(self, collection_id: str) -> dict[str, Any]:
        """
        Get collection by ID

        Args:
            collection_id (string): collection_id

        Returns:
            dict[str, Any]: Returns an array of items in the collection.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Collections
        """
        if collection_id is None:
            raise ValueError("Missing required parameter 'collection_id'.")
        url = f"{self.base_url}/collections/{collection_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_recent_items(
        self,
        fields: list[str] | None = None,
        limit: int | None = None,
        marker: str | None = None,
    ) -> dict[str, Any]:
        """
        List recently accessed items

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.

        Returns:
            dict[str, Any]: Returns a list recent items access by a user.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Recent items
        """
        url = f"{self.base_url}/recent_items"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("limit", limit), ("marker", marker)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_retention_policies(
        self,
        policy_name: str | None = None,
        policy_type: str | None = None,
        created_by_user_id: str | None = None,
        fields: list[str] | None = None,
        limit: int | None = None,
        marker: str | None = None,
    ) -> dict[str, Any]:
        """
        List retention policies

        Args:
            policy_name (string): Filters results by a case sensitive prefix of the name of
        retention policies. Example: 'Sales Policy'.
            policy_type (string): Filters results by the type of retention policy. Example: 'finite'.
            created_by_user_id (string): Filters results by the ID of the user who created policy. Example: '21312321'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.

        Returns:
            dict[str, Any]: Returns a list retention policies in the enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policies
        """
        url = f"{self.base_url}/retention_policies"
        query_params = {
            k: v
            for k, v in [
                ("policy_name", policy_name),
                ("policy_type", policy_type),
                ("created_by_user_id", created_by_user_id),
                ("fields", fields),
                ("limit", limit),
                ("marker", marker),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_retention_policies(
        self,
        policy_name: str | None = None,
        description: str | None = None,
        policy_type: str | None = None,
        disposition_action: str | None = None,
        retention_length: Any | None = None,
        retention_type: str | None = None,
        can_owner_extend_retention: bool | None = None,
        are_owners_notified: bool | None = None,
        custom_notification_recipients: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Create retention policy

        Args:
            policy_name (string): The name for the retention policy Example: 'Some Policy Name'.
            description (string): The additional text description of the retention policy. Example: 'Policy to retain all reports for at least one month'.
            policy_type (string): The type of the retention policy. A retention
        policy type can either be `finite`, where a
        specific amount of time to retain the content is known
        upfront, or `indefinite`, where the amount of time
        to retain the content is still unknown. Example: 'finite'.
            disposition_action (string): The disposition action of the retention policy.
        `permanently_delete` deletes the content
        retained by the policy permanently.
        `remove_retention` lifts retention policy
        from the content, allowing it to be deleted
        by users once the retention policy has expired. Example: 'permanently_delete'.
            retention_length (string): The length of the retention policy. This value
        specifies the duration in days that the retention
        policy will be active for after being assigned to
        content.  If the policy has a `policy_type` of
        `indefinite`, the `retention_length` will also be
        `indefinite`. Example: '365'.
            retention_type (string): Specifies the retention type:

        * `modifiable`: You can modify the retention policy. For example,
        you can add or remove folders, shorten or lengthen
        the policy duration, or delete the assignment.
        Use this type if your retention policy
        is not related to any regulatory purposes.

        * `non_modifiable`: You can modify the retention policy
        only in a limited way: add a folder, lengthen the duration,
        retire the policy, change the disposition action
        or notification settings. You cannot perform other actions,
        such as deleting the assignment or shortening the
        policy duration. Use this type to ensure
        compliance with regulatory retention policies. Example: 'modifiable'.
            can_owner_extend_retention (boolean): Whether the owner of a file will be allowed to
        extend the retention. Example: 'True'.
            are_owners_notified (boolean): Whether owner and co-owners of a file are notified
        when the policy nears expiration. Example: 'True'.
            custom_notification_recipients (array): A list of users notified when
        the retention policy duration is about to end.

        Returns:
            dict[str, Any]: Returns a new retention policy object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policies
        """
        request_body_data = None
        request_body_data = {
            "policy_name": policy_name,
            "description": description,
            "policy_type": policy_type,
            "disposition_action": disposition_action,
            "retention_length": retention_length,
            "retention_type": retention_type,
            "can_owner_extend_retention": can_owner_extend_retention,
            "are_owners_notified": are_owners_notified,
            "custom_notification_recipients": custom_notification_recipients,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/retention_policies"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_retention_policies_id(
        self, retention_policy_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get retention policy

        Args:
            retention_policy_id (string): retention_policy_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the retention policy object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policies
        """
        if retention_policy_id is None:
            raise ValueError("Missing required parameter 'retention_policy_id'.")
        url = f"{self.base_url}/retention_policies/{retention_policy_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_retention_policies_id(
        self,
        retention_policy_id: str,
        policy_name: str | None = None,
        description: str | None = None,
        disposition_action: Any | None = None,
        retention_type: str | None = None,
        retention_length: Any | None = None,
        status: str | None = None,
        can_owner_extend_retention: bool | None = None,
        are_owners_notified: bool | None = None,
        custom_notification_recipients: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Update retention policy

        Args:
            retention_policy_id (string): retention_policy_id
            policy_name (string): The name for the retention policy Example: 'Some Policy Name'.
            description (string): The additional text description of the retention policy. Example: 'Policy to retain all reports for at least one month'.
            disposition_action (string): The disposition action of the retention policy.
        This action can be `permanently_delete`, which
        will cause the content retained by the policy
        to be permanently deleted, or `remove_retention`,
        which will lift the retention policy from the content,
        allowing it to be deleted by users,
        once the retention policy has expired.
        You can use `null` if you don't want to change `disposition_action`. Example: 'permanently_delete'.
            retention_type (string): Specifies the retention type:

        * `modifiable`: You can modify the retention policy. For example,
        you can add or remove folders, shorten or lengthen
        the policy duration, or delete the assignment.
        Use this type if your retention policy
        is not related to any regulatory purposes.
        * `non-modifiable`: You can modify the retention policy
        only in a limited way: add a folder, lengthen the duration,
        retire the policy, change the disposition action
        or notification settings. You cannot perform other actions,
        such as deleting the assignment or shortening the
        policy duration. Use this type to ensure
        compliance with regulatory retention policies.

        When updating a retention policy, you can use
        `non-modifiable` type only. You can convert a
        `modifiable` policy to `non-modifiable`, but
        not the other way around. Example: 'non-modifiable'.
            retention_length (string): The length of the retention policy. This value
        specifies the duration in days that the retention
        policy will be active for after being assigned to
        content.  If the policy has a `policy_type` of
        `indefinite`, the `retention_length` will also be
        `indefinite`. Example: '365'.
            status (string): Used to retire a retention policy.

        If not retiring a policy, do not include this parameter
        or set it to `null`. Example: 'retired'.
            can_owner_extend_retention (boolean): Determines if the owner of items under the policy
        can extend the retention when the original retention
        duration is about to end. Example: 'False'.
            are_owners_notified (boolean): Determines if owners and co-owners of items
        under the policy are notified when
        the retention duration is about to end. Example: 'False'.
            custom_notification_recipients (array): A list of users notified when the retention duration is about to end.

        Returns:
            dict[str, Any]: Returns the updated retention policy object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policies
        """
        if retention_policy_id is None:
            raise ValueError("Missing required parameter 'retention_policy_id'.")
        request_body_data = None
        request_body_data = {
            "policy_name": policy_name,
            "description": description,
            "disposition_action": disposition_action,
            "retention_type": retention_type,
            "retention_length": retention_length,
            "status": status,
            "can_owner_extend_retention": can_owner_extend_retention,
            "are_owners_notified": are_owners_notified,
            "custom_notification_recipients": custom_notification_recipients,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/retention_policies/{retention_policy_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_retention_policies_id(self, retention_policy_id: str) -> Any:
        """
        Delete retention policy

        Args:
            retention_policy_id (string): retention_policy_id

        Returns:
            Any: Returns an empty response when the policy has been deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policies
        """
        if retention_policy_id is None:
            raise ValueError("Missing required parameter 'retention_policy_id'.")
        url = f"{self.base_url}/retention_policies/{retention_policy_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_retention_policy_assignments(
        self,
        retention_policy_id: str,
        type: str | None = None,
        fields: list[str] | None = None,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List retention policy assignments

        Args:
            retention_policy_id (string): retention_policy_id
            type (string): The type of the retention policy assignment to retrieve. Example: 'metadata_template'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list of the retention policy assignments associated with the
        specified retention policy.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policy assignments
        """
        if retention_policy_id is None:
            raise ValueError("Missing required parameter 'retention_policy_id'.")
        url = f"{self.base_url}/retention_policies/{retention_policy_id}/assignments"
        query_params = {
            k: v
            for k, v in [
                ("type", type),
                ("fields", fields),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_retention_policy_assignment(
        self,
        policy_id: str | None = None,
        assign_to: dict[str, Any] | None = None,
        filter_fields: list[dict[str, Any]] | None = None,
        start_date_field: str | None = None,
    ) -> dict[str, Any]:
        """
        Assign retention policy

        Args:
            policy_id (string): The ID of the retention policy to assign Example: '173463'.
            assign_to (object): The item to assign the policy to
            filter_fields (array): If the `assign_to` type is `metadata_template`,
        then optionally add the `filter_fields` parameter which will
        require an array of objects with a field entry and a value entry.
        Currently only one object of `field` and `value` is supported.
            start_date_field (string): The date the retention policy assignment begins.

        If the `assigned_to` type is `metadata_template`,
        this field can be a date field's metadata attribute key id. Example: 'upload_date'.

        Returns:
            dict[str, Any]: Returns a new retention policy assignment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policy assignments
        """
        request_body_data = None
        request_body_data = {
            "policy_id": policy_id,
            "assign_to": assign_to,
            "filter_fields": filter_fields,
            "start_date_field": start_date_field,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/retention_policy_assignments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_retention_policy_assignment_by_id(
        self, retention_policy_assignment_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get retention policy assignment

        Args:
            retention_policy_assignment_id (string): retention_policy_assignment_id
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the retention policy assignment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policy assignments
        """
        if retention_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'retention_policy_assignment_id'."
            )
        url = f"{self.base_url}/retention_policy_assignments/{retention_policy_assignment_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_retention_policy_assignment_by_id(
        self, retention_policy_assignment_id: str
    ) -> Any:
        """
        Remove retention policy assignment

        Args:
            retention_policy_assignment_id (string): retention_policy_assignment_id

        Returns:
            Any: Returns an empty response when the policy assignment
        is successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policy assignments
        """
        if retention_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'retention_policy_assignment_id'."
            )
        url = f"{self.base_url}/retention_policy_assignments/{retention_policy_assignment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_under_retention(
        self,
        retention_policy_assignment_id: str,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Get files under retention

        Args:
            retention_policy_assignment_id (string): retention_policy_assignment_id
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list of files under retention that are associated with the
        specified retention policy assignment.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policy assignments
        """
        if retention_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'retention_policy_assignment_id'."
            )
        url = f"{self.base_url}/retention_policy_assignments/{retention_policy_assignment_id}/files_under_retention"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_retention_policy_assignment_file_versions(
        self,
        retention_policy_assignment_id: str,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Get file versions under retention

        Args:
            retention_policy_assignment_id (string): retention_policy_assignment_id
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list of file versions under retention that are associated with
        the specified retention policy assignment.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Retention policy assignments
        """
        if retention_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'retention_policy_assignment_id'."
            )
        url = f"{self.base_url}/retention_policy_assignments/{retention_policy_assignment_id}/file_versions_under_retention"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_legal_hold_policies(
        self,
        policy_name: str | None = None,
        fields: list[str] | None = None,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List all legal hold policies

        Args:
            policy_name (string): Limits results to policies for which the names start with
        this search term. This is a case-insensitive prefix. Example: 'Sales Policy'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list of legal hold policies.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policies
        """
        url = f"{self.base_url}/legal_hold_policies"
        query_params = {
            k: v
            for k, v in [
                ("policy_name", policy_name),
                ("fields", fields),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_legal_hold_policies(
        self,
        policy_name: str | None = None,
        description: str | None = None,
        filter_started_at: str | None = None,
        filter_ended_at: str | None = None,
        is_ongoing: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create legal hold policy

        Args:
            policy_name (string): The name of the policy. Example: 'Sales Policy'.
            description (string): A description for the policy. Example: 'A custom policy for the sales team'.
            filter_started_at (string): The filter start date.

        When this policy is applied using a `custodian` legal
        hold assignments, it will only apply to file versions
        created or uploaded inside of the
        date range. Other assignment types, such as folders and
        files, will ignore the date filter.

        Required if `is_ongoing` is set to `false`. Example: '2012-12-12T10:53:43-08:00'.
            filter_ended_at (string): The filter end date.

        When this policy is applied using a `custodian` legal
        hold assignments, it will only apply to file versions
        created or uploaded inside of the
        date range. Other assignment types, such as folders and
        files, will ignore the date filter.

        Required if `is_ongoing` is set to `false`. Example: '2012-12-18T10:53:43-08:00'.
            is_ongoing (boolean): Whether new assignments under this policy should
        continue applying to files even after initialization.

        When this policy is applied using a legal hold assignment,
        it will continue applying the policy to any new file versions
        even after it has been applied.

        For example, if a legal hold assignment is placed on a user
        today, and that user uploads a file tomorrow, that file will
        get held. This will continue until the policy is retired.

        Required if no filter dates are set. Example: 'True'.

        Returns:
            dict[str, Any]: Returns a new legal hold policy object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policies
        """
        request_body_data = None
        request_body_data = {
            "policy_name": policy_name,
            "description": description,
            "filter_started_at": filter_started_at,
            "filter_ended_at": filter_ended_at,
            "is_ongoing": is_ongoing,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/legal_hold_policies"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_legal_hold_policies_id(self, legal_hold_policy_id: str) -> dict[str, Any]:
        """
        Get legal hold policy

        Args:
            legal_hold_policy_id (string): legal_hold_policy_id

        Returns:
            dict[str, Any]: Returns a legal hold policy object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policies
        """
        if legal_hold_policy_id is None:
            raise ValueError("Missing required parameter 'legal_hold_policy_id'.")
        url = f"{self.base_url}/legal_hold_policies/{legal_hold_policy_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_legal_hold_policies_id(
        self,
        legal_hold_policy_id: str,
        policy_name: str | None = None,
        description: str | None = None,
        release_notes: str | None = None,
    ) -> dict[str, Any]:
        """
        Update legal hold policy

        Args:
            legal_hold_policy_id (string): legal_hold_policy_id
            policy_name (string): The name of the policy. Example: 'Sales Policy'.
            description (string): A description for the policy. Example: 'A custom policy for the sales team'.
            release_notes (string): Notes around why the policy was released. Example: 'Required for GDPR'.

        Returns:
            dict[str, Any]: Returns a new legal hold policy object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policies
        """
        if legal_hold_policy_id is None:
            raise ValueError("Missing required parameter 'legal_hold_policy_id'.")
        request_body_data = None
        request_body_data = {
            "policy_name": policy_name,
            "description": description,
            "release_notes": release_notes,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/legal_hold_policies/{legal_hold_policy_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_legal_hold_policies_id(self, legal_hold_policy_id: str) -> Any:
        """
        Remove legal hold policy

        Args:
            legal_hold_policy_id (string): legal_hold_policy_id

        Returns:
            Any: A blank response is returned if the policy was
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policies
        """
        if legal_hold_policy_id is None:
            raise ValueError("Missing required parameter 'legal_hold_policy_id'.")
        url = f"{self.base_url}/legal_hold_policies/{legal_hold_policy_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_legal_hold_policy_assignments(
        self,
        policy_id: str,
        assign_to_type: str | None = None,
        assign_to_id: str | None = None,
        marker: str | None = None,
        limit: int | None = None,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        List legal hold policy assignments

        Args:
            policy_id (string): The ID of the legal hold policy Example: '324432'.
            assign_to_type (string): Filters the results by the type of item the
        policy was applied to. Example: 'file'.
            assign_to_id (string): Filters the results by the ID of item the
        policy was applied to. Example: '1234323'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns a list of legal hold policy assignments.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policy assignments
        """
        url = f"{self.base_url}/legal_hold_policy_assignments"
        query_params = {
            k: v
            for k, v in [
                ("policy_id", policy_id),
                ("assign_to_type", assign_to_type),
                ("assign_to_id", assign_to_id),
                ("marker", marker),
                ("limit", limit),
                ("fields", fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def assign_legal_hold_policy(
        self,
        policy_id: str | None = None,
        assign_to: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Assign legal hold policy

        Args:
            policy_id (string): The ID of the policy to assign. Example: '123244'.
            assign_to (object): The item to assign the policy to

        Returns:
            dict[str, Any]: Returns a new legal hold policy assignment.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policy assignments
        """
        request_body_data = None
        request_body_data = {
            "policy_id": policy_id,
            "assign_to": assign_to,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/legal_hold_policy_assignments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_legal_hold_policy_assignment(
        self, legal_hold_policy_assignment_id: str
    ) -> dict[str, Any]:
        """
        Get legal hold policy assignment

        Args:
            legal_hold_policy_assignment_id (string): legal_hold_policy_assignment_id

        Returns:
            dict[str, Any]: Returns a legal hold policy object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policy assignments
        """
        if legal_hold_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'legal_hold_policy_assignment_id'."
            )
        url = f"{self.base_url}/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_legal_hold_assignment(self, legal_hold_policy_assignment_id: str) -> Any:
        """
        Unassign legal hold policy

        Args:
            legal_hold_policy_assignment_id (string): legal_hold_policy_assignment_id

        Returns:
            Any: A blank response is returned if the assignment was
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policy assignments
        """
        if legal_hold_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'legal_hold_policy_assignment_id'."
            )
        url = f"{self.base_url}/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_files_on_hold_by_legl_hld_polcy_asgnmt_id(
        self,
        legal_hold_policy_assignment_id: str,
        marker: str | None = None,
        limit: int | None = None,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        List files with current file versions for legal hold policy assignment

        Args:
            legal_hold_policy_assignment_id (string): legal_hold_policy_assignment_id
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the list of current file versions held under legal hold for a
        specific legal hold policy assignment.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policy assignments
        """
        if legal_hold_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'legal_hold_policy_assignment_id'."
            )
        url = f"{self.base_url}/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/files_on_hold"
        query_params = {
            k: v
            for k, v in [("marker", marker), ("limit", limit), ("fields", fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_file_version_retentions(
        self,
        file_id: str | None = None,
        file_version_id: str | None = None,
        policy_id: str | None = None,
        disposition_action: str | None = None,
        disposition_before: str | None = None,
        disposition_after: str | None = None,
        limit: int | None = None,
        marker: str | None = None,
    ) -> dict[str, Any]:
        """
        List file version retentions

        Args:
            file_id (string): Filters results by files with this ID. Example: '43123123'.
            file_version_id (string): Filters results by file versions with this ID. Example: '1'.
            policy_id (string): Filters results by the retention policy with this ID. Example: '982312'.
            disposition_action (string): Filters results by the retention policy with this disposition
        action. Example: 'permanently_delete'.
            disposition_before (string): Filters results by files that will have their disposition
        come into effect before this date. Example: '2012-12-12T10:53:43-08:00'.
            disposition_after (string): Filters results by files that will have their disposition
        come into effect after this date. Example: '2012-12-19T10:34:23-08:00'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.

        Returns:
            dict[str, Any]: Returns a list of all file version retentions for the enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File version retentions
        """
        url = f"{self.base_url}/file_version_retentions"
        query_params = {
            k: v
            for k, v in [
                ("file_id", file_id),
                ("file_version_id", file_version_id),
                ("policy_id", policy_id),
                ("disposition_action", disposition_action),
                ("disposition_before", disposition_before),
                ("disposition_after", disposition_after),
                ("limit", limit),
                ("marker", marker),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_legal_hold_file_versions_on_hold(
        self,
        legal_hold_policy_assignment_id: str,
        marker: str | None = None,
        limit: int | None = None,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        List previous file versions for legal hold policy assignment

        Args:
            legal_hold_policy_assignment_id (string): legal_hold_policy_assignment_id
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".

        Returns:
            dict[str, Any]: Returns the list of previous file versions held under legal hold for a
        specific legal hold policy assignment.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Legal hold policy assignments
        """
        if legal_hold_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'legal_hold_policy_assignment_id'."
            )
        url = f"{self.base_url}/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/file_versions_on_hold"
        query_params = {
            k: v
            for k, v in [("marker", marker), ("limit", limit), ("fields", fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_file_version_retentions_id(
        self, file_version_retention_id: str
    ) -> dict[str, Any]:
        """
        Get retention on file

        Args:
            file_version_retention_id (string): file_version_retention_id

        Returns:
            dict[str, Any]: Returns a file version retention object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File version retentions
        """
        if file_version_retention_id is None:
            raise ValueError("Missing required parameter 'file_version_retention_id'.")
        url = f"{self.base_url}/file_version_retentions/{file_version_retention_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_legal_hold(self, file_version_legal_hold_id: str) -> dict[str, Any]:
        """
        Get file version legal hold

        Args:
            file_version_legal_hold_id (string): file_version_legal_hold_id

        Returns:
            dict[str, Any]: Returns the legal hold policy assignments for the file version.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File version legal holds
        """
        if file_version_legal_hold_id is None:
            raise ValueError("Missing required parameter 'file_version_legal_hold_id'.")
        url = f"{self.base_url}/file_version_legal_holds/{file_version_legal_hold_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_file_version_legal_holds(
        self, policy_id: str, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List file version legal holds

        Args:
            policy_id (string): The ID of the legal hold policy to get the file version legal
        holds for. Example: '133870'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns the list of file version legal holds for a specific legal
        hold policy.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            File version legal holds
        """
        url = f"{self.base_url}/file_version_legal_holds"
        query_params = {
            k: v
            for k, v in [("policy_id", policy_id), ("marker", marker), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_information_barrier_by_id(
        self, shield_information_barrier_id: str
    ) -> dict[str, Any]:
        """
        Get shield information barrier with specified ID

        Args:
            shield_information_barrier_id (string): shield_information_barrier_id

        Returns:
            dict[str, Any]: Returns the shield information barrier object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barriers
        """
        if shield_information_barrier_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_id'."
            )
        url = f"{self.base_url}/shield_information_barriers/{shield_information_barrier_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def change_shield_status(
        self, id: str | None = None, status: str | None = None
    ) -> dict[str, Any]:
        """
        Add changed status of shield information barrier with specified ID

        Args:
            id (string): The ID of the shield information barrier. Example: '1910967'.
            status (string): The desired status for the shield information barrier. Example: 'pending'.

        Returns:
            dict[str, Any]: Returns the updated shield information barrier object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barriers
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "status": status,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_information_barriers/change_status"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_information_barriers(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List shield information barriers

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a paginated list of
        shield information barrier objects,
        empty list if currently no barrier.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barriers
        """
        url = f"{self.base_url}/shield_information_barriers"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_shield_barriers(self, enterprise: Any | None = None) -> dict[str, Any]:
        """
        Create shield information barrier

        Args:
            enterprise (string): The `type` and `id` of enterprise this barrier is under.

        Returns:
            dict[str, Any]: Returns a new shield information barrier object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barriers
        """
        request_body_data = None
        request_body_data = {
            "enterprise": enterprise,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_information_barriers"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_information_barrier_reports(
        self,
        shield_information_barrier_id: str,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List shield information barrier reports

        Args:
            shield_information_barrier_id (string): The ID of the shield information barrier. Example: '1910967'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a paginated list of shield information barrier report objects.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier reports
        """
        url = f"{self.base_url}/shield_information_barrier_reports"
        query_params = {
            k: v
            for k, v in [
                ("shield_information_barrier_id", shield_information_barrier_id),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def generate_shield_report(
        self, shield_information_barrier: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Create shield information barrier report

        Args:
            shield_information_barrier (object): A base representation of a
        shield information barrier object

        Returns:
            dict[str, Any]: Returns the shield information barrier report information object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier reports
        """
        request_body_data = None
        request_body_data = {
            "shield_information_barrier": shield_information_barrier,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_information_barrier_reports"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_report_by_id(
        self, shield_information_barrier_report_id: str
    ) -> dict[str, Any]:
        """
        Get shield information barrier report by ID

        Args:
            shield_information_barrier_report_id (string): shield_information_barrier_report_id

        Returns:
            dict[str, Any]: Returns the  shield information barrier report object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier reports
        """
        if shield_information_barrier_report_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_report_id'."
            )
        url = f"{self.base_url}/shield_information_barrier_reports/{shield_information_barrier_report_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_segment_by_id(
        self, shield_information_barrier_segment_id: str
    ) -> dict[str, Any]:
        """
        Get shield information barrier segment with specified ID

        Args:
            shield_information_barrier_segment_id (string): shield_information_barrier_segment_id

        Returns:
            dict[str, Any]: Returns the shield information barrier segment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segments
        """
        if shield_information_barrier_segment_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_segment_id'."
            )
        url = f"{self.base_url}/shield_information_barrier_segments/{shield_information_barrier_segment_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_shield_inft_barrier_sgmt_by_id(
        self, shield_information_barrier_segment_id: str
    ) -> Any:
        """
        Delete shield information barrier segment

        Args:
            shield_information_barrier_segment_id (string): shield_information_barrier_segment_id

        Returns:
            Any: Empty body in response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segments
        """
        if shield_information_barrier_segment_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_segment_id'."
            )
        url = f"{self.base_url}/shield_information_barrier_segments/{shield_information_barrier_segment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_shield_barrier_segment(
        self,
        shield_information_barrier_segment_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        """
        Update shield information barrier segment with specified ID

        Args:
            shield_information_barrier_segment_id (string): shield_information_barrier_segment_id
            name (string): The updated name for the shield information barrier segment. Example: 'Investment Banking'.
            description (string): The updated description for
        the shield information barrier segment. Example: "'Corporate division that engages in advisory_based\nfinancial transactions on behalf of individuals,\ncorporations, and governments.'".

        Returns:
            dict[str, Any]: Returns the updated shield information barrier segment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segments
        """
        if shield_information_barrier_segment_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_segment_id'."
            )
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_information_barrier_segments/{shield_information_barrier_segment_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_segments(
        self,
        shield_information_barrier_id: str,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List shield information barrier segments

        Args:
            shield_information_barrier_id (string): The ID of the shield information barrier. Example: '1910967'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a paginated list of shield information barrier segment objects.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segments
        """
        url = f"{self.base_url}/shield_information_barrier_segments"
        query_params = {
            k: v
            for k, v in [
                ("shield_information_barrier_id", shield_information_barrier_id),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_shield_barrier_segments(
        self,
        shield_information_barrier: dict[str, Any] | None = None,
        name: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        """
        Create shield information barrier segment

        Args:
            shield_information_barrier (object): A base representation of a
        shield information barrier object
            name (string): Name of the shield information barrier segment Example: 'Investment Banking'.
            description (string): Description of the shield information barrier segment Example: "'Corporate division that engages in\n advisory_based financial\ntransactions on behalf of individuals,\ncorporations, and governments.'".

        Returns:
            dict[str, Any]: Returns a new shield information barrier segment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segments
        """
        request_body_data = None
        request_body_data = {
            "shield_information_barrier": shield_information_barrier,
            "name": name,
            "description": description,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_information_barrier_segments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_infmt_barrier_sgmnt_member_by_id(
        self, shield_information_barrier_segment_member_id: str
    ) -> dict[str, Any]:
        """
        Get shield information barrier segment member by ID

        Args:
            shield_information_barrier_segment_member_id (string): shield_information_barrier_segment_member_id

        Returns:
            dict[str, Any]: Returns the shield information barrier segment member object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segment members
        """
        if shield_information_barrier_segment_member_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_segment_member_id'."
            )
        url = f"{self.base_url}/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_shield_member(
        self, shield_information_barrier_segment_member_id: str
    ) -> Any:
        """
        Delete shield information barrier segment member by ID

        Args:
            shield_information_barrier_segment_member_id (string): shield_information_barrier_segment_member_id

        Returns:
            Any: Returns an empty response if the
        segment member was deleted successfully.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segment members
        """
        if shield_information_barrier_segment_member_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_segment_member_id'."
            )
        url = f"{self.base_url}/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_infmt_barrier_sgmnt_members(
        self,
        shield_information_barrier_segment_id: str,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List shield information barrier segment members

        Args:
            shield_information_barrier_segment_id (string): The ID of the shield information barrier segment. Example: '3423'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a paginated list of
        shield information barrier segment member objects.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segment members
        """
        url = f"{self.base_url}/shield_information_barrier_segment_members"
        query_params = {
            k: v
            for k, v in [
                (
                    "shield_information_barrier_segment_id",
                    shield_information_barrier_segment_id,
                ),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def add_shield_members(
        self,
        type: str | None = None,
        shield_information_barrier: dict[str, Any] | None = None,
        shield_information_barrier_segment: dict[str, Any] | None = None,
        user: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create shield information barrier segment member

        Args:
            type (string): -| A type of the shield barrier segment member. Example: 'shield_information_barrier_segment_member'.
            shield_information_barrier (object): A base representation of a
        shield information barrier object
            shield_information_barrier_segment (object): The `type` and `id` of the
        requested shield information barrier segment.
            user (string): User to which restriction will be applied.

        Returns:
            dict[str, Any]: Returns a new shield information barrier segment member object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segment members
        """
        request_body_data = None
        request_body_data = {
            "type": type,
            "shield_information_barrier": shield_information_barrier,
            "shield_information_barrier_segment": shield_information_barrier_segment,
            "user": user,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_information_barrier_segment_members"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_barrier_segment_restriction_by_id(
        self, shield_information_barrier_segment_restriction_id: str
    ) -> dict[str, Any]:
        """
        Get shield information barrier segment restriction by ID

        Args:
            shield_information_barrier_segment_restriction_id (string): shield_information_barrier_segment_restriction_id

        Returns:
            dict[str, Any]: Returns the shield information barrier segment
        restriction object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segment restrictions
        """
        if shield_information_barrier_segment_restriction_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_segment_restriction_id'."
            )
        url = f"{self.base_url}/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_shield_restriction(
        self, shield_information_barrier_segment_restriction_id: str
    ) -> Any:
        """
        Delete shield information barrier segment restriction by ID

        Args:
            shield_information_barrier_segment_restriction_id (string): shield_information_barrier_segment_restriction_id

        Returns:
            Any: Empty body in response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segment restrictions
        """
        if shield_information_barrier_segment_restriction_id is None:
            raise ValueError(
                "Missing required parameter 'shield_information_barrier_segment_restriction_id'."
            )
        url = f"{self.base_url}/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_infmt_barrier_sgmnt_restrictions(
        self,
        shield_information_barrier_segment_id: str,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List shield information barrier segment restrictions

        Args:
            shield_information_barrier_segment_id (string): The ID of the shield information barrier segment. Example: '3423'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a paginated list of
        shield information barrier segment restriction objects.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segment restrictions
        """
        url = f"{self.base_url}/shield_information_barrier_segment_restrictions"
        query_params = {
            k: v
            for k, v in [
                (
                    "shield_information_barrier_segment_id",
                    shield_information_barrier_segment_id,
                ),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_shield_restrictions(
        self,
        type: str | None = None,
        shield_information_barrier: dict[str, Any] | None = None,
        shield_information_barrier_segment: dict[str, Any] | None = None,
        restricted_segment: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create shield information barrier segment restriction

        Args:
            type (string): The type of the shield barrier segment
        restriction for this member. Example: 'shield_information_barrier_segment_restriction'.
            shield_information_barrier (object): A base representation of a
        shield information barrier object
            shield_information_barrier_segment (object): The `type` and `id` of the requested
        shield information barrier segment.
            restricted_segment (object): The `type` and `id` of the restricted
        shield information barrier segment.

        Returns:
            dict[str, Any]: Returns the newly created Shield
        Information Barrier Segment Restriction object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield information barrier segment restrictions
        """
        request_body_data = None
        request_body_data = {
            "type": type,
            "shield_information_barrier": shield_information_barrier,
            "shield_information_barrier_segment": shield_information_barrier_segment,
            "restricted_segment": restricted_segment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_information_barrier_segment_restrictions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_device_pinners_id(self, device_pinner_id: str) -> dict[str, Any]:
        """
        Get device pin

        Args:
            device_pinner_id (string): device_pinner_id

        Returns:
            dict[str, Any]: Returns information about a single device pin.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Device pinners
        """
        if device_pinner_id is None:
            raise ValueError("Missing required parameter 'device_pinner_id'.")
        url = f"{self.base_url}/device_pinners/{device_pinner_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_device_pinners_id(self, device_pinner_id: str) -> Any:
        """
        Remove device pin

        Args:
            device_pinner_id (string): device_pinner_id

        Returns:
            Any: Returns an empty response when the pin has been deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Device pinners
        """
        if device_pinner_id is None:
            raise ValueError("Missing required parameter 'device_pinner_id'.")
        url = f"{self.base_url}/device_pinners/{device_pinner_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_device_pins(
        self,
        enterprise_id: str,
        marker: str | None = None,
        limit: int | None = None,
        direction: str | None = None,
    ) -> dict[str, Any]:
        """
        List enterprise device pins

        Args:
            enterprise_id (string): enterprise_id
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            direction (string): The direction to sort results in. This can be either in alphabetical ascending
        (`ASC`) or descending (`DESC`) order. Example: 'ASC'.

        Returns:
            dict[str, Any]: Returns a list of device pins for a given enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Device pinners
        """
        if enterprise_id is None:
            raise ValueError("Missing required parameter 'enterprise_id'.")
        url = f"{self.base_url}/enterprises/{enterprise_id}/device_pinners"
        query_params = {
            k: v
            for k, v in [("marker", marker), ("limit", limit), ("direction", direction)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_terms_of_services(self, tos_type: str | None = None) -> dict[str, Any]:
        """
        List terms of services

        Args:
            tos_type (string): Limits the results to the terms of service of the given type. Example: 'managed'.

        Returns:
            dict[str, Any]: Returns a collection of terms of service text and settings for the
        enterprise.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Terms of service
        """
        url = f"{self.base_url}/terms_of_services"
        query_params = {k: v for k, v in [("tos_type", tos_type)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_terms_of_services(
        self,
        status: str | None = None,
        tos_type: str | None = None,
        text: str | None = None,
    ) -> dict[str, Any]:
        """
        Create terms of service

        Args:
            status (string): Whether this terms of service is active. Example: 'enabled'.
            tos_type (string): The type of user to set the terms of
        service for. Example: 'managed'.
            text (string): The terms of service text to display to users.

        The text can be set to empty if the `status` is set to `disabled`. Example: 'By collaborating on this file you are accepting...'.

        Returns:
            dict[str, Any]: Returns a new task object

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Terms of service
        """
        request_body_data = None
        request_body_data = {
            "status": status,
            "tos_type": tos_type,
            "text": text,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/terms_of_services"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_terms_of_services_id(self, terms_of_service_id: str) -> dict[str, Any]:
        """
        Get terms of service

        Args:
            terms_of_service_id (string): terms_of_service_id

        Returns:
            dict[str, Any]: Returns a terms of service object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Terms of service
        """
        if terms_of_service_id is None:
            raise ValueError("Missing required parameter 'terms_of_service_id'.")
        url = f"{self.base_url}/terms_of_services/{terms_of_service_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_terms_of_services_id(
        self,
        terms_of_service_id: str,
        status: str | None = None,
        text: str | None = None,
    ) -> dict[str, Any]:
        """
        Update terms of service

        Args:
            terms_of_service_id (string): terms_of_service_id
            status (string): Whether this terms of service is active. Example: 'enabled'.
            text (string): The terms of service text to display to users.

        The text can be set to empty if the `status` is set to `disabled`. Example: 'By collaborating on this file you are accepting...'.

        Returns:
            dict[str, Any]: Returns an updated terms of service object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Terms of service
        """
        if terms_of_service_id is None:
            raise ValueError("Missing required parameter 'terms_of_service_id'.")
        request_body_data = None
        request_body_data = {
            "status": status,
            "text": text,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/terms_of_services/{terms_of_service_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_tos_user_statuses(
        self, tos_id: str, user_id: str | None = None
    ) -> dict[str, Any]:
        """
        List terms of service user statuses

        Args:
            tos_id (string): The ID of the terms of service. Example: '324234'.
            user_id (string): Limits results to the given user ID. Example: '123334'.

        Returns:
            dict[str, Any]: Returns a list of terms of service statuses.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Terms of service user statuses
        """
        url = f"{self.base_url}/terms_of_service_user_statuses"
        query_params = {
            k: v for k, v in [("tos_id", tos_id), ("user_id", user_id)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_terms_of_service_statuses(
        self,
        tos: dict[str, Any] | None = None,
        user: dict[str, Any] | None = None,
        is_accepted: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create terms of service status for new user

        Args:
            tos (object): The terms of service to set the status for.
            user (object): The user to set the status for.
            is_accepted (boolean): Whether the user has accepted the terms. Example: 'True'.

        Returns:
            dict[str, Any]: Returns a terms of service status object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Terms of service user statuses
        """
        request_body_data = None
        request_body_data = {
            "tos": tos,
            "user": user,
            "is_accepted": is_accepted,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/terms_of_service_user_statuses"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_terms_of_service_user_status_by_id(
        self, terms_of_service_user_status_id: str, is_accepted: bool | None = None
    ) -> dict[str, Any]:
        """
        Update terms of service status for existing user

        Args:
            terms_of_service_user_status_id (string): terms_of_service_user_status_id
            is_accepted (boolean): Whether the user has accepted the terms. Example: 'True'.

        Returns:
            dict[str, Any]: Returns the updated terms of service status object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Terms of service user statuses
        """
        if terms_of_service_user_status_id is None:
            raise ValueError(
                "Missing required parameter 'terms_of_service_user_status_id'."
            )
        request_body_data = None
        request_body_data = {
            "is_accepted": is_accepted,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/terms_of_service_user_statuses/{terms_of_service_user_status_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_collaboration_whitelist_entries(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List allowed collaboration domains

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of domains that are allowed for collaboration.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain restrictions for collaborations
        """
        url = f"{self.base_url}/collaboration_whitelist_entries"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_collaboration_whitelist_entry(
        self, domain: str | None = None, direction: str | None = None
    ) -> dict[str, Any]:
        """
        Add domain to list of allowed collaboration domains

        Args:
            domain (string): The domain to add to the list of allowed domains. Example: 'example.com'.
            direction (string): The direction in which to allow collaborations. Example: 'inbound'.

        Returns:
            dict[str, Any]: Returns a new entry on the list of allowed domains.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain restrictions for collaborations
        """
        request_body_data = None
        request_body_data = {
            "domain": domain,
            "direction": direction,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/collaboration_whitelist_entries"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_whitelist_entry_by_id(
        self, collaboration_whitelist_entry_id: str
    ) -> dict[str, Any]:
        """
        Get allowed collaboration domain

        Args:
            collaboration_whitelist_entry_id (string): collaboration_whitelist_entry_id

        Returns:
            dict[str, Any]: Returns an entry on the list of allowed domains.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain restrictions for collaborations
        """
        if collaboration_whitelist_entry_id is None:
            raise ValueError(
                "Missing required parameter 'collaboration_whitelist_entry_id'."
            )
        url = f"{self.base_url}/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_collaboration_whitelist_entry_by_id(
        self, collaboration_whitelist_entry_id: str
    ) -> Any:
        """
        Remove domain from list of allowed collaboration domains

        Args:
            collaboration_whitelist_entry_id (string): collaboration_whitelist_entry_id

        Returns:
            Any: A blank response is returned if the entry was
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain restrictions for collaborations
        """
        if collaboration_whitelist_entry_id is None:
            raise ValueError(
                "Missing required parameter 'collaboration_whitelist_entry_id'."
            )
        url = f"{self.base_url}/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_whitelist_targets(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List users exempt from collaboration domain restrictions

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of user exemptions.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain restrictions (User exemptions)
        """
        url = f"{self.base_url}/collaboration_whitelist_exempt_targets"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_collaboration_whitelist_exempt_target(
        self, user: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Create user exemption from collaboration domain restrictions

        Args:
            user (object): The user to exempt.

        Returns:
            dict[str, Any]: Returns a new exemption entry.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain restrictions (User exemptions)
        """
        request_body_data = None
        request_body_data = {
            "user": user,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/collaboration_whitelist_exempt_targets"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_exempt_target_by_id(
        self, collaboration_whitelist_exempt_target_id: str
    ) -> dict[str, Any]:
        """
        Get user exempt from collaboration domain restrictions

        Args:
            collaboration_whitelist_exempt_target_id (string): collaboration_whitelist_exempt_target_id

        Returns:
            dict[str, Any]: Returns the user's exempted from the list of collaboration domains.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain restrictions (User exemptions)
        """
        if collaboration_whitelist_exempt_target_id is None:
            raise ValueError(
                "Missing required parameter 'collaboration_whitelist_exempt_target_id'."
            )
        url = f"{self.base_url}/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_collab_whitelist_exempt_target_by_id(
        self, collaboration_whitelist_exempt_target_id: str
    ) -> Any:
        """
        Remove user from list of users exempt from domain restrictions

        Args:
            collaboration_whitelist_exempt_target_id (string): collaboration_whitelist_exempt_target_id

        Returns:
            Any: A blank response is returned if the exemption was
        successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain restrictions (User exemptions)
        """
        if collaboration_whitelist_exempt_target_id is None:
            raise ValueError(
                "Missing required parameter 'collaboration_whitelist_exempt_target_id'."
            )
        url = f"{self.base_url}/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_storage_policies(
        self,
        fields: list[str] | None = None,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List storage policies

        Args:
            fields (array): A comma-separated list of attributes to include in the
        response. This can be used to request fields that are
        not normally returned in a standard response.

        Be aware that specifying this parameter will have the
        effect that none of the standard fields are returned in
        the response unless explicitly specified, instead only
        fields for the mini representation are returned, additional
        to the fields requested. Example: "['id', 'type', 'name']".
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of storage policies.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Standard and Zones Storage Policies
        """
        url = f"{self.base_url}/storage_policies"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("marker", marker), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_storage_policies_id(self, storage_policy_id: str) -> dict[str, Any]:
        """
        Get storage policy

        Args:
            storage_policy_id (string): storage_policy_id

        Returns:
            dict[str, Any]: Returns a storage policy object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Standard and Zones Storage Policies
        """
        if storage_policy_id is None:
            raise ValueError("Missing required parameter 'storage_policy_id'.")
        url = f"{self.base_url}/storage_policies/{storage_policy_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_storage_policy_assignments(
        self, resolved_for_type: str, resolved_for_id: str, marker: str | None = None
    ) -> dict[str, Any]:
        """
        List storage policy assignments

        Args:
            resolved_for_type (string): The target type to return assignments for Example: 'user'.
            resolved_for_id (string): The ID of the user or enterprise to return assignments for Example: '984322'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.

        Returns:
            dict[str, Any]: Returns a collection of storage policies for
        the enterprise or user.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Standard and Zones Storage Policy Assignments
        """
        url = f"{self.base_url}/storage_policy_assignments"
        query_params = {
            k: v
            for k, v in [
                ("marker", marker),
                ("resolved_for_type", resolved_for_type),
                ("resolved_for_id", resolved_for_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_storage_policy_assignment(
        self,
        storage_policy: dict[str, Any] | None = None,
        assigned_to: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Assign storage policy

        Args:
            storage_policy (object): The storage policy to assign to the user or
        enterprise
            assigned_to (object): The user or enterprise to assign the storage
        policy to.

        Returns:
            dict[str, Any]: Returns the new storage policy assignment created.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Standard and Zones Storage Policy Assignments
        """
        request_body_data = None
        request_body_data = {
            "storage_policy": storage_policy,
            "assigned_to": assigned_to,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/storage_policy_assignments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_storage_policy_assignment(
        self, storage_policy_assignment_id: str
    ) -> dict[str, Any]:
        """
        Get storage policy assignment

        Args:
            storage_policy_assignment_id (string): storage_policy_assignment_id

        Returns:
            dict[str, Any]: Returns a storage policy assignment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Standard and Zones Storage Policy Assignments
        """
        if storage_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'storage_policy_assignment_id'."
            )
        url = (
            f"{self.base_url}/storage_policy_assignments/{storage_policy_assignment_id}"
        )
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_storage_policy_assignment(
        self,
        storage_policy_assignment_id: str,
        storage_policy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update storage policy assignment

        Args:
            storage_policy_assignment_id (string): storage_policy_assignment_id
            storage_policy (object): The storage policy to assign to the user or
        enterprise

        Returns:
            dict[str, Any]: Returns an updated storage policy assignment object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Standard and Zones Storage Policy Assignments
        """
        if storage_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'storage_policy_assignment_id'."
            )
        request_body_data = None
        request_body_data = {
            "storage_policy": storage_policy,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.base_url}/storage_policy_assignments/{storage_policy_assignment_id}"
        )
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_storage_policy_assignment(
        self, storage_policy_assignment_id: str
    ) -> Any:
        """
        Unassign storage policy

        Args:
            storage_policy_assignment_id (string): storage_policy_assignment_id

        Returns:
            Any: Returns an empty response when the storage policy
        assignment is successfully deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Standard and Zones Storage Policy Assignments
        """
        if storage_policy_assignment_id is None:
            raise ValueError(
                "Missing required parameter 'storage_policy_assignment_id'."
            )
        url = (
            f"{self.base_url}/storage_policy_assignments/{storage_policy_assignment_id}"
        )
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_zip_downloads(
        self,
        items: list[dict[str, Any]] | None = None,
        download_file_name: str | None = None,
    ) -> dict[str, Any]:
        """
        Create zip download

        Args:
            items (array): A list of items to add to the `zip` archive. These can
        be folders or files.
            download_file_name (string): The optional name of the `zip` archive. This name will be appended by the
        `.zip` file extension, for example `January Financials.zip`. Example: 'January Financials'.

        Returns:
            dict[str, Any]: If the `zip` archive is ready to be downloaded, the API will return a
        response that will include a `download_url`, a `status_url`, as well as
        any conflicts that might have occurred when creating the request.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Zip Downloads
        """
        request_body_data = None
        request_body_data = {
            "items": items,
            "download_file_name": download_file_name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/zip_downloads"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_zip_downloads_id_content(self, zip_download_id: str) -> Any:
        """
        Download zip archive

        Args:
            zip_download_id (string): zip_download_id

        Returns:
            Any: Returns the content of the items requested for this download, formatted as
        a stream of files and folders in a `zip` archive.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Zip Downloads
        """
        if zip_download_id is None:
            raise ValueError("Missing required parameter 'zip_download_id'.")
        url = f"{self.base_url}/zip_downloads/{zip_download_id}/content"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_zip_downloads_id_status(self, zip_download_id: str) -> dict[str, Any]:
        """
        Get zip download status

        Args:
            zip_download_id (string): zip_download_id

        Returns:
            dict[str, Any]: Returns the status of the `zip` archive that is being downloaded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Zip Downloads
        """
        if zip_download_id is None:
            raise ValueError("Missing required parameter 'zip_download_id'.")
        url = f"{self.base_url}/zip_downloads/{zip_download_id}/status"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_sign_requests_id_cancel(self, sign_request_id: str) -> dict[str, Any]:
        """
        Cancel Box Sign request

        Args:
            sign_request_id (string): sign_request_id

        Returns:
            dict[str, Any]: Returns a Sign Request object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Sign requests
        """
        if sign_request_id is None:
            raise ValueError("Missing required parameter 'sign_request_id'.")
        request_body_data = None
        url = f"{self.base_url}/sign_requests/{sign_request_id}/cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_sign_requests_id_resend(self, sign_request_id: str) -> Any:
        """
        Resend Box Sign request

        Args:
            sign_request_id (string): sign_request_id

        Returns:
            Any: Returns an empty response when the API call was successful.
        The email notifications will be sent asynchronously.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Sign requests
        """
        if sign_request_id is None:
            raise ValueError("Missing required parameter 'sign_request_id'.")
        request_body_data = None
        url = f"{self.base_url}/sign_requests/{sign_request_id}/resend"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_sign_requests_id(self, sign_request_id: str) -> dict[str, Any]:
        """
        Get Box Sign request by ID

        Args:
            sign_request_id (string): sign_request_id

        Returns:
            dict[str, Any]: Returns a signature request.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Sign requests
        """
        if sign_request_id is None:
            raise ValueError("Missing required parameter 'sign_request_id'.")
        url = f"{self.base_url}/sign_requests/{sign_request_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_sign_requests(
        self,
        marker: str | None = None,
        limit: int | None = None,
        senders: list[str] | None = None,
        shared_requests: bool | None = None,
    ) -> dict[str, Any]:
        """
        List Box Sign requests

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            senders (array): A list of sender emails to filter the signature requests by sender.
        If provided, `shared_requests` must be set to `true`. Example: "['sender1@boxdemo.com', 'sender2@boxdemo.com']".
            shared_requests (boolean): If set to `true`, only includes requests that user is not an owner,
        but user is a collaborator. Collaborator access is determined by the
        user access level of the sign files of the request.
        Default is `false`. Must be set to `true` if `senders` are provided. Example: 'True'.

        Returns:
            dict[str, Any]: Returns a collection of sign requests

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Sign requests
        """
        url = f"{self.base_url}/sign_requests"
        query_params = {
            k: v
            for k, v in [
                ("marker", marker),
                ("limit", limit),
                ("senders", senders),
                ("shared_requests", shared_requests),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_sign_requests(
        self,
        is_document_preparation_needed: bool | None = None,
        redirect_url: str | None = None,
        declined_redirect_url: str | None = None,
        are_text_signatures_enabled: bool | None = None,
        email_subject: str | None = None,
        email_message: str | None = None,
        are_reminders_enabled: bool | None = None,
        name: str | None = None,
        prefill_tags: list[dict[str, Any]] | None = None,
        days_valid: int | None = None,
        external_id: str | None = None,
        template_id: str | None = None,
        external_system_name: str | None = None,
        source_files: list[dict[str, Any]] | None = None,
        signature_color: str | None = None,
        signers: list[dict[str, Any]] | None = None,
        parent_folder: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create Box Sign request

        Args:
            is_document_preparation_needed (boolean): Indicates if the sender should receive a `prepare_url` in the response to complete document preparation using the UI. Example: 'True'.
            redirect_url (string): When specified, the signature request will be redirected to this url when a document is signed. Example: 'https://www.example.com'.
            declined_redirect_url (string): The uri that a signer will be redirected to after declining to sign a document. Example: 'https://declined-redirect.com'.
            are_text_signatures_enabled (boolean): Disables the usage of signatures generated by typing (text). Example: 'True'.
            email_subject (string): Subject of sign request email. This is cleaned by sign request. If this field is not passed, a default subject will be used. Example: 'Sign Request from Acme'.
            email_message (string): Message to include in sign request email. The field is cleaned through sanitization of specific characters. However, some html tags are allowed. Links included in the message are also converted to hyperlinks in the email. The message may contain the following html tags including `a`, `abbr`, `acronym`, `b`, `blockquote`, `code`, `em`, `i`, `ul`, `li`, `ol`, and `strong`. Be aware that when the text to html ratio is too high, the email may end up in spam filters. Custom styles on these tags are not allowed. If this field is not passed, a default message will be used. Example: 'Hello! Please sign the document below'.
            are_reminders_enabled (boolean): Reminds signers to sign a document on day 3, 8, 13 and 18. Reminders are only sent to outstanding signers. Example: 'True'.
            name (string): Name of the signature request. Example: 'name'.
            prefill_tags (array): When a document contains sign-related tags in the content, you can prefill them using this `prefill_tags` by referencing the 'id' of the tag as the `external_id` field of the prefill tag.
            days_valid (integer): Set the number of days after which the created signature request will automatically expire if not completed. By default, we do not apply any expiration date on signature requests, and the signature request does not expire. Example: '2'.
            external_id (string): This can be used to reference an ID in an external system that the sign request is related to. Example: '123'.
            template_id (string): When a signature request is created from a template this field will indicate the id of that template. Example: '123075213-af2c8822-3ef2-4952-8557-52d69c2fe9cb'.
            external_system_name (string): Used as an optional system name to appear in the signature log next to the signers who have been assigned the `embed_url_external_id`. Example: 'Box'.
            source_files (array): List of files to create a signing document from. This is currently limited to ten files. Only the ID and type fields are required for each file.
            signature_color (string): Force a specific color for the signature (blue, black, or red) Example: 'blue'.
            signers (array): Array of signers for the signature request. 35 is the
        max number of signers permitted.

        **Note**: It may happen that some signers belong to conflicting [segments](r://shield-information-barrier-segment-member) (user groups).
        This means that due to the security policies, users are assigned to segments to prevent exchanges or communication that could lead to ethical conflicts.
        In such a case, an attempt to send the sign request will result in an error.

        Read more about [segments and ethical walls](https://support.box.com/hc/en-us/articles/9920431507603-Understanding-Information-Barriers#h_01GFVJEHQA06N7XEZ4GCZ9GFAQ).
            parent_folder (string): parent_folder

        Returns:
            dict[str, Any]: Returns a Box Sign request object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Sign requests
        """
        request_body_data = None
        request_body_data = {
            "is_document_preparation_needed": is_document_preparation_needed,
            "redirect_url": redirect_url,
            "declined_redirect_url": declined_redirect_url,
            "are_text_signatures_enabled": are_text_signatures_enabled,
            "email_subject": email_subject,
            "email_message": email_message,
            "are_reminders_enabled": are_reminders_enabled,
            "name": name,
            "prefill_tags": prefill_tags,
            "days_valid": days_valid,
            "external_id": external_id,
            "template_id": template_id,
            "external_system_name": external_system_name,
            "source_files": source_files,
            "signature_color": signature_color,
            "signers": signers,
            "parent_folder": parent_folder,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/sign_requests"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_workflows(
        self,
        folder_id: str,
        trigger_type: str | None = None,
        limit: int | None = None,
        marker: str | None = None,
    ) -> dict[str, Any]:
        """
        List workflows

        Args:
            folder_id (string): The unique identifier that represent a folder.

        The ID for any folder can be determined
        by visiting this folder in the web application
        and copying the ID from the URL. For example,
        for the URL `https://*.app.box.com/folder/123`
        the `folder_id` is `123`.

        The root folder of a Box account is
        always represented by the ID `0`. Example: '12345'.
            trigger_type (string): Type of trigger to search for. Example: 'WORKFLOW_MANUAL_START'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.

        Returns:
            dict[str, Any]: Returns the workflow.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Workflows
        """
        url = f"{self.base_url}/workflows"
        query_params = {
            k: v
            for k, v in [
                ("folder_id", folder_id),
                ("trigger_type", trigger_type),
                ("limit", limit),
                ("marker", marker),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_workflows_id_start(
        self,
        workflow_id: str,
        type: str | None = None,
        flow: dict[str, Any] | None = None,
        files: list[dict[str, Any]] | None = None,
        folder: dict[str, Any] | None = None,
        outcomes: list[dict[str, Any]] | None = None,
    ) -> Any:
        """
        Starts workflow based on request body

        Args:
            workflow_id (string): workflow_id
            type (string): The type of the parameters object Example: 'workflow_parameters'.
            flow (object): The flow that will be triggered
            files (array): The array of files for which the workflow should start. All files
        must be in the workflow's configured folder.
            folder (object): The folder object for which the workflow is configured.
            outcomes (array): A configurable outcome the workflow should complete.

        Returns:
            Any: Starts the workflow.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Workflows
        """
        if workflow_id is None:
            raise ValueError("Missing required parameter 'workflow_id'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "flow": flow,
            "files": files,
            "folder": folder,
            "outcomes": outcomes,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/workflows/{workflow_id}/start"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_sign_templates(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List Box Sign templates

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of templates.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Sign templates
        """
        url = f"{self.base_url}/sign_templates"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_sign_templates_id(self, template_id: str) -> dict[str, Any]:
        """
        Get Box Sign template by ID

        Args:
            template_id (string): template_id

        Returns:
            dict[str, Any]: Returns details of a template.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Sign templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'.")
        url = f"{self.base_url}/sign_templates/{template_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_integration_mappings_slack(
        self,
        marker: str | None = None,
        limit: int | None = None,
        partner_item_type: str | None = None,
        partner_item_id: str | None = None,
        box_item_id: str | None = None,
        box_item_type: str | None = None,
        is_manually_created: bool | None = None,
    ) -> dict[str, Any]:
        """
        List Slack integration mappings

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.
            partner_item_type (string): Mapped item type, for which the mapping should be returned Example: 'channel'.
            partner_item_id (string): ID of the mapped item, for which the mapping should be returned Example: '12345'.
            box_item_id (string): Box item ID, for which the mappings should be returned Example: '12345'.
            box_item_type (string): Box item type, for which the mappings should be returned Example: 'folder'.
            is_manually_created (boolean): Whether the mapping has been manually created Example: 'True'.

        Returns:
            dict[str, Any]: Returns a collection of integration mappings

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Integration mappings
        """
        url = f"{self.base_url}/integration_mappings/slack"
        query_params = {
            k: v
            for k, v in [
                ("marker", marker),
                ("limit", limit),
                ("partner_item_type", partner_item_type),
                ("partner_item_id", partner_item_id),
                ("box_item_id", box_item_id),
                ("box_item_type", box_item_type),
                ("is_manually_created", is_manually_created),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_slack_mapping(
        self,
        partner_item: Any | None = None,
        box_item: Any | None = None,
        options: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create Slack integration mapping

        Args:
            partner_item (string): partner_item
            box_item (string): box_item
            options (string): options

        Returns:
            dict[str, Any]: Returns the created integration mapping.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Integration mappings
        """
        request_body_data = None
        request_body_data = {
            "partner_item": partner_item,
            "box_item": box_item,
            "options": options,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/integration_mappings/slack"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_slack_integration_mapping_by_id(
        self,
        integration_mapping_id: str,
        box_item: Any | None = None,
        options: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update Slack integration mapping

        Args:
            integration_mapping_id (string): integration_mapping_id
            box_item (string): box_item
            options (string): options

        Returns:
            dict[str, Any]: Returns the updated integration mapping object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Integration mappings
        """
        if integration_mapping_id is None:
            raise ValueError("Missing required parameter 'integration_mapping_id'.")
        request_body_data = None
        request_body_data = {
            "box_item": box_item,
            "options": options,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/integration_mappings/slack/{integration_mapping_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_slack_mapping_by_id(self, integration_mapping_id: str) -> Any:
        """
        Delete Slack integration mapping

        Args:
            integration_mapping_id (string): integration_mapping_id

        Returns:
            Any: Empty body in response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Integration mappings
        """
        if integration_mapping_id is None:
            raise ValueError("Missing required parameter 'integration_mapping_id'.")
        url = f"{self.base_url}/integration_mappings/slack/{integration_mapping_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_integration_mappings_teams(
        self,
        partner_item_type: str | None = None,
        partner_item_id: str | None = None,
        box_item_id: str | None = None,
        box_item_type: str | None = None,
    ) -> dict[str, Any]:
        """
        List Teams integration mappings

        Args:
            partner_item_type (string): Mapped item type, for which the mapping should be returned Example: 'channel'.
            partner_item_id (string): ID of the mapped item, for which the mapping should be returned Example: '12345'.
            box_item_id (string): Box item ID, for which the mappings should be returned Example: '12345'.
            box_item_type (string): Box item type, for which the mappings should be returned Example: 'folder'.

        Returns:
            dict[str, Any]: Returns a collection of integration mappings

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Integration mappings
        """
        url = f"{self.base_url}/integration_mappings/teams"
        query_params = {
            k: v
            for k, v in [
                ("partner_item_type", partner_item_type),
                ("partner_item_id", partner_item_id),
                ("box_item_id", box_item_id),
                ("box_item_type", box_item_type),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_integration_mapping_team(
        self, partner_item: Any | None = None, box_item: Any | None = None
    ) -> dict[str, Any]:
        """
        Create Teams integration mapping

        Args:
            partner_item (string): partner_item
            box_item (string): box_item

        Returns:
            dict[str, Any]: Returns the created integration mapping.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Integration mappings
        """
        request_body_data = None
        request_body_data = {
            "partner_item": partner_item,
            "box_item": box_item,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/integration_mappings/teams"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_integration_mapping_team(
        self, integration_mapping_id: str, box_item: Any | None = None
    ) -> dict[str, Any]:
        """
        Update Teams integration mapping

        Args:
            integration_mapping_id (string): integration_mapping_id
            box_item (string): box_item

        Returns:
            dict[str, Any]: Returns the updated integration mapping object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Integration mappings
        """
        if integration_mapping_id is None:
            raise ValueError("Missing required parameter 'integration_mapping_id'.")
        request_body_data = None
        request_body_data = {
            "box_item": box_item,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/integration_mappings/teams/{integration_mapping_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_integration_mapping_by_id(self, integration_mapping_id: str) -> Any:
        """
        Delete Teams integration mapping

        Args:
            integration_mapping_id (string): integration_mapping_id

        Returns:
            Any: Empty body in response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Integration mappings
        """
        if integration_mapping_id is None:
            raise ValueError("Missing required parameter 'integration_mapping_id'.")
        url = f"{self.base_url}/integration_mappings/teams/{integration_mapping_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_ai_ask(
        self,
        mode: str | None = None,
        prompt: str | None = None,
        items: list[dict[str, Any]] | None = None,
        dialogue_history: list[dict[str, Any]] | None = None,
        include_citations: bool | None = None,
        ai_agent: Any | None = None,
    ) -> dict[str, Any]:
        """
        Ask question

        Args:
            mode (string): Box AI handles text documents with text representations up to 1MB in size, or a maximum of 25 files, whichever comes first. If the text file size exceeds 1MB, the first 1MB of text representation will be processed. Box AI handles image documents with a resolution of 1024 x 1024 pixels, with a maximum of 5 images or 5 pages for multi-page images. If the number of image or image pages exceeds 5, the first 5 images or pages will be processed. If you set mode parameter to `single_item_qa`, the items array can have one element only. Currently Box AI does not support multi-modal requests. If both images and text are sent Box AI will only process the text. Example: 'multiple_item_qa'.
            prompt (string): The prompt provided by the client to be answered by the LLM. The prompt's length is limited to 10000 characters. Example: 'What is the value provided by public APIs based on this document?'.
            items (array): The items to be processed by the LLM, often files.
            dialogue_history (array): The history of prompts and answers previously passed to the LLM. This provides additional context to the LLM in generating the response.
            include_citations (boolean): A flag to indicate whether citations should be returned. Example: 'True'.
            ai_agent (string): ai_agent

        Returns:
            dict[str, Any]: A successful response including the answer from the LLM.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI
        """
        request_body_data = None
        request_body_data = {
            "mode": mode,
            "prompt": prompt,
            "items": items,
            "dialogue_history": dialogue_history,
            "include_citations": include_citations,
            "ai_agent": ai_agent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/ai/ask"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_ai_text_gen(
        self,
        prompt: str | None = None,
        items: list[dict[str, Any]] | None = None,
        dialogue_history: list[dict[str, Any]] | None = None,
        ai_agent: Any | None = None,
    ) -> dict[str, Any]:
        """
        Generate text

        Args:
            prompt (string): The prompt provided by the client to be answered by the LLM. The prompt's length is limited to 10000 characters. Example: 'Write an email to a client about the importance of public APIs.'.
            items (array): The items to be processed by the LLM, often files.
        The array can include **exactly one** element.

        **Note**: Box AI handles documents with text representations up to 1MB in size.
        If the file size exceeds 1MB, the first 1MB of text representation will be processed.
            dialogue_history (array): The history of prompts and answers previously passed to the LLM. This parameter provides the additional context to the LLM when generating the response.
            ai_agent (string): ai_agent

        Returns:
            dict[str, Any]: A successful response including the answer from the LLM.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI
        """
        request_body_data = None
        request_body_data = {
            "prompt": prompt,
            "items": items,
            "dialogue_history": dialogue_history,
            "ai_agent": ai_agent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/ai/text_gen"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_ai_agent_default(
        self, mode: str, language: str | None = None, model: str | None = None
    ) -> Any:
        """
        Get AI agent default configuration

        Args:
            mode (string): The mode to filter the agent config to return. Example: 'ask'.
            language (string): The ISO language code to return the agent config for.
        If the language is not supported the default agent config is returned. Example: 'ja'.
            model (string): The model to return the default agent config for. Example: 'azure__openai__gpt_4o_mini'.

        Returns:
            Any: A successful response including the default agent configuration.
        This response can be one of the following four objects:
        * AI agent for questions
        * AI agent for text generation
        * AI agent for freeform metadata extraction
        * AI agent for structured metadata extraction.
        The response depends on the agent configuration requested in this endpoint.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI
        """
        url = f"{self.base_url}/ai_agent_default"
        query_params = {
            k: v
            for k, v in [("mode", mode), ("language", language), ("model", model)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_ai_extract(
        self,
        prompt: str | None = None,
        items: list[dict[str, Any]] | None = None,
        ai_agent: Any | None = None,
    ) -> dict[str, Any]:
        """
        Extract metadata (freeform)

        Args:
            prompt (string): The prompt provided to a Large Language Model (LLM) in the request. The prompt can be up to 10000 characters long and it can be an XML or a JSON schema. Example: '\\"fields\\":[{\\"type\\":\\"string\\",\\"key\\":\\"name\\",\\"displayName\\":\\"Name\\",\\"description\\":\\"The customer name\\",\\"prompt\\":\\"Name is always the first word in the document\\"},{\\"type\\":\\"date\\",\\"key\\":\\"last_contacted_at\\",\\"displayName\\":\\"Last Contacted At\\",\\"description\\":\\"When this customer was last contacted at\\"}]'.
            items (array): The items that LLM will process. Currently, you can use files only.
            ai_agent (string): ai_agent

        Returns:
            dict[str, Any]: A response including the answer from the LLM.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI
        """
        request_body_data = None
        request_body_data = {
            "prompt": prompt,
            "items": items,
            "ai_agent": ai_agent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/ai/extract"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_ai_extract_structured(
        self,
        items: list[dict[str, Any]] | None = None,
        metadata_template: dict[str, Any] | None = None,
        fields: list[dict[str, Any]] | None = None,
        ai_agent: Any | None = None,
    ) -> dict[str, Any]:
        """
        Extract metadata (structured)

        Args:
            items (array): The items to be processed by the LLM. Currently you can use files only.
            metadata_template (object): The metadata template containing the fields to extract.
        For your request to work, you must provide either `metadata_template` or `fields`, but not both.
            fields (array): The fields to be extracted from the provided items.
        For your request to work, you must provide either `metadata_template` or `fields`, but not both.
            ai_agent (string): ai_agent

        Returns:
            dict[str, Any]: A successful response including the answer from the LLM.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI
        """
        request_body_data = None
        request_body_data = {
            "items": items,
            "metadata_template": metadata_template,
            "fields": fields,
            "ai_agent": ai_agent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/ai/extract_structured"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_ai_agents(
        self,
        mode: list[str] | None = None,
        fields: list[str] | None = None,
        agent_state: list[str] | None = None,
        include_box_default: bool | None = None,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List AI agents

        Args:
            mode (array): The mode to filter the agent config to return. Possible values are: `ask`, `text_gen`, and `extract`. Example: "['ask', 'text_gen', 'extract']".
            fields (array): The fields to return in the response. Example: "['ask', 'text_gen', 'extract']".
            agent_state (array): The state of the agents to return. Possible values are: `enabled`, `disabled` and `enabled_for_selected_users`. Example: "['enabled']".
            include_box_default (boolean): Whether to include the Box default agents in the response. Example: 'True'.
            marker (string): Defines the position marker at which to begin returning results. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: A successful response including the agents list.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI Studio, important
        """
        url = f"{self.base_url}/ai_agents"
        query_params = {
            k: v
            for k, v in [
                ("mode", mode),
                ("fields", fields),
                ("agent_state", agent_state),
                ("include_box_default", include_box_default),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_ai_agents(
        self,
        type: str | None = None,
        name: str | None = None,
        access_state: str | None = None,
        icon_reference: str | None = None,
        allowed_entities: list[dict[str, Any]] | None = None,
        ask: dict[str, Any] | None = None,
        text_gen: dict[str, Any] | None = None,
        extract: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create AI agent

        Args:
            type (string): The type of agent used to handle queries. Example: 'ai_agent'.
            name (string): The name of the AI Agent. Example: 'My AI Agent'.
            access_state (string): The state of the AI Agent. Possible values are: `enabled`, `disabled`, and `enabled_for_selected_users`. Example: 'enabled'.
            icon_reference (string): The icon reference of the AI Agent. It should have format of the URL `https://cdn01.boxcdn.net/app-assets/aistudio/avatars/<file_name>`
        where possible values of `file_name` are: `logo_boxAi.png`,`logo_stamp.png`,`logo_legal.png`,`logo_finance.png`,`logo_config.png`,`logo_handshake.png`,`logo_analytics.png`,`logo_classification.png` Example: 'https://cdn01.boxcdn.net/app-assets/aistudio/avatars/logo_analytics.svg'.
            allowed_entities (array): List of allowed users or groups.
            ask (object): The AI Agent to be used for ask.
            text_gen (object): The AI agent used for generating text.
            extract (object): The AI Agent to be used for extraction.

        Returns:
            dict[str, Any]: Definition of created AI agent.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI Studio
        """
        request_body_data = None
        request_body_data = {
            "type": type,
            "name": name,
            "access_state": access_state,
            "icon_reference": icon_reference,
            "allowed_entities": allowed_entities,
            "ask": ask,
            "text_gen": text_gen,
            "extract": extract,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/ai_agents"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_ai_agents_id(
        self,
        agent_id: str,
        type: str | None = None,
        name: str | None = None,
        access_state: str | None = None,
        icon_reference: str | None = None,
        allowed_entities: list[dict[str, Any]] | None = None,
        ask: dict[str, Any] | None = None,
        text_gen: dict[str, Any] | None = None,
        extract: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update AI agent

        Args:
            agent_id (string): agent_id
            type (string): The type of agent used to handle queries. Example: 'ai_agent'.
            name (string): The name of the AI Agent. Example: 'My AI Agent'.
            access_state (string): The state of the AI Agent. Possible values are: `enabled`, `disabled`, and `enabled_for_selected_users`. Example: 'enabled'.
            icon_reference (string): The icon reference of the AI Agent. It should have format of the URL `https://cdn01.boxcdn.net/app-assets/aistudio/avatars/<file_name>`
        where possible values of `file_name` are: `logo_boxAi.png`,`logo_stamp.png`,`logo_legal.png`,`logo_finance.png`,`logo_config.png`,`logo_handshake.png`,`logo_analytics.png`,`logo_classification.png` Example: 'https://cdn01.boxcdn.net/app-assets/aistudio/avatars/logo_analytics.svg'.
            allowed_entities (array): List of allowed users or groups.
            ask (object): The AI Agent to be used for ask.
            text_gen (object): The AI agent used for generating text.
            extract (object): The AI Agent to be used for extraction.

        Returns:
            dict[str, Any]: Definition of created AI agent.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI Studio
        """
        if agent_id is None:
            raise ValueError("Missing required parameter 'agent_id'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "name": name,
            "access_state": access_state,
            "icon_reference": icon_reference,
            "allowed_entities": allowed_entities,
            "ask": ask,
            "text_gen": text_gen,
            "extract": extract,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/ai_agents/{agent_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_ai_agents_id(
        self, agent_id: str, fields: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Get AI agent by agent ID

        Args:
            agent_id (string): agent_id
            fields (array): The fields to return in the response. Example: "['ask', 'text_gen', 'extract']".

        Returns:
            dict[str, Any]: A successful response including the agent.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI Studio
        """
        if agent_id is None:
            raise ValueError("Missing required parameter 'agent_id'.")
        url = f"{self.base_url}/ai_agents/{agent_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_ai_agents_id(self, agent_id: str) -> Any:
        """
        Delete AI agent

        Args:
            agent_id (string): agent_id

        Returns:
            Any: A successful response with no content.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            AI Studio
        """
        if agent_id is None:
            raise ValueError("Missing required parameter 'agent_id'.")
        url = f"{self.base_url}/ai_agents/{agent_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_docgen_templates_v(self, file: Any) -> dict[str, Any]:
        """
        Create Box Doc Gen template

        Args:
            file (string): file

        Returns:
            dict[str, Any]: The file which has now been marked as a Box Doc Gen template.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen templates
        """
        request_body_data = None
        request_body_data = {
            "file": file,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/docgen_templates"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_docgen_templates_v(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List Box Doc Gen templates

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a collection of templates.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen templates
        """
        url = f"{self.base_url}/docgen_templates"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_template_by_id(self, template_id: str) -> Any:
        """
        Delete Box Doc Gen template

        Args:
            template_id (string): template_id

        Returns:
            Any: Returns an empty response when a file is no longer marked as a Box Doc Gen template.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'.")
        url = f"{self.base_url}/docgen_templates/{template_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_docgen_template_by_id(self, template_id: str) -> dict[str, Any]:
        """
        Get Box Doc Gen template by ID

        Args:
            template_id (string): template_id

        Returns:
            dict[str, Any]: Returns a template.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'.")
        url = f"{self.base_url}/docgen_templates/{template_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_docgen_template_tags(
        self,
        template_id: str,
        template_version_id: str | None = None,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        List all Box Doc Gen template tags in template

        Args:
            template_id (string): template_id
            template_version_id (string): Id of template version. Example: '123'.
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: A list of document generation template tags.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'.")
        url = f"{self.base_url}/docgen_templates/{template_id}/tags"
        query_params = {
            k: v
            for k, v in [
                ("template_version_id", template_version_id),
                ("marker", marker),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_docgen_jobs_id_v(self, job_id: str) -> dict[str, Any]:
        """
        Get Box Doc Gen job by ID

        Args:
            job_id (string): job_id

        Returns:
            dict[str, Any]: Details of the Box Doc Gen job.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'.")
        url = f"{self.base_url}/docgen_jobs/{job_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_docgen_jobs_v(
        self, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        List all Box Doc Gen jobs

        Args:
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: A list of Box Doc Gen jobs.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen
        """
        url = f"{self.base_url}/docgen_jobs"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_template_job(
        self,
        template_id: str,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Get list of all Box Doc Gen jobs for template

        Args:
            template_id (string): template_id
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: A single Box Doc Gen template.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'.")
        url = f"{self.base_url}/docgen_template_jobs/{template_id}"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_batch_job_details(
        self, batch_id: str, marker: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        Get Box Doc Gen jobs by batch ID

        Args:
            batch_id (string): batch_id
            marker (string): Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`. Example: 'JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii'.
            limit (integer): The maximum number of items to return per page. Example: '1000'.

        Returns:
            dict[str, Any]: Returns a list of Box Doc Gen jobs in a Box Doc Gen batch.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen
        """
        if batch_id is None:
            raise ValueError("Missing required parameter 'batch_id'.")
        url = f"{self.base_url}/docgen_batch_jobs/{batch_id}"
        query_params = {
            k: v for k, v in [("marker", marker), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_docgen_batches_v(
        self,
        file: Any,
        input_source: str,
        destination_folder: Any,
        output_type: str,
        document_generation_data: list[dict[str, Any]],
        file_version: Any | None = None,
    ) -> dict[str, Any]:
        """
        Generate document using Box Doc Gen template

        Args:
            file (string): file
            input_source (string): Source of input. The value has to be `api` for all the API-based document generation requests. Example: 'api'.
            destination_folder (string): destination_folder
            output_type (string): Type of the output file. Example: 'docx'.
            document_generation_data (array): document_generation_data
            file_version (string): file_version

        Returns:
            dict[str, Any]: The created Batch ID.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Box Doc Gen
        """
        request_body_data = None
        request_body_data = {
            "file": file,
            "file_version": file_version,
            "input_source": input_source,
            "destination_folder": destination_folder,
            "output_type": output_type,
            "document_generation_data": document_generation_data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/docgen_batches"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_lists_v(self) -> dict[str, Any]:
        """
        Get all shield lists in enterprise

        Returns:
            dict[str, Any]: Returns the list of shield list objects.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield lists
        """
        url = f"{self.base_url}/shield_lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_shield_lists_v(
        self, name: str, content: Any, description: str | None = None
    ) -> dict[str, Any]:
        """
        Create shield list

        Args:
            name (string): The name of the shield list. Example: 'My Shield List'.
            content (string): content
            description (string): Description of Shield List: Optional. Example: 'A list of things that are shielded'.

        Returns:
            dict[str, Any]: Returns the shield list object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield lists
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "content": content,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_lists"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_shield_lists_id_v(self, shield_list_id: str) -> dict[str, Any]:
        """
        Get single shield list by shield list id

        Args:
            shield_list_id (string): shield_list_id

        Returns:
            dict[str, Any]: Returns the shield list object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield lists
        """
        if shield_list_id is None:
            raise ValueError("Missing required parameter 'shield_list_id'.")
        url = f"{self.base_url}/shield_lists/{shield_list_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_shield_lists_id_v(self, shield_list_id: str) -> Any:
        """
        Delete single shield list by shield list id

        Args:
            shield_list_id (string): shield_list_id

        Returns:
            Any: Shield List correctly removed. No content in response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield lists
        """
        if shield_list_id is None:
            raise ValueError("Missing required parameter 'shield_list_id'.")
        url = f"{self.base_url}/shield_lists/{shield_list_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_shield_lists_id_v(
        self,
        shield_list_id: str,
        name: str | None = None,
        description: str | None = None,
        content: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update shield list

        Args:
            shield_list_id (string): shield_list_id
            name (string): The name of the shield list. Example: 'My Shield List'.
            description (string): Description of Shield List: Optional. Example: 'A list of things that are shielded'.
            content (string): content

        Returns:
            dict[str, Any]: Returns the shield list object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shield lists
        """
        if shield_list_id is None:
            raise ValueError("Missing required parameter 'shield_list_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "content": content,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/shield_lists/{shield_list_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_tools(self):
        return [
            self.get_authorize,
            self.post_oauth_token,
            self.post_oauth_token_refresh,
            self.post_oauth_revoke,
            self.get_files_id,
            self.post_files_id,
            self.put_files_id,
            self.delete_files_id,
            self.list_file_associations,
            self.get_files_id_content,
            self.post_files_id_content,
            self.options_files_content,
            self.post_files_content,
            self.post_files_upload_sessions,
            self.post_files_id_upload_sessions,
            self.get_files_upload_sessions_id,
            self.put_files_upload_sessions_id,
            self.delete_upload_session_by_id,
            self.get_upload_session_parts,
            self.commit_upload_session,
            self.post_files_id_copy,
            self.get_files_id_thumbnail_id,
            self.get_files_id_collaborations,
            self.get_files_id_comments,
            self.get_files_id_tasks,
            self.get_files_id_trash,
            self.delete_files_id_trash,
            self.get_files_id_versions,
            self.get_files_id_versions_id,
            self.delete_files_id_versions_id,
            self.put_files_id_versions_id,
            self.post_files_id_versions_current,
            self.get_files_id_metadata,
            self.get_file_security_classification_by_id,
            self.update_file_security_classification,
            self.put_update_file_security_classification,
            self.delete_file_metadata,
            self.get_files_id_metadata_id_id,
            self.post_files_id_metadata_id_id,
            self.put_files_id_metadata_id_id,
            self.delete_files_id_metadata_id_id,
            self.get_global_metadata,
            self.post_file_metadata_global_box_skills_cards,
            self.update_file_metadata,
            self.delete_file_global_box_skills_cards,
            self.get_files_id_watermark,
            self.put_files_id_watermark,
            self.delete_files_id_watermark,
            self.get_file_requests_id,
            self.put_file_requests_id,
            self.delete_file_requests_id,
            self.post_file_requests_id_copy,
            self.get_folders_id,
            self.post_folders_id,
            self.put_folders_id,
            self.delete_folders_id,
            self.get_folder_app_item_associations,
            self.get_folders_id_items,
            self.post_folders,
            self.post_folders_id_copy,
            self.get_folders_id_collaborations,
            self.get_folders_id_trash,
            self.delete_folders_id_trash,
            self.get_folders_id_metadata,
            self.get_folder_security_classification,
            self.post_folder_metadata_security_classification,
            self.update_folder_security_classification,
            self.delete_security_classification_by_folder_id,
            self.get_folders_id_metadata_id_id,
            self.post_folders_id_metadata_id_id,
            self.put_folders_id_metadata_id_id,
            self.delete_folder_metadata,
            self.get_folders_trash_items,
            self.get_folders_id_watermark,
            self.put_folders_id_watermark,
            self.delete_folders_id_watermark,
            self.get_folder_locks,
            self.post_folder_locks,
            self.delete_folder_locks_id,
            self.get_metadata_templates,
            self.get_security_classification_schema,
            self.add_security_classification_schema,
            self.update_security_classification_schema,
            self.get_schema_template,
            self.update_schema_template,
            self.delete_metadata_template_schema,
            self.get_metadata_templates_id,
            self.get_metadata_templates_global,
            self.get_metadata_templates_enterprise,
            self.post_metadata_templates_schema,
            self.create_metadata_template_classification,
            self.get_metadata_cascade_policies,
            self.post_metadata_cascade_policies,
            self.get_metadata_cascade_policy_by_id,
            self.delete_metadata_cascade_policy,
            self.apply_metadata_cascade_policy_by_id,
            self.execute_metadata_query,
            self.get_comments_id,
            self.put_comments_id,
            self.delete_comments_id,
            self.post_comments,
            self.get_collaborations_id,
            self.put_collaborations_id,
            self.delete_collaborations_id,
            self.get_collaborations,
            self.post_collaborations,
            self.get_search,
            self.post_tasks,
            self.get_tasks_id,
            self.put_tasks_id,
            self.delete_tasks_id,
            self.get_tasks_id_assignments,
            self.post_task_assignments,
            self.get_task_assignments_id,
            self.put_task_assignments_id,
            self.delete_task_assignments_id,
            self.get_shared_items,
            self.get_files_id_get_shared_link,
            self.put_files_id_add_shared_link,
            self.update_file_shared_link,
            self.remove_shared_link_by_id,
            self.get_shared_items_folders,
            self.get_folders_id_get_shared_link,
            self.put_folders_id_add_shared_link,
            self.update_shared_linkfolder,
            self.remove_shared_link_by_folder_id,
            self.post_web_links,
            self.get_web_links_id,
            self.post_web_links_id,
            self.put_web_links_id,
            self.delete_web_links_id,
            self.get_web_links_id_trash,
            self.delete_web_links_id_trash,
            self.get_shared_items_web_links,
            self.get_shared_link_by_id,
            self.update_web_link_shared_link,
            self.update_shared_link,
            self.remove_shared_link_by_web_link_id,
            self.get_shared_items_app_items,
            self.get_users,
            self.post_users,
            self.get_users_me,
            self.post_users_terminate_sessions,
            self.get_users_id,
            self.put_users_id,
            self.delete_users_id,
            self.get_users_id_avatar,
            self.post_users_id_avatar,
            self.delete_users_id_avatar,
            self.put_users_id_folders,
            self.get_users_id_email_aliases,
            self.post_users_id_email_aliases,
            self.delete_email_alias_by_id,
            self.get_users_id_memberships,
            self.post_invites,
            self.get_invites_id,
            self.get_groups,
            self.post_groups,
            self.post_groups_terminate_sessions,
            self.get_groups_id,
            self.put_groups_id,
            self.delete_groups_id,
            self.get_groups_id_memberships,
            self.get_groups_id_collaborations,
            self.post_group_memberships,
            self.get_group_memberships_id,
            self.put_group_memberships_id,
            self.delete_group_memberships_id,
            self.get_webhooks,
            self.post_webhooks,
            self.get_webhooks_id,
            self.put_webhooks_id,
            self.delete_webhooks_id,
            self.put_skill_invocations_id,
            self.options_events,
            self.get_events,
            self.get_collections,
            self.get_collections_id_items,
            self.get_collections_id,
            self.get_recent_items,
            self.get_retention_policies,
            self.post_retention_policies,
            self.get_retention_policies_id,
            self.put_retention_policies_id,
            self.delete_retention_policies_id,
            self.get_retention_policy_assignments,
            self.create_retention_policy_assignment,
            self.get_retention_policy_assignment_by_id,
            self.delete_retention_policy_assignment_by_id,
            self.get_files_under_retention,
            self.get_retention_policy_assignment_file_versions,
            self.get_legal_hold_policies,
            self.post_legal_hold_policies,
            self.get_legal_hold_policies_id,
            self.put_legal_hold_policies_id,
            self.delete_legal_hold_policies_id,
            self.get_legal_hold_policy_assignments,
            self.assign_legal_hold_policy,
            self.get_legal_hold_policy_assignment,
            self.delete_legal_hold_assignment,
            self.get_files_on_hold_by_legl_hld_polcy_asgnmt_id,
            self.get_file_version_retentions,
            self.get_legal_hold_file_versions_on_hold,
            self.get_file_version_retentions_id,
            self.get_legal_hold,
            self.get_file_version_legal_holds,
            self.get_shield_information_barrier_by_id,
            self.change_shield_status,
            self.get_shield_information_barriers,
            self.create_shield_barriers,
            self.get_shield_information_barrier_reports,
            self.generate_shield_report,
            self.get_shield_report_by_id,
            self.get_shield_segment_by_id,
            self.delete_shield_inft_barrier_sgmt_by_id,
            self.update_shield_barrier_segment,
            self.get_shield_segments,
            self.create_shield_barrier_segments,
            self.get_shield_infmt_barrier_sgmnt_member_by_id,
            self.delete_shield_member,
            self.get_shield_infmt_barrier_sgmnt_members,
            self.add_shield_members,
            self.get_shield_barrier_segment_restriction_by_id,
            self.delete_shield_restriction,
            self.get_shield_infmt_barrier_sgmnt_restrictions,
            self.create_shield_restrictions,
            self.get_device_pinners_id,
            self.delete_device_pinners_id,
            self.list_device_pins,
            self.get_terms_of_services,
            self.post_terms_of_services,
            self.get_terms_of_services_id,
            self.put_terms_of_services_id,
            self.get_tos_user_statuses,
            self.create_terms_of_service_statuses,
            self.update_terms_of_service_user_status_by_id,
            self.list_collaboration_whitelist_entries,
            self.create_collaboration_whitelist_entry,
            self.get_whitelist_entry_by_id,
            self.delete_collaboration_whitelist_entry_by_id,
            self.list_whitelist_targets,
            self.create_collaboration_whitelist_exempt_target,
            self.get_exempt_target_by_id,
            self.delete_collab_whitelist_exempt_target_by_id,
            self.get_storage_policies,
            self.get_storage_policies_id,
            self.get_storage_policy_assignments,
            self.create_storage_policy_assignment,
            self.get_storage_policy_assignment,
            self.update_storage_policy_assignment,
            self.delete_storage_policy_assignment,
            self.post_zip_downloads,
            self.get_zip_downloads_id_content,
            self.get_zip_downloads_id_status,
            self.post_sign_requests_id_cancel,
            self.post_sign_requests_id_resend,
            self.get_sign_requests_id,
            self.get_sign_requests,
            self.post_sign_requests,
            self.get_workflows,
            self.post_workflows_id_start,
            self.get_sign_templates,
            self.get_sign_templates_id,
            self.get_integration_mappings_slack,
            self.create_slack_mapping,
            self.update_slack_integration_mapping_by_id,
            self.delete_slack_mapping_by_id,
            self.get_integration_mappings_teams,
            self.create_integration_mapping_team,
            self.update_integration_mapping_team,
            self.delete_integration_mapping_by_id,
            self.post_ai_ask,
            self.post_ai_text_gen,
            self.get_ai_agent_default,
            self.post_ai_extract,
            self.post_ai_extract_structured,
            self.get_ai_agents,
            self.post_ai_agents,
            self.put_ai_agents_id,
            self.get_ai_agents_id,
            self.delete_ai_agents_id,
            self.post_docgen_templates_v,
            self.get_docgen_templates_v,
            self.delete_template_by_id,
            self.get_docgen_template_by_id,
            self.get_docgen_template_tags,
            self.get_docgen_jobs_id_v,
            self.get_docgen_jobs_v,
            self.get_template_job,
            self.get_batch_job_details,
            self.post_docgen_batches_v,
            self.get_shield_lists_v,
            self.post_shield_lists_v,
            self.get_shield_lists_id_v,
            self.delete_shield_lists_id_v,
            self.put_shield_lists_id_v,
        ]
