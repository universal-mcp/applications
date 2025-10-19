import base64
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

    def get_my_profile(self) -> dict[str, Any]:
        """
        Fetches the profile for the currently authenticated user.

        Returns:
            dict[str, Any]: A dictionary containing the user's id and userPrincipalName.

        Raises:
            HTTPStatusError: If the API request fails.
        
        Tags:
            profile, user, account
        """
        url = f"{self.base_url}/me"
        query_params = {"$select": "id,userPrincipalName"}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_drive_info(self) -> dict[str, Any]:
        """
        Retrieves information about the current user's OneDrive, including owner and quota.

        Returns:
            A dictionary containing drive information.
            
        Tags:
            drive, storage, quota, info
        """
        url = f"{self.base_url}/me/drive"
        response = self._get(url)
        return self._handle_response(response)

    def _list_drive_items(self, item_id: str = "root") -> dict[str, Any]:
        """
        Lists the files and folders in the current user's OneDrive.

        Args:
            item_id (str, optional): The ID of the folder to list. Defaults to 'root'.

        Returns:
            A dictionary containing the list of files and folders.
        """
        url = f"{self.base_url}/me/drive/items/{item_id}/children"
        response = self._get(url)
        return self._handle_response(response)

    def search_files(self, query: str) -> dict[str, Any]:
        """
        Searches for files and folders in the current user's OneDrive.

        Args:
            query (str): The search query.

        Returns:
            A dictionary containing the search results.
            
        Tags:
            search, find, query, files, important
        """
        if not query:
            raise ValueError("Search query cannot be empty.")

        url = f"{self.base_url}/me/drive/root/search(q='{query}')"
        response = self._get(url)
        return self._handle_response(response)

    def get_item_metadata(self, item_id: str) -> dict[str, Any]:
        """
        Retrieves the metadata for a file or folder.

        Args:
            item_id (str): The ID of the file or folder.

        Returns:
            A dictionary containing the item's metadata.
            
        Tags:
            metadata, info, file, folder
        """
        if not item_id:
            raise ValueError("Missing required parameter 'item_id'.")

        url = f"{self.base_url}/me/drive/items/{item_id}"
        response = self._get(url)
        return self._handle_response(response)

    def create_folder(self, name: str, parent_id: str = "root") -> dict[str, Any]:
        """
        Creates a new folder.

        Args:
            name (str): The name of the new folder.
            parent_id (str, optional): The ID of the parent folder. Defaults to 'root'.

        Returns:
            A dictionary containing the new folder's metadata.
            
        Tags:
            create, folder, directory, important
        """
        if not name:
            raise ValueError("Folder name cannot be empty.")

        url = f"{self.base_url}/me/drive/items/{parent_id}/children"
        data = {
            "name": name,
            "folder": {},
            "@microsoft.graph.conflictBehavior": "rename"
        }
        response = self._post(url, data=data)
        return self._handle_response(response)

    def delete_item(self, item_id: str) -> dict[str, Any]:
        """
        Deletes a file or folder.

        Args:
            item_id (str): The ID of the item to delete.

        Returns:
            An empty dictionary if successful.
            
        Tags:
            delete, remove, file, folder, important
        """
        if not item_id:
            raise ValueError("Missing required parameter 'item_id'.")

        url = f"{self.base_url}/me/drive/items/{item_id}"
        response = self._delete(url)
        return self._handle_response(response)

    def download_file(self, item_id: str) -> dict[str, Any]:
        """
        Gets the download URL for a file.

        Args:
            item_id (str): The ID of the file to download.

        Returns:
            A dictionary containing the download URL for the file under the key '@microsoft.graph.downloadUrl'.
            
        Tags:
            download, file, get, important
        """
        if not item_id:
            raise ValueError("Missing required parameter 'item_id'.")

        url = f"{self.base_url}/me/drive/items/{item_id}"
        response = self._get(url)
        metadata = self._handle_response(response)
        download_url = metadata.get("@microsoft.graph.downloadUrl")
        if not download_url:
            raise ValueError("Could not retrieve download URL for the item.")
        return {"download_url": download_url}


    def upload_file(
        self, file_path: str, parent_id: str = "root", file_name: str | None = None
    ) -> dict[str, Any]:
        """
        Uploads a file to OneDrive (for files smaller than 4MB).

        Args:
            file_path (str): The local path to the file to upload.
            parent_id (str, optional): The ID of the folder to upload the file to. Defaults to 'root'.
            file_name (str, optional): The name to give the uploaded file. If not provided, the local filename is used.

        Returns:
            A dictionary containing the uploaded file's metadata.
            
        Tags:
            upload, file, put, important
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file was not found at path: {file_path}")

        if not file_name:
            file_name = os.path.basename(file_path)

        url = f"{self.base_url}/me/drive/items/{parent_id}:/{file_name}:/content"
        with open(file_path, "rb") as f:
            data = f.read()
        response = self._put(url, data=data, content_type="application/octet-stream")
        return self._handle_response(response)

    def list_folders(self, item_id: str = "root") -> dict[str, Any]:
        """
        Lists the folders in the current user's OneDrive.

        Args:
            item_id (str, optional): The ID of the folder to list from. Defaults to 'root'.

        Returns:
            A dictionary containing the list of folders.
            
        Tags:
            list, folders, directories, important
        """
        all_items = self._list_drive_items(item_id=item_id)
        folders = [item for item in all_items.get("value", []) if "folder" in item]
        return {"value": folders}

    def list_files(self, item_id: str = "root") -> dict[str, Any]:
        """
        Lists the files in the current user's OneDrive.

        Args:
            item_id (str, optional): The ID of the folder to list files from. Defaults to 'root'.

        Returns:
            A dictionary containing the list of files.
            
        Tags:
            list, files, documents, important
        """
        all_items = self._list_drive_items(item_id=item_id)
        files = [item for item in all_items.get("value", []) if "file" in item]
        return {"value": files}

    def create_folder_and_list(self, name: str, parent_id: str = "root") -> dict[str, Any]:
        """
        Creates a new folder and then lists all items in the parent folder.

        Args:
            name (str): The name of the new folder.
            parent_id (str, optional): The ID of the parent folder. Defaults to 'root'.

        Returns:
            A dictionary containing the list of items in the parent folder after creation.
            
        Tags:
            create, folder, list, important
        """
        self.create_folder(name=name, parent_id=parent_id)
        return self._list_drive_items(item_id=parent_id)

    def upload_text_file(
        self, content: str, parent_id: str = "root", file_name: str = "new_file.txt"
    ) -> dict[str, Any]:
        """
        Uploads text content as a file to OneDrive.

        Args:
            content (str): The text content to upload.
            parent_id (str, optional): The ID of the folder to upload the file to. Defaults to 'root'.
            file_name (str, optional): The name to give the uploaded file. Defaults to 'new_file.txt'.

        Returns:
            A dictionary containing the uploaded file's metadata.
            
        Tags:
            upload, text, file, create, important
        """
        if not file_name:
            raise ValueError("File name cannot be empty.")

        url = f"{self.base_url}/me/drive/items/{parent_id}:/{file_name}:/content"
        data = content.encode('utf-8')
        response = self._put(url, data=data, content_type="text/plain")
        return self._handle_response(response)

    def get_document_content(self, item_id: str) -> dict[str, Any]:
        """
        Retrieves the content of a file from OneDrive.

        Args:
            item_id (str): The ID of the file.

        Returns:
            A dictionary containing the file content. For text files, content is string. For binary, it's base64 encoded.
            
        Tags:
            get, content, read, file, important
        """
        if not item_id:
            raise ValueError("Missing required parameter 'item_id'.")
        
        metadata = self.get_item_metadata(item_id=item_id)
        file_metadata = metadata.get("file")
        if not file_metadata:
            raise ValueError(f"Item with ID '{item_id}' is not a file.")
            
        file_mime_type = file_metadata.get("mimeType", "")

        url = f"{self.base_url}/me/drive/items/{item_id}/content"
        response = self._get(url)
        
        if response.status_code >= 400:
            # Try to handle as JSON error response from Graph API
            return self._handle_response(response)

        content = response.content
        
        is_text = file_mime_type.startswith("text/") or \
                any(t in file_mime_type for t in ['json', 'xml', 'csv', 'javascript', 'html'])

        content_dict = {}
        if is_text:
            try:
                content_dict["content"] = content.decode("utf-8")
            except UnicodeDecodeError:
                is_text = False
        
        if not is_text:
            content_dict["content_base64"] = base64.b64encode(content).decode("ascii")

        return {
            "name": metadata.get("name"),
            "content_type": "text" if is_text else "binary",
            **content_dict,
            "size": len(content),
        }

    def list_tools(self):
        return [
            self.get_drive_info,
            self.search_files,
            self.get_item_metadata,
            self.create_folder,
            self.delete_item,
            self.download_file,
            self.upload_file,
            self.get_my_profile,
            self.list_folders,
            self.list_files,
            self.create_folder_and_list,
            self.upload_text_file,
            self.get_document_content,
        ]
