from datetime import UTC, datetime, timedelta
from typing import Any

from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class GoogleCalendarApp(APIApplication):
    def __init__(self, integration: Integration) -> None:
        super().__init__(name="google_calendar", integration=integration)
        self.base_api_url = "https://www.googleapis.com/calendar/v3/calendars/primary"
        self.base_url = "https://www.googleapis.com/calendar/v3"

    def _format_datetime(self, dt_string: str) -> str:
        """Format a datetime string from ISO format to a human-readable format.

        Args:
            dt_string: A datetime string in ISO format (e.g., "2023-06-01T10:00:00Z")

        Returns:
            A formatted datetime string (e.g., "2023-06-01 10:00 AM") or the original string with
            "(All day)" appended if it's just a date
        """
        if not dt_string or dt_string == "Unknown":
            return "Unknown"

        # Check if it's just a date (all-day event) or a datetime
        if "T" in dt_string:
            # It's a datetime - parse and format it
            try:
                # Handle Z (UTC) suffix by replacing with +00:00 timezone
                if dt_string.endswith("Z"):
                    dt_string = dt_string.replace("Z", "+00:00")

                # Parse the ISO datetime string
                dt = datetime.fromisoformat(dt_string)

                # Format to a more readable form
                return dt.strftime("%Y-%m-%d %I:%M %p")
            except ValueError:
                # In case of parsing error, return the original
                logger.warning(f"Could not parse datetime string: {dt_string}")
                return dt_string
        else:
            # It's just a date (all-day event)
            return f"{dt_string} (All day)"

    def get_upcoming_events(
        self,
        days: int = 1,
        max_results: int | None = None,
        time_zone: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves events for a specified number of days, starting from today. This function simplifies date-range queries by auto-calculating start/end times, unlike the more comprehensive `list_events` function, which offers granular control with explicit time filters, text search, and custom sorting.

        Args:
            days: Number of days to retrieve events for (default: 1, which is just today)
            max_results: Maximum number of events to return (optional)
            time_zone: Time zone used in the response (optional, default is calendar's time zone)

        Returns:
            Dictionary containing the complete API response with all events and metadata

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code

        Tags:
            fetch, list, calendar, events, date-time, important, api
        """
        today = datetime.now(UTC).date()
        end_date = today + timedelta(days=days)
        time_min = f"{today.isoformat()}T00:00:00Z"
        time_max = f"{end_date.isoformat()}T00:00:00Z"
        url = f"{self.base_api_url}/events"
        params = {
            "timeMin": time_min,
            "timeMax": time_max,
            "singleEvents": "true",
            "orderBy": "startTime",
        }
        if max_results is not None:
            params["maxResults"] = str(max_results)
        if time_zone:
            params["timeZone"] = time_zone
        date_range = "today" if days == 1 else f"the next {days} days"
        logger.info(f"Retrieving calendar events for {date_range}")
        response = self._get(url, params=params)

        return self._handle_response(response)

    def get_event_by_id(
        self,
        event_id: str,
        max_attendees: int | None = None,
        time_zone: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific calendar event using its unique ID. Unlike `list_events`, which fetches multiple events based on date ranges or search queries, this function targets a single, known event. It can optionally limit attendees returned and specify a time zone for date formatting in the response.

        Args:
            event_id: The unique identifier of the calendar event to retrieve
            max_attendees: Optional. The maximum number of attendees to include in the response. If None, includes all attendees
            time_zone: Optional. The time zone to use for formatting dates in the response. If None, uses the calendar's default time zone

        Returns:
            Dictionary containing the complete API response with all event details

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code
            JSONDecodeError: Raised when the API response cannot be parsed as JSON

        Tags:
            retrieve, calendar, event, api, important
        """
        url = f"{self.base_api_url}/events/{event_id}"
        params = {}
        if max_attendees is not None:
            params["maxAttendees"] = max_attendees
        if time_zone:
            params["timeZone"] = time_zone
        logger.info(f"Retrieving calendar event with ID: {event_id}")
        response = self._get(url, params=params)
        return self._handle_response(response)

    def list_events(
        self,
        max_results: int = 10,
        time_min: str | None = None,
        time_max: str | None = None,
        q: str | None = None,
        order_by: str = "startTime",
        single_events: bool = True,
        time_zone: str | None = None,
        page_token: str | None = None,
    ) -> dict[str, Any]:
        """
        Fetches a customizable list of events using filters for date range, text search, sorting, and pagination. This advanced function provides more granular control than `get_upcoming_events`, which is limited to fetching events for a specific number of upcoming days.

        Args:
            max_results: Maximum number of events to return (default: 10, max: 2500)
            time_min: Start time in ISO format (e.g., '2023-12-01T00:00:00Z'). Defaults to current time if not specified
            time_max: End time in ISO format (e.g., '2023-12-31T23:59:59Z')
            q: Free text search terms to filter events (searches across summary, description, location, attendees)
            order_by: Sort order for results - either 'startTime' (default) or 'updated'
            single_events: Whether to expand recurring events into individual instances (default: True)
            time_zone: Time zone for response formatting (defaults to calendar's time zone)
            page_token: Token for retrieving a specific page of results in paginated responses

        Returns:
            Dictionary containing the complete API response with all events and metadata

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code
            JSONDecodeError: Raised when the API response cannot be parsed as JSON

        Tags:
            list, retrieve, calendar, events, pagination, api, important
        """
        url = f"{self.base_api_url}/events"
        params = {
            "maxResults": str(max_results),
            "orderBy": order_by,
            "singleEvents": str(single_events).lower(),
        }
        if time_min:
            params["timeMin"] = time_min
        else:
            # Default to current time if not specified
            now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
            params["timeMin"] = now
        if time_max:
            params["timeMax"] = time_max
        if q:
            params["q"] = q
        if time_zone:
            params["timeZone"] = time_zone
        if page_token:
            params["pageToken"] = page_token
        logger.info(f"Retrieving calendar events with params: {params}")
        response = self._get(url, params=params)

        return self._handle_response(response)

    def create_event(
        self,
        start: dict[str, Any],
        end: dict[str, Any],
        summary: str,
        description: str | None = None,
        location: str | None = None,
        attendees: list[dict[str, str]] | None = None,
        recurrence: list[str] | None = None,
        calendar_id: str = "primary",
    ) -> dict[str, Any]:
        """
        Creates a calendar event using structured data for start/end times, summary, attendees, and recurrence. This method provides precise control for complex appointments, unlike `create_event_from_text` which parses natural language, making it ideal for detailed or recurring event creation.

        Args:
            start: Start time of the event (required). Must include timezone offset or timeZone field.
                   Examples:
                   - {"dateTime": "2025-08-7T16:30:00+05:30"} (with offset)
                   - {"dateTime": "2025-08-7T16:30:00", "timeZone": "Asia/Kolkata"} (with timeZone field)
                   - {"dateTime": "2025-08-7T16:30:00Z", "timeZone": "UTC"} (UTC time)
            end: End time of the event (required). Must include timezone offset or timeZone field.
                 Examples:
                 - {"dateTime": "2025-08-7T17:30:00+05:30"} (with offset)
                 - {"dateTime": "2025-08-7T17:30:00", "timeZone": "Asia/Kolkata"} (with timeZone field)
                 - {"dateTime": "2025-08-7T17:30:00Z", "timeZone": "UTC"} (UTC time)
            summary: Event title/summary (required). Example: "New"
            description: Event description. Example: "hey"
            location: Event location. Example: "Delhi"
            attendees: List of attendee dictionaries. Example: [{"email": "example@gmail.com"}]
            recurrence: List of RRULE, RDATE, or EXDATE strings for recurring events (optional).
                       Example: ["RRULE:FREQ=WEEKLY;COUNT=5;BYDAY=TU,FR"],
                       # For an all-day event starting on June 1st, 2015 and repeating every 3 days throughout the month,excluding June 10th but including June 9th and 11th:
                       Example: [
                           "EXDATE;VALUE=DATE:20150610",
                           "RDATE;VALUE=DATE:20150609,20150611",
                           "RRULE:FREQ=DAILY;UNTIL=20150628;INTERVAL=3"
                       ],
            calendar_id: Calendar identifier (default: "primary")

        Returns:
            Dictionary containing the complete API response with the created event details

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code

        Tags:
            create, calendar, event, insert, recurring, important
        """

        request_body_data = {
            "start": start,
            "end": end,
            "summary": summary,
            "description": description,
            "location": location,
            "attendees": attendees,
            "recurrence": recurrence,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }

        url = f"{self.base_url}/calendars/{calendar_id}/events"

        response = self._post(url, data=request_body_data)

        return self._handle_response(response)

    def create_event_from_text(
        self, text: str, send_updates: str = "none"
    ) -> dict[str, Any]:
        """
        Creates a calendar event by parsing a natural language string (e.g., "Meeting tomorrow at 10am"). This offers a user-friendly shortcut, contrasting with the structured `create_event` function which requires explicit fields like start and end times.

        Args:
            text: Natural language text describing the event (e.g., 'Meeting with John at Coffee Shop tomorrow 3pm-4pm')
            send_updates: Specifies who should receive event notifications: 'all', 'externalOnly', or 'none' (default)

        Returns:
            Dictionary containing the complete API response with the created event details

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code

        Tags:
            create, calendar, event, quick-add, natural-language, important
        """
        url = f"{self.base_api_url}/events/quickAdd"
        params = {"text": text, "sendUpdates": send_updates}
        logger.info(f"Creating event via quickAdd: '{text}'")
        response = self._post(url, data=None, params=params)

        return self._handle_response(response)

    def list_recurring_event_instances(
        self,
        event_id: str,
        max_results: int = 25,
        time_min: str | None = None,
        time_max: str | None = None,
        time_zone: str | None = None,
        show_deleted: bool = False,
        page_token: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves all individual occurrences of a specific recurring event using its ID. Unlike `list_events`, which fetches multiple distinct events, this function expands a single recurring event into its separate instances, allowing filtering by time range and pagination for detailed scheduling views.

        Args:
            event_id: ID of the recurring event
            max_results: Maximum number of event instances to return (default: 25, max: 2500)
            time_min: Lower bound (inclusive) for event's end time in ISO format
            time_max: Upper bound (exclusive) for event's start time in ISO format
            time_zone: Time zone used in the response (defaults to calendar's time zone)
            show_deleted: Whether to include deleted instances (default: False)
            page_token: Token for retrieving a specific page of results

        Returns:
            Dictionary containing the complete API response with all event instances and metadata

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code
            JSONDecodeError: Raised when the API response cannot be parsed as JSON

        Tags:
            list, retrieve, calendar, events, recurring, pagination, api, important
        """
        url = f"{self.base_api_url}/events/{event_id}/instances"
        params = {
            "maxResults": str(max_results),
            "showDeleted": str(show_deleted).lower(),
        }
        if time_min:
            params["timeMin"] = time_min
        if time_max:
            params["timeMax"] = time_max
        if time_zone:
            params["timeZone"] = time_zone
        if page_token:
            params["pageToken"] = page_token
        logger.info(f"Retrieving instances of recurring event with ID: {event_id}")
        response = self._get(url, params=params)

        return self._handle_response(response)

    def delete_event(
        self,
        calendarId,
        eventId,
        sendNotifications=None,
        sendUpdates=None,
        alt=None,
        fields=None,
        key=None,
        oauth_token=None,
        prettyPrint=None,
        quotaUser=None,
        userIp=None,
    ) -> Any:
        """
        Permanently deletes a specific event from a Google Calendar using its event and calendar IDs. It can optionally send cancellation notifications to attendees, distinguishing it from functions that retrieve (`get_event_by_id`) or modify events (`replace_event`), which do not remove entries from the calendar.

        Args:
            calendarId (string): calendarId
            eventId (string): eventId
            sendNotifications (string): No description provided. Example: 'true'.
            sendUpdates (string): No description provided. Example: 'amet in'.
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: 'amet in'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: 'amet in'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: 'amet in'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: 'true'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: 'amet in'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: 'amet in'.

        Returns:
            Any: No Content

        Tags:
            calendars, {calendarId}, events, {eventId}
        """
        if calendarId is None:
            raise ValueError("Missing required parameter 'calendarId'")
        if eventId is None:
            raise ValueError("Missing required parameter 'eventId'")
        url = f"{self.base_url}/calendars/{calendarId}/events/{eventId}"
        query_params = {
            k: v
            for k, v in [
                ("sendNotifications", sendNotifications),
                ("sendUpdates", sendUpdates),
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def replace_event(
        self,
        event_id: str,
        start: dict[str, Any],
        end: dict[str, Any],
        summary: str,
        description: str | None = None,
        location: str | None = None,
        attendees: list[dict[str, str]] | None = None,
        recurrence: list[str] | None = None,
        calendar_id: str = "primary",
        send_updates: str = "none",
        max_attendees: int | None = None,
    ) -> dict[str, Any]:
        """
        Replaces an existing calendar event, identified by its ID, with new data. This function performs a full update, overwriting all event properties like start/end times and summary. It does not support partial modifications, requiring all necessary fields for the replacement to be provided.

        Args:
            event_id: The unique identifier of the calendar event to update (required)
            start: Start time of the event (required). Must include timezone offset or timeZone field.
                   Examples:
                   - {"dateTime": "2025-08-7T16:30:00+05:30"} (with offset)
                   - {"dateTime": "2025-08-7T16:30:00", "timeZone": "Asia/Kolkata"} (with timeZone field)
                   - {"dateTime": "2025-08-7T16:30:00Z", "timeZone": "UTC"} (UTC time)
            end: End time of the event (required). Must include timezone offset or timeZone field.
                 Examples:
                 - {"dateTime": "2025-08-7T17:30:00+05:30"} (with offset)
                 - {"dateTime": "2025-08-7T17:30:00", "timeZone": "Asia/Kolkata"} (with timeZone field)
                 - {"dateTime": "2025-08-7T17:30:00Z", "timeZone": "UTC"} (UTC time)
            summary: Event title/summary (required). Example: "Updated Meeting"
            description: Event description. Example: "Updated description"
            location: Event location. Example: "Updated Location"
            attendees: List of attendee dictionaries. Example: [{"email": "example@gmail.com"}]
            recurrence: List of RRULE, RDATE, or EXDATE strings for recurring events (optional).
                       Example: ["RRULE:FREQ=WEEKLY;COUNT=5;BYDAY=TU,FR"]
            calendar_id: Calendar identifier (default: "primary")
            send_updates: Specifies who should receive event notifications: 'all', 'externalOnly', or 'none' (default)
            max_attendees: Maximum number of attendees to include in the response (optional)

        Returns:
            Dictionary containing the complete API response with the updated event details

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code

        Tags:
            update, calendar, event, modify, important
        """
        request_body_data = {
            "start": start,
            "end": end,
            "summary": summary,
            "description": description,
            "location": location,
            "attendees": attendees,
            "recurrence": recurrence,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }

        url = f"{self.base_url}/calendars/{calendar_id}/events/{event_id}"
        params = {"sendUpdates": send_updates}
        if max_attendees is not None:
            params["maxAttendees"] = str(max_attendees)

        logger.info(f"Updating calendar event with ID: {event_id}")
        response = self._put(url, data=request_body_data, params=params)

        return self._handle_response(response)

    def get_primary_calendar_details(self) -> dict[str, Any]:
        """
        Retrieves metadata for the user's primary calendar, including its default timezone. This information is essential for creating new events with accurate, timezone-aware start and end times using other functions like `create_event`, preventing potential scheduling errors across different regions.

        Returns:
            Dictionary containing the user's timezone information

        Raises:
            HTTPError: Raised when the API request fails or returns an error status code

        Tags:
            get, calendar, timezone, settings, important
        """
        url = f"{self.base_api_url}"
        logger.info("Retrieving user's calendar timezone settings")
        response = self._get(url)
        return self._handle_response(response)

    def get_free_busy_info(
        self,
        alt=None,
        fields=None,
        key=None,
        oauth_token=None,
        prettyPrint=None,
        quotaUser=None,
        userIp=None,
        calendarExpansionMax=None,
        groupExpansionMax=None,
        items=None,
        timeMax=None,
        timeMin=None,
        timeZone=None,
    ) -> dict[str, Any]:
        """
        Queries the free/busy status for one or more calendars within a specified time range. It returns a list of busy time intervals, making it ideal for finding open slots and scheduling new events without conflicts.


        Args:
            alt (string): Data format for the response. Example: 'json'.
            fields (string): Selector specifying which fields to include in a partial response. Example: 'amet in'.
            key (string): API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. Example: 'amet in'.
            oauth_token (string): OAuth 2.0 token for the current user. Example: 'amet in'.
            prettyPrint (string): Returns response with indentations and line breaks. Example: 'true'.
            quotaUser (string): An opaque string that represents a user for quota purposes. Must not exceed 40 characters. Example: 'amet in'.
            userIp (string): Deprecated. Please use quotaUser instead. Example: 'amet in'.
            calendarExpansionMax (number): calendarExpansionMax Example: '37977981'.
            groupExpansionMax (number): groupExpansionMax Example: '-92198829'.
            items (array): items Example: "[{'id': 'qui labore velit in anim'}, {'id': 'sed dolore dolor laborum eiusmod'}]".
            timeMax (string): timeMax Example: '2016-10-26T20:45:39.467Z'.
            timeMin (string): timeMin Example: '1971-06-26T00:25:33.327Z'.
            timeZone (string): timeZone
                Example:
                ```json
                {
                  "calendarExpansionMax": 37977981,
                  "groupExpansionMax": -92198829,
                  "items": [
                    {
                      "id": "qui labore velit in anim"
                    },
                    {
                      "id": "sed dolore dolor laborum eiusmod"
                    }
                  ],
                  "timeMax": "2016-10-26T20:45:39.467Z",
                  "timeMin": "1971-06-26T00:25:33.327Z",
                  "timeZone": "UTC"
                }
                ```

        Returns:
            dict[str, Any]: Successful response
        """
        request_body = {
            "calendarExpansionMax": calendarExpansionMax,
            "groupExpansionMax": groupExpansionMax,
            "items": items,
            "timeMax": timeMax,
            "timeMin": timeMin,
            "timeZone": timeZone,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/freeBusy"
        query_params = {
            k: v
            for k, v in [
                ("alt", alt),
                ("fields", fields),
                ("key", key),
                ("oauth_token", oauth_token),
                ("prettyPrint", prettyPrint),
                ("quotaUser", quotaUser),
                ("userIp", userIp),
            ]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_event_by_id,
            self.get_upcoming_events,
            self.list_events,
            self.create_event_from_text,
            self.create_event,
            self.replace_event,
            self.list_recurring_event_instances,
            self.get_primary_calendar_details,
            # Auto Generated from Openapi spec
            self.delete_event,
            self.get_free_busy_info,
        ]
