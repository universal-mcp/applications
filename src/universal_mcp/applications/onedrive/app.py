from typing import Any
import os

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class OneDriveApp(APIApplication):
    """
    Application for interacting with Microsoft OneDrive API (via Microsoft Graph).
    Provides tools to manage files, folders, and access Drive information.
    """

    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="onedrive", integration=integration, **kwargs)
        self.base_url = "https://graph.microsoft.com/v1.0"

    def _handle_response(self, response: Any) -> dict[str, Any]:
        """Handles the HTTP response, raising an error for non-successful status codes."""
        response.raise_for_status()
        if response.status_code == 204:  # No Content
            return {}
        try:
            return response.json()
        except ValueError:
            return {} # Return empty dict if response is not JSON

    def get_my_profile(self) -> dict[str, Any]:
        """
        Fetches the profile for the currently authenticated user.

        Returns:
            dict[str, Any]: A dictionary containing the user's id and userPrincipalName.

        Raises:
            HTTPStatusError: If the API request fails.
        """
        url = f"{self.base_url}/me"
        query_params = {"$select": "id,userPrincipalName"}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_drive_info(self, user_id: str | None = None) -> dict[str, Any]:
        """
        Retrieves information about a user's OneDrive, including owner and quota.

        Args:
            user_id (str, optional): The ID or userPrincipalName of the user. Defaults to the authenticated user.

        Returns:
            A dictionary containing drive information.
        """
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("id")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        url = f"{self.base_url}/users/{user_id}/drive"
        response = self._get(url)
        return self._handle_response(response)

    def list_drive_items(self, user_id: str | None = None, item_id: str = "root") -> dict[str, Any]:
        """
        Lists the files and folders in a user's OneDrive.

        Args:
            user_id (str, optional): The ID or userPrincipalName of the user. Defaults to the authenticated user.
            item_id (str, optional): The ID of the folder to list. Defaults to 'root'.

        Returns:
            A dictionary containing the list of files and folders.
        """
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("id")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        url = f"{self.base_url}/users/{user_id}/drive/items/{item_id}/children"
        response = self._get(url)
        return self._handle_response(response)

    def search_files(self, query: str, user_id: str | None = None) -> dict[str, Any]:
        """
        Searches for files and folders in a user's OneDrive.

        Args:
            query (str): The search query.
            user_id (str, optional): The ID or userPrincipalName of the user. Defaults to the authenticated user.

        Returns:
            A dictionary containing the search results.
        """
        if not query:
            raise ValueError("Search query cannot be empty.")
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("id")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        url = f"{self.base_url}/users/{user_id}/drive/root/search(q='{query}')"
        response = self._get(url)
        return self._handle_response(response)

    def get_item_metadata(self, item_id: str, user_id: str | None = None) -> dict[str, Any]:
        """
        Retrieves the metadata for a file or folder.

        Args:
            item_id (str): The ID of the file or folder.
            user_id (str, optional): The ID or userPrincipalName of the user. Defaults to the authenticated user.

        Returns:
            A dictionary containing the item's metadata.
        """
        if not item_id:
            raise ValueError("Missing required parameter 'item_id'.")
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("id")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        url = f"{self.base_url}/users/{user_id}/drive/items/{item_id}"
        response = self._get(url)
        return self._handle_response(response)

    def create_folder(self, name: str, parent_id: str = "root", user_id: str | None = None) -> dict[str, Any]:
        """
        Creates a new folder.

        Args:
            name (str): The name of the new folder.
            parent_id (str, optional): The ID of the parent folder. Defaults to 'root'.
            user_id (str, optional): The ID or userPrincipalName of the user. Defaults to the authenticated user.

        Returns:
            A dictionary containing the new folder's metadata.
        """
        if not name:
            raise ValueError("Folder name cannot be empty.")
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("id")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        url = f"{self.base_url}/users/{user_id}/drive/items/{parent_id}/children"
        data = {
            "name": name,
            "folder": {},
            "@microsoft.graph.conflictBehavior": "rename"
        }
        response = self._post(url, data=data)
        return self._handle_response(response)

    def delete_item(self, item_id: str, user_id: str | None = None) -> dict[str, Any]:
        """
        Deletes a file or folder.

        Args:
            item_id (str): The ID of the item to delete.
            user_id (str, optional): The ID or userPrincipalName of the user. Defaults to the authenticated user.

        Returns:
            An empty dictionary if successful.
        """
        if not item_id:
            raise ValueError("Missing required parameter 'item_id'.")
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("id")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        url = f"{self.base_url}/users/{user_id}/drive/items/{item_id}"
        response = self._delete(url)
        return self._handle_response(response)

    def download_file(self, item_id: str, user_id: str | None = None) -> dict[str, Any]:
        """
        Gets the download URL for a file.

        Args:
            item_id (str): The ID of the file to download.
            user_id (str, optional): The ID or userPrincipalName of the user. Defaults to the authenticated user.

        Returns:
            A dictionary containing the download URL for the file under the key '@microsoft.graph.downloadUrl'.
        """
        if not item_id:
            raise ValueError("Missing required parameter 'item_id'.")
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("id")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        url = f"{self.base_url}/users/{user_id}/drive/items/{item_id}"
        response = self._get(url)
        metadata = self._handle_response(response)
        download_url = metadata.get("@microsoft.graph.downloadUrl")
        if not download_url:
            raise ValueError("Could not retrieve download URL for the item.")
        return {"download_url": download_url}


    def upload_file(
        self, file_path: str, parent_id: str = "root", file_name: str | None = None, user_id: str | None = None
    ) -> dict[str, Any]:
        """
        Uploads a file to OneDrive (for files smaller than 4MB).

        Args:
            file_path (str): The local path to the file to upload.
            parent_id (str, optional): The ID of the folder to upload the file to. Defaults to 'root'.
            file_name (str, optional): The name to give the uploaded file. If not provided, the local filename is used.
            user_id (str, optional): The ID or userPrincipalName of the user. Defaults to the authenticated user.

        Returns:
            A dictionary containing the uploaded file's metadata.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file was not found at path: {file_path}")

        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("id")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        if not file_name:
            file_name = os.path.basename(file_path)

        url = f"{self.base_url}/users/{user_id}/drive/items/{parent_id}:/{file_name}:/content"
        with open(file_path, "rb") as f:
            data = f.read()
        response = self._put(url, data=data, content_type="application/octet-stream")
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.get_drive_info,
            self.list_drive_items,
            self.search_files,
            self.get_item_metadata,
            self.create_folder,
            self.delete_item,
            self.download_file,
            self.upload_file,
            self.get_my_profile,
        ]
