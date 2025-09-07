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
        """Gets the GraphClient instance, initializing it if necessary.

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

        def acquire_token():
            access_token = credentials.get("access_token")
            refresh_token = credentials.get("refresh_token")
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "Bearer",
            }

        if self._client is None:
            self._client = GraphClient(token_callback=acquire_token)
            # Get me
            me = self._client.me.get().execute_query()
            logger.debug(me.properties)
            # Get sites
            sites = self._client.sites.root.get().execute_query()
            self._site_url = sites.properties.get("id")
        return self._client

    def list_folders(self, folder_path: str | None = None) -> list[dict[str, Any]]:
        """Lists folders in the specified directory or root if not specified.

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

    def create_folder(
        self, folder_name: str, folder_path: str | None = None
    ) -> dict[str, Any]:
        """Creates a folder in the specified directory or root if not specified.

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

    def list_documents(self, folder_path: str) -> list[dict[str, Any]]:
        """Lists all documents in a specified folder.

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

    def create_document(
        self, file_path: str, file_name: str, content: str
    ) -> dict[str, Any]:
        """Creates a document in the specified folder.

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
        """Gets the content of a specified document.

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

    def delete_file(self, file_path: str):
        """Deletes a file from OneDrive.

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
            self.create_folder,
            self.list_documents,
            self.create_document,
            self.get_document_content,
            self.delete_file,
        ]
