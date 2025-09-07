# SentryApp MCP Server

An MCP Server for the SentryApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the SentryApp API.


| Tool | Description |
|------|-------------|
| `list_your_organizations` | Retrieves a list of organizations using the "GET" method, allowing filtering by owner, query, and sorting, and requires authentication with admin, read, or write permissions. |
| `retrieve_an_organization` | Retrieves detailed information about a specified organization by its ID or slug, optionally including extended details, requiring appropriate organizational permissions. |
| `update_an_organization` | Updates an existing organization using the provided JSON data, replacing its current details, and requires authentication with permissions to write or administer the organization. |
| `list_an_organization_s_metric_alert_rules` | Retrieves the list of alert rules associated with the specified organization and requires appropriate read and organization permissions. |
| `create_organization_metric_alert_rule` | Creates a new alert rule for an organization using the provided JSON data and returns a success response upon creation. |
| `get_organization_metric_alert_rule` | Retrieves an alert rule by its ID within a specified organization using the organization's ID or slug. |
| `update_a_metric_alert_rule` | Updates an alert rule for a specified organization using the provided JSON payload, requiring authentication with the necessary permissions. |
| `delete_a_metric_alert_rule` | Deletes the specified alert rule for the given organization using the alert rule identifier, returning a 202 Accepted status if the deletion is initiated. |
| `get_metric_alert_rule_activations` | Retrieves a list of activations for a specific alert rule within an organization. |
| `get_integration_provider_information` | Retrieves the list of configured integrations for a specified organization, optionally filtered by provider key, and returns integration details if found. |
| `list_an_organization_s_custom_dashboards` | Retrieves a list of dashboards for a specified organization using pagination parameters. |
| `create_a_new_dashboard_for_an_organization` | Creates a new dashboard for the specified organization using provided JSON data, requiring appropriate organization-level authentication. |
| `retrieve_an_organization_s_custom_dashboard` | Retrieves details of a specific dashboard within an organization using its ID or slug and the dashboard ID. |
| `edit_an_organization_s_custom_dashboard` | Updates the specified dashboard within an organization by replacing it with the provided data using the PUT method. |
| `delete_an_organization_s_custom_dashboard` | Deletes a specific dashboard in an organization using the provided organization ID or slug and dashboard ID, requiring authentication with admin or write permissions. |
| `list_an_organization_s_discover_saved_queries` | Retrieves a list of saved discoveries for an organization, allowing filtering by query, sorting, and pagination. |
| `create_a_new_saved_query` | Saves a discovery configuration for a specified organization using the provided JSON data and returns a success status upon completion. |
| `retrieve_an_organization_s_discover_saved_query` | Retrieves saved discovery data for a specified query within an organization using the provided organization ID or slug and query ID. |
| `edit_organization_discover_saved_query` | Updates or replaces a saved Discover query for the specified organization using the provided query details. |
| `delete_organization_discover_saved_query` | Deletes a saved query for a specified organization and query ID, returning a 204 (No Content) on success. |
| `list_an_organization_s_environments` | Lists all environments for a specified organization, optionally filtered by visibility, when authenticated with sufficient permissions. |
| `query_discover_events_in_table_format` | Retrieves a list of events for a specified organization, allowing filtering and sorting by various query parameters such as fields, environment, project, time range, and pagination. |
| `create_an_external_user` | Links a user from an external provider to a Sentry user within the specified organization and returns the external user resource. |
| `update_an_external_user` | Updates the details of a specified external user within an organization using the provided request body. |
| `delete_an_external_user` | Removes an external user from an organization using the organization ID or slug and the external user ID. |
| `list_organization_available_integrations` | Retrieves a list of integrations for a specified organization using the provided organization ID or slug, allowing optional filtering by provider key, features, and configuration inclusion. |
| `get_organization_integration` | Retrieves details for a specific integration within an organization using its ID or slug. |
| `delete_organization_integration` | Deletes an integration from an organization using the provided organization ID or slug and integration ID, returning a 204 status code upon successful deletion. |
| `list_an_organization_s_members` | Retrieves a list of members belonging to a specified organization, with access controlled by member-specific permissions. |
| `add_a_member_to_an_organization` | Invites a new member to the specified organization by creating their membership with the provided details. |
| `retrieve_an_organization_member` | Retrieves information about a specific member in an organization using the provided organization ID or slug and member ID. |
| `update_an_organization_member_s_roles` | Updates a member's details in an organization using the PUT method, requiring the organization ID or slug and member ID in the path, and supports JSON content in the request body. |
| `delete_an_organization_member` | Deletes a member from an organization using the provided organization ID or slug and member ID. |
| `add_an_organization_member_to_a_team` | Adds a member to a specified team within an organization. |
| `update_an_organization_member_s_team_role` | Updates a team membership for a specific member in an organization using the provided team ID or slug. |
| `delete_an_organization_member_from_a_team` | Removes a member from a specific team in an organization using the provided organization ID or slug, member ID, and team ID or slug. |
| `retrieve_monitors_for_an_organization` | Retrieves a list of monitors for an organization using the provided organization ID or slug, with optional filtering by project, environment, and owner. |
| `create_a_monitor` | Creates a new monitor for an organization using the provided JSON body and returns a status message, requiring authentication with permissions to read or write within the organization. |
| `retrieve_a_monitor` | Retrieves details about a specific monitor in an organization based on the provided organization ID or slug and monitor ID or slug, optionally filtered by environment. |
| `update_a_monitor` | Updates the specified monitor within the given organization by replacing its configuration using the provided JSON data. |
| `delete_a_monitor_or_monitor_environments` | Deletes a monitor from a specified organization in an API, identified by organization ID or slug and monitor ID or slug, with optional environment parameters. |
| `retrieve_check_ins_for_a_monitor` | Retrieves check-ins for a specific monitor within an organization using the provided organization ID or slug and monitor ID or slug. |
| `list_spike_protection_notifications` | Retrieves a list of notification actions available for the specified organization, optionally filtered by project or trigger type. |
| `create_spike_protection_notification` | Performs an action on notifications for a specified organization using the provided JSON body and returns a success status. |
| `retrieve_a_spike_protection_notification_action` | Retrieves information about a specific notification action for an organization using the provided organization identifier or slug and action ID. |
| `update_a_spike_protection_notification_action` | Updates a notification action for a specific organization using the provided JSON data and returns a success status upon completion. |
| `delete_a_spike_protection_notification_action` | Deletes a notification action by its ID for a specific organization identified by its ID or slug, using the provided authentication token with appropriate permissions. |
| `list_an_organization_s_projects` | Retrieves a paginated list of projects within the specified organization identified by its ID or slug. |
| `list_an_organization_s_trusted_relays` | Retrieves relay usage information for a specified organization using its ID or slug, requiring appropriate authentication tokens for administrative or read access. |
| `get_release_threshold_statuses` | Retrieves the current statuses of release thresholds for a specified organization within a given time range, optionally filtered by environment, project, or release. |
| `retrieve_an_organization_s_release` | Retrieves detailed information about a specific release version within an organization, optionally filtered and sorted by project, health metrics, adoption stages, summary statistics, and status. |
| `update_an_organization_s_release` | Updates a specific release version within an organization using the provided JSON data and returns a status message. |
| `delete_an_organization_s_release` | Deletes a release version associated with an organization in the API, identified by the organization ID or slug and the version number, and returns a successful deletion status with a 204 response code. |
| `retrieve_a_count_of_replays` | Retrieves the replay count for a specified organization, filtered by optional parameters such as environment, time range, project, and custom query. |
| `list_an_organization_s_selectors` | Retrieves a list of replay selectors for an organization using the provided parameters such as environment, stats period, project, and query filters. |
| `list_an_organization_s_replays` | Retrieves and lists replays for an organization, allowing filtering by various parameters such as statistics period, date range, fields, projects, environment, sorting, and query filters. |
| `retrieve_a_replay_instance` | Retrieves replay data for a specified organization and replay ID, allowing filtering by various parameters such as stats period, date range, fields, projects, and environment. |
| `list_an_organization_s_paginated_teams` | Retrieves a list of SCIM groups for a specified organization using query parameters such as startIndex, count, filter, and excludedAttributes. |
| `provision_a_new_team` | Creates a new SCIM group for the specified organization using a POST request to the Groups endpoint, requiring organization details in the request body. |
| `query_an_individual_team` | Retrieves details about a specific team using its ID within an organization, returning relevant SCIM group information. |
| `update_a_team_s_attributes` | Modifies a specific group within an organization using SCIM 2.0, allowing updates to group attributes with the provided JSON payload. |
| `delete_an_individual_team` | Deletes a specific team from an organization using SCIM, identified by a team ID, and removes associated permissions and access. |
| `list_an_organization_s_scim_members` | Retrieves a list of users from the specified organization using SCIM 2.0, allowing pagination and filtering based on query parameters such as `startIndex`, `count`, and `filter`. |
| `provision_a_new_organization_member` | Creates a new user in an organization using the SCIM API by sending a POST request to the specified Users endpoint. |
| `query_an_individual_organization_member` | Retrieves a specific member's details within an organization using the SCIM API, based on the organization ID or slug and the member ID. |
| `update_an_organization_member_s_attributes` | Updates specific attributes of a SCIM user within an organization using a PATCH request. |
| `delete_an_organization_member_via_scim` | Deletes an organization member by ID using the SCIM API, requiring a valid admin token for authentication. |
| `retrieve_release_health_session_statistics` | Retrieves sessions for a specified organization using the provided filters and parameters, such as fields, date range, environment, and statistics period. |
| `get_organization_events_count_by_project` | Retrieves a summary of statistics for an organization specified by its ID or slug, allowing for filtering by field, time period, and other criteria, and optionally returns the data in a downloadable format. |
| `get_organization_event_counts_v2` | Retrieves statistical data for an organization using the `GET` method, allowing filtering by group, field, and time period. |
| `list_an_organization_s_teams` | Retrieves a list of teams associated with the specified organization, optionally with detailed information and pagination support. |
| `create_a_new_team` | Creates a team within a specified organization using the provided JSON data and returns a status message upon successful creation. |
| `list_a_user_s_teams_for_an_organization` | Retrieves a list of user teams associated with the specified organization. |
| `retrieve_a_project` | Retrieves details about a specific project within an organization using the organization ID or slug and project ID or slug. |
| `update_a_project` | Updates a project specified by organization ID or slug and project ID or slug using JSON data in the request body, requiring appropriate authentication. |
| `delete_a_project` | Deletes a project identified by the specified organization ID or slug and project ID or slug using the DELETE method, requiring admin authentication. |
| `list_a_project_s_environments` | Get a list of environments for a specified project within an organization, optionally filtered by visibility. |
| `retrieve_a_project_environment` | Retrieves details for a specific environment within a project using the organization ID or slug, project ID or slug, and environment name. |
| `update_a_project_environment` | Updates the environment settings for a specific project using the provided JSON data and returns a status message. |
| `list_a_project_s_error_events` | Retrieves a list of events for a specific project in an organization using the provided identifiers and optional query parameters for pagination and data filtering. |
| `debug_event_source_maps` | Retrieves source map debug information for a specific event within a project, using the `GET` method and requiring an organization ID or slug, project ID or slug, event ID, frame index, and exception index. |
| `list_a_project_s_data_filters` | Retrieves a list of filters for a project in a specified organization using the provided organization ID or slug and project ID or slug. |
| `update_an_inbound_data_filter` | Updates a filter in a project using the organization ID or slug, project ID or slug, and filter ID, with the new filter details provided in the JSON body, requiring appropriate authentication for project administration or writing permissions. |
| `list_a_project_s_client_keys` | Retrieves a list of keys for a project, allowing optional filtering by status and pagination with a cursor. |
| `create_a_new_client_key` | Create a new key for a specific project within an organization by providing the necessary details in the request body. |
| `retrieve_a_client_key` | Retrieves details about a specific project key using the organization ID or slug and project ID or slug. |
| `update_a_client_key` | Updates a project key using the PUT method, requiring the organization ID or slug, project ID or slug, and key ID, with authentication for project admin or write permissions. |
| `delete_a_client_key` | Deletes a specified API key within a project under an organization, requiring project admin authorization. |
| `list_a_project_s_organization_members` | Retrieves a list of members for a specific project within an organization using the provided organization ID or slug and project ID or slug. |
| `retrieve_a_monitor_for_a_project` | Retrieves details for a specific monitor within a project and organization using their respective IDs or slugs. |
| `update_a_monitor_for_a_project` | Updates a monitor in a project using the organization and project identifiers. |
| `delete_project_monitor_or_environments` | Deletes a specific monitor from a project in an organization and returns an HTTP status indicating the outcome. |
| `retrieve_check_ins_for_a_monitor_by_project` | Retrieves checkin data for a specific monitor in a project, identified by the organization ID or slug, project ID or slug, and monitor ID or slug. |
| `get_project_ownership_config` | Retrieves project ownership details for a specific project within an organization using the provided organization ID or slug and project ID or slug. |
| `update_project_ownership_config` | Updates the ownership configuration for a specific project, allowing modification of ownership rules, fallthrough assignment, auto-assignment settings, and CODEOWNERS synchronization[1]. |
| `delete_a_replay_instance` | Deletes a specified replay associated with a project and organization using its unique identifier. |
| `list_clicked_nodes` | Retrieves a list of user click events recorded during a specific replay session within a project and organization, with optional filtering and pagination. |
| `list_recording_segments` | Retrieves a paginated list of recording segments for a specified replay within a project and organization. |
| `retrieve_a_recording_segment` | Retrieves a specific recording segment from a replay within a project using the organization ID or slug and project ID or slug. |
| `list_users_who_have_viewed_a_replay` | Get a list of users who have viewed a specific replay in a project within an organization. |
| `list_a_project_s_issue_alert_rules` | Retrieves the list of rules configured for a specified project within an organization. |
| `create_an_issue_alert_rule_for_a_project` | Creates a new rule for a project within an organization using the provided JSON data and returns a success status upon creation. |
| `retrieve_an_issue_alert_rule_for_a_project` | Retrieves information about a specific rule in a project using the organization ID or slug, project ID or slug, and rule ID. |
| `update_an_issue_alert_rule` | Updates a specific rule in a project by replacing its current state with new values provided in the request body, requiring authentication with the necessary permissions. |
| `delete_an_issue_alert_rule` | Deletes a specific rule from a project within an organization by rule ID. |
| `retrieve_a_project_s_symbol_sources` | Retrieves a list of symbol sources for a specified project within an organization using the provided organization and project identifiers. |
| `add_a_symbol_source_to_a_project` | Creates a new symbol source for a specified project within an organization using the provided JSON data and returns a 201 status on success. |
| `update_a_project_s_symbol_source` | Updates or replaces a symbol source configuration for a specified project within an organization using the provided JSON data. |
| `delete_a_symbol_source_from_a_project` | Deletes symbol sources from a specific project identified by organization ID or slug and project ID or slug using the provided ID, requiring project admin authentication. |
| `list_a_project_s_teams` | Retrieves a list of teams within a specified project using the provided organization and project identifiers. |
| `add_a_team_to_a_project` | Adds a specified team to a project within an organization and returns a response indicating successful creation. |
| `delete_a_team_from_a_project` | Deletes a team from a project within a specified organization using the API with appropriate permissions. |
| `retrieve_a_team` | Retrieves information about a team within an organization using the provided organization ID or slug and team ID or slug, allowing optional expansion or collapse of additional details. |
| `update_a_team` | Updates the details of a specified team within a given organization using the provided data and requires administrative or write permissions. |
| `delete_a_team` | Deletes a team from an organization using the provided organization ID or slug and team ID or slug, requiring the team admin authentication token for authorization. |
| `create_an_external_team` | Create a new external team associated with a specified organization and team using the provided JSON data. |
| `update_an_external_team` | Updates an external team's details for a specified team and organization, requiring admin or write permissions, with the request body containing the updated data. |
| `delete_an_external_team` | Deletes an external team association with the specified team in an organization using the provided organization identifier, team identifier, and external team ID. |
| `list_a_team_s_members` | Retrieves a list of members belonging to the specified team within the given organization, supporting pagination via a cursor parameter. |
| `list_a_team_s_projects` | Retrieves a paginated list of projects associated with a specific team within an organization, using optional cursor-based pagination. |
| `create_a_new_project` | Creates a new project within the specified team and organization using provided details and returns the project resource upon success. |
| `list_user_emails` | Retrieves a list of email addresses associated with the specified user ID, requiring authentication. |
| `add_a_secondary_email_address` | Adds a new email address for a specified user using the provided JSON data and returns a success message. |
| `update_a_primary_email_address` | Updates the email address of a user specified by the `user_id` using the provided JSON data in the request body. |
| `remove_an_email_address` | Deletes a user's email configurations associated with the specified user ID using the DELETE method. |
| `retrieve_event_counts_for_a_team` | Retrieves team statistics for a specified organization and team, allowing filtering by specific stat, date range, and resolution. |
| `resolve_an_event_id` | Retrieves event details for a specific event within an organization identified by the provided organization ID or slug and event ID. |
| `list_an_organization_s_repositories` | Retrieves a list of repositories for the specified organization identified by its ID or slug, requiring organization read authorization. |
| `list_a_repository_s_commits` | Retrieves a list of commits from a specified repository within an organization, requiring read access for authentication. |
| `resolve_a_short_id` | Retrieves information for a specific short ID within an organization using the provided organization ID or slug. |
| `list_your_projects` | Get a list of projects accessible to the user, optionally paginated using a cursor. |
| `list_project_debug_files` | Retrieves a list of dSYM files for a specific project within an organization using the provided organization ID or slug and project ID or slug. |
| `delete_project_debug_file` | Deletes a dSYM file from a project using its ID, requiring a write authorization token for the project. |
| `list_a_project_s_users` | Retrieves a list of users associated with a specified project within an organization, optionally filtered by a query parameter. |
| `list_a_tag_s_values` | Retrieves a list of values for a specific tag key within a project, using the organization ID or slug and project ID or slug. |
| `retrieve_event_counts_for_a_project` | Retrieves statistics for a specific project within an organization, optionally filtered by stat type, time range, and resolution. |
| `list_a_project_s_user_feedback` | Retrieves a list of user feedback items for a specified project within an organization. |
| `submit_user_feedback` | Submits user feedback for a specific project within an organization using the provided JSON body and authenticates via an authentication token with project write permissions. |
| `list_a_project_s_service_hooks` | Retrieves a list of hooks for a specific project within an organization using the project and organization identifiers. |
| `register_a_new_service_hook` | Creates a new webhook for the specified project within an organization and returns a success status upon creation. |
| `retrieve_a_service_hook` | Retrieves a specific hook from a project using organization and project identifiers. |
| `update_a_service_hook` | Updates a specific hook in a project using the provided JSON payload and returns a success response upon completion. |
| `remove_a_service_hook` | Deletes a webhook hook identified by the specified hook ID within a project, requiring administrative privileges for the project. |
| `retrieve_an_event_for_a_project` | Retrieves details for a specific event within a project using the organization ID or slug and project ID or slug. |
| `list_project_issues` | Get a list of issues for a specified project within an organization, with optional filters for query, stats period, short ID lookup, hashes, and pagination. |
| `bulk_mutate_a_list_of_issues` | Updates an issue in a specific project within an organization using the provided JSON body and returns a status code indicating the outcome of the update. |
| `bulk_remove_a_list_of_issues` | Deletes issues from a project by organization or project identifier using the "DELETE" method, requiring authentication as an event administrator. |
| `list_a_tag_s_values_related_to_an_issue` | Retrieves the available values for a specific tag key associated with an issue within the specified organization. |
| `list_an_issue_s_hashes` | Retrieves hashes for a specific issue in an organization using the provided organization ID or slug and issue ID, optionally including additional details if the "full" query parameter is set. |
| `retrieve_an_issue` | Retrieves details about a specific issue within an organization using the provided organization ID or slug and issue ID. |
| `update_an_issue` | Updates an existing issue within an organization by modifying its details using the provided JSON payload. |
| `remove_an_issue` | Deletes an issue identified by `{issue_id}` within an organization specified by `{organization_id_or_slug}` using the DELETE method. |
| `list_an_organization_s_releases` | Retrieves a list of releases for a specified organization using the provided organization ID or slug, with optional query filtering. |
| `create_a_new_release_for_an_organization` | Creates a new release for the specified organization using the provided release data. |
| `list_an_organization_s_release_files` | Retrieves a list of files associated with a specific release version within an organization using the provided organization ID or slug and version number. |
| `list_a_project_s_release_files` | Get a list of files associated with a specific release version for a project within an organization. |
| `retrieve_an_organization_release_s_file` | Retrieves a file from a release in an organization using the provided organization ID or slug, version, and file ID, optionally allowing for file download. |
| `update_an_organization_release_file` | Updates a file with the specified ID in a release of an organization using the provided JSON data. |
| `delete_an_organization_release_s_file` | Deletes a specific file associated with a release in an organization using the provided organization ID or slug, version, and file ID. |
| `retrieve_a_project_release_s_file` | Retrieves a specific file from a project release using the "GET" method, requiring organization ID or slug, project ID or slug, version, and file ID, and optionally allows for a download option via query parameter. |
| `update_a_project_release_file` | Updates a specific file associated with a project release using the provided JSON data. |
| `delete_a_project_release_s_file` | Deletes a specific file from a release version in a project using the organization and project identifiers. |
| `list_an_organization_release_s_commits` | Retrieves a list of commits for a specific version within an organization using the provided organization ID or slug and version number. |
| `list_a_project_release_s_commits` | Get the list of commits associated with a specific release version in a project within an organization. |
| `retrieve_files_changed_in_a_release_s_commits` | Retrieves a list of commit files for a specific release version within an organization, identified by its ID or slug. |
| `list_a_release_s_deploys` | Retrieves deployment information for a specific release version within an organization. |
| `create_a_new_deploy_for_an_organization` | Records a new deployment of a specific release version for an organization identified by its ID or slug and returns status codes indicating success, conflict, or error. |
| `list_organization_integration_installations` | Retrieves a list of Sentry app installations for a specified organization using the organization ID or slug. |
| `create_or_update_an_external_issue` | Creates or updates an external issue linked to a Sentry issue using the integration platform integration specified by the `uuid` path parameter, requiring authentication with a token having the `event:write` scope. |
| `delete_an_external_issue` | Deletes an external issue associated with a specific integration installation in Sentry, requiring authentication with the `event:admin` scope. |
| `enable_spike_protection` | Creates a new spike protection for an organization using the provided JSON data and returns a status message, requiring authentication with permissions to read, write, or administer projects. |
| `list_an_issue_s_events` | Retrieves a list of events associated with a specific issue, optionally filtered by date range, environment, and other query parameters. |
| `retrieve_an_issue_event` | Retrieves event details for a specific event within an issue using the provided issue ID and event ID, optionally filtered by environment. |
| `retrieve_tag_details` | Retrieves a tag for a specific issue based on the provided key, with optional filtering by environment. |
| `list_a_tag_s_values_for_an_issue` | Retrieves a list of values for a specific tag key associated with an issue, allowing optional sorting and filtering by environment. |
