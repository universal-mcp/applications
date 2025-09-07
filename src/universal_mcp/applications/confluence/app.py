from typing import Any

import httpx

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class ConfluenceApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="confluence", integration=integration, **kwargs)
        self._base_url: str | None = None

    def get_base_url(self):
        headers = self._get_headers()
        url = "https://api.atlassian.com/oauth/token/accessible-resources"

        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        resources = response.json()

        if not resources:
            raise ValueError(
                "No accessible Confluence resources found for the provided credentials."
            )

        first_resource = resources[0]
        resource_id = first_resource.get("id")

        if not resource_id:
            raise ValueError(
                "Could not determine the resource ID from the first accessible resource."
            )

        return f"https://api.atlassian.com/ex/confluence/{resource_id}/api/v2"

    @property
    def base_url(self):
        """Fetches accessible resources and sets the base_url for the first resource found."""
        if self._base_url:
            return self._base_url
        self._base_url = self.get_base_url()
        return self._base_url

    @base_url.setter
    def base_url(self, value: str) -> None:
        """Sets the base URL for the Confluence API.

        Args:
            value (str): The base URL to set.
        """
        self._base_url = value

    def get_attachments(
        self,
        sort=None,
        cursor=None,
        status=None,
        mediaType=None,
        filename=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of attachments based on specified filters like sort order, cursor position, status, media type, filename, and limit, using the GET method.

        Args:
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            status (array): Filter the results to attachments based on their status. By default, `current` and `archived` are used.
            mediaType (string): Filters on the mediaType of attachments. Only one may be specified.
            filename (string): Filters on the file-name of attachments. Only one may be specified.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested attachments are returned.

        Tags:
            Attachment, important
        """
        url = f"{self.base_url}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("sort", sort),
                ("cursor", cursor),
                ("status", status),
                ("mediaType", mediaType),
                ("filename", filename),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachment_by_id(
        self,
        id,
        version=None,
        include_labels=None,
        include_properties=None,
        include_operations=None,
        include_versions=None,
        include_version=None,
        include_collaborators=None,
    ) -> Any:
        """
        Retrieves a specific attachment by ID with optional parameters to include labels, properties, operations, versions, collaborators, or specify a version.

        Args:
            id (string): id
            version (integer): Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
            include_labels (boolean): Includes labels associated with this attachment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes content properties associated with this attachment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this attachment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_versions (boolean): Includes versions associated with this attachment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_version (boolean): Includes the current version associated with this attachment in the response.
        By default this is included and can be omitted by setting the value to `false`.
            include_collaborators (boolean): Includes collaborators on the attachment.

        Returns:
            Any: Returned if the requested attachment is returned.

        Tags:
            Attachment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/attachments/{id}"
        query_params = {
            k: v
            for k, v in [
                ("version", version),
                ("include-labels", include_labels),
                ("include-properties", include_properties),
                ("include-operations", include_operations),
                ("include-versions", include_versions),
                ("include-version", include_version),
                ("include-collaborators", include_collaborators),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_attachment(self, id, purge=None) -> Any:
        """
        Deletes the specified attachment using its unique identifier and optionally purges it permanently.

        Args:
            id (string): id
            purge (boolean): If attempting to purge the attachment.

        Returns:
            Any: Returned if the attachment was successfully deleted.

        Tags:
            Attachment, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/attachments/{id}"
        query_params = {k: v for k, v in [("purge", purge)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachment_labels(
        self, id, prefix=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves labels associated with a specific attachment, optionally filtered by prefix, sorted, and paginated using cursor-based pagination.

        Args:
            id (string): id
            prefix (string): Filter the results to labels based on their prefix.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested labels are returned.

        Tags:
            Label
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/attachments/{id}/labels"
        query_params = {
            k: v
            for k, v in [
                ("prefix", prefix),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachment_operations(self, id) -> dict[str, Any]:
        """
        Retrieves operations associated with a specific attachment using its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/attachments/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachment_content_properties(
        self, attachment_id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves properties of a specific attachment identified by `attachment-id`, with optional filtering, sorting, and pagination via query parameters.

        Args:
            attachment_id (string): attachment-id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties, important
        """
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'")
        url = f"{self.base_url}/attachments/{attachment_id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_attachment_property(
        self, attachment_id, key=None, value=None
    ) -> dict[str, Any]:
        """
        Creates a new property for the specified attachment and returns the created property.

        Args:
            attachment_id (string): attachment-id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/attachments/{attachment_id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachment_content_properties_by_id(
        self, attachment_id, property_id
    ) -> dict[str, Any]:
        """
        Retrieves a specific property of an attachment using the provided attachment ID and property ID.

        Args:
            attachment_id (string): attachment-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/attachments/{attachment_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_attachment_property_by_id(
        self, attachment_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates a specific property for an attachment by its ID and returns the updated result.

        Args:
            attachment_id (string): attachment-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/attachments/{attachment_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_attachment_property_by_id(self, attachment_id, property_id) -> Any:
        """
        Deletes a specific property from an attachment using the DELETE method, identified by both the attachment ID and the property ID.

        Args:
            attachment_id (string): attachment-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/attachments/{attachment_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachment_versions(
        self, id, cursor=None, limit=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of versions for a specific attachment using the "id" parameter and supports query parameters for pagination and sorting.

        Args:
            id (string): id
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the requested attachment versions are returned.

        Tags:
            Version
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/attachments/{id}/versions"
        query_params = {
            k: v
            for k, v in [("cursor", cursor), ("limit", limit), ("sort", sort)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachment_version_details(
        self, attachment_id, version_number
    ) -> dict[str, Any]:
        """
        Retrieves a specific version of an attachment file using the attachment ID and version number, returning the details of the specified version.

        Args:
            attachment_id (string): attachment-id
            version_number (string): version-number

        Returns:
            dict[str, Any]: Returned if the requested version details are successfully retrieved.

        Tags:
            Version
        """
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'")
        if version_number is None:
            raise ValueError("Missing required parameter 'version-number'")
        url = f"{self.base_url}/attachments/{attachment_id}/versions/{version_number}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachment_comments(
        self, id, body_format=None, cursor=None, limit=None, sort=None, version=None
    ) -> dict[str, Any]:
        """
        Retrieves paginated footer comments for a specific attachment using query parameters for formatting, pagination, sorting, and version control.

        Args:
            id (string): id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.
            version (integer): Version number of the attachment to retrieve comments for. If no version provided, retrieves comments for the latest version.

        Returns:
            dict[str, Any]: Returned if the attachment comments were successfully retrieved

        Tags:
            Comment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/attachments/{id}/footer-comments"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
                ("sort", sort),
                ("version", version),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_posts(
        self,
        id=None,
        space_id=None,
        sort=None,
        status=None,
        title=None,
        body_format=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of blog posts using the "GET" method at the "/blogposts" endpoint, allowing filtering by parameters such as ID, space ID, sort order, status, title, and body format.

        Args:
            id (array): Filter the results based on blog post ids. Multiple blog post ids can be specified as a comma-separated list.
            space_id (array): Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.
            sort (string): Used to sort the result by a particular field.
            status (array): Filter the results to blog posts based on their status. By default, `current` is used.
            title (string): Filter the results to blog posts based on their title.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of blog posts per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested blog posts are returned.

        Tags:
            Blog Post
        """
        url = f"{self.base_url}/blogposts"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("space-id", space_id),
                ("sort", sort),
                ("status", status),
                ("title", title),
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_blog_post(
        self, spaceId, private=None, status=None, title=None, body=None, createdAt=None
    ) -> Any:
        """
        Creates a new blog post using the POST method at the "/blogposts" endpoint, with an optional parameter to specify whether the post should be private.

        Args:
            spaceId (string): ID of the space
            private (boolean): The blog post will be private. Only the user who creates this blog post will have permission to view and edit one.
            status (string): The status of the blog post, specifies if the blog post will be created as a new blog post or a draft
            title (string): Title of the blog post, required if creating non-draft.
            body (string): body
            createdAt (string): Created date of the blog post in the format of "yyyy-MM-ddTHH:mm:ss.SSSZ".

        Returns:
            Any: Returned if the blog post was created successfully.

        Tags:
            Blog Post
        """
        request_body = {
            "spaceId": spaceId,
            "status": status,
            "title": title,
            "body": body,
            "createdAt": createdAt,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/blogposts"
        query_params = {k: v for k, v in [("private", private)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_by_id(
        self,
        id,
        body_format=None,
        get_draft=None,
        status=None,
        version=None,
        include_labels=None,
        include_properties=None,
        include_operations=None,
        include_likes=None,
        include_versions=None,
        include_version=None,
        include_favorited_by_current_user_status=None,
        include_webresources=None,
        include_collaborators=None,
    ) -> Any:
        """
        Retrieves a specific blog post by ID, allowing optional filtering by various parameters such as body format, draft status, and inclusion of additional metadata like labels, properties, and collaborators.

        Args:
            id (string): id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            get_draft (boolean): Retrieve the draft version of this blog post.
            status (array): Filter the blog post being retrieved by its status.
            version (integer): Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
            include_labels (boolean): Includes labels associated with this blog post in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes content properties associated with this blog post in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this blog post in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_likes (boolean): Includes likes associated with this blog post in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_versions (boolean): Includes versions associated with this blog post in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_version (boolean): Includes the current version associated with this blog post in the response.
        By default this is included and can be omitted by setting the value to `false`.
            include_favorited_by_current_user_status (boolean): Includes whether this blog post has been favorited by the current user.
            include_webresources (boolean): Includes web resources that can be used to render blog post content on a client.
            include_collaborators (boolean): Includes collaborators on the blog post.

        Returns:
            Any: Returned if the requested blog post is returned.

        Tags:
            Blog Post
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("get-draft", get_draft),
                ("status", status),
                ("version", version),
                ("include-labels", include_labels),
                ("include-properties", include_properties),
                ("include-operations", include_operations),
                ("include-likes", include_likes),
                ("include-versions", include_versions),
                ("include-version", include_version),
                (
                    "include-favorited-by-current-user-status",
                    include_favorited_by_current_user_status,
                ),
                ("include-webresources", include_webresources),
                ("include-collaborators", include_collaborators),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_blog_post(
        self, id, status, title, body, version, spaceId=None, createdAt=None
    ) -> Any:
        """
        Updates or creates a blog post with the specified ID and returns a status message.

        Args:
            id (string): id
            status (string): The updated status of the blog post.

        Note, if you change the status of a blog post from 'current' to 'draft' and it has an existing draft, the existing draft will be deleted in favor of the updated draft.
        Additionally, this endpoint can be used to restore a 'trashed' or 'deleted' blog post to 'current' status. For restoration, blog post contents will not be updated and only the blog post status will be changed.
            title (string): Title of the blog post.
            body (string): body
            version (object): version
            spaceId (string): ID of the containing space.

        This currently **does not support moving the blog post to a different space**.
            createdAt (string): Created date of the blog post in the format of "yyyy-MM-ddTHH:mm:ss.SSSZ".

        Returns:
            Any: Returned if the requested blog post is successfully updated.

        Tags:
            Blog Post
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id,
            "status": status,
            "title": title,
            "spaceId": spaceId,
            "body": body,
            "version": version,
            "createdAt": createdAt,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/blogposts/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_blog_post(self, id, purge=None, draft=None) -> Any:
        """
        Deletes a blog post with the specified ID using the DELETE method, with optional parameters to purge or manage draft status.

        Args:
            id (string): id
            purge (boolean): If attempting to purge the blog post.
            draft (boolean): If attempting to delete a blog post that is a draft.

        Returns:
            Any: Returned if the blog post was successfully deleted.

        Tags:
            Blog Post
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}"
        query_params = {
            k: v for k, v in [("purge", purge), ("draft", draft)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blogpost_attachments(
        self,
        id,
        sort=None,
        cursor=None,
        status=None,
        mediaType=None,
        filename=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of attachments associated with a specific blog post, supporting filtering by status, media type, filename, and pagination via query parameters.

        Args:
            id (string): id
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            status (array): Filter the results to attachments based on their status. By default, `current` and `archived` are used.
            mediaType (string): Filters on the mediaType of attachments. Only one may be specified.
            filename (string): Filters on the file-name of attachments. Only one may be specified.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested attachments are returned.

        Tags:
            Attachment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("sort", sort),
                ("cursor", cursor),
                ("status", status),
                ("mediaType", mediaType),
                ("filename", filename),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_by_type_in_blog_post(
        self, id, type, sort=None, cursor=None, limit=None, body_format=None
    ) -> dict[str, Any]:
        """
        Retrieves custom content for a specific blog post using the "GET" method with options to filter by type, sort order, and other parameters.

        Args:
            id (string): id
            type (string): The type of custom content being requested. See: for additional details on custom content.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field. Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.

        Returns:
            dict[str, Any]: Returned if the requested custom content is returned.

        Tags:
            Custom Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/custom-content"
        query_params = {
            k: v
            for k, v in [
                ("type", type),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
                ("body-format", body_format),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_labels(
        self, id, prefix=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of labels associated with a specific blog post, filtered by prefix, sorted, and paginated based on provided query parameters.

        Args:
            id (string): id
            prefix (string): Filter the results to labels based on their prefix.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested labels are returned.

        Tags:
            Label
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/labels"
        query_params = {
            k: v
            for k, v in [
                ("prefix", prefix),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_like_count(self, id) -> dict[str, Any]:
        """
        Retrieves the number of likes for a blog post using the specified ID via the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested count is returned.

        Tags:
            Like
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/likes/count"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_like_users(self, id, cursor=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of users who liked a specific blog post, using cursor-based pagination parameters.

        Args:
            id (string): id
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested account IDs are returned.

        Tags:
            Like
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/likes/users"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blogpost_content_properties(
        self, blogpost_id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves properties of a specific blog post identified by its ID, allowing optional filtering by key, sorting, and pagination using cursor and limit parameters.

        Args:
            blogpost_id (string): blogpost-id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties
        """
        if blogpost_id is None:
            raise ValueError("Missing required parameter 'blogpost-id'")
        url = f"{self.base_url}/blogposts/{blogpost_id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_blogpost_property(
        self, blogpost_id, key=None, value=None
    ) -> dict[str, Any]:
        """
        Adds custom properties to a specified blogpost and returns a success or error status.

        Args:
            blogpost_id (string): blogpost-id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if blogpost_id is None:
            raise ValueError("Missing required parameter 'blogpost-id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/blogposts/{blogpost_id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blogpost_content_properties_by_id(
        self, blogpost_id, property_id
    ) -> dict[str, Any]:
        """
        Retrieves a specific property from a blog post using the provided blogpost and property IDs.

        Args:
            blogpost_id (string): blogpost-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if blogpost_id is None:
            raise ValueError("Missing required parameter 'blogpost-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/blogposts/{blogpost_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_blogpost_property_by_id(
        self, blogpost_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates the specified property of a blog post using the provided identifiers and returns a status message.

        Args:
            blogpost_id (string): blogpost-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if blogpost_id is None:
            raise ValueError("Missing required parameter 'blogpost-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/blogposts/{blogpost_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_blogpost_property_by_id(self, blogpost_id, property_id) -> Any:
        """
        Deletes a specific property from a blog post using the blog post ID and property ID.

        Args:
            blogpost_id (string): blogpost-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if blogpost_id is None:
            raise ValueError("Missing required parameter 'blogpost-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/blogposts/{blogpost_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_operations(self, id) -> dict[str, Any]:
        """
        Retrieves operations associated with a specific blog post identified by the provided ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_versions(
        self, id, body_format=None, cursor=None, limit=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of version history entries for a specific blog post, optionally paginated and sorted, with customizable response formatting.

        Args:
            id (string): id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the requested blog post versions are returned.

        Tags:
            Version
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/versions"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_version_details(
        self, blogpost_id, version_number
    ) -> dict[str, Any]:
        """
        Retrieves a specific version of a blog post identified by its ID and version number using the GET method.

        Args:
            blogpost_id (string): blogpost-id
            version_number (string): version-number

        Returns:
            dict[str, Any]: Returned if the requested version details are successfully retrieved.

        Tags:
            Version
        """
        if blogpost_id is None:
            raise ValueError("Missing required parameter 'blogpost-id'")
        if version_number is None:
            raise ValueError("Missing required parameter 'version-number'")
        url = f"{self.base_url}/blogposts/{blogpost_id}/versions/{version_number}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def convert_content_ids_to_content_types(self, contentIds) -> dict[str, Any]:
        """
        Converts content IDs to their corresponding types using a POST request and returns appropriate responses based on the conversion outcome.

        Args:
            contentIds (array): The content ids to convert. They may be provided as strings or numbers.

        Returns:
            dict[str, Any]: Returned if the requested content ids are successfully converted to their content types

        Tags:
            Content
        """
        request_body = {
            "contentIds": contentIds,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/content/convert-ids-to-types"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_by_type(
        self,
        type,
        id=None,
        space_id=None,
        sort=None,
        cursor=None,
        limit=None,
        body_format=None,
    ) -> dict[str, Any]:
        """
        Retrieves custom content at the specified path "/custom-content" using the GET method, allowing for filtering by type, id, space-id, sort order, and pagination with optional cursor and limit parameters.

        Args:
            type (string): The type of custom content being requested. See: for additional details on custom content.
            id (array): Filter the results based on custom content ids. Multiple custom content ids can be specified as a comma-separated list.
            space_id (array): Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field. Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.

        Returns:
            dict[str, Any]: Returned if the requested custom content is returned.

        Tags:
            Custom Content
        """
        url = f"{self.base_url}/custom-content"
        query_params = {
            k: v
            for k, v in [
                ("type", type),
                ("id", id),
                ("space-id", space_id),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
                ("body-format", body_format),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_custom_content(
        self,
        type,
        title,
        body,
        status=None,
        spaceId=None,
        pageId=None,
        blogPostId=None,
        customContentId=None,
    ) -> Any:
        """
        Creates custom content via a POST request and returns appropriate status codes indicating success or specific errors.

        Args:
            type (string): Type of custom content.
            title (string): Title of the custom content.
            body (string): body
            status (string): The status of the custom content. Defaults to `current` when status not provided.
            spaceId (string): ID of the containing space.
            pageId (string): ID of the containing page.
            blogPostId (string): ID of the containing Blog Post.
            customContentId (string): ID of the containing custom content.

        Returns:
            Any: Returned if the requested custom content is created successfully.

        Tags:
            Custom Content
        """
        request_body = {
            "type": type,
            "status": status,
            "spaceId": spaceId,
            "pageId": pageId,
            "blogPostId": blogPostId,
            "customContentId": customContentId,
            "title": title,
            "body": body,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom-content"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_by_id(
        self,
        id,
        body_format=None,
        version=None,
        include_labels=None,
        include_properties=None,
        include_operations=None,
        include_versions=None,
        include_version=None,
        include_collaborators=None,
    ) -> Any:
        """
        Retrieves custom content by a specified ID using the "GET" method, allowing optional formatting and inclusion of additional details such as labels, properties, operations, versions, and collaborators.

        Args:
            id (string): id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field. Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.
            version (integer): Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
            include_labels (boolean): Includes labels associated with this custom content in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes content properties associated with this custom content in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this custom content in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_versions (boolean): Includes versions associated with this custom content in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_version (boolean): Includes the current version associated with this custom content in the response.
        By default this is included and can be omitted by setting the value to `false`.
            include_collaborators (boolean): Includes collaborators on the custom content.

        Returns:
            Any: Returned if the requested custom content is returned.

        Tags:
            Custom Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/custom-content/{id}"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("version", version),
                ("include-labels", include_labels),
                ("include-properties", include_properties),
                ("include-operations", include_operations),
                ("include-versions", include_versions),
                ("include-version", include_version),
                ("include-collaborators", include_collaborators),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_custom_content(
        self,
        id,
        type,
        status,
        title,
        body,
        version,
        spaceId=None,
        pageId=None,
        blogPostId=None,
        customContentId=None,
    ) -> Any:
        """
        Updates or replaces a custom content resource identified by the provided ID using the PUT method, returning various status responses based on the request's success or failure.

        Args:
            id (string): id
            type (string): Type of custom content.
            status (string): The status of the custom content.
            title (string): Title of the custom content.
            body (string): body
            version (object): version
            spaceId (string): ID of the containing space.
            pageId (string): ID of the containing page.
            blogPostId (string): ID of the containing Blog Post.
            customContentId (string): ID of the containing custom content.

        Returns:
            Any: Returned if the requested custom content is updated successfully.

        Tags:
            Custom Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id,
            "type": type,
            "status": status,
            "spaceId": spaceId,
            "pageId": pageId,
            "blogPostId": blogPostId,
            "customContentId": customContentId,
            "title": title,
            "body": body,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom-content/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_custom_content(self, id, purge=None) -> Any:
        """
        Deletes a custom content resource identified by its ID from the system, with an optional query parameter to specify whether to purge the content.

        Args:
            id (string): id
            purge (boolean): If attempting to purge the custom content.

        Returns:
            Any: Returned if the custom content was deleted.

        Tags:
            Custom Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/custom-content/{id}"
        query_params = {k: v for k, v in [("purge", purge)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_attachments(
        self,
        id,
        sort=None,
        cursor=None,
        status=None,
        mediaType=None,
        filename=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of attachments associated with custom content identified by the given ID, allowing for filtering by sort order, cursor, status, media type, filename, and limiting the number of results.

        Args:
            id (string): id
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            status (array): Filter the results to attachments based on their status. By default, `current` and `archived` are used.
            mediaType (string): Filters on the mediaType of attachments. Only one may be specified.
            filename (string): Filters on the file-name of attachments. Only one may be specified.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested attachments are returned.

        Tags:
            Attachment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/custom-content/{id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("sort", sort),
                ("cursor", cursor),
                ("status", status),
                ("mediaType", mediaType),
                ("filename", filename),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_comments(
        self, id, body_format=None, cursor=None, limit=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of footer comments associated with a specific custom content item using the "GET" method, allowing for optional filtering by body format, cursor, limit, and sort order.

        Args:
            id (string): id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the custom content comments were successfully retrieved

        Tags:
            Comment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/custom-content/{id}/footer-comments"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_labels(
        self, id, prefix=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves labels for custom content with a specified ID, allowing filtering by prefix, sorting, and pagination using query parameters.

        Args:
            id (string): id
            prefix (string): Filter the results to labels based on their prefix.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested labels are returned.

        Tags:
            Label
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/custom-content/{id}/labels"
        query_params = {
            k: v
            for k, v in [
                ("prefix", prefix),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_operations(self, id) -> dict[str, Any]:
        """
        Retrieves operational details for a custom content item identified by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/custom-content/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_content_properties(
        self, custom_content_id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves the properties associated with a specific custom content item by its ID, with optional filtering and pagination via query parameters.

        Args:
            custom_content_id (string): custom-content-id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties
        """
        if custom_content_id is None:
            raise ValueError("Missing required parameter 'custom-content-id'")
        url = f"{self.base_url}/custom-content/{custom_content_id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_custom_content_property(
        self, custom_content_id, key=None, value=None
    ) -> dict[str, Any]:
        """
        Adds or updates properties for a specified custom content item and returns the operation result.

        Args:
            custom_content_id (string): custom-content-id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if custom_content_id is None:
            raise ValueError("Missing required parameter 'custom-content-id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom-content/{custom_content_id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_content_properties_by_id(
        self, custom_content_id, property_id
    ) -> dict[str, Any]:
        """
        Retrieves properties of a specific item identified by a custom content ID and property ID using the GET method.

        Args:
            custom_content_id (string): custom-content-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if custom_content_id is None:
            raise ValueError("Missing required parameter 'custom-content-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/custom-content/{custom_content_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_custom_content_property_by_id(
        self, custom_content_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates a specific custom property of a custom content item in Confluence and returns the updated property.

        Args:
            custom_content_id (string): custom-content-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if custom_content_id is None:
            raise ValueError("Missing required parameter 'custom-content-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom-content/{custom_content_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_custom_content_property_by_id(
        self, custom_content_id, property_id
    ) -> Any:
        """
        Deletes a specified property from a custom content resource.

        Args:
            custom_content_id (string): custom-content-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if custom_content_id is None:
            raise ValueError("Missing required parameter 'custom-content-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/custom-content/{custom_content_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_labels(
        self, label_id=None, prefix=None, cursor=None, sort=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of labels using the "GET" method at the "/labels" endpoint, allowing filtering by label ID, prefix, sorting, and pagination via query parameters.

        Args:
            label_id (array): Filters on label ID. Multiple IDs can be specified as a comma-separated list.
            prefix (array): Filters on label prefix. Multiple IDs can be specified as a comma-separated list.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            sort (string): Used to sort the result by a particular field.
            limit (integer): Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested labels are returned.

        Tags:
            Label
        """
        url = f"{self.base_url}/labels"
        query_params = {
            k: v
            for k, v in [
                ("label-id", label_id),
                ("prefix", prefix),
                ("cursor", cursor),
                ("sort", sort),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_label_attachments(
        self, id, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of attachments associated with a label identified by the provided ID, allowing for sorting and pagination via query parameters.

        Args:
            id (string): id
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested attachments for specified label were successfully fetched.

        Tags:
            Attachment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/labels/{id}/attachments"
        query_params = {
            k: v
            for k, v in [("sort", sort), ("cursor", cursor), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_label_blog_posts(
        self, id, space_id=None, body_format=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of blog posts associated with a specific label by ID, allowing optional filtering by space ID, body format, sorting, cursor pagination, and content limit, using the GET method.

        Args:
            id (string): id
            space_id (array): Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of blog posts per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested blog posts for specified label were successfully fetched.

        Tags:
            Blog Post
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/labels/{id}/blogposts"
        query_params = {
            k: v
            for k, v in [
                ("space-id", space_id),
                ("body-format", body_format),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_label_pages(
        self, id, space_id=None, body_format=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of pages associated with a label identified by `{id}`, allowing filtering by space, body format, sorting, and pagination options.

        Args:
            id (string): id
            space_id (array): Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested pages for specified label were successfully fetched.

        Tags:
            Page
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/labels/{id}/pages"
        query_params = {
            k: v
            for k, v in [
                ("space-id", space_id),
                ("body-format", body_format),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_pages(
        self,
        id=None,
        space_id=None,
        sort=None,
        status=None,
        title=None,
        body_format=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of pages based on specified parameters such as ID, space ID, sort order, status, title, body format, cursor, and limit using the GET method at the "/pages" endpoint.

        Args:
            id (array): Filter the results based on page ids. Multiple page ids can be specified as a comma-separated list.
            space_id (array): Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.
            sort (string): Used to sort the result by a particular field.
            status (array): Filter the results to pages based on their status. By default, `current` and `archived` are used.
            title (string): Filter the results to pages based on their title.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested pages are returned.

        Tags:
            Page, important
        """
        url = f"{self.base_url}/pages"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("space-id", space_id),
                ("sort", sort),
                ("status", status),
                ("title", title),
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_page(
        self,
        spaceId,
        embedded=None,
        private=None,
        root_level=None,
        status=None,
        title=None,
        parentId=None,
        body=None,
    ) -> Any:
        """
        Creates a new page with optional query parameters to specify visibility (private/public), embedding, and root-level placement, returning appropriate status codes.

        Args:
            spaceId (string): ID of the space.
            embedded (boolean): Tag the content as embedded and content will be created in NCS.
            private (boolean): The page will be private. Only the user who creates this page will have permission to view and edit one.
            root_level (boolean): The page will be created at the root level of the space (outside the space homepage tree). If true, then a value may not be supplied for the `parentId` body parameter.
            status (string): The status of the page, published or draft.
            title (string): Title of the page, required if page status is not draft.
            parentId (string): The parent content ID of the page. If the `root-level` query parameter is set to false and a value is
        not supplied for this parameter, then the space homepage's ID will be used. If the `root-level` query
        parameter is set to true, then a value may not be supplied for this parameter.
            body (string): body

        Returns:
            Any: Returned if the page was successfully created.

        Tags:
            Page
        """
        request_body = {
            "spaceId": spaceId,
            "status": status,
            "title": title,
            "parentId": parentId,
            "body": body,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/pages"
        query_params = {
            k: v
            for k, v in [
                ("embedded", embedded),
                ("private", private),
                ("root-level", root_level),
            ]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_by_id(
        self,
        id,
        body_format=None,
        get_draft=None,
        status=None,
        version=None,
        include_labels=None,
        include_properties=None,
        include_operations=None,
        include_likes=None,
        include_versions=None,
        include_version=None,
        include_favorited_by_current_user_status=None,
        include_webresources=None,
        include_collaborators=None,
    ) -> Any:
        """
        Retrieves a specific page by its ID, including optional details such as version history, labels, collaborators, and web resources based on query parameters.

        Args:
            id (string): id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            get_draft (boolean): Retrieve the draft version of this page.
            status (array): Filter the page being retrieved by its status.
            version (integer): Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
            include_labels (boolean): Includes labels associated with this page in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes content properties associated with this page in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this page in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_likes (boolean): Includes likes associated with this page in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_versions (boolean): Includes versions associated with this page in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_version (boolean): Includes the current version associated with this page in the response.
        By default this is included and can be omitted by setting the value to `false`.
            include_favorited_by_current_user_status (boolean): Includes whether this page has been favorited by the current user.
            include_webresources (boolean): Includes web resources that can be used to render page content on a client.
            include_collaborators (boolean): Includes collaborators on the page.

        Returns:
            Any: Returned if the requested page is returned.

        Tags:
            Page
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("get-draft", get_draft),
                ("status", status),
                ("version", version),
                ("include-labels", include_labels),
                ("include-properties", include_properties),
                ("include-operations", include_operations),
                ("include-likes", include_likes),
                ("include-versions", include_versions),
                ("include-version", include_version),
                (
                    "include-favorited-by-current-user-status",
                    include_favorited_by_current_user_status,
                ),
                ("include-webresources", include_webresources),
                ("include-collaborators", include_collaborators),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_page(
        self,
        id,
        status,
        title,
        body,
        version,
        spaceId=None,
        parentId=None,
        ownerId=None,
    ) -> Any:
        """
        Updates or creates a page resource at the specified ID and returns a status.

        Args:
            id (string): id
            status (string): The updated status of the page.

        Note, if you change the status of a page from 'current' to 'draft' and it has an existing draft, the existing draft will be deleted in favor of the updated draft.
        Additionally, this endpoint can be used to restore a 'trashed' or 'deleted' page to 'current' status. For restoration, page contents will not be updated and only the page status will be changed.
            title (string): Title of the page.
            body (string): body
            version (object): version
            spaceId (string): ID of the containing space.

        This currently **does not support moving the page to a different space**.
            parentId (string): ID of the parent page.

        This allows the page to be moved under a different parent within the same space.
            ownerId (string): Account ID of the page owner.

        This allows page ownership to be transferred to another user.

        Returns:
            Any: Returned if the requested page is successfully updated.

        Tags:
            Page
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id,
            "status": status,
            "title": title,
            "spaceId": spaceId,
            "parentId": parentId,
            "ownerId": ownerId,
            "body": body,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/pages/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_page(self, id, purge=None, draft=None) -> Any:
        """
        Deletes a page specified by ID using the DELETE method, with optional purge and draft query parameters, returning a successful response if the operation is completed without providing content.

        Args:
            id (string): id
            purge (boolean): If attempting to purge the page.
            draft (boolean): If attempting to delete a page that is a draft.

        Returns:
            Any: Returned if the page was successfully deleted.

        Tags:
            Page
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}"
        query_params = {
            k: v for k, v in [("purge", purge), ("draft", draft)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_attachments(
        self,
        id,
        sort=None,
        cursor=None,
        status=None,
        mediaType=None,
        filename=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of attachments for a page with the specified ID, allowing optional sorting, filtering, and pagination based on query parameters.

        Args:
            id (string): id
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            status (array): Filter the results to attachments based on their status. By default, `current` and `archived` are used.
            mediaType (string): Filters on the mediaType of attachments. Only one may be specified.
            filename (string): Filters on the file-name of attachments. Only one may be specified.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested attachments are returned.

        Tags:
            Attachment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("sort", sort),
                ("cursor", cursor),
                ("status", status),
                ("mediaType", mediaType),
                ("filename", filename),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_by_type_in_page(
        self, id, type, sort=None, cursor=None, limit=None, body_format=None
    ) -> dict[str, Any]:
        """
        Retrieves custom content for a page with the specified ID using the GET method, allowing filtering by type, sorting, pagination, and body format customization.

        Args:
            id (string): id
            type (string): The type of custom content being requested. See: for additional details on custom content.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field. Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.

        Returns:
            dict[str, Any]: Returned if the requested custom content is returned.

        Tags:
            Custom Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/custom-content"
        query_params = {
            k: v
            for k, v in [
                ("type", type),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
                ("body-format", body_format),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_labels(
        self, id, prefix=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of labels for a page with the specified ID, optionally filtering by prefix, sorting, and paginating using cursor and limit parameters.

        Args:
            id (string): id
            prefix (string): Filter the results to labels based on their prefix.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested labels are returned.

        Tags:
            Label
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/labels"
        query_params = {
            k: v
            for k, v in [
                ("prefix", prefix),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_like_count(self, id) -> dict[str, Any]:
        """
        Retrieves the number of likes for a page identified by the given ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested count is returned.

        Tags:
            Like
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/likes/count"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_like_users(self, id, cursor=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of users who have liked a page with the specified ID using the GET method, with optional parameters for pagination.

        Args:
            id (string): id
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested account IDs are returned.

        Tags:
            Like
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/likes/users"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_operations(self, id) -> dict[str, Any]:
        """
        Retrieves operations associated with a specific page based on the provided ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_content_properties(
        self, page_id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves properties associated with a specific page using the Notion API and returns them based on query parameters like key, sort, cursor, and limit.

        Args:
            page_id (string): page-id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties
        """
        if page_id is None:
            raise ValueError("Missing required parameter 'page-id'")
        url = f"{self.base_url}/pages/{page_id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_page_property(self, page_id, key=None, value=None) -> dict[str, Any]:
        """
        Updates properties for a page using the page ID provided in the path.

        Args:
            page_id (string): page-id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if page_id is None:
            raise ValueError("Missing required parameter 'page-id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/pages/{page_id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_content_properties_by_id(self, page_id, property_id) -> dict[str, Any]:
        """
        Retrieves the properties of a specific page element using the page ID and property ID.

        Args:
            page_id (string): page-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if page_id is None:
            raise ValueError("Missing required parameter 'page-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/pages/{page_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_page_property_by_id(
        self, page_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates a specific property for a given page using the provided path parameters and returns the operation status.

        Args:
            page_id (string): page-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if page_id is None:
            raise ValueError("Missing required parameter 'page-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/pages/{page_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_page_property_by_id(self, page_id, property_id) -> Any:
        """
        Deletes a specific property from a specified page using the provided page-id and property-id as path parameters.

        Args:
            page_id (string): page-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if page_id is None:
            raise ValueError("Missing required parameter 'page-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/pages/{page_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_versions(
        self, id, body_format=None, cursor=None, limit=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves versions of a page identified by the specified ID, allowing optional filtering by body format, sorting, and pagination using cursor and limit parameters.

        Args:
            id (string): id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the requested page versions are returned.

        Tags:
            Version
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/versions"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_whiteboard(
        self,
        spaceId,
        private=None,
        title=None,
        parentId=None,
        templateKey=None,
        locale=None,
    ) -> Any:
        """
        Creates a new whiteboard with optional privacy settings and returns the result.

        Args:
            spaceId (string): ID of the space.
            private (boolean): The whiteboard will be private. Only the user who creates this whiteboard will have permission to view and edit one.
            title (string): Title of the whiteboard.
            parentId (string): The parent content ID of the whiteboard.
            templateKey (string): Providing a template key will add that template to the new whiteboard.
            locale (string): If you provide a templateKey, the locale determines the language for creating the template. If you omit the locale, the user's locale is used.

        Returns:
            Any: Returned if the whiteboard was successfully created.

        Tags:
            Whiteboard
        """
        request_body = {
            "spaceId": spaceId,
            "title": title,
            "parentId": parentId,
            "templateKey": templateKey,
            "locale": locale,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/whiteboards"
        query_params = {k: v for k, v in [("private", private)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_whiteboard_by_id(
        self,
        id,
        include_collaborators=None,
        include_direct_children=None,
        include_operations=None,
        include_properties=None,
    ) -> Any:
        """
        Retrieves a specific whiteboard by ID, optionally including additional details such as collaborators, direct children, operations, and properties using query parameters.

        Args:
            id (string): id
            include_collaborators (boolean): Includes collaborators on the whiteboard.
            include_direct_children (boolean): Includes direct children of the whiteboard.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this whiteboard in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes content properties associated with this whiteboard in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.

        Returns:
            Any: Returned if the requested whiteboard is returned.

        Tags:
            Whiteboard
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/whiteboards/{id}"
        query_params = {
            k: v
            for k, v in [
                ("include-collaborators", include_collaborators),
                ("include-direct-children", include_direct_children),
                ("include-operations", include_operations),
                ("include-properties", include_properties),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_whiteboard(self, id) -> Any:
        """
        Deletes the specified whiteboard by its ID and moves it to the trash.

        Args:
            id (string): id

        Returns:
            Any: Returned if the whiteboard was successfully deleted.

        Tags:
            Whiteboard
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/whiteboards/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_whiteboard_content_properties(
        self, id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves properties for a whiteboard with the specified ID, optionally filtering by key, sorting, and paginating results using a cursor and limit parameters.

        Args:
            id (string): id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/whiteboards/{id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_whiteboard_property(self, id, key=None, value=None) -> dict[str, Any]:
        """
        Updates the properties of a specific whiteboard using the API at path "/whiteboards/{id}/properties" via the POST method.

        Args:
            id (string): id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/whiteboards/{id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_whiteboard_content_properties_by_id(
        self, whiteboard_id, property_id
    ) -> dict[str, Any]:
        """
        Retrieves a specific property from a designated whiteboard using the provided whiteboard and property identifiers.

        Args:
            whiteboard_id (string): whiteboard-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if whiteboard_id is None:
            raise ValueError("Missing required parameter 'whiteboard-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/whiteboards/{whiteboard_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_whiteboard_property_by_id(
        self, whiteboard_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates a specific property of a whiteboard using the "PUT" method, specifying the whiteboard and property IDs in the path.

        Args:
            whiteboard_id (string): whiteboard-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if whiteboard_id is None:
            raise ValueError("Missing required parameter 'whiteboard-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/whiteboards/{whiteboard_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_whiteboard_property_by_id(self, whiteboard_id, property_id) -> Any:
        """
        Deletes a specific property from a whiteboard by ID using the DELETE method.

        Args:
            whiteboard_id (string): whiteboard-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if whiteboard_id is None:
            raise ValueError("Missing required parameter 'whiteboard-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/whiteboards/{whiteboard_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_whiteboard_operations(self, id) -> dict[str, Any]:
        """
        Retrieves a list of operations for a specific whiteboard identified by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/whiteboards/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_whiteboard_ancestors(self, id, limit=None) -> dict[str, Any]:
        """
        Retrieves all ancestors for a specified whiteboard in top-to-bottom order, limited by the `limit` parameter, with minimal details returned for each ancestor.

        Args:
            id (string): id
            limit (integer): Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested ancestors are returned.

        Tags:
            Ancestors
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/whiteboards/{id}/ancestors"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_database(self, spaceId, private=None, title=None, parentId=None) -> Any:
        """
        Creates a new database (optionally with private access restrictions) and returns the operation result.

        Args:
            spaceId (string): ID of the space.
            private (boolean): The database will be private. Only the user who creates this database will have permission to view and edit one.
            title (string): Title of the database.
            parentId (string): The parent content ID of the database.

        Returns:
            Any: Returned if the database was successfully created.

        Tags:
            Database
        """
        request_body = {
            "spaceId": spaceId,
            "title": title,
            "parentId": parentId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/databases"
        query_params = {k: v for k, v in [("private", private)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_database_by_id(
        self,
        id,
        include_collaborators=None,
        include_direct_children=None,
        include_operations=None,
        include_properties=None,
    ) -> Any:
        """
        Retrieves a database by its ID and optionally includes additional details such as collaborators, direct children, operations, or properties using the specified query parameters.

        Args:
            id (string): id
            include_collaborators (boolean): Includes collaborators on the database.
            include_direct_children (boolean): Includes direct children of the database.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this database in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes content properties associated with this database in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.

        Returns:
            Any: Returned if the requested database is returned.

        Tags:
            Database
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/databases/{id}"
        query_params = {
            k: v
            for k, v in [
                ("include-collaborators", include_collaborators),
                ("include-direct-children", include_direct_children),
                ("include-operations", include_operations),
                ("include-properties", include_properties),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_database(self, id) -> Any:
        """
        Deletes a database identified by its ID using the DELETE method, returning a success status of 204 if successful, or error statuses for unauthorized access, invalid requests, or if the database is not found.

        Args:
            id (string): id

        Returns:
            Any: Returned if the database was successfully deleted.

        Tags:
            Database
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/databases/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_database_content_properties(
        self, id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves the properties (columns) of a Notion database identified by its ID, supporting pagination and sorting via query parameters.

        Args:
            id (string): id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/databases/{id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_database_property(self, id, key=None, value=None) -> dict[str, Any]:
        """
        Creates a new property in a database using the specified database ID and returns the result.

        Args:
            id (string): id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/databases/{id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_database_content_properties_by_id(
        self, database_id, property_id
    ) -> dict[str, Any]:
        """
        Retrieves specific property details from a designated database using the provided database and property identifiers.

        Args:
            database_id (string): database-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if database_id is None:
            raise ValueError("Missing required parameter 'database-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/databases/{database_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_database_property_by_id(
        self, database_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates a specific property in a database by providing the database ID and property ID, using the PUT method to modify its schema or settings.

        Args:
            database_id (string): database-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if database_id is None:
            raise ValueError("Missing required parameter 'database-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/databases/{database_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_database_property_by_id(self, database_id, property_id) -> Any:
        """
        Removes a specified property from a database and returns a confirmation response upon success.

        Args:
            database_id (string): database-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if database_id is None:
            raise ValueError("Missing required parameter 'database-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/databases/{database_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_database_operations(self, id) -> dict[str, Any]:
        """
        Retrieves and performs operations on a specific database by its identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/databases/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_database_ancestors(self, id, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of ancestors for a database specified by its ID, returning them in top-to-bottom order, with optional filtering by a limit parameter.

        Args:
            id (string): id
            limit (integer): Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested ancestors are returned.

        Tags:
            Ancestors
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/databases/{id}/ancestors"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_smart_link(
        self, spaceId, title=None, parentId=None, embedUrl=None
    ) -> Any:
        """
        Creates or processes embedded content via the API and returns a status or the created resource.

        Args:
            spaceId (string): ID of the space.
            title (string): Title of the Smart Link in the content tree.
            parentId (string): The parent content ID of the Smart Link in the content tree.
            embedUrl (string): The URL that the Smart Link in the content tree should be populated with.

        Returns:
            Any: Returned if the Smart Link was successfully created in the content tree.

        Tags:
            Smart Link
        """
        request_body = {
            "spaceId": spaceId,
            "title": title,
            "parentId": parentId,
            "embedUrl": embedUrl,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/embeds"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_smart_link_by_id(
        self,
        id,
        include_collaborators=None,
        include_direct_children=None,
        include_operations=None,
        include_properties=None,
    ) -> Any:
        """
        Retrieves an embed with the specified ID and optionally includes collaborators, direct children, operations, and properties based on query parameters.

        Args:
            id (string): id
            include_collaborators (boolean): Includes collaborators on the Smart Link.
            include_direct_children (boolean): Includes direct children of the Smart Link.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this Smart Link in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes content properties associated with this Smart Link in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.

        Returns:
            Any: Returned if the requested Smart Link in the content tree is returned.

        Tags:
            Smart Link
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/embeds/{id}"
        query_params = {
            k: v
            for k, v in [
                ("include-collaborators", include_collaborators),
                ("include-direct-children", include_direct_children),
                ("include-operations", include_operations),
                ("include-properties", include_properties),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_smart_link(self, id) -> Any:
        """
        Deletes an embed resource by ID and returns a success status upon removal.

        Args:
            id (string): id

        Returns:
            Any: Returned if the Smart Link in the content tree was successfully deleted.

        Tags:
            Smart Link
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/embeds/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_smart_link_content_properties(
        self, id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves properties for an embed with the specified ID, allowing optional filtering by key, sorting, and pagination using query parameters.

        Args:
            id (string): id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/embeds/{id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_smart_link_property(self, id, key=None, value=None) -> dict[str, Any]:
        """
        Creates or updates properties for a specific embed using the embed ID and returns the operation status.

        Args:
            id (string): id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/embeds/{id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_smart_link_content_properties_by_id(
        self, embed_id, property_id
    ) -> dict[str, Any]:
        """
        Retrieves the properties of a specific embed using its embed ID and property ID.

        Args:
            embed_id (string): embed-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if embed_id is None:
            raise ValueError("Missing required parameter 'embed-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/embeds/{embed_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_smart_link_property_by_id(
        self, embed_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates a specific property of an embed using the provided embed ID and property ID.

        Args:
            embed_id (string): embed-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if embed_id is None:
            raise ValueError("Missing required parameter 'embed-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/embeds/{embed_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_smart_link_property_by_id(self, embed_id, property_id) -> Any:
        """
        Deletes a specific property from an embed identified by embed-id and property-id.

        Args:
            embed_id (string): embed-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if embed_id is None:
            raise ValueError("Missing required parameter 'embed-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/embeds/{embed_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_smart_link_operations(self, id) -> dict[str, Any]:
        """
        Retrieves the operations associated with a specific embed identified by {id}.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/embeds/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_smart_link_ancestors(self, id, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of ancestors associated with a specified embed ID using a path parameter and an optional query limit.

        Args:
            id (string): id
            limit (integer): Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested ancestors are returned.

        Tags:
            Ancestors
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/embeds/{id}/ancestors"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_folder(self, spaceId, title=None, parentId=None) -> Any:
        """
        Creates a new folder within a specified parent folder using the POST method and returns details of the newly created folder.

        Args:
            spaceId (string): ID of the space.
            title (string): Title of the folder.
            parentId (string): The parent content ID of the folder.

        Returns:
            Any: Returned if the folder was successfully created in the content tree.

        Tags:
            Folder
        """
        request_body = {
            "spaceId": spaceId,
            "title": title,
            "parentId": parentId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/folders"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_folder_by_id(
        self,
        id,
        include_collaborators=None,
        include_direct_children=None,
        include_operations=None,
        include_properties=None,
    ) -> Any:
        """
        Retrieves a specific folder's details including its collaborators, direct children, operations, and properties based on the provided ID.

        Args:
            id (string): id
            include_collaborators (boolean): Includes collaborators on the folder.
            include_direct_children (boolean): Includes direct children of the folder.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this folder in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes content properties associated with this folder in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.

        Returns:
            Any: Returned if the requested folder is returned.

        Tags:
            Folder
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/folders/{id}"
        query_params = {
            k: v
            for k, v in [
                ("include-collaborators", include_collaborators),
                ("include-direct-children", include_direct_children),
                ("include-operations", include_operations),
                ("include-properties", include_properties),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_folder(self, id) -> Any:
        """
        Deletes a folder by its ID using the DELETE method, returning a 204 status code upon successful removal.

        Args:
            id (string): id

        Returns:
            Any: Returned if the folder was successfully deleted.

        Tags:
            Folder
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/folders/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_folder_content_properties(
        self, id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves properties for a folder identified by the provided ID, allowing filtering by key and optional sorting, pagination, and limiting of results.

        Args:
            id (string): id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/folders/{id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_folder_property(self, id, key=None, value=None) -> dict[str, Any]:
        """
        Creates and updates properties for a specific folder identified by `{id}` using the "POST" method.

        Args:
            id (string): id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/folders/{id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_folder_content_properties_by_id(
        self, folder_id, property_id
    ) -> dict[str, Any]:
        """
        Retrieves a specific property associated with a folder using the folder ID and property ID.

        Args:
            folder_id (string): folder-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/folders/{folder_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_folder_property_by_id(
        self, folder_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates a specific property of a folder by ID using the specified property identifier.

        Args:
            folder_id (string): folder-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/folders/{folder_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_folder_property_by_id(self, folder_id, property_id) -> Any:
        """
        Deletes a specific property from a folder using the "DELETE" method by providing the folder ID and property ID in the request path.

        Args:
            folder_id (string): folder-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if folder_id is None:
            raise ValueError("Missing required parameter 'folder-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/folders/{folder_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_folder_operations(self, id) -> dict[str, Any]:
        """
        Retrieves a list of available operations for a specific folder identified by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/folders/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_folder_ancestors(self, id, limit=None) -> dict[str, Any]:
        """
        Retrieves a flat list of a folder's ancestors starting from its parent up to the root folder.

        Args:
            id (string): id
            limit (integer): Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested ancestors are returned.

        Tags:
            Ancestors
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/folders/{id}/ancestors"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_version_details(self, page_id, version_number) -> dict[str, Any]:
        """
        Retrieves a specific version of a page using the provided page ID and version number.

        Args:
            page_id (string): page-id
            version_number (string): version-number

        Returns:
            dict[str, Any]: Returned if the requested version details are successfully retrieved.

        Tags:
            Version
        """
        if page_id is None:
            raise ValueError("Missing required parameter 'page-id'")
        if version_number is None:
            raise ValueError("Missing required parameter 'version-number'")
        url = f"{self.base_url}/pages/{page_id}/versions/{version_number}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_versions(
        self, custom_content_id, body_format=None, cursor=None, limit=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of versions for a specific custom content item, supporting filtering, sorting, and format customization.

        Args:
            custom_content_id (string): custom-content-id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field. Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the requested custom content versions are returned.

        Tags:
            Version
        """
        if custom_content_id is None:
            raise ValueError("Missing required parameter 'custom-content-id'")
        url = f"{self.base_url}/custom-content/{custom_content_id}/versions"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_version_details(
        self, custom_content_id, version_number
    ) -> dict[str, Any]:
        """
        Retrieves a specific version of custom content by its ID and version number using the "GET" method.

        Args:
            custom_content_id (string): custom-content-id
            version_number (string): version-number

        Returns:
            dict[str, Any]: Returned if the requested version details are successfully retrieved.

        Tags:
            Version
        """
        if custom_content_id is None:
            raise ValueError("Missing required parameter 'custom-content-id'")
        if version_number is None:
            raise ValueError("Missing required parameter 'version-number'")
        url = f"{self.base_url}/custom-content/{custom_content_id}/versions/{version_number}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_spaces(
        self,
        ids=None,
        keys=None,
        type=None,
        status=None,
        labels=None,
        favorited_by=None,
        not_favorited_by=None,
        sort=None,
        description_format=None,
        include_icon=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of spaces filtered by criteria such as IDs, keys, type, status, labels, favorited status, and pagination parameters.

        Args:
            ids (array): Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list.
            keys (array): Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list.
            type (string): Filter the results to spaces based on their type.
            status (string): Filter the results to spaces based on their status.
            labels (array): Filter the results to spaces based on their labels. Multiple labels can be specified as a comma-separated list.
            favorited_by (string): Filter the results to spaces favorited by the user with the specified account ID.
            not_favorited_by (string): Filter the results to spaces NOT favorited by the user with the specified account ID.
            sort (string): Used to sort the result by a particular field.
            description_format (string): The content format type to be returned in the `description` field of the response. If available, the representation will be available under a response field of the same name under the `description` field.
            include_icon (boolean): If the icon for the space should be fetched or not.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of spaces per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested spaces are returned.

        Tags:
            Space
        """
        url = f"{self.base_url}/spaces"
        query_params = {
            k: v
            for k, v in [
                ("ids", ids),
                ("keys", keys),
                ("type", type),
                ("status", status),
                ("labels", labels),
                ("favorited-by", favorited_by),
                ("not-favorited-by", not_favorited_by),
                ("sort", sort),
                ("description-format", description_format),
                ("include-icon", include_icon),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_space(
        self, name, key=None, alias=None, description=None, roleAssignments=None
    ) -> Any:
        """
        Creates a new space resource and returns a success response upon creation.

        Args:
            name (string): The name of the space to be created.
            key (string): The key for the new space. See [Space Keys](https://support.atlassian.com/confluence-cloud/docs/create-a-space/). If the key property is not provided, the alias property is required to be used instead.
            alias (string): This field will be used as the new identifier for the space in confluence page URLs. If the alias property is not provided, the key property is required to be used instead. Maximum 255 alphanumeric characters in length.
            description (object): The description of the new/updated space. Note, only the 'plain' representation is currently supported.
            roleAssignments (object): The role assignments for the new space. If none are provided, the Default Space Roles are applied. If roles are provided, the space is created with exactly the provided set of roles. A private space is created if only the creator is assigned to a role and it's the Admin role. At least one Admin role assignment must be specified.

        Returns:
            Any: Returned if the requested space is created.

        Tags:
            Space, EAP
        """
        self._ensure_base_url_set()
        request_body = {
            "name": name,
            "key": key,
            "alias": alias,
            "description": description,
            "roleAssignments": roleAssignments,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/spaces"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_by_id(
        self,
        id,
        description_format=None,
        include_icon=None,
        include_operations=None,
        include_properties=None,
        include_permissions=None,
        include_role_assignments=None,
        include_labels=None,
    ) -> Any:
        """
        Retrieves a space's details by its ID, optionally including descriptions, icons, operations, properties, permissions, role assignments, and labels based on query parameters.

        Args:
            id (string): id
            description_format (string): The content format type to be returned in the `description` field of the response. If available, the representation will be available under a response field of the same name under the `description` field.
            include_icon (boolean): If the icon for the space should be fetched or not.
            include_operations (boolean): Includes operations associated with this space in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_properties (boolean): Includes space properties associated with this space in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_permissions (boolean): Includes space permissions associated with this space in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_role_assignments (boolean): Includes role assignments associated with this space in the response. This parameter is only accepted for EAP sites.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_labels (boolean): Includes labels associated with this space in the response.
        The number of results will be limited to 50 and sorted in the default sort order.
        A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.

        Returns:
            Any: Returned if the requested space is returned.

        Tags:
            Space
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}"
        query_params = {
            k: v
            for k, v in [
                ("description-format", description_format),
                ("include-icon", include_icon),
                ("include-operations", include_operations),
                ("include-properties", include_properties),
                ("include-permissions", include_permissions),
                ("include-role-assignments", include_role_assignments),
                ("include-labels", include_labels),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_posts_in_space(
        self,
        id,
        sort=None,
        status=None,
        title=None,
        body_format=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of blog posts associated with a specific space, allowing filtering by status, title, and sorting options.

        Args:
            id (string): id
            sort (string): Used to sort the result by a particular field.
            status (array): Filter the results to blog posts based on their status. By default, `current` is used.
            title (string): Filter the results to blog posts based on their title.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of blog posts per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested blog posts are returned.

        Tags:
            Blog Post
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/blogposts"
        query_params = {
            k: v
            for k, v in [
                ("sort", sort),
                ("status", status),
                ("title", title),
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_labels(
        self, id, prefix=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of labels for a specific space identified by its ID, allowing optional filtering by prefix, sorting, and pagination using query parameters.

        Args:
            id (string): id
            prefix (string): Filter the results to labels based on their prefix.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested labels are returned.

        Tags:
            Label
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/labels"
        query_params = {
            k: v
            for k, v in [
                ("prefix", prefix),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_content_labels(
        self, id, prefix=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of content labels for a specific space using the provided ID, with optional filtering by prefix, sorting, and pagination.

        Args:
            id (string): id
            prefix (string): Filter the results to labels based on their prefix.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested labels are returned.

        Tags:
            Label
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/content/labels"
        query_params = {
            k: v
            for k, v in [
                ("prefix", prefix),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_content_by_type_in_space(
        self, id, type, cursor=None, limit=None, body_format=None
    ) -> dict[str, Any]:
        """
        Retrieves custom content for a specific space, allowing users to filter by type, cursor, and limit, with options for different body formats.

        Args:
            id (string): id
            type (string): The type of custom content being requested. See: for additional details on custom content.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field. Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.

        Returns:
            dict[str, Any]: Returned if the requested custom content is returned.

        Tags:
            Custom Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/custom-content"
        query_params = {
            k: v
            for k, v in [
                ("type", type),
                ("cursor", cursor),
                ("limit", limit),
                ("body-format", body_format),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_operations(self, id) -> dict[str, Any]:
        """
        Retrieves a list of operations for a specific space identified by the given ID using the provided API endpoint.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_pages_in_space(
        self,
        id,
        depth=None,
        sort=None,
        status=None,
        title=None,
        body_format=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of pages for a specified space, allowing filtering by depth, sort order, status, title, body format, and pagination controls.

        Args:
            id (string): id
            depth (string): Filter the results to pages at the root level of the space or to all pages in the space.
            sort (string): Used to sort the result by a particular field.
            status (array): Filter the results to pages based on their status. By default, `current` and `archived` are used.
            title (string): Filter the results to pages based on their title.
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested pages are returned.

        Tags:
            Page
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/pages"
        query_params = {
            k: v
            for k, v in [
                ("depth", depth),
                ("sort", sort),
                ("status", status),
                ("title", title),
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_properties(
        self, space_id, key=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of properties for a specified space, optionally filtered by key, with pagination support via cursor and limit parameters.

        Args:
            space_id (string): space-id
            key (string): The key of the space property to retrieve. This should be used when a user knows the key of their property, but needs to retrieve the id for use in other methods.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested space properties are returned. `results` may be empty if no results were found.

        Tags:
            Space Properties
        """
        if space_id is None:
            raise ValueError("Missing required parameter 'space-id'")
        url = f"{self.base_url}/spaces/{space_id}/properties"
        query_params = {
            k: v
            for k, v in [("key", key), ("cursor", cursor), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_space_property(self, space_id, key=None, value=None) -> dict[str, Any]:
        """
        Creates a new property for a specified space using the "POST" method, where the space is identified by the `{space-id}` path parameter.

        Args:
            space_id (string): space-id
            key (string): Key of the space property
            value (string): Value of the space property.

        Returns:
            dict[str, Any]: Returned if the space property was created successfully.

        Tags:
            Space Properties
        """
        if space_id is None:
            raise ValueError("Missing required parameter 'space-id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/spaces/{space_id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_property_by_id(self, space_id, property_id) -> dict[str, Any]:
        """
        Retrieves the specified property details for a space using the provided space and property identifiers.

        Args:
            space_id (string): space-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the space property was retrieved.

        Tags:
            Space Properties
        """
        if space_id is None:
            raise ValueError("Missing required parameter 'space-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/spaces/{space_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_space_property_by_id(
        self, space_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates the specified property within a designated space and returns a success status upon completion.

        Args:
            space_id (string): space-id
            property_id (string): property-id
            key (string): Key of the space property
            value (string): Value of the space property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the space property was updated successfully.

        Tags:
            Space Properties
        """
        if space_id is None:
            raise ValueError("Missing required parameter 'space-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/spaces/{space_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_space_property_by_id(self, space_id, property_id) -> Any:
        """
        Deletes a property from a specified space using the provided space ID and property ID.

        Args:
            space_id (string): space-id
            property_id (string): property-id

        Returns:
            Any: Returned if the space property was deleted successfully.

        Tags:
            Space Properties
        """
        if space_id is None:
            raise ValueError("Missing required parameter 'space-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/spaces/{space_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_permissions_assignments(
        self, id, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves the list of permissions assigned to a specific space, supporting pagination via cursor and limit parameters.

        Args:
            id (string): id
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of assignments to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested assignments are returned.

        Tags:
            Space Permissions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/permissions"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_available_space_permissions(
        self, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves space permissions with pagination support using cursor and limit parameters.

        Args:
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of space permissions to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested space permissions are retrieved.

        Tags:
            Space Permissions, EAP
        """
        url = f"{self.base_url}/space-permissions"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_available_space_roles(
        self,
        space_id=None,
        role_type=None,
        principal_id=None,
        principal_type=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of space roles, filtered by space ID, role type, principal ID, and principal type, with options for pagination using a cursor and limit, returning relevant space role information.

        Args:
            space_id (string): The space ID for which to filter available space roles; if empty, return all available space roles for the tenant.
            role_type (string): The space role type to filter results by.
            principal_id (string): The principal ID to filter results by. If specified, a principal-type must also be specified. Paired with a `principal-type` of `ACCESS_CLASS`, valid values include [`anonymous-users`, `jsm-project-admins`, `authenticated-users`, `all-licensed-users`, `all-product-admins`]
            principal_type (string): The principal type to filter results by. If specified, a principal-id must also be specified.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of space roles to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested space roles are retrieved.

        Tags:
            Space Roles, EAP
        """
        url = f"{self.base_url}/space-roles"
        query_params = {
            k: v
            for k, v in [
                ("space-id", space_id),
                ("role-type", role_type),
                ("principal-id", principal_id),
                ("principal-type", principal_type),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_roles_by_id(self, id) -> Any:
        """
        Retrieves space role assignments for a specified space ID, returning role-based permissions and user access details.

        Args:
            id (string): id

        Returns:
            Any: Returned if the requested space role is retrieved.

        Tags:
            Space Roles, EAP
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/space-roles/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_role_assignments(
        self,
        id,
        role_id=None,
        role_type=None,
        principal_id=None,
        principal_type=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves role assignments for a specific space with optional filtering by role type, role ID, principal type, principal ID, and pagination controls.

        Args:
            id (string): id
            role_id (string): Filters the returned role assignments to the provided role ID.
            role_type (string): Filters the returned role assignments to the provided role type.
            principal_id (string): Filters the returned role assignments to the provided principal id. If specified, a principal-type must also be specified. Paired with a `principal-type` of `ACCESS_CLASS`, valid values include [`anonymous-users`, `jsm-project-admins`, `authenticated-users`, `all-licensed-users`, `all-product-admins`]
            principal_type (string): Filters the returned role assignments to the provided principal type. If specified, a principal-id must also be specified.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of space roles to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested space role assignments are retrieved.

        Tags:
            Space Roles, EAP
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/role-assignments"
        query_params = {
            k: v
            for k, v in [
                ("role-id", role_id),
                ("role-type", role_type),
                ("principal-id", principal_id),
                ("principal-type", principal_type),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_space_role_assignments(self, id, principal, roleId=None) -> dict[str, Any]:
        """
        Assigns a role to a specific space identified by the path parameter ID and returns the assignment status.

        Args:
            id (string): id
            principal (object): The principal of the role assignment.
            roleId (string): The role to which the principal is assigned.

        Returns:
            dict[str, Any]: Returned if the requested update to space role assignments succeeds in its entirety.

        Tags:
            Space Roles, EAP
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "principal": principal,
            "roleId": roleId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/spaces/{id}/role-assignments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_footer_comments(
        self, id, body_format=None, status=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves comments from the footer section of a specific page identified by its ID, allowing for optional filtering by body format, status, sorting, cursor, and limit.

        Args:
            id (string): id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            status (array): Filter the footer comment being retrieved by its status.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested footer comments are returned.

        Tags:
            Comment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/footer-comments"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("status", status),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_inline_comments(
        self,
        id,
        body_format=None,
        status=None,
        resolution_status=None,
        sort=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of inline comments for a specific page, allowing customization by body format, status, resolution status, sorting, cursor, and limit, using the API at "/pages/{id}/inline-comments" via the GET method.

        Args:
            id (string): id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            status (array): Filter the inline comment being retrieved by its status.
            resolution_status (array): Filter the inline comment being retrieved by its resolution status.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of inline comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested inline comments are returned.

        Tags:
            Comment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/inline-comments"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("status", status),
                ("resolution-status", resolution_status),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_footer_comments(
        self, id, body_format=None, status=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves comments from the footer section of a specific blog post using the "GET" method, allowing for customizable output format and sorting options based on query parameters.

        Args:
            id (string): id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            status (array): Filter the footer comment being retrieved by its status.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested footer comments are returned.

        Tags:
            Comment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/footer-comments"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("status", status),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_inline_comments(
        self,
        id,
        body_format=None,
        status=None,
        resolution_status=None,
        sort=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of inline comments associated with a specific blog post using the provided parameters for filtering and sorting.

        Args:
            id (string): id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            status (array): Filter the inline comment being retrieved by its status.
            resolution_status (array): Filter the inline comment being retrieved by its resolution status.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of inline comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested inline comments are returned.

        Tags:
            Comment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/inline-comments"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("status", status),
                ("resolution-status", resolution_status),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_footer_comments(
        self, body_format=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of comments for the footer, allowing customization through query parameters for body format, sorting, pagination with a cursor, and limiting the number of results.

        Args:
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested footer comments are returned.

        Tags:
            Comment
        """
        url = f"{self.base_url}/footer-comments"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_footer_comment(
        self,
        blogPostId=None,
        pageId=None,
        parentCommentId=None,
        attachmentId=None,
        customContentId=None,
        body=None,
    ) -> Any:
        """
        Creates a new footer comment entry and returns a success status upon creation.

        Args:
            blogPostId (string): ID of the containing blog post, if intending to create a top level footer comment. Do not provide if creating a reply.
            pageId (string): ID of the containing page, if intending to create a top level footer comment. Do not provide if creating a reply.
            parentCommentId (string): ID of the parent comment, if intending to create a reply. Do not provide if creating a top level comment.
            attachmentId (string): ID of the attachment, if intending to create a comment against an attachment.
            customContentId (string): ID of the custom content, if intending to create a comment against a custom content.
            body (string): body

        Returns:
            Any: Returned if the footer comment is created.

        Tags:
            Comment
        """
        request_body = {
            "blogPostId": blogPostId,
            "pageId": pageId,
            "parentCommentId": parentCommentId,
            "attachmentId": attachmentId,
            "customContentId": customContentId,
            "body": body,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/footer-comments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_footer_comment_by_id(
        self,
        comment_id,
        body_format=None,
        version=None,
        include_properties=None,
        include_operations=None,
        include_likes=None,
        include_versions=None,
        include_version=None,
    ) -> Any:
        """
        Retrieves information about a specific footer comment using the comment ID, with optional configurations for formatting and included metadata.

        Args:
            comment_id (string): comment-id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            version (integer): Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
            include_properties (boolean): Includes content properties associated with this footer comment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this footer comment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_likes (boolean): Includes likes associated with this footer comment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_versions (boolean): Includes versions associated with this footer comment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_version (boolean): Includes the current version associated with this footer comment in the response.
        By default this is included and can be omitted by setting the value to `false`.

        Returns:
            Any: Returned if the footer comment is successfully retrieved.

        Tags:
            Comment
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        url = f"{self.base_url}/footer-comments/{comment_id}"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("version", version),
                ("include-properties", include_properties),
                ("include-operations", include_operations),
                ("include-likes", include_likes),
                ("include-versions", include_versions),
                ("include-version", include_version),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_footer_comment(
        self, comment_id, version=None, body=None, alinks=None
    ) -> dict[str, Any]:
        """
        Updates a Confluence footer comment's content and returns a success response.

        Args:
            comment_id (string): comment-id
            version (object): version
            body (string): body
            _links (object): _links

        Returns:
            dict[str, Any]: Returned if the footer comment is updated successfully

        Tags:
            Comment
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        request_body = {
            "version": version,
            "body": body,
            "links": alinks,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/footer-comments/{comment_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_footer_comment(self, comment_id) -> Any:
        """
        Deletes a specific footer comment identified by its ID using the DELETE method, returning a 204 status code upon successful deletion.

        Args:
            comment_id (string): comment-id

        Returns:
            Any: Returned if the footer comment is deleted.

        Tags:
            Comment
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        url = f"{self.base_url}/footer-comments/{comment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_footer_comment_children(
        self, id, body_format=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves child comments for a specific footer comment with optional filtering, sorting, and pagination parameters.

        Args:
            id (string): id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested footer comments are returned.

        Tags:
            Comment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/footer-comments/{id}/children"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_footer_like_count(self, id) -> dict[str, Any]:
        """
        Retrieves the count of likes for a specific footer comment using the "GET" method at the "/footer-comments/{id}/likes/count" endpoint.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested count is returned.

        Tags:
            Like
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/footer-comments/{id}/likes/count"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_footer_like_users(self, id, cursor=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of users who have liked a specific comment with the given ID using the GET method, allowing for pagination through cursor and limit parameters.

        Args:
            id (string): id
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested account IDs are returned.

        Tags:
            Like
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/footer-comments/{id}/likes/users"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_footer_comment_operations(self, id) -> dict[str, Any]:
        """
        Retrieves the operations for a specific footer comment identified by the provided ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/footer-comments/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_footer_comment_versions(
        self, id, body_format=None, cursor=None, limit=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves and lists versions of a specific comment identified by `{id}` in the footer, allowing customization through query parameters such as format, sorting, and pagination.

        Args:
            id (string): id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the requested footer comment versions are returned.

        Tags:
            Version
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/footer-comments/{id}/versions"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_footer_comment_version_details(self, id, version_number) -> dict[str, Any]:
        """
        Retrieves a specific version of a footer comment by its ID and version number.

        Args:
            id (string): id
            version_number (string): version-number

        Returns:
            dict[str, Any]: Returned if the requested version details are successfully retrieved.

        Tags:
            Version
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if version_number is None:
            raise ValueError("Missing required parameter 'version-number'")
        url = f"{self.base_url}/footer-comments/{id}/versions/{version_number}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_inline_comments(
        self, body_format=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of inline comments with optional parameters for body formatting, sorting, pagination (cursor), and result limit.

        Args:
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested inline comments are returned.

        Tags:
            Comment
        """
        url = f"{self.base_url}/inline-comments"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_inline_comment(
        self,
        blogPostId=None,
        pageId=None,
        parentCommentId=None,
        body=None,
        inlineCommentProperties=None,
    ) -> Any:
        """
        Creates inline comments on a specified line of a pull request file using the GitHub API and returns the created comment.

        Args:
            blogPostId (string): ID of the containing blog post, if intending to create a top level footer comment. Do not provide if creating a reply.
            pageId (string): ID of the containing page, if intending to create a top level footer comment. Do not provide if creating a reply.
            parentCommentId (string): ID of the parent comment, if intending to create a reply. Do not provide if creating a top level comment.
            body (string): body
            inlineCommentProperties (object): Object describing the text to highlight on the page/blog post. Only applicable for top level inline comments (not replies) and required in that case.

        Returns:
            Any: Returned if the inline comment is created.

        Tags:
            Comment
        """
        request_body = {
            "blogPostId": blogPostId,
            "pageId": pageId,
            "parentCommentId": parentCommentId,
            "body": body,
            "inlineCommentProperties": inlineCommentProperties,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/inline-comments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_inline_comment_by_id(
        self,
        comment_id,
        body_format=None,
        version=None,
        include_properties=None,
        include_operations=None,
        include_likes=None,
        include_versions=None,
        include_version=None,
    ) -> Any:
        """
        Retrieves the specified inline comment by ID, optionally including formatted content and associated metadata.

        Args:
            comment_id (string): comment-id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            version (integer): Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
            include_properties (boolean): Includes content properties associated with this inline comment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_operations (boolean): Includes operations associated with this inline comment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_likes (boolean): Includes likes associated with this inline comment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_versions (boolean): Includes versions associated with this inline comment in the response.
        The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.
            include_version (boolean): Includes the current version associated with this inline comment in the response.
        By default this is included and can be omitted by setting the value to `false`.

        Returns:
            Any: Returned if the inline comment is successfully retrieved.

        Tags:
            Comment
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        url = f"{self.base_url}/inline-comments/{comment_id}"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("version", version),
                ("include-properties", include_properties),
                ("include-operations", include_operations),
                ("include-likes", include_likes),
                ("include-versions", include_versions),
                ("include-version", include_version),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_inline_comment(
        self, comment_id, version=None, body=None, resolved=None
    ) -> Any:
        """
        Updates an inline comment's content in a version control system using the specified comment identifier.

        Args:
            comment_id (string): comment-id
            version (object): version
            body (string): body
            resolved (boolean): Resolved state of the comment. Set to true to resolve the comment, set to false to reopen it. If
        matching the existing state (i.e. true -> resolved or false -> open/reopened) , no change will occur. A dangling
        comment cannot be updated.

        Returns:
            Any: Returned if the inline comment is updated successfully.

        Tags:
            Comment
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        request_body = {
            "version": version,
            "body": body,
            "resolved": resolved,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/inline-comments/{comment_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_inline_comment(self, comment_id) -> Any:
        """
        Deletes an inline comment specified by its ID using the DELETE method and returns a successful status upon completion.

        Args:
            comment_id (string): comment-id

        Returns:
            Any: Returned if the inline comment is deleted.

        Tags:
            Comment
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        url = f"{self.base_url}/inline-comments/{comment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_inline_comment_children(
        self, id, body_format=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of child comments for a specific inline comment, supporting query parameters for formatting, sorting, and pagination.

        Args:
            id (string): id
            body_format (string): The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested footer comments are returned.

        Tags:
            Comment
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/inline-comments/{id}/children"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_inline_like_count(self, id) -> dict[str, Any]:
        """
        Retrieves the total number of likes for a specific inline comment using the API endpoint "/inline-comments/{id}/likes/count" via the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested count is returned.

        Tags:
            Like
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/inline-comments/{id}/likes/count"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_inline_like_users(self, id, cursor=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of users who have liked an inline comment with the specified ID, with optional pagination using cursor and limit parameters.

        Args:
            id (string): id
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested account IDs are returned.

        Tags:
            Like
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/inline-comments/{id}/likes/users"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_inline_comment_operations(self, id) -> dict[str, Any]:
        """
        Retrieves an inline comment by ID from a GitHub repository using the GitHub API.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested operations are returned.

        Tags:
            Operation
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/inline-comments/{id}/operations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_inline_comment_versions(
        self, id, body_format=None, cursor=None, limit=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves version history for a specific inline comment, supporting pagination and body formatting options.

        Args:
            id (string): id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the requested inline comment versions are returned.

        Tags:
            Version
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/inline-comments/{id}/versions"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("cursor", cursor),
                ("limit", limit),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_inline_comment_version_details(self, id, version_number) -> dict[str, Any]:
        """
        Retrieves a specific version of an inline comment by its ID and version number using the GET method.

        Args:
            id (string): id
            version_number (string): version-number

        Returns:
            dict[str, Any]: Returned if the requested version details are successfully retrieved.

        Tags:
            Version
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if version_number is None:
            raise ValueError("Missing required parameter 'version-number'")
        url = f"{self.base_url}/inline-comments/{id}/versions/{version_number}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_comment_content_properties(
        self, comment_id, key=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves specific properties of a comment using its ID, optionally filtered by key, sorted, and paginated.

        Args:
            comment_id (string): comment-id
            key (string): Filters the response to return a specific content property with matching key (case sensitive).
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested content properties are successfully retrieved.

        Tags:
            Content Properties
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        url = f"{self.base_url}/comments/{comment_id}/properties"
        query_params = {
            k: v
            for k, v in [
                ("key", key),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_comment_property(
        self, comment_id, key=None, value=None
    ) -> dict[str, Any]:
        """
        Updates properties of a comment identified by the given "comment-id" using the specified API.

        Args:
            comment_id (string): comment-id
            key (string): Key of the content property
            value (string): Value of the content property.

        Returns:
            dict[str, Any]: Returned if the content property was created successfully.

        Tags:
            Content Properties
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        request_body = {
            "key": key,
            "value": value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/comments/{comment_id}/properties"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_comment_content_properties_by_id(
        self, comment_id, property_id
    ) -> dict[str, Any]:
        """
        Retrieves the specified property of a comment using the provided comment ID and property ID.

        Args:
            comment_id (string): comment-id
            property_id (string): property-id

        Returns:
            dict[str, Any]: Returned if the requested content property is successfully retrieved.

        Tags:
            Content Properties
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/comments/{comment_id}/properties/{property_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_comment_property_by_id(
        self, comment_id, property_id, key=None, value=None, version=None
    ) -> dict[str, Any]:
        """
        Updates the specified property of a comment using the provided path parameters and returns a status message.

        Args:
            comment_id (string): comment-id
            property_id (string): property-id
            key (string): Key of the content property
            value (string): Value of the content property.
            version (object): New version number and associated message

        Returns:
            dict[str, Any]: Returned if the content property was updated successfully.

        Tags:
            Content Properties
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        request_body = {
            "key": key,
            "value": value,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/comments/{comment_id}/properties/{property_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_comment_property_by_id(self, comment_id, property_id) -> Any:
        """
        Deletes a specific property from a comment using the provided `comment-id` and `property-id`, returning a status code upon successful deletion.

        Args:
            comment_id (string): comment-id
            property_id (string): property-id

        Returns:
            Any: Returned if the content property was deleted successfully.

        Tags:
            Content Properties
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment-id'")
        if property_id is None:
            raise ValueError("Missing required parameter 'property-id'")
        url = f"{self.base_url}/comments/{comment_id}/properties/{property_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks(
        self,
        body_format=None,
        include_blank_tasks=None,
        status=None,
        task_id=None,
        space_id=None,
        page_id=None,
        blogpost_id=None,
        created_by=None,
        assigned_to=None,
        completed_by=None,
        created_at_from=None,
        created_at_to=None,
        due_at_from=None,
        due_at_to=None,
        completed_at_from=None,
        completed_at_to=None,
        cursor=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Retrieves a filtered list of tasks from a specified space, page, or blog post, allowing filtering by status, assignment, creation/due dates, and other criteria.

        Args:
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.
            include_blank_tasks (boolean): Specifies whether to include blank tasks in the response. Defaults to `true`.
            status (string): Filters on the status of the task.
            task_id (array): Filters on task ID. Multiple IDs can be specified.
            space_id (array): Filters on the space ID of the task. Multiple IDs can be specified.
            page_id (array): Filters on the page ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction.
            blogpost_id (array): Filters on the blog post ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction.
            created_by (array): Filters on the Account ID of the user who created this task. Multiple IDs can be specified.
            assigned_to (array): Filters on the Account ID of the user to whom this task is assigned. Multiple IDs can be specified.
            completed_by (array): Filters on the Account ID of the user who completed this task. Multiple IDs can be specified.
            created_at_from (integer): Filters on start of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds.
            created_at_to (integer): Filters on end of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds.
            due_at_from (integer): Filters on start of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds.
            due_at_to (integer): Filters on end of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds.
            completed_at_from (integer): Filters on start of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds.
            completed_at_to (integer): Filters on end of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of tasks per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested tasks are returned.

        Tags:
            Task
        """
        url = f"{self.base_url}/tasks"
        query_params = {
            k: v
            for k, v in [
                ("body-format", body_format),
                ("include-blank-tasks", include_blank_tasks),
                ("status", status),
                ("task-id", task_id),
                ("space-id", space_id),
                ("page-id", page_id),
                ("blogpost-id", blogpost_id),
                ("created-by", created_by),
                ("assigned-to", assigned_to),
                ("completed-by", completed_by),
                ("created-at-from", created_at_from),
                ("created-at-to", created_at_to),
                ("due-at-from", due_at_from),
                ("due-at-to", due_at_to),
                ("completed-at-from", completed_at_from),
                ("completed-at-to", completed_at_to),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_task_by_id(self, id, body_format=None) -> dict[str, Any]:
        """
        Retrieves a specific task by ID and optionally formats the response body based on the body-format query parameter.

        Args:
            id (string): id
            body_format (string): The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.

        Returns:
            dict[str, Any]: Returned if the requested task is returned.

        Tags:
            Task
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/tasks/{id}"
        query_params = {
            k: v for k, v in [("body-format", body_format)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_child_pages(self, id, cursor=None, limit=None, sort=None) -> dict[str, Any]:
        """
        Retrieves a list of child pages for a given page, identified by the `{id}`, allowing optional filtering by cursor, limit, and sort order.

        Args:
            id (string): id
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the requested child pages are returned.

        Tags:
            Children
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/children"
        query_params = {
            k: v
            for k, v in [("cursor", cursor), ("limit", limit), ("sort", sort)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_child_custom_content(
        self, id, cursor=None, limit=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of child content items for a specified custom content item identified by `{id}`, allowing optional filtering by `cursor`, `limit`, and `sort` parameters.

        Args:
            id (string): id
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.
            sort (string): Used to sort the result by a particular field.

        Returns:
            dict[str, Any]: Returned if the requested child custom content are returned.

        Tags:
            Children
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/custom-content/{id}/children"
        query_params = {
            k: v
            for k, v in [("cursor", cursor), ("limit", limit), ("sort", sort)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_ancestors(self, id, limit=None) -> dict[str, Any]:
        """
        Retrieves the hierarchical ancestors of a specified Confluence page in top-to-bottom order, returning minimal page details with optional limit control.

        Args:
            id (string): id
            limit (integer): Maximum number of pages per result to return. If more results exist, call this endpoint with the highest ancestor's ID to fetch the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested ancestors are returned.

        Tags:
            Ancestors
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/ancestors"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_bulk_user_lookup(self, accountIds) -> dict[str, Any]:
        """
        Creates a bulk operation on user data using the POST method at the "/users-bulk" endpoint.

        Args:
            accountIds (array): List of accountIds to retrieve user info for.

        Returns:
            dict[str, Any]: Returned if the user info is returned for the account IDs. `results` may be empty if no account IDs were found.

        Tags:
            User
        """
        request_body = {
            "accountIds": accountIds,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users-bulk"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def check_access_by_email(self, emails) -> dict[str, Any]:
        """
        Checks user access by email using a POST request to the "/user/access/check-access-by-email" endpoint, returning relevant access information.

        Args:
            emails (array): List of emails to check access to site.

        Returns:
            dict[str, Any]: Returns object with list of emails without access to site.

        Tags:
            User
        """
        request_body = {
            "emails": emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/user/access/check-access-by-email"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def invite_by_email(self, emails) -> Any:
        """
        Sends an email invitation to grant user access and returns a success or error status.

        Args:
            emails (array): List of emails to check access to site.

        Returns:
            Any: Returns object with list of emails without access to site.

        Tags:
            User
        """
        request_body = {
            "emails": emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/user/access/invite-by-email"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_data_policy_metadata(self) -> dict[str, Any]:
        """
        Retrieves data policy metadata from a workspace using the Confluence Cloud REST API.

        Returns:
            dict[str, Any]: Returned if the request is successful.

        Tags:
            Data Policies
        """
        url = f"{self.base_url}/data-policies/metadata"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_data_policy_spaces(
        self, ids=None, keys=None, sort=None, cursor=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves information about data policies affecting spaces, returning details on whether content is blocked for each space specified by query parameters like `ids`, `keys`, `sort`, `cursor`, and `limit`.

        Args:
            ids (array): Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list.
            keys (array): Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list.
            sort (string): Used to sort the result by a particular field.
            cursor (string): Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.
            limit (integer): Maximum number of spaces per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.

        Returns:
            dict[str, Any]: Returned if the requested spaces are returned.

        Tags:
            Data Policies
        """
        url = f"{self.base_url}/data-policies/spaces"
        query_params = {
            k: v
            for k, v in [
                ("ids", ids),
                ("keys", keys),
                ("sort", sort),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_classification_levels(self) -> list[Any]:
        """
        Retrieves a list of classification levels using the "GET" method at the "/classification-levels" path.

        Returns:
            list[Any]: Returned if classifications levels are returned.

        Tags:
            Classification Level
        """
        url = f"{self.base_url}/classification-levels"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_space_default_classification_level(self, id) -> dict[str, Any]:
        """
        Retrieves the default classification level for a specified space using its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested default classification level for a space is returned.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/classification-level/default"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_space_default_classification_level(self, id, status) -> Any:
        """
        Updates the default classification level for a space with the specified ID using the "PUT" method via the API endpoint "/spaces/{id}/classification-level/default."

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the default classification level was successfully updated.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/spaces/{id}/classification-level/default"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_space_default_classification_level(self, id) -> Any:
        """
        Removes the default classification level from a specified space identified by its ID.

        Args:
            id (string): id

        Returns:
            Any: Returned if the default classification level was successfully deleted.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/spaces/{id}/classification-level/default"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_page_classification_level(self, id, status=None) -> dict[str, Any]:
        """
        Retrieves the classification level for a specified page using the `GET` method, accepting a page ID and an optional status query parameter.

        Args:
            id (string): id
            status (string): Status of page from which classification level will fetched.

        Returns:
            dict[str, Any]: Returned if the requested classification level for a page is returned.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pages/{id}/classification-level"
        query_params = {k: v for k, v in [("status", status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_page_classification_level(self, id, status) -> Any:
        """
        Updates the classification level of a page with the specified ID using the PUT method.

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the classification level was successfully updated.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/pages/{id}/classification-level"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_page_classification_level(self, id, status) -> Any:
        """
        Resets the classification level for a specific page to the default, removing any custom classification settings.

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the classification level was successfully reset.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/pages/{id}/classification-level/reset"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_blog_post_classification_level(self, id, status=None) -> dict[str, Any]:
        """
        Retrieves the classification level for a specific blog post identified by its ID using the GET method at the "/blogposts/{id}/classification-level" endpoint, allowing for optional filtering by status.

        Args:
            id (string): id
            status (string): Status of blog post from which classification level will fetched.

        Returns:
            dict[str, Any]: Returned if the requested classification level for a blog post is returned.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/blogposts/{id}/classification-level"
        query_params = {k: v for k, v in [("status", status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_blog_post_classification_level(self, id, status) -> Any:
        """
        Updates the classification level of the blog post with the specified ID and returns a success status upon completion.

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the classification level was successfully updated.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/blogposts/{id}/classification-level"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_blog_post_classification_level(self, id, status) -> Any:
        """
        Resets the classification level for a specific blog post to the space's default level using the Confluence REST API.

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the classification level was successfully reset.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/blogposts/{id}/classification-level/reset"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_whiteboard_classification_level(self, id) -> dict[str, Any]:
        """
        Retrieves the classification level of a specific whiteboard identified by its ID, returning relevant information if the request is successful.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested classification level for a whiteboard is returned.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/whiteboards/{id}/classification-level"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_whiteboard_classification_level(self, id, status) -> Any:
        """
        Updates the classification level for a specific whiteboard identified by its ID using the Confluence Cloud REST API.

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the classification level was successfully updated.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/whiteboards/{id}/classification-level"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_whiteboard_classification_level(self, id, status) -> Any:
        """
        Resets the classification level for a specific whiteboard to the default space classification level using the Confluence Cloud REST API.

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the classification level was successfully reset.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/whiteboards/{id}/classification-level/reset"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_database_classification_level(self, id) -> dict[str, Any]:
        """
        Retrieves the classification level of a specific database by its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Returned if the requested classification level for a database is returned.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/databases/{id}/classification-level"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_database_classification_level(self, id, status) -> Any:
        """
        Updates the classification level of a database identified by `{id}` using the PUT method.

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the classification level was successfully updated.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/databases/{id}/classification-level"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_database_classification_level(self, id, status) -> Any:
        """
        Resets the classification level for a specified database using a POST request and returns an empty response on success.

        Args:
            id (string): id
            status (string): Status of the content.

        Returns:
            Any: Returned if the classification level was successfully reset.

        Tags:
            Classification Level
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/databases/{id}/classification-level/reset"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_attachments,
            self.get_attachment_by_id,
            self.delete_attachment,
            self.get_attachment_labels,
            self.get_attachment_operations,
            self.get_attachment_content_properties,
            self.create_attachment_property,
            self.get_attachment_content_properties_by_id,
            self.update_attachment_property_by_id,
            self.delete_attachment_property_by_id,
            self.get_attachment_versions,
            self.get_attachment_version_details,
            self.get_attachment_comments,
            self.get_blog_posts,
            self.create_blog_post,
            self.get_blog_post_by_id,
            self.update_blog_post,
            self.delete_blog_post,
            self.get_blogpost_attachments,
            self.get_custom_content_by_type_in_blog_post,
            self.get_blog_post_labels,
            self.get_blog_post_like_count,
            self.get_blog_post_like_users,
            self.get_blogpost_content_properties,
            self.create_blogpost_property,
            self.get_blogpost_content_properties_by_id,
            self.update_blogpost_property_by_id,
            self.delete_blogpost_property_by_id,
            self.get_blog_post_operations,
            self.get_blog_post_versions,
            self.get_blog_post_version_details,
            self.convert_content_ids_to_content_types,
            self.get_custom_content_by_type,
            self.create_custom_content,
            self.get_custom_content_by_id,
            self.update_custom_content,
            self.delete_custom_content,
            self.get_custom_content_attachments,
            self.get_custom_content_comments,
            self.get_custom_content_labels,
            self.get_custom_content_operations,
            self.get_custom_content_content_properties,
            self.create_custom_content_property,
            self.get_custom_content_content_properties_by_id,
            self.update_custom_content_property_by_id,
            self.delete_custom_content_property_by_id,
            self.get_labels,
            self.get_label_attachments,
            self.get_label_blog_posts,
            self.get_label_pages,
            self.get_pages,
            self.create_page,
            self.get_page_by_id,
            self.update_page,
            self.delete_page,
            self.get_page_attachments,
            self.get_custom_content_by_type_in_page,
            self.get_page_labels,
            self.get_page_like_count,
            self.get_page_like_users,
            self.get_page_operations,
            self.get_page_content_properties,
            self.create_page_property,
            self.get_page_content_properties_by_id,
            self.update_page_property_by_id,
            self.delete_page_property_by_id,
            self.get_page_versions,
            self.create_whiteboard,
            self.get_whiteboard_by_id,
            self.delete_whiteboard,
            self.get_whiteboard_content_properties,
            self.create_whiteboard_property,
            self.get_whiteboard_content_properties_by_id,
            self.update_whiteboard_property_by_id,
            self.delete_whiteboard_property_by_id,
            self.get_whiteboard_operations,
            self.get_whiteboard_ancestors,
            self.create_database,
            self.get_database_by_id,
            self.delete_database,
            self.get_database_content_properties,
            self.create_database_property,
            self.get_database_content_properties_by_id,
            self.update_database_property_by_id,
            self.delete_database_property_by_id,
            self.get_database_operations,
            self.get_database_ancestors,
            self.create_smart_link,
            self.get_smart_link_by_id,
            self.delete_smart_link,
            self.get_smart_link_content_properties,
            self.create_smart_link_property,
            self.get_smart_link_content_properties_by_id,
            self.update_smart_link_property_by_id,
            self.delete_smart_link_property_by_id,
            self.get_smart_link_operations,
            self.get_smart_link_ancestors,
            self.create_folder,
            self.get_folder_by_id,
            self.delete_folder,
            self.get_folder_content_properties,
            self.create_folder_property,
            self.get_folder_content_properties_by_id,
            self.update_folder_property_by_id,
            self.delete_folder_property_by_id,
            self.get_folder_operations,
            self.get_folder_ancestors,
            self.get_page_version_details,
            self.get_custom_content_versions,
            self.get_custom_content_version_details,
            self.get_spaces,
            self.create_space,
            self.get_space_by_id,
            self.get_blog_posts_in_space,
            self.get_space_labels,
            self.get_space_content_labels,
            self.get_custom_content_by_type_in_space,
            self.get_space_operations,
            self.get_pages_in_space,
            self.get_space_properties,
            self.create_space_property,
            self.get_space_property_by_id,
            self.update_space_property_by_id,
            self.delete_space_property_by_id,
            self.get_space_permissions_assignments,
            self.get_available_space_permissions,
            self.get_available_space_roles,
            self.get_space_roles_by_id,
            self.get_space_role_assignments,
            self.set_space_role_assignments,
            self.get_page_footer_comments,
            self.get_page_inline_comments,
            self.get_blog_post_footer_comments,
            self.get_blog_post_inline_comments,
            self.get_footer_comments,
            self.create_footer_comment,
            self.get_footer_comment_by_id,
            self.update_footer_comment,
            self.delete_footer_comment,
            self.get_footer_comment_children,
            self.get_footer_like_count,
            self.get_footer_like_users,
            self.get_footer_comment_operations,
            self.get_footer_comment_versions,
            self.get_footer_comment_version_details,
            self.get_inline_comments,
            self.create_inline_comment,
            self.get_inline_comment_by_id,
            self.update_inline_comment,
            self.delete_inline_comment,
            self.get_inline_comment_children,
            self.get_inline_like_count,
            self.get_inline_like_users,
            self.get_inline_comment_operations,
            self.get_inline_comment_versions,
            self.get_inline_comment_version_details,
            self.get_comment_content_properties,
            self.create_comment_property,
            self.get_comment_content_properties_by_id,
            self.update_comment_property_by_id,
            self.delete_comment_property_by_id,
            self.get_tasks,
            self.get_task_by_id,
            self.get_child_pages,
            self.get_child_custom_content,
            self.get_page_ancestors,
            self.create_bulk_user_lookup,
            self.check_access_by_email,
            self.invite_by_email,
            self.get_data_policy_metadata,
            self.get_data_policy_spaces,
            self.get_classification_levels,
            self.get_space_default_classification_level,
            self.put_space_default_classification_level,
            self.delete_space_default_classification_level,
            self.get_page_classification_level,
            self.put_page_classification_level,
            self.post_page_classification_level,
            self.get_blog_post_classification_level,
            self.put_blog_post_classification_level,
            self.post_blog_post_classification_level,
            self.get_whiteboard_classification_level,
            self.put_whiteboard_classification_level,
            self.post_whiteboard_classification_level,
            self.get_database_classification_level,
            self.put_database_classification_level,
            self.post_database_classification_level,
        ]
