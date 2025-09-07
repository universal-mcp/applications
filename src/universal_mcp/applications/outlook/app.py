from typing import Any
from urllib.parse import parse_qs, urlparse

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class OutlookApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="outlook", integration=integration, **kwargs)
        self.base_url = "https://graph.microsoft.com/v1.0"

    def users_message_reply(
        self,
        message_id: str,
        user_id: str | None = None,
        comment: str | None = None,
        message: dict[str, Any] | None = None,
    ) -> Any:
        """
        Replies to a specific message for a user using the POST method, accepting JSON content in the request body and returning status codes indicating success or error.

        Args:
            user_id (string, optional): user-id. If not provided, will automatically get the current user's ID.
            message_id (string): message-id
            comment (string): A comment to include in the reply. Example: 'Thank you for your email. Here is my reply.'.
            message (object): A message object to specify additional properties for the reply, such as attachments. Example: {'subject': 'RE: Project Update', 'body': {'contentType': 'Text', 'content': 'Thank you for the update. Looking forward to the next steps.'}, 'toRecipients': [{'emailAddress': {'address': 'alice@contoso.com'}}], 'attachments': [{'@odata.type': '#microsoft.graph.fileAttachment', 'name': 'agenda.pdf', 'contentType': 'application/pdf', 'contentBytes': 'SGVsbG8gV29ybGQh'}]}.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message, important
        """
        # If user_id is not provided, get it automatically
        if user_id is None:
            user_info = self.get_user_id()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError(
                    "Could not retrieve user ID from get_user_id response."
                )
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "comment": comment,
            "message": message,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/{user_id}/messages/{message_id}/reply"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_send_mail(
        self,
        message: dict[str, Any],
        user_id: str | None = None,
        saveToSentItems: bool | None = None,
    ) -> Any:
        """
        Sends an email on behalf of the specified user, accepting the email details as JSON in the request body and returning a 204 No Content response on success.

        Args:
            user_id (string, optional): user-id. If not provided, will automatically get the current user's ID.
            message (object): message Example: {'subject': 'Meet for lunch?', 'body': {'contentType': 'Text', 'content': 'The new cafeteria is open.'}, 'toRecipients': [{'emailAddress': {'address': 'frannis@contoso.com'}}], 'ccRecipients': [{'emailAddress': {'address': 'danas@contoso.com'}}], 'bccRecipients': [{'emailAddress': {'address': 'bccuser@contoso.com'}}], 'attachments': [{'@odata.type': '#microsoft.graph.fileAttachment', 'name': 'attachment.txt', 'contentType': 'text/plain', 'contentBytes': 'SGVsbG8gV29ybGQh'}]}.
            saveToSentItems (boolean): saveToSentItems Example: 'False'.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.user.Actions, important
        """
        # If user_id is not provided, get it automatically
        if user_id is None:
            user_info = self.get_user_id()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError(
                    "Could not retrieve user ID from get_user_id response."
                )
        request_body_data = None
        request_body_data = {
            "message": message,
            "saveToSentItems": saveToSentItems,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/{user_id}/sendMail"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_get_mail_folder(
        self,
        mailFolder_id: str,
        user_id: str | None = None,
        includeHiddenFolders: str | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> Any:
        """
        Retrieves a specific mail folder for a specified user using optional query parameters to include hidden folders or select/expand properties.

        Args:
            user_id (string, optional): user-id. If not provided, will automatically get the current user's ID.
            mailFolder_id (string): mailFolder-id
            includeHiddenFolders (string): Include Hidden Folders
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder, important
        """
        # If user_id is not provided, get it automatically
        if user_id is None:
            user_info = self.get_user_id()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError(
                    "Could not retrieve user ID from get_user_id response."
                )
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.base_url}/users/{user_id}/mailFolders/{mailFolder_id}"
        query_params = {
            k: v
            for k, v in [
                ("includeHiddenFolders", includeHiddenFolders),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_list_message(
        self,
        user_id: str | None = None,
        select: list[str] = ["bodyPreview"],
        includeHiddenMessages: bool | None = None,
        top: int | None = None,
        skip: int | None = None,
        search: str | None = None,
        filter: str | None = None,
        count: bool | None = None,
        orderby: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of messages for a user, allowing optional filtering and sorting of results based on parameters such as includeHiddenMessages, search, filter, top, skip, orderby, select, and expand.

        Args:
            user_id (string, optional): user-id. If not provided, will automatically get the current user's ID.
            select (list): Select properties to be returned. Defaults to ['bodyPreview'].
                Example: [
                    'id', 'categories', 'receivedDateTime', 'sentDateTime', 'hasAttachments', 'internetMessageId',
                    'subject', 'body', 'bodyPreview', 'importance', 'parentFolderId', 'conversationId',
                    'conversationIndex', 'isDeliveryReceiptRequested', 'isReadReceiptRequested', 'isRead', 'isDraft',
                    'webLink', 'inferenceClassification', 'sender', 'from', 'toRecipients', 'ccRecipients',
                    'bccRecipients', 'replyTo', 'flag', 'attachments', 'extensions', 'mentions', 'uniqueBody'
                ]
            includeHiddenMessages (boolean): Include Hidden Messages
            top (integer): Specify the number of items to be included in the result Example: '50'.
            skip (integer): Specify the number of items to skip in the result Example: '10'.
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message, important
        """
        # If user_id is not provided, get it automatically
        if user_id is None:
            user_info = self.get_user_id()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError(
                    "Could not retrieve user ID from get_user_id response."
                )

        url = f"{self.base_url}/users/{user_id}/messages"

        # Handle list parameters by joining with commas
        select_str = ",".join(select) if select else None
        orderby_str = ",".join(orderby) if orderby else None
        expand_str = ",".join(expand) if expand else None

        query_params = {
            k: v
            for k, v in [
                ("includeHiddenMessages", includeHiddenMessages),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby_str),
                ("$select", select_str),
                ("$expand", expand_str),
            ]
            if v is not None
        }

        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_get_message(
        self,
        message_id: str,
        user_id: str | None = None,
        includeHiddenMessages: str | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> Any:
        """
        Retrieves a specific message for a user, optionally including hidden messages, selecting specific fields, or expanding related data.

        Args:
            user_id (string, optional): user-id. If not provided, will automatically get the current user's ID.
            message_id (string): message-id
            includeHiddenMessages (string): Include Hidden Messages
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message, important
        """
        # If user_id is not provided, get it automatically
        if user_id is None:
            user_info = self.get_user_id()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError(
                    "Could not retrieve user ID from get_user_id response."
                )
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.base_url}/users/{user_id}/messages/{message_id}"
        query_params = {
            k: v
            for k, v in [
                ("includeHiddenMessages", includeHiddenMessages),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_delete_message(self, message_id: str, user_id: str | None = None) -> Any:
        """
        Deletes a specific message for a given user using the DELETE method and optional If-Match header for conditional requests.

        Args:
            user_id (string, optional): user-id. If not provided, will automatically get the current user's ID.
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message, important
        """
        # If user_id is not provided, get it automatically
        if user_id is None:
            user_info = self.get_user_id()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError(
                    "Could not retrieve user ID from get_user_id response."
                )
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.base_url}/users/{user_id}/messages/{message_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_message_list_attachment(
        self,
        message_id: str,
        user_id: str | None = None,
        top: int | None = None,
        skip: int | None = None,
        search: str | None = None,
        filter: str | None = None,
        count: bool | None = None,
        orderby: list[str] | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves attachments associated with a specified user's message, supporting filtering, pagination, and field selection via query parameters.

        Args:
            user_id (string, optional): user-id. If not provided, will automatically get the current user's ID.
            message_id (string): message-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message, important
        """
        # If user_id is not provided, get it automatically
        if user_id is None:
            user_info = self.get_user_id()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError(
                    "Could not retrieve user ID from get_user_id response."
                )
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.base_url}/users/{user_id}/messages/{message_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_user_id(
        self,
    ) -> dict[str, Any]:
        """
        Retrieves the current user.


        Returns:
            dict[str, Any]: Current user information

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            me, important
        """
        url = f"{self.base_url}/me"
        query_params = {
            "$select": "userPrincipalName",
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_from_url(self, url: str) -> dict[str, Any]:
        """
        Makes a GET request to a full @odata.nextLink or @odata.deltaLink URL.
        """
        if not url:
            raise ValueError("Missing required parameter 'url'.")
        if not url.startswith(self.base_url):
            raise ValueError(
                f"The provided URL '{url}' does not start with the expected base URL '{self.base_url}'."
            )
        relative_part = url[len(self.base_url) :]
        parsed_relative = urlparse(relative_part)
        path_only = parsed_relative.path
        params = {k: v[0] for k, v in parse_qs(parsed_relative.query).items()}
        response = self._get(path_only, params=params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.users_message_reply,
            self.user_send_mail,
            self.user_get_mail_folder,
            self.user_list_message,
            self.user_get_message,
            self.user_delete_message,
            self.user_message_list_attachment,
            self.get_user_id,
            self.get_from_url,
        ]
