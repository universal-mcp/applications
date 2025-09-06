# WrikeApp MCP Server

An MCP Server for the WrikeApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the WrikeApp API.


| Tool | Description |
|------|-------------|
| `get_contacts` | Retrieves contacts from the server with optional deleted status filtering, field selection, and metadata inclusion. |
| `get_contacts_by_contactid` | Retrieves contact information for a specific contact ID, optionally returning only specified fields. |
| `put_contacts_by_contactid` | Updates an existing contact using the specified contact ID with provided details including metadata, billing/cost rates, job role, and custom fields. |
| `get_users_by_userid` | Retrieves user information by ID from the API endpoint. |
| `put_users_by_userid` | Updates a user's profile information by user ID using a PUT request. |
| `get_groups` | Retrieves a list of groups from the API, applying optional filtering and pagination parameters. |
| `post_groups` | Creates a new group with the specified title and optional details via a POST request to the groups endpoint. |
| `get_groups_by_groupid` | Retrieves details for a specific group by its group ID, optionally returning only specified fields. |
| `put_groups_by_groupid` | Updates an existing group by groupId with new properties and membership changes via a PUT request. |
| `delete_groups_by_groupid` | Deletes a group resource identified by the provided groupId using an HTTP DELETE request. |
| `put_groups_bulk` | Updates multiple group memberships in bulk by sending a PUT request with the given member data. |
| `get_invitations` | Retrieves all invitations from the server using a GET request. |
| `post_invitations` | Sends an invitation email to a user with optional details such as name, role, and custom message. |
| `put_invitations_by_invitationid` | Updates an existing invitation by its unique ID with optional parameters, handling conditional updates and API communication. |
| `delete_invitations_by_invitationid` | Deletes a specific invitation using its unique identifier |
| `get_a_ccount` | Retrieves account information from the API, optionally including only specified fields. |
| `put_a_ccount` | Sends a PUT request to update or create an account with the provided metadata and returns the server response as a JSON object. |
| `get_workflows` | Retrieves all workflows from the server using a GET request. |
| `post_workflows` | Creates a new workflow by sending a POST request to the workflows endpoint with optional name and request body. |
| `put_workflows_by_workflowid` | Updates an existing workflow by workflow ID with optional name, hidden status, and request body data. |
| `get_customfields` | Retrieves all custom fields from the API and returns them as a parsed JSON object. |
| `post_customfields` | Creates a custom field by sending a POST request to the customfields endpoint with the specified parameters. |
| `get_customfields_by_customfieldid` | Retrieves details for a custom field by its unique identifier from the API |
| `put_customfields_by_customfieldid` | Updates a custom field specified by its ID with the provided parameters. |
| `delete_customfields_by_customfieldid` | Deletes a custom field resource identified by its custom field ID. |
| `get_folders` | Retrieves a list of folders from the API with support for filtering, pagination, and field selection. |
| `get_folders_by_folderid_folders` | Retrieves subfolders of a specified folder, applying optional filters and pagination parameters. |
| `post_folders_by_folderid_folders` | Creates a new subfolder within a specified folder by folder ID, with configurable attributes such as title, description, sharing, metadata, and permissions. |
| `delete_folders_by_folderid` | Deletes a folder resource identified by its folder ID via an HTTP DELETE request. |
| `put_folders_by_folderid` | Updates a folder's properties and relationships using a PUT request, allowing comprehensive modifications including metadata, access roles, and parent associations. |
| `get_tasks` | Retrieves tasks from the API with optional filtering, sorting, pagination, and field selection parameters. |
| `get_tasks_by_taskid` | Retrieves a task by its ID from the remote service, optionally returning only specified fields. |
| `put_tasks_by_taskid` | Updates a task's properties and relationships by ID, returning the updated task data. |
| `delete_tasks_by_taskid` | Deletes a task identified by the given task ID via an HTTP DELETE request and returns the response as a JSON object. |
| `post_folders_by_folderid_tasks` | Creates a new task in a specified folder with configurable attributes including title, description, assignments, and custom fields. |
