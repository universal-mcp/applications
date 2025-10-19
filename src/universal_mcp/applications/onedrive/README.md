# OnedriveApp MCP Server

An MCP Server for the OnedriveApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the OnedriveApp API.


| Tool | Description |
|------|-------------|
| `get_drive_info` | Fetches high-level information about the user's entire OneDrive. It returns drive-wide details like the owner and storage quota, differing from `get_item_metadata` which describes a specific item, and `get_my_profile` which retrieves general user account information. |
| `search_files` | Searches the user's entire OneDrive for files and folders matching a specified text query. This function performs a comprehensive search from the drive's root, distinguishing it from `list_files` or `list_folders` which only browse the contents of a single directory. |
| `get_item_metadata` | Fetches detailed metadata for a specific file or folder using its unique ID. It returns properties like name, size, and type. Unlike `get_document_content`, it doesn't retrieve the file's actual content, focusing solely on the item's attributes for quick inspection without a full download. |
| `create_folder` | Creates a new folder with a specified name within a parent directory, which defaults to the root. Returns metadata for the new folder. Unlike `create_folder_and_list`, this function only creates the folder and returns its specific metadata, not the parent directory's contents. |
| `delete_item` | Permanently deletes a specified file or folder from OneDrive using its unique item ID. This versatile function can remove any type of drive item, distinguished from functions that only list or create specific types. A successful deletion returns an empty response, confirming the item's removal. |
| `download_file` | Retrieves a temporary, pre-authenticated download URL for a specific file using its item ID. This function provides a link for subsequent download, differing from `get_document_content` which directly fetches the file's raw content. The URL is returned within a dictionary. |
| `upload_file` | Uploads a local binary file (under 4MB) from a given path to a specified OneDrive folder. Unlike `upload_text_file`, which uploads string content, this function reads from the filesystem. The destination filename can be customized, and it returns the new file's metadata upon completion. |
| `get_my_profile` | Fetches the profile for the currently authenticated user, specifically retrieving their ID and user principal name. This function confirms user identity, distinguishing it from `get_drive_info`, which returns details about the OneDrive storage space (e.g., quota) rather than the user's personal profile. |
| `list_folders` | Retrieves a list of only the folders within a specified parent directory in OneDrive. Unlike `_list_drive_items` which returns all items, this function filters the results to exclude files. Defaults to the root directory if no parent `item_id` is provided. |
| `list_files` | Retrieves a list of files within a specified OneDrive folder, defaulting to the root. Unlike `_list_drive_items` which fetches all items, this function filters the results to exclusively return items identified as files, excluding any subdirectories. |
| `create_folder_and_list` | Performs a composite action: creates a new folder, then lists all items (files and folders) within that parent directory. This confirms creation by returning the parent's updated contents, distinct from `create_folder` which only returns the new folder's metadata. |
| `upload_text_file` | Creates and uploads a new file to OneDrive directly from a string of text content. Unlike `upload_file`, which requires a local file path, this function is specifically for creating a text file from in-memory string data, with a customizable name and destination folder. |
| `get_document_content` | Retrieves the content of a specific file by its item ID and returns it directly as base64-encoded data. This function is distinct from `download_file`, which only provides a temporary URL for the content, and from `get_item_metadata`, which returns file attributes without the content itself. The function fetches the content by following the file's pre-authenticated download URL. |
