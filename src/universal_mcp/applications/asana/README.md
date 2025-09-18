# AsanaApp MCP Server

An MCP Server for the AsanaApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the AsanaApp API.


| Tool | Description |
|------|-------------|
| `get_an_allocation` | Retrieves details about an allocation by its GUID using the API endpoint "/allocations/{allocation_gid}" with optional fields and formatting controlled by query parameters "opt_fields" and "opt_pretty". |
| `update_an_allocation` | Updates or creates a resource identified by the allocation GID at the "/allocations/{allocation_gid}" path using the PUT method. |
| `delete_an_allocation` | Deletes the specified allocation by its global identifier and returns a status code indicating success or failure. |
| `get_multiple_allocations` | Retrieves a list of resource allocations filtered by parent, assignee, workspace, and pagination parameters. |
| `create_an_allocation` | Creates a new allocation using the API and returns a successful response upon completion, with optional fields and pretty printing available through query parameters. |
| `get_an_attachment` | Retrieves details for a specific attachment using its identifier, with optional fields and pretty-printed responses. |
| `delete_an_attachment` | Deletes an attachment identified by the attachment GID using the DELETE method. |
| `get_attachments_from_an_object` | Retrieves a list of attachments using the "GET" method at the "/attachments" endpoint, allowing optional filtering by limit, offset, parent, and additional fields for custom output. |
| `get_audit_log_events` | Retrieves a list of audit log events for a specified workspace, allowing filtering by time range, event type, actor type, and other parameters. |
| `submit_parallel_requests` | Processes a batch of API requests in a single call, allowing for efficient execution of multiple operations defined at the "/batch" path using the "POST" method. |
| `create_acustom_field` | Creates a new custom field at the "/custom_fields" endpoint using the "POST" method, allowing for optional parameters to specify additional fields or formatting options. |
| `get_acustom_field` | Retrieves the details of a specific custom field using its unique identifier and supports optional query parameters for additional field data and formatted output. |
| `update_acustom_field` | Updates the specified custom field's configuration for the given object (e.g., project) and returns the modified resource. |
| `delete_acustom_field` | Deletes a specific custom field by its globally unique identifier (GID) and returns an empty response upon success. |
| `get_aworkspace_scustom_fields` | Retrieves a list of custom fields for a specified workspace using the Asana API, allowing for optional filtering and formatting of the response. |
| `create_an_enum_option` | Creates a new enum option for a custom field and allows specifying its position relative to existing options. |
| `reorder_acustom_field_senum` | Reorders the enum options for a custom field using the Asana API by inserting an enum option at a specified position, allowing customization of the options' order. |
| `update_an_enum_option` | Updates an existing enum option's details in the custom field and returns the modified enum option. |
| `get_aproject_scustom_fields` | Retrieves custom field settings for a project using a specified project GID, allowing for optional filtering by fields, formatting, and pagination. |
| `get_aportfolio_scustom_fields` | Retrieves custom field settings for a portfolio using the "GET" method, allowing for optional parameters to customize the output. |
| `get_events_on_aresource` | Retrieves a list of events using the "GET" method at the "/events" endpoint, allowing optional filtering by fields, resource, synchronization status, and output format. |
| `get_agoal` | Retrieves information about a specific goal using the `GET` method at the path `/goals/{goal_gid}`, allowing optional parameters for customizing output fields and formatting. |
| `update_agoal` | Updates a specific goal identified by its GID using the PUT method at the path "/goals/{goal_gid}", optionally including query parameters for custom fields and formatting. |
| `delete_agoal` | Deletes a specific goal resource identified by the `goal_gid` at the path "/goals/{goal_gid}" using the HTTP DELETE method. |
| `get_goals` | Retrieves a list of goals using the GET method at the "/goals" endpoint, allowing filtering by parameters such as portfolio, project, task, team, workspace, and time periods. |
| `create_agoal` | Creates a new goal in the system and returns the created resource. |
| `create_agoal_metric` | Sets a metric for a specific goal identified by `{goal_gid}` and returns the updated goal data. |
| `update_agoal_metric` | Sets the current metric value for a specified goal using the "POST" method at the "/goals/{goal_gid}/setMetricCurrentValue" endpoint. |
| `add_acollaborator_to_agoal` | Adds followers to a specific goal using the "POST" method at the "/goals/{goal_gid}/addFollowers" endpoint and returns a status message based on the operation's success or failure. |
| `remove_acollaborator_from_agoal` | Removes followers from a specified goal using the POST method at the "/goals/{goal_gid}/removeFollowers" path. |
| `get_parent_goals_from_agoal` | Retrieves parent goals associated with a specific goal identified by its goal_gid. |
| `get_agoal_relationship` | Retrieves a goal relationship object by its GID, optionally including additional fields in the response, using the Asana API. |
| `update_agoal_relationship` | Updates a goal relationship using the Asana API and returns a response indicating the outcome of the operation. |
| `get_goal_relationships` | Retrieves compact goal relationship objects between goals, projects, or portfolios with optional filtering and field selection. |
| `add_asupporting_goal_relationship` | Adds a supporting relationship to a specified goal using the POST method at the "/goals/{goal_gid}/addSupportingRelationship" endpoint. |
| `removes_asupporting_goal_relationship` | Removes the supporting relationship from a specified goal and returns a status message. |
| `get_ajob_by_id` | Retrieves job details using the specified job GID, with optional fields and formatting controls, via a GET request to the "/jobs/{job_gid}" endpoint. |
| `get_multiple_memberships` | Retrieves paginated membership records with optional parent, member, and field selection parameters. |
| `create_amembership` | Creates a new membership by sending a POST request to the "/memberships" endpoint, potentially returning a newly created membership resource with a status code indicating successful creation. |
| `get_amembership` | Retrieves membership details for a specified membership ID, supporting optional field selection and formatted responses. |
| `update_amembership` | Updates an existing membership identified by `{membership_gid}` using the PUT method. |
| `delete_amembership` | Deletes a membership by its GUID using the API, removing the associated relationship between entities. |
| `create_an_organization_export_request` | Initiates a request to export an organization's complete data in JSON format, returning a status response upon successful creation. |
| `get_details_on_an_org_export_request` | Retrieves information about an organization export using the provided GID, allowing optional specification of additional fields and pretty-print formatting. |
| `get_multiple_portfolios` | Retrieves a list of portfolios with optional filtering and field selection parameters. |
| `create_aportfolio` | Creates a new portfolio and returns the result, optionally including specified fields and formatted output, using the Portfolio API. |
| `get_aportfolio` | Retrieves details about a specific portfolio identified by `{portfolio_gid}` using the `GET` method, allowing optional fields (`opt_fields`) and pretty formatting (`opt_pretty`) in the query parameters. |
| `update_aportfolio` | Replaces the entire portfolio resource with the provided data and returns the updated portfolio. |
| `delete_aportfolio` | Deletes the specified portfolio and returns a success status or error code. |
| `get_portfolio_items` | Retrieves a list of items associated with a specified portfolio using a GET request, allowing for optional parameters to customize the response fields and pagination. |
| `add_aportfolio_item` | Adds an item to a specified portfolio using a POST request, requiring item placement parameters. |
| `remove_aportfolio_item` | Removes an item from a portfolio using the provided path "/portfolios/{portfolio_gid}/removeItem" via a POST request. |
| `add_acustom_field_to_aportfolio` | Adds a custom field to a specified portfolio by creating a custom field setting using the Asana API. |
| `remove_acustom_field_from_aportfolio` | Removes a custom field setting from a portfolio and returns a success status. |
| `add_users_to_aportfolio` | Adds specified users as members to a portfolio and returns the updated portfolio record. |
| `remove_users_from_aportfolio` | Removes members from a portfolio using the specified portfolio ID and returns a status message. |
| `get_multiple_portfolio_memberships` | Retrieves portfolio membership details in Asana, including associated users and workspaces, with optional filtering and output field selection. |
| `get_aportfolio_membership` | Retrieves details about a portfolio membership by its GID, optionally including additional fields and formatted output. |
| `get_memberships_from_aportfolio` | Retrieves a list of portfolio memberships for a specific portfolio identified by its GID, allowing for optional filtering by user and customizing the response with additional fields. |
| `get_multiple_projects` | Retrieves a list of projects using the specified parameters such as limit, offset, workspace, team, archived status, optional fields, and formatting options. |
| `create_aproject` | Creates a new GitLab project with customizable fields and returns a success status upon completion. |
| `get_aproject` | Retrieves a specific project's details using its unique identifier (project_gid) with options to customize the response fields and formatting. |
| `update_aproject` | Updates an existing project at the specified path, replacing its entire resource with the provided request content, using the PUT method. |
| `delete_aproject` | Deletes a project identified by the project GID using the DELETE method at the path "/projects/{project_gid}", with optional support for pretty-printed output. |
| `duplicate_aproject` | Creates a duplicate of the specified project, including its structure and dependencies, while allowing optional field customization. |
| `get_projects_atask_is_in` | Retrieves the projects associated with a specific task using the GET method, allowing for optional customization of output fields and pagination. |
| `get_ateam_sprojects` | Retrieves a paginated list of projects associated with a specific team, supporting optional filtering for archived status and custom field selection. |
| `create_aproject_in_ateam` | Adds a project to a team using the GitHub API and returns a success status. |
| `get_all_projects_in_aworkspace` | Retrieves a list of projects for a specified workspace, allowing customization through parameters such as limit, offset, archived status, and optional fields, using the GET method. |
| `create_aproject_in_aworkspace` | Creates a new project within the specified workspace using optional query parameters to control response fields and formatting. |
| `add_acustom_field_to_aproject` | Adds a custom field setting to a specified project using the POST method via the API endpoint "/projects/{project_gid}/addCustomFieldSetting", allowing optional query parameters for field selection and response formatting. |
| `remove_acustom_field_from_aproject` | Removes a custom field setting from a specified project using the Asana API by sending a POST request to the "/projects/{project_gid}/removeCustomFieldSetting" endpoint. |
| `get_task_count_of_aproject` | Retrieves task counts for a specified project using the Asana API, allowing users to obtain an object containing task count fields by opting in with the `opt_fields` parameter. |
| `add_users_to_aproject` | Adds members to a project specified by its project GID using the POST method. |
| `remove_users_from_aproject` | Removes specified members from a project using their identifiers and returns an updated project object or error status. |
| `add_followers_to_aproject` | Adds specified users as followers to a project and returns a success or error status. |
| `remove_followers_from_aproject` | Removes specified followers from a project identified by its GID, updating the project's record without affecting its membership status. |
| `create_aproject_template_from_aproject` | Saves a project as a template using the POST method at "/projects/{project_gid}/saveAsTemplate," allowing for the creation of new projects with predefined structures based on existing projects. |
| `get_aproject_brief` | Retrieves a specific project brief identified by its unique identifier and returns its details, optionally including additional fields or formatted responses. |
| `update_aproject_brief` | Updates or replaces a project brief with the specified ID and returns the modified resource. |
| `delete_aproject_brief` | Deletes a specific project brief identified by its GID using the Asana API and returns an empty data record upon successful deletion. |
| `create_aproject_brief` | Creates a project brief for the specified project using the provided data and returns the newly created brief. |
| `get_aproject_membership` | Retrieves details of a specific project membership by its ID, including optional fields and formatted output. |
| `get_memberships_from_aproject` | Retrieves a list of project memberships with optional query parameters for filtering and pagination. |
| `get_aproject_status` | Retrieves a specific project status by its GID using the "GET" method, allowing for optional fields and pretty-printing. |
| `delete_aproject_status` | Deletes a specific project status by its GID and returns an empty response upon success. |
| `get_statuses_from_aproject` | Retrieves a list of project statuses for a specified project and returns paginated results with optional field filtering. |
| `create_aproject_status` | Creates a new project status for the specified project and returns the created status, supporting optional field selection and pretty-printed responses. |
| `get_aproject_template` | Retrieves a specific project template by its unique identifier, providing configurable output fields and formatted responses. |
| `delete_aproject_template` | Deletes an existing project template using the Asana API and returns an empty data record. |
| `get_multiple_project_templates` | Retrieves a list of project templates, optionally filtered by workspace or team, with support for pagination and field selection. |
| `get_ateam_sproject_templates` | Retrieves a paginated list of project templates associated with a specific team, supporting optional filtering and field customization. |
| `instantiate_aproject_from_aproject_template` | Instantiates a project template using the Asana API, creating a new project based on the specified template and optionally including additional fields and formatting options. |
| `trigger_arule` | Triggers the execution of a specific rule using the API defined at the path "/rule_triggers/{rule_trigger_gid}/run" via a POST request. |
| `get_asection` | Retrieves information about a specific section using the "GET" method at the "/sections/{section_gid}" endpoint, optionally allowing customization with additional fields and pretty-printing. |
| `update_asection` | Updates or replaces a specific section resource identified by its GID, returning relevant status messages based on success or failure, with optional parameters for customizing output fields and formatting. |
| `delete_asection` | Deletes the specified section identified by its global ID and returns a success or error status. |
| `get_sections_in_aproject` | Retrieves a list of sections associated with a specific project, supporting optional query parameters for pagination and field customization. |
| `create_asection_in_aproject` | Creates a new section in a specified project using the Asana API and returns a status message. |
| `add_task_to_section` | Adds a task to the specified section using the POST method. |
| `move_or_insert_sections` | Inserts a new section into a specific project and returns the operation's status. |
| `get_astatus_update` | Retrieves a specific status update's details and associated metadata based on the provided status update identifier. |
| `delete_astatus_update` | Deletes a specific status update identified by its GID and returns a response based on the operation's success or failure. |
| `get_status_updates_from_an_object` | Retrieves status updates with filtering options for parent, creation date, and other parameters, returning paginated results. |
| `create_astatus_update` | Creates a status update with optional fields, pagination controls, and returns success or error responses based on provided parameters. |
| `get_astory` | Retrieves a specific story by its globally unique identifier (GID) with optional fields and formatting parameters. |
| `update_astory` | Updates or creates a story at the specified path "/stories/{story_gid}" using the provided data. |
| `delete_astory` | Deletes a specific story identified by its story GID from the collection of stories. |
| `get_stories_from_atask` | Retrieves the stories associated with a specific task using the task's unique identifier and supports optional query parameters for pagination and field selection. |
| `create_astory_on_atask` | Creates a story for a specific task using the "POST" method at the "/tasks/{task_gid}/stories" endpoint, allowing for optional fields and formatting through query parameters. |
| `get_multiple_tags` | Retrieves a list of tags using the "GET" method at the "/tags" endpoint, allowing customization with parameters for limit, offset, workspace, optional fields, and pretty formatting. |
| `create_atag` | Creates a new tag entry with optional fields and formatted response. |
| `get_atag` | Retrieves information about a specific tag, identified by its GID, using the "GET" method at the path "/tags/{tag_gid}" with optional formatting and field selection. |
| `update_atag` | Updates or replaces a Git tag with the specified GID and returns the operation status. |
| `delete_atag` | Deletes a specific tag from a repository using the API and returns relevant status messages, depending on the outcome of the deletion operation. |
| `get_atask_stags` | Retrieves the tags associated with a specific task using the task's unique identifier and supports optional filtering/pagination through query parameters. |
| `get_tags_in_aworkspace` | Retrieves a list of tags associated with a specific workspace, with options to limit the response size and customize the output fields. |
| `create_atag_in_aworkspace` | Adds tags to a specified workspace using a POST request to the "/workspaces/{workspace_gid}/tags" endpoint. |
| `get_multiple_tasks` | Retrieves a list of tasks based on specified query parameters such as assignee, project, and completion status, using the GET method at the "/tasks" endpoint. |
| `create_atask` | Creates a new task using the API and returns a status message, allowing optional fields and pretty-printing configurations through query parameters. |
| `get_atask` | Retrieves task details using the Asana API and returns information about the specified task, with optional fields and formatting available through query parameters. |
| `update_atask` | Updates an existing task specified by its ID using the PUT method, allowing for a complete replacement of the task resource. |
| `delete_atask` | Deletes the specified task identified by the task_gid and returns an appropriate HTTP status code. |
| `duplicate_atask` | Duplicates a task using the Asana API and returns a job ID, requiring a subsequent update call to modify the new task's properties. |
| `get_tasks_from_aproject` | Retrieves a list of tasks associated with a specific project, supporting optional filtering and pagination parameters. |
| `get_tasks_from_asection` | Retrieves a list of tasks within a specified section using the Asana API and returns the data based on optional query parameters such as fields, formatting, limit, offset, and completion status. |
| `get_tasks_from_atag` | Retrieves a list of tasks associated with a specific tag, allowing for optional filtering by fields, formatting, and pagination using query parameters. |
| `get_tasks_from_auser_task_list` | Retrieves a list of tasks associated with a specific user task list, allowing optional filtering by completion status, custom fields, and pagination limits. |
| `get_subtasks_from_atask` | Retrieves a list of subtasks for a specified task using the GET method, allowing optional parameters for customizing the response. |
| `create_asubtask` | Creates a new subtask for the specified parent task and returns the created subtask details. |
| `set_the_parent_of_atask` | Changes the parent task of a specified task by submitting a POST request to the "/tasks/{task_gid}/setParent" endpoint. |
| `get_dependencies_from_atask` | Retrieves a list of dependencies for a task with the specified task GID, allowing customization with optional fields, pretty formatting, and pagination limits. |
| `set_dependencies_for_atask` | Adds dependencies to a task using the task's GID and returns a status message, with optional pretty formatting. |
| `unlink_dependencies_from_atask` | Removes dependencies from a task using the "POST" method at the "/tasks/{task_gid}/removeDependencies" path. |
| `get_dependents_from_atask` | Retrieves a list of dependent tasks for a specified task using the GET method at "/tasks/{task_gid}/dependents," allowing for optional filtering with parameters such as `opt_fields`, `opt_pretty`, `limit`, and `offset`. |
| `set_dependents_for_atask` | Adds dependent tasks to a specified task using the POST method. |
| `unlink_dependents_from_atask` | Removes dependent tasks from the specified task using the POST method. |
| `add_aproject_to_atask` | Adds a project to a specific task using the "POST" method at the path "/tasks/{task_gid}/addProject". |
| `remove_aproject_from_atask` | Removes the specified project from a task while retaining the task in the system. |
| `add_atag_to_atask` | Adds a tag to a specified task in the system using the provided task identifier and returns a status message. |
| `remove_atag_from_atask` | Removes a tag from a task with the specified identifier using the "POST" method and returns a status message. |
| `add_followers_to_atask` | Adds followers to a specific task identified by its GID using the POST method, allowing optional fields and formatting for the response. |
| `remove_followers_from_atask` | Removes specified followers from a task using the POST method, returning the updated task record. |
| `get_atask_for_agiven_custom_id` | Retrieves a task by its custom ID from a specified workspace using the Asana API. |
| `search_tasks_in_aworkspace` | Searches for tasks within a specified workspace using various filters, such as text, assignees, projects, tags, and due dates, and returns a list of tasks matching these criteria. |
| `get_multiple_task_templates` | Retrieves a list of available task templates for standardized task creation, supporting optional filters like project, pagination (limit/offset), and field customization (opt_fields). |
| `get_atask_template` | Retrieves detailed information about a specific task template in Asana using the "GET" method at the "/task_templates/{task_template_gid}" path. |
| `delete_atask_template` | Deletes a specific task template by making a DELETE request to the API endpoint, returning an empty response upon success. |
| `instantiate_atask_from_atask_template` | Instantiates a task from a specified task template using the Asana API, allowing for the creation of standardized and repeatable workflows by leveraging pre-defined templates. |
| `create_ateam` | Creates a new team resource using the API at the "/teams" path with the "POST" method. |
| `get_ateam` | Retrieves details for a specific GitHub team by its global ID, supporting optional query parameters to customize the response format and included fields. |
| `update_ateam` | Updates the details of a team with the specified GID using the provided parameters, returning a status response based on the operation's success or failure. |
| `get_teams_in_aworkspace` | Retrieves a list of teams in a specified workspace using the GET method, allowing optional query parameters for customizing output fields, formatting, and pagination. |
| `get_teams_for_auser` | Retrieves a paginated list of teams associated with a specific user, optionally filtered by organization, using query parameters for customization. |
| `add_auser_to_ateam` | Adds a user to a team using the provided team ID, allowing for optional specification of additional fields and formatting preferences. |
| `remove_auser_from_ateam` | Removes a user from a specified team using a POST request and returns a success status upon completion. |
| `get_ateam_membership` | Retrieves a specific team membership using the "GET" method at "/team_memberships/{team_membership_gid}", allowing optional fields and formatting parameters to be specified. |
| `get_team_memberships` | Retrieves team membership information for a specified user within a team and workspace, allowing optional fields and pagination. |
| `get_memberships_from_ateam` | Retrieves team memberships for a specified team using the GitHub API, returning details about members based on optional fields and pagination parameters. |
| `get_memberships_from_auser` | Retrieves a paginated list of team memberships for a specified user, including optional filtering by workspace and customizable response fields. |
| `get_atime_period` | Retrieves details about a specific time period, identified by its GID, using the "GET" method at the "/time_periods/{time_period_gid}" path. |
| `get_time_periods` | Retrieves a list of time periods filtered by start and end dates, workspace, and other optional parameters. |
| `get_time_tracking_entries_for_atask` | Retrieves a list of time tracking entries for a specific task based on provided query parameters, such as limit, offset, and optional fields, returning the data in a formatted response. |
| `create_atime_tracking_entry` | Creates a new time tracking entry for a specified task using the POST method, allowing for optional fields and formatting through query parameters. |
| `get_atime_tracking_entry` | Retrieves a specific time tracking entry by its global ID, allowing optional field selection for the response. |
| `update_atime_tracking_entry` | Updates an existing time tracking entry by its GID and returns the modified entry. |
| `delete_atime_tracking_entry` | Deletes a specific time tracking entry identified by the `time_tracking_entry_gid` using the DELETE method and returns relevant status messages based on the success or failure of the operation. |
| `get_objects_via_typeahead` | Queries a workspace for typeahead results using the specified parameters and returns relevant objects or suggestions. |
| `get_multiple_users` | Retrieves a list of users with optional filtering parameters and pagination support. |
| `get_auser` | Retrieves details for a specific user using their unique identifier (user_gid) and offers optional query parameters for customizing the returned data fields (opt_fields) and response formatting (opt_pretty). |
| `get_auser_sfavorites` | Retrieves a list of favorites for a user with the specified `user_gid`, allowing optional filtering by resource type and workspace, and customizable output through additional query parameters. |
| `get_users_in_ateam` | Retrieves a paginated list of users associated with a specified team, supporting optional fields, pretty formatting, and offset parameters. |
| `get_users_in_aworkspace_or_organization` | Retrieves a list of users associated with the specified workspace, supporting optional fields, pagination, and response formatting. |
| `get_auser_task_list` | Retrieves details of a user task list by its global ID, supporting optional query parameters for field selection and response formatting. |
| `get_auser_stask_list` | Retrieves a list of tasks for a user identified by the user_gid parameter, allowing optional filtering by additional fields or workspace. |
| `get_multiple_webhooks` | Retrieves a list of webhooks, allowing for optional filtering by workspace, resource, and additional fields, with pagination options via limit and offset parameters. |
| `establish_awebhook` | Creates a new webhook subscription to receive event notifications and returns the subscription details. |
| `get_awebhook` | Retrieves information about a webhook with the specified ID using the "GET" method, allowing optional fields and pretty-print formatting. |
| `update_awebhook` | Updates a webhook identified by its GID at the "/webhooks/{webhook_gid}" path, allowing modifications to existing webhook configurations. |
| `delete_awebhook` | Deletes a webhook identified by the `{webhook_gid}` and returns a status message, allowing for the removal of existing webhook configurations. |
| `get_multiple_workspaces` | Retrieves a paginated list of workspaces with optional filtering and formatting parameters. |
| `get_aworkspace` | Retrieves a specific workspace by its GID using the Asana API, optionally including additional fields and formatting options. |
| `update_aworkspace` | Updates a specified workspace's properties and returns the modified workspace data. |
| `add_auser_to_aworkspace_or_organization` | Adds a user to a specified workspace and returns the full user record upon successful completion. |
| `remove_auser_from_aworkspace_or_organization` | Removes a user from a workspace using the specified POST API operation at the "/workspaces/{workspace_gid}/removeUser" path. |
| `get_aworkspace_membership` | Retrieves a specific workspace membership entry by its global identifier (GID) with optional field filtering and formatted output. |
| `get_workspace_memberships_for_auser` | Retrieves a list of workspace memberships for a specified user based on the provided query parameters, including optional fields, formatting preferences, and pagination settings. |
| `get_the_workspace_memberships_for_aworkspace` | Retrieves a list of workspace memberships for a specified workspace, providing details about users and their roles within the workspace, allowing for optional filtering and customization of the response. |
