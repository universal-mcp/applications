# CalComV2App MCP Server

An MCP Server for the CalComV2App API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the CalComV2App API.


| Tool | Description |
|------|-------------|
| `get_provider_details` | Retrieves information for a provider using the client ID provided in the path. |
| `get_provider_access_token` | Retrieves an access token for the specified client ID using a GET request. |
| `gcal_controller_redirect` | Retrieves and returns an authorization URL for Google Calendar OAuth using the "GET" method at the "/v2/gcal/oauth/auth-url" path. |
| `gcal_controller_save` | Handles Google Calendar OAuth 2.0 authorization callback by exchanging an authorization code for an access token and saving credentials. |
| `gcal_controller_check` | Checks the Google Calendar availability or status using the v2 API and returns a success response if valid. |
| `list_client_users` | Retrieves a list of users associated with a specific OAuth client ID, optionally limited by the specified query parameter. |
| `create_oauth_client_user` | Creates a new user for an OAuth client specified by the `clientId` and returns a successful response with a 201 status code. |
| `get_oauth_client_user_by_id` | Retrieves user-specific information associated with an OAuth client using the provided client ID and user ID. |
| `patch_oauth_client_user_by_id` | Updates the association of a user with a specified OAuth client using the PATCH method on the "/v2/oauth-clients/{clientId}/users/{userId}" path. |
| `delete_user_by_client_id_id` | Removes a user's association with an OAuth client identified by the client ID and user ID. |
| `force_refresh_user` | Forces a refresh for the OAuth client's user session, invalidating existing tokens and generating new ones. |
| `refresh_oauth_client_token` | Refreshes an access token for a specified client using OAuth 2.0, allowing the client to obtain a new access token without user interaction. |
| `create_oauth_client_webhook` | Creates a webhook for an OAuth client using the client ID specified in the path, enabling event-driven communication. |
| `list_webhooks_by_client_id` | Retrieves a paginated list of webhooks associated with a specific OAuth client using clientId, take, and skip parameters for pagination. |
| `delete_client_webhook` | Deletes a webhook associated with an OAuth client identified by the provided client ID using the DELETE method. |
| `update_webhook` | Updates an existing webhook for a specified OAuth client using the "PATCH" method, modifying its configuration as needed. |
| `get_oauth_client_webhook_by_id` | Retrieves information about a specific webhook associated with an OAuth client using the "GET" method at the specified path. |
| `delete_oauth_client_webhook_by_id` | Deletes a webhook associated with a specific OAuth client using the provided client and webhook IDs. |
| `list_org_attributes` | Retrieves a list of organization attributes filtered by pagination parameters. |
| `create_org_attributes` | Adds new attributes to an organization using the API, specifying the organization ID in the path, and returns a successful creation status. |
| `fetch_organization_attribute_by_id` | Retrieves a specific attribute for an organization based on the provided orgId and attributeId. |
| `update_organization_attribute` | Modifies an attribute of an organization using the PATCH method, updating the specified attribute by ID within the given organization. |
| `delete_org_attribute` | Deletes a specified attribute from an organization using the provided orgId and attributeId path parameters. |
| `create_org_attribute_option` | Creates a new option for the specified attribute in the given organization and returns the created resource. |
| `get_org_attribute_options` | Retrieves options for a specific attribute within an organization using the "GET" method at the "/v2/organizations/{orgId}/attributes/{attributeId}/options" endpoint. |
| `delete_attribute_option_by_id` | Deletes a specific attribute option for an organization's custom attributes using the provided orgId, attributeId, and optionId. |
| `patch_option_by_id` | Updates a specific option for an organization's attribute using partial modifications. |
| `set_user_attribute_option` | Assigns attribute options to a user within an organization using the POST method and returns a creation status. |
| `get_user_org_attribute_options` | Retrieves attribute options for a specified user within an organization using the "GET" method. |
| `delete_attribute_option` | Deletes a specific attribute option for a user within an organization via the provided path parameters. |
| `create_event_type` | Creates a new event type within a specified team and organization. |
| `list_event_types_by_team_and_org` | Retrieves event types for a specific team within an organization using the "GET" method at the "/v2/organizations/{orgId}/teams/{teamId}/event-types" endpoint, optionally filtering by event slug. |
| `get_event_types_by_team_id` | Retrieves details about a specific event type within a team of an organization using the provided organization ID, team ID, and event type ID. |
| `create_phone_call_event` | Initiates a phone call for a specific event type under an organization's team context and returns a 201 Created response upon successful creation. |
| `list_event_types_by_org_id` | Retrieves a paginated list of event types for teams within a specified organization. |
| `list_organization_memberships` | Retrieves a list of memberships for an organization identified by the specified `orgId`, allowing pagination through optional `take` and `skip` query parameters. |
| `create_membership` | Creates a new membership for an organization identified by {orgId} using the API. |
| `get_org_membership_by_id` | Retrieves membership details for a specific organization membership using the provided organization ID and membership ID. |
| `delete_org_membership_by_id` | Removes a user's membership from the specified organization by deleting the membership record at the given path. |
| `update_membership_by_id_org` | Updates an organization membership's details using the PATCH method and returns the updated membership data. |
| `get_organization_schedules` | Retrieves a list of schedules for the specified organization, using pagination parameters to limit results. |
| `create_user_schedule` | Creates a schedule for the specified user within an organization and returns a success status upon creation. |
| `get_user_schedule` | Retrieves a user's schedule for a specific organization using the GET method. |
| `get_schedule_detail` | Retrieves the specified schedule for a user within an organization. |
| `update_user_schedule_by_id` | Updates a user's schedule for a specified organization by applying partial modifications to the schedule's details using the PATCH method. |
| `delete_user_schedule_by_id` | Deletes a specific schedule for a user within an organization and returns a success status. |
| `get_organization_teams` | Retrieves a list of teams for a specified organization using the provided orgId, with optional pagination control via take and skip parameters. |
| `create_team_in_organization` | Creates a new team within the specified organization using the provided organization ID and returns a success status upon creation. |
| `get_organization_team_me` | Retrieves the teams for the current user within a specified organization using the "GET" method, optionally allowing pagination through query parameters. |
| `get_organization_team_by_id` | Retrieves information about a specific team within an organization using the organization and team IDs. |
| `delete_team_by_id` | Deletes a specific team within an organization and returns a success status upon completion. |
| `update_team` | Updates the specified team properties within an organization using partial modifications. |
| `list_team_memberships` | Retrieves a paginated list of memberships for a specified team within an organization, using path parameters for orgId and teamId, and query parameters for pagination (take and skip). |
| `create_team_membership` | Adds a member to the specified team within an organization and returns the membership details. |
| `get_membership_details` | Retrieves a specific membership record for a team within an organization, identified by membership ID, team ID, and organization ID. |
| `delete_org_team_membership_by_id` | Removes a user's team membership in an organization using the specified organization, team, and membership identifiers. |
| `patch_team_membership_by_id` | Updates membership details for a specific organization team member using partial modifications and returns a success status. |
| `get_schedule_by_user` | Retrieves the schedule details for a specific user within a designated team and organization. |
| `list_org_users` | Retrieves a list of users for a specified organization, allowing filtering by take, skip, and emails parameters, using the GET method on the "/v2/organizations/{orgId}/users" endpoint. |
| `create_org_user` | Creates a new user within an organization using the provided organization ID. |
| `delete_member_by_id` | Deletes a user with the specified user ID from an organization identified by the provided organization ID using the DELETE method, returning a status message upon success. |
| `get_org_webhooks` | Retrieves a list of webhooks for the specified organization, supporting pagination through skip and take parameters. |
| `create_webhook` | Creates an organization webhook that triggers HTTP POST payloads for specified events and returns a success status on creation. |
| `get_organization_webhook_by_id` | Retrieves information about a specific webhook identified by `webhookId` for an organization specified by `orgId`. |
| `delete_organization_webhook_by_id` | Deletes a specified webhook from an organization using the provided organization and webhook identifiers. |
| `update_webhook_by_id` | Updates a specific webhook for an organization using partial modifications via the PATCH method. |
| `list_bookings` | Retrieves a filtered list of bookings based on parameters like status, attendee details, event types, time ranges, and pagination settings. |
| `get_booking_by_uid` | Retrieves the details of a specific booking using its unique identifier. |
| `reschedule_booking_by_uid` | Reschedules an existing booking identified by its unique `bookingUid`, using the `POST` method at the "/v2/bookings/{bookingUid}/reschedule" endpoint. |
| `cancel_booking_by_uid` | Cancels a booking by sending a POST request to the "/v2/bookings/{bookingUid}/cancel" endpoint, using the provided booking UID to identify the booking to be canceled. |
| `mark_booking_absent_by_uid` | Marks a booking as absent using the provided booking UID and authentication token, indicating that the owner of the booking is absent. |
| `reassign_booking` | Reassigns a booking to a different team member or booking page via a POST request to the specified booking UID, potentially allowing double bookings if availability conflicts exist. |
| `reassign_booking_to_user` | Reassigns a booking to a specific user specified by the `userId` using a POST request, requiring authorization and providing a reason for the reassignment. |
| `confirm_booking` | Confirms a specific booking by its unique identifier and returns a success status upon completion. |
| `decline_booking` | Declines a specific booking identified by the bookingUid using the Booking.com API and returns a success status upon completion. |
| `save_ics_feed_post` | Saves an ICS calendar feed configuration and returns the created resource. |
| `check_ics_feed` | Checks the status and validity of an ICS calendar feed. |
| `get_calendars_busy_times` | Retrieves a list of busy times for specified calendars within a given date range using the "GET" method at "/v2/calendars/busy-times," allowing for time zone and credential specification. |
| `get_calendars` | Retrieves a list of calendars using the API at the "/v2/calendars" endpoint via the GET method. |
| `calendars_controller_redirect` | Retrieves a connection status for the specified calendar at path "/v2/calendars/{calendar}/connect" using the GET method, requiring authorization and calendar identifier. |
| `calendars_controller_save` | Retrieves the saved state of a specified calendar using the given parameters. |
| `create_calendar_credentials` | Creates credentials for a specified Google Calendar using the POST method at the "/v2/calendars/{calendar}/credentials" path. |
| `calendars_controller_check` | Checks the status or availability of a specified calendar using the "GET" method at the "/v2/calendars/{calendar}/check" endpoint. |
| `disconnect_calendar` | Disconnects a specified calendar from a user's account using the Cal.com API, requiring a POST request to the "/v2/calendars/{calendar}/disconnect" endpoint with the calendar type and credential ID in the request body. |
| `conferencing_controller_connect` | Establishes a connection for conferencing using the specified application via the POST method at the "/v2/conferencing/{app}/connect" endpoint. |
| `get_auth_url` | Generates an authorization URL for OAuth in a conferencing application using the "GET" method at the "/v2/conferencing/{app}/oauth/auth-url" path, accepting parameters such as the application name and return URLs. |
| `conferencing_controller_save` | Handles OAuth authorization callbacks for conferencing applications, processing authorization codes and states to authenticate users via the "GET" method. |
| `list_conferencing` | Retrieves conferencing data using the "GET" method at the "/v2/conferencing" endpoint, returning relevant information. |
| `conferencing_controller_default` | Sets the default conferencing application for the specified app identifier. |
| `get_default_conferencing` | Retrieves the default conferencing configuration from the API. |
| `disconnect_conferencing_app` | Disconnects all participants from a specified conferencing application instance using the path parameter and returns a success response upon completion. |
| `update_destination_calendars` | Updates a destination calendar at the specified path "/v2/destination-calendars" using the PUT method. |
| `list_event_types` | Retrieves a list of event types using the GET method, allowing filtering by username, event slug, usernames list, organization slug, and organization ID through query parameters. |
| `get_event_type_by_id` | Retrieves detailed information about a specific event type by its ID using the Events API. |
| `delete_event_type_by_id` | Deletes the specified event type using the provided ID and returns a success status upon completion. |
| `create_event_type_webhook` | Creates a webhook subscription for a specific event type, returning a success status upon creation. |
| `get_event_webhooks` | Retrieves a list of webhooks configured for a specific event type, supporting pagination via take and skip parameters. |
| `delete_event_webhook` | Deletes a webhook associated with a specific event type ID using the DELETE method. |
| `patch_event_type_webhook_by_id` | Updates a webhook associated with a specific event type using the PATCH method, modifying its properties at the path "/v2/event-types/{eventTypeId}/webhooks/{webhookId}". |
| `get_webhook_by_id` | Retrieves details about a specific webhook for a given event type using the provided event type ID and webhook ID. |
| `delete_event_type_webhook_by_id` | Deletes a webhook associated with a specific event type using the provided `eventTypeId` and `webhookId` parameters. |
| `me_controller_get_me` | Retrieves the authenticated user's profile information and returns it in the API response. |
| `me_controller_update_me` | Updates the properties of the current user's profile at the "/v2/me" path using the PATCH method. |
| `create_schedule` | Creates a new schedule using the provided data and returns a successful creation response with a 201 status code. |
| `list_schedules` | Retrieves a list of schedules using specified authorization headers and API version. |
| `get_default_schedule` | Retrieves the default schedule of the authenticated user using the Cal.com API, returning relevant scheduling information. |
| `get_schedule_by_id` | Retrieves a specific schedule by its ID using the "GET" method at the "/v2/schedules/{scheduleId}" endpoint. |
| `update_schedule_by_id` | Updates a schedule's configuration partially by specifying scheduleId and modified fields in the request body, returning a success status upon completion. |
| `delete_schedule_by_id` | Deletes a specific schedule identified by the `scheduleId` using the `DELETE` method. |
| `add_selected_calendar` | Creates a new selected calendar entry for external integrations using provided identifiers. |
| `delete_selected_calendars` | Deletes one or more selected calendars based on integration, external ID, and credential ID using the DELETE method at the "/v2/selected-calendars" path. |
| `slots_controller_reserve_slot` | Reserves a slot using the "POST" method at "/v2/slots/reserve", creating a new reservation and returning a successful response when the operation is completed. |
| `delete_selected_slot` | Deletes the specified slot identified by the uid parameter and returns a successful response upon completion. |
| `list_available_slots` | Retrieves a list of available slots within a specified time range, filtered by event type, user list, and other criteria, using the `GET` method at `/v2/slots/available`. |
| `stripe_controller_redirect` | Retrieves details of a connected Stripe account using the Stripe-Account header for authorization. |
| `stripe_controller_save` | Retrieves a Stripe resource using a state and code query parameter and returns the result upon successful authentication. |
| `stripe_controller_check` | Checks system status or configuration in Stripe's v2 API and returns a success response. |
| `get_team_stripe_check` | Retrieves Stripe payment or subscription data for a specific team using the provided `teamId` and returns relevant information via a GET request. |
| `teams_controller_create_team` | Creates a new team using the API and returns a successful response with a 201 status code, indicating the creation of a resource. |
| `teams_controller_get_teams` | Retrieves a list of teams and returns their details in the response. |
| `teams_controller_get_team` | Retrieves information about a team specified by the team ID using the GET method. |
| `teams_controller_update_team` | Updates team configuration details for the specified team ID. |
| `teams_controller_delete_team` | Deletes a specified team using the provided team ID. |
| `create_team_event_type` | Creates a new event type for a specified team using the API and returns a successful creation status. |
| `get_team_event_types` | Retrieves a list of event types for a specified team using the provided team ID and optionally filters by event slug. |
| `get_event_type_by_team_id` | Retrieves details about a specific event type within a team using the "GET" method, requiring both team ID and event type ID as path parameters. |
| `delete_team_event_type_by_id` | Deletes a specific event type for a team using the provided path parameters. |
| `create_phone_call_for_event` | Creates a phone call for a specific event type within a team using the "POST" method, returning a successful creation status. |
| `add_team_membership` | Adds multiple users to a team using their organization membership IDs through a POST request to the specified team endpoint. |
| `get_team_memberships` | Retrieves paginated membership details for a specific team using `take` and `skip` parameters to manage results. |
| `get_membership_by_id` | Retrieves the membership details for a specific user in a team using the provided membership ID. |
| `update_membership` | Updates the membership role for a user in a specific team using the GitHub API and returns a success status. |
| `deletegithub_membership_by_id` | Removes a user's team membership in GitHub, requiring admin permissions or organization ownership. |
| `get_timezones` | Retrieves a list of time zones with associated metadata, including codes, descriptions, and identifiers. |
| `createandconfigure_webhook` | Creates and configures a webhook endpoint to receive HTTP POST notifications for specific events, returning a success response upon creation. |
| `webhooks_controller_get_webhooks` | Retrieves a list of webhooks, allowing pagination with optional parameters to specify the number of items to take and skip. |
| `patch_webhook` | Updates a webhook identified by its ID using the PATCH method to modify its configuration. |
| `webhooks_controller_get_webhook` | Retrieves information about a specific webhook identified by its ID using the "GET" method. |
| `delete_user_webhook_by_id` | Deletes a webhook by its ID using the DELETE method at the "/v2/webhooks/{webhookId}" path, removing the specified webhook endpoint. |
