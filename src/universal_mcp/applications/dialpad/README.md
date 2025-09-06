# DialpadApp MCP Server

An MCP Server for the DialpadApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the DialpadApp API.


| Tool | Description |
|------|-------------|
| `accesscontrolpolicies_assign` | Assigns an access control policy to a target entity using the provided policy ID and returns a success status. |
| `accesscontrolpolicies_list` | Retrieves a list of access control policies using the "GET" method, optionally paginating results with a cursor parameter. |
| `accesscontrolpolicies_create` | Creates a new access control policy using JSON data and returns a successful response upon completion. |
| `accesscontrolpolicies_delete` | Deletes the specified access control policy identified by the provided ID. |
| `accesscontrolpolicies_get` | Retrieves a specific access control policy by its ID using the GET method. |
| `accesscontrolpolicies_update` | Partially updates an existing access control policy by its ID using a JSON payload. |
| `accesscontrolpolicies_assignments` | Retrieves the assignments of an access control policy identified by the specified ID. |
| `accesscontrolpolicies_unassign` | Unassigns an access control policy from a specified ID using a POST request, allowing for the removal of policy assignments based on the provided ID. |
| `app_settings_get` | Retrieves application settings using the provided target ID and type from version 2 of the API. |
| `blockednumbers_add` | Adds a phone number to the blocked numbers list using a JSON-formatted request body and returns a success status. |
| `blockednumbers_get` | Retrieves information about a specific blocked number identified by the given number parameter. |
| `blockednumbers_remove` | Removes a blocked number using the POST method, sending data in JSON format to the defined API endpoint and returns a status response. |
| `blockednumbers_list` | Retrieves a list of blocked numbers using the provided cursor for pagination. |
| `call_participants_add` | Adds participants to a call using the provided call ID. |
| `call_get_call_info` | Retrieves details of a call resource by its unique identifier. |
| `call_initiate_ivr_call` | Initiates an outbound call to ring an IVR workflow by sending a POST request and returns a confirmation upon success[1]. |
| `call_list` | Retrieves a list of calls using the provided query parameters for filtering by cursor, start time, end time, target ID, and target type, and returns the results. |
| `call_call` | Initiates a call using a JSON payload and returns a successful response upon completion. |
| `call_transfer_call` | Transfers a call identified by the provided ID using the POST method, sending the request body in JSON format. |
| `call_unpark` | Unparks a call with the specified ID using the POST method. |
| `call_actions_hangup` | Hangs up a call with the specified ID using the PUT method. |
| `call_put_call_labels` | Updates the labels of a call with the specified ID using the provided JSON data. |
| `call_callback` | Registers a callback endpoint using a POST request to the "/api/v2/callback" path, accepting a JSON payload in the request body, and returns a successful response upon registration. |
| `call_validate_callback` | Validates a callback using the provided JSON data and returns a success response if the validation is successful. |
| `callcenters_listall` | Retrieves a list of call centers using the specified query parameters, such as cursor for pagination, office_id for filtering by office, and name_search for searching by name. |
| `callcenters_create` | Creates a new call center resource using JSON data and returns a successful response upon completion. |
| `callcenters_delete` | Deletes a call center identified by the specified ID. |
| `callcenters_get` | Retrieves details for the specified call center identified by its unique ID. |
| `callcenters_update` | Updates partial properties of the call center resource identified by the given ID using a JSON Patch document. |
| `callcenters_status` | Retrieves the status of a call center identified by the provided ID. |
| `callcenters_operators_get_dutystatus` | Retrieves the duty status of a specific call center operator identified by the provided ID. |
| `callcenters_operators_dutystatus` | Updates the duty status of a call center operator with the specified ID using the PATCH method and returns a 200 OK response upon success. |
| `callcenters_operators_get_skilllevel` | Retrieves the skill information for a specific operator associated with a given call center. |
| `callcenters_operators_skilllevel` | Updates the skill information for a specific operator in a call center using the PATCH method, requiring a JSON payload with the updated details. |
| `callcenters_operators_delete` | Deletes an operator associated with a specific call center identified by the provided ID. |
| `callcenters_operators_get` | Retrieves the list of operators associated with the specified call center by its ID. |
| `callcenters_operators_post` | Adds a new operator to the call center specified by the given ID using a JSON request body. |
| `calllabel_list` | Retrieves a list of call labels, optionally limited by the specified number of results. |
| `call_review_share_link_create` | Creates a shareable link for a call review, returning the generated link upon successful creation. |
| `call_review_share_link_delete` | Deletes a call review share link identified by the provided ID using the DELETE method. |
| `call_review_share_link_get` | Retrieves a share link for a call review by its ID using the Dialpad API. |
| `call_review_share_link_update` | Updates a call review share link for the specified ID using the provided JSON data. |
| `callrouters_list` | Retrieves a list of call routers, optionally filtered by office ID and paginated using a cursor. |
| `callrouters_create` | Creates a new call router configuration using the provided JSON data and returns a successful response upon completion. |
| `callrouters_delete` | Deletes a call router identified by the provided ID from the system. |
| `callrouters_get` | Retrieves details for a specific call router identified by its unique ID. |
| `callrouters_update` | Updates a call router with a specified ID using partial modifications via a JSON Patch document. |
| `numbers_assign_call_router_number_post` | Assigns a phone number to a call router with the specified ID using the provided JSON data. |
| `channels_delete` | Deletes the channel identified by the specified ID and returns a status response confirming the deletion. |
| `channels_get` | Retrieves information about a specific channel by its ID using the GET method. |
| `channels_list` | Retrieves a paginated list of channels, optionally filtered by state, using the provided cursor for pagination. |
| `channels_post` | Creates a new channel by submitting channel details in JSON format. |
| `channels_members_delete` | Removes a member from a channel specified by the given ID using the DELETE method. |
| `channels_members_list` | Get a list of members in a specific channel, optionally paginated using a cursor. |
| `channels_members_post` | Adds a member to a channel specified by the provided ID using the provided JSON data. |
| `coaching_team_members_get` | Retrieves the members of a coaching team identified by the provided ID. |
| `coaching_team_members_add` | Adds a new member to a coaching team identified by the provided ID using the POST method and returns a status message. |
| `coaching_team_get` | Retrieves information about a coaching team specified by its identifier using the GET method. |
| `coaching_team_listall` | Retrieves a list of coaching teams using the GET method, optionally allowing pagination with a cursor query parameter. |
| `company_get` | Retrieves company data using the "GET" method at the "/api/v2/company" endpoint and returns the response. |
| `company_sms_opt_out` | Retrieves a list of SMS opt-out information for a specified company, filtered by optional parameters such as a2p campaign ID and cursor, with a required opt-out state parameter. |
| `conference_rooms_list` | Retrieves a list of conference rooms using the "GET" method, optionally paginating results with a query parameter cursor, secured by either an API key in the URL or a Bearer token. |
| `conference_meetings_list` | Retrieves a list of meetings for a conference, allowing optional filtering by room ID and pagination using a cursor. |
| `contacts_delete` | Deletes a specific contact by ID and removes all associated list memberships for that contact. |
| `contacts_get` | Retrieves detailed information for a specific contact identified by the given ID. |
| `contacts_update` | Partially updates the contact resource identified by the given ID with the provided JSON data. |
| `contacts_list` | Retrieves a paginated list of contacts, optionally filtered by owner and local inclusion status. |
| `contacts_create` | Creates or updates one or multiple contacts by submitting their data in JSON format to the server. |
| `contacts_create_with_uid` | Updates or replaces the entire contact resource at the specified path with the provided request data, returning a status code on success. |
| `ivr_delete` | Deletes a specific customer IVR configuration based on the target type, target ID, and IVR type using the provided JSON payload. |
| `ivr_update` | Modifies a custom IVR configuration using the PATCH method by updating specific properties for a target identified by type, ID, and IVR type. |
| `custom_ivrs_get` | Retrieves custom IVR data based on the specified target type and ID, with optional pagination using a cursor. |
| `ivr_create` | Creates a new custom IVR entry via API and returns a confirmation upon success. |
| `ivr_details_update` | Updates a custom IVR configuration identified by the `ivr_id` using partial modifications specified in the JSON request body. |
| `departments_delete` | Deletes the department identified by the specified ID from the system. |
| `departments_get` | Retrieves detailed information for a department by its ID using the GET method. |
| `departments_update` | Updates a department partially using the provided JSON data at the specified department ID. |
| `departments_listall` | Retrieves a list of departments, optionally filtered by office ID or name, and supports pagination via cursor. |
| `departments_create` | Creates a new department resource using the provided JSON data and returns a successful response if the operation is completed. |
| `departments_operators_delete` | Deletes a department operator by ID using the specified API endpoint and returns a status message. |
| `departments_operators_get` | Retrieves information about operators associated with a specific department by department ID using the GET method. |
| `departments_operators_post` | Creates a new operator for the specified department and returns a successful status on completion. |
| `faxline_create` | Creates a new fax line resource using the provided JSON data and returns a successful response upon creation. |
| `numbers_assign_number_post` | Assigns a specified number to a resource by sending a POST request with the number as a path parameter and the assignment details in the request body. |
| `numbers_assign_target_number_post` | Assigns numbers using a JSON payload in the request body via the "POST" method and returns a successful response upon completion. |
| `numbers_delete` | Deletes a number resource identified by the path parameter "number" and optionally considers the "release" status if specified in the query. |
| `numbers_get` | Retrieves information for a specific number using the provided number identifier. |
| `numbers_list` | Retrieves a list of numbers with optional filtering by status and supports pagination using a cursor parameter. |
| `format_post` | Formats a given number according to the specified country code and returns the formatted result. |
| `oauth2_authorize_get` | Initiates the OAuth 2.0 authorization code flow by redirecting the user to authenticate and grant permissions, then redirects back to the specified callback URL with an authorization code or error. |
| `oauth2_deauthorize_post` | Revokes OAuth 2.0 access tokens associated with the client or user, returning a successful response with no content. |
| `plan_get` | Retrieves the plan details for a specified office identified by its office_id. |
| `callcenters_list` | Retrieves a list of call centers associated with a specific office, supporting pagination via a cursor parameter. |
| `coaching_team_list` | Retrieves a list of teams associated with a specific office, identified by the office ID provided in the path, with optional pagination using the cursor query parameter. |
| `departments_list` | Retrieves a list of departments associated with a specific office identified by the provided office ID. |
| `numbers_assign_office_number_post` | Assigns a phone number to an office identified by the specified ID using a JSON request body. |
| `numbers_office_unassign_number_post` | Unassigns a phone number from an office using the POST method by specifying the office ID in the path and providing additional details in the JSON request body. |
| `offices_e911_get` | Retrieves Enhanced 911 (E911) information for a specific office identified by the provided office ID. |
| `offices_e911_update` | Updates or replaces the E911 configuration for the specified office using the provided data in the request body. |
| `plan_available_licenses_get` | Retrieves the available licenses for a specific office identified by its ID. |
| `offices_offdutystatuses_get` | Retrieves a list of off-duty statuses for the specified office, identified by its ID. |
| `offices_get` | Retrieves details about a specific office by ID using the API. |
| `offices_list` | Retrieves a list of offices, optionally filtering by active status and supporting pagination with a cursor parameter. |
| `offices_create` | Creates a new office using the provided JSON data in the request body. |
| `offices_operators_delete` | Deletes the specified operator(s) associated with the office whose ID is provided in the path, returning a success status upon completion. |
| `offices_operators_get` | Get the list of operators associated with the specified office by its ID. |
| `offices_operators_post` | Creates a new operator resource within the specified office using the provided data and returns a success status. |
| `recording_share_link_create` | Creates a recording share link by accepting JSON input and returns a success response upon completion. |
| `recording_share_link_delete` | Deletes the recording share link identified by the specified ID and returns a confirmation upon successful completion. |
| `recording_share_link_get` | Retrieves a recording share link by its ID using the GET method. |
| `recording_share_link_update` | Updates or replaces the recording share link resource identified by the given ID with the provided data. |
| `numbers_assign_room_number_post` | Assigns a number to the specified room and returns a success status. |
| `numbers_room_unassign_number_post` | Unassigns a phone number from a room using the API and returns a success status. |
| `rooms_delete` | Deletes a room by its ID and returns a successful response. |
| `rooms_get` | Retrieves details of a specific room identified by its ID using the GET method. |
| `rooms_patch` | Updates a room with the specified ID by partially modifying its properties using the provided JSON payload. |
| `rooms_list` | Retrieves a list of rooms, optionally filtered by office ID, using the provided cursor for pagination. |
| `rooms_post` | Creates a new room resource and returns a success response upon completion. |
| `deskphones_rooms_create_international_pin` | Creates an international PIN for a room and returns the result. |
| `deskphones_rooms_delete` | Deletes a deskphone with the specified ID from a room with the given parent ID using the DELETE method. |
| `deskphones_rooms_get` | Retrieves details of a specific desk phone identified by `{id}` within a room associated with `{parent_id}`. |
| `deskphones_rooms_list` | Retrieves a list of desk phones associated with a specific room, identified by the parent ID. |
| `schedule_reports_delete` | Deletes a schedule report by ID using the DELETE method, returning a successful response if the operation is completed. |
| `schedule_reports_get` | Retrieves a scheduled report by its ID using the "GET" method, returning details or results of the specified report. |
| `schedule_reports_update` | Updates a scheduled report by modifying specific properties of the resource identified by the provided ID using a JSON payload. |
| `schedule_reports_list` | Retrieves a list of scheduled reports, optionally paginated by a cursor, and returns them in response. |
| `schedule_reports_create` | Schedules reports for retrieval using the POST method, sending a JSON request to configure the reporting parameters. |
| `sms_send` | Sends an SMS message using the provided JSON data in the request body and returns a status message upon successful execution. |
| `stats_get` | Retrieves statistics for the specified resource identified by the provided ID. |
| `stats_create` | Submits statistical data via a POST request to the "/api/v2/stats" endpoint and expects a successful (200) response upon completion. |
| `webhook_agent_status_event_subscription_list` | Retrieves the current status of agent subscriptions, optionally paginated using a cursor parameter. |
| `webhook_agent_status_event_subscription_create` | Updates the agent status for a subscription using JSON data and returns a successful response. |
| `webhook_agent_status_event_subscription_delete` | Deletes an agent status event subscription by its unique identifier. |
| `webhook_agent_status_event_subscription_get` | Retrieves the status information of a subscription agent identified by the given ID. |
| `webhook_agent_status_event_subscription_update` | Updates the status of a specific agent subscription using a JSON payload. |
| `webhook_call_event_subscription_list` | Retrieves information about a call subscription using optional parameters for cursor, target type, and target ID. |
| `webhook_call_event_subscription_create` | Subscribes a user to a call notification service using a JSON payload and returns a success response upon successful subscription. |
| `webhook_call_event_subscription_delete` | Cancels a subscription identified by the provided ID using the DELETE method, preventing future charges and updating the subscription status to canceled. |
| `webhook_call_event_subscription_get` | Retrieves the subscription details identified by the specified subscription ID. |
| `webhook_call_event_subscription_update` | Partially updates a subscription identified by the provided ID using the PATCH method, allowing for selective modification of specific fields in the subscription resource. |
| `webhook_change_log_event_subscription_list` | Retrieves a changelog of subscription updates using the "GET" method, optionally filtering results by a specified cursor, and authenticates via either an API key or Bearer token. |
| `webhook_change_log_event_subscription_create` | Submits a subscription changelog entry by posting JSON data and returns a 200 response if successful, with authentication handled via API key or bearer token. |
| `webhook_change_log_event_subscription_delete` | Deletes a specific changelog entry identified by the provided ID using the "DELETE" method. |
| `webhook_change_log_event_subscription_get` | Retrieves the changelog for a specific subscription with the given ID using a GET request, requiring either an API key in the URL or a Bearer token for authentication. |
| `webhook_change_log_event_subscription_update` | Updates a specific changelog subscription by modifying its properties using a JSON patch document, and returns a status message indicating the success of the operation. |
| `webhook_contact_event_subscription_list` | Retrieves a list of contact details for subscriptions, allowing pagination via a cursor parameter. |
| `webhook_contact_event_subscription_create` | Creates a new contact subscription using the provided JSON data and returns a successful response. |
| `webhook_contact_event_subscription_delete` | Deletes a subscription associated with a specific contact ID, removing the subscription from the system and preventing future charges. |
| `webhook_contact_event_subscription_get` | Retrieves a subscription associated with a specific contact by their ID using the GET method. |
| `webhook_contact_event_subscription_update` | Modifies a specific subscription contact by ID using a JSON patch document to update its properties. |
| `webhook_sms_event_subscription_list` | Retrieves a list of SMS subscriptions, optionally filtered by cursor, target type, and target ID. |
| `webhook_sms_event_subscription_create` | Sends a subscription request for SMS notifications by creating an SMS subscription. |
| `webhook_sms_event_subscription_delete` | Cancels an SMS subscription by its ID using the DELETE method, removing future charges and updating the subscription status to reflect cancellation. |
| `webhook_sms_event_subscription_get` | Retrieves the details of a specific SMS subscription identified by the provided subscription ID. |
| `webhook_sms_event_subscription_update` | Updates an SMS subscription identified by its ID, modifying specific properties using JSON Patch operations. |
| `transcripts_get` | Retrieves a transcript for a specific call identified by the call ID using the GET method. |
| `transcripts_get_url` | Retrieves the URL for a transcript associated with a specific call ID using the GET method. |
| `userdevices_get` | Retrieves details about a user device specified by its ID using the GET method. |
| `userdevices_list` | Retrieves a list of user devices, optionally filtered by a user ID or a cursor for pagination. |
| `users_initiate_call` | Initiates a call for a user identified by the provided ID using the POST method, sending JSON data in the request body. |
| `users_update_active_call` | Updates the active call status for a user with the specified ID using the PATCH method and returns a status message. |
| `users_toggle_call_vi` | Toggles the "vi" setting for a user with the specified ID using the PATCH method. |
| `caller_id_users_get` | Retrieves the caller ID information for a user identified by the provided ID using the GET method. |
| `caller_id_users_post` | Updates the caller ID for a user with the specified ID using a JSON payload and returns a successful response upon completion. |
| `deskphones_users_delete` | Deletes a specific deskphone associated with a user identified by the parent ID and deskphone ID using the DELETE method. |
| `deskphones_users_get` | Retrieves details of a specific desk phone associated with a user, identified by the parent ID and desk phone ID. |
| `deskphones_users_list` | Retrieves a list of desk phones associated with a specific parent ID. |
| `numbers_assign_user_number_post` | Assigns a number to the user identified by the given ID using a POST request with JSON payload and returns a 200 status on success. |
| `numbers_user_unassign_number_post` | Unassigns a phone number from a user using the POST method by providing the user ID in the path and the necessary details in the JSON request body. |
| `users_toggle_dnd` | Toggles the DND status for a user with the specified ID using the PATCH method, accepting a JSON payload. |
| `users_e911_get` | Retrieves the Enhanced 911 (E911) information for a specific user identified by their ID. |
| `users_e911_update` | Updates the E911 (Enhanced 911) location information for a user identified by the specified ID. |
| `users_personas_get` | Retrieves the personas associated with a user identified by the provided `{id}` parameter using the `GET` method. |
| `screen_pop_initiate` | Triggers a screen pop for the specified user by their ID, requiring a JSON request body, and returns a success status upon completion. |
| `users_delete` | Deletes a user with the specified ID from the system, potentially removing associated data and roles. |
| `users_get` | Retrieves the details of a specific user identified by the provided ID. |
| `users_update` | Partially updates the user identified by the given ID with the specified JSON data and returns a success response. |
| `users_list` | Retrieves a list of users with optional filtering by cursor, state, company admin status, email, or number using the "/api/v2/users" GET endpoint. |
| `users_create` | Creates a new user resource using JSON data and returns a success response with a status code of 200 OK. |
| `users_move_office_patch` | Updates the office location of a user with the specified ID using a JSON payload. |
| `users_update_status` | Updates the status of a user with the specified ID using the PATCH method. |
| `webhooks_list` | Retrieves a list of webhooks, optionally supporting pagination with a cursor query parameter. |
| `webhooks_create` | Creates a new webhook endpoint that sends HTTP notifications in response to specified events. |
| `webhooks_delete` | Deletes the webhook with the specified ID and returns a success status. |
| `webhooks_get` | Retrieves details of a webhook by its ID using the "GET" method. |
| `webhook_update` | Updates a specific webhook resource by its ID using a partial payload sent via PATCH. |
| `websockets_list` | Establishes a WebSocket connection at "/api/v2/websockets" using the GET method, allowing optional specification of a cursor for resuming data consumption. |
| `websockets_create` | Establishes a WebSocket connection using the POST method to the "/api/v2/websockets" endpoint, accepting JSON data in the request body. |
| `websockets_delete` | Deletes a WebSocket by its ID, specified in the path, using the "DELETE" method. |
| `websockets_get` | Retrieves details for a specific WebSocket connection identified by its integer ID. |
| `websockets_update` | Updates the WebSocket connection resource identified by the specified ID using a JSON-formatted patch request. |
