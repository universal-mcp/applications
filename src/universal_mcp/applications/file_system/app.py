import os
import shutil
import uuid

from universal_mcp.applications.application import BaseApplication


class FileSystemApp(BaseApplication):
    def __init__(self, **kwargs):
        super().__init__(name="file_system", **kwargs)

    @staticmethod
    async def _generate_file_path():
        return f"/tmp/{uuid.uuid4()}"

    @staticmethod
    async def read_file(file_path: str):
        """Reads file data from a file path.

        Args:
            file_path (str): The path to the file to read.

        Returns:
            bytes: The file content as bytes.

        Raises:
            FileNotFoundError: If the file doesn't exist.
            IOError: If there's an error reading the file.
            
        Tags: 
            important
        """
        with open(file_path, "rb") as f:
            return f.read()

    @staticmethod
    async def write_file(file_data: bytes, file_path: str = None):
        """Writes file data to a file path.

        Args:
            file_data (bytes): The data to write to the file.
            file_path (str, optional): The path where to write the file.
                If None, generates a random path in /tmp. Defaults to None.

        Returns:
            dict: A dictionary containing the operation result with keys:
                - status (str): "success" if the operation completed successfully
                - data (dict): Contains file information with keys:
                    - url (str): The file path where the data was written
                    - filename (str): The filename (same as url in this implementation)
                    - size (int): The size of the written data in bytes

        Raises:
            IOError: If there's an error writing the file.
            PermissionError: If there are insufficient permissions to write to the path.
            
        Tags:
            important
        """
        if file_path is None:
            file_path = await FileSystemApp._generate_file_path()
        with open(file_path, "wb") as f:
            f.write(file_data)
            result = {
                "status": "success",
                "data": {
                    "url": file_path,
                    "filename": file_path,
                    "size": len(file_data),
                },
            }
            return result

    @staticmethod
    async def delete_file(file_path: str):
        """Deletes a file from the file system."""
        os.remove(file_path)
        return {"status": "success"}

    @staticmethod
    async def move_file(source_file_path: str, dest_file_path: str):
        """Moves a file from one path to another."""
        os.rename(source_file_path, dest_file_path)
        return {"status": "success"}

    @staticmethod
    async def copy_file(source_file_path: str, dest_file_path: str):
        """Copies a file from one path to another."""
        shutil.copy(source_file_path, dest_file_path)
        return {"status": "success"}

    def list_tools(self):
        return [
            FileSystemApp.read_file,
            FileSystemApp.write_file,
        ]
