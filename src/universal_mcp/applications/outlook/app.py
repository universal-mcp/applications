from typing import Any
from urllib.parse import parse_qs, urlparse
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class OutlookApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="outlook", integration=integration, **kwargs)
        self.base_url = "https://graph.microsoft.com/v1.0"

    async def _get_user_id(self) -> str:
        """Helper to get the userPrincipalName from the profile."""
        user_info = await self.get_my_profile()
        user_id = user_info.get("userPrincipalName")
        if not user_id:
            raise ValueError("Could not retrieve user ID from get_my_profile response.")
        return user_id

    async def reply_to_email(
        self, message_id: str, comment: str, attachments: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Replies to a specific email message.

        Args:
            message_id (str): The ID of the email message to reply to.
            comment (str): The body of the reply.
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
            ValueError: If message_id is missing.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        if not message_id:
            raise ValueError("Missing required parameter 'message_id'.")
        request_body_data = {"comment": comment}
        if attachments:
            request_body_data["message"] = {"attachments": attachments}
        url = f"{self.base_url}/users/{user_id}/messages/{message_id}/reply"
        response = await self._apost(url, data=request_body_data, params={}, content_type="application/json")
        return self._handle_response(response)

    async def send_email(
        self,
        subject: str,
        body: str,
        to_recipients: list[str],
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
            cc_recipients (list[str], optional): A list of email addresses for the 'Cc' recipients.
            bcc_recipients (list[str], optional): A list of email addresses for the 'Bcc' recipients.
            attachments (list[dict[str, Any]], optional): A list of attachment objects. See `reply_to_email` for an example.
            body_content_type (str, optional): The content type of the email body, e.g., "Text" or "HTML". Defaults to "Text".
            save_to_sent_items (bool, optional): Whether to save the email to the 'Sent Items' folder. Defaults to True.

        Returns:
            dict[str, Any]: A dictionary confirming the send action.

        Raises:
            HTTPStatusError: If the API request fails.

        Tags:
            important
        """
        user_id = await self._get_user_id()
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
        request_body_data = {"message": message, "saveToSentItems": save_to_sent_items}
        url = f"{self.base_url}/users/{user_id}/sendMail"
        response = await self._apost(url, data=request_body_data, params={}, content_type="application/json")
        return self._handle_response(response)

    async def get_email_folder(
        self,
        folder_id: str,
        include_hidden: bool | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific email folder's metadata by its ID.

        Args:
            folder_id (str): The unique identifier for the mail folder.
            include_hidden (bool, optional): If true, includes hidden folders in the results.
            select (list[str], optional): A list of properties to return.
            expand (list[str], optional): A list of related entities to expand.

        Returns:
            dict[str, Any]: A dictionary containing the mail folder's metadata.

        Raises:
            HTTPStatusError: If the API request fails.
            ValueError: If folder_id is missing.
        Tags:
            important
        """
        user_id = await self._get_user_id()
        if not folder_id:
            raise ValueError("Missing required parameter 'folder_id'.")
        url = f"{self.base_url}/users/{user_id}/mailFolders/{folder_id}"
        select_str = ",".join(select) if select else None
        expand_str = ",".join(expand) if expand else None
        query_params = {
            k: v for k, v in [("includeHiddenFolders", include_hidden), ("$select", select_str), ("$expand", expand_str)] if v is not None
        }
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def list_emails(
        self,
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
        user_id = await self._get_user_id()
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
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_email(
        self,
        message_id: str,
        include_hidden: bool | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific email by its ID.

        Args:
            message_id (str): The unique identifier for the email.
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
        user_id = await self._get_user_id()
        if not message_id:
            raise ValueError("Missing required parameter 'message_id'.")
        url = f"{self.base_url}/users/{user_id}/messages/{message_id}"
        select_str = ",".join(select) if select else None
        expand_str = ",".join(expand) if expand else None
        query_params = {
            k: v for k, v in [("includeHiddenMessages", include_hidden), ("$select", select_str), ("$expand", expand_str)] if v is not None
        }
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def delete_email(self, message_id: str) -> dict[str, Any]:
        """
        Permanently deletes a specific email by its ID.

        Args:
            message_id (str): The unique identifier for the email to be deleted.

        Returns:
            dict[str, Any]: A dictionary confirming the deletion.

        Raises:
            HTTPStatusError: If the API request fails.
            ValueError: If message_id is missing.
        Tags:
            important
        """
        user_id = await self._get_user_id()
        if not message_id:
            raise ValueError("Missing required parameter 'message_id'.")
        url = f"{self.base_url}/users/{user_id}/messages/{message_id}"
        response = await self._adelete(url, params={})
        return self._handle_response(response)

    async def list_email_attachments(
        self,
        message_id: str,
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
        user_id = await self._get_user_id()
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
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_attachment(self, message_id: str, attachment_id: str) -> dict[str, Any]:
        """
        Retrieves a specific attachment from an email message and formats it as a dictionary.

        Args:
            message_id (str): The ID of the email message.
            attachment_id (str): The ID of the attachment.

        Returns:
            dict[str, Any]: A dictionary containing the attachment details:
                - 'type' (str): The general type of the attachment (e.g., "image", "audio", "video", "file").
                - 'data' (str): The base64 encoded content of the attachment.
                - 'mime_type' (str): The MIME type of the attachment.
                - 'file_name' (str): The name of the attachment file.
        Tags:
            important
        """
        user_id = await self._get_user_id()
        if not message_id or not attachment_id:
            raise ValueError("Missing required parameter 'message_id' or 'attachment_id'.")
        url = f"{self.base_url}/users/{user_id}/messages/{message_id}/attachments/{attachment_id}"
        response = await self._aget(url, params={})
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

    async def get_my_profile(self) -> dict[str, Any]:
        """
        Fetches the userPrincipalName for the currently authenticated user.

        Returns:
            dict[str, Any]: A dictionary containing the user's principal name.

        Raises:
            HTTPStatusError: If the API request fails.
        """
        url = f"{self.base_url}/me"
        query_params = {"$select": "userPrincipalName"}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def list_calendars(
        self,
        top: int | None = None,
        skip: int | None = None,
        select: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of calendars for the user.

        Args:
            top (int, optional): The maximum number of calendars to return.
            skip (int, optional): The number of calendars to skip.
            select (list[str], optional): A list of properties to return for each calendar.

        Returns:
            dict[str, Any]: A dictionary containing a list of calendars.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/calendars"
        select_str = ",".join(select) if select else None
        query_params = {k: v for k, v in [("$top", top), ("$skip", skip), ("$select", select_str)] if v is not None}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_calendar(
        self, calendar_id: str, select: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Retrieves a specific calendar by its ID.

        Args:
            calendar_id (str): The unique identifier for the calendar.
            select (list[str], optional): A list of properties to return.

        Returns:
            dict[str, Any]: A dictionary containing the calendar's details.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/calendars/{calendar_id}"
        select_str = ",".join(select) if select else None
        query_params = {"$select": select_str} if select_str else {}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def create_calendar(self, name: str) -> dict[str, Any]:
        """
        Creates a new calendar for the user.

        Args:
            name (str): The name of the new calendar.

        Returns:
            dict[str, Any]: A dictionary containing the created calendar's details.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/calendars"
        request_body = {"name": name}
        response = await self._apost(url, data=request_body, params={}, content_type="application/json")
        return self._handle_response(response)

    async def update_calendar(self, calendar_id: str, name: str) -> dict[str, Any]:
        """
        Updates an existing calendar's name.

        Args:
            calendar_id (str): The unique identifier for the calendar.
            name (str): The new name for the calendar.

        Returns:
            dict[str, Any]: A dictionary containing the updated calendar's details.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/calendars/{calendar_id}"
        request_body = {"name": name}
        response = await self._apatch(url, data=request_body, params={}, content_type="application/json")
        return self._handle_response(response)

    async def delete_calendar(self, calendar_id: str) -> dict[str, Any]:
        """
        Deletes a specific calendar.

        Args:
            calendar_id (str): The unique identifier for the calendar to delete.

        Returns:
            dict[str, Any]: A dictionary confirming the deletion.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/calendars/{calendar_id}"
        response = await self._adelete(url, params={})
        return self._handle_response(response)

    async def list_events(
        self,
        calendar_id: str | None = None,
        top: int | None = None,
        skip: int | None = None,
        filter: str | None = None,
        select: list[str] | None = None,
        orderby: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of events from a calendar or the user's default calendar.

        Args:
            calendar_id (str, optional): The ID of the calendar. If not provided, the default calendar is used.
            top (int, optional): The maximum number of events to return.
            skip (int, optional): The number of events to skip.
            filter (str, optional): A filter query (e.g., "start/dateTime ge '2023-01-01T00:00:00Z'").
            select (list[str], optional): A list of properties to return for each event.
            orderby (list[str], optional): A list of properties to sort the results by.

        Returns:
            dict[str, Any]: A dictionary containing a list of events.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        if calendar_id:
            url = f"{self.base_url}/users/{user_id}/calendars/{calendar_id}/events"
        else:
            url = f"{self.base_url}/users/{user_id}/calendar/events"
        select_str = ",".join(select) if select else None
        orderby_str = ",".join(orderby) if orderby else None
        query_params = {
            k: v
            for k, v in [("$top", top), ("$skip", skip), ("$filter", filter), ("$select", select_str), ("$orderby", orderby_str)]
            if v is not None
        }
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_event(
        self, event_id: str, select: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Retrieves a specific event by its ID.

        Args:
            event_id (str): The unique identifier for the event.
            select (list[str], optional): A list of properties to return.

        Returns:
            dict[str, Any]: A dictionary containing the event's details.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/events/{event_id}"
        select_str = ",".join(select) if select else None
        query_params = {"$select": select_str} if select_str else {}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def create_event(
        self,
        subject: str,
        start_datetime: str,
        end_datetime: str,
        start_timezone: str = "UTC",
        end_timezone: str = "UTC",
        body: str | None = None,
        body_content_type: str = "HTML",
        location_display_name: str | None = None,
        attendees: list[dict[str, Any]] | None = None,
        calendar_id: str | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Creates a new event in a calendar.

        Args:
            subject (str): The subject of the event.
            start_datetime (str): The start time of the event (ISO 8601 string, e.g., '2023-12-25T09:00:00').
            end_datetime (str): The end time of the event (ISO 8601 string, e.g., '2023-12-25T10:00:00').
            start_timezone (str, optional): The timezone for the start time. Defaults to 'UTC'.
            end_timezone (str, optional): The timezone for the end time. Defaults to 'UTC'.
            body (str, optional): The body content of the event.
            body_content_type (str, optional): The content type of the body (Text or HTML). Defaults to 'HTML'.
            location_display_name (str, optional): The display name for the event location.
            attendees (list[dict[str, Any]], optional): A list of attendee objects.
                Example attendee: {"type": "required", "emailAddress": {"address": "bob@example.com", "name": "Bob"}}
            calendar_id (str, optional): The ID of the calendar. If not provided, the default calendar is used.
            **kwargs: Additional properties for the event (e.g., isOnlineMeeting, reminderMinutesBeforeStart).

        Returns:
            dict[str, Any]: A dictionary containing the created event's details.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        if calendar_id:
            url = f"{self.base_url}/users/{user_id}/calendars/{calendar_id}/events"
        else:
            url = f"{self.base_url}/users/{user_id}/calendar/events"
        request_body = {
            "subject": subject,
            "start": {"dateTime": start_datetime, "timeZone": start_timezone},
            "end": {"dateTime": end_datetime, "timeZone": end_timezone},
        }
        if body:
            request_body["body"] = {"contentType": body_content_type, "content": body}
        if location_display_name:
            request_body["location"] = {"displayName": location_display_name}
        if attendees:
            request_body["attendees"] = attendees
        request_body.update(kwargs)
        response = await self._apost(url, data=request_body, params={}, content_type="application/json")
        return self._handle_response(response)

    async def update_event(
        self,
        event_id: str,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Updates an existing event.

        Args:
            event_id (str): The unique identifier for the event.
            **kwargs: Event properties to update (e.g., subject, start, end, body, attendees).
                For start/end, use nested dictionaries: start={"dateTime": "...", "timeZone": "..."}.

        Returns:
            dict[str, Any]: A dictionary containing the updated event's details.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/events/{event_id}"
        response = await self._apatch(url, data=kwargs, params={}, content_type="application/json")
        return self._handle_response(response)

    async def delete_event(self, event_id: str) -> dict[str, Any]:
        """
        Deletes a specific event.

        Args:
            event_id (str): The unique identifier for the event to delete.

        Returns:
            dict[str, Any]: A dictionary confirming the deletion.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/events/{event_id}"
        response = await self._adelete(url, params={})
        return self._handle_response(response)

    async def list_calendar_view(
        self,
        start_datetime: str,
        end_datetime: str,
        calendar_id: str | None = None,
        top: int | None = None,
        skip: int | None = None,
        select: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves events between a start and end time (includes expanded recurring events).

        Args:
            start_datetime (str): The start of the time range (ISO 8601, e.g., '2023-12-25T00:00:00Z').
            end_datetime (str): The end of the time range (ISO 8601, e.g., '2023-12-26T00:00:00Z').
            calendar_id (str, optional): The ID of the calendar. If not provided, the default calendar is used.
            top (int, optional): The maximum number of events to return.
            skip (int, optional): The number of events to skip.
            select (list[str], optional): A list of properties to return for each event.

        Returns:
            dict[str, Any]: A dictionary containing a list of event instances.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        if calendar_id:
            url = f"{self.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView"
        else:
            url = f"{self.base_url}/users/{user_id}/calendar/calendarView"
        select_str = ",".join(select) if select else None
        query_params = {
            "startDateTime": start_datetime,
            "endDateTime": end_datetime,
        }
        if top is not None:
            query_params["$top"] = top
        if skip is not None:
            query_params["$skip"] = skip
        if select_str:
            query_params["$select"] = select_str
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_schedule(
        self,
        schedules: list[str],
        start_datetime: str,
        end_datetime: str,
        availability_view_interval: int = 30,
    ) -> dict[str, Any]:
        """
        Retrieves free/busy information for a set of users, groups, or resources.

        Args:
            schedules (list[str]): A list of SMTP addresses (emails) to get schedules for.
            start_datetime (str): The start of the time range (ISO 8601 with 'Z', e.g., '2023-12-25T00:00:00Z').
            end_datetime (str): The end of the time range (ISO 8601 with 'Z', e.g., '2023-12-26T00:00:00Z').
            availability_view_interval (int, optional): The duration of each time slot in minutes. Defaults to 30.

        Returns:
            dict[str, Any]: A dictionary containing schedule information.

        Tags:
            important
        """
        user_id = await self._get_user_id()
        url = f"{self.base_url}/users/{user_id}/calendar/getSchedule"
        request_body = {
            "schedules": schedules,
            "startTime": {"dateTime": start_datetime, "timeZone": "UTC"},
            "endTime": {"dateTime": end_datetime, "timeZone": "UTC"},
            "availabilityViewInterval": availability_view_interval,
        }
        response = await self._apost(url, data=request_body, params={}, content_type="application/json")
        return self._handle_response(response)

    async def get_next_page_results(self, url: str) -> dict[str, Any]:
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
        response = await self._aget(path_only, params=params)
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
            self.list_calendars,
            self.get_calendar,
            self.create_calendar,
            self.update_calendar,
            self.delete_calendar,
            self.list_events,
            self.get_event,
            self.create_event,
            self.update_event,
            self.delete_event,
            self.list_calendar_view,
            self.get_schedule,
        ]
