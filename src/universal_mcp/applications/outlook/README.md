---
name: outlook
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# Outlook Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `reply_to_email` | Replies to a specific email message. |
| `send_email` | Sends a new email. |
| `get_email_folder` | Retrieves a specific email folder's metadata by its ID. |
| `list_emails` | Retrieves a list of emails from a user's mailbox. |
| `get_email` | Retrieves a specific email by its ID. |
| `delete_email` | Permanently deletes a specific email by its ID. |
| `list_email_attachments` | Retrieves attachments for a specific email. |
| `get_attachment` | Retrieves a specific attachment from an email message and formats it as a dictionary. |
| `get_my_profile` | Fetches the userPrincipalName for the currently authenticated user. |
| `get_next_page_results` | Retrieves the next page of results from a paginated API response. |
| `list_calendars` | Retrieves a list of calendars for the user. |
| `get_calendar` | Retrieves a specific calendar by its ID. |
| `create_calendar` | Creates a new calendar for the user. |
| `update_calendar` | Updates an existing calendar's name. |
| `delete_calendar` | Deletes a specific calendar. |
| `list_events` | Retrieves a list of events from a calendar or the user's default calendar. |
| `get_event` | Retrieves a specific event by its ID. |
| `create_event` | Creates a new event in a calendar. |
| `update_event` | Updates an existing event. |
| `delete_event` | Deletes a specific event. |
| `list_calendar_view` | Retrieves events between a start and end time (includes expanded recurring events). |
| `get_schedule` | Retrieves free/busy information for a set of users, groups, or resources. |
