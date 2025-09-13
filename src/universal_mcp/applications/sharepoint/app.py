import base64
import io
from datetime import datetime
from io import BytesIO
from typing import Any

from loguru import logger
from office365.graph_client import GraphClient

from universal_mcp.applications.application import BaseApplication
from universal_mcp.integrations import Integration


def _to_iso_optional(dt_obj: datetime | None) -> str | None:
    """Converts a datetime object to ISO format string, or returns None if the object is None."""
    if dt_obj is not None:
        return dt_obj.isoformat()
    return None


class SharepointApp(BaseApplication):
    """
    Base class for Universal MCP Applications.
    """

    def __init__(self, integration: Integration = None, client=None, **kwargs) -> None:
        """Initializes the SharepointApp.
        Args:
            client (GraphClient | None, optional): An existing GraphClient instance. If None, a new client will be created on first use.
        """
        super().__init__(name="sharepoint", integration=integration, **kwargs)
        self._client = client
        self.integration = integration
        self._site_url = None

    @property
    def client(self):
        """
        A lazy-loaded property that gets or creates an authenticated GraphClient instance. On its first call, it uses integration credentials to initialize the client, fetches the user's profile and root site ID, and caches the instance for subsequent use. This ensures efficient connection management.
        
        Returns:
            GraphClient: The authenticated GraphClient instance.
        """
        if not self.integration:
            raise ValueError("Integration is required")
        credentials = self.integration.get_credentials()
        if not credentials:
            raise ValueError("No credentials found")

        if not credentials.get("access_token"):
            raise ValueError("No access token found")

        def _acquire_token():
            """
            Formats stored credentials for the `GraphClient` authentication callback. It packages existing access and refresh tokens from the integration into the specific dictionary structure required by the client library for authentication, including a hardcoded 'Bearer' token type.
            """
            access_token = credentials.get("access_token")
            refresh_token = credentials.get("refresh_token")
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "Bearer",
            }

        if self._client is None:
            self._client = GraphClient(token_callback=_acquire_token)
            # Get me
            me = self._client.me.get().execute_query()
            logger.debug(me.properties)
            # Get sites
            sites = self._client.sites.root.get().execute_query()
            self._site_url = sites.properties.get("id")
        return self._client

    def list_folders(self, folder_path: str | None = None) -> list[dict[str, Any]]:
        """
        Retrieves the names of all immediate subfolders within a specified directory. If a path is not provided, it defaults to listing folders in the root of the user's drive. This function is distinct from `list_documents`, which lists files.
        
        Args:
            folder_path (Optional[str], optional): The path to the parent folder. If None, lists folders in the root.
        
        Returns:
            List[Dict[str, Any]]: A list of folder names in the specified directory.
        
        Tags:
            important
        """
        if folder_path:
            folder = self.client.me.drive.root.get_by_path(folder_path)
            folders = folder.get_folders(False).execute_query()
        else:
            folders = self.client.me.drive.root.get_folders(False).execute_query()

        return [folder.properties.get("name") for folder in folders]

    def create_folder_and_list(
        self, folder_name: str, folder_path: str | None = None
    ) -> dict[str, Any]:
        """
        Creates a new folder with a given name inside a specified parent directory on SharePoint. If no path is provided, the folder is created in the root. It then returns an updated list of all folder names within that parent directory.
        
        Args:
            folder_name (str): The name of the folder to create.
            folder_path (str | None, optional): The path to the parent folder. If None, creates in the root.
        
        Returns:
            Dict[str, Any]: The updated list of folders in the target directory.
        
        Tags:
            important
        """
        if folder_path:
            folder = self.client.me.drive.root.get_by_path(folder_path)
        else:
            folder = self.client.me.drive.root
        folder.create_folder(folder_name).execute_query()
        return self.list_folders(folder_path)

    def list_files(self, folder_path: str) -> list[dict[str, Any]]:
        """
        Retrieves files from a specified folder path. For each file, it returns a dictionary containing key metadata like its name, URL, size, creation date, and last modified date. This function specifically lists files, distinct from `list_folders` which only lists directories.
        
        Args:
            folder_path (str): The path to the folder whose documents are to be listed.
        
        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing document metadata.
        
        Tags:
            important
        """
        folder = self.client.me.drive.root.get_by_path(folder_path)
        files = folder.get_files(False).execute_query()

        return [
            {
                "name": f.name,
                "url": f.properties.get("ServerRelativeUrl"),
                "size": f.properties.get("Length"),
                "created": _to_iso_optional(f.properties.get("TimeCreated")),
                "modified": _to_iso_optional(f.properties.get("TimeLastModified")),
            }
            for f in files
        ]

    def upload_text_file(
        self, file_path: str, file_name: str, content: str
    ) -> dict[str, Any]:
        """
        Uploads string content to a new file within a specified SharePoint folder path. After creation, it returns an updated list of all documents and their metadata residing in that folder, effectively confirming the file was added successfully.
        
        Args:
            file_path (str): The path to the folder where the document will be created.
            file_name (str): The name of the document to create.
            content (str): The content to write into the document.
        
        Returns:
            Dict[str, Any]: The updated list of documents in the folder.
        
        Tags: important
        """
        file = self.client.me.drive.root.get_by_path(file_path)
        file_io = io.StringIO(content)
        file_io.name = file_name
        file.upload_file(file_io).execute_query()
        return self.list_documents(file_path)

    def get_document_content(self, file_path: str) -> dict[str, Any]:
        """
        Retrieves a document's content from SharePoint. It returns a dictionary with the content, name, and size. Content is decoded as a string for text files or Base64-encoded for binary files. This is distinct from `list_documents` which only returns metadata without content.
        
        Args:
            file_path (str): The path to the document.
        
        Returns:
            Dict[str, Any]: A dictionary containing the document's name, content type, content (as text or base64), and size.
        
        Tags: important
        """
        file = self.client.me.drive.root.get_by_path(file_path).get().execute_query()
        content_stream = BytesIO()
        file.download(content_stream).execute_query()
        content_stream.seek(0)
        content = content_stream.read()

        is_text_file = file_path.lower().endswith(
            (".txt", ".csv", ".json", ".xml", ".html", ".md", ".js", ".css", ".py")
        )
        content_dict = (
            {"content": content.decode("utf-8")}
            if is_text_file
            else {"content_base64": base64.b64encode(content).decode("ascii")}
        )
        return {
            "name": file_path.split("/")[-1],
            "content_type": "text" if is_text_file else "binary",
            **content_dict,
            "size": len(content),
        }

    def delete_document(self, file_path: str):
        """
        Permanently deletes a specified file from SharePoint/OneDrive. The function takes the file path as an argument and returns True upon successful deletion. An exception is raised if the file is not found or the deletion fails.
        
        Args:
            file_path (str): The path to the file to delete.
        
        Returns:
            bool: True if the file was deleted successfully.
        
        Tags:
            important
        """
        file = self.client.me.drive.root.get_by_path(file_path)
        file.delete_object().execute_query()
        return True

    def list_tools(self):
        return [
            self.list_folders,
            self.create_folder_and_list,
            self.list_files,
            self.upload_text_file,
            self.get_document_content,
            self.delete_document,
        ]
