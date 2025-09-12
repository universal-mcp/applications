from typing import Any

import httpx
from loguru import logger

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class GoogleDriveApp(APIApplication):
    """
    Application for interacting with Google Drive API.
    Provides tools to manage files, folders, and access Drive information.
    """

    def __init__(self, integration: Integration | None = None) -> None:
        super().__init__(name="google_drive", integration=integration)
        self.base_url = "https://www.googleapis.com/drive/v3"

    def move_files(
        self, file_id: str, add_parents: str, remove_parents: str
    ) -> dict[str, Any]:
        """
        Moves a file from one folder to another by adding a new parent and removing the old parent.

        Args:
            file_id: The ID of the file to move
            add_parents: The ID of the destination folder (new parent)
            remove_parents: The ID of the source folder (old parent to remove)

        Returns:
            A dictionary containing the updated file information

        Raises:
            HTTPError: If the API request fails or returns an error status code
            ConnectionError: If there are network connectivity issues
            AuthenticationError: If the authentication credentials are invalid or expired

        Tags:
            move, file, folder, parent, patch, api, important
        """
        url = f"{self.base_url}/files/{file_id}"
        data = {}
        params = {"addParents": add_parents, "removeParents": remove_parents}
        response = self._patch(url, params=params, data=data)
        response.raise_for_status()
        return response.json()

    def get_drive_info(self) -> dict[str, Any]:
        """
        Retrieves detailed information about the user's Google Drive storage and account.

        Returns:
            A dictionary containing Drive information including storage quota (usage, limit) and user details (name, email, etc.).

        Raises:
            HTTPError: If the API request fails or returns an error status code
            ConnectionError: If there are network connectivity issues
            AuthenticationError: If the authentication credentials are invalid or expired

        Tags:
            get, info, storage, drive, quota, user, api, important
        """
        url = f"{self.base_url}/about"
        params = {"fields": "storageQuota,user"}
        response = self._get(url, params=params)
        return response.json()

    def list_files(
        self, page_size: int = 10, query: str | None = None, order_by: str | None = None
    ) -> dict[str, Any]:
        """
        Lists and retrieves files from Google Drive with optional filtering, pagination, and sorting.

        Args:
            page_size: Maximum number of files to return per page (default: 10)
            query: Optional search query string using Google Drive query syntax (e.g., "mimeType='image/jpeg'")
            order_by: Optional field name to sort results by, with optional direction (e.g., "modifiedTime desc")

        Returns:
            Dictionary containing a list of files and metadata, including 'files' array and optional 'nextPageToken' for pagination

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code
            RequestException: Raised when network connectivity issues occur during the API request

        Tags:
            list, files, search, google-drive, pagination, important
        """
        url = f"{self.base_url}/files"
        params = {
            "pageSize": page_size,
        }
        if query:
            params["q"] = query
        if order_by:
            params["orderBy"] = order_by
        response = self._get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_file(self, file_id: str) -> dict[str, Any]:
        """
        Retrieves detailed metadata for a specific file using its ID.

        Args:
            file_id: String identifier of the file whose metadata should be retrieved

        Returns:
            Dictionary containing the file's metadata including properties such as name, size, type, and other attributes

        Raises:
            HTTPError: When the API request fails due to invalid file_id or network issues
            JSONDecodeError: When the API response cannot be parsed as JSON

        Tags:
            retrieve, file, metadata, get, api, important
        """
        url = f"{self.base_url}/files/{file_id}"
        response = self._get(url)
        return response.json()

    def delete_file(self, file_id: str) -> dict[str, Any]:
        """
        Deletes a specified file from Google Drive and returns a status message.

        Args:
            file_id: The unique identifier string of the file to be deleted from Google Drive

        Returns:
            A dictionary containing either a success message {'message': 'File deleted successfully'} or an error message {'error': 'error description'}

        Raises:
            Exception: When the DELETE request fails due to network issues, invalid file_id, insufficient permissions, or other API errors

        Tags:
            delete, file-management, google-drive, api, important
        """
        url = f"{self.base_url}/files/{file_id}"
        try:
            self._delete(url)
            return {"message": "File deleted successfully"}
        except Exception as e:
            return {"error": str(e)}

    def create_file_from_text(
        self,
        file_name: str,
        text_content: str,
        parent_id: str = None,
        mime_type: str = "text/plain",
    ) -> dict[str, Any]:
        """
        Creates a new file in Google Drive with specified text content and returns the file's metadata.

        Args:
            file_name: Name of the file to create on Google Drive
            text_content: Plain text content to be written to the file
            parent_id: Optional ID of the parent folder where the file will be created
            mime_type: MIME type of the file (defaults to 'text/plain')

        Returns:
            Dictionary containing metadata of the created file including ID, name, and other Google Drive file properties

        Raises:
            HTTPStatusError: Raised when the API request fails during file creation or content upload
            UnicodeEncodeError: Raised when the text_content cannot be encoded in UTF-8

        Tags:
            create, file, upload, drive, text, important, storage, document
        """
        metadata = {"name": file_name, "mimeType": mime_type}
        if parent_id:
            metadata["parents"] = [parent_id]
        create_url = f"{self.base_url}/files"
        create_response = self._post(create_url, data=metadata)
        file_data = create_response.json()
        file_id = file_data.get("id")
        upload_url = f"https://www.googleapis.com/upload/drive/v3/files/{file_id}?uploadType=media"
        upload_headers = self._get_headers()
        upload_headers["Content-Type"] = f"{mime_type}; charset=utf-8"
        upload_response = httpx.patch(
            upload_url, headers=upload_headers, content=text_content.encode("utf-8")
        )
        upload_response.raise_for_status()
        response_data = upload_response.json()
        return response_data

    def find_folder_id_by_name(self, folder_name: str) -> str | None:
        """
        Searches for and retrieves a Google Drive folder's ID using its name.

        Args:
            folder_name: The name of the folder to search for in Google Drive

        Returns:
            str | None: The folder's ID if a matching folder is found, None if no folder is found or if an error occurs

        Raises:
            Exception: Caught internally and logged when API requests fail or response parsing errors occur

        Tags:
            search, find, google-drive, folder, query, api, utility
        """
        query = f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and trashed=false"
        try:
            response = self._get(
                f"{self.base_url}/files",
                params={"q": query, "fields": "files(id,name)"},
            )
            files = response.json().get("files", [])
            return files[0]["id"] if files else None
        except Exception as e:
            logger.error(f"Error finding folder ID by name: {e}")
            return None

    def create_folder(self, folder_name: str, parent_id: str = None) -> dict[str, Any]:
        """
        Creates a new folder in Google Drive with optional parent folder specification

        Args:
            folder_name: Name of the folder to create
            parent_id: ID or name of the parent folder. Can be either a folder ID string or a folder name that will be automatically looked up

        Returns:
            Dictionary containing the created folder's metadata including its ID, name, and other Drive-specific information

        Raises:
            ValueError: Raised when a parent folder name is provided but cannot be found in Google Drive

        Tags:
            create, folder, drive, storage, important, management
        """
        import re

        metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
        }
        if parent_id:
            if not re.match(r"^[a-zA-Z0-9_-]{28,33}$", parent_id):
                found_id = self.find_folder_id_by_name(parent_id)
                if found_id:
                    metadata["parents"] = [found_id]
                else:
                    raise ValueError(
                        f"Could not find parent folder with name: {parent_id}"
                    )
            else:
                metadata["parents"] = [parent_id]
        url = f"{self.base_url}/files"
        params = {"supportsAllDrives": "true"}
        response = self._post(url, data=metadata, params=params)
        return response.json()

    def upload_a_file(
        self,
        file_name: str,
        file_path: str,
        parent_id: str = None,
        mime_type: str = None,
    ) -> dict[str, Any]:
        """
        Uploads a file to Google Drive by creating a file metadata entry and uploading the binary content.

        Args:
            file_name: Name to give the file on Google Drive
            file_path: Path to the local file to upload
            parent_id: Optional ID of the parent folder to create the file in
            mime_type: MIME type of the file (e.g., 'image/jpeg', 'image/png', 'application/pdf')

        Returns:
            Dictionary containing the uploaded file's metadata from Google Drive

        Raises:
            FileNotFoundError: When the specified file_path does not exist or is not accessible
            HTTPError: When the API request fails or returns an error status code
            IOError: When there are issues reading the file content

        Tags:
            upload, file-handling, google-drive, api, important, binary, storage
        """
        metadata = {"name": file_name, "mimeType": mime_type}
        if parent_id:
            metadata["parents"] = [parent_id]
        create_url = f"{self.base_url}/files"
        create_response = self._post(create_url, data=metadata)
        file_data = create_response.json()
        file_id = file_data.get("id")
        with open(file_path, "rb") as file_content:
            binary_content = file_content.read()

            upload_url = f"https://www.googleapis.com/upload/drive/v3/files/{file_id}?uploadType=media"
            upload_headers = self._get_headers()
            upload_headers["Content-Type"] = mime_type

            upload_response = httpx.patch(
                upload_url, headers=upload_headers, content=binary_content
            )
            upload_response.raise_for_status()
        response_data = upload_response.json()
        return response_data

    def list_user_sinstalled_apps(
        self,
        appFilterExtensions: str | None = None,
        appFilterMimeTypes: str | None = None,
        languageCode: str | None = None,
        access_token: str | None = None,
        alt: str | None = None,
        callback: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        upload_protocol: str | None = None,
        uploadType: str | None = None,
        xgafv: str | None = None,
    ) -> dict[str, Any]:
        """
        List user's installed apps

        Args:
            appFilterExtensions (string): A query parameter to filter applications based on extensions, allowing string values to be specified in the URL. Example: '<string>'.
            appFilterMimeTypes (string): Filters the results to include only apps that can open any of the provided comma-separated list of MIME types[4][1]. Example: '<string>'.
            languageCode (string): Specifies the language code for the query results returned from the apps endpoint. Example: '<string>'.
            access_token (string): OAuth access token. Example: '{{accessToken}}'.
            alt (string): Data format for response. Example: '<string>'.
            callback (string): JSONP Example: '<string>'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Example: '<string>'.
            upload_protocol (string): Upload protocol for media (e.g. "raw", "multipart"). Example: '<string>'.
            uploadType (string): Legacy upload protocol for media (e.g. "media", "multipart"). Example: '<string>'.
            xgafv (string): V1 error format. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        url = f"{self.base_url}/apps"
        query_params = {
            k: v
            for k, v in [
                ("appFilterExtensions", appFilterExtensions),
                ("appFilterMimeTypes", appFilterMimeTypes),
                ("languageCode", languageCode),
                ("access_token", access_token),
                ("alt", alt),
                ("callback", callback),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("upload_protocol", upload_protocol),
                ("uploadType", uploadType),
                ("$.xgafv", xgafv),
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

    def get_aspecific_app(
        self,
        appId: str,
        access_token: str | None = None,
        alt: str | None = None,
        callback: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        upload_protocol: str | None = None,
        uploadType: str | None = None,
        xgafv: str | None = None,
    ) -> dict[str, Any]:
        """
        Get a specific app

        Args:
            appId (string): appId
            access_token (string): OAuth access token. Example: '{{accessToken}}'.
            alt (string): Data format for response. Example: '<string>'.
            callback (string): JSONP Example: '<string>'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Example: '<string>'.
            upload_protocol (string): Upload protocol for media (e.g. "raw", "multipart"). Example: '<string>'.
            uploadType (string): Legacy upload protocol for media (e.g. "media", "multipart"). Example: '<string>'.
            xgafv (string): V1 error format. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.base_url}/apps/{appId}"
        query_params = {
            k: v
            for k, v in [
                ("access_token", access_token),
                ("alt", alt),
                ("callback", callback),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("upload_protocol", upload_protocol),
                ("uploadType", uploadType),
                ("$.xgafv", xgafv),
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

    def information_about_user_and_drive(
        self,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Information about user and drive

        Args:
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Information
        """
        url = f"{self.base_url}/about"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def list_changes_made_to_afile_or_drive(
        self,
        pageToken: str | None = None,
        driveId: str | None = None,
        includeCorpusRemovals: str | None = None,
        includeItemsFromAllDrives: str | None = None,
        includeLabels: str | None = None,
        includePermissionsForView: str | None = None,
        includeRemoved: str | None = None,
        includeTeamDriveItems: str | None = None,
        pageSize: str | None = None,
        restrictToMyDrive: str | None = None,
        spaces: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        teamDriveId: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        List changes made to a file or drive

        Args:
            pageToken (string): (Required) The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method. Example: '{{pageToken}}'.
            driveId (string): The shared drive from which changes are returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier. Example: '{{driveId}}'.
            includeCorpusRemovals (string): Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file. Example: '<boolean>'.
            includeItemsFromAllDrives (string): Whether both My Drive and shared drive items should be included in results. Example: '<boolean>'.
            includeLabels (string): A comma-separated list of IDs of labels to include in the labelInfo part of the response. Example: '<string>'.
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            includeRemoved (string): Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access. Example: '<boolean>'.
            includeTeamDriveItems (string): Deprecated use includeItemsFromAllDrives instead. Example: '<boolean>'.
            pageSize (string): The maximum number of changes to return per page. Example: '<integer>'.
            restrictToMyDrive (string): Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive. Example: '<boolean>'.
            spaces (string): A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'. Example: '<string>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            teamDriveId (string): Deprecated use driveId instead. Example: '<string>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Changes
        """
        url = f"{self.base_url}/changes"
        query_params = {
            k: v
            for k, v in [
                ("pageToken", pageToken),
                ("driveId", driveId),
                ("includeCorpusRemovals", includeCorpusRemovals),
                ("includeItemsFromAllDrives", includeItemsFromAllDrives),
                ("includeLabels", includeLabels),
                ("includePermissionsForView", includePermissionsForView),
                ("includeRemoved", includeRemoved),
                ("includeTeamDriveItems", includeTeamDriveItems),
                ("pageSize", pageSize),
                ("restrictToMyDrive", restrictToMyDrive),
                ("spaces", spaces),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("teamDriveId", teamDriveId),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def get_start_page_token(
        self,
        driveId: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        teamDriveId: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Gets the starting pageToken for listing future changes

        Args:
            driveId (string): The ID of the shared drive for which the starting pageToken for listing future changes from that shared drive is returned. Example: '{{driveId}}'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            teamDriveId (string): Deprecated use driveId instead. Example: '<string>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Changes
        """
        url = f"{self.base_url}/changes/startPageToken"
        query_params = {
            k: v
            for k, v in [
                ("driveId", driveId),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("teamDriveId", teamDriveId),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def subscribe_to_changes_for_auser(
        self,
        pageToken: str | None = None,
        driveId: str | None = None,
        includeCorpusRemovals: str | None = None,
        includeItemsFromAllDrives: str | None = None,
        includeLabels: str | None = None,
        includePermissionsForView: str | None = None,
        includeRemoved: str | None = None,
        includeTeamDriveItems: str | None = None,
        pageSize: str | None = None,
        restrictToMyDrive: str | None = None,
        spaces: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        teamDriveId: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        address: str | None = None,
        expiration: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        params: dict[str, Any] | None = None,
        payload: str | None = None,
        resourceId: str | None = None,
        resourceUri: str | None = None,
        token: str | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        """
        Subscribe to changes for a user

        Args:
            pageToken (string): (Required) The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method. Example: '{{pageToken}}'.
            driveId (string): The shared drive from which changes are returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier. Example: '{{driveId}}'.
            includeCorpusRemovals (string): Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file. Example: '<boolean>'.
            includeItemsFromAllDrives (string): Whether both My Drive and shared drive items should be included in results. Example: '<boolean>'.
            includeLabels (string): A comma-separated list of IDs of labels to include in the labelInfo part of the response. Example: '<string>'.
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            includeRemoved (string): Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access. Example: '<boolean>'.
            includeTeamDriveItems (string): Deprecated use includeItemsFromAllDrives instead. Example: '<boolean>'.
            pageSize (string): The maximum number of changes to return per page. Example: '<integer>'.
            restrictToMyDrive (string): Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive. Example: '<boolean>'.
            spaces (string): A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'. Example: '<string>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            teamDriveId (string): Deprecated use driveId instead. Example: '<string>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            address (string): address Example: '<string>'.
            expiration (string): expiration Example: '<int64>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'api#channel'.
            params (object): params Example: {'adipisicing1': '<string>', 'eu2': '<string>', 'qui_9': '<string>'}.
            payload (string): payload Example: '<boolean>'.
            resourceId (string): resourceId Example: '<string>'.
            resourceUri (string): resourceUri Example: '<string>'.
            token (string): token Example: '<string>'.
            type (string): type Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Changes
        """
        request_body_data = None
        request_body_data = {
            "address": address,
            "expiration": expiration,
            "id": id,
            "kind": kind,
            "params": params,
            "payload": payload,
            "resourceId": resourceId,
            "resourceUri": resourceUri,
            "token": token,
            "type": type,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/changes/watch"
        query_params = {
            k: v
            for k, v in [
                ("pageToken", pageToken),
                ("driveId", driveId),
                ("includeCorpusRemovals", includeCorpusRemovals),
                ("includeItemsFromAllDrives", includeItemsFromAllDrives),
                ("includeLabels", includeLabels),
                ("includePermissionsForView", includePermissionsForView),
                ("includeRemoved", includeRemoved),
                ("includeTeamDriveItems", includeTeamDriveItems),
                ("pageSize", pageSize),
                ("restrictToMyDrive", restrictToMyDrive),
                ("spaces", spaces),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("teamDriveId", teamDriveId),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def post_stop_channel(
        self,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        address: str | None = None,
        expiration: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        params: dict[str, Any] | None = None,
        payload: str | None = None,
        resourceId: str | None = None,
        resourceUri: str | None = None,
        token: str | None = None,
        type: str | None = None,
    ) -> Any:
        """
        Stop watching resources through a channel

        Args:
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            address (string): address Example: '<string>'.
            expiration (string): expiration Example: '<int64>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'api#channel'.
            params (object): params Example: {'adipisicing1': '<string>', 'eu2': '<string>', 'qui_9': '<string>'}.
            payload (string): payload Example: '<boolean>'.
            resourceId (string): resourceId Example: '<string>'.
            resourceUri (string): resourceUri Example: '<string>'.
            token (string): token Example: '<string>'.
            type (string): type Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Channels
        """
        request_body_data = None
        request_body_data = {
            "address": address,
            "expiration": expiration,
            "id": id,
            "kind": kind,
            "params": params,
            "payload": payload,
            "resourceId": resourceId,
            "resourceUri": resourceUri,
            "token": token,
            "type": type,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/channels/stop"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def lists_afile_scomments(
        self,
        fileId: str,
        includeDeleted: str | None = None,
        pageSize: str | None = None,
        pageToken: str | None = None,
        startModifiedTime: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Lists a file's comments

        Args:
            fileId (string): fileId
            includeDeleted (string): Whether to include deleted comments. Deleted comments will not include their original content. Example: '<boolean>'.
            pageSize (string): The maximum number of comments to return per page. Example: '<integer>'.
            pageToken (string): The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response. Example: '{{pageToken}}'.
            startModifiedTime (string): The minimum value of 'modifiedTime' for the result comments (RFC 3339 date-time). Example: '<string>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        url = f"{self.base_url}/files/{fileId}/comments"
        query_params = {
            k: v
            for k, v in [
                ("includeDeleted", includeDeleted),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("startModifiedTime", startModifiedTime),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def create_acomment_on_afile(
        self,
        fileId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        anchor: str | None = None,
        author: dict[str, Any] | None = None,
        content: str | None = None,
        createdTime: str | None = None,
        deleted: str | None = None,
        htmlContent: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        modifiedTime: str | None = None,
        quotedFileContent: dict[str, Any] | None = None,
        replies: list[dict[str, Any]] | None = None,
        resolved: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a comment on a file

        Args:
            fileId (string): fileId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            anchor (string): anchor Example: '<string>'.
            author (object): author Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            content (string): content Example: '<string>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            deleted (string): deleted Example: '<boolean>'.
            htmlContent (string): htmlContent Example: '<string>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'drive#comment'.
            modifiedTime (string): modifiedTime Example: '<dateTime>'.
            quotedFileContent (object): quotedFileContent Example: {'mimeType': '<string>', 'value': '<string>'}.
            replies (array): replies Example: "[{'action': '<string>', 'author': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'content': '<string>', 'createdTime': '<dateTime>', 'deleted': '<boolean>', 'htmlContent': '<string>', 'id': '<string>', 'kind': 'drive#reply', 'modifiedTime': '<dateTime>'}, {'action': '<string>', 'author': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'content': '<string>', 'createdTime': '<dateTime>', 'deleted': '<boolean>', 'htmlContent': '<string>', 'id': '<string>', 'kind': 'drive#reply', 'modifiedTime': '<dateTime>'}]".
            resolved (string): resolved Example: '<boolean>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        request_body_data = None
        request_body_data = {
            "anchor": anchor,
            "author": author,
            "content": content,
            "createdTime": createdTime,
            "deleted": deleted,
            "htmlContent": htmlContent,
            "id": id,
            "kind": kind,
            "modifiedTime": modifiedTime,
            "quotedFileContent": quotedFileContent,
            "replies": replies,
            "resolved": resolved,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/comments"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def get_comment_by_id(
        self,
        fileId: str,
        commentId: str,
        includeDeleted: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Get comment by ID

        Args:
            fileId (string): fileId
            commentId (string): commentId
            includeDeleted (string): Whether to return deleted comments. Deleted comments will not include their original content. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'.")
        url = f"{self.base_url}/files/{fileId}/comments/{commentId}"
        query_params = {
            k: v
            for k, v in [
                ("includeDeleted", includeDeleted),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def delete_acomment(
        self,
        fileId: str,
        commentId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> Any:
        """
        Delete a comment

        Args:
            fileId (string): fileId
            commentId (string): commentId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'.")
        url = f"{self.base_url}/files/{fileId}/comments/{commentId}"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def update_comment(
        self,
        fileId: str,
        commentId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        anchor: str | None = None,
        author: dict[str, Any] | None = None,
        content: str | None = None,
        createdTime: str | None = None,
        deleted: str | None = None,
        htmlContent: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        modifiedTime: str | None = None,
        quotedFileContent: dict[str, Any] | None = None,
        replies: list[dict[str, Any]] | None = None,
        resolved: str | None = None,
    ) -> dict[str, Any]:
        """
        Update comment

        Args:
            fileId (string): fileId
            commentId (string): commentId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            anchor (string): anchor Example: '<string>'.
            author (object): author Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            content (string): content Example: '<string>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            deleted (string): deleted Example: '<boolean>'.
            htmlContent (string): htmlContent Example: '<string>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'drive#comment'.
            modifiedTime (string): modifiedTime Example: '<dateTime>'.
            quotedFileContent (object): quotedFileContent Example: {'mimeType': '<string>', 'value': '<string>'}.
            replies (array): replies Example: "[{'action': '<string>', 'author': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'content': '<string>', 'createdTime': '<dateTime>', 'deleted': '<boolean>', 'htmlContent': '<string>', 'id': '<string>', 'kind': 'drive#reply', 'modifiedTime': '<dateTime>'}, {'action': '<string>', 'author': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'content': '<string>', 'createdTime': '<dateTime>', 'deleted': '<boolean>', 'htmlContent': '<string>', 'id': '<string>', 'kind': 'drive#reply', 'modifiedTime': '<dateTime>'}]".
            resolved (string): resolved Example: '<boolean>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Comments
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'.")
        request_body_data = None
        request_body_data = {
            "anchor": anchor,
            "author": author,
            "content": content,
            "createdTime": createdTime,
            "deleted": deleted,
            "htmlContent": htmlContent,
            "id": id,
            "kind": kind,
            "modifiedTime": modifiedTime,
            "quotedFileContent": quotedFileContent,
            "replies": replies,
            "resolved": resolved,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/comments/{commentId}"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
        }
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_user_sshared_drive(
        self,
        pageSize: str | None = None,
        pageToken: str | None = None,
        q: str | None = None,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        List user's shared drive

        Args:
            pageSize (string): Maximum number of shared drives to return per page. Example: '<integer>'.
            pageToken (string): Page token for shared drives. Example: '{{pageToken}}'.
            q (string): Query string for searching shared drives. Example: 'query'.
            useDomainAdminAccess (string): Issue the request as a domain administrator; if set to true, then all shared drives of the domain in which the requester is an administrator are returned. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared Drive
        """
        url = f"{self.base_url}/drives"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("q", q),
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def create_ashared_drive(
        self,
        requestId: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        backgroundImageFile: dict[str, Any] | None = None,
        backgroundImageLink: str | None = None,
        capabilities: dict[str, Any] | None = None,
        colorRgb: str | None = None,
        createdTime: str | None = None,
        hidden: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        name: str | None = None,
        orgUnitId: str | None = None,
        restrictions: dict[str, Any] | None = None,
        themeId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a shared drive

        Args:
            requestId (string): (Required) An ID, such as a random UUID, which uniquely identifies this user's request for idempotent creation of a shared drive. A repeated request by the same user and with the same request ID will avoid creating duplicates by attempting to create the same shared drive. If the shared drive already exists a 409 error will be returned. Example: 'requestId'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            backgroundImageFile (object): backgroundImageFile Example: {'id': '<string>', 'width': '<float>', 'xCoordinate': '<float>', 'yCoordinate': '<float>'}.
            backgroundImageLink (string): backgroundImageLink Example: '<string>'.
            capabilities (object): capabilities Example: {'canAddChildren': '<boolean>', 'canChangeCopyRequiresWriterPermissionRestriction': '<boolean>', 'canChangeDomainUsersOnlyRestriction': '<boolean>', 'canChangeDriveBackground': '<boolean>', 'canChangeDriveMembersOnlyRestriction': '<boolean>', 'canChangeSharingFoldersRequiresOrganizerPermissionRestriction': '<boolean>', 'canComment': '<boolean>', 'canCopy': '<boolean>', 'canDeleteChildren': '<boolean>', 'canDeleteDrive': '<boolean>', 'canDownload': '<boolean>', 'canEdit': '<boolean>', 'canListChildren': '<boolean>', 'canManageMembers': '<boolean>', 'canReadRevisions': '<boolean>', 'canRename': '<boolean>', 'canRenameDrive': '<boolean>', 'canResetDriveRestrictions': '<boolean>', 'canShare': '<boolean>', 'canTrashChildren': '<boolean>'}.
            colorRgb (string): colorRgb Example: '<string>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            hidden (string): hidden Example: '<boolean>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'drive#drive'.
            name (string): name Example: '<string>'.
            orgUnitId (string): orgUnitId Example: '<string>'.
            restrictions (object): restrictions Example: {'adminManagedRestrictions': '<boolean>', 'copyRequiresWriterPermission': '<boolean>', 'domainUsersOnly': '<boolean>', 'driveMembersOnly': '<boolean>', 'sharingFoldersRequiresOrganizerPermission': '<boolean>'}.
            themeId (string): themeId Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared Drive
        """
        request_body_data = None
        request_body_data = {
            "backgroundImageFile": backgroundImageFile,
            "backgroundImageLink": backgroundImageLink,
            "capabilities": capabilities,
            "colorRgb": colorRgb,
            "createdTime": createdTime,
            "hidden": hidden,
            "id": id,
            "kind": kind,
            "name": name,
            "orgUnitId": orgUnitId,
            "restrictions": restrictions,
            "themeId": themeId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/drives"
        query_params = {
            k: v
            for k, v in [
                ("requestId", requestId),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def get_ashared_drive_smetadata_by_id(
        self,
        driveId: str,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Get a shared drive's metadata by ID

        Args:
            driveId (string): driveId
            useDomainAdminAccess (string): Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared Drive
        """
        if driveId is None:
            raise ValueError("Missing required parameter 'driveId'.")
        url = f"{self.base_url}/drives/{driveId}"
        query_params = {
            k: v
            for k, v in [
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def permanently_delete_ashared_drive(
        self,
        driveId: str,
        allowItemDeletion: str | None = None,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> Any:
        """
        Permanently delete a shared drive

        Args:
            driveId (string): driveId
            allowItemDeletion (string): Whether any items inside the shared drive should also be deleted. This option is only supported when useDomainAdminAccess is also set to true. Example: '<boolean>'.
            useDomainAdminAccess (string): Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared Drive
        """
        if driveId is None:
            raise ValueError("Missing required parameter 'driveId'.")
        url = f"{self.base_url}/drives/{driveId}"
        query_params = {
            k: v
            for k, v in [
                ("allowItemDeletion", allowItemDeletion),
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def update_metadata_for_ashared_drive(
        self,
        driveId: str,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        backgroundImageFile: dict[str, Any] | None = None,
        backgroundImageLink: str | None = None,
        capabilities: dict[str, Any] | None = None,
        colorRgb: str | None = None,
        createdTime: str | None = None,
        hidden: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        name: str | None = None,
        orgUnitId: str | None = None,
        restrictions: dict[str, Any] | None = None,
        themeId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update metadata for a shared drive

        Args:
            driveId (string): driveId
            useDomainAdminAccess (string): Issue the request as a domain administrator. If set to true, then the requester is granted access if they're an administrator of the domain to which the shared drive belongs. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            backgroundImageFile (object): backgroundImageFile Example: {'id': '<string>', 'width': '<float>', 'xCoordinate': '<float>', 'yCoordinate': '<float>'}.
            backgroundImageLink (string): backgroundImageLink Example: '<string>'.
            capabilities (object): capabilities Example: {'canAddChildren': '<boolean>', 'canChangeCopyRequiresWriterPermissionRestriction': '<boolean>', 'canChangeDomainUsersOnlyRestriction': '<boolean>', 'canChangeDriveBackground': '<boolean>', 'canChangeDriveMembersOnlyRestriction': '<boolean>', 'canChangeSharingFoldersRequiresOrganizerPermissionRestriction': '<boolean>', 'canComment': '<boolean>', 'canCopy': '<boolean>', 'canDeleteChildren': '<boolean>', 'canDeleteDrive': '<boolean>', 'canDownload': '<boolean>', 'canEdit': '<boolean>', 'canListChildren': '<boolean>', 'canManageMembers': '<boolean>', 'canReadRevisions': '<boolean>', 'canRename': '<boolean>', 'canRenameDrive': '<boolean>', 'canResetDriveRestrictions': '<boolean>', 'canShare': '<boolean>', 'canTrashChildren': '<boolean>'}.
            colorRgb (string): colorRgb Example: '<string>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            hidden (string): hidden Example: '<boolean>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'drive#drive'.
            name (string): name Example: '<string>'.
            orgUnitId (string): orgUnitId Example: '<string>'.
            restrictions (object): restrictions Example: {'adminManagedRestrictions': '<boolean>', 'copyRequiresWriterPermission': '<boolean>', 'domainUsersOnly': '<boolean>', 'driveMembersOnly': '<boolean>', 'sharingFoldersRequiresOrganizerPermission': '<boolean>'}.
            themeId (string): themeId Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared Drive
        """
        if driveId is None:
            raise ValueError("Missing required parameter 'driveId'.")
        request_body_data = None
        request_body_data = {
            "backgroundImageFile": backgroundImageFile,
            "backgroundImageLink": backgroundImageLink,
            "capabilities": capabilities,
            "colorRgb": colorRgb,
            "createdTime": createdTime,
            "hidden": hidden,
            "id": id,
            "kind": kind,
            "name": name,
            "orgUnitId": orgUnitId,
            "restrictions": restrictions,
            "themeId": themeId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/drives/{driveId}"
        query_params = {
            k: v
            for k, v in [
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
        }
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def hide_drive_by_id_post(
        self,
        driveId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Hide a shared drive from the default view

        Args:
            driveId (string): driveId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared Drive
        """
        if driveId is None:
            raise ValueError("Missing required parameter 'driveId'.")
        request_body_data = None
        url = f"{self.base_url}/drives/{driveId}/hide"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def unhide_drive(
        self,
        driveId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Restore shared drive to default view

        Args:
            driveId (string): driveId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Shared Drive
        """
        if driveId is None:
            raise ValueError("Missing required parameter 'driveId'.")
        request_body_data = None
        url = f"{self.base_url}/drives/{driveId}/unhide"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def list_user_sfiles(
        self,
        corpora: str | None = None,
        driveId: str | None = None,
        includeItemsFromAllDrives: str | None = None,
        includeLabels: str | None = None,
        includePermissionsForView: str | None = None,
        includeTeamDriveItems: str | None = None,
        orderBy: str | None = None,
        pageSize: str | None = None,
        pageToken: str | None = None,
        q: str | None = None,
        spaces: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        teamDriveId: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        List user's files

        Args:
            corpora (string): Groupings of files to which the query applies. Supported groupings are: 'user' (files created by, opened by, or shared directly with the user), 'drive' (files in the specified shared drive as indicated by the 'driveId'), 'domain' (files shared to the user's domain), and 'allDrives' (A combination of 'user' and 'drive' for all drives where the user is a member). When able, use 'user' or 'drive', instead of 'allDrives', for efficiency. Example: '<string>'.
            driveId (string): ID of the shared drive to search. Example: '{{driveId}}'.
            includeItemsFromAllDrives (string): Whether both My Drive and shared drive items should be included in results. Example: '<boolean>'.
            includeLabels (string): A comma-separated list of IDs of labels to include in the labelInfo part of the response. Example: '<string>'.
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            includeTeamDriveItems (string): Deprecated use includeItemsFromAllDrives instead. Example: '<boolean>'.
            orderBy (string): A comma-separated list of sort keys. Valid keys are 'createdTime', 'folder', 'modifiedByMeTime', 'modifiedTime', 'name', 'name_natural', 'quotaBytesUsed', 'recency', 'sharedWithMeTime', 'starred', and 'viewedByMeTime'. Each key sorts ascending by default, but may be reversed with the 'desc' modifier. Example usage: ?orderBy=folder,modifiedTime desc,name. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored. Example: '<string>'.
            pageSize (string): The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached. Example: '<integer>'.
            pageToken (string): The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response. Example: '{{pageToken}}'.
            q (string): A query for filtering the file results. See the "Search for Files" guide for supported syntax. Example: 'query'.
            spaces (string): A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'. Example: '<string>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            teamDriveId (string): Deprecated use driveId instead. Example: '<string>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        url = f"{self.base_url}/files"
        query_params = {
            k: v
            for k, v in [
                ("corpora", corpora),
                ("driveId", driveId),
                ("includeItemsFromAllDrives", includeItemsFromAllDrives),
                ("includeLabels", includeLabels),
                ("includePermissionsForView", includePermissionsForView),
                ("includeTeamDriveItems", includeTeamDriveItems),
                ("orderBy", orderBy),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("q", q),
                ("spaces", spaces),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("teamDriveId", teamDriveId),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def create_anew_file(
        self,
        enforceSingleParent: str | None = None,
        ignoreDefaultVisibility: str | None = None,
        includeLabels: str | None = None,
        includePermissionsForView: str | None = None,
        keepRevisionForever: str | None = None,
        ocrLanguage: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        useContentAsIndexableText: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        appProperties: dict[str, Any] | None = None,
        capabilities: dict[str, Any] | None = None,
        contentHints: dict[str, Any] | None = None,
        contentRestrictions: list[dict[str, Any]] | None = None,
        copyRequiresWriterPermission: str | None = None,
        createdTime: str | None = None,
        description: str | None = None,
        driveId: str | None = None,
        explicitlyTrashed: str | None = None,
        exportLinks: dict[str, Any] | None = None,
        fileExtension: str | None = None,
        folderColorRgb: str | None = None,
        fullFileExtension: str | None = None,
        hasAugmentedPermissions: str | None = None,
        hasThumbnail: str | None = None,
        headRevisionId: str | None = None,
        iconLink: str | None = None,
        id: str | None = None,
        imageMediaMetadata: dict[str, Any] | None = None,
        isAppAuthorized: str | None = None,
        kind: str | None = None,
        labelInfo: dict[str, Any] | None = None,
        lastModifyingUser: dict[str, Any] | None = None,
        linkShareMetadata: dict[str, Any] | None = None,
        md5Checksum: str | None = None,
        mimeType: str | None = None,
        modifiedByMe: str | None = None,
        modifiedByMeTime: str | None = None,
        modifiedTime: str | None = None,
        name: str | None = None,
        originalFilename: str | None = None,
        ownedByMe: str | None = None,
        owners: list[dict[str, Any]] | None = None,
        parents: list[str] | None = None,
        permissionIds: list[str] | None = None,
        permissions: list[dict[str, Any]] | None = None,
        properties: dict[str, Any] | None = None,
        quotaBytesUsed: str | None = None,
        resourceKey: str | None = None,
        sha1Checksum: str | None = None,
        sha256Checksum: str | None = None,
        shared: str | None = None,
        sharedWithMeTime: str | None = None,
        sharingUser: dict[str, Any] | None = None,
        shortcutDetails: dict[str, Any] | None = None,
        size: str | None = None,
        spaces: list[str] | None = None,
        starred: str | None = None,
        teamDriveId: str | None = None,
        thumbnailLink: str | None = None,
        thumbnailVersion: str | None = None,
        trashed: str | None = None,
        trashedTime: str | None = None,
        trashingUser: dict[str, Any] | None = None,
        version: str | None = None,
        videoMediaMetadata: dict[str, Any] | None = None,
        viewedByMe: str | None = None,
        viewedByMeTime: str | None = None,
        viewersCanCopyContent: str | None = None,
        webContentLink: str | None = None,
        webViewLink: str | None = None,
        writersCanShare: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a new file

        Args:
            enforceSingleParent (string): Deprecated. Creating files in multiple folders is no longer supported. Example: '<boolean>'.
            ignoreDefaultVisibility (string): Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders. Example: '<boolean>'.
            includeLabels (string): A comma-separated list of IDs of labels to include in the labelInfo part of the response. Example: '<string>'.
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            keepRevisionForever (string): Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. Example: '<boolean>'.
            ocrLanguage (string): A language hint for OCR processing during image import (ISO 639-1 code). Example: '<string>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            useContentAsIndexableText (string): Whether to use the uploaded content as indexable text. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            appProperties (object): appProperties Example: {'essef3a': '<string>', 'magna9e': '<string>'}.
            capabilities (object): capabilities Example: {'canAcceptOwnership': '<boolean>', 'canAddChildren': '<boolean>', 'canAddFolderFromAnotherDrive': '<boolean>', 'canAddMyDriveParent': '<boolean>', 'canChangeCopyRequiresWriterPermission': '<boolean>', 'canChangeSecurityUpdateEnabled': '<boolean>', 'canChangeViewersCanCopyContent': '<boolean>', 'canComment': '<boolean>', 'canCopy': '<boolean>', 'canDelete': '<boolean>', 'canDeleteChildren': '<boolean>', 'canDownload': '<boolean>', 'canEdit': '<boolean>', 'canListChildren': '<boolean>', 'canModifyContent': '<boolean>', 'canModifyContentRestriction': '<boolean>', 'canModifyLabels': '<boolean>', 'canMoveChildrenOutOfDrive': '<boolean>', 'canMoveChildrenOutOfTeamDrive': '<boolean>', 'canMoveChildrenWithinDrive': '<boolean>', 'canMoveChildrenWithinTeamDrive': '<boolean>', 'canMoveItemIntoTeamDrive': '<boolean>', 'canMoveItemOutOfDrive': '<boolean>', 'canMoveItemOutOfTeamDrive': '<boolean>', 'canMoveItemWithinDrive': '<boolean>', 'canMoveItemWithinTeamDrive': '<boolean>', 'canMoveTeamDriveItem': '<boolean>', 'canReadDrive': '<boolean>', 'canReadLabels': '<boolean>', 'canReadRevisions': '<boolean>', 'canReadTeamDrive': '<boolean>', 'canRemoveChildren': '<boolean>', 'canRemoveMyDriveParent': '<boolean>', 'canRename': '<boolean>', 'canShare': '<boolean>', 'canTrash': '<boolean>', 'canTrashChildren': '<boolean>', 'canUntrash': '<boolean>'}.
            contentHints (object): contentHints Example: {'indexableText': '<string>', 'thumbnail': {'image': '<string>', 'mimeType': '<string>'}}.
            contentRestrictions (array): contentRestrictions Example: "[{'readOnly': '<boolean>', 'reason': '<string>', 'restrictingUser': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'restrictionTime': '<dateTime>', 'type': '<string>'}, {'readOnly': '<boolean>', 'reason': '<string>', 'restrictingUser': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'restrictionTime': '<dateTime>', 'type': '<string>'}]".
            copyRequiresWriterPermission (string): copyRequiresWriterPermission Example: '<boolean>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            description (string): description Example: '<string>'.
            driveId (string): driveId Example: '<string>'.
            explicitlyTrashed (string): explicitlyTrashed Example: '<boolean>'.
            exportLinks (object): exportLinks Example: {'ea2eb': '<string>'}.
            fileExtension (string): fileExtension Example: '<string>'.
            folderColorRgb (string): folderColorRgb Example: '<string>'.
            fullFileExtension (string): fullFileExtension Example: '<string>'.
            hasAugmentedPermissions (string): hasAugmentedPermissions Example: '<boolean>'.
            hasThumbnail (string): hasThumbnail Example: '<boolean>'.
            headRevisionId (string): headRevisionId Example: '<string>'.
            iconLink (string): iconLink Example: '<string>'.
            id (string): id Example: '<string>'.
            imageMediaMetadata (object): imageMediaMetadata Example: {'aperture': '<float>', 'cameraMake': '<string>', 'cameraModel': '<string>', 'colorSpace': '<string>', 'exposureBias': '<float>', 'exposureMode': '<string>', 'exposureTime': '<float>', 'flashUsed': '<boolean>', 'focalLength': '<float>', 'height': '<integer>', 'isoSpeed': '<integer>', 'lens': '<string>', 'location': {'altitude': '<double>', 'latitude': '<double>', 'longitude': '<double>'}, 'maxApertureValue': '<float>', 'meteringMode': '<string>', 'rotation': '<integer>', 'sensor': '<string>', 'subjectDistance': '<integer>', 'time': '<string>', 'whiteBalance': '<string>', 'width': '<integer>'}.
            isAppAuthorized (string): isAppAuthorized Example: '<boolean>'.
            kind (string): kind Example: 'drive#file'.
            labelInfo (object): labelInfo Example: {'labels': [{'fields': {'eu_9c': {'dateString': ['<date>', '<date>'], 'id': '<string>', 'integer': ['<int64>', '<int64>'], 'kind': 'drive#labelField', 'selection': ['<string>', '<string>'], 'text': ['<string>', '<string>'], 'user': [{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}], 'valueType': '<string>'}}, 'id': '<string>', 'kind': 'drive#label', 'revisionId': '<string>'}, {'fields': {'dolor65': {'dateString': ['<date>', '<date>'], 'id': '<string>', 'integer': ['<int64>', '<int64>'], 'kind': 'drive#labelField', 'selection': ['<string>', '<string>'], 'text': ['<string>', '<string>'], 'user': [{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}], 'valueType': '<string>'}}, 'id': '<string>', 'kind': 'drive#label', 'revisionId': '<string>'}]}.
            lastModifyingUser (object): lastModifyingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            linkShareMetadata (object): linkShareMetadata Example: {'securityUpdateEligible': '<boolean>', 'securityUpdateEnabled': '<boolean>'}.
            md5Checksum (string): md5Checksum Example: '<string>'.
            mimeType (string): mimeType Example: '<string>'.
            modifiedByMe (string): modifiedByMe Example: '<boolean>'.
            modifiedByMeTime (string): modifiedByMeTime Example: '<dateTime>'.
            modifiedTime (string): modifiedTime Example: '<dateTime>'.
            name (string): name Example: '<string>'.
            originalFilename (string): originalFilename Example: '<string>'.
            ownedByMe (string): ownedByMe Example: '<boolean>'.
            owners (array): owners Example: "[{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}]".
            parents (array): parents Example: "['<string>', '<string>']".
            permissionIds (array): permissionIds Example: "['<string>', '<string>']".
            permissions (array): permissions Example: "[{'allowFileDiscovery': '<boolean>', 'deleted': '<boolean>', 'displayName': '<string>', 'domain': '<string>', 'emailAddress': '<string>', 'expirationTime': '<dateTime>', 'id': '<string>', 'kind': 'drive#permission', 'pendingOwner': '<boolean>', 'permissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}], 'photoLink': '<string>', 'role': '<string>', 'teamDrivePermissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}], 'type': '<string>', 'view': '<string>'}, {'allowFileDiscovery': '<boolean>', 'deleted': '<boolean>', 'displayName': '<string>', 'domain': '<string>', 'emailAddress': '<string>', 'expirationTime': '<dateTime>', 'id': '<string>', 'kind': 'drive#permission', 'pendingOwner': '<boolean>', 'permissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}], 'photoLink': '<string>', 'role': '<string>', 'teamDrivePermissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}], 'type': '<string>', 'view': '<string>'}]".
            properties (object): properties Example: {'eiusmod_21': '<string>', 'non3c': '<string>'}.
            quotaBytesUsed (string): quotaBytesUsed Example: '<int64>'.
            resourceKey (string): resourceKey Example: '<string>'.
            sha1Checksum (string): sha1Checksum Example: '<string>'.
            sha256Checksum (string): sha256Checksum Example: '<string>'.
            shared (string): shared Example: '<boolean>'.
            sharedWithMeTime (string): sharedWithMeTime Example: '<dateTime>'.
            sharingUser (object): sharingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            shortcutDetails (object): shortcutDetails Example: {'targetId': '<string>', 'targetMimeType': '<string>', 'targetResourceKey': '<string>'}.
            size (string): size Example: '<int64>'.
            spaces (array): spaces Example: "['<string>', '<string>']".
            starred (string): starred Example: '<boolean>'.
            teamDriveId (string): teamDriveId Example: '<string>'.
            thumbnailLink (string): thumbnailLink Example: '<string>'.
            thumbnailVersion (string): thumbnailVersion Example: '<int64>'.
            trashed (string): trashed Example: '<boolean>'.
            trashedTime (string): trashedTime Example: '<dateTime>'.
            trashingUser (object): trashingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            version (string): version Example: '<int64>'.
            videoMediaMetadata (object): videoMediaMetadata Example: {'durationMillis': '<int64>', 'height': '<integer>', 'width': '<integer>'}.
            viewedByMe (string): viewedByMe Example: '<boolean>'.
            viewedByMeTime (string): viewedByMeTime Example: '<dateTime>'.
            viewersCanCopyContent (string): viewersCanCopyContent Example: '<boolean>'.
            webContentLink (string): webContentLink Example: '<string>'.
            webViewLink (string): webViewLink Example: '<string>'.
            writersCanShare (string): writersCanShare Example: '<boolean>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        request_body_data = None
        request_body_data = {
            "appProperties": appProperties,
            "capabilities": capabilities,
            "contentHints": contentHints,
            "contentRestrictions": contentRestrictions,
            "copyRequiresWriterPermission": copyRequiresWriterPermission,
            "createdTime": createdTime,
            "description": description,
            "driveId": driveId,
            "explicitlyTrashed": explicitlyTrashed,
            "exportLinks": exportLinks,
            "fileExtension": fileExtension,
            "folderColorRgb": folderColorRgb,
            "fullFileExtension": fullFileExtension,
            "hasAugmentedPermissions": hasAugmentedPermissions,
            "hasThumbnail": hasThumbnail,
            "headRevisionId": headRevisionId,
            "iconLink": iconLink,
            "id": id,
            "imageMediaMetadata": imageMediaMetadata,
            "isAppAuthorized": isAppAuthorized,
            "kind": kind,
            "labelInfo": labelInfo,
            "lastModifyingUser": lastModifyingUser,
            "linkShareMetadata": linkShareMetadata,
            "md5Checksum": md5Checksum,
            "mimeType": mimeType,
            "modifiedByMe": modifiedByMe,
            "modifiedByMeTime": modifiedByMeTime,
            "modifiedTime": modifiedTime,
            "name": name,
            "originalFilename": originalFilename,
            "ownedByMe": ownedByMe,
            "owners": owners,
            "parents": parents,
            "permissionIds": permissionIds,
            "permissions": permissions,
            "properties": properties,
            "quotaBytesUsed": quotaBytesUsed,
            "resourceKey": resourceKey,
            "sha1Checksum": sha1Checksum,
            "sha256Checksum": sha256Checksum,
            "shared": shared,
            "sharedWithMeTime": sharedWithMeTime,
            "sharingUser": sharingUser,
            "shortcutDetails": shortcutDetails,
            "size": size,
            "spaces": spaces,
            "starred": starred,
            "teamDriveId": teamDriveId,
            "thumbnailLink": thumbnailLink,
            "thumbnailVersion": thumbnailVersion,
            "trashed": trashed,
            "trashedTime": trashedTime,
            "trashingUser": trashingUser,
            "version": version,
            "videoMediaMetadata": videoMediaMetadata,
            "viewedByMe": viewedByMe,
            "viewedByMeTime": viewedByMeTime,
            "viewersCanCopyContent": viewersCanCopyContent,
            "webContentLink": webContentLink,
            "webViewLink": webViewLink,
            "writersCanShare": writersCanShare,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files"
        query_params = {
            k: v
            for k, v in [
                ("enforceSingleParent", enforceSingleParent),
                ("ignoreDefaultVisibility", ignoreDefaultVisibility),
                ("includeLabels", includeLabels),
                ("includePermissionsForView", includePermissionsForView),
                ("keepRevisionForever", keepRevisionForever),
                ("ocrLanguage", ocrLanguage),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("useContentAsIndexableText", useContentAsIndexableText),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def generate_aset_of_file_ids(
        self,
        count: str | None = None,
        space: str | None = None,
        type: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Generate a set of file IDs

        Args:
            count (string): The number of IDs to return. Example: '<integer>'.
            space (string): The space in which the IDs can be used to create new files. Supported values are 'drive' and 'appDataFolder'. (Default: 'drive') Example: '<string>'.
            type (string): The type of items which the IDs can be used for. Supported values are 'files' and 'shortcuts'. Note that 'shortcuts' are only supported in the drive 'space'. (Default: 'files') Example: '<string>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        url = f"{self.base_url}/files/generateIds"
        query_params = {
            k: v
            for k, v in [
                ("count", count),
                ("space", space),
                ("type", type),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def empty_trash_files(
        self,
        driveId: str | None = None,
        enforceSingleParent: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> Any:
        """
        Permanently delete all of the trashed files

        Args:
            driveId (string): If set, empties the trash of the provided shared drive. Example: '{{driveId}}'.
            enforceSingleParent (string): Deprecated. If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner's root. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        url = f"{self.base_url}/files/trash"
        query_params = {
            k: v
            for k, v in [
                ("driveId", driveId),
                ("enforceSingleParent", enforceSingleParent),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def get_file_metadata(
        self,
        fileId: str,
        acknowledgeAbuse: str | None = None,
        includeLabels: str | None = None,
        includePermissionsForView: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Get a file's metadata. Use to it to get infromation like parents

        Args:
            fileId (string): fileId
            acknowledgeAbuse (string): Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media. Example: '<boolean>'.
            includeLabels (string): A comma-separated list of IDs of labels to include in the labelInfo part of the response. Example: '<string>'.
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: "id","name","parents"
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        url = f"{self.base_url}/files/{fileId}"
        query_params = {
            k: v
            for k, v in [
                ("acknowledgeAbuse", acknowledgeAbuse),
                ("includeLabels", includeLabels),
                ("includePermissionsForView", includePermissionsForView),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def delete_file_by_id(
        self,
        fileId: str,
        enforceSingleParent: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> Any:
        """
        Permanently delete a file without moving it to the trash

        Args:
            fileId (string): fileId
            enforceSingleParent (string): Deprecated. If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner's root. Example: '<boolean>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        url = f"{self.base_url}/files/{fileId}"
        query_params = {
            k: v
            for k, v in [
                ("enforceSingleParent", enforceSingleParent),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def update_file(
        self,
        fileId: str,
        addParents: str | None = None,
        enforceSingleParent: str | None = None,
        includeLabels: str | None = None,
        includePermissionsForView: str | None = None,
        keepRevisionForever: str | None = None,
        ocrLanguage: str | None = None,
        removeParents: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        useContentAsIndexableText: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        appProperties: dict[str, Any] | None = None,
        capabilities: dict[str, Any] | None = None,
        contentHints: dict[str, Any] | None = None,
        contentRestrictions: list[dict[str, Any]] | None = None,
        copyRequiresWriterPermission: str | None = None,
        createdTime: str | None = None,
        description: str | None = None,
        driveId: str | None = None,
        explicitlyTrashed: str | None = None,
        exportLinks: dict[str, Any] | None = None,
        fileExtension: str | None = None,
        folderColorRgb: str | None = None,
        fullFileExtension: str | None = None,
        hasAugmentedPermissions: str | None = None,
        hasThumbnail: str | None = None,
        headRevisionId: str | None = None,
        iconLink: str | None = None,
        id: str | None = None,
        imageMediaMetadata: dict[str, Any] | None = None,
        isAppAuthorized: str | None = None,
        kind: str | None = None,
        labelInfo: dict[str, Any] | None = None,
        lastModifyingUser: dict[str, Any] | None = None,
        linkShareMetadata: dict[str, Any] | None = None,
        md5Checksum: str | None = None,
        mimeType: str | None = None,
        modifiedByMe: str | None = None,
        modifiedByMeTime: str | None = None,
        modifiedTime: str | None = None,
        name: str | None = None,
        originalFilename: str | None = None,
        ownedByMe: str | None = None,
        owners: list[dict[str, Any]] | None = None,
        parents: list[str] | None = None,
        permissionIds: list[str] | None = None,
        permissions: list[dict[str, Any]] | None = None,
        properties: dict[str, Any] | None = None,
        quotaBytesUsed: str | None = None,
        resourceKey: str | None = None,
        sha1Checksum: str | None = None,
        sha256Checksum: str | None = None,
        shared: str | None = None,
        sharedWithMeTime: str | None = None,
        sharingUser: dict[str, Any] | None = None,
        shortcutDetails: dict[str, Any] | None = None,
        size: str | None = None,
        spaces: list[str] | None = None,
        starred: str | None = None,
        teamDriveId: str | None = None,
        thumbnailLink: str | None = None,
        thumbnailVersion: str | None = None,
        trashed: str | None = None,
        trashedTime: str | None = None,
        trashingUser: dict[str, Any] | None = None,
        version: str | None = None,
        videoMediaMetadata: dict[str, Any] | None = None,
        viewedByMe: str | None = None,
        viewedByMeTime: str | None = None,
        viewersCanCopyContent: str | None = None,
        webContentLink: str | None = None,
        webViewLink: str | None = None,
        writersCanShare: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a file's metadata and/or content

        Args:
            fileId (string): fileId
            addParents (string): A comma-separated list of parent IDs to add. Example: '<string>'.
            enforceSingleParent (string): Deprecated. Adding files to multiple folders is no longer supported. Use shortcuts instead. Example: '<boolean>'.
            includeLabels (string): A comma-separated list of IDs of labels to include in the labelInfo part of the response. Example: '<string>'.
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            keepRevisionForever (string): Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. Example: '<boolean>'.
            ocrLanguage (string): A language hint for OCR processing during image import (ISO 639-1 code). Example: '<string>'.
            removeParents (string): A comma-separated list of parent IDs to remove. Example: '<string>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            useContentAsIndexableText (string): Whether to use the uploaded content as indexable text. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            appProperties (object): appProperties Example: {'essef3a': '<string>', 'magna9e': '<string>'}.
            capabilities (object): capabilities Example: {'canAcceptOwnership': '<boolean>', 'canAddChildren': '<boolean>', 'canAddFolderFromAnotherDrive': '<boolean>', 'canAddMyDriveParent': '<boolean>', 'canChangeCopyRequiresWriterPermission': '<boolean>', 'canChangeSecurityUpdateEnabled': '<boolean>', 'canChangeViewersCanCopyContent': '<boolean>', 'canComment': '<boolean>', 'canCopy': '<boolean>', 'canDelete': '<boolean>', 'canDeleteChildren': '<boolean>', 'canDownload': '<boolean>', 'canEdit': '<boolean>', 'canListChildren': '<boolean>', 'canModifyContent': '<boolean>', 'canModifyContentRestriction': '<boolean>', 'canModifyLabels': '<boolean>', 'canMoveChildrenOutOfDrive': '<boolean>', 'canMoveChildrenOutOfTeamDrive': '<boolean>', 'canMoveChildrenWithinDrive': '<boolean>', 'canMoveChildrenWithinTeamDrive': '<boolean>', 'canMoveItemIntoTeamDrive': '<boolean>', 'canMoveItemOutOfDrive': '<boolean>', 'canMoveItemOutOfTeamDrive': '<boolean>', 'canMoveItemWithinDrive': '<boolean>', 'canMoveItemWithinTeamDrive': '<boolean>', 'canMoveTeamDriveItem': '<boolean>', 'canReadDrive': '<boolean>', 'canReadLabels': '<boolean>', 'canReadRevisions': '<boolean>', 'canReadTeamDrive': '<boolean>', 'canRemoveChildren': '<boolean>', 'canRemoveMyDriveParent': '<boolean>', 'canRename': '<boolean>', 'canShare': '<boolean>', 'canTrash': '<boolean>', 'canTrashChildren': '<boolean>', 'canUntrash': '<boolean>'}.
            contentHints (object): contentHints Example: {'indexableText': '<string>', 'thumbnail': {'image': '<string>', 'mimeType': '<string>'}}.
            contentRestrictions (array): contentRestrictions Example: "[{'readOnly': '<boolean>', 'reason': '<string>', 'restrictingUser': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'restrictionTime': '<dateTime>', 'type': '<string>'}, {'readOnly': '<boolean>', 'reason': '<string>', 'restrictingUser': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'restrictionTime': '<dateTime>', 'type': '<string>'}]".
            copyRequiresWriterPermission (string): copyRequiresWriterPermission Example: '<boolean>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            description (string): description Example: '<string>'.
            driveId (string): driveId Example: '<string>'.
            explicitlyTrashed (string): explicitlyTrashed Example: '<boolean>'.
            exportLinks (object): exportLinks Example: {'ea2eb': '<string>'}.
            fileExtension (string): fileExtension Example: '<string>'.
            folderColorRgb (string): folderColorRgb Example: '<string>'.
            fullFileExtension (string): fullFileExtension Example: '<string>'.
            hasAugmentedPermissions (string): hasAugmentedPermissions Example: '<boolean>'.
            hasThumbnail (string): hasThumbnail Example: '<boolean>'.
            headRevisionId (string): headRevisionId Example: '<string>'.
            iconLink (string): iconLink Example: '<string>'.
            id (string): id Example: '<string>'.
            imageMediaMetadata (object): imageMediaMetadata Example: {'aperture': '<float>', 'cameraMake': '<string>', 'cameraModel': '<string>', 'colorSpace': '<string>', 'exposureBias': '<float>', 'exposureMode': '<string>', 'exposureTime': '<float>', 'flashUsed': '<boolean>', 'focalLength': '<float>', 'height': '<integer>', 'isoSpeed': '<integer>', 'lens': '<string>', 'location': {'altitude': '<double>', 'latitude': '<double>', 'longitude': '<double>'}, 'maxApertureValue': '<float>', 'meteringMode': '<string>', 'rotation': '<integer>', 'sensor': '<string>', 'subjectDistance': '<integer>', 'time': '<string>', 'whiteBalance': '<string>', 'width': '<integer>'}.
            isAppAuthorized (string): isAppAuthorized Example: '<boolean>'.
            kind (string): kind Example: 'drive#file'.
            labelInfo (object): labelInfo Example: {'labels': [{'fields': {'eu_9c': {'dateString': ['<date>', '<date>'], 'id': '<string>', 'integer': ['<int64>', '<int64>'], 'kind': 'drive#labelField', 'selection': ['<string>', '<string>'], 'text': ['<string>', '<string>'], 'user': [{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}], 'valueType': '<string>'}}, 'id': '<string>', 'kind': 'drive#label', 'revisionId': '<string>'}, {'fields': {'dolor65': {'dateString': ['<date>', '<date>'], 'id': '<string>', 'integer': ['<int64>', '<int64>'], 'kind': 'drive#labelField', 'selection': ['<string>', '<string>'], 'text': ['<string>', '<string>'], 'user': [{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}], 'valueType': '<string>'}}, 'id': '<string>', 'kind': 'drive#label', 'revisionId': '<string>'}]}.
            lastModifyingUser (object): lastModifyingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            linkShareMetadata (object): linkShareMetadata Example: {'securityUpdateEligible': '<boolean>', 'securityUpdateEnabled': '<boolean>'}.
            md5Checksum (string): md5Checksum Example: '<string>'.
            mimeType (string): mimeType Example: '<string>'.
            modifiedByMe (string): modifiedByMe Example: '<boolean>'.
            modifiedByMeTime (string): modifiedByMeTime Example: '<dateTime>'.
            modifiedTime (string): modifiedTime Example: '<dateTime>'.
            name (string): name Example: '<string>'.
            originalFilename (string): originalFilename Example: '<string>'.
            ownedByMe (string): ownedByMe Example: '<boolean>'.
            owners (array): owners Example: "[{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}]".
            parents (array): parents Example: "['<string>', '<string>']".
            permissionIds (array): permissionIds Example: "['<string>', '<string>']".
            permissions (array): permissions Example: "[{'allowFileDiscovery': '<boolean>', 'deleted': '<boolean>', 'displayName': '<string>', 'domain': '<string>', 'emailAddress': '<string>', 'expirationTime': '<dateTime>', 'id': '<string>', 'kind': 'drive#permission', 'pendingOwner': '<boolean>', 'permissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}], 'photoLink': '<string>', 'role': '<string>', 'teamDrivePermissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}], 'type': '<string>', 'view': '<string>'}, {'allowFileDiscovery': '<boolean>', 'deleted': '<boolean>', 'displayName': '<string>', 'domain': '<string>', 'emailAddress': '<string>', 'expirationTime': '<dateTime>', 'id': '<string>', 'kind': 'drive#permission', 'pendingOwner': '<boolean>', 'permissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}], 'photoLink': '<string>', 'role': '<string>', 'teamDrivePermissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}], 'type': '<string>', 'view': '<string>'}]".
            properties (object): properties Example: {'eiusmod_21': '<string>', 'non3c': '<string>'}.
            quotaBytesUsed (string): quotaBytesUsed Example: '<int64>'.
            resourceKey (string): resourceKey Example: '<string>'.
            sha1Checksum (string): sha1Checksum Example: '<string>'.
            sha256Checksum (string): sha256Checksum Example: '<string>'.
            shared (string): shared Example: '<boolean>'.
            sharedWithMeTime (string): sharedWithMeTime Example: '<dateTime>'.
            sharingUser (object): sharingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            shortcutDetails (object): shortcutDetails Example: {'targetId': '<string>', 'targetMimeType': '<string>', 'targetResourceKey': '<string>'}.
            size (string): size Example: '<int64>'.
            spaces (array): spaces Example: "['<string>', '<string>']".
            starred (string): starred Example: '<boolean>'.
            teamDriveId (string): teamDriveId Example: '<string>'.
            thumbnailLink (string): thumbnailLink Example: '<string>'.
            thumbnailVersion (string): thumbnailVersion Example: '<int64>'.
            trashed (string): trashed Example: '<boolean>'.
            trashedTime (string): trashedTime Example: '<dateTime>'.
            trashingUser (object): trashingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            version (string): version Example: '<int64>'.
            videoMediaMetadata (object): videoMediaMetadata Example: {'durationMillis': '<int64>', 'height': '<integer>', 'width': '<integer>'}.
            viewedByMe (string): viewedByMe Example: '<boolean>'.
            viewedByMeTime (string): viewedByMeTime Example: '<dateTime>'.
            viewersCanCopyContent (string): viewersCanCopyContent Example: '<boolean>'.
            webContentLink (string): webContentLink Example: '<string>'.
            webViewLink (string): webViewLink Example: '<string>'.
            writersCanShare (string): writersCanShare Example: '<boolean>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        request_body_data = None
        request_body_data = {
            "appProperties": appProperties,
            "capabilities": capabilities,
            "contentHints": contentHints,
            "contentRestrictions": contentRestrictions,
            "copyRequiresWriterPermission": copyRequiresWriterPermission,
            "createdTime": createdTime,
            "description": description,
            "driveId": driveId,
            "explicitlyTrashed": explicitlyTrashed,
            "exportLinks": exportLinks,
            "fileExtension": fileExtension,
            "folderColorRgb": folderColorRgb,
            "fullFileExtension": fullFileExtension,
            "hasAugmentedPermissions": hasAugmentedPermissions,
            "hasThumbnail": hasThumbnail,
            "headRevisionId": headRevisionId,
            "iconLink": iconLink,
            "id": id,
            "imageMediaMetadata": imageMediaMetadata,
            "isAppAuthorized": isAppAuthorized,
            "kind": kind,
            "labelInfo": labelInfo,
            "lastModifyingUser": lastModifyingUser,
            "linkShareMetadata": linkShareMetadata,
            "md5Checksum": md5Checksum,
            "mimeType": mimeType,
            "modifiedByMe": modifiedByMe,
            "modifiedByMeTime": modifiedByMeTime,
            "modifiedTime": modifiedTime,
            "name": name,
            "originalFilename": originalFilename,
            "ownedByMe": ownedByMe,
            "owners": owners,
            "parents": parents,
            "permissionIds": permissionIds,
            "permissions": permissions,
            "properties": properties,
            "quotaBytesUsed": quotaBytesUsed,
            "resourceKey": resourceKey,
            "sha1Checksum": sha1Checksum,
            "sha256Checksum": sha256Checksum,
            "shared": shared,
            "sharedWithMeTime": sharedWithMeTime,
            "sharingUser": sharingUser,
            "shortcutDetails": shortcutDetails,
            "size": size,
            "spaces": spaces,
            "starred": starred,
            "teamDriveId": teamDriveId,
            "thumbnailLink": thumbnailLink,
            "thumbnailVersion": thumbnailVersion,
            "trashed": trashed,
            "trashedTime": trashedTime,
            "trashingUser": trashingUser,
            "version": version,
            "videoMediaMetadata": videoMediaMetadata,
            "viewedByMe": viewedByMe,
            "viewedByMeTime": viewedByMeTime,
            "viewersCanCopyContent": viewersCanCopyContent,
            "webContentLink": webContentLink,
            "webViewLink": webViewLink,
            "writersCanShare": writersCanShare,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}"
        query_params = {
            k: v
            for k, v in [
                ("addParents", addParents),
                ("enforceSingleParent", enforceSingleParent),
                ("includeLabels", includeLabels),
                ("includePermissionsForView", includePermissionsForView),
                ("keepRevisionForever", keepRevisionForever),
                ("ocrLanguage", ocrLanguage),
                ("removeParents", removeParents),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("useContentAsIndexableText", useContentAsIndexableText),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
        }
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def copy_file_by_id(
        self,
        fileId: str,
        enforceSingleParent: str | None = None,
        ignoreDefaultVisibility: str | None = None,
        includeLabels: str | None = None,
        includePermissionsForView: str | None = None,
        keepRevisionForever: str | None = None,
        ocrLanguage: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        appProperties: dict[str, Any] | None = None,
        capabilities: dict[str, Any] | None = None,
        contentHints: dict[str, Any] | None = None,
        contentRestrictions: list[dict[str, Any]] | None = None,
        copyRequiresWriterPermission: str | None = None,
        createdTime: str | None = None,
        description: str | None = None,
        driveId: str | None = None,
        explicitlyTrashed: str | None = None,
        exportLinks: dict[str, Any] | None = None,
        fileExtension: str | None = None,
        folderColorRgb: str | None = None,
        fullFileExtension: str | None = None,
        hasAugmentedPermissions: str | None = None,
        hasThumbnail: str | None = None,
        headRevisionId: str | None = None,
        iconLink: str | None = None,
        id: str | None = None,
        imageMediaMetadata: dict[str, Any] | None = None,
        isAppAuthorized: str | None = None,
        kind: str | None = None,
        labelInfo: dict[str, Any] | None = None,
        lastModifyingUser: dict[str, Any] | None = None,
        linkShareMetadata: dict[str, Any] | None = None,
        md5Checksum: str | None = None,
        mimeType: str | None = None,
        modifiedByMe: str | None = None,
        modifiedByMeTime: str | None = None,
        modifiedTime: str | None = None,
        name: str | None = None,
        originalFilename: str | None = None,
        ownedByMe: str | None = None,
        owners: list[dict[str, Any]] | None = None,
        parents: list[str] | None = None,
        permissionIds: list[str] | None = None,
        permissions: list[dict[str, Any]] | None = None,
        properties: dict[str, Any] | None = None,
        quotaBytesUsed: str | None = None,
        resourceKey: str | None = None,
        sha1Checksum: str | None = None,
        sha256Checksum: str | None = None,
        shared: str | None = None,
        sharedWithMeTime: str | None = None,
        sharingUser: dict[str, Any] | None = None,
        shortcutDetails: dict[str, Any] | None = None,
        size: str | None = None,
        spaces: list[str] | None = None,
        starred: str | None = None,
        teamDriveId: str | None = None,
        thumbnailLink: str | None = None,
        thumbnailVersion: str | None = None,
        trashed: str | None = None,
        trashedTime: str | None = None,
        trashingUser: dict[str, Any] | None = None,
        version: str | None = None,
        videoMediaMetadata: dict[str, Any] | None = None,
        viewedByMe: str | None = None,
        viewedByMeTime: str | None = None,
        viewersCanCopyContent: str | None = None,
        webContentLink: str | None = None,
        webViewLink: str | None = None,
        writersCanShare: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a copy of a file and apply any requested update

        Args:
            fileId (string): fileId
            enforceSingleParent (string): Deprecated. Copying files into multiple folders is no longer supported. Use shortcuts instead. Example: '<boolean>'.
            ignoreDefaultVisibility (string): Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders. Example: '<boolean>'.
            includeLabels (string): A comma-separated list of IDs of labels to include in the labelInfo part of the response. Example: '<string>'.
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            keepRevisionForever (string): Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. Example: '<boolean>'.
            ocrLanguage (string): A language hint for OCR processing during image import (ISO 639-1 code). Example: '<string>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            appProperties (object): appProperties Example: {'essef3a': '<string>', 'magna9e': '<string>'}.
            capabilities (object): capabilities Example: {'canAcceptOwnership': '<boolean>', 'canAddChildren': '<boolean>', 'canAddFolderFromAnotherDrive': '<boolean>', 'canAddMyDriveParent': '<boolean>', 'canChangeCopyRequiresWriterPermission': '<boolean>', 'canChangeSecurityUpdateEnabled': '<boolean>', 'canChangeViewersCanCopyContent': '<boolean>', 'canComment': '<boolean>', 'canCopy': '<boolean>', 'canDelete': '<boolean>', 'canDeleteChildren': '<boolean>', 'canDownload': '<boolean>', 'canEdit': '<boolean>', 'canListChildren': '<boolean>', 'canModifyContent': '<boolean>', 'canModifyContentRestriction': '<boolean>', 'canModifyLabels': '<boolean>', 'canMoveChildrenOutOfDrive': '<boolean>', 'canMoveChildrenOutOfTeamDrive': '<boolean>', 'canMoveChildrenWithinDrive': '<boolean>', 'canMoveChildrenWithinTeamDrive': '<boolean>', 'canMoveItemIntoTeamDrive': '<boolean>', 'canMoveItemOutOfDrive': '<boolean>', 'canMoveItemOutOfTeamDrive': '<boolean>', 'canMoveItemWithinDrive': '<boolean>', 'canMoveItemWithinTeamDrive': '<boolean>', 'canMoveTeamDriveItem': '<boolean>', 'canReadDrive': '<boolean>', 'canReadLabels': '<boolean>', 'canReadRevisions': '<boolean>', 'canReadTeamDrive': '<boolean>', 'canRemoveChildren': '<boolean>', 'canRemoveMyDriveParent': '<boolean>', 'canRename': '<boolean>', 'canShare': '<boolean>', 'canTrash': '<boolean>', 'canTrashChildren': '<boolean>', 'canUntrash': '<boolean>'}.
            contentHints (object): contentHints Example: {'indexableText': '<string>', 'thumbnail': {'image': '<string>', 'mimeType': '<string>'}}.
            contentRestrictions (array): contentRestrictions Example: "[{'readOnly': '<boolean>', 'reason': '<string>', 'restrictingUser': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'restrictionTime': '<dateTime>', 'type': '<string>'}, {'readOnly': '<boolean>', 'reason': '<string>', 'restrictingUser': {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, 'restrictionTime': '<dateTime>', 'type': '<string>'}]".
            copyRequiresWriterPermission (string): copyRequiresWriterPermission Example: '<boolean>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            description (string): description Example: '<string>'.
            driveId (string): driveId Example: '<string>'.
            explicitlyTrashed (string): explicitlyTrashed Example: '<boolean>'.
            exportLinks (object): exportLinks Example: {'ea2eb': '<string>'}.
            fileExtension (string): fileExtension Example: '<string>'.
            folderColorRgb (string): folderColorRgb Example: '<string>'.
            fullFileExtension (string): fullFileExtension Example: '<string>'.
            hasAugmentedPermissions (string): hasAugmentedPermissions Example: '<boolean>'.
            hasThumbnail (string): hasThumbnail Example: '<boolean>'.
            headRevisionId (string): headRevisionId Example: '<string>'.
            iconLink (string): iconLink Example: '<string>'.
            id (string): id Example: '<string>'.
            imageMediaMetadata (object): imageMediaMetadata Example: {'aperture': '<float>', 'cameraMake': '<string>', 'cameraModel': '<string>', 'colorSpace': '<string>', 'exposureBias': '<float>', 'exposureMode': '<string>', 'exposureTime': '<float>', 'flashUsed': '<boolean>', 'focalLength': '<float>', 'height': '<integer>', 'isoSpeed': '<integer>', 'lens': '<string>', 'location': {'altitude': '<double>', 'latitude': '<double>', 'longitude': '<double>'}, 'maxApertureValue': '<float>', 'meteringMode': '<string>', 'rotation': '<integer>', 'sensor': '<string>', 'subjectDistance': '<integer>', 'time': '<string>', 'whiteBalance': '<string>', 'width': '<integer>'}.
            isAppAuthorized (string): isAppAuthorized Example: '<boolean>'.
            kind (string): kind Example: 'drive#file'.
            labelInfo (object): labelInfo Example: {'labels': [{'fields': {'eu_9c': {'dateString': ['<date>', '<date>'], 'id': '<string>', 'integer': ['<int64>', '<int64>'], 'kind': 'drive#labelField', 'selection': ['<string>', '<string>'], 'text': ['<string>', '<string>'], 'user': [{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}], 'valueType': '<string>'}}, 'id': '<string>', 'kind': 'drive#label', 'revisionId': '<string>'}, {'fields': {'dolor65': {'dateString': ['<date>', '<date>'], 'id': '<string>', 'integer': ['<int64>', '<int64>'], 'kind': 'drive#labelField', 'selection': ['<string>', '<string>'], 'text': ['<string>', '<string>'], 'user': [{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}], 'valueType': '<string>'}}, 'id': '<string>', 'kind': 'drive#label', 'revisionId': '<string>'}]}.
            lastModifyingUser (object): lastModifyingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            linkShareMetadata (object): linkShareMetadata Example: {'securityUpdateEligible': '<boolean>', 'securityUpdateEnabled': '<boolean>'}.
            md5Checksum (string): md5Checksum Example: '<string>'.
            mimeType (string): mimeType Example: '<string>'.
            modifiedByMe (string): modifiedByMe Example: '<boolean>'.
            modifiedByMeTime (string): modifiedByMeTime Example: '<dateTime>'.
            modifiedTime (string): modifiedTime Example: '<dateTime>'.
            name (string): name Example: '<string>'.
            originalFilename (string): originalFilename Example: '<string>'.
            ownedByMe (string): ownedByMe Example: '<boolean>'.
            owners (array): owners Example: "[{'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}, {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}]".
            parents (array): parents Example: "['<string>', '<string>']".
            permissionIds (array): permissionIds Example: "['<string>', '<string>']".
            permissions (array): permissions Example: "[{'allowFileDiscovery': '<boolean>', 'deleted': '<boolean>', 'displayName': '<string>', 'domain': '<string>', 'emailAddress': '<string>', 'expirationTime': '<dateTime>', 'id': '<string>', 'kind': 'drive#permission', 'pendingOwner': '<boolean>', 'permissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}], 'photoLink': '<string>', 'role': '<string>', 'teamDrivePermissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}], 'type': '<string>', 'view': '<string>'}, {'allowFileDiscovery': '<boolean>', 'deleted': '<boolean>', 'displayName': '<string>', 'domain': '<string>', 'emailAddress': '<string>', 'expirationTime': '<dateTime>', 'id': '<string>', 'kind': 'drive#permission', 'pendingOwner': '<boolean>', 'permissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}], 'photoLink': '<string>', 'role': '<string>', 'teamDrivePermissionDetails': [{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}], 'type': '<string>', 'view': '<string>'}]".
            properties (object): properties Example: {'eiusmod_21': '<string>', 'non3c': '<string>'}.
            quotaBytesUsed (string): quotaBytesUsed Example: '<int64>'.
            resourceKey (string): resourceKey Example: '<string>'.
            sha1Checksum (string): sha1Checksum Example: '<string>'.
            sha256Checksum (string): sha256Checksum Example: '<string>'.
            shared (string): shared Example: '<boolean>'.
            sharedWithMeTime (string): sharedWithMeTime Example: '<dateTime>'.
            sharingUser (object): sharingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            shortcutDetails (object): shortcutDetails Example: {'targetId': '<string>', 'targetMimeType': '<string>', 'targetResourceKey': '<string>'}.
            size (string): size Example: '<int64>'.
            spaces (array): spaces Example: "['<string>', '<string>']".
            starred (string): starred Example: '<boolean>'.
            teamDriveId (string): teamDriveId Example: '<string>'.
            thumbnailLink (string): thumbnailLink Example: '<string>'.
            thumbnailVersion (string): thumbnailVersion Example: '<int64>'.
            trashed (string): trashed Example: '<boolean>'.
            trashedTime (string): trashedTime Example: '<dateTime>'.
            trashingUser (object): trashingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            version (string): version Example: '<int64>'.
            videoMediaMetadata (object): videoMediaMetadata Example: {'durationMillis': '<int64>', 'height': '<integer>', 'width': '<integer>'}.
            viewedByMe (string): viewedByMe Example: '<boolean>'.
            viewedByMeTime (string): viewedByMeTime Example: '<dateTime>'.
            viewersCanCopyContent (string): viewersCanCopyContent Example: '<boolean>'.
            webContentLink (string): webContentLink Example: '<string>'.
            webViewLink (string): webViewLink Example: '<string>'.
            writersCanShare (string): writersCanShare Example: '<boolean>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        request_body_data = None
        request_body_data = {
            "appProperties": appProperties,
            "capabilities": capabilities,
            "contentHints": contentHints,
            "contentRestrictions": contentRestrictions,
            "copyRequiresWriterPermission": copyRequiresWriterPermission,
            "createdTime": createdTime,
            "description": description,
            "driveId": driveId,
            "explicitlyTrashed": explicitlyTrashed,
            "exportLinks": exportLinks,
            "fileExtension": fileExtension,
            "folderColorRgb": folderColorRgb,
            "fullFileExtension": fullFileExtension,
            "hasAugmentedPermissions": hasAugmentedPermissions,
            "hasThumbnail": hasThumbnail,
            "headRevisionId": headRevisionId,
            "iconLink": iconLink,
            "id": id,
            "imageMediaMetadata": imageMediaMetadata,
            "isAppAuthorized": isAppAuthorized,
            "kind": kind,
            "labelInfo": labelInfo,
            "lastModifyingUser": lastModifyingUser,
            "linkShareMetadata": linkShareMetadata,
            "md5Checksum": md5Checksum,
            "mimeType": mimeType,
            "modifiedByMe": modifiedByMe,
            "modifiedByMeTime": modifiedByMeTime,
            "modifiedTime": modifiedTime,
            "name": name,
            "originalFilename": originalFilename,
            "ownedByMe": ownedByMe,
            "owners": owners,
            "parents": parents,
            "permissionIds": permissionIds,
            "permissions": permissions,
            "properties": properties,
            "quotaBytesUsed": quotaBytesUsed,
            "resourceKey": resourceKey,
            "sha1Checksum": sha1Checksum,
            "sha256Checksum": sha256Checksum,
            "shared": shared,
            "sharedWithMeTime": sharedWithMeTime,
            "sharingUser": sharingUser,
            "shortcutDetails": shortcutDetails,
            "size": size,
            "spaces": spaces,
            "starred": starred,
            "teamDriveId": teamDriveId,
            "thumbnailLink": thumbnailLink,
            "thumbnailVersion": thumbnailVersion,
            "trashed": trashed,
            "trashedTime": trashedTime,
            "trashingUser": trashingUser,
            "version": version,
            "videoMediaMetadata": videoMediaMetadata,
            "viewedByMe": viewedByMe,
            "viewedByMeTime": viewedByMeTime,
            "viewersCanCopyContent": viewersCanCopyContent,
            "webContentLink": webContentLink,
            "webViewLink": webViewLink,
            "writersCanShare": writersCanShare,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/copy"
        query_params = {
            k: v
            for k, v in [
                ("enforceSingleParent", enforceSingleParent),
                ("ignoreDefaultVisibility", ignoreDefaultVisibility),
                ("includeLabels", includeLabels),
                ("includePermissionsForView", includePermissionsForView),
                ("keepRevisionForever", keepRevisionForever),
                ("ocrLanguage", ocrLanguage),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def export_agoogle_workspace_document(
        self,
        fileId: str,
        mimeType: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> Any:
        """
        Export a Google Workspace document

        Args:
            fileId (string): fileId
            mimeType (string): (Required) The MIME type of the format requested for this export. Example: 'mimeType'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        url = f"{self.base_url}/files/{fileId}/export"
        query_params = {
            k: v
            for k, v in [
                ("mimeType", mimeType),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def list_the_labels_on_afile(
        self,
        fileId: str,
        maxResults: str | None = None,
        pageToken: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        List the labels on a file

        Args:
            fileId (string): fileId
            maxResults (string): The maximum number of labels to return per page. When not set, this defaults to 100. Example: '<integer>'.
            pageToken (string): The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response. Example: '{{pageToken}}'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        url = f"{self.base_url}/files/{fileId}/listLabels"
        query_params = {
            k: v
            for k, v in [
                ("maxResults", maxResults),
                ("pageToken", pageToken),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def modify_labels_applied_to_afile(
        self,
        fileId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        kind: str | None = None,
        labelModifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Modify labels applied to a file

        Args:
            fileId (string): fileId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            kind (string): kind Example: 'drive#modifyLabelsRequest'.
            labelModifications (array): labelModifications Example: "[{'fieldModifications': [{'fieldId': '<string>', 'kind': 'drive#labelFieldModification', 'setDateValues': ['<date>', '<date>'], 'setIntegerValues': ['<int64>', '<int64>'], 'setSelectionValues': ['<string>', '<string>'], 'setTextValues': ['<string>', '<string>'], 'setUserValues': ['<string>', '<string>'], 'unsetValues': '<boolean>'}, {'fieldId': '<string>', 'kind': 'drive#labelFieldModification', 'setDateValues': ['<date>', '<date>'], 'setIntegerValues': ['<int64>', '<int64>'], 'setSelectionValues': ['<string>', '<string>'], 'setTextValues': ['<string>', '<string>'], 'setUserValues': ['<string>', '<string>'], 'unsetValues': '<boolean>'}], 'kind': 'drive#labelModification', 'labelId': '<string>', 'removeLabel': '<boolean>'}, {'fieldModifications': [{'fieldId': '<string>', 'kind': 'drive#labelFieldModification', 'setDateValues': ['<date>', '<date>'], 'setIntegerValues': ['<int64>', '<int64>'], 'setSelectionValues': ['<string>', '<string>'], 'setTextValues': ['<string>', '<string>'], 'setUserValues': ['<string>', '<string>'], 'unsetValues': '<boolean>'}, {'fieldId': '<string>', 'kind': 'drive#labelFieldModification', 'setDateValues': ['<date>', '<date>'], 'setIntegerValues': ['<int64>', '<int64>'], 'setSelectionValues': ['<string>', '<string>'], 'setTextValues': ['<string>', '<string>'], 'setUserValues': ['<string>', '<string>'], 'unsetValues': '<boolean>'}], 'kind': 'drive#labelModification', 'labelId': '<string>', 'removeLabel': '<boolean>'}]".

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        request_body_data = None
        request_body_data = {
            "kind": kind,
            "labelModifications": labelModifications,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/modifyLabels"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def subscribe_to_changes_to_afile(
        self,
        fileId: str,
        acknowledgeAbuse: str | None = None,
        includeLabels: str | None = None,
        includePermissionsForView: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        address: str | None = None,
        expiration: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        params: dict[str, Any] | None = None,
        payload: str | None = None,
        resourceId: str | None = None,
        resourceUri: str | None = None,
        token: str | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        """
        Subscribe to changes to a file

        Args:
            fileId (string): fileId
            acknowledgeAbuse (string): Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media. Example: '<boolean>'.
            includeLabels (string): A comma-separated list of IDs of labels to include in the labelInfo part of the response. Example: '<string>'.
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            address (string): address Example: '<string>'.
            expiration (string): expiration Example: '<int64>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'api#channel'.
            params (object): params Example: {'adipisicing1': '<string>', 'eu2': '<string>', 'qui_9': '<string>'}.
            payload (string): payload Example: '<boolean>'.
            resourceId (string): resourceId Example: '<string>'.
            resourceUri (string): resourceUri Example: '<string>'.
            token (string): token Example: '<string>'.
            type (string): type Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Files
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        request_body_data = None
        request_body_data = {
            "address": address,
            "expiration": expiration,
            "id": id,
            "kind": kind,
            "params": params,
            "payload": payload,
            "resourceId": resourceId,
            "resourceUri": resourceUri,
            "token": token,
            "type": type,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/watch"
        query_params = {
            k: v
            for k, v in [
                ("acknowledgeAbuse", acknowledgeAbuse),
                ("includeLabels", includeLabels),
                ("includePermissionsForView", includePermissionsForView),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def list_file_permissions(
        self,
        fileId: str,
        includePermissionsForView: str | None = None,
        pageSize: str | None = None,
        pageToken: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        List a file's or shared drive's permissions

        Args:
            fileId (string): fileId
            includePermissionsForView (string): Specifies which additional view's permissions to include in the response. Only 'published' is supported. Example: '<string>'.
            pageSize (string): The maximum number of permissions to return per page. When not set for files in a shared drive, at most 100 results will be returned. When not set for files that are not in a shared drive, the entire list will be returned. Example: '<integer>'.
            pageToken (string): The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response. Example: '{{pageToken}}'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            useDomainAdminAccess (string): Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Permissions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        url = f"{self.base_url}/files/{fileId}/permissions"
        query_params = {
            k: v
            for k, v in [
                ("includePermissionsForView", includePermissionsForView),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def post_file_permission(
        self,
        fileId: str,
        emailMessage: str | None = None,
        enforceSingleParent: str | None = None,
        moveToNewOwnersRoot: str | None = None,
        sendNotificationEmail: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        transferOwnership: str | None = None,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        allowFileDiscovery: str | None = None,
        deleted: str | None = None,
        displayName: str | None = None,
        domain: str | None = None,
        emailAddress: str | None = None,
        expirationTime: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        pendingOwner: str | None = None,
        permissionDetails: list[dict[str, Any]] | None = None,
        photoLink: str | None = None,
        role: str | None = None,
        teamDrivePermissionDetails: list[dict[str, Any]] | None = None,
        type: str | None = None,
        view: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a permission for a file or shared drive

        Args:
            fileId (string): fileId
            emailMessage (string): A plain text custom message to include in the notification email. Example: '<string>'.
            enforceSingleParent (string): Deprecated. See moveToNewOwnersRoot for details. Example: '<boolean>'.
            moveToNewOwnersRoot (string): This parameter will only take effect if the item is not in a shared drive and the request is attempting to transfer the ownership of the item. If set to true, the item will be moved to the new owner's My Drive root folder and all prior parents removed. If set to false, parents are not changed. Example: '<boolean>'.
            sendNotificationEmail (string): Whether to send a notification email when sharing to users or groups. This defaults to true for users and groups, and is not allowed for other requests. It must not be disabled for ownership transfers. Example: '<boolean>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            transferOwnership (string): Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect. File owners can only transfer ownership of files existing on My Drive. Files existing in a shared drive are owned by the organization that owns that shared drive. Ownership transfers are not supported for files and folders in shared drives. Organizers of a shared drive can move items from that shared drive into their My Drive which transfers the ownership to them. Example: '<boolean>'.
            useDomainAdminAccess (string): Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            allowFileDiscovery (string): allowFileDiscovery Example: '<boolean>'.
            deleted (string): deleted Example: '<boolean>'.
            displayName (string): displayName Example: '<string>'.
            domain (string): domain Example: '<string>'.
            emailAddress (string): emailAddress Example: '<string>'.
            expirationTime (string): expirationTime Example: '<dateTime>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'drive#permission'.
            pendingOwner (string): pendingOwner Example: '<boolean>'.
            permissionDetails (array): permissionDetails Example: "[{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}]".
            photoLink (string): photoLink Example: '<string>'.
            role (string): role Example: '<string>'.
            teamDrivePermissionDetails (array): teamDrivePermissionDetails Example: "[{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}]".
            type (string): type Example: '<string>'.
            view (string): view Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Permissions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        request_body_data = None
        request_body_data = {
            "allowFileDiscovery": allowFileDiscovery,
            "deleted": deleted,
            "displayName": displayName,
            "domain": domain,
            "emailAddress": emailAddress,
            "expirationTime": expirationTime,
            "id": id,
            "kind": kind,
            "pendingOwner": pendingOwner,
            "permissionDetails": permissionDetails,
            "photoLink": photoLink,
            "role": role,
            "teamDrivePermissionDetails": teamDrivePermissionDetails,
            "type": type,
            "view": view,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/permissions"
        query_params = {
            k: v
            for k, v in [
                ("emailMessage", emailMessage),
                ("enforceSingleParent", enforceSingleParent),
                ("moveToNewOwnersRoot", moveToNewOwnersRoot),
                ("sendNotificationEmail", sendNotificationEmail),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("transferOwnership", transferOwnership),
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def get_permission_by_id(
        self,
        fileId: str,
        permissionId: str,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Get permission by ID

        Args:
            fileId (string): fileId
            permissionId (string): permissionId
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            useDomainAdminAccess (string): Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Permissions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if permissionId is None:
            raise ValueError("Missing required parameter 'permissionId'.")
        url = f"{self.base_url}/files/{fileId}/permissions/{permissionId}"
        query_params = {
            k: v
            for k, v in [
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def delete_apermission(
        self,
        fileId: str,
        permissionId: str,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> Any:
        """
        Delete a permission

        Args:
            fileId (string): fileId
            permissionId (string): permissionId
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            useDomainAdminAccess (string): Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Permissions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if permissionId is None:
            raise ValueError("Missing required parameter 'permissionId'.")
        url = f"{self.base_url}/files/{fileId}/permissions/{permissionId}"
        query_params = {
            k: v
            for k, v in [
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def update_apermission(
        self,
        fileId: str,
        permissionId: str,
        removeExpiration: str | None = None,
        supportsAllDrives: str | None = None,
        supportsTeamDrives: str | None = None,
        transferOwnership: str | None = None,
        useDomainAdminAccess: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        allowFileDiscovery: str | None = None,
        deleted: str | None = None,
        displayName: str | None = None,
        domain: str | None = None,
        emailAddress: str | None = None,
        expirationTime: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        pendingOwner: str | None = None,
        permissionDetails: list[dict[str, Any]] | None = None,
        photoLink: str | None = None,
        role: str | None = None,
        teamDrivePermissionDetails: list[dict[str, Any]] | None = None,
        type: str | None = None,
        view: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a permission

        Args:
            fileId (string): fileId
            permissionId (string): permissionId
            removeExpiration (string): Whether to remove the expiration date. Example: '<boolean>'.
            supportsAllDrives (string): Whether the requesting application supports both My Drives and shared drives. Example: '<boolean>'.
            supportsTeamDrives (string): Deprecated use supportsAllDrives instead. Example: '<boolean>'.
            transferOwnership (string): Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect. File owners can only transfer ownership of files existing on My Drive. Files existing in a shared drive are owned by the organization that owns that shared drive. Ownership transfers are not supported for files and folders in shared drives. Organizers of a shared drive can move items from that shared drive into their My Drive which transfers the ownership to them. Example: '<boolean>'.
            useDomainAdminAccess (string): Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            allowFileDiscovery (string): allowFileDiscovery Example: '<boolean>'.
            deleted (string): deleted Example: '<boolean>'.
            displayName (string): displayName Example: '<string>'.
            domain (string): domain Example: '<string>'.
            emailAddress (string): emailAddress Example: '<string>'.
            expirationTime (string): expirationTime Example: '<dateTime>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'drive#permission'.
            pendingOwner (string): pendingOwner Example: '<boolean>'.
            permissionDetails (array): permissionDetails Example: "[{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'permissionType': '<string>', 'role': '<string>'}]".
            photoLink (string): photoLink Example: '<string>'.
            role (string): role Example: '<string>'.
            teamDrivePermissionDetails (array): teamDrivePermissionDetails Example: "[{'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}, {'inherited': '<boolean>', 'inheritedFrom': '<string>', 'role': '<string>', 'teamDrivePermissionType': '<string>'}]".
            type (string): type Example: '<string>'.
            view (string): view Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Permissions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if permissionId is None:
            raise ValueError("Missing required parameter 'permissionId'.")
        request_body_data = None
        request_body_data = {
            "allowFileDiscovery": allowFileDiscovery,
            "deleted": deleted,
            "displayName": displayName,
            "domain": domain,
            "emailAddress": emailAddress,
            "expirationTime": expirationTime,
            "id": id,
            "kind": kind,
            "pendingOwner": pendingOwner,
            "permissionDetails": permissionDetails,
            "photoLink": photoLink,
            "role": role,
            "teamDrivePermissionDetails": teamDrivePermissionDetails,
            "type": type,
            "view": view,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/permissions/{permissionId}"
        query_params = {
            k: v
            for k, v in [
                ("removeExpiration", removeExpiration),
                ("supportsAllDrives", supportsAllDrives),
                ("supportsTeamDrives", supportsTeamDrives),
                ("transferOwnership", transferOwnership),
                ("useDomainAdminAccess", useDomainAdminAccess),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
        }
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_acomment_sreplies(
        self,
        fileId: str,
        commentId: str,
        includeDeleted: str | None = None,
        pageSize: str | None = None,
        pageToken: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        List a comment's replies

        Args:
            fileId (string): fileId
            commentId (string): commentId
            includeDeleted (string): Whether to include deleted replies. Deleted replies will not include their original content. Example: '<boolean>'.
            pageSize (string): The maximum number of replies to return per page. Example: '<integer>'.
            pageToken (string): The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response. Example: '{{pageToken}}'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Replies
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'.")
        url = f"{self.base_url}/files/{fileId}/comments/{commentId}/replies"
        query_params = {
            k: v
            for k, v in [
                ("includeDeleted", includeDeleted),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def create_areply_to_acomment(
        self,
        fileId: str,
        commentId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        action: str | None = None,
        author: dict[str, Any] | None = None,
        content: str | None = None,
        createdTime: str | None = None,
        deleted: str | None = None,
        htmlContent: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        modifiedTime: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a reply to a comment

        Args:
            fileId (string): fileId
            commentId (string): commentId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            action (string): action Example: '<string>'.
            author (object): author Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            content (string): content Example: '<string>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            deleted (string): deleted Example: '<boolean>'.
            htmlContent (string): htmlContent Example: '<string>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'drive#reply'.
            modifiedTime (string): modifiedTime Example: '<dateTime>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Replies
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'.")
        request_body_data = None
        request_body_data = {
            "action": action,
            "author": author,
            "content": content,
            "createdTime": createdTime,
            "deleted": deleted,
            "htmlContent": htmlContent,
            "id": id,
            "kind": kind,
            "modifiedTime": modifiedTime,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/comments/{commentId}/replies"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def get_reply_by_id(
        self,
        fileId: str,
        commentId: str,
        replyId: str,
        includeDeleted: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Get reply by ID

        Args:
            fileId (string): fileId
            commentId (string): commentId
            replyId (string): replyId
            includeDeleted (string): Whether to return deleted replies. Deleted replies will not include their original content. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Replies
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'.")
        if replyId is None:
            raise ValueError("Missing required parameter 'replyId'.")
        url = f"{self.base_url}/files/{fileId}/comments/{commentId}/replies/{replyId}"
        query_params = {
            k: v
            for k, v in [
                ("includeDeleted", includeDeleted),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def delete_areply(
        self,
        fileId: str,
        commentId: str,
        replyId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> Any:
        """
        Delete a reply

        Args:
            fileId (string): fileId
            commentId (string): commentId
            replyId (string): replyId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Replies
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'.")
        if replyId is None:
            raise ValueError("Missing required parameter 'replyId'.")
        url = f"{self.base_url}/files/{fileId}/comments/{commentId}/replies/{replyId}"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def update_areply(
        self,
        fileId: str,
        commentId: str,
        replyId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        action: str | None = None,
        author: dict[str, Any] | None = None,
        content: str | None = None,
        createdTime: str | None = None,
        deleted: str | None = None,
        htmlContent: str | None = None,
        id: str | None = None,
        kind: str | None = None,
        modifiedTime: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a reply

        Args:
            fileId (string): fileId
            commentId (string): commentId
            replyId (string): replyId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            action (string): action Example: '<string>'.
            author (object): author Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            content (string): content Example: '<string>'.
            createdTime (string): createdTime Example: '<dateTime>'.
            deleted (string): deleted Example: '<boolean>'.
            htmlContent (string): htmlContent Example: '<string>'.
            id (string): id Example: '<string>'.
            kind (string): kind Example: 'drive#reply'.
            modifiedTime (string): modifiedTime Example: '<dateTime>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Replies
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'.")
        if replyId is None:
            raise ValueError("Missing required parameter 'replyId'.")
        request_body_data = None
        request_body_data = {
            "action": action,
            "author": author,
            "content": content,
            "createdTime": createdTime,
            "deleted": deleted,
            "htmlContent": htmlContent,
            "id": id,
            "kind": kind,
            "modifiedTime": modifiedTime,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/comments/{commentId}/replies/{replyId}"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
        }
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_afile_srevisions(
        self,
        fileId: str,
        pageSize: str | None = None,
        pageToken: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        List a file's revisions

        Args:
            fileId (string): fileId
            pageSize (string): The maximum number of revisions to return per page. Example: '<integer>'.
            pageToken (string): The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response. Example: '{{pageToken}}'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Revisions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        url = f"{self.base_url}/files/{fileId}/revisions"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def get_aspecific_revision(
        self,
        fileId: str,
        revisionId: str,
        acknowledgeAbuse: str | None = None,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> dict[str, Any]:
        """
        Get a specific revision

        Args:
            fileId (string): fileId
            revisionId (string): revisionId
            acknowledgeAbuse (string): Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media. Example: '<boolean>'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Revisions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        url = f"{self.base_url}/files/{fileId}/revisions/{revisionId}"
        query_params = {
            k: v
            for k, v in [
                ("acknowledgeAbuse", acknowledgeAbuse),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
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

    def permanently_delete_afile_version(
        self,
        fileId: str,
        revisionId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
    ) -> Any:
        """
        Permanently delete a file version

        Args:
            fileId (string): fileId
            revisionId (string): revisionId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.

        Returns:
            Any: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Revisions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        url = f"{self.base_url}/files/{fileId}/revisions/{revisionId}"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
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

    def update_arevision(
        self,
        fileId: str,
        revisionId: str,
        alt: str | None = None,
        fields: str | None = None,
        key: str | None = None,
        oauth_token: str | None = None,
        prettyPrint: str | None = None,
        quotaUser: str | None = None,
        userIp: str | None = None,
        exportLinks: dict[str, Any] | None = None,
        id: str | None = None,
        keepForever: str | None = None,
        kind: str | None = None,
        lastModifyingUser: dict[str, Any] | None = None,
        md5Checksum: str | None = None,
        mimeType: str | None = None,
        modifiedTime: str | None = None,
        originalFilename: str | None = None,
        publishAuto: str | None = None,
        published: str | None = None,
        publishedLink: str | None = None,
        publishedOutsideDomain: str | None = None,
        size: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a revision

        Args:
            fileId (string): fileId
            revisionId (string): revisionId
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: '<string>'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: '{{key}}'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: '{{oauthToken}}'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: '<boolean>'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: '<string>'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: '<string>'.
            exportLinks (object): exportLinks Example: {'in3': '<string>', 'quis_d': '<string>'}.
            id (string): id Example: '<string>'.
            keepForever (string): keepForever Example: '<boolean>'.
            kind (string): kind Example: 'drive#revision'.
            lastModifyingUser (object): lastModifyingUser Example: {'displayName': '<string>', 'emailAddress': '<string>', 'kind': 'drive#user', 'me': '<boolean>', 'permissionId': '<string>', 'photoLink': '<string>'}.
            md5Checksum (string): md5Checksum Example: '<string>'.
            mimeType (string): mimeType Example: '<string>'.
            modifiedTime (string): modifiedTime Example: '<dateTime>'.
            originalFilename (string): originalFilename Example: '<string>'.
            publishAuto (string): publishAuto Example: '<boolean>'.
            published (string): published Example: '<boolean>'.
            publishedLink (string): publishedLink Example: '<string>'.
            publishedOutsideDomain (string): publishedOutsideDomain Example: '<boolean>'.
            size (string): size Example: '<int64>'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Revisions
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        request_body_data = None
        request_body_data = {
            "exportLinks": exportLinks,
            "id": id,
            "keepForever": keepForever,
            "kind": kind,
            "lastModifyingUser": lastModifyingUser,
            "md5Checksum": md5Checksum,
            "mimeType": mimeType,
            "modifiedTime": modifiedTime,
            "originalFilename": originalFilename,
            "publishAuto": publishAuto,
            "published": published,
            "publishedLink": publishedLink,
            "publishedOutsideDomain": publishedOutsideDomain,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/files/{fileId}/revisions/{revisionId}"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
        }
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    

    def grant_google_drive_access(
        self,
        fileId: str,
        emailAddress: str | None = None,
        role: str | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        """
        Grant Google Drive Access

        Args:
            fileId (string): fileId
            emailAddress (string): emailAddress Example: '{{currentEmailId}}'.
            role (string): role Example: 'reader'.
            type (string): type Example: 'user'.

        Returns:
            dict[str, Any]: Grant Google Drive Access

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Google Drive API Use Cases, Share file access to a slack channel
        """
        if fileId is None:
            raise ValueError("Missing required parameter 'fileId'.")
        request_body_data = None
        request_body_data = {
            "emailAddress": emailAddress,
            "role": role,
            "type": type,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/drive/v3/files/{fileId}/permissions"
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

    def list_tools(self):
        return [
            self.get_drive_info,
            self.list_files,
            self.create_file_from_text,
            self.upload_a_file,
            self.find_folder_id_by_name,
            self.create_folder,
            self.get_file,
            self.delete_file,
            # Auto generated from openapi spec
            self.list_user_sinstalled_apps,
            self.get_aspecific_app,
            self.information_about_user_and_drive,
            self.list_changes_made_to_afile_or_drive,
            self.get_start_page_token,
            self.subscribe_to_changes_for_auser,
            self.post_stop_channel,
            self.lists_afile_scomments,
            self.create_acomment_on_afile,
            self.get_comment_by_id,
            self.delete_acomment,
            self.update_comment,
            self.list_user_sshared_drive,
            self.create_ashared_drive,
            self.get_ashared_drive_smetadata_by_id,
            self.permanently_delete_ashared_drive,
            self.update_metadata_for_ashared_drive,
            self.hide_drive_by_id_post,
            self.unhide_drive,
            self.list_user_sfiles,
            self.create_anew_file,
            self.generate_aset_of_file_ids,
            self.empty_trash_files,
            self.get_file_metadata,
            self.delete_file_by_id,
            self.update_file,
            self.copy_file_by_id,
            self.export_agoogle_workspace_document,
            self.list_the_labels_on_afile,
            self.modify_labels_applied_to_afile,
            self.subscribe_to_changes_to_afile,
            self.list_file_permissions,
            self.post_file_permission,
            self.get_permission_by_id,
            self.delete_apermission,
            self.update_apermission,
            self.list_acomment_sreplies,
            self.create_areply_to_acomment,
            self.get_reply_by_id,
            self.delete_areply,
            self.update_areply,
            self.list_afile_srevisions,
            self.get_aspecific_revision,
            self.permanently_delete_afile_version,
            self.update_arevision,
            self.grant_google_drive_access,
            self.move_files,
        ]
