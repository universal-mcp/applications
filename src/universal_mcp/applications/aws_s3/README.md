# AwsS3App MCP Server

An MCP Server for the AwsS3App API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the AwsS3App API.


| Tool | Description |
|------|-------------|
| `create_bucket` | Creates a new Amazon S3 bucket with a specified name and optional region. Returns `True` upon successful creation, or `False` if an AWS client error, such as a naming conflict or permission issue, occurs. |
| `delete_bucket` | Deletes a specified S3 bucket. The operation requires the bucket to be empty to succeed. It returns `True` if the bucket is successfully deleted and `False` if an error occurs, such as the bucket not being found or containing objects. |
| `get_bucket_policy` | Retrieves the IAM resource policy for a specified S3 bucket, parsing the JSON string into a dictionary. If the operation fails due to permissions or a non-existent policy, it returns an error dictionary. This complements `put_bucket_policy`, which applies a new policy. |
| `set_bucket_policy` | Applies or replaces the access policy for a specified S3 bucket. The function accepts the policy as a dictionary, converts it to JSON, and assigns it to the bucket. This write operation is the counterpart to `get_bucket_policy` and returns `True` on success. |
| `list_subdirectories` | Lists immediate subdirectories (common prefixes) within an S3 bucket. If a prefix is provided, it returns subdirectories under that path; otherwise, it lists top-level directories. This function specifically lists folders, distinguishing it from `list_objects`, which lists files. |
| `create_prefix` | Creates a prefix (folder) in an S3 bucket, optionally nested under a parent prefix. It simulates a directory by creating a zero-byte object with a key ending in a slash ('/'), distinguishing it from put_object, which uploads content. |
| `list_objects` | Paginates through and lists all objects within a specified S3 bucket prefix. It returns a curated list of metadata for each object (key, name, size, last modified), excluding folder placeholders. This function specifically lists files, distinguishing it from `list_prefixes` which lists folders. |
| `put_text_object` | Uploads string content to create an object in a specified S3 bucket and prefix. The content is UTF-8 encoded before being written. This method is for text, distinguishing it from `put_object_from_base64` which handles binary data. |
| `put_object_from_base64` | Decodes a base64 string into binary data and uploads it as an object to a specified S3 location. This method is designed for binary files, differentiating it from `put_object` which handles plain text content. Returns true on success. |
| `get_object_with_content` | Retrieves an S3 object's content. It decodes text files as UTF-8 or encodes binary files as base64 based on the object's key. This function downloads the full object body, unlike `get_object_metadata` which only fetches metadata without content, returning the content, name, size, and type. |
| `get_object_metadata` | Efficiently retrieves metadata for a specified S3 object, such as size and last modified date, without downloading its content. This function uses a HEAD request, making it faster than `get_object_content` for accessing object properties. Returns a dictionary of metadata or an error message on failure. |
| `copy_object` | Copies an S3 object from a specified source location to a destination, which can be in the same or a different bucket. Unlike `move_object`, the original object remains at the source after the copy operation. It returns `True` for a successful operation. |
| `move_object` | Moves an S3 object from a source to a destination. This is achieved by first copying the object to the new location and subsequently deleting the original. The move can occur within the same bucket or between different ones, returning `True` on success. |
| `delete_single_object` | Deletes a single, specified object from an S3 bucket using its key. Returns `True` if successful, otherwise `False`. For bulk deletions in a single request, the `delete_objects` function should be used instead. |
| `delete_objects` | Performs a bulk deletion of objects from a specified S3 bucket in a single request. Given a list of keys, it returns a dictionary detailing successful deletions and any errors. This method is the batch-processing counterpart to the singular `delete_object` function, designed for efficiency. |
| `generate_presigned_url` | Generates a temporary, secure URL for a specific S3 object. This URL grants time-limited permissions for actions like GET, PUT, or DELETE, expiring after a defined period. It allows object access without sharing permanent AWS credentials. |
| `search_objects` | Filters objects within an S3 bucket and prefix based on a name pattern and size range. It retrieves all objects via `list_objects` and then applies the specified criteria client-side, returning a refined list of matching objects and their metadata. |
| `get_storage_summary` | Calculates and returns statistics for an S3 bucket or prefix. The result includes the total number of objects, their combined size in bytes, and a human-readable string representation of the size (e.g., '15.2 MB'). |
