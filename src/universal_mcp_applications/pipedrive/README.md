# PipedriveApp MCP Server

An MCP Server for the PipedriveApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the PipedriveApp API.


| Tool | Description |
|------|-------------|
| `oauth_request_authorization` | Redirects the user to an authorization server toassistant |
| `oauth_refresh_token` | Issues OAuth 2.0 access tokens, ID tokens, and refresh tokens in response to authentication grants using the POST method. |
| `activities_delete_bulk` | Deletes multiple activities by their IDs using query parameters and returns a success response upon completion. |
| `activities_list_user_activities` | Retrieves a list of activities filtered by user_id, type, date range, completion status, and other parameters. |
| `activities_add_new_activity` | Creates a new activity resource and returns a success status upon creation. |
| `activities_get_all_activities` | Retrieves a paginated collection of activities filtered by parameters such as user, time range, completion status, and activity type. |
| `activities_mark_as_deleted` | Deletes the specified activity by its unique identifier. |
| `activities_get_details` | Retrieves details of an activity by its ID using the GET method. |
| `update_activity` | Updates an existing activity specified by {id} and returns a success status upon completion. |
| `activity_fields_get_all` | Retrieves all activity fields from the Pipedrive API using the "GET" method at the path "/activityFields". |
| `delete_activity_types` | Deletes specified activity types by IDs using their identifiers and returns a success status upon completion. |
| `get_activity_types` | Retrieves a list of available activity types with their details from the Fitbit activity database. |
| `activity_types_add_new_type` | Creates a new activity type using the specified data and returns a success status upon completion. |
| `activity_types_mark_as_deleted` | Deletes an activity type by its ID using the Pipedrive API. |
| `activity_types_update_type` | Updates an existing activity type by modifying its details using the API and returns a successful response. |
| `list_addons` | Retrieves available addons for billing subscriptions, returning a list of additional features or services that can be added to a subscription plan. |
| `call_logs_add_new_log` | Logs API calls at the "/callLogs" endpoint via POST and returns HTTP status codes for operation results. |
| `call_logs_get_all_logs` | Retrieves a list of call logs based on specified query parameters, allowing users to view and manage call history by setting a start point and limiting the number of results returned. |
| `call_logs_delete_log` | Deletes a call log (including any attached audio recordings) without affecting related activities using the specified ID. |
| `call_logs_get_details` | Retrieves a specific call log entry by its unique identifier. |
| `call_logs_attach_recording` | Records a call log using the provided ID by sending a POST request to the specified API endpoint. |
| `channels_create_new_channel` | Creates a new channel resource and returns the operation status. |
| `channels_delete_channel_by_id` | Deletes a channel specified by the ID in the path and returns an empty response on success. |
| `channels_receive_message` | Receives messages on a specified channel and returns a success or error status. |
| `channels_delete_conversation` | Deletes a specific conversation within a channel and returns a success status upon completion. |
| `currencies_get_all_supported` | Retrieves a list of currencies based on a search term using the "GET" method at the "/currencies" path. |
| `deals_get_all_deals` | Retrieves a list of deals based on specified parameters such as user ID, filter ID, stage ID, status, and sorting options, allowing for pagination and filtering by ownership. |
| `deals_create_deal` | Creates a new deal in a CRM system using the POST method at the "/deals" endpoint and returns a success response with a status code of 201. |
| `deals_delete_bulk` | Deletes multiple deals by their comma-separated IDs and returns a success status. |
| `dealsget_all_deals` | Retrieves a paginated list of deals with filtering options for cursor-based navigation, date ranges, user association, stage, and status. |
| `deals_search_by_title_and_notes` | Retrieves a list of deals based on search criteria, including terms, fields, and filters such as person ID, organization ID, status, and other parameters, using the GET method at the "/deals/search" endpoint. |
| `deals_get_summary` | Retrieves a summary of deals based on specified parameters such as status, filter ID, user ID, and stage ID using the GET method at the "/deals/summary" path. |
| `deals_get_timeline_data` | Retrieves a timeline of deal events, allowing users to list and group deals by specified intervals and criteria, including start date, interval type, and additional filters like user or pipeline, and optionally convert totals into a specified currency. |
| `deals_mark_as_deleted` | Deletes a deal by its ID using the "DELETE" method, removing the specified deal from the system. |
| `deals_get_details` | Retrieves details about a specific deal by its ID using the API endpoint "/deals/{id}" with the GET method. |
| `deals_update_properties` | Updates a specific deal by replacing it with new data at the path "/deals/{id}". |
| `deals_list_activities` | Retrieves a list of activities associated with a specific deal, optionally filtered by status and pagination parameters. |
| `deals_duplicate_deal` | Creates a duplicate of the specified deal using its ID and returns the new deal in the response. |
| `deals_list_deal_files` | Retrieves a list of files associated with a specific deal by ID, allowing pagination and sorting of the results. |
| `deals_list_deal_updates` | Retrieves the workflow history and associated changes for a specific deal, optionally filtered by parameters like start time, limit, and item types. |
| `get_participants_changelog` | Retrieves paginated changelog data tracking participant-related modifications for a specific deal using cursor-based pagination. |
| `deals_list_followers` | Retrieves a list of users following a deal, identified by its ID, using the GET method at the "/deals/{id}/followers" path. |
| `deals_add_follower` | Adds followers to a specified deal and returns a success status. |
| `deals_remove_follower` | Removes a specific follower from a deal using the "DELETE" method at the "/deals/{id}/followers/{follower_id}" endpoint. |
| `deals_list_mail_messages` | Retrieves a list of mail messages associated with a specific deal identified by its ID, allowing pagination through optional start and limit parameters. |
| `deals_merge_deals` | Merges a specific deal identified by its ID with another deal and returns the merged result. |
| `deals_list_participants` | Retrieves participants associated with a specific deal, including their marketing status if applicable, and supports pagination parameters. |
| `deals_add_participant` | Lists participants associated with a specific deal in Pipedrive using the provided deal ID. |
| `deals_delete_participant` | Removes a participant from a deal using the DELETE method at the endpoint "/deals/{id}/participants/{deal_participant_id}". |
| `deals_list_permitted_users` | Retrieves the list of users with permission to access a specific deal in Pipedrive. |
| `deals_list_persons_associated` | Retrieves a list of persons associated with a specific deal, optionally paginated using start and limit query parameters. |
| `deals_list_deal_products` | Retrieves a list of products associated with a specific deal, optionally including product data and pagination support. |
| `deals_add_product_to_deal` | Adds one or more products to a deal identified by the specified ID and returns a success status. |
| `deals_update_product_attachment` | Updates or replaces product attachment information associated with a specific deal using the provided `id` and `product_attachment_id`. |
| `deals_delete_attached_product` | Deletes a specific product attachment associated with a deal identified by both IDs and returns a success status upon removal. |
| `deal_fields_get_all_fields` | Retrieves all deal fields configuration with pagination support using start and limit parameters. |
| `deal_fields_add_new_field` | Creates a new custom deal field in the Pipedrive CRM system. |
| `deal_fields_delete_multiple_bulk` | Deletes multiple custom deal fields in Pipedrive by specifying their IDs via a DELETE request to the "/dealFields" endpoint. |
| `deal_fields_get_one_field` | Retrieves the details of a specific deal field by its ID, including schema and configuration. |
| `deal_fields_mark_as_deleted` | Deletes a specific deal field by its ID using the Pipedrive API. |
| `deal_fields_update_field` | Updates an existing deal field's configuration by ID, modifying its properties and schema definition. |
| `files_get_all_files` | Retrieves a list of files using the "GET" method, allowing optional filtering by start position, number of items, and sorting order. |
| `files_upload_and_associate` | Uploads files to the server and returns a success status upon completion. |
| `files_create_remote_file_and_link` | Uploads a remote file using the POST method at the "/files/remote" endpoint. |
| `files_link_remote_file` | Creates a remote link for a file and returns a success status upon completion. |
| `files_mark_as_deleted` | Deletes a specified file using the provided ID and returns a success status upon completion. |
| `files_get_one_file` | Retrieves a file resource identified by the provided ID using the GET method. |
| `files_update_details` | Updates or replaces a file with the specified ID using the PUT method, returning a successful status upon completion. |
| `files_download_file` | Downloads a file from the server using the provided ID and returns the file content upon success. |
| `filters_delete_bulk` | Deletes one or more filters identified by their IDs passed as query parameters. |
| `filters_get_all` | Retrieves a list of filters based on the specified type. |
| `filters_add_new_filter` | Applies filters using the API at the "/filters" endpoint via the POST method and returns a response. |
| `filters_get_helpers` | Retrieves a list of filter helper resources. |
| `filters_mark_as_deleted` | Deletes the specified filter by its ID and returns a success response upon completion. |
| `filters_get_details` | Retrieves a specific filter by its unique identifier from the API. |
| `filters_update_filter` | Updates a filter with a specified ID using the PUT method, allowing for modification of its properties. |
| `goals_create_report` | Creates a new goal entry in the system and returns a status message upon successful creation. |
| `goals_get_by_criteria` | Retrieves a list of goals based on specified criteria, such as type, title, status, assignee, expected outcome details, and timeframe, using the "GET" method at the "/goals/find" endpoint. |
| `goals_update_existing_goal` | Updates an existing goal with the specified ID using the provided data and returns a success response upon completion. |
| `goals_mark_as_deleted` | Deletes a goal identified by its ID using the DELETE method. |
| `goals_get_result` | Retrieves results for a specific goal using a goal ID, optionally filtered by start and end date periods. |
| `item_search_search_multiple_items` | Searches for items using optional filters like term, item types, and exact match, supporting pagination and field selection in the results. |
| `item_search_by_field_values` | Performs a search for specific field values across various entity types, allowing for exact or partial matches, and returns either distinct field values for autocomplete or item IDs based on the specified search criteria. |
| `leads_get_all` | Retrieves a list of leads using the "GET" method at the "/leads" endpoint, allowing filtering by various criteria such as limit, start, archived status, owner ID, person ID, organization ID, filter ID, and sort options. |
| `leads_create_lead` | Creates a new lead by sending a POST request to the "/leads" endpoint, returning a success response upon creation. |
| `leads_get_details` | Retrieves a lead by its unique identifier from the system. |
| `leads_update_lead_properties` | Updates a specific lead by partially modifying its details using the provided ID. |
| `leads_delete_lead` | Deletes a lead with the specified ID and removes all associated data from the system. |
| `leads_list_permitted_users` | Retrieves a list of permitted users for a specific lead, identified by the provided lead ID, using the GET method on the "/leads/{id}/permittedUsers" endpoint. |
| `leads_search_leads` | Retrieves a list of leads based on search criteria, allowing filtering by term, person, or organization, and supports pagination and field selection. |
| `lead_labels_get_all` | Retrieves a list of all lead labels from the Pipedrive API, allowing users to view and manage the labels used to categorize leads visually. |
| `lead_labels_add_new_label` | Creates a new lead label in Pipedrive with specified name and color. |
| `lead_labels_update_properties` | Updates one or more properties of a lead label using the Pipedrive API, allowing for partial modification of a label with the specified ID. |
| `lead_labels_delete_label` | Deletes a specific lead label by its unique identifier. |
| `lead_sources_get_all` | Retrieves a list of available lead sources using the `GET` method at the `/leadSources` path. |
| `legacy_teams_get_all_teams` | Retrieves a list of legacy teams within an organization using the GET method, allowing for optional sorting by specific fields and excluding user IDs from the response. |
| `legacy_teams_add_new_team` | Creates a new team within an organization using the Pipedrive API and returns the team details upon successful creation. |
| `legacy_teams_get_data` | Retrieves data about a specific team identified by its ID, optionally excluding user information, using the Pipedrive Legacy Teams API. |
| `legacy_teams_update_team_object` | Updates an existing team with the specified ID using the Pipedrive API, potentially allowing modifications to team details such as name, manager, or members. |
| `legacy_teams_get_all_users` | Retrieves the list of user IDs belonging to a specified legacy team by team ID. |
| `legacy_teams_add_users_to_team` | Adds users to an existing team in Pipedrive using the API endpoint "/legacyTeams/{id}/users" with the POST method. |
| `legacy_teams_get_user_teams` | Retrieves information about the team memberships of a specific user identified by `{id}` using the Pipedrive API, with options to customize the response by sorting teams and excluding user IDs. |
| `mailbox_get_mail_message` | Retrieves details of a specific email message from the mailbox, optionally including the full message body. |
| `mailbox_get_mail_threads` | Retrieves a list of email threads from a mailbox, filtered by a specified folder, starting from a certain position, and limited to a defined number of results. |
| `mailbox_mark_thread_deleted` | Deletes a specific mail thread by its ID from the mailbox using the "DELETE" method. |
| `mailbox_get_mail_thread` | Retrieves a specific email thread from the mailbox by its ID using the Pipedrive API. |
| `update_mail_thread_by_id` | Updates the properties of a mail thread (e.g., associated deal, read status, or archived state) for the specified thread ID. |
| `mailbox_get_all_mail_messages` | Retrieves all email messages within a specified mail thread using the provided thread ID. |
| `meetings_link_user_provider` | Creates user provider links for meetings using the POST method and returns a status message upon success. |
| `delete_user_provider_link_by_id` | Deletes a user provider link by the specified ID using the DELETE method. |
| `notes_get_all` | Retrieves a filtered list of notes based on specified query parameters like user, lead, deal, person, organization IDs, date ranges, and pinned statuses. |
| `notes_create_note` | Creates a new note entry via the specified endpoint and returns a success status upon completion. |
| `notes_delete_note` | Deletes a note with the specified {id} from the collection of notes using the DELETE method. |
| `notes_get_details` | Retrieves a specific note by its ID using the "GET" method at "/notes/{id}". |
| `notes_update_note` | Updates an existing note resource identified by the path ID and returns the updated data. |
| `notes_get_all_comments` | Retrieves comments for a specific note with pagination support using path and query parameters. |
| `notes_add_new_comment` | Adds a new comment to a note specified by its ID using the POST method. |
| `notes_get_comment_details` | Retrieves a specific comment from a note by its ID and comment ID using the API. |
| `notes_update_comment` | Updates a specific comment for a note using the PUT method, allowing complete replacement of the comment's content identified by the note ID and comment ID. |
| `notes_delete_comment` | Deletes a specific comment from a note using the provided comment identifier and note ID. |
| `note_fields_get_all_note_fields` | Retrieves a list of note fields using the API endpoint at "/noteFields" via the GET method. |
| `delete_organizations` | Deletes one or more organizations identified by their IDs using the "DELETE" method on the "/organizations" path. |
| `organizations_get_all` | Retrieves a list of organizations filtered by user ID, filter criteria, alphabetical starting character, pagination settings, and sorting parameters. |
| `create_organization` | Creates a new organization using the API and returns a success status upon creation. |
| `list_organizations` | Retrieves a list of organizations with optional filtering by owner, time range, and alphabetical criteria[1][2][5]. |
| `organizations_search_by_criteria` | Retrieves a list of organizations based on a search term, allowing for customization by specifying fields, exact match, and pagination parameters using the "GET" method. |
| `delete_organization_by_id` | Deletes an organization and disassociates all members from it using the specified organization ID in the path. |
| `organizations_get_details` | Retrieves details of a specific organization by its unique identifier. |
| `organizations_update_properties` | Updates the specified organization's details using the provided ID and returns a success status upon completion. |
| `organizations_list_activities` | Retrieves a filtered list of activities for an organization including optional parameters for start time, result limits, completion status, and exclusions. |
| `organizations_list_deals` | Retrieves a list of deals associated with a specific organization using the Pipedrive API, allowing for pagination and filtering by status. |
| `get_organization_files` | Retrieves a list of files associated with a specific organization, optionally filtered, paginated, and sorted by query parameters. |
| `organizations_list_updates_about` | Retrieves flow-related data for a specific organization, optionally filtered by time range, item type, and pagination parameters. |
| `organizations_list_followers` | Retrieves a list of followers for an organization with the specified ID using the GitHub API. |
| `organizations_add_follower` | Adds a follower to a GitHub organization using the POST method at the "/organizations/{id}/followers" endpoint. |
| `organizations_delete_follower` | Removes a follower from an organization with the specified ID and follower ID using the GitHub API. |
| `organizations_list_mail_messages` | Retrieves a list of mail messages associated with an organization identified by the specified ID, allowing pagination through the start and limit parameters. |
| `organizations_merge_two` | Configures merge settings for a GitHub organization using the provided organization ID and returns a success status upon completion. |
| `list_permitted_users_by_org_id` | Retrieves a list of permitted users for a specified organization using the "GET" method at the "/organizations/{id}/permittedUsers" endpoint. |
| `organizations_list_persons` | Retrieves a list of persons associated with an organization, identified by the organization ID, with optional pagination using start and limit parameters. |
| `list_organization_fields` | Retrieves a list of organization fields, including custom fields, using the "GET" method at "/organizationFields", supporting query parameters like "start" and "limit" for pagination. |
| `organization_fields_add_new_field` | Adds a new organization field using the POST method at the "/organizationFields" path, allowing the creation of custom fields for organizational data management. |
| `delete_organization_fields` | Deletes specified organization fields by their IDs and returns a success status upon completion. |
| `get_organization_field_by_id` | Retrieves data about a specific organization field based on the provided field ID using the Pipedrive API. |
| `delete_organization_field_by_id` | Deletes an organization field identified by the provided ID using the DELETE method. |
| `organization_fields_update_field` | Updates an existing organization field by ID and returns the updated field data upon success. |
| `get_organization_relationships` | Retrieves organization relationships based on the specified organization ID. |
| `create_organization_relationship` | Creates an organization relationship and returns a success confirmation upon completion. |
| `delete_org_relationship_by_id` | Deletes a specific organization relationship by its ID using the GitHub API. |
| `get_org_relationship_by_id` | Retrieves a specific organization relationship by its ID along with calculated values for the base organization. |
| `update_org_relationship_by_id` | Updates an organizational relationship identified by `{id}` using the GitHub API and returns a success status upon completion. |
| `permission_sets_get_all` | Retrieves all permission sets for a specified application using query parameters. |
| `permission_sets_get_one` | Retrieves a specific permission set by its ID from the collection of permission sets using the GET method, returning detailed information about the set. |
| `permission_sets_list_assignments` | Retrieves a paginated list of assignments associated with a specific permission set using the provided ID and query parameters for pagination. |
| `persons_delete_multiple_bulk` | Deletes one or more persons from a database by specifying their IDs in the query parameters. |
| `persons_list_all_persons` | Retrieves a list of persons based on specified parameters such as user ID, filter ID, first character, start index, limit, and sort order. |
| `persons_create_new_person` | Creates a new person record in the system and returns the created resource. |
| `persons_get_all` | Retrieves a collection of persons based on specified criteria such as cursor, limit, date range, owner ID, and first character, using the GET method at the "/persons/collection" endpoint. |
| `persons_search_by_criteria` | Searches for persons based on a given term, allowing filtering by fields, exact match, organization ID, and additional options to customize the search results, using the GET method at the "/persons/search" endpoint. |
| `persons_mark_as_deleted` | Deletes a specific person by ID and returns a success status upon completion. |
| `persons_get_person_details` | Retrieves details of a specific person by their unique identifier. |
| `persons_update_properties` | Updates a person's details at the specified ID using the PUT method, replacing the entire existing record with the new data provided. |
| `persons_list_activities` | Retrieves a list of activities for a person identified by `{id}`, allowing optional filtering by start time, activity limit, completion status, and exclusions. |
| `persons_list_deals` | Retrieves a list of deals associated with a person, filtered by status, sorted as specified, and paginated based on the provided start and limit parameters. |
| `persons_list_person_files` | Retrieves a list of files associated with a specific person ID, optionally filtered by start date, size limit, and sorting parameters. |
| `persons_list_updates_about` | Retrieves a workflow or process flow associated with a specific person ID, optionally filtered by start time, result limit, inclusion of all changes, and specific items. |
| `persons_list_followers` | Retrieves a list of followers associated with the specified person ID. |
| `persons_add_follower` | Adds followers to a person with the specified ID using the API. |
| `persons_delete_follower` | Removes a specific follower from a person's followers list using the "DELETE" method. |
| `persons_list_mail_messages` | Retrieves mail messages associated with a specific person ID, with pagination support via start and limit parameters. |
| `persons_merge_two` | Merges user data by updating the specified person's record using the provided ID in the path. |
| `persons_list_permitted_users` | Retrieves a list of users permitted to access or interact with the specified person's data or resources. |
| `persons_delete_picture` | Deletes the profile picture associated with the specified person ID and returns a success status. |
| `persons_add_picture` | Adds a picture to a person's profile using their ID. |
| `persons_list_products` | Retrieves a list of products associated with a person identified by their ID, with optional filtering by start index and limit. |
| `person_fields_get_all_fields` | Retrieves data about all person fields associated with the authorized user's company using the Pipedrive API, returning a schema that includes custom fields. |
| `person_fields_add_new_field` | Creates or updates person field definitions in the Pipedrive API, returning a success status upon completion. |
| `delete_person_fields` | Deletes one or more person fields in Pipedrive by specifying their IDs using the `ids` parameter in the API request. |
| `person_fields_get_specific_field` | Retrieves specific details about a person field using the "GET" method at the path "/personFields/{id}". |
| `person_fields_mark_as_deleted` | Deletes a custom person field in Pipedrive using the specified field ID. |
| `person_fields_update_field` | Updates a specific person's fields identified by `{id}` using the PUT method. |
| `pipelines_get_all` | Retrieves a list of pipelines and returns them in the response. |
| `pipelines_create_new_pipeline` | Creates a new pipeline using the POST method and returns a response upon successful creation. |
| `pipelines_delete_pipeline` | Deletes a pipeline with the specified ID using the DELETE method. |
| `get_pipeline_by_id` | Retrieves details for a specific pipeline identified by its ID, optionally converting totals to a specified currency. |
| `pipelines_update_properties` | Updates a pipeline by its ID using the specified data and returns a successful response upon completion. |
| `get_conversion_stats_for_pipeline` | Retrieves pipeline conversion statistics (e.g., rates or metrics) for a specified pipeline ID, filtered by date range and/or user ID. |
| `pipelines_list_deals` | Retrieves deals in a specific pipeline across all stages, optionally filtered by user, stage, or custom criteria, and supports pagination and summary conversion. |
| `get_pipeline_movement_stats` | Retrieves movement statistics for a specific pipeline identified by `{id}`, allowing users to filter the data by `start_date`, `end_date`, and `user_id`. |
| `products_get_all_products` | Retrieves a list of products using the "GET" method at the "/products" endpoint, allowing filtering by user ID, filter ID, product IDs, first character, summary preference, and pagination controls via start and limit parameters. |
| `products_create_product` | Creates a new product resource and returns a success status upon creation. |
| `products_search_by_fields` | Retrieves a list of products based on a search term, allowing for customization with parameters such as fields to include, exact match requirements, and pagination options. |
| `products_mark_as_deleted` | Deletes the specified product by its ID and returns a success status upon completion. |
| `products_get_details` | Retrieves product details by ID. |
| `products_update_product_data` | Updates an entire product at the specified ID using the PUT method, replacing all existing data with new values. |
| `products_get_deals` | Retrieves a list of deals associated with a specific product, identified by its ID, using the "GET" method at the "/products/{id}/deals" path. |
| `products_list_product_files` | Retrieves a list of files for a specific product by ID, with options to filter using start index, limit results, and sort order. |
| `products_list_product_followers` | Retrieves a list of followers for a specific product identified by `{id}`, allowing optional filtering by pagination parameters `start` and `limit`. |
| `products_add_follower` | Adds a follower to a product using the provided product ID and returns a success status upon addition. |
| `products_delete_follower` | Deletes a follower from a product, specified by the product's ID and the follower's ID. |
| `products_list_permitted_users` | Retrieves a list of permitted users for a specific product identified by its ID using the "GET" method. |
| `delete_product_fields_by_ids` | Deletes product fields by ID using the DELETE method at the "/productFields" path. |
| `product_fields_get_all_fields` | Retrieves a paginated list of product fields, supporting optional start and limit parameters for result filtering. |
| `product_fields_add_new_field` | Adds a new product field using the "POST" method at the "/productFields" endpoint, allowing customization of product data fields for integration purposes. |
| `product_fields_mark_as_deleted` | Deletes a specific product field by its ID via the Pipedrive API. |
| `product_fields_get_one_field` | Retrieves specific product fields by ID using the "GET" method at the "/productFields/{id}" endpoint. |
| `product_fields_update_field` | Updates a product field by replacing its entire record with a new version, specified by the ID provided in the path. |
| `projects_get_all_projects` | Retrieves a list of projects using the "GET" method at the "/projects" endpoint, allowing users to filter results by ID, status, phase, and include archived projects. |
| `projects_create_project` | Creates a new GitLab project and returns the created project details. |
| `projects_get_details` | Retrieves a project by its specified ID using the GET method and returns the associated data. |
| `projects_update_project` | Updates a project with the specified ID at the path "/projects/{id}" by replacing its entire resource with the provided data using the PUT method. |
| `projects_mark_as_deleted` | Deletes a project by its ID using the specified DELETE method. |
| `projects_archive_project` | Archives a project using the provided project ID and returns a status message. |
| `projects_get_project_plan` | Retrieves the plan details for a specific project identified by its unique ID. |
| `update_project_plan_activity` | Updates a project activity using the PUT method, specifying the project and activity IDs in the path. |
| `projects_update_plan_task` | Updates a specific task in a project plan and returns the updated task details. |
| `projects_get_groups` | Retrieves a list of groups associated with a specific project based on the provided project ID. |
| `projects_get_project_tasks` | Retrieves a list of tasks for a specific project using the project ID. |
| `projects_get_project_activities` | Retrieves a list of activities for a specific project identified by the path parameter "id" using the "GET" method. |
| `projects_get_all_boards` | Retrieves a list of project boards using the GET method. |
| `get_project_board_by_id` | Retrieves a specific project board by its ID using the "GET" method at the "/projects/boards/{id}" endpoint. |
| `projects_get_phases` | Retrieves a list of project phases filtered by board_id. |
| `get_project_phase_by_id` | Retrieves a specific project phase by its unique identifier. |
| `list_project_templates` | Retrieves a list of project templates using the "GET" method at the "/projectTemplates" path, allowing pagination via optional query parameters for cursor and limit. |
| `project_templates_get_details` | Retrieves the details of a specific project template by its ID. |
| `recents_get_changes_after` | Retrieves a paginated list of recent items filtered by timestamp and quantity parameters. |
| `roles_get_all_roles` | Retrieves a list of roles with optional pagination parameters (start and limit) for managing or displaying role-based data. |
| `roles_create_role` | Creates a new role using the API by sending a POST request to the "/roles" endpoint. |
| `roles_mark_as_deleted` | Deletes a role by its unique identifier and returns a success status upon removal. |
| `roles_get_one_role` | Retrieves role details by ID using the GET method from the "/roles/{id}" endpoint. |
| `roles_update_role_details` | Updates an existing role identified by the specified ID using the PUT method. |
| `roles_list_role_assignments` | Retrieves a list of assignments for a role identified by `{id}`, allowing optional pagination with `start` and `limit` query parameters. |
| `roles_assign_user` | Assigns roles to specific resources using the "POST" method at the path "/roles/{id}/assignments". |
| `roles_get_role_settings` | Retrieves the settings for a specific role identified by the provided ID. |
| `roles_add_or_update_setting` | Updates the settings for a specific role identified by the ID and returns a success status. |
| `roles_list_pipeline_visibility` | Retrieves a list of pipelines for a role identified by `{id}` using the `GET` method, allowing optional filtering by visibility. |
| `roles_update_pipeline_visibility` | Updates or creates a pipeline for a specific role identified by the "id" parameter using the PUT method. |
| `stages_delete_bulk` | Deletes a specified stage in Amazon API Gateway, which removes the stage resource and may impact API usability if it's the only stage associated with a deployment. |
| `stages_get_all` | Retrieves a list of stages filtered by pipeline, paginated with start and limit parameters. |
| `stages_create_new_stage` | Creates a new stage entry via the specified path and returns a success status upon completion. |
| `stages_delete_stage` | Deletes a stage by its ID using the DELETE method at the "/stages/{id}" path. |
| `stages_get_one_stage` | Retrieves specific stage details by ID, optionally filtering by visibility using the "everyone" query parameter. |
| `stages_update_details` | Updates a stage with the specified ID using the "PUT" method at the path "/stages/{id}". |
| `stages_get_stage_deals` | Retrieves a list of deals in a specific stage using optional filtering, pagination, and ownership parameters. |
| `subscriptions_get_details` | Retrieves the subscription details for the specified subscription ID. |
| `subscriptions_delete_marked` | Deletes a specific subscription using its identifier. |
| `subscriptions_find_by_deal_id` | Retrieves subscription details for a specific deal using the provided deal ID. |
| `subscriptions_get_payments` | Retrieves payment details for a specific subscription identified by its ID. |
| `subscriptions_add_recurring` | Creates a new recurring subscription using the POST method at the "/subscriptions/recurring" path, allowing for scheduled payments to be set up for ongoing services or products. |
| `create_installment_plan` | Creates an installment subscription with variable payment amounts and dates for a deal, returning details upon successful creation. |
| `subscriptions_update_recurring` | Updates a recurring subscription identified by the provided ID using the PUT method. |
| `update_installment_subscription` | Updates an installment subscription by modifying its details using the provided ID. |
| `cancel_recurring_subscription` | Cancels a recurring subscription by ID using the specified HTTP PUT method and returns a success status upon successful cancellation. |
| `tasks_list_all_tasks` | Retrieves a list of tasks with optional filtering by assignee, project, parent task, status, and pagination parameters. |
| `tasks_create_task` | Creates a new task entity and returns a success status upon resource creation. |
| `tasks_get_details` | Retrieves a specific task by its unique identifier. |
| `tasks_update_task` | Updates a specific task by replacing it entirely with new data using the provided task ID. |
| `tasks_delete_task` | Deletes the specified task by its unique identifier and returns a success status upon completion. |
| `users_get_all` | Retrieves a list of users using the "GET" method at the "/users" path. |
| `users_add_new_user` | Creates a new user account using the POST method and returns a success message upon completion. |
| `users_find_by_name` | Searches for users by specified criteria or email and returns matching results. |
| `users_get_current_user_data` | Retrieves information about the currently authenticated user using the API. |
| `users_get_user` | Retrieves a specific user's details by their unique identifier. |
| `users_update_details` | Updates a user's information by replacing the entire resource at the specified ID using the PUT method, returning success or error status codes based on the operation's outcome. |
| `users_list_followers` | Retrieves the list of followers for a specified user. |
| `users_list_permissions` | Retrieves the permissions associated with a specific user identified by their unique ID. |
| `users_list_role_assignments` | Retrieves a list of role assignments for a specified user, allowing pagination with optional start and limit query parameters. |
| `users_list_role_settings` | Retrieves the role settings for a specific user identified by the `id` path parameter. |
| `get_user_connections` | Retrieves user connections using the "GET" method and returns relevant data. |
| `get_user_settings` | Retrieves user settings metadata including available endpoints for managing user configurations. |
| `webhooks_get_all` | Retrieves information about existing webhooks, returning details about registered endpoints and event triggers. |
| `webhooks_create_new_webhook` | Sends a webhook notification via the POST method to the "/webhooks" endpoint, triggering event-driven data transfer and processing between systems. |
| `webhooks_delete_existing_webhook` | Deletes a webhook endpoint by its ID and returns a confirmation or error message. |
