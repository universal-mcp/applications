# PosthogApp MCP Server

An MCP Server for the PosthogApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the PosthogApp API.


| Tool | Description |
|------|-------------|
| `is_generating_demo_data_retrieve` | Checks if demo data is being generated for a specific project within an organization. |
| `reset_token_partial_update` | Resets the authentication token for a specific project within an organization and returns a success status. |
| `proxy_records_list` | Retrieves a paginated list of proxy records for a specified organization using query parameters for limit and offset. |
| `proxy_records_create` | Creates a proxy record for the specified organization using the provided organization ID. |
| `proxy_records_retrieve` | Retrieves a specific proxy record by its ID for a given organization using the PostHog API. |
| `proxy_records_update` | Updates a specific proxy record within an organization using the provided identifier and returns a status upon success. |
| `proxy_records_partial_update` | Updates a proxy record for an organization using the provided ID and organization ID, and returns a status message. |
| `proxy_records_destroy` | Deletes a specific proxy record identified by `{id}` within an organization specified by `{organization_id}` using the `DELETE` method. |
| `roles_list` | Retrieves a list of roles for a specified organization using the provided organization ID, with optional parameters to limit and offset the results. |
| `roles_create` | Creates a new role within the specified organization and returns the created resource upon success. |
| `roles_retrieve` | Retrieves a specific role within an organization based on the role and organization identifiers. |
| `roles_update` | Updates a specific role in an organization using the provided role ID and organization ID. |
| `roles_partial_update` | Updates the specified role within an organization using partial modifications via the PATCH method and returns a success response. |
| `roles_destroy` | Removes a specific role from an organization by its ID using a DELETE request and returns a 204 No Content response upon success. |
| `roles_role_memberships_list` | Retrieves a paginated list of role memberships for a specific role within an organization using query parameters for limit and offset. |
| `roles_role_memberships_create` | Assigns a role to an organization member by associating the role ID with the membership via a POST request. |
| `roles_role_memberships_destroy` | Removes a specific role membership from an organization role using the provided organization ID, role ID, and membership ID. |
| `actions_list` | Retrieves a list of actions for a specified project using the "GET" method, allowing optional filtering by format, limit, and offset. |
| `actions_create` | Creates an action for a specified project using the POST method and returns a status message upon success. |
| `notebooks_list` | Retrieves a list of notebooks for a specific project with optional filtering by content, creator, date range, and pagination parameters. |
| `notebooks_create` | Creates a new notebook for a specified project using the project ID. |
| `notebooks_retrieve` | Retrieves the details of a specific notebook identified by its short ID within a given project. |
| `notebooks_update` | Updates a notebook in the specified project and returns a success status. |
| `notebooks_partial_update` | Updates a notebook identified by its project ID and short ID using the provided data. |
| `notebooks_destroy` | Deletes a notebook specified by its short ID from a project identified by its project ID using the API. |
| `notebooks_activity_retrieve_2` | Retrieves the activity history for a specific notebook within a project. |
| `notebooks_activity_retrieve` | Retrieves activity information for a notebook within a specified project. |
| `notebooks_recording_comments_retrieve` | Retrieves a list of recording comments associated with a specific project by its ID. |
| `persons_list` | Retrieves a list of persons associated with a specific project, optionally filtered by distinct ID, email, properties, or search criteria. |
| `persons_retrieve` | Retrieves a specific person's details from a project using their ID and allows optional response formatting. |
| `persons_update` | Updates a specific person's details within a designated project and returns a success response upon completion. |
| `persons_partial_update` | Updates the details of a specific person associated with a project using the PATCH method, allowing for partial modification of the person's information. |
| `persons_destroy` | Deletes a specific person within a project, optionally removing associated events, without returning content. |
| `persons_activity_retrieve_2` | Retrieves activity information for a specific person within a project using the "GET" method. |
| `persons_delete_events_create` | Deletes events associated with a person in a project using the POST method and returns a status message. |
| `persons_delete_property_create` | Removes a specified property from a person within a project using a POST request, returning a success status on completion. |
| `persons_properties_timeline_retrieve` | Retrieves a timeline of property changes for a specific person in a project, optionally formatted. |
| `persons_split_create` | Splits a specified person into separate entities within a project and returns the operation result. |
| `persons_update_property_create` | Updates a property for a specified person within a project using the provided key and value. |
| `persons_activity_retrieve` | Retrieves activity data for persons associated with a specific project in the requested format. |
| `persons_bulk_delete_create` | Deletes multiple persons from a project in bulk using their IDs or distinct IDs, optionally including the deletion of associated events, via a POST request to `/api/projects/{project_id}/persons/bulk_delete/`. |
| `persons_cohorts_retrieve` | Retrieves a list of person cohorts for a specified project using the provided project ID. |
| `persons_funnel_retrieve` | Retrieves a list of persons in a funnel for a specific project using the project ID and optionally formats the output. |
| `persons_funnel_create` | Tracks user funnel data for a specific project and returns formatted results. |
| `persons_funnel_correlation_retrieve` | Retrieves correlation data for persons in a project, identified by the project ID, and optionally formats the output based on the specified format parameter. |
| `persons_funnel_correlation_create` | Calculates and returns the correlation between funnel data for individuals within a specified project using the POST method. |
| `persons_lifecycle_retrieve` | Retrieves lifecycle information for persons associated with a project, identified by the specified project ID, allowing optional format specification. |
| `persons_reset_person_distinct_id_create` | Resets and unlinks a person's distinct identifier in the specified project, clearing associated user data across devices or sessions. |
| `persons_stickiness_retrieve` | Retrieves stickiness data for persons associated with a specific project, optionally formatted. |
| `persons_trends_retrieve` | Retrieves trends related to persons in a specified project using the GET method and returns the data in a requested format. |
| `persons_values_retrieve` | Retrieves a list of person values for a specified project using the provided project ID. |
| `plugin_configs_logs_list` | Retrieves and returns log entries for a specific plugin configuration within a project, allowing pagination through query parameters for limit and offset. |
| `property_definitions_list` | Retrieves property definitions for a specific project with optional filtering for event names, excluded properties, hidden status, numerical type, and feature flags. |
| `property_definitions_retrieve` | Retrieves a specific property definition by ID for a given project. |
| `property_definitions_update` | Updates or replaces a specific property definition within a project using the PUT method, where the project and property definition are identified by their respective IDs. |
| `property_definitions_partial_update` | Updates a specific property definition for a project using the "PATCH" method, allowing partial modifications to the resource at "/api/projects/{project_id}/property_definitions/{id}/". |
| `property_definitions_destroy` | Deletes a specified property definition from a project using the provided project ID and property definition ID. |
| `property_definitions_seen_together_retrieve` | Retrieves property definitions that are commonly seen together for a specified project. |
| `query_create` | Submits a query to process or retrieve project-specific data and returns the results. |
| `query_retrieve` | Retrieves query details for a specific query within a project identified by the project ID and query ID. |
| `query_destroy` | Deletes a query identified by the given ID within a specified project using the DELETE method and returns a successful response without content upon deletion. |
| `query_check_auth_for_async_create` | Checks authorization for asynchronous operations on a specified project and returns the result. |
| `query_draft_sql_retrieve` | Retrieves draft SQL queries for a specified project using the project's ID. |
| `session_recording_playlists_list` | Retrieves a paginated list of session recording playlists for a specified project, filtered by creator, short ID, or other parameters. |
| `session_recording_playlists_create` | Creates a new session recording playlist for a specified project, allowing users to organize session recordings, using the PostHog API. |
| `session_recording_playlists_retrieve` | Retrieves a session recording playlist by project ID and short ID using the GET method. |
| `session_recording_playlists_update` | Updates a session recording playlist's configurations (name, description, filters, etc.) for a specified project and playlist identifier using the provided parameters. |
| `session_recording_playlists_partial_update` | Updates a session recording playlist for a specific project identified by project_id and playlist short_id. |
| `session_recording_playlists_destroy` | Deletes a session recording playlist in a specified project using its short identifier, returning a 405 status code (method not allowed for hard deletes). |
| `session_recording_playlists_recordings_retrieve` | Retrieves a list of recordings associated with a specific session recording playlist in a project. |
| `session_recording_playlists_recordings_create` | Creates a new recording for a session recording playlist within a specified project using the provided session recording ID and short ID. |
| `session_recording_playlists_recordings_destroy` | Deletes a specific session recording from a session recording playlist in a project using the provided project, playlist, and recording identifiers. |
| `session_recordings_list` | Retrieves a list of session recordings for a specified project, allowing pagination through limit and offset parameters. |
| `session_recordings_retrieve` | Retrieves a specific session recording for a project identified by project_id and session ID. |
| `session_recordings_update` | Updates or replaces a specific session recording within a project using the provided ID and returns a success status upon completion. |
| `session_recordings_partial_update` | Updates the specified session recording within a project with partial modifications using the PATCH HTTP method. |
| `session_recordings_destroy` | Deletes a specific session recording using the provided project ID and session recording ID. |
| `session_recordings_analyze_similar_retrieve` | Analyzes a session recording for similar recordings within a specific project using the provided project ID and session recording ID. |
| `session_recordings_sharing_list` | Retrieves sharing details for a specific session recording within a project. |
| `session_recordings_ai_regex_create` | Creates AI-powered regex session recordings for a specified project using the POST method. |
| `sessions_property_definitions_retrieve` | Retrieves property definitions associated with sessions for a specified project. |
| `sessions_values_retrieve` | Retrieves session values for a specific project identified by its project_id. |
| `subscriptions_list` | Retrieves a list of subscriptions for a specified project by project ID, allowing pagination through query parameters for limit and offset. |
| `subscriptions_create` | Creates a new subscription for a project using the provided project ID and returns a successful creation status. |
| `subscriptions_retrieve` | Retrieves details about a specific subscription within a project. |
| `subscriptions_update` | Updates an existing subscription associated with a specific project by replacing it with the provided data. |
| `subscriptions_partial_update` | Updates a subscription by partially modifying its properties, such as specified fields, using the "/api/projects/{project_id}/subscriptions/{id}/" endpoint with the PATCH method. |
| `subscriptions_destroy` | Deletes a specific subscription associated with a project by its identifier. |
| `surveys_list` | Retrieves a paginated list of surveys for a specific project with optional search and pagination parameters. |
| `surveys_create` | Creates a new survey under the specified project and returns a status message upon successful creation. |
| `surveys_retrieve` | Retrieves details for a specific survey in a project using the provided ID. |
| `surveys_update` | Updates a survey specified by its ID within a project identified by its ID using the PUT method. |
| `surveys_partial_update` | Updates a specific survey within a project by applying partial modifications and returns a success status. |
| `surveys_destroy` | Deletes a survey identified by `{id}` within a project specified by `{project_id}` using the HTTP DELETE method. |
| `surveys_activity_retrieve_2` | Retrieves the activity details for a specific survey within a project. |
| `surveys_stats_retrieve_2` | Retrieves aggregated response statistics for a specific survey within a project. |
| `surveys_summarize_responses_create` | Generates summarized insights from survey responses for a specified project and survey using AI-powered summarization. |
| `surveys_activity_retrieve` | Retrieves activity data for surveys associated with a specific project ID. |
| `surveys_responses_count_retrieve` | Retrieves the count of survey responses for a specified project using the project ID. |
| `surveys_stats_retrieve` | Retrieves aggregated response statistics across all surveys for a specified project, providing total counts and rates, using the "GET" method. |
| `web_experiments_list` | Retrieves a list of web experiments for a specified project using the Optimizely Web Experimentation API, allowing for pagination via optional limit and offset parameters. |
| `web_experiments_create` | Creates a new web experiment within a specified project using the Optimizely Web Experimentation API and returns a successful creation status message. |
| `web_experiments_retrieve` | Retrieves details about a specific web experiment defined by its ID within a specified project using the Optimizely Web Experimentation API. |
| `web_experiments_update` | Updates a web experiment for a specified project using the provided ID and returns a success status upon completion. |
| `web_experiments_partial_update` | Updates specific properties of a web experiment in a project using the PATCH method, returning a successful response upon modification. |
| `web_experiments_destroy` | Deletes a web experiment associated with a specified project using the project ID and experiment ID. |
| `users_list` | Retrieves a list of user records from the system, filtered by staff status, with optional pagination using limit and offset parameters. |
| `users_retrieve` | Retrieves user data for a specific user identified by the provided UUID using the GET method. |
| `users_update` | Updates or replaces a user's entire resource at the specified UUID endpoint using the provided data. |
| `users_partial_update` | Updates a specific user's details, identified by their UUID, using partial modifications via the PATCH method. |
| `users_hedgehog_config_retrieve` | Retrieves the hedgehog configuration for a user identified by the specified UUID. |
| `users_hedgehog_config_partial_update` | Updates the hedgehog configuration settings for a specific user identified by UUID using a PATCH request. |
| `users_scene_personalisation_create` | Sends a request to personalize a scene for a user identified by their UUID, enabling tailored experiences based on user-specific data. |
| `users_start_2fa_setup_retrieve` | Starts the setup process for two-factor authentication (2FA) for a user identified by their UUID. |
| `users_two_factor_backup_codes_create` | Generates and stores backup codes for two-factor authentication (2FA) associated with the specified user UUID. |
| `users_two_factor_disable_create` | Disables two-factor authentication for a specific user identified by their UUID. |
| `users_two_factor_start_setup_retrieve` | Initiates two-factor authentication setup for a user identified by their UUID, facilitating an additional security layer beyond the primary login credentials. |
| `users_two_factor_status_retrieve` | Retrieves the two-factor authentication status for a user identified by the specified UUID using the GET method. |
| `users_two_factor_validate_create` | Validates two-factor authentication for a user identified by the provided UUID using the POST method. |
| `users_validate_2fa_create` | Validates two-factor authentication for a user identified by the provided UUID using the API. |
| `users_request_email_verification_create` | Sends an email verification request to a user using the POST method at the path "/api/users/request_email_verification/". |
| `users_verify_email_create` | Verifies an email address for a user using a POST request to the "/api/users/verify_email/" endpoint. |
