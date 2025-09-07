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
        Gets the S3 client.
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
        Lists all S3 buckets.

        Returns:
            List[str]: A list of bucket names.
        """
        response = self.client.list_buckets()
        return [bucket["Name"] for bucket in response["Buckets"]]

    def create_bucket(self, bucket_name: str, region: str | None = None) -> bool:
        """
        Creates a new S3 bucket.

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
        Deletes an S3 bucket (must be empty).

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
        Gets the bucket policy for the specified bucket.

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

    def put_bucket_policy(self, bucket_name: str, policy: dict[str, Any]) -> bool:
        """
        Sets the bucket policy for the specified bucket.

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

    def list_prefixes(self, bucket_name: str, prefix: str | None = None) -> list[str]:
        """
        Lists common prefixes ("folders") in the specified S3 bucket and prefix.

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

    def put_prefix(
        self, bucket_name: str, prefix_name: str, parent_prefix: str | None = None
    ) -> bool:
        """
        Creates a prefix ("folder") in the specified S3 bucket.

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
        Lists all objects in a specified S3 prefix.

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

    def put_object(
        self, bucket_name: str, prefix: str, object_name: str, content: str
    ) -> bool:
        """
        Uploads an object to the specified S3 prefix.

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
        Uploads a binary object from base64 content to the specified S3 prefix.

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

    def get_object_content(self, bucket_name: str, key: str) -> dict[str, Any]:
        """
        Gets the content of a specified object.

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
        Gets metadata for a specified object without downloading the content.

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
        Copies an object from one location to another.

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
        Moves an object from one location to another (copy then delete).

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

    def delete_object(self, bucket_name: str, key: str) -> bool:
        """
        Deletes an object from S3.

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
        Deletes multiple objects from S3.

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
        Generates a presigned URL for accessing an S3 object.

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
        Searches for objects in S3 based on various criteria.

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

    def get_bucket_size(self, bucket_name: str, prefix: str = "") -> dict[str, Any]:
        """
        Calculates the total size and object count for a bucket or prefix.

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
            self.put_bucket_policy,
            self.list_prefixes,
            self.put_prefix,
            self.list_objects,
            self.put_object,
            self.put_object_from_base64,
            self.get_object_content,
            self.get_object_metadata,
            self.copy_object,
            self.move_object,
            self.delete_object,
            self.delete_objects,
            self.generate_presigned_url,
            self.search_objects,
            self.get_bucket_size,
        ]
