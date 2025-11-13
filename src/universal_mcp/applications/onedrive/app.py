import base64
import os
from typing import Any
from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class OnedriveApp(APIApplication):
    """
    Application for interacting with Microsoft OneDrive API (via Microsoft Graph).
    Provides tools to manage files, folders, and access Drive information.
    """

    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="onedrive", integration=integration, **kwargs)
        self.base_url = "https://graph.microsoft.com/v1.0"

    async def get_my_profile(self) -> dict[str, Any]:
        """
        Fetches the profile for the currently authenticated user, specifically retrieving their ID and user principal name. This function confirms user identity, distinguishing it from `get_drive_info`, which returns details about the OneDrive storage space (e.g., quota) rather than the user's personal profile.

        Returns:
            dict[str, Any]: A dictionary containing the user's id and userPrincipalName.

        Raises:
            HTTPStatusError: If the API request fails.

        Tags:
            profile, user, account
        """
        url = f"{self.base_url}/me"
        query_params = {"$select": "id,userPrincipalName"}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_drive_info(self) -> dict[str, Any]:
        """
        Fetches high-level information about the user's entire OneDrive. It returns drive-wide details like the owner and storage quota, differing from `get_item_metadata` which describes a specific item, and `get_my_profile` which retrieves general user account information.

        Returns:
            A dictionary containing drive information.

        Tags:
            drive, storage, quota, info
        """
        url = f"{self.base_url}/me/drive"
        response = await self._aget(url)
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

    async def search_files(self, query: str) -> dict[str, Any]:
        """
        Searches the user's entire OneDrive for files and folders matching a specified text query. This function performs a comprehensive search from the drive's root, distinguishing it from `list_files` or `list_folders` which only browse the contents of a single directory.

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
        response = await self._aget(url)
        return self._handle_response(response)

    async def get_item_metadata(self, item_id: str) -> dict[str, Any]:
        """
        Fetches detailed metadata for a specific file or folder using its unique ID. It returns properties like name, size, and type. Unlike `get_document_content`, it doesn't retrieve the file's actual content, focusing solely on the item's attributes for quick inspection without a full download.

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
        response = await self._aget(url)
        return self._handle_response(response)

    async def create_folder(self, name: str, parent_id: str = "root") -> dict[str, Any]:
        """
        Creates a new folder with a specified name within a parent directory, which defaults to the root. Returns metadata for the new folder. Unlike `create_folder_and_list`, this function only creates the folder and returns its specific metadata, not the parent directory's contents.

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
        data = {"name": name, "folder": {}, "@microsoft.graph.conflictBehavior": "rename"}
        response = await self._apost(url, data=data)
        return self._handle_response(response)

    async def delete_item(self, item_id: str) -> dict[str, Any]:
        """
        Permanently deletes a specified file or folder from OneDrive using its unique item ID. This versatile function can remove any type of drive item, distinguished from functions that only list or create specific types. A successful deletion returns an empty response, confirming the item's removal.

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
        response = await self._adelete(url)
        return self._handle_response(response)

    async def download_file(self, item_id: str) -> dict[str, Any]:
        """
        Retrieves a temporary, pre-authenticated download URL for a specific file using its item ID. This function provides a link for subsequent download, differing from `get_document_content` which directly fetches the file's raw content. The URL is returned within a dictionary.

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
        response = await self._aget(url)
        metadata = self._handle_response(response)
        download_url = metadata.get("@microsoft.graph.downloadUrl")
        if not download_url:
            raise ValueError("Could not retrieve download URL for the item.")
        return {"download_url": download_url}

    async def upload_file(self, file_path: str, parent_id: str = "root", file_name: str | None = None) -> dict[str, Any]:
        """
        Uploads a local binary file (under 4MB) from a given path to a specified OneDrive folder. Unlike `upload_text_file`, which uploads string content, this function reads from the filesystem. The destination filename can be customized, and it returns the new file's metadata upon completion.

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
        response = await self._aput(url, data=data, content_type="application/octet-stream")
        return self._handle_response(response)

    async def list_folders(self, item_id: str = "root") -> dict[str, Any]:
        """
        Retrieves a list of only the folders within a specified parent directory in OneDrive. Unlike `_list_drive_items` which returns all items, this function filters the results to exclude files. Defaults to the root directory if no parent `item_id` is provided.

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

    async def list_files(self, item_id: str = "root") -> dict[str, Any]:
        """
        Retrieves a list of files within a specified OneDrive folder, defaulting to the root. Unlike `_list_drive_items` which fetches all items, this function filters the results to exclusively return items identified as files, excluding any subdirectories.

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

    async def create_folder_and_list(self, name: str, parent_id: str = "root") -> dict[str, Any]:
        """
        Performs a composite action: creates a new folder, then lists all items (files and folders) within that parent directory. This confirms creation by returning the parent's updated contents, distinct from `create_folder` which only returns the new folder's metadata.

        Args:
            name (str): The name of the new folder.
            parent_id (str, optional): The ID of the parent folder. Defaults to 'root'.

        Returns:
            A dictionary containing the list of items in the parent folder after creation.

        Tags:
            create, folder, list, important
        """
        await self.create_folder(name=name, parent_id=parent_id)
        return self._list_drive_items(item_id=parent_id)

    async def upload_text_file(self, content: str, parent_id: str = "root", file_name: str = "new_file.txt") -> dict[str, Any]:
        """
        Creates and uploads a new file to OneDrive directly from a string of text content. Unlike `upload_file`, which requires a local file path, this function is specifically for creating a text file from in-memory string data, with a customizable name and destination folder.

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
        data = content.encode("utf-8")
        response = await self._aput(url, data=data, content_type="text/plain")
        return self._handle_response(response)

    async def get_document_content(self, item_id: str) -> dict[str, Any]:
        """
        Retrieves the content of a specific file by its item ID and returns it directly as base64-encoded data. This function is distinct from `download_file`, which only provides a temporary URL for the content, and from `get_item_metadata`, which returns file attributes without the content itself. The function fetches the content by following the file's pre-authenticated download URL.

        Args:
            item_id (str): The ID of the file.

        Returns:
            dict[str, Any]: A dictionary containing the file details:
                - 'type' (str): The general type of the file (e.g., "image", "audio", "video", "file").
                - 'data' (str): The base64 encoded content of the file.
                - 'mime_type' (str): The MIME type of the file.
                - 'file_name' (str): The name of the file.

        Tags:
            get, content, read, file, important
        """
        if not item_id:
            raise ValueError("Missing required parameter 'item_id'.")
        metadata = await self.get_item_metadata(item_id=item_id)
        file_metadata = metadata.get("file")
        if not file_metadata:
            raise ValueError(f"Item with ID '{item_id}' is not a file.")
        file_mime_type = file_metadata.get("mimeType", "application/octet-stream")
        file_name = metadata.get("name")
        download_url = metadata.get("@microsoft.graph.downloadUrl")
        if not download_url:
            logger.error(f"Could not find @microsoft.graph.downloadUrl in metadata for item {item_id}")
            raise ValueError("Could not retrieve download URL for the item.")
        response = await self._aget(download_url)
        response.raise_for_status()
        content = response.content
        attachment_type = file_mime_type.split("/")[0] if "/" in file_mime_type else "file"
        if attachment_type not in ["image", "audio", "video", "text"]:
            attachment_type = "file"
        return {"type": attachment_type, "data": content, "mime_type": file_mime_type, "file_name": file_name}

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
