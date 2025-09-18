# SharepointApp MCP Server

An MCP Server for the SharepointApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the SharepointApp API.


| Tool | Description |
|------|-------------|
| `list_folders` | Retrieves a list of immediate subfolder names within a specified SharePoint directory. If no path is provided, it defaults to the root drive. This function is distinct from `list_files`, as it exclusively lists directories, not files. |
| `create_folder_and_list` | Creates a new folder with a given name inside a specified parent directory (or the root). It then returns an updated list of all folder names within that same directory, effectively confirming that the creation operation was successful. |
| `list_files` | Retrieves metadata for all files in a specified folder. For each file, it returns key details like name, URL, size, and timestamps. This function exclusively lists file properties, distinguishing it from `list_folders` (which lists directories) and `get_document_content` (which retrieves file content). |
| `upload_text_file` | Uploads string content to create a new file in a specified SharePoint folder. To confirm the operation, it returns an updated list of all files and their metadata from that directory, including the newly created file. |
| `get_document_content` | Retrieves a file's content from a specified SharePoint path. It returns a dictionary containing the file's name and size, decoding text files as a string and Base64-encoding binary files. Unlike `list_files`, which only fetches metadata, this function provides the actual file content. |
| `delete_document` | Permanently deletes a specified file from a SharePoint drive using its full path. This is the sole destructive file operation, contrasting with functions that read or create files. It returns `True` on successful deletion and raises an exception on failure, such as if the file is not found. |
