# SharePoint Application

This application provides tools for interacting with the Microsoft SharePoint API via Microsoft Graph. It allows you to manage files, folders, and retrieve information about your SharePoint drive.

## Available Tools

-   `get_my_profile`: Fetches the profile for the currently authenticated user.
-   `get_drive_info`: Fetches high-level information about the user's SharePoint drive.
-   `search_files`: Searches for files and folders in the user's SharePoint.
-   `get_item_metadata`: Fetches metadata for a specific file or folder.
-   `create_folder`: Creates a new folder.
-   `delete_item`: Deletes a file or folder.
-   `download_file`: Retrieves a download URL for a file.
-   `upload_file`: Uploads a local file.
-   `list_folders`: Lists all folders in a specified directory.
-   `list_files`: Lists all files in a specified directory.
-   `create_folder_and_list`: Creates a folder and then lists the contents of the parent directory.
-   `upload_text_file`: Uploads content from a string to a new text file.
-   `get_document_content`: Retrieves the content of a file.