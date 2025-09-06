# JiraApp MCP Server

An MCP Server for the JiraApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the JiraApp API.


| Tool | Description |
|------|-------------|
| `get_banner` | Retrieves the configuration of the announcement banner using the Jira Cloud API. |
| `set_banner` | Updates the announcement banner configuration in Jira Cloud, including message, visibility, and dismissal settings. |
| `get_custom_fields_configurations` | Retrieves and filters a list of custom field context configurations in Jira based on specified criteria like field ID, project, or issue type, returning paginated results. |
| `set_field_value` | Updates the value of a custom field added by a Forge app on one or more Jira issues. |
| `get_custom_field_configuration` | Retrieves the configuration of a custom field context in Jira using the provided field ID or key, optionally filtered by specific IDs, field context IDs, issue IDs, project keys or IDs, or issue types, and returns a paginated list of configurations. |
| `update_custom_field_configuration` | Updates the configuration of a custom field context in Jira using the provided field ID or key. |
| `update_custom_field_value` | Updates the value of a custom field for an issue using the Jira API, but this endpoint is limited to working with fields provided by Forge apps. |
| `get_application_property` | Retrieves application properties with optional filtering by key, permission level, or key filter. |
| `get_advanced_settings` | The API retrieves Jira's advanced settings properties, returning configuration details displayed on the "General Configuration > Advanced Settings" page. |
| `set_application_property` | Updates a specific Jira application property identified by its ID using a PUT request. |
| `get_all_application_roles` | Retrieves information about application roles using the Jira Cloud API and returns data relevant to the specified application roles. |
| `get_application_role` | Retrieves details of a specific application role in Jira Cloud using the provided `key` parameter via the GET method. |
| `get_attachment_content` | Retrieves the contents of a Jira Cloud attachment by ID and returns the binary file data or a redirect URL. |
| `get_attachment_meta` | Retrieves Jira's attachment settings, including whether attachments are enabled and the maximum allowed upload size. |
| `get_attachment_thumbnail` | Retrieves a thumbnail image for a specified attachment ID in Jira, supporting optional parameters for dimensions and redirect behavior. |
| `remove_attachment` | Deletes an attachment from a Jira issue by its ID and returns a success status upon removal. |
| `get_attachment` | Retrieves metadata for a specific attachment in Jira using the provided attachment ID. |
| `expand_attachment_for_humans` | Retrieves human-readable metadata for a specific Jira Cloud attachment in an expanded format. |
| `expand_attachment_for_machines` | Retrieves the contents metadata for an expanded attachment in Jira Cloud using the "GET /rest/api/3/attachment/{id}/expand/raw" endpoint, suitable for processing without presenting the data to users. |
| `get_audit_records` | Retrieves Jira audit records with filtering by parameters like date range, text, and category, returning activity logs of administrative actions and changes. |
| `get_all_system_avatars` | Retrieves a list of system avatar details for a specified owner type (e.g., user, project, issue type) via the Jira Cloud REST API. |
| `submit_bulk_delete` | Deletes multiple Jira issues in a single request using the Bulk Delete API. |
| `get_bulk_editable_fields` | Retrieves a list of fields that can be edited in bulk for specified Jira issues, allowing for the identification of editable fields for bulk operations using query parameters such as issue IDs or keys, search text, and pagination options. |
| `submit_bulk_edit` | Edits multiple Jira issues in bulk by updating fields using the Jira Cloud API. |
| `submit_bulk_move` | Moves multiple issues from one Jira project to another using the POST method. |
| `get_available_transitions` | Retrieves valid workflow transitions for multiple Jira issues based on provided issue IDs or keys. |
| `submit_bulk_transition` | Transitions multiple Jira issues to a specified status in bulk using the Jira REST API, allowing for streamlined workflow management and automation of repetitive tasks. |
| `submit_bulk_unwatch` | Unwatches up to 1,000 specified Jira issues in a single bulk operation via POST request, requiring write permissions and returning success/error responses. |
| `submit_bulk_watch` | Adds watchers to multiple Jira issues in bulk through a single operation. |
| `get_bulk_operation_progress` | Retrieves the status of a bulk operation task identified by the specified taskId. |
| `get_bulk_changelogs` | Retrieves changelog data for multiple Jira issues in a single request, eliminating the need for individual API calls per issue. |
| `list_classification_levels` | Retrieves a list of all classification levels in Jira Cloud, supporting optional filtering by status and ordering using the "orderBy" parameter. |
| `get_comments_by_ids` | Fetches a paginated list of Jira comments by their IDs using a POST request. |
| `get_comment_property_keys` | Retrieves the keys of all properties associated with a specified issue comment in Jira Cloud using the REST API. |
| `delete_comment_property` | Deletes a specific property from a comment in Jira using the Jira Cloud REST API and returns a status code upon successful deletion. |
| `get_comment_property` | Retrieves the value of a specific property for an issue comment in Jira using the comment ID and property key. |
| `set_comment_property` | Updates the value of a specific property for a Jira comment using the PUT method, storing custom data against a comment identified by its ID and property key. |
| `find_components_for_projects` | Retrieves a list of Jira components using the GET method at the "/rest/api/3/component" path, allowing filtering by project IDs, pagination, and sorting, and returns the results in a paginated format. |
| `create_component` | Creates a new component in Jira, providing a container for issues within a project, using the POST method on the "/rest/api/3/component" endpoint. |
| `delete_component` | Deletes a specific component in Jira by ID, optionally reassigning its issues to another component. |
| `get_component` | Retrieves detailed information about a specific Jira component, identified by its ID, using the Jira REST API. |
| `update_component` | Updates the specified component's details using the provided ID. |
| `get_component_related_issues` | Retrieves the issue counts related to a specific Jira component identified by its ID using the "GET" method. |
| `get_configuration` | Retrieves configuration details from Jira using the GET method and returns the result in the response. |
| `get_time_tracking_config` | Retrieves the time tracking settings in Jira, including time format and default time unit, using the GET method at "/rest/api/3/configuration/timetracking". |
| `update_time_tracking_config` | Updates time tracking settings in Jira using the Jira Cloud platform REST API at "/rest/api/3/configuration/timetracking" with a "PUT" method, allowing configurations such as time format and default time unit. |
| `list_time_tracking_configs` | Retrieves a list of all configured time tracking providers in Jira, including the active provider if time tracking is enabled. |
| `get_time_tracking_options` | Retrieves time tracking configuration settings such as time format and default units using the Jira Cloud REST API. |
| `update_time_tracking_options` | Updates Jira time tracking configuration settings including time format, working hours, and default time unit. |
| `get_custom_field_option` | Retrieves a full representation of a custom field option by its ID using the Jira REST API. |
| `get_all_dashboards` | Retrieves a list of Jira dashboards using the GET method, allowing for optional filtering, pagination with start and max results parameters. |
| `create_dashboard` | Creates a new dashboard in Jira Cloud using the REST API and returns a response indicating the success or failure of the operation. |
| `bulk_edit_dashboards` | Bulk updates permissions and settings for multiple Jira dashboards in a single operation. |
| `get_gadgets` | Retrieves a list of available gadgets that can be added to Jira dashboards using the Jira Cloud API. |
| `get_dashboards_paginated` | Searches for Jira dashboards using specified criteria, such as dashboard name, account ID, owner, group name, group ID, project ID, and other parameters, and returns a list of matching dashboards. |
| `get_all_gadgets` | Retrieves a specific gadget or all gadgets from a Jira dashboard. |
| `add_gadget` | Adds a gadget to a specified Jira dashboard using the provided configuration and returns the created gadget details upon success. |
| `remove_gadget` | Removes a specific gadget from a Jira Cloud dashboard using the DELETE method, where other gadgets in the same column are automatically moved up to fill the emptied position. |
| `update_gadget` | Updates a gadget's configuration (e.g., color, position, title) on a specified Jira dashboard. |
| `get_dashboard_item_property_keys` | Retrieves all property keys for a specific dashboard item in Jira using provided dashboard and item IDs. |
| `delete_dashboard_item_property` | Deletes a dashboard item property (identified by propertyKey) from a specific dashboard item, accessible anonymously but requiring dashboard ownership for successful deletion. |
| `get_dashboard_item_property` | Retrieves a specific property of a dashboard item using the Jira API, returning the property value associated with the given dashboard ID, item ID, and property key. |
| `set_dashboard_item_property` | Updates or creates a specific property for an item on a dashboard using the PUT method, identified by dashboardId, itemId, and propertyKey, returning success or creation status. |
| `delete_dashboard` | Deletes a dashboard identified by its ID using the "DELETE" method and returns a successful status if the operation is completed without errors. |
| `get_dashboard` | Retrieves the details of a specific Jira dashboard by ID. |
| `update_dashboard` | Updates a dashboard with the specified ID using the PUT method, optionally extending admin permissions, and returns a status message if successful. |
| `copy_dashboard` | Copies a dashboard and replaces specified parameters in the copied dashboard, returning the new dashboard details. |
| `get_policy` | Retrieves details about the data policy for a workspace using the Jira Cloud REST API, returning information on whether data policies are enabled for the workspace. |
| `get_policies` | Retrieves data policies affecting specific projects in Jira using the "/rest/api/3/data-policy/project" endpoint, returning details about which projects are impacted by data security policies. |
| `get_events` | Retrieves a list of events using the Jira Cloud API by sending a GET request to "/rest/api/3/events," providing a paginated response based on the specified parameters. |
| `analyse_expression` | Analyzes a Jira expression to statically check its characteristics, such as complexity, without evaluating it, using a POST method at "/rest/api/3/expression/analyse" with the option to specify what to check via a query parameter. |
| `evaluate_jira_expression` | Evaluates Jira expressions using an enhanced search API for scalable processing of JQL queries and returns primitive values, lists, or objects. |
| `evaluate_jsisjira_expression` | Evaluates Jira expressions using the enhanced search API with support for pagination and eventually consistent JQL queries, returning primitive values, lists, or objects. |
| `get_fields` | Retrieves a list of available fields in Jira using the GET method at the "/rest/api/3/field" path. |
| `create_custom_field` | Creates a custom field using a definition and returns a successful creation message when the operation is completed successfully. |
| `remove_associations` | Deletes an association between a field and its related entities, returning response codes for success or error conditions. |
| `create_associations` | Associates or unassociates custom fields with projects and issue types in Jira using the PUT method. |
| `get_fields_paginated` | Retrieves and filters Jira fields by criteria such as ID, type, or name, supporting pagination and field expansion. |
| `get_trashed_fields_paginated` | Retrieves a paginated list of custom fields that have been trashed in Jira, allowing filtering by field ID, name, or description. |
| `update_custom_field` | Updates a Jira custom field using the `PUT` method, specifying the field ID in the path, and returns a status response upon successful modification. |
| `get_contexts_for_field` | Retrieves a list of custom field contexts for a specified field in Jira using the path "/rest/api/3/field/{fieldId}/context" with optional filters for issue type and global context. |
| `create_custom_field_context` | Creates a new custom field context for the specified field ID, defining its project and issue type associations. |
| `get_default_values` | Retrieves the default values for contexts of a specified custom field in Jira, including optional pagination parameters for larger datasets. |
| `set_default_values` | Sets the default value for a specified custom field context via the Jira REST API. |
| `get_field_issue_type_mappings` | Retrieves a paginated list of context to issue type mappings for a specified custom field using the Jira Cloud API, allowing for filters by context ID, start index, and maximum results. |
| `post_field_context_mapping` | Retrieves and maps custom field contexts to specific projects and issue types for a given custom field ID. |
| `get_project_context_mapping` | Retrieves paginated mappings between projects and custom field contexts, optionally filtered by context ID. |
| `delete_custom_field_context` | Deletes a custom field context in Jira using the provided `fieldId` and `contextId`, removing it from the system. |
| `update_custom_field_context` | Updates a custom field context's configuration in Jira, including associated projects and issue types. |
| `add_issue_types_to_context` | Updates the issue type associations for a specific custom field context in Jira using the specified field and context IDs. |
| `remove_issue_types_from_context` | Removes issue types from a custom field context in Jira, reverting them to apply to all issue types if none remain. |
| `get_options_for_context` | Retrieves and paginates custom field options (single/multiple choice values) for a specific field and context in Jira, including filtering by option ID. |
| `create_custom_field_option` | Creates new custom field options for a specific context in Jira using the POST method, allowing for the addition of options to select lists or similar fields. |
| `update_custom_field_option` | Updates options for a custom field context in Jira using the provided field and context IDs, but this endpoint is not explicitly documented for a PUT method; typically, such endpoints involve updating or adding options to a select field within a specific context. |
| `reorder_custom_field_options` | Reorders custom field options or cascading options within a specified context using the provided IDs and position parameters. |
| `delete_custom_field_option` | Deletes a specific custom field option within a designated custom field context in Jira. |
| `replace_custom_field_option` | Deletes a specific custom field option within a context for a Jira field, allowing optional replacement via query parameters. |
| `assign_project_field_context` | Updates a custom field context by adding a project to it, using the Jira Cloud platform REST API, and returns a status message based on the operation's success or failure. |
| `remove_project_from_field_context` | Removes specified projects from a custom field context in Jira, causing it to apply to all projects if no projects remain. |
| `get_contexts_for_field_deprecated` | Retrieves a paginated list of contexts for a specified custom field in Jira, allowing filtering by start index and maximum number of results. |
| `get_screens_for_field` | Retrieves a list of screens that include a specified field, identified by the `fieldId` parameter, allowing for pagination and expansion of results. |
| `get_all_issue_field_options` | Retrieves a paginated list of all custom field options for a specified field, supporting pagination via startAt and maxResults parameters. |
| `create_issue_field_option` | Adds a new option to a specified custom field in Jira using the POST method, requiring the field's key as a path parameter. |
| `get_selectable_issue_field_options` | Retrieves paginated suggestions for editable options of a specific custom field, filtered by project ID if provided, in Jira Cloud. |
| `get_visible_issue_field_options` | Searches for and returns a list of option suggestions for a specific custom field in Jira, based on the provided field key, allowing for pagination using query parameters like `startAt` and `maxResults`. |
| `delete_issue_field_option` | Deletes a specific custom field option in Jira and initiates asynchronous cleanup of associated issue data. |
| `get_issue_field_option` | Retrieves a specific custom field option's details for a given field key and option ID in Jira. |
| `update_issue_field_option` | Updates a custom field option identified by its ID in Jira using the PUT method, allowing for modification of existing option details such as value or status. |
| `replace_issue_field_option` | Deletes a custom field option from specific issues using the Jira API, allowing for parameters such as replacing the option, filtering by JQL, and overriding screen security and editable flags. |
| `delete_custom_field` | Deletes a custom field in Jira Cloud using the REST API with the "DELETE" method at the path "/rest/api/3/field/{id}", where "{id}" is the identifier of the field to be deleted. |
| `restore_custom_field` | Restores a custom field from trash in Jira using the specified field ID. |
| `trash_custom_field` | Moves a custom field to trash in Jira using the specified field ID, requiring admin permissions. |
| `get_all_field_configurations` | Retrieves field configurations from Jira using the GET method at the "/rest/api/3/fieldconfiguration" path, allowing filtering by parameters such as startAt, maxResults, id, isDefault, and query. |
| `create_field_configuration` | Creates a new field configuration in Jira to manage field visibility and behavior, returning the configuration details upon success. |
| `delete_field_configuration` | Deletes a Jira field configuration by ID and returns a success status upon completion. |
| `update_field_configuration` | Updates a field configuration (name and description) in company-managed Jira projects, requiring Administer Jira permissions. |
| `get_field_configuration_items` | Retrieves a list of fields associated with a field configuration specified by its ID, allowing pagination via optional startAt and maxResults parameters. |
| `update_field_configuration_items` | Updates the fields of a field configuration in Jira using the PUT method with the specified configuration ID. |
| `list_field_configs` | Retrieves field configuration schemes in Jira with support for pagination and optional ID filtering. |
| `create_field_configuration_scheme` | Creates a field configuration scheme using the Jira Cloud platform REST API. |
| `get_field_mapping` | Retrieves mappings for a specified field configuration scheme using the Jira API, providing details of how fields are configured across projects. |
| `get_field_configs_for_project` | Retrieves a paginated list of field configuration schemes for a specified project, including the projects that use each scheme, using the `GET` method at the `/rest/api/3/fieldconfigurationscheme/project` path. |
| `update_field_config_scheme_project` | Updates a field configuration scheme associated with a project using the Jira Cloud API, specifically for company-managed (classic) projects. |
| `delete_field_configuration_scheme` | Deletes a field configuration scheme from Jira by ID, requiring Administer Jira permissions. |
| `update_field_configuration_scheme` | Updates a field configuration scheme using its ID, applicable only to company-managed projects, requiring the *Administer Jira* global permission. |
| `update_field_config_scheme_mapping` | Updates the field configuration scheme mapping using the Jira Cloud API and returns a status message. |
| `delete_field_config_mapping` | Removes specified issue types from a field configuration scheme in Jira via a POST request. |
| `create_filter` | Creates a Jira filter with specified parameters such as name, JQL query, and visibility, returning the newly created filter details. |
| `get_default_share_scope` | Retrieves the default sharing scope setting for Jira filters. |
| `set_default_share_scope` | Sets the default share scope for new filters and dashboards using the Jira Cloud REST API, allowing users to set the scope to either GLOBAL or PRIVATE. |
| `get_favourite_filters` | Retrieves the user's visible favorite filters with optional expansion details. |
| `get_my_filters` | Retrieves a list of filters accessible by the user, with options to expand and include favorite filters, using the Jira REST API. |
| `get_filters_paginated` | Retrieves a list of filters accessible to the user based on parameters like name, owner, project, or group, supporting pagination and substring matching. |
| `delete_filter` | Deletes a specific Jira filter by its ID using the Jira API and returns a success status if the operation is successful. |
| `get_filter` | Retrieves a specific filter's details by ID from Jira, optionally expanding fields or overriding share permissions. |
| `update_filter` | Updates an existing Jira filter (including permissions if overrideSharePermissions is specified) and returns the modified filter. |
| `reset_columns` | Deletes the columns configuration for a specific filter in Jira using the filter ID. |
| `get_columns` | Retrieves the column configuration for a specified filter in Jira using the filter ID. |
| `set_columns` | Updates the columns of a specific filter in Jira using the REST API and returns a response indicating the status of the update operation. |
| `delete_favourite_for_filter` | Removes a filter with the specified ID from the user's favorites list using the Jira Cloud API. |
| `set_favourite_for_filter` | Adds a filter to the user's favorites list in Jira and returns the updated filter details. |
| `change_filter_owner` | Updates the owner of a Jira filter specified by ID via PUT request, requiring admin rights or ownership and returning a 204 status on success. |
| `get_share_permissions` | Retrieves the permissions for a specific Jira filter identified by its ID using the GET method, returning details about the permissions assigned to the filter. |
| `add_share_permission` | Adds permissions to an existing filter using the filter ID, allowing control over who can access or modify the filter via the API. |
| `delete_share_permission` | Deletes a specific permission associated with a filter in Jira using the REST API. |
| `get_share_permission` | Retrieves the specified permission details for a given filter ID in the API, allowing access to specific permission information. |
| `remove_group` | Deletes a group from the organization's directory using the `DELETE` method, allowing for optional group swapping, and returns a status message based on the operation's success or failure. |
| `get_group` | Retrieves group information from Jira by group name or ID, optionally expanding the response with additional details. |
| `create_group` | Creates a new group using the Jira Cloud REST API and returns a response indicating the creation status. |
| `bulk_get_groups` | Retrieves multiple groups in bulk from Jira Cloud based on query parameters such as group IDs, names, and access types. |
| `get_users_from_group` | Retrieves paginated members of a Jira group with optional filtering for inactive users, supporting group identification via name or ID. |
| `remove_user_from_group` | Removes a specified user from a group in Jira Cloud using account ID, username, groupname, or groupId as parameters. |
| `add_user_to_group` | Adds a user to a specified Jira group using the "POST" method at the "/rest/api/3/group/user" endpoint, requiring a group ID or name to identify the target group. |
| `find_groups` | Searches for groups matching query parameters and returns results with highlighted matches and a picker-friendly header indicating the number of matching groups. |
| `find_users_and_groups` | Searches for users and groups matching a query string in Jira Cloud and returns results with HTML highlighting for picker fields. |
| `get_license` | Retrieves licensing information about a Jira instance, returning details such as license metrics using the Jira Cloud REST API. |
| `create_issue` | Creates a new Jira issue using the specified project and issue type, returning a successful creation response if valid. |
| `archive_issues_async` | Archives Jira issues via ID/key using a POST request, returning async status codes for success/failure. |
| `archive_issues` | Archives Jira issues via the specified issue IDs/keys using the PUT method, handling bulk operations and returning status/error details. |
| `create_issues` | Performs bulk operations on Jira issues, such as moving or editing multiple issues at once, using the POST method at the "/rest/api/3/issue/bulk" endpoint. |
| `bulk_fetch_issues` | Fetches multiple issues in bulk from Jira using the POST method at "/rest/api/3/issue/bulkfetch", returning the specified issues based on provided issue IDs or keys. |
| `get_create_issue_meta` | Retrieves metadata including required fields, default values, and allowed configurations for creating Jira issues based on specified projects and issue types. |
| `get_create_issue_meta_issue_types` | Retrieves metadata for creating issues in Jira for a specific project's issue types, including available fields and mandatory requirements. |
| `get_create_issue_meta_issue_type_id` | Retrieves metadata for specific issue types within a project in Jira using the "GET" method, returning details such as available fields and their schemas based on the project and issue type identifiers. |
| `get_issue_limit_report` | Retrieves a report of issues approaching their worklog limit thresholds using the specified parameters. |
| `get_issue_picker_resource` | Provides auto-completion suggestions for Jira issues based on search queries and JQL filters, returning matching issues from user history and current searches. |
| `bulk_set_issues_properties_list` | Sets or updates multiple issue properties for specified issues using JIRA's REST API, supporting bulk operations on custom data storage. |
| `bulk_set_issue_properties_by_issue` | Sets or updates custom properties on multiple Jira issues in a single request and returns the task status for asynchronous processing. |
| `bulk_delete_issue_property` | Deletes a specified issue property from multiple Jira issues using filter criteria including entity IDs or property values. |
| `bulk_set_issue_property` | Updates or sets a custom property value for a Jira issue identified by the property key, returning a status reference for asynchronous processing. |
| `unarchive_issues` | Unarchives up to 1000 Jira issues in a single request using their IDs or keys, returning the count of unarchived issues and any errors encountered. |
| `get_is_watching_issue_bulk` | Determines whether the current user is watching specific issues using the Jira Cloud API, returning a status of whether the user is watching each provided issue. |
| `delete_issue` | Deletes a Jira issue identified by its ID or key, optionally deleting associated subtasks if the `deleteSubtasks` query parameter is set to `true`. |
| `get_issue` | Retrieves detailed information about a Jira issue using its ID or key, allowing optional parameters to specify fields, expansions, and additional data. |
| `edit_issue` | Updates an issue in Jira using the specified issue ID or key, allowing modification of issue fields, with optional parameters to control notification, screen security, editable flags, and response details. |
| `assign_issue` | Assigns or unassigns a Jira issue to a specific user, sets it to unassigned, or assigns it to the project's default assignee using the provided account ID or null value. |
| `add_attachment` | Adds one or more attachments to a specified Jira issue using the "POST" method, with the issue identified by its ID or key. |
| `get_change_logs` | Retrieves paginated changelog history for a specified Jira issue, including parameters for result pagination. |
| `get_change_logs_by_ids` | Retrieves the full changelog history for a specified Jira issue using its ID or key, allowing for pagination and retrieval of all changes. |
| `get_comments` | Retrieves all comments for a specified Jira issue using pagination parameters. |
| `add_comment` | Adds a comment to a Jira issue with support for visibility settings and returns the created comment. |
| `delete_comment` | Deletes a specific comment from a Jira issue using the comment ID and issue identifier. |
| `get_comment` | Retrieves a specific comment from a Jira issue using its ID and returns the comment details. |
| `update_comment` | Updates an existing comment on a Jira issue and returns the modified comment details. |
| `get_edit_issue_meta` | Retrieves editable field metadata and supported operations for a specific Jira issue to guide modifications via the API. |
| `notify` | Sends notifications related to a specific Jira issue, identified by its ID or key, allowing customization of the notification content and recipients. |
| `get_issue_property_keys` | Retrieves the URLs and keys of all properties associated with a specified Jira issue using the issue ID or key. |
| `delete_issue_property` | Deletes a specific property from an issue in Jira, identified by its issue ID or key and the property key, using the Jira API. |
| `get_issue_property` | Retrieves the value of a specific property associated with a Jira issue using the provided issue ID or key and property key. |
| `set_issue_property` | Updates an issue property in Jira using the PUT method, allowing users to set or modify custom data associated with an issue by issue ID or key and property key. |
| `delete_remote_link` | Deletes a remote issue link from a Jira issue using either the link's internal ID or its global ID. |
| `get_remote_issue_links` | Retrieves a list of remote links associated with a specified Jira issue, identified by its ID or key, using the GET method at the "/rest/api/3/issue/{issueIdOrKey}/remotelink" path, allowing for optional filtering by global ID. |
| `create_or_update_remote_issue_link` | Creates a remote link to an external object for a specified Jira issue, allowing users to associate external resources with issue tracking in Jira. |
| `delete_remote_issue_link_by_id` | Deletes a remote issue link from a specified Jira issue using the link's internal ID. |
| `get_remote_issue_link_by_id` | Retrieves a specific remote link by its ID associated with a Jira issue, identified by the issue ID or key. |
| `update_remote_issue_link` | Updates a specific remote issue link by ID using a PUT request for the specified Jira issue. |
| `get_transitions` | Retrieves all available transitions for a Jira issue in its current status, including optional details like required fields and validation rules. |
| `do_transition` | Transitions a Jira issue to a new workflow status using the specified transition ID. |
| `remove_vote` | Deletes a user's vote from a specified Jira issue, identified by its ID or key, using the Jira REST API. |
| `get_votes` | Retrieves details about the votes on a specific Jira issue, identified by its issue ID or key. |
| `add_vote` | Casts a vote on a Jira issue and returns no content on success. |
| `remove_watcher` | Removes a specified user as a watcher from a Jira issue via their username or account ID and returns a success status upon completion. |
| `get_issue_watchers` | Retrieves the list of watchers for a specific Jira issue using the provided issue ID or key. |
| `add_watcher` | Adds a user as a watcher to a specified Jira issue by passing the user's account ID, returning a status message upon successful execution. |
| `bulk_delete_worklogs` | Deletes a worklog from a specific issue in Jira using the provided issue ID or key, allowing for optional adjustments to the estimate and overriding of editable flags. |
| `get_issue_worklog` | Retrieves a paginated list of worklogs for a specific Jira issue using the "GET" method, allowing filtering by start date and other parameters. |
| `add_worklog` | Adds a worklog entry to a Jira issue for time tracking and returns the created worklog details. |
| `bulk_move_worklogs` | Moves worklogs from one Jira issue to another using the `POST` method, allowing adjustments to estimates and overriding editable flags if necessary. |
| `delete_worklog` | Deletes a specific worklog entry from a Jira issue using the worklog ID and returns a success status upon removal. |
| `get_worklog` | Retrieves a specific worklog by its ID for a given Jira issue using the GET method. |
| `update_worklog` | Updates a specific worklog for an issue in Jira using the PUT method, allowing modifications to attributes such as the worklog comments, time spent, and start date, while requiring permissions to access and edit issue worklogs. |
| `get_worklog_property_keys` | Retrieves the keys of all custom properties stored against a specific worklog entry in Jira issues. |
| `delete_worklog_property` | Deletes a specific property from a Jira issue's worklog entry. |
| `get_worklog_property` | Retrieves the value of a specific property associated with a worklog for a given issue in Jira using the specified issue ID/key, worklog ID, and property key. |
| `set_worklog_property` | Updates a specific property of a worklog in Jira using the PUT method, allowing for custom data storage against the worklog. |
| `link_issues` | Creates a link between two Jira issues, allowing you to define the relationship type and optionally include a comment, using the POST method at the "/rest/api/3/issueLink" endpoint. |
| `delete_issue_link` | Deletes a specific issue link in Jira by its link ID and returns a success status. |
| `get_issue_link` | Retrieves details of a specific issue link in Jira by its unique identifier using the Jira REST API. |
| `get_issue_link_types` | Retrieves information about an issue link type in Jira using the provided ID. |
| `create_issue_link_type` | Creates a new issue link type in Jira to define relationships between linked issues. |
| `delete_issue_link_type` | Deletes a specified issue link type in Jira and returns a success status upon removal. |
| `get_issue_link_type` | Retrieves a specific issue link type by its ID from Jira, including relationship descriptions for inward and outward links. |
| `update_issue_link_type` | Updates the specified issue link type (e.g., Duplicate, Blocks) by ID to modify its name and relationship descriptions. |
| `export_archived_issues` | Exports archived issues using the Jira API, initiating a task that sends an email with a link to download a CSV file containing the issue details upon completion. |
| `get_issue_security_schemes` | Retrieves a list of all issue security schemes available in a Jira instance, allowing administrators to manage which users or groups can view issues. |
| `create_issue_security_scheme` | Creates an issue security scheme in Jira Cloud using the POST method, allowing administrators to define security levels and members, and returns the ID of the newly created scheme upon success. |
| `get_security_levels` | Retrieves details of issue security levels within a scheme, including pagination support and filtering by scheme ID or default status. |
| `set_default_levels` | Sets default issue security levels for schemes, allowing administrators to configure which security levels are applied by default across specified issue security schemes. |
| `get_security_level_members` | Retrieves the members of a specific issue security level using the Jira Cloud API, allowing for pagination and expansion of details by specifying parameters such as start index, maximum results, and expansion options. |
| `list_security_schemes_by_project` | Retrieves projects associated with specific issue security schemes based on scheme ID or project ID query parameters. |
| `associate_schemes_to_projects` | Associates an issue security scheme with a project using the Jira Cloud API, allowing for the remapping of security levels for issues, with the operation being asynchronous. |
| `search_security_schemes` | Searches for and returns issue security schemes in Jira Cloud, allowing filtering by start index, maximum results, ID, or project ID. |
| `get_issue_security_scheme` | Retrieves the details of a specific issue security scheme by its ID, including associated security levels and project mappings. |
| `update_issue_security_scheme` | Updates an existing issue security scheme by specifying the ID in the path using the Jira Cloud API. |
| `get_issue_security_level_members` | Retrieves a list of members associated with issue security levels in a specified issue security scheme using the Jira API. |
| `delete_security_scheme` | Deletes an issue security scheme in Jira and disassociates it from all projects. |
| `add_security_level` | Updates an issue security level within a specified security scheme in Jira. |
| `remove_level` | Deletes an issue security level with the specified `levelId` from an issue security scheme identified by `schemeId`, optionally allowing replacement with another level using the `replaceWith` query parameter. |
| `update_security_level` | Updates an issue security level in a Jira issue security scheme by modifying its name and description using the `PUT` method. |
| `add_security_level_members` | Adds members to a specific security level within an issue security scheme in Jira. |
| `remove_member_from_security_level` | Removes a specified member from an issue security level within a Jira issue security scheme. |
| `get_issue_all_types` | Retrieves a list of all issue types available in Jira using the GET method at the "/rest/api/3/issuetype" endpoint. |
| `create_issue_type` | Creates a new issue type in Jira and adds it to the default issue type scheme. |
| `get_issue_types_for_project` | Retrieves issue types associated with a specified project in Jira using the "GET" method at the "/rest/api/3/issuetype/project" endpoint. |
| `delete_issue_type` | Deletes the specified Jira issue type and migrates associated issues to an alternative type if provided. |
| `get_issue_type` | Retrieves detailed information about a specific issue type in Jira by its ID using the "GET" method. |
| `update_issue_type` | Updates an existing Jira issue type by its ID, returning the modified issue type details or relevant error responses. |
| `get_alternative_issue_types` | Retrieves alternative issue types for a specified issue type ID using the Jira Cloud REST API. |
| `create_issue_type_avatar` | Generates an avatar for a specific issue type in Jira using the "POST" method at the path "/rest/api/3/issuetype/{id}/avatar2", allowing parameters such as size and other query parameters. |
| `get_issue_type_property_keys` | Retrieves all property keys for a specific Jira issue type using the issueTypeId path parameter. |
| `delete_issue_type_property` | Deletes a specific property from an issue type in Jira using the specified property key and issue type ID. |
| `get_issue_type_property` | Retrieves a specific custom property associated with an issue type using its unique identifier and property key. |
| `set_issue_type_property` | Creates or updates a custom property value for a specific Jira issue type, requiring admin permissions and returning success codes for creation/update. |
| `get_all_issue_type_schemes` | Retrieves a paginated list of issue type schemes with optional filtering by ID, ordering, and expansion of related entities. |
| `create_issue_type_scheme` | Creates a new issue type scheme in Jira and returns the created resource. |
| `get_issue_type_schemes_mapping` | Retrieves a paginated list of issue type scheme mappings for classic Jira projects, filtered by scheme ID. |
| `get_issue_type_scheme_for_projects` | Retrieves a paginated list of issue type schemes associated with specific Jira projects using query parameters for pagination (startAt, maxResults) and project filtering (projectId). |
| `assign_issue_type_scheme_to_project` | Assigns an issue type scheme to a Jira Cloud project, requiring global Administer Jira permissions and validating all project issues use scheme types. |
| `delete_issue_type_scheme` | Deletes an issue type scheme by its ID, reassigning any associated projects to the default issue type scheme. |
| `update_issue_type_scheme` | Updates an issue type scheme by modifying its configuration (such as associated issue types) for the specified scheme ID. |
| `add_issue_types_to_issue_type_scheme` | Adds issue types to an existing issue type scheme in Jira Cloud, appending them to the current list and returning a success status if the operation completes without conflicts. |
| `move_issue_type_in_scheme` | Moves issue types within a specified issue type scheme in Jira and returns an empty response on success. |
| `remove_issue_type_from_scheme_by_id` | Deletes an issue type from an issue type scheme using the Jira Cloud API by specifying the `issueTypeSchemeId` and `issueTypeId`, allowing for removal of issue types from schemes. |
| `get_all_issue_type_screen_schemes` | Retrieves a list of issue type screen schemes in Jira with options to filter, paginate, and expand results. |
| `create_issue_type_screen_scheme` | Creates an issue type screen scheme using the Jira Cloud API, allowing administrators to map issue types to specific screen schemes for organizing project workflows. |
| `list_mappings` | Retrieves a list of issue type to screen scheme mappings associated with a specified issue type screen scheme using the Jira Cloud API. |
| `get_project_screen_schemes` | Retrieves a paginated list of issue type screen schemes and their associated projects using the specified query parameters. |
| `update_project_scheme` | Assigns an issue type screen scheme to a project using the Jira API, requiring *Administer Jira* global permission to update project configurations. |
| `delete_issue_type_screen_scheme` | Deletes an issue type screen scheme in Jira and returns a success status upon removal. |
| `update_issue_type_screen_scheme` | Updates the default screen scheme for unmapped issue types in the specified issue type screen scheme. |
| `update_issue_type_screen_mapping` | Updates the mappings of an issue type screen scheme using the PUT method, specifically allowing administrators to append or modify issue type to screen scheme mappings by providing the necessary `issueTypeScreenSchemeId` in the path. |
| `update_default_screen_scheme` | Updates the default screen scheme mapping for an issue type screen scheme identified by the `{issueTypeScreenSchemeId}` using the PUT method, which is used for all unmapped issue types in Jira. |
| `remove_issue_type_mapping` | Removes issue type to screen scheme mappings from an issue type screen scheme in Jira using the provided issue type IDs. |
| `fetch_project_by_scheme` | Retrieves a paginated list of projects associated with a specific issue type screen scheme. |
| `get_auto_complete` | Retrieves JQL search auto-complete data including field references, operators, and suggestions to assist in programmatic query construction. |
| `get_auto_complete_post` | Provides JQL search auto-complete data and field reference information to assist in programmatic query construction or validation. |
| `get_jql_suggestions` | Retrieves JQL search autocomplete suggestions for specific fields, values, predicates, or predicate values to assist in query construction. |
| `get_precomputations` | Retrieves a list of precomputations for a specified JQL function, including when they were created, updated, and last used, allowing apps to inspect their own functions. |
| `update_precomputations` | Updates precomputations (JQL fragments mapped to custom functions) and optionally skips invalid entries based on query parameters. |
| `get_precomputations_by_id` | Performs a computation search using JQL functions in Jira Cloud, allowing users to specify an **orderBy** parameter and returns the results of the computation search via a POST request. |
| `match_issues` | Checks which issues from a provided list match specified JQL queries and returns matched issues for each query. |
| `parse_jql_queries` | Parses a JQL query using the POST method at "/rest/api/3/jql/parse" and returns its abstract syntax tree, allowing for analysis or processing of JQL queries, with optional validation configuration. |
| `migrate_queries` | Converts JQL queries containing usernames or user keys to equivalent queries with account IDs, handling unknown users appropriately. |
| `sanitise_jql_queries` | Sanitizes one or more JQL queries by converting readable details into IDs where a user lacks permission to view the entity, ensuring that unauthorized project names are replaced with project IDs. |
| `get_all_labels` | Retrieves a paginated list of labels starting from a specified index and limited by a maximum number of results using the Jira API. |
| `get_approximate_license_count` | Retrieves the approximate user license count for a Jira instance, which may be cached for up to 7 days. |
| `get_license_count_by_product_key` | Retrieves the approximate license count for a specific application in Jira Cloud using the provided application key. |
| `get_my_permissions` | Retrieves the current user's permissions in Jira, optionally filtered by project, issue, or specific permission keys, and indicates whether each permission is granted. |
| `remove_preference` | Deletes a user's Jira preference specified by the key query parameter and returns a 204 status code on success. |
| `get_preference` | Retrieves the specified user preference value for the currently authenticated user using the provided key parameter. |
| `set_preference` | Creates or updates a user preference in Jira by setting or modifying a specific key-value pair using the PUT method. |
| `delete_locale` | Deletes the locale preference for a user, restoring the default locale setting, using the Jira Cloud platform REST API. |
| `get_locale` | Retrieves the locale preference for the currently authenticated user in Jira using the GET method. |
| `set_locale` | Updates the user's locale preference in Jira, restoring the default if no value is specified (deprecated, use user management API instead). |
| `get_current_user` | Retrieves the authenticated user's profile details (with privacy-based limitations on sensitive fields) from Jira Cloud. |
| `get_notification_schemes` | Retrieves notification schemes listing configured events and their notification recipients for Jira issues, supporting filtering by project, ID, and pagination. |
| `create_notification_scheme` | Creates a new notification scheme using the "POST" method at the "/rest/api/3/notificationscheme" endpoint, returning a successful creation response when the operation is completed. |
| `get_notification_scheme_projects` | Retrieves the association between notification schemes and projects in Jira, including scheme IDs and project IDs, based on query parameters such as notificationSchemeId and projectId. |
| `get_notification_scheme` | Retrieves details of a specific notification scheme by its ID using the Jira API, optionally expanding the response with additional details. |
| `update_notification_scheme` | Updates a notification scheme using its ID, allowing modifications to the scheme's configuration, such as events and recipients. |
| `add_notifications` | Updates notifications for a specific notification scheme in Jira by adding or modifying event-based notification rules. |
| `delete_notification_scheme` | Deletes a specific notification scheme in Jira using its ID, returning appropriate status codes for success or error conditions. |
| `delete_notification_from_scheme` | Deletes a specific notification from a notification scheme in Jira using the specified notification scheme and notification IDs. |
| `get_all_permissions` | Retrieves details of global and project permissions granted to a user using the Jira Cloud REST API. |
| `get_bulk_permissions` | Checks user permissions in Jira projects and returns global and project-specific permission details. |
| `get_permitted_projects` | Retrieves all projects where a user has specified project permissions and returns the list of projects with granted access. |
| `get_all_permission_schemes` | Retrieves a list of all permission schemes in Jira Cloud, optionally expanding the response to include additional details such as groups by using the "expand" query parameter. |
| `create_permission_scheme` | Creates a new permission scheme in Jira using the "POST" method at the "/rest/api/3/permissionscheme" path, allowing for the definition of a permission set with various grants. |
| `delete_permission_scheme` | Deletes a permission scheme specified by the provided `schemeId` using the Jira REST API, removing it from the system. |
| `get_permission_scheme` | Retrieves a specific permission scheme in Jira, identified by its scheme ID, and optionally expands its details with certain information based on the provided expand parameter. |
| `update_permission_scheme` | Updates a permission scheme identified by `{schemeId}` using the PUT method, allowing modifications to its permissions and settings. |
| `get_permission_scheme_grants` | Retrieves the permissions granted by a specific permission scheme in Jira, including details about each permission grant within the scheme. |
| `create_permission_grant` | Adds permissions to a specific permission scheme in Jira, enabling access control configuration for users, groups, or roles. |
| `delete_permission_scheme_entity` | Deletes a permission grant from a permission scheme in Jira using the specified `schemeId` and `permissionId`. |
| `get_permission_scheme_grant` | Retrieves a specific permission grant's details within a Jira permission scheme identified by the scheme ID and permission ID. |
| `get_plans` | Retrieves plan details using pagination and optional filters for trashed or archived items. |
| `create_plan` | Creates a new plan resource via the specified endpoint, requiring a request body with plan details and supporting optional useGroupId query parameter for group association. |
| `get_plan` | Retrieves the details of a specific plan identified by its planId using a GET request. |
| `update_plan` | Updates a plan with the specified ID in "/rest/api/3/plans/plan/{planId}" using the PUT method, potentially modifying plan details based on provided parameters. |
| `archive_plan` | Archives a specific plan in Jira using the PUT method at the "/rest/api/3/plans/plan/{planId}/archive" endpoint, identified by the planId parameter. |
| `duplicate_plan` | Creates a duplicate of the specified Jira plan using the provided plan ID and returns the new plan's details. |
| `get_teams` | Retrieves a paginated list of teams associated with a specific plan in Jira Cloud. |
| `add_atlassian_team` | Adds an Atlassian team to a plan using the Jira Cloud API and returns a status message, allowing for the management of team configurations within plans. |
| `remove_atlassian_team` | Deletes an Atlassian team from a specified plan in Jira Cloud using the "DELETE" method, requiring plan ID and Atlassian team ID as path parameters. |
| `get_atlassian_team` | Retrieves planning settings for an Atlassian team within a specific plan in Jira. |
| `update_atlassian_team` | Associates a specified Atlassian team with a plan identified by a plan ID, using the "PUT" method to update the team assignment. |
| `create_plan_only_team` | Creates a plan-only team in a Jira Cloud plan with specified planning settings and returns the configuration. |
| `delete_plan_only_team` | Deletes a specific team associated with a plan in a REST API (likely related to project management or issue tracking). |
| `get_plan_only_team` | Retrieves planning settings for a specific plan-only team in a Jira plan using the Jira Cloud REST API. |
| `update_plan_only_team` | Updates planning settings for a specific team in a Jira plan using the provided parameters and returns a success status upon completion. |
| `trash_plan` | Moves a specified plan to trash using the Jira API and returns an empty response on success. |
| `get_priorities` | Retrieves a list of all issue priorities in Jira using the "/rest/api/3/priority" endpoint with the GET method. |
| `create_priority` | Creates a new priority in Jira with specified properties and returns the generated ID. |
| `set_default_priority` | Sets the default issue priority in Jira using the PUT method at the "/rest/api/3/priority/default" path. |
| `move_priorities` | Reorders the priority of issues in Jira by updating their sequence using a PUT request. |
| `search_priorities` | Retrieves a list of priorities from Jira using the GET method at "/rest/api/3/priority/search", allowing for customizable queries with parameters like start index, maximum results, ID, project ID, priority name, and expansion options. |
| `delete_priority` | Deletes an issue priority asynchronously by its ID using the Jira Cloud REST API, requiring administrative permissions and returning various status messages based on the outcome. |
| `get_priority` | Retrieves details of a specific issue priority by its ID in Jira. |
| `update_priority` | Updates an issue priority with the specified ID using the Jira Cloud API, allowing modifications to priority details such as name or icon URL. |
| `get_priority_schemes` | Retrieves priority schemes and their associated priorities from a Jira instance using various filters such as priority ID, scheme ID, scheme name, and more. |
| `create_priority_scheme` | Creates a new priority scheme with configurable priority mappings and project associations in Jira. |
| `suggested_priorities_for_mappings` | Submits priority mappings for a scheme and returns the updated configuration upon completion. |
| `list_priorities` | Retrieves a paginated list of available priorities for a specified priority scheme or across all schemes, supporting filtering by query and exclusion criteria. |
| `delete_priority_scheme` | Deletes a specific priority scheme identified by its scheme ID, causing projects that were using it to default to the standard priority scheme. |
| `update_priority_scheme` | Updates a Jira priority scheme configuration with the given ID, rejecting updates if they would require issue migrations. |
| `get_priorities_by_priority_scheme` | Retrieves a paginated list of priorities associated with a specific priority scheme in Jira, supporting startAt and maxResults parameters. |
| `get_projects_by_priority_scheme` | Retrieves a list of projects associated with a specific priority scheme in Jira. |
| `get_all_projects` | Retrieves project details from Jira with optional parameters to expand properties, limit to recent projects, or include specific properties. |
| `create_project` | Creates a new Jira project using the REST API, allowing the specification of project details such as key, name, type, and description. |
| `create_project_template` | Creates a project in Jira from a specified project template and returns a redirect response to the new project. |
| `get_recent` | Retrieves a list of up to 20 recently viewed projects still visible to the user. |
| `search_projects` | Searches for Jira projects using various criteria such as project ID, keys, category, and more, returning a list of matching projects based on the specified parameters using the Jira Cloud REST API. |
| `get_all_project_types` | Retrieves all project types available in Jira Cloud, including those without valid licenses, and can be accessed anonymously without permissions. |
| `get_all_accessible_project_types` | Retrieves a list of project types accessible to the calling user via the Jira Cloud REST API. |
| `get_project_type_by_key` | Retrieves the project type details for a specified project type key using the "GET" method. |
| `get_accessible_project_type_by_key` | Retrieves details of a specific project type accessible to the user in Jira Cloud based on the provided project type key. |
| `delete_project` | Deletes a Jira project identified by its ID or key, with an optional undo capability via query parameter. |
| `get_project` | Retrieves details about a specific Jira project by its ID or key, allowing optional expansion of additional details and properties, using the Jira REST API. |
| `update_project` | Updates or replaces a Jira project identified by the projectIdOrKey and returns the modified project. |
| `archive_project` | Archives a Jira project using the "POST" method by specifying the project ID or key in the path "/rest/api/3/project/{projectIdOrKey}/archive". |
| `update_project_avatar` | Sets the displayed avatar for a Jira project using the specified project ID or key. |
| `delete_project_avatar` | Deletes a custom project avatar (system avatars cannot be deleted) using the Jira REST API. |
| `create_project_avatar` | Loads a custom avatar for a Jira project using the specified parameters and returns the avatar details upon success. |
| `get_all_project_avatars` | Retrieves the list of avatars associated with a specified Jira project, including system and custom avatars. |
| `delete_classification_level` | Removes the default data classification level from a Jira project using the Jira Cloud API, returning a status code indicating success or failure. |
| `get_project_classification_level` | Retrieves the default data classification level configured for a specified Jira project. |
| `update_project_class_default` | Updates the default data classification level for a Jira project. |
| `get_project_components_paginated` | Retrieves a paginated list of components associated with a specified Jira project, optionally filtered and ordered by query parameters. |
| `get_project_components` | Retrieves a list of components for a specified Jira project using its ID or key, with optional filtering by component source. |
| `delete_project_asynchronously` | Deletes a Jira project specified by its ID or key via a POST request and returns relevant status codes. |
| `get_features_for_project` | Retrieves the list of features for a specified Jira project using the project ID or key. |
| `toggle_feature_for_project` | Updates the configuration of a specific feature for a Jira project using the project identifier and feature key. |
| `get_project_property_keys` | Retrieves a list of project property keys for a specified project in Jira Cloud using the provided project ID or key. |
| `delete_project_property` | Deletes a specific project property from a Jira project using the project ID or key and property key, requiring administrative permissions. |
| `get_project_property` | Retrieves the value of a specific project property using the Jira Cloud API and returns it based on the provided project ID or key and property key. |
| `set_project_property` | Updates a project property using the Jira Cloud REST API, allowing custom data to be stored against a specific project by setting the value of a specified property key. |
| `restore` | Restores a deleted or archived Jira project identified by its project ID or key. |
| `get_project_roles` | Retrieves a list of project roles (including names, IDs, and self URLs) for a specific Jira project using its ID or key. |
| `delete_actor` | Deletes a user or group from a specific project role in Jira, returning a success status if removed. |
| `get_project_role` | Retrieves a specific project role's details and associated actors for a Jira project using the provided project identifier and role ID. |
| `add_actor_users` | Partially updates a project role's name or description using the Jira REST API. |
| `set_actors` | Fully updates a project role by ID for a specified Jira project using the provided parameters. |
| `get_project_role_details` | Retrieves role details for a specified project, including information about project roles and their associated members, using a GET request. |
| `get_all_statuses` | Retrieves a list of statuses available for a specific Jira project, identified by its ID or key, using the GET method. |
| `get_project_versions_paginated` | Retrieves a list of versions for a specified Jira project, allowing for pagination, filtering, and expansion of details using various query parameters. |
| `get_project_versions` | Retrieves all versions of a specified Jira project, including version details like names, descriptions, and issue status counts. |
| `get_project_email` | Retrieves email-related information for a specified project using its unique identifier. |
| `update_project_email` | Updates the sender email address for a specific project's notifications and returns a success status upon completion. |
| `get_hierarchy` | Retrieves the hierarchy details for a specific project using the `GET` method at path "/rest/api/3/project/{projectId}/hierarchy". |
| `get_project_issue_security_scheme` | Retrieves the issue security level scheme associated with a specified project in Jira. |
| `get_notification_scheme_by_project` | Retrieves the notification scheme associated with a specific project in Jira, including event configurations and recipient details. |
| `get_assigned_permission_scheme` | Retrieves the permission scheme associated with a specified Jira project by its key or ID, allowing optional expansion of certain details. |
| `assign_permission_scheme` | Assigns a permission scheme to a project using the Jira Cloud API, allowing administrators to manage project permissions by associating a specific permission scheme with a given project. |
| `get_security_levels_for_project` | Retrieves issue security levels for a specified project using the provided project key or ID, returning details about the security levels associated with the project. |
| `get_all_project_categories` | Retrieves a project category from Jira using its ID and returns the category details. |
| `create_project_category` | Creates a new project category in Jira and returns the created category details. |
| `remove_project_category` | Deletes a project category by its ID using the Jira Cloud API, requiring admin permissions and returning a successful response without content if the operation is completed. |
| `get_project_category_by_id` | Retrieves a specific project category by ID from Jira using the REST API. |
| `update_project_category` | Updates a specific project category by ID in Jira using the PUT method, allowing modifications to the category details such as name and description. |
| `validate_project_key` | Validates a project key by confirming the key's validity and checking for existing usage in Jira Cloud. |
| `get_valid_project_key` | Validates a project key by confirming it is a valid string and not in use, returning success or error messages using the Jira Cloud REST API. |
| `get_valid_project_name` | Validates a project name's availability, returning the original name if available or generating a new valid name if unavailable. |
| `get_resolutions` | Retrieves a list of available resolution statuses for Jira issues. |
| `create_resolution` | Creates a new issue resolution in Jira using the REST API and returns the created resolution details. |
| `set_default_resolution` | Sets the default issue resolution in Jira using the REST API, requiring administrative permissions. |
| `move_resolutions` | Moves issue resolutions using the Jira Cloud API with a PUT request to the "/rest/api/3/resolution/move" endpoint. |
| `search_resolutions` | Retrieves a paginated list of Jira issue resolutions using the GET method at the "/rest/api/3/resolution/search" path, allowing for filtering by parameters such as start position, maximum results, resolution ID, and default-only options. |
| `delete_resolution` | Deletes an issue resolution by ID using the Jira API and optionally replaces it with another resolution if specified. |
| `get_resolution` | Retrieves the details of a specific resolution by its ID using the Jira Cloud Platform REST API and returns the resolution information. |
| `update_resolution` | Updates the specified resolution's details in Jira using the provided ID, returning a success status upon completion. |
| `get_all_project_roles` | Retrieves role details in Jira projects using the specified REST API endpoint. |
| `create_project_role` | Creates a new role using the Jira API and returns a status message, handling responses for various HTTP status codes including successful creation, bad requests, unauthorized access, forbidden actions, and conflicts. |
| `delete_project_role` | Deletes a role by its ID using the REST API. |
| `get_project_role_by_id` | Retrieves a specific role in Jira by its ID using the GET method and returns the role details. |
| `partial_update_project_role` | Updates a specific project role's configuration and returns the modified role details. |
| `fully_update_project_role` | Updates or replaces an existing role's configuration via specified ID and returns the operation status. |
| `delete_role_actor_by_id` | Deletes actors from a role using the "DELETE" method with options to specify a user or group ID, and returns corresponding status codes based on the success or failure of the operation. |
| `get_project_role_actors_for_role` | Retrieves a list of actors associated with a specified role ID using the Jira REST API. |
| `add_project_role_actors_to_role` | Adds or modifies actors (users/groups) for a specific project role ID and returns the updated role details. |
| `get_screens` | Retrieves a paginated list of all screens or specified screens by ID in Jira, allowing for optional filtering by query parameters such as start position, maximum results, and query string. |
| `create_screen` | Creates a new screen in Jira using the REST API and returns a successful response if the operation is completed without errors. |
| `add_field_to_default_screen` | Adds a custom field to the default tab of the default screen using the Jira Cloud REST API. |
| `get_bulk_screen_tabs` | Retrieves the list of tabs for a specified screen in Jira Cloud, including pagination support through startAt and maxResult parameters. |
| `delete_screen` | Deletes a specified screen in Jira if not used in screen schemes, workflows, or workflow drafts, returning success if the operation completes. |
| `update_screen` | Updates or replaces a screen resource identified by the specified `screenId` using the PUT method. |
| `get_available_screen_fields` | Retrieves available fields for a specified screen in Jira, including both system and custom fields. |
| `get_all_screen_tabs` | Retrieves the list of tabs configured for a specific screen in Jira using the provided screen ID. |
| `add_screen_tab` | Creates a new tab in a Jira screen using the specified screen ID and returns the created screen tab. |
| `delete_screen_tab` | Deletes a specified screen tab from a Jira screen and returns a success status upon completion. |
| `rename_screen_tab` | Updates the details of a specific screen tab identified by `screenId` and `tabId` using the Jira API, returning a status message upon successful modification. |
| `get_all_screen_tab_fields` | Retrieves all fields associated with a specific screen tab in Jira Cloud. |
| `add_screen_tab_field` | Adds a field to a specified screen tab in Jira and returns the field configuration upon success. |
| `remove_screen_tab_field` | Removes a field from a specific screen tab in Jira and returns an empty response upon success. |
| `move_screen_tab_field` | Moves a screen tab field to a new position using the Jira Cloud platform REST API, allowing for reorganization of issue details fields on a specific screen tab. |
| `move_screen_tab` | Moves a tab to a specified position within a screen using the "POST" method. |
| `get_screen_schemes` | Retrieves a paginated list of screen schemes used in classic projects in Jira Cloud using the GET method, allowing for optional filtering by query parameters such as startAt, maxResults, id, expand, queryString, and orderBy. |
| `create_screen_scheme` | Creates a new screen scheme in Jira for defining screen configurations associated with workflows and returns the created resource upon success. |
| `delete_screen_scheme` | Deletes a screen scheme in Jira using the `DELETE` method, provided it is not used in an issue type screen scheme and is associated with a classic project. |
| `update_screen_scheme` | Updates a specific screen scheme, identified by its ID, in Jira Cloud's classic projects, allowing modifications to its details and settings. |
| `search_for_issues_using_jql` | Searches for Jira issues using JQL queries and returns paginated results with specified fields and expansion options. |
| `search_for_issues_using_jql_post` | Searches Jira issues using JQL queries and returns paginated results. |
| `count_issues` | Retrieves an approximate count of Jira issues matching a specified JQL query using the POST method at the "/rest/api/3/search/approximate-count" endpoint. |
| `search_for_issues_ids` | Searches for Jira issues using JQL (Jira Query Language) and returns a list of matching issue IDs, along with a token for fetching additional results if needed, using the `POST` method at the path "/rest/api/3/search/id". |
| `get_search_by_jql` | Retrieves a list of Jira issues matching a JQL query with pagination support, customizable field selection, and result optimization options. |
| `post_search_jql` | Executes a JQL query to search for issues, returning matching results and pagination tokens. |
| `get_issue_security_level` | Retrieves details of a specific issue security level by its ID in Jira. |
| `get_server_info` | Retrieves information about the Jira instance using the "GET" method at the "/rest/api/3/serverInfo" endpoint. |
| `list_columns` | Retrieves settings for columns using the Jira API and returns relevant data. |
| `update_settings_columns` | Updates board column configurations via a PUT request to modify their settings. |
| `get_statuses` | Retrieves the operational status and readiness of the Jira instance via a lightweight endpoint for monitoring. |
| `get_status` | Retrieves a specific status by its ID or name from Jira using the Jira REST API. |
| `get_status_categories` | Retrieves a list of all visible Jira issue status categories in JSON format. |
| `get_status_category` | Retrieves a specific Jira issue status category by its ID or key using the GET method. |
| `delete_statuses_by_id` | Deletes a specific status entry identified by its ID using the provided parameters and returns a success or error code. |
| `get_statuses_by_id` | Retrieves a list of statuses in Jira using the "/rest/api/3/statuses" endpoint, allowing you to fetch details of statuses based on query parameters like expansion and ID, though specific details about what statuses are returned are not provided. |
| `create_statuses` | Creates commit statuses (error, failure, pending, success) with optional descriptions and target URLs via the GitHub API. |
| `update_statuses` | Updates the statuses in Jira using the PUT method at the "/rest/api/3/statuses" endpoint and returns a status message. |
| `search` | Retrieves a paginated list of Jira statuses with optional filtering by project, search string, or status category. |
| `get_issue_type_usages` | Retrieves a paginated list of issue types associated with a specific project and status, including pagination controls via `nextPageToken` and `maxResults`. |
| `get_project_usages_for_status` | Retrieves project usage information for a specific status identified by the status ID, supporting pagination through optional parameters for the next page token and maximum results. |
| `get_workflow_usages_for_status` | Retrieves the workflows associated with a specific status ID and returns their usage details. |
| `get_task` | Retrieves details for a specific task by ID using a REST API GET request. |
| `cancel_task` | Cancels a specific task by its ID using the POST method at the "/rest/api/3/task/{taskId}/cancel" path. |
| `get_ui_modifications` | Retrieves a paginated list of UI modifications (including project, issue type, and view contexts) from Jira's REST API. |
| `create_ui_modification` | Applies modifications to the user interface using the REST API at the "/rest/api/3/uiModifications" endpoint, returning status codes to indicate success or failure. |
| `delete_ui_modification` | Deletes a UI modification with the specified ID from the system using the DELETE HTTP method. |
| `update_ui_modification` | Updates a UI modification identified by `uiModificationId` using the PUT method. |
| `get_avatars` | Retrieves details about a universal avatar by its type and owner entity ID using the Jira API. |
| `store_avatar` | Creates a new avatar for the specified entity type (e.g., project, issue) using provided parameters (x, y, size) and returns a success status. |
| `delete_avatar` | Deletes a specified avatar associated with a resource type and owner using the Jira API. |
| `get_avatar_image_by_type` | Retrieves a Jira avatar image by type using the "GET" method, allowing specification of size and format for customization. |
| `get_avatar_image_by_id` | Retrieves a specific avatar by type and ID using the Jira Universal Avatar API, allowing customization and display in various formats and sizes. |
| `get_avatar_image_by_owner` | Retrieves an avatar image for a specified owner entity (like user, project, or issue type) by type and ID, allowing optional size and format customization. |
| `remove_user` | Deletes a user from the system using the provided query parameters such as account ID, username, or key, and returns a status code indicating success or failure. |
| `get_user` | Retrieves a specific Jira user's details using the provided account ID, username, or user key via the Jira REST API. |
| `create_user` | Creates a new user in Jira and returns the created user resource upon success. |
| `find_bulk_assignable_users` | Retrieves a list of users who can be assigned issues in one or more specified projects, allowing filtering by various user attributes such as name or account ID. |
| `find_assignable_users` | Searches for users who can be assigned to issues in Jira, allowing filtering by query, session ID, username, account ID, project, issue key, issue ID, and other parameters, returning a list of assignable users. |
| `bulk_get_users` | Retrieves a paginated list of user details for specified account IDs using the Jira REST API. |
| `bulk_get_users_migration` | Retrieves user migration information in bulk for Jira using the GET method, allowing filtering by username, key, and pagination via startAt and maxResults parameters. |
| `reset_user_columns` | Deletes a user's saved column configuration in Jira based on either their account ID or username. |
| `get_user_default_columns` | Retrieves the default issue table columns for a Jira user, specified by either an accountId or the calling user if no accountId is provided, using the Jira Cloud Platform REST API. |
| `set_user_columns` | Updates the columns displayed for a specific user's issue list view in Jira and returns a success status upon completion. |
| `get_user_email` | Retrieves a user's email address for the specified Atlassian account ID using the Jira Cloud API. |
| `get_user_email_bulk` | Retrieves email addresses for multiple Jira users by their account IDs in a single request, bypassing profile visibility restrictions. |
| `get_user_groups` | Retrieves a list of groups associated with a specified Jira user account using their accountId, username, or key. |
| `get_user_nav_property` | Retrieves the value associated with a specified property key for a given account using the GET method. |
| `set_user_nav_property` | Updates a user's navigation property (specified by propertyKey) in Jira using account-based identification and returns the operation status. |
| `find_users_with_all_permissions` | Retrieves users with specified global or project permissions, filtered by query, account ID, or project/issue context, including pagination support. |
| `find_users_for_picker` | Retrieves a list of users and groups for a picker field, allowing filtering by query, exclusion parameters, and pagination, to populate user or group suggestion lists in Jira applications. |
| `get_user_property_keys` | Retrieves the keys of all properties for a user using the Jira Cloud REST API. |
| `delete_user_property` | Deletes a user property identified by a specific property key using the Jira Cloud platform REST API, requiring permissions to manage user properties. |
| `get_user_property` | Retrieves the value of a specified user property using the Jira Cloud API, returning the custom data associated with a user for a given property key. |
| `set_user_property` | Sets or updates a custom property value for a specific Jira user, enabling per-user data storage for integrations and apps. |
| `find_users` | Searches for Jira users by matching a query against display names and email addresses, supporting pagination and specific property filters. |
| `find_users_by_query` | Searches for users in Jira based on query parameters, returning paginated results. |
| `find_user_keys_by_query` | Searches for users based on a specified query, returning a list of matching users, with options to control the result set size and starting point. |
| `find_users_with_browse_permission` | Searches for Jira issues based on specified parameters such as query, username, account ID, issue key, project key, and returns a list of matching issues with pagination options. |
| `get_all_users_default` | Retrieves a list of Jira users, supporting pagination via the `startAt` and `maxResults` parameters, using the GET method at the `/rest/api/3/users` endpoint. |
| `get_all_users` | Searches for Jira users matching query criteria and returns paginated results. |
| `create_version` | Creates a new project version in Jira and returns the details of the created version. |
| `delete_version` | Deletes a Jira project version using the DELETE method, optionally allowing issues to be moved to alternative versions by specifying replacement versions for `fixVersion` and `affectedVersion` fields. |
| `get_version` | Retrieves detailed information about a specific Jira version using the Jira REST API, with options to expand additional fields. |
| `update_version` | Updates an existing version's details (e.g., name, description, release status) in Jira using the specified version ID. |
| `merge_versions` | Merges a Jira version with another specified version and optionally moves associated issues to the target version. |
| `move_version` | Moves a project version to a new position within the ordered version list by specifying its ID and returns a status message indicating the success or failure of the operation. |
| `get_version_related_issues` | Retrieves counts of issues related to a specific Jira version, such as those with the version set as the fix version or affected version, using the "GET" method. |
| `get_related_work` | Retrieves related work items associated with a specific version ID in Jira. |
| `create_related_work` | Associates external related work (e.g., design files, communication links) with a Jira project version via a POST request. |
| `update_related_work` | Updates a version's related work links in Jira using the PUT method at the "/rest/api/3/version/{id}/relatedwork" endpoint. |
| `delete_and_replace_version` | Deletes a project version by ID and swaps it with another version in fixVersion and affectedVersion fields using a POST request. |
| `get_version_unresolved_issues` | Retrieves the count of unresolved issues associated with a specific version ID in Jira using the REST API. |
| `delete_related_work` | Deletes a related work item identified by the specified `relatedWorkId` within a version specified by `versionId`, returning a 204 status code upon successful deletion. |
| `delete_webhook_by_id` | Deletes a Jira webhook by ID using the "DELETE" method at the "/rest/api/3/webhook" endpoint, removing a previously registered webhook. |
| `get_dynamic_webhooks_for_app` | Retrieves a list of webhooks from Jira, allowing for pagination through parameters `startAt` and `maxResults`. |
| `register_dynamic_webhooks` | Registers a new webhook in Jira to trigger HTTP callbacks for specified events. |
| `get_failed_webhooks` | Retrieves a paginated list of failed webhook delivery attempts, supporting pagination via maxResults and after parameters. |
| `refresh_webhooks` | Refreshes Jira webhooks created via Connect Apps to extend their expiration dates using a PUT request. |
| `get_all_workflows` | Retrieves a list of all workflows in Jira or a specific workflow by name, depending on whether the `workflowName` parameter is provided, using the Jira Cloud REST API. |
| `create_workflow` | Creates a new workflow configuration in Jira Cloud using the REST API by sending a POST request to the "/rest/api/3/workflow" endpoint. |
| `list_workflow_rule_configs` | Retrieves and configures workflow rule configurations in Jira using the GET method, allowing filtering by various parameters such as workflow names and types. |
| `update_workflow_rule_config` | Updates the configuration of a workflow transition rule using the Jira API, allowing customization of conditions under which a transition can occur. |
| `delete_workflow_rule_config` | Deletes workflow transition rule configurations from Jira workflows using the "PUT" method. |
| `get_workflows_paginated` | Retrieves a list of workflows in Jira using pagination, allowing filtering by parameters such as workflow name, query string, and active status, and optionally expanding details like statuses. |
| `delete_transition_property` | Deletes a specified property from a workflow transition in Jira using the "DELETE" method, allowing changes to the behavior of transitions by removing custom properties. |
| `get_transition_properties` | Retrieves workflow transition properties for a specified transition ID using query parameters to filter results by keys and workflow details. |
| `update_transition_property` | Creates a workflow transition property using the Jira Cloud API by sending a POST request to the specified endpoint, allowing users to store custom data against a workflow transition and modify its behavior. |
| `put_workflow_transition_property` | Updates a workflow transition property (or creates it if nonexistent) in Jira Cloud using the transition ID, workflow name, and key. |
| `delete_inactive_workflow` | Deletes a specified workflow by its entity ID using the Jira API and returns an empty response on success. |
| `get_workflow_issue_type_usages` | Retrieves issue type usage for a specific workflow within a project using the Jira API, returning data on how issue types are used in that workflow. |
| `get_project_usages_for_workflow` | Retrieves the list of projects that use a specified workflow in Jira, supporting pagination with optional parameters for next page token and maximum results. |
| `list_workflow_schemes` | Retrieves a list of workflow schemes associated with a specific workflow ID, allowing pagination through query parameters like nextPageToken and maxResults. |
| `read_workflows` | Creates new workflows in Jira Cloud using the REST API with the specified parameters and returns a response indicating the outcome. |
| `workflow_capabilities` | Retrieves workflow capabilities (e.g., transitions, statuses) based on specified workflow, project, or issue type identifiers. |
| `create_workflows` | Creates a Jira workflow via REST API and returns success/failure status codes. |
| `validate_create_workflows` | Validates the creation of a new workflow using the Jira API and returns a response based on the validation outcome. |
| `search_workflows` | Searches for and retrieves workflows in Jira using specified query parameters, allowing for pagination, expansion of details, and filtering by active status. |
| `update_workflows` | Updates a workflow using the specified parameters via the POST method at the "/rest/api/3/workflows/update" endpoint, potentially allowing expansion details based on the query parameter "expand". |
| `validate_update_workflows` | Validates workflow updates for Jira Cloud using specified criteria and returns validation results. |
| `get_all_workflow_schemes` | Retrieves a list of workflow schemes in Jira Cloud, allowing for pagination by specifying a start index and maximum number of results, using the Atlassian Jira Cloud REST API. |
| `create_workflow_scheme` | Creates a new workflow scheme in Jira Cloud with specified configurations like default workflow and issue type mappings. |
| `get_workflow_schemes_by_project_id` | Retrieves the workflow scheme project associations for a specified project using the provided `projectId` in the query parameters. |
| `assign_scheme_to_project` | Associates a workflow scheme with a Jira project using the specified scheme ID. |
| `read_workflow_schemes` | Retrieves a list of workflow schemes using provided workflow scheme IDs or project IDs via the Jira Cloud REST API. |
| `update_schemes` | Updates Jira workflow schemes (company-managed or team-managed projects) with immediate effect, optionally creating a draft if active, and migrates issues asynchronously when changing status mappings. |
| `update_workflow_scheme_mappings` | Updates workflow scheme status mappings asynchronously for issue types and triggers issue migrations if needed. |
| `delete_workflow_scheme` | Deletes a specified workflow scheme in Jira, which cannot be active (used by projects), and returns a success status upon completion. |
| `get_workflow_scheme` | Retrieves a workflow scheme by ID from Jira, optionally returning the draft version if it exists. |
| `update_workflow_scheme` | Updates a workflow scheme by setting a new default workflow, allowing for the creation or update of a draft scheme if the original is active. |
| `create_workflow_draft` | Creates a draft copy of a specified workflow scheme in Jira using the REST API. |
| `delete_default_workflow` | Deletes the default workflow from a Jira workflow scheme, resetting it to the system default (jira workflow) and optionally creates/updates a draft workflow scheme if specified. |
| `get_default_workflow` | Retrieves the default workflow assigned to unassociated issue types in a specified Jira workflow scheme. |
| `update_default_workflow` | Updates the default workflow in a Jira Cloud workflow scheme, which applies to all unassigned issue types. |
| `delete_workflow_scheme_draft` | Deletes a draft workflow scheme for a specified workflow scheme ID using the Jira Cloud platform REST API. |
| `get_workflow_scheme_draft` | Retrieves the draft workflow scheme for a specified workflow scheme ID in Jira Cloud, allowing modifications to the active workflow scheme through its draft copy. |
| `update_workflow_scheme_draft` | Updates a draft workflow scheme, creating one if it does not exist for the specified active workflow scheme, using the provided details such as default workflow and issue type mappings. |
| `delete_draft_default_workflow` | Deletes the default workflow for a draft workflow scheme, resetting it to Jira's system workflow, using the specified scheme ID. |
| `get_draft_default_workflow` | Retrieves the default workflow configuration for a draft workflow scheme in Jira. |
| `update_draft_default_workflow` | Sets the default workflow for a draft workflow scheme in Jira, enabling configuration changes before publication. |
| `delete_issue_type_draft_from_scheme` | Deletes a specific issue type mapping from a draft workflow scheme in Jira using the provided workflow scheme ID and issue type. |
| `get_issue_type_draft` | Retrieves the workflow configuration for a specific issue type in a draft workflow scheme. |
| `update_workflow_draft_issue_type` | Updates an issue type in a workflow scheme draft using the Jira Cloud API, allowing modifications to workflow mappings without affecting the active scheme until published. |
| `publish_draft_workflow_scheme` | Publishes a draft workflow scheme in Jira, replacing the active scheme upon successful execution. |
| `delete_draft_workflow_mapping` | Deletes a specific workflow associated with a draft workflow scheme in Jira. |
| `get_draft_workflow` | Retrieves the workflow configuration for a draft workflow scheme in Jira by ID and optional workflow name. |
| `update_draft_workflow_mapping` | Updates the draft workflow scheme's associated workflow for a specified workflow name. |
| `delete_workflow_scheme_issue_type` | Removes the workflow-issue type mapping for a specified issue type in a workflow scheme, creating/updating a draft if the scheme is active and updateDraftIfNeeded is enabled. |
| `get_workflow_scheme_issue_type` | Retrieves the workflow associated with a specific issue type in a workflow scheme, optionally returning the draft configuration if it exists. |
| `set_workflow_scheme_issue_type` | Sets the workflow for a specific issue type in a workflow scheme using the provided ID and issue type parameters. |
| `delete_workflow_mapping` | Deletes a specific workflow from a workflow scheme identified by the provided ID, optionally updating a draft if the scheme is active, using the Jira Cloud REST API. |
| `get_workflow` | Retrieves the workflow configuration for a specified workflow scheme in Jira, optionally returning draft configurations if they exist. |
| `update_workflow_mapping` | Updates a specified workflow scheme by assigning a new workflow, identified by the `workflowName` query parameter, to it using the Jira Cloud platform's REST API. |
| `get_project_usages` | Retrieves the list of projects associated with a specific workflow scheme using pagination. |
| `get_ids_of_worklogs_deleted_since` | Retrieves a list of IDs and delete timestamps for worklogs that have been deleted since a specified time using the Jira API. |
| `get_worklogs_for_ids` | Retrieves a list of worklogs for specified IDs using the Jira API and returns their details. |
| `get_ids_of_worklogs_modified_since` | Retrieves a paginated list of updated worklogs in Jira with optional filtering by timestamp and property expansion. |
| `get_addon_properties` | Retrieves all property keys for a specified Atlassian Connect app. |
| `delete_addon_property` | Deletes a specific property of an Atlassian Connect app using the "DELETE" method, requiring the app's addon key and the property key to be specified in the request path. |
| `get_addon_property` | Retrieves a specific property value for a Connect app using the provided addon key and property key. |
| `update_addon_property` | Updates an app property in Jira Cloud by setting a value for the specified `propertyKey` under the provided `addonKey`, allowing Connect apps to store custom data. |
| `delete_module` | Removes specified or all dynamically registered modules for the calling app via query parameters. |
| `list_dynamic_modules` | Retrieves all dynamically registered modules for the calling Connect app in Jira. |
| `create_module` | Registers dynamic modules in Atlassian Connect apps using the POST method, allowing the specification of modules to be registered via a JSON object. |
| `put_migration_field_update` | Updates multiple entity properties (up to 50 per request) for a specified object during Connect app migrations. |
| `update_entity_properties` | Updates properties for a specific entity type during Atlassian Connect app migration using the provided transfer ID. |
| `search_workflow_rules` | Searches for and returns workflow transition rule configurations migrated from server to cloud, owned by the calling Connect app, using the Jira Cloud REST API. |
| `get_service_registry_by_ids` | Retrieves and registers services from the Atlassian Connect service registry using the provided service IDs. |
| `delete_forge_app_property` | Deletes a property identified by the provided `propertyKey` from the application using the DELETE method and returns a successful response if the operation completes without returning any content. |
| `put_forge_app_property` | Updates or creates a specific application property using the PUT method at the specified path "/rest/forge/1/app/properties/{propertyKey}" based on the provided property key. |
