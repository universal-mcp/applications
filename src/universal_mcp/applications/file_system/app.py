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
        """
        Asynchronously reads the entire content of a specified file in binary mode. This static method takes a file path and returns its data as a bytes object, serving as a fundamental file retrieval operation within the FileSystem application.

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
        """
        Writes binary data to a specified file path. If no path is provided, it creates a unique temporary file in `/tmp`. The function returns a dictionary confirming success and providing metadata about the new file, including its path and size.

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
    async def remove_file(file_path: str):
        """
        Permanently removes a file from the local file system at the specified path. Unlike `move_file`, which relocates a file, this operation is irreversible. It returns a dictionary with a 'success' status to confirm deletion.
        """
        os.remove(file_path)
        return {"status": "success"}

    @staticmethod
    async def move_file(source_file_path: str, dest_file_path: str):
        """
        Relocates a file from a source path to a destination path on the same filesystem. This function effectively renames or moves the file, differing from `copy_file` which creates a duplicate. It returns a dictionary confirming the successful completion of the operation.
        """
        os.rename(source_file_path, dest_file_path)
        return {"status": "success"}

    @staticmethod
    async def copy_file(source_file_path: str, dest_file_path: str):
        """
        Duplicates a file by copying it from a source path to a destination path, leaving the original file untouched. This contrasts with `move_file`, which relocates the file. It returns a success status dictionary upon successful completion of the operation.
        """
        shutil.copy(source_file_path, dest_file_path)
        return {"status": "success"}

    def list_tools(self):
        return [
            FileSystemApp.read_file,
            FileSystemApp.write_file,
        ]
