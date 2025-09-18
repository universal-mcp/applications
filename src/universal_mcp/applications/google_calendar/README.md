# GoogleCalendarApp MCP Server

An MCP Server for the GoogleCalendarApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the GoogleCalendarApp API.


| Tool | Description |
|------|-------------|
| `get_event_by_id` | Retrieves a specific calendar event using its unique ID. Unlike `list_events`, which fetches multiple events based on date ranges or search queries, this function targets a single, known event. It can optionally limit attendees returned and specify a time zone for date formatting in the response. |
| `get_upcoming_events` | Retrieves events for a specified number of days, starting from today. This function simplifies date-range queries by auto-calculating start/end times, unlike the more comprehensive `list_events` function, which offers granular control with explicit time filters, text search, and custom sorting. |
| `list_events` | Fetches a customizable list of events using filters for date range, text search, sorting, and pagination. This advanced function provides more granular control than `get_upcoming_events`, which is limited to fetching events for a specific number of upcoming days. |
| `create_event_from_text` | Creates a calendar event by parsing a natural language string (e.g., "Meeting tomorrow at 10am"). This offers a user-friendly shortcut, contrasting with the structured `create_event` function which requires explicit fields like start and end times. |
| `create_event` | Creates a calendar event using structured data for start/end times, summary, attendees, and recurrence. This method provides precise control for complex appointments, unlike `create_event_from_text` which parses natural language, making it ideal for detailed or recurring event creation. |
| `replace_event` | Replaces an existing calendar event, identified by its ID, with new data. This function performs a full update, overwriting all event properties like start/end times and summary. It does not support partial modifications, requiring all necessary fields for the replacement to be provided. |
| `list_recurring_event_instances` | Retrieves all individual occurrences of a specific recurring event using its ID. Unlike `list_events`, which fetches multiple distinct events, this function expands a single recurring event into its separate instances, allowing filtering by time range and pagination for detailed scheduling views. |
| `get_primary_calendar_details` | Retrieves metadata for the user's primary calendar, including its default timezone. This information is essential for creating new events with accurate, timezone-aware start and end times using other functions like `create_event`, preventing potential scheduling errors across different regions. |
| `delete_event` | Permanently deletes a specific event from a Google Calendar using its event and calendar IDs. It can optionally send cancellation notifications to attendees, distinguishing it from functions that retrieve (`get_event_by_id`) or modify events (`replace_event`), which do not remove entries from the calendar. |
| `get_free_busy_info` | Queries the free/busy status for one or more calendars within a specified time range. It returns a list of busy time intervals, making it ideal for finding open slots and scheduling new events without conflicts. |
