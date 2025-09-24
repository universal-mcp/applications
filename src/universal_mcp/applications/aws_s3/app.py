import base64
import json
from typing import Any

import boto3
from botocore.exceptions import ClientError
from universal_mcp.applications.application import BaseApplication
from universal_mcp.integrations import Integration


class AwsS3App(BaseApplication):
    """
    A class to interact with Amazon S3.
    """

    def __init__(self, integration: Integration | None = None, client=None, **kwargs):
        """
        Initializes the AmazonS3App.

        Args:
            aws_access_key_id (str, optional): AWS access key ID.
            aws_secret_access_key (str, optional): AWS secret access key.
            region_name (str, optional): AWS region name.
        """
        super().__init__(name="aws_s3", integration=integration, **kwargs)
        self._client = client
        self.integration = integration

    @property
    def client(self):
        """
        Lazily initializes and returns a cached Boto3 S3 client instance. It retrieves authentication credentials from the associated `integration` object. This property is the core mechanism used by all other methods in the class to interact with AWS S3, raising an error if the integration is not set.
        """
        if not self.integration:
            raise ValueError("Integration not initialized")
        if not self._client:
            credentials = self.integration.get_credentials()
            credentials = {
                "aws_access_key_id": credentials.get("access_key_id")
                or credentials.get("username"),
                "aws_secret_access_key": credentials.get("secret_access_key")
                or credentials.get("password"),
                "region_name": credentials.get("region"),
            }
            self._client = boto3.client("s3", **credentials)
        return self._client

    def list_buckets(self) -> list[str]:
        """
        Retrieves all S3 buckets accessible by the configured AWS credentials. It calls the S3 API's list_buckets operation and processes the response to return a simple list containing just the names of the buckets.

        Returns:
            List[str]: A list of bucket names.
        """
        response = self.client.list_buckets()
        return [bucket["Name"] for bucket in response["Buckets"]]

    def create_bucket(self, bucket_name: str, region: str | None = None) -> bool:
        """
        Creates a new Amazon S3 bucket with a specified name and optional region. Returns `True` upon successful creation, or `False` if an AWS client error, such as a naming conflict or permission issue, occurs.

        Args:
            bucket_name (str): The name of the bucket to create.
            region (str, optional): The region to create the bucket in.

        Returns:
            bool: True if the bucket was created successfully.
        Tags:
            important
        """
        try:
            if region:
                self.client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={"LocationConstraint": region},
                )
            else:
                self.client.create_bucket(Bucket=bucket_name)
            return True
        except ClientError:
            return False

    def delete_bucket(self, bucket_name: str) -> bool:
        """
        Deletes a specified S3 bucket. The operation requires the bucket to be empty to succeed. It returns `True` if the bucket is successfully deleted and `False` if an error occurs, such as the bucket not being found or containing objects.

        Args:
            bucket_name (str): The name of the bucket to delete.

        Returns:
            bool: True if the bucket was deleted successfully.
        Tags:
            important
        """
        try:
            self.client.delete_bucket(Bucket=bucket_name)
            return True
        except ClientError:
            return False

    def get_bucket_policy(self, bucket_name: str) -> dict[str, Any]:
        """
        Retrieves the IAM resource policy for a specified S3 bucket, parsing the JSON string into a dictionary. If the operation fails due to permissions or a non-existent policy, it returns an error dictionary. This complements `put_bucket_policy`, which applies a new policy.

        Args:
            bucket_name (str): The name of the S3 bucket.

        Returns:
            Dict[str, Any]: The bucket policy as a dictionary.
        Tags:
            important
        """
        try:
            response = self.client.get_bucket_policy(Bucket=bucket_name)
            return json.loads(response["Policy"])
        except ClientError as e:
            return {"error": str(e)}

    def set_bucket_policy(self, bucket_name: str, policy: dict[str, Any]) -> bool:
        """
        Applies or replaces the access policy for a specified S3 bucket. The function accepts the policy as a dictionary, converts it to JSON, and assigns it to the bucket. This write operation is the counterpart to `get_bucket_policy` and returns `True` on success.

        Args:
            bucket_name (str): The name of the S3 bucket.
            policy (Dict[str, Any]): The bucket policy as a dictionary.

        Returns:
            bool: True if the policy was set successfully.
        Tags:
            important
        """
        try:
            self.client.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))
            return True
        except ClientError:
            return False

    def list_subdirectories(
        self, bucket_name: str, prefix: str | None = None
    ) -> list[str]:
        """
        Lists immediate subdirectories (common prefixes) within an S3 bucket. If a prefix is provided, it returns subdirectories under that path; otherwise, it lists top-level directories. This function specifically lists folders, distinguishing it from `list_objects`, which lists files.

        Args:
            bucket_name (str): The name of the S3 bucket.
            prefix (str, optional): The prefix to list folders under.

        Returns:
            List[str]: A list of folder prefixes.
        Tags:
            important
        """
        paginator = self.client.get_paginator("list_objects_v2")
        operation_parameters = {"Bucket": bucket_name}
        if prefix:
            operation_parameters["Prefix"] = prefix
            operation_parameters["Delimiter"] = "/"
        else:
            operation_parameters["Delimiter"] = "/"

        prefixes = []
        for page in paginator.paginate(**operation_parameters):
            for cp in page.get("CommonPrefixes", []):
                prefixes.append(cp.get("Prefix"))
        return prefixes

    def create_prefix(
        self, bucket_name: str, prefix_name: str, parent_prefix: str | None = None
    ) -> bool:
        """
        Creates a prefix (folder) in an S3 bucket, optionally nested under a parent prefix. It simulates a directory by creating a zero-byte object with a key ending in a slash ('/'), distinguishing it from put_object, which uploads content.

        Args:
            bucket_name (str): The name of the S3 bucket.
            prefix_name (str): The name of the prefix to create.
            parent_prefix (str, optional): The parent prefix (folder path).

        Returns:
            bool: True if the prefix was created successfully.
        Tags:
            important
        """
        if parent_prefix:
            key = f"{parent_prefix.rstrip('/')}/{prefix_name}/"
        else:
            key = f"{prefix_name}/"
        self.client.put_object(Bucket=bucket_name, Key=key)
        return True

    def list_objects(self, bucket_name: str, prefix: str) -> list[dict[str, Any]]:
        """
        Paginates through and lists all objects within a specified S3 bucket prefix. It returns a curated list of metadata for each object (key, name, size, last modified), excluding folder placeholders. This function specifically lists files, distinguishing it from `list_prefixes` which lists folders.

        Args:
            bucket_name (str): The name of the S3 bucket.
            prefix (str): The prefix (folder path) to list objects under.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing object metadata.
        Tags:
            important
        """
        paginator = self.client.get_paginator("list_objects_v2")
        operation_parameters = {"Bucket": bucket_name, "Prefix": prefix}
        objects = []
        for page in paginator.paginate(**operation_parameters):
            for obj in page.get("Contents", []):
                if not obj["Key"].endswith("/"):
                    objects.append(
                        {
                            "key": obj["Key"],
                            "name": obj["Key"].split("/")[-1],
                            "size": obj["Size"],
                            "last_modified": obj["LastModified"].isoformat()
                            if hasattr(obj["LastModified"], "isoformat")
                            else str(obj["LastModified"]),
                        }
                    )
        return objects

    def put_text_object(
        self, bucket_name: str, prefix: str, object_name: str, content: str
    ) -> bool:
        """
        Uploads string content to create an object in a specified S3 bucket and prefix. The content is UTF-8 encoded before being written. This method is for text, distinguishing it from `put_object_from_base64` which handles binary data.

        Args:
            bucket_name (str): The name of the S3 bucket.
            prefix (str): The prefix (folder path) where the object will be created.
            object_name (str): The name of the object to create.
            content (str): The content to write into the object.

        Returns:
            bool: True if the object was created successfully.
        Tags:
            important
        """
        key = f"{prefix.rstrip('/')}/{object_name}" if prefix else object_name
        self.client.put_object(
            Bucket=bucket_name, Key=key, Body=content.encode("utf-8")
        )
        return True

    def put_object_from_base64(
        self, bucket_name: str, prefix: str, object_name: str, base64_content: str
    ) -> bool:
        """
        Decodes a base64 string into binary data and uploads it as an object to a specified S3 location. This method is designed for binary files, differentiating it from `put_object` which handles plain text content. Returns true on success.

        Args:
            bucket_name (str): The name of the S3 bucket.
            prefix (str): The prefix (folder path) where the object will be created.
            object_name (str): The name of the object to create.
            base64_content (str): The base64-encoded content to upload.

        Returns:
            bool: True if the object was created successfully.
        Tags:
            important
        """
        try:
            key = f"{prefix.rstrip('/')}/{object_name}" if prefix else object_name
            content = base64.b64decode(base64_content)
            self.client.put_object(Bucket=bucket_name, Key=key, Body=content)
            return True
        except Exception:
            return False

    def get_object_with_content(self, bucket_name: str, key: str) -> dict[str, Any]:
        """
        Retrieves an S3 object's content. It decodes text files as UTF-8 or encodes binary files as base64 based on the object's key. This function downloads the full object body, unlike `get_object_metadata` which only fetches metadata without content, returning the content, name, size, and type.

        Args:
            bucket_name (str): The name of the S3 bucket.
            key (str): The key (path) to the object.

        Returns:
            Dict[str, Any]: A dictionary containing the object's name, content type, content (as text or base64), and size.
        Tags:
            important
        """
        try:
            obj = self.client.get_object(Bucket=bucket_name, Key=key)
            content = obj["Body"].read()
            is_text_file = key.lower().endswith(
                (".txt", ".csv", ".json", ".xml", ".html", ".md", ".js", ".css", ".py")
            )
            content_dict = (
                {"content": content.decode("utf-8")}
                if is_text_file
                else {"content_base64": base64.b64encode(content).decode("ascii")}
            )
            return {
                "name": key.split("/")[-1],
                "content_type": "text" if is_text_file else "binary",
                **content_dict,
                "size": len(content),
            }
        except ClientError as e:
            return {"error": str(e)}

    def get_object_metadata(self, bucket_name: str, key: str) -> dict[str, Any]:
        """
        Efficiently retrieves metadata for a specified S3 object, such as size and last modified date, without downloading its content. This function uses a HEAD request, making it faster than `get_object_content` for accessing object properties. Returns a dictionary of metadata or an error message on failure.

        Args:
            bucket_name (str): The name of the S3 bucket.
            key (str): The key (path) to the object.

        Returns:
            Dict[str, Any]: A dictionary containing the object's metadata.
        Tags:
            important
        """
        try:
            response = self.client.head_object(Bucket=bucket_name, Key=key)
            return {
                "key": key,
                "name": key.split("/")[-1],
                "size": response.get("ContentLength", 0),
                "last_modified": response.get("LastModified", "").isoformat()
                if response.get("LastModified")
                else "",
                "content_type": response.get("ContentType", ""),
                "etag": response.get("ETag", ""),
                "metadata": response.get("Metadata", {}),
            }
        except ClientError as e:
            return {"error": str(e)}

    def copy_object(
        self, source_bucket: str, source_key: str, dest_bucket: str, dest_key: str
    ) -> bool:
        """
        Copies an S3 object from a specified source location to a destination, which can be in the same or a different bucket. Unlike `move_object`, the original object remains at the source after the copy operation. It returns `True` for a successful operation.

        Args:
            source_bucket (str): The source bucket name.
            source_key (str): The source object key.
            dest_bucket (str): The destination bucket name.
            dest_key (str): The destination object key.

        Returns:
            bool: True if the object was copied successfully.
        Tags:
            important
        """
        try:
            copy_source = {"Bucket": source_bucket, "Key": source_key}
            self.client.copy_object(
                CopySource=copy_source, Bucket=dest_bucket, Key=dest_key
            )
            return True
        except ClientError:
            return False

    def move_object(
        self, source_bucket: str, source_key: str, dest_bucket: str, dest_key: str
    ) -> bool:
        """
        Moves an S3 object from a source to a destination. This is achieved by first copying the object to the new location and subsequently deleting the original. The move can occur within the same bucket or between different ones, returning `True` on success.

        Args:
            source_bucket (str): The source bucket name.
            source_key (str): The source object key.
            dest_bucket (str): The destination bucket name.
            dest_key (str): The destination object key.

        Returns:
            bool: True if the object was moved successfully.
        Tags:
            important
        """
        if self.copy_object(source_bucket, source_key, dest_bucket, dest_key):
            return self.delete_object(source_bucket, source_key)
        return False

    def delete_single_object(self, bucket_name: str, key: str) -> bool:
        """
        Deletes a single, specified object from an S3 bucket using its key. Returns `True` if successful, otherwise `False`. For bulk deletions in a single request, the `delete_objects` function should be used instead.

        Args:
            bucket_name (str): The name of the S3 bucket.
            key (str): The key (path) to the object to delete.

        Returns:
            bool: True if the object was deleted successfully.
        Tags:
            important
        """
        try:
            self.client.delete_object(Bucket=bucket_name, Key=key)
            return True
        except ClientError:
            return False

    def delete_objects(self, bucket_name: str, keys: list[str]) -> dict[str, Any]:
        """
        Performs a bulk deletion of objects from a specified S3 bucket in a single request. Given a list of keys, it returns a dictionary detailing successful deletions and any errors. This method is the batch-processing counterpart to the singular `delete_object` function, designed for efficiency.

        Args:
            bucket_name (str): The name of the S3 bucket.
            keys (List[str]): List of object keys to delete.

        Returns:
            Dict[str, Any]: Results of the deletion operation.
        Tags:
            important
        """
        try:
            delete_dict = {"Objects": [{"Key": key} for key in keys]}
            response = self.client.delete_objects(
                Bucket=bucket_name, Delete=delete_dict
            )
            return {
                "deleted": [obj.get("Key") for obj in response.get("Deleted", [])],
                "errors": [obj for obj in response.get("Errors", [])],
            }
        except ClientError as e:
            return {"error": str(e)}

    def generate_presigned_url(
        self,
        bucket_name: str,
        key: str,
        expiration: int = 3600,
        http_method: str = "GET",
    ) -> str:
        """
        Generates a temporary, secure URL for a specific S3 object. This URL grants time-limited permissions for actions like GET, PUT, or DELETE, expiring after a defined period. It allows object access without sharing permanent AWS credentials.

        Args:
            bucket_name (str): The name of the S3 bucket.
            key (str): The key (path) to the object.
            expiration (int): Time in seconds for the presigned URL to remain valid (default: 3600).
            http_method (str): HTTP method for the presigned URL (default: 'GET').

        Returns:
            str: The presigned URL or error message.
        Tags:
            important
        """
        try:
            method_map = {
                "GET": "get_object",
                "PUT": "put_object",
                "DELETE": "delete_object",
            }

            response = self.client.generate_presigned_url(
                method_map.get(http_method.upper(), "get_object"),
                Params={"Bucket": bucket_name, "Key": key},
                ExpiresIn=expiration,
            )
            return response
        except ClientError as e:
            return f"Error: {str(e)}"

    def search_objects(
        self,
        bucket_name: str,
        prefix: str = "",
        name_pattern: str = "",
        min_size: int | None = None,
        max_size: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Filters objects within an S3 bucket and prefix based on a name pattern and size range. It retrieves all objects via `list_objects` and then applies the specified criteria client-side, returning a refined list of matching objects and their metadata.

        Args:
            bucket_name (str): The name of the S3 bucket.
            prefix (str): The prefix to search within.
            name_pattern (str): Pattern to match in object names (case-insensitive).
            min_size (int, optional): Minimum object size in bytes.
            max_size (int, optional): Maximum object size in bytes.

        Returns:
            List[Dict[str, Any]]: List of matching objects with metadata.
        Tags:
            important
        """
        all_objects = self.list_objects(bucket_name, prefix)
        filtered_objects = []

        for obj in all_objects:
            # Filter by name pattern
            if name_pattern and name_pattern.lower() not in obj["name"].lower():
                continue

            # Filter by size
            if min_size and obj["size"] < min_size:
                continue
            if max_size and obj["size"] > max_size:
                continue

            filtered_objects.append(obj)

        return filtered_objects

    def get_storage_summary(self, bucket_name: str, prefix: str = "") -> dict[str, Any]:
        """
        Calculates and returns statistics for an S3 bucket or prefix. The result includes the total number of objects, their combined size in bytes, and a human-readable string representation of the size (e.g., '15.2 MB').

        Args:
            bucket_name (str): The name of the S3 bucket.
            prefix (str): The prefix to calculate size for (default: entire bucket).

        Returns:
            Dict[str, Any]: Dictionary containing total size, object count, and human-readable size.
        Tags:
            important
        """
        objects = self.list_objects(bucket_name, prefix)
        total_size = sum(obj["size"] for obj in objects)
        object_count = len(objects)

        # Convert to human-readable format
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if total_size < 1024.0:
                human_size = f"{total_size:.2f} {unit}"
                break
            total_size /= 1024.0
        else:
            human_size = f"{total_size:.2f} PB"

        return {
            "total_size_bytes": sum(obj["size"] for obj in objects),
            "human_readable_size": human_size,
            "object_count": object_count,
        }

    def list_tools(self):
        return [
            self.create_bucket,
            self.delete_bucket,
            self.get_bucket_policy,
            self.set_bucket_policy,
            self.list_subdirectories,
            self.create_prefix,
            self.list_objects,
            self.put_text_object,
            self.put_object_from_base64,
            self.get_object_with_content,
            self.get_object_metadata,
            self.copy_object,
            self.move_object,
            self.delete_single_object,
            self.delete_objects,
            self.generate_presigned_url,
            self.search_objects,
            self.get_storage_summary,
        ]
