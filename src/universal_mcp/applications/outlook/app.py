from typing import Any
from urllib.parse import parse_qs, urlparse

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class OutlookApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="outlook", integration=integration, **kwargs)
        self.base_url = "https://graph.microsoft.com/v1.0"

    def reply_to_email(
        self,
        message_id: str,
        comment: str,
        user_id: str | None = None,
        attachments: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Replies to a specific email message.

        Args:
            message_id (str): The ID of the email message to reply to.
            comment (str): The body of the reply.
            user_id (str, optional): The ID of the user to send the reply from. Defaults to the authenticated user.
            attachments (list[dict[str, Any]], optional): A list of attachment objects to include in the reply.
                Each attachment dictionary should conform to the Microsoft Graph API specification.
                Example:
                [
                    {
                        "@odata.type": "#microsoft.graph.fileAttachment",
                        "name": "attachment.txt",
                        "contentType": "text/plain",
                        "contentBytes": "SGVsbG8gV29ybGQh"
                    }
                ]

        Returns:
            dict[str, Any]: A dictionary confirming the reply action.

        Raises:
            HTTPStatusError: If the API request fails.
            ValueError: If the user_id cannot be retrieved or message_id is missing.

        Tags:
            important
        """
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")
        if not message_id:
            raise ValueError("Missing required parameter 'message_id'.")

        request_body_data = {"comment": comment}
        if attachments:
            request_body_data["message"] = {"attachments": attachments}

        url = f"{self.base_url}/users/{user_id}/messages/{message_id}/reply"

        response = self._post(
            url,
            data=request_body_data,
            params={},
            content_type="application/json",
        )
        return self._handle_response(response)

    def send_email(
        self,
        subject: str,
        body: str,
        to_recipients: list[str],
        user_id: str | None = None,
        cc_recipients: list[str] | None = None,
        bcc_recipients: list[str] | None = None,
        attachments: list[dict[str, Any]] | None = None,
        body_content_type: str = "Text",
        save_to_sent_items: bool = True,
    ) -> dict[str, Any]:
        """
        Sends a new email.

        Args:
            subject (str): The subject of the email.
            body (str): The body of the email.
            to_recipients (list[str]): A list of email addresses for the 'To' recipients.
            user_id (str, optional): The ID of the user to send the email from. Defaults to the authenticated user.
            cc_recipients (list[str], optional): A list of email addresses for the 'Cc' recipients.
            bcc_recipients (list[str], optional): A list of email addresses for the 'Bcc' recipients.
            attachments (list[dict[str, Any]], optional): A list of attachment objects. See `reply_to_email` for an example.
            body_content_type (str, optional): The content type of the email body, e.g., "Text" or "HTML". Defaults to "Text".
            save_to_sent_items (bool, optional): Whether to save the email to the 'Sent Items' folder. Defaults to True.

        Returns:
            dict[str, Any]: A dictionary confirming the send action.

        Raises:
            HTTPStatusError: If the API request fails.
            ValueError: If the user_id cannot be retrieved.

        Tags:
            important
        """
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        message = {
            "subject": subject,
            "body": {"contentType": body_content_type, "content": body},
            "toRecipients": [{"emailAddress": {"address": email}} for email in to_recipients],
        }
        if cc_recipients:
            message["ccRecipients"] = [{"emailAddress": {"address": email}} for email in cc_recipients]
        if bcc_recipients:
            message["bccRecipients"] = [{"emailAddress": {"address": email}} for email in bcc_recipients]
        if attachments:
            message["attachments"] = attachments

        request_body_data = {
            "message": message,
            "saveToSentItems": save_to_sent_items,
        }

        url = f"{self.base_url}/users/{user_id}/sendMail"

        response = self._post(
            url,
            data=request_body_data,
            params={},
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_email_folder(
        self,
        folder_id: str,
        user_id: str | None = None,
        include_hidden: bool | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific email folder's metadata by its ID.

        Args:
            folder_id (str): The unique identifier for the mail folder.
            user_id (str, optional): The ID of the user who owns the folder. Defaults to the authenticated user.
            include_hidden (bool, optional): If true, includes hidden folders in the results.
            select (list[str], optional): A list of properties to return.
            expand (list[str], optional): A list of related entities to expand.

        Returns:
            dict[str, Any]: A dictionary containing the mail folder's metadata.

        Raises:
            HTTPStatusError: If the API request fails.
            ValueError: If user_id cannot be retrieved or folder_id is missing.
        Tags:
            important
        """
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")
        if not folder_id:
            raise ValueError("Missing required parameter 'folder_id'.")

        url = f"{self.base_url}/users/{user_id}/mailFolders/{folder_id}"
        select_str = ",".join(select) if select else None
        expand_str = ",".join(expand) if expand else None

        query_params = {
            k: v
            for k, v in [
                ("includeHiddenFolders", include_hidden),
                ("$select", select_str),
                ("$expand", expand_str),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_emails(
        self,
        user_id: str | None = None,
        select: list[str] = ["bodyPreview"],
        include_hidden: bool | None = None,
        top: int | None = None,
        skip: int | None = None,
        search: str | None = None,
        filter: str | None = None,
        count: bool | None = None,
        orderby: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of emails from a user's mailbox.

        Args:
            user_id (str, optional): The ID of the user. Defaults to the authenticated user.
            select (list[str], optional): A list of properties to return for each email. Defaults to ['bodyPreview'].
            include_hidden (bool, optional): If true, includes hidden messages.
            top (int, optional): The maximum number of emails to return.
            skip (int, optional): The number of emails to skip. Cannot be used with 'search'.
            search (str, optional): A search query. Cannot be used with 'filter', 'orderby', or 'skip'.
            filter (str, optional): A filter query. Cannot be used with 'search'.
            count (bool, optional): If true, includes the total count of emails in the response.
            orderby (list[str], optional): A list of properties to sort the results by. Cannot be used with 'search'.
            expand (list[str], optional): A list of related entities to expand.

        Returns:
            dict[str, Any]: A dictionary containing a list of emails and pagination information.

        Raises:
            ValueError: If incompatible parameters are used together (e.g., 'search' with 'filter').
            HTTPStatusError: If the API request fails.
        Tags:
            important
        """
        if search:
            if filter:
                raise ValueError("The 'search' parameter cannot be used with 'filter'.")
            if orderby:
                raise ValueError("The 'search' parameter cannot be used with 'orderby'.")
            if skip:
                raise ValueError("The 'search' parameter cannot be used with 'skip'. Use pagination via @odata.nextLink instead.")

        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")

        url = f"{self.base_url}/users/{user_id}/messages"
        select_str = ",".join(select) if select else None
        orderby_str = ",".join(orderby) if orderby else None
        expand_str = ",".join(expand) if expand else None

        query_params = {
            k: v
            for k, v in [
                ("includeHiddenMessages", include_hidden),
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

    def get_email(
        self,
        message_id: str,
        user_id: str | None = None,
        include_hidden: bool | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific email by its ID.

        Args:
            message_id (str): The unique identifier for the email.
            user_id (str, optional): The ID of the user who owns the email. Defaults to the authenticated user.
            include_hidden (bool, optional): If true, includes hidden messages.
            select (list[str], optional): A list of properties to return.
            expand (list[str], optional): A list of related entities to expand.

        Returns:
            dict[str, Any]: A dictionary containing the email's details.

        Raises:
            HTTPStatusError: If the API request fails.
            ValueError: If user_id cannot be retrieved or message_id is missing.
        Tags:
            important
        """
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")
        if not message_id:
            raise ValueError("Missing required parameter 'message_id'.")

        url = f"{self.base_url}/users/{user_id}/messages/{message_id}"
        select_str = ",".join(select) if select else None
        expand_str = ",".join(expand) if expand else None

        query_params = {
            k: v
            for k, v in [
                ("includeHiddenMessages", include_hidden),
                ("$select", select_str),
                ("$expand", expand_str),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_email(self, message_id: str, user_id: str | None = None) -> dict[str, Any]:
        """
        Permanently deletes a specific email by its ID.

        Args:
            message_id (str): The unique identifier for the email to be deleted.
            user_id (str, optional): The ID of the user who owns the email. Defaults to the authenticated user.

        Returns:
            dict[str, Any]: A dictionary confirming the deletion.

        Raises:
            HTTPStatusError: If the API request fails.
            ValueError: If user_id cannot be retrieved or message_id is missing.
        Tags:
            important
        """
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")
        if not message_id:
            raise ValueError("Missing required parameter 'message_id'.")

        url = f"{self.base_url}/users/{user_id}/messages/{message_id}"
        response = self._delete(url, params={})
        return self._handle_response(response)

    def list_email_attachments(
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
        Retrieves attachments for a specific email.

        Args:
            message_id (str): The unique identifier for the email.
            user_id (str, optional): The ID of the user who owns the email. Defaults to the authenticated user.
            top (int, optional): The maximum number of attachments to return.
            skip (int, optional): The number of attachments to skip. Cannot be used with 'search'.
            search (str, optional): A search query. Cannot be used with 'filter', 'orderby', or 'skip'.
            filter (str, optional): A filter query. Cannot be used with 'search'.
            count (bool, optional): If true, includes the total count of attachments.
            orderby (list[str], optional): A list of properties to sort by. Cannot be used with 'search'.
            select (list[str], optional): A list of properties to return.
            expand (list[str], optional): A list of related entities to expand.

        Returns:
            dict[str, Any]: A dictionary containing a list of attachments.

        Raises:
            ValueError: If incompatible parameters are used together.
            HTTPStatusError: If the API request fails.
        Tags:
            important
        """
        if search:
            if filter:
                raise ValueError("The 'search' parameter cannot be used with 'filter'.")
            if orderby:
                raise ValueError("The 'search' parameter cannot be used with 'orderby'.")
            if skip:
                raise ValueError("The 'search' parameter cannot be used with 'skip'. Use pagination via @odata.nextLink instead.")

        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError("Could not retrieve user ID from get_my_profile response.")
        if not message_id:
            raise ValueError("Missing required parameter 'message_id'.")

        url = f"{self.base_url}/users/{user_id}/messages/{message_id}/attachments"
        orderby_str = ",".join(orderby) if orderby else None
        select_str = ",".join(select) if select else None
        expand_str = ",".join(expand) if expand else None

        query_params = {
            k: v
            for k, v in [
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

    def get_attachment(
        self,
        message_id: str,
        attachment_id: str,
        user_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific attachment from an email message and formats it as a dictionary.

        Args:
            message_id (str): The ID of the email message.
            attachment_id (str): The ID of the attachment.
            user_id (str, optional): The ID of the user. Defaults to the authenticated user.

        Returns:
            dict[str, Any]: A dictionary containing the attachment details:
                - 'type' (str): The general type of the attachment (e.g., "image", "audio", "video", "file").
                - 'data' (str): The base64 encoded content of the attachment.
                - 'mime_type' (str): The MIME type of the attachment.
                - 'file_name' (str): The name of the attachment file.
        Tags:
            important
        """
        if user_id is None:
            user_info = self.get_my_profile()
            user_id = user_info.get("userPrincipalName")
            if not user_id:
                raise ValueError("Could not retrieve user ID.")
        if not message_id or not attachment_id:
            raise ValueError("Missing required parameter 'message_id' or 'attachment_id'.")

        url = f"{self.base_url}/users/{user_id}/messages/{message_id}/attachments/{attachment_id}"

        response = self._get(url, params={})
        attachment_data = self._handle_response(response)

        content_type = attachment_data.get("contentType", "application/octet-stream")
        attachment_type = content_type.split("/")[0] if "/" in content_type else "file"
        if attachment_type not in ["image", "audio", "video", "text"]:
            attachment_type = "file"

        return {
            "type": attachment_type,
            "data": attachment_data.get("contentBytes"),
            "mime_type": content_type,
            "file_name": attachment_data.get("name"),
        }

    def get_my_profile(self) -> dict[str, Any]:
        """
        Fetches the userPrincipalName for the currently authenticated user.

        Returns:
            dict[str, Any]: A dictionary containing the user's principal name.

        Raises:
            HTTPStatusError: If the API request fails.
        """
        url = f"{self.base_url}/me"
        query_params = {"$select": "userPrincipalName"}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_next_page_results(self, url: str) -> dict[str, Any]:
        """
        Retrieves the next page of results from a paginated API response.

        Args:
            url (str): The full URL for the next page of results (@odata.nextLink).

        Returns:
            dict[str, Any]: A dictionary containing the next page of results.

        Raises:
            ValueError: If the URL is missing or invalid.
        Tags:
            important
        """
        if not url:
            raise ValueError("Missing required parameter 'url'.")
        if not url.startswith(self.base_url):
            raise ValueError(f"The provided URL must start with '{self.base_url}'.")

        relative_part = url[len(self.base_url) :]
        parsed_relative = urlparse(relative_part)
        path_only = parsed_relative.path
        params = {k: v[0] for k, v in parse_qs(parsed_relative.query).items()}

        response = self._get(path_only, params=params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.reply_to_email,
            self.send_email,
            self.get_email_folder,
            self.list_emails,
            self.get_email,
            self.delete_email,
            self.list_email_attachments,
            self.get_attachment,
            self.get_my_profile,
            self.get_next_page_results,
        ]
