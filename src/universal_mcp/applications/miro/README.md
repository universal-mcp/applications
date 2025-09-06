# MiroApp MCP Server

An MCP Server for the MiroApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the MiroApp API.


| Tool | Description |
|------|-------------|
| `revoke_token_v1` | Revokes an OAuth access token using the POST method at "/v1/oauth/revoke", allowing clients to invalidate tokens as needed. |
| `get_access_token_information` | Retrieves an OAuth 2.0 token using the GET method for client authorization purposes. |
| `get_audit_logs` | Retrieves audit logs with optional filtering by time range, pagination, and sorting parameters. |
| `get_organization_settings` | Retrieves data classification settings for an organization, providing information on how data is categorized and handled within the specified organization. |
| `bulk_update_boards_classification` | Updates the data classification settings for a specific team in an organization using the "PATCH" method. |
| `get_team_settings` | Retrieves the data classification settings for a specific team within an organization. |
| `update_team_settings` | Updates data classification settings for a specific team within an organization using the PATCH method. |
| `get_board_classification` | Retrieves data classification details for a specified organization, team, and board using the provided identifiers. |
| `update_board_classification` | Assigns data classifications to a board within a specified organization and team using the provided criteria and returns a success status upon completion. |
| `get_all_cases` | Retrieves a list of cases for a specified organization using the "GET" method, allowing optional query parameters for pagination via "limit" and "cursor". |
| `get_case` | Retrieves a specific case for an organization with the provided org_id and case_id. |
| `get_all_legal_holds_within_acase` | Retrieves a paginated list of legal holds for a specific case and organization using cursor-based pagination. |
| `get_legal_hold_information` | Retrieves a specific legal hold for a case within an organization using the provided identifiers. |
| `get_content_items_under_legal_hold` | Retrieves a list of content items under a specific legal hold in a case for an organization, allowing for pagination using limit and cursor parameters. |
| `create_board_export_job` | Exports board data for a specified organization using the "POST" method and returns a job status. |
| `get_board_export_job_status` | Retrieves the status and details of a specified board export job for an organization using the API. |
| `get_results_for_board_export_job` | Retrieves the export results for a specific organization's board export job using the API. |
| `retrieve_content_change_logs_of_board_items` | Retrieves organization content logs with filtering options such as board IDs, email addresses, date ranges, and pagination parameters. |
| `reset_all_sessions_of_auser` | Resets all active sessions for a specified user (identified by email), requiring reauthentication. |
| `get_organization_info` | Retrieves information about an organization specified by its ID using the API endpoint "/v2/orgs/{org_id}" with the GET method. |
| `get_organization_members` | Retrieves a list of members from an organization specified by `{org_id}` using query parameters for filtering by email, role, license status, and member activity, with pagination options. |
| `get_organization_member` | Retrieves a specific member's details within an organization using their unique identifiers. |
| `get_boards` | Retrieves a list of boards filtered by team, project, search query, owner, and pagination parameters. |
| `copy_board` | Updates a board's configuration (with optional source copying) and returns the updated board details. |
| `create_board` | Creates a new board resource and returns a success status upon completion. |
| `get_specific_board` | Retrieves information about a specific board identified by its ID using the API endpoint "/v2/boards/{board_id}" with the GET method. |
| `delete_board` | Deletes a specific board identified by its ID using the "DELETE" method, effectively removing it from the system and returning a success status when completed. |
| `update_board` | Updates a Trello board identified by `{board_id}` using the Trello API and returns a status message. |
| `create_app_card_item` | Creates a new app card on a specified board using the "POST" method, identified by the path "/v2/boards/{board_id}/app_cards". |
| `get_app_card_item` | Retrieves the details of an app card with the specified item ID from a board using the GET method. |
| `delete_app_card_item` | Deletes an app card item from the specified board using the DELETE method and returns a success status upon completion. |
| `update_app_card_item` | Updates a specific app card on the specified board using partial modifications via the PATCH method. |
| `create_card_item` | Creates a new card on the specified board using the provided data and returns the operation status upon success. |
| `get_card_item` | Retrieves a specific card from a board using its board ID and item ID, returning relevant details in the response. |
| `delete_card_item` | Deletes a specific card item from a board by ID and returns a success status upon removal. |
| `update_card_item` | Updates specified fields of a card item on a board using partial modifications. |
| `get_connectors` | Retrieves a list of connectors associated with a specific board, allowing optional filtering by limit and cursor parameters. |
| `create_connector` | Establishes a connection to a specific board by creating a new connector using the API at the path "/v2/boards/{board_id}/connectors" with the POST method. |
| `get_specific_connector` | Retrieves a specific connector from a board using the provided board and connector identifiers. |
| `delete_connector` | Deletes a specific connector associated with a board, identified by the provided `board_id` and `connector_id`, removing it along with any related configurations. |
| `update_connector` | Updates a connector on a specific board using the PATCH method, returning a status message upon successful modification. |
| `create_document_item_using_url` | Adds a document to a specified board using the POST method and returns a status message. |
| `get_document_item` | Retrieves a specific document from a board using the provided board ID and item ID. |
| `delete_document_item` | Deletes a specified document from a board using its unique identifier and returns a success status upon completion. |
| `update_document_item_using_url` | Updates a specific document within a board using partial modifications and returns a success status. |
| `create_embed_item` | Creates an embed associated with a specific board, returning the result upon successful creation. |
| `get_embed_item` | Retrieves an embedded item from a specified board using the provided board and item identifiers. |
| `delete_embed_item` | Deletes the specified embed item from the board by its ID and returns a success status upon removal. |
| `update_embed_item` | Updates an embedded item within a specified board and returns the updated result. |
| `create_image_item_using_url` | Uploads an image to a specified board and returns success status upon completion. |
| `get_image_item` | Retrieves a specific image item from a designated board using the provided identifiers. |
| `delete_image_item` | Deletes a specific image from a specified board. |
| `update_image_item_using_url` | Updates a specific image in a board using the PATCH method, applying partial modifications to the image's properties. |
| `get_items_on_board` | Retrieves a paginated list of items from a specified board using query parameters for limit, type, and cursor-based pagination. |
| `get_specific_item_on_board` | Retrieves details of a specific item from a board using the GET method and returns the data in response. |
| `delete_item` | Deletes a specific item from a board by its ID and returns a success status. |
| `update_item_position_or_parent` | Partially updates an existing item on a board using the PATCH method, allowing for specific modifications to resource properties. |
| `get_items_within_frame` | Retrieves a paginated list of items from a specified board, filtered by parent item ID and type, using cursor-based pagination. |
| `get_specific_item_on_board1` | Retrieves a specific item from a board using the specified identifiers. |
| `delete_item1` | Deletes a specific item from a Miro board using the "DELETE" method. |
| `get_all_board_members` | Retrieves a paginated list of board members using query parameters for limit and offset, returning a 200 status on success. |
| `share_board` | Adds a new member to a board using the API at path "/v2/boards/{board_id}/members" and returns a successful status message upon completion. |
| `get_specific_board_member` | Retrieves information about a specific board member using the "GET" method, providing details associated with the member identified by `{board_member_id}` within the board identified by `{board_id}`. |
| `remove_board_member` | Removes a user from a board using the Miro API and returns a successful response upon completion. |
| `update_board_member` | Updates a board member's details for the specified board using the PATCH method. |
| `create_shape_item` | Creates a new shape on a specified board using the provided data. |
| `get_shape_item` | Retrieves a specific shape from the specified board. |
| `delete_shape_item` | Deletes a specified shape from a board using the provided board and item identifiers. |
| `update_shape_item` | Updates a specific shape on a board by its ID and returns a success status. |
| `create_sticky_note_item` | Creates a new sticky note on a specific board using the "POST" method and returns a successful status message when the operation is completed. |
| `get_sticky_note_item` | Retrieves a specific sticky note from a board using the provided board and item IDs. |
| `delete_sticky_note_item` | Deletes a specific sticky note from a board using the DELETE method, returning a successful status message. |
| `update_sticky_note_item` | Updates a sticky note on the specified board using partial modifications and returns a success status. |
| `create_text_item` | Creates a new text entry on a specified board and returns a success status. |
| `get_text_item` | Retrieves a specific text item from a board using the provided board and item identifiers. |
| `delete_text_item` | Deletes a specific text item from a board using the provided board and item identifiers. |
| `update_text_item` | Updates a specific text item on a board using the PATCH method, allowing partial modifications of the item's properties. |
| `create_items_in_bulk` | Bulk updates or creates items on a specified board using the API endpoint "/v2/boards/{board_id}/items/bulk" via the POST method. |
| `create_frame` | Creates a new frame in the specified board using the API and returns a successful response. |
| `get_frame` | Retrieves the details of a specific frame within a board using the "GET" method. |
| `delete_frame` | Deletes a frame with the specified item ID from a board with the given board ID. |
| `update_frame` | Updates specific frame properties for a board using partial modifications and returns a success status. |
| `get_app_metrics` | Retrieves application metrics for a specified time period using the `startDate`, `endDate`, and `period` query parameters. |
| `get_total_app_metrics` | Retrieves total metrics for a specified application by its ID. |
| `create_webhook_subscription` | Creates a board subscription webhook and returns a success status upon configuration. |
| `update_webhook_subscription` | Updates a webhook subscription for a board using the GitHub API and returns a success status. |
| `get_webhook_subscriptions` | Retrieves a paginated list of webhook subscriptions using cursor-based pagination. |
| `get_specific_webhook_subscription` | Retrieves details about a specific webhook subscription identified by the provided subscription ID using the GET method. |
| `delete_webhook_subscription` | Deletes a webhook subscription by a specified `subscription_id`, stopping the delivery of notifications associated with that subscription. |
| `get_specific_mind_map_node` | Retrieves a specific mind map node by ID from a specified board using the GET method. |
| `delete_mind_map_node` | Deletes a specified mindmap node from a board using the experimental v2 API. |
| `get_mind_map_nodes` | Retrieves a paginated list of mindmap nodes from a specified Miro board, supporting limit and cursor parameters for result pagination. |
| `create_mind_map_node` | Creates a new mind map node in a specified Miro board using the POST method and returns a response upon successful creation. |
| `get_items_on_board1` | Retrieves a paginated list of items from a specified board, filtered by type and limited by cursor-based pagination. |
| `create_shape_item1` | Creates a new shape on a board with the specified `board_id` using the API. |
| `get_shape_item1` | Retrieves shape details from a specific item within a board, identified by the board ID and item ID. |
| `delete_shape_item1` | Deletes a specific shape from the specified board. |
| `update_shape_item1` | Updates a specific shape on a board and returns a status message. |
| `get_all_groups_on_aboard` | Retrieves a list of groups associated with a specified board, allowing for pagination with optional limit and cursor parameters. |
| `create_group` | Creates a new group in the specified board using the provided board ID and returns a success status. |
| `get_items_of_agroup_by_id` | Retrieves a paginated list of group items for a specific board, optionally filtered by group item ID, with cursor-based pagination support. |
| `get_agroup_by_its_id` | Retrieves a group associated with a specific board from the API. |
| `updates_agroup_with_new_items` | Updates a group on a specific board using the provided group ID and board ID. |
| `ungroup_items` | Deletes a group from a specified board using the DELETE method, optionally allowing for the deletion of associated items. |
| `deletes_the_group` | Deletes a group from a specified board, with an option to delete associated items, and returns a success status. |
| `revoke_token_v2` | Revokes an OAuth 2.0 access or refresh token at the authorization server's revocation endpoint and returns a successful status upon invalidation. |
| `get_tags_from_item` | Retrieves tags associated with a specific item on a board using the API. |
| `get_tags_from_board` | Retrieves a list of tags associated with a specific board, allowing for pagination control via limit and offset parameters. |
| `create_tag` | Creates and adds new tags to a specific board using the provided board ID. |
| `get_tag` | Retrieves information about a specific tag associated with a board, identified by the board ID and tag ID, using the GET method. |
| `delete_tag` | Deletes a tag from a specific board using the API and returns a successful status message. |
| `update_tag` | Updates a tag associated with a specific board by modifying its details using the specified `board_id` and `tag_id`. |
| `get_items_by_tag` | Retrieves paginated items from a specific board's platform tags, optionally filtered by tag ID. |
| `attach_tag_to_item` | Adds an item to a board with specific platform tags using the POST method, optionally specifying a tag ID in the query parameters. |
| `remove_tag_from_item` | Deletes a specific item from a board's PlatformTags collection, requiring a tag_id parameter for identification. |
| `list_of_projects` | Retrieves a list of projects for a specified team within an organization, allowing pagination via limit and cursor parameters. |
| `create_project` | Assigns a project to a team within an organization using a POST request and returns a success status upon completion. |
| `get_project` | Retrieves project details for a specific team within an organization. |
| `delete_project` | Deletes a specific organization's team project and returns a success message upon removal. |
| `update_project` | Updates project details within the specified team and organization using the PATCH method and returns a successful response upon completion. |
| `get_project_settings` | Retrieves the settings for a specified organization's team project. |
| `update_project_settings` | Updates organization, team, and project settings for the specified project. |
| `list_of_project_members` | Retrieves a list of members in a specific project within a team for an organization using the provided limit and cursor query parameters. |
| `add_member_in_aproject` | Adds a member to a specified project within a team and organization. |
| `get_project_member` | Retrieves a specific member's details from a project team within an organization. |
| `remove_project_member` | Deletes a member from a specific project within a team in an organization using the provided member ID. |
| `update_project_member` | Updates team member information in an organization project using the "PATCH" method and returns a successful status response. |
| `list_teams` | Retrieves a paginated list of teams for a specified organization with optional filtering by name. |
| `create_team` | Creates a new team within the specified organization using the POST method. |
| `get_team` | Retrieves team details for the specified organization and team ID. |
| `delete_team` | Deletes a team within an organization using the specified organization and team IDs. |
| `update_team` | Updates specific properties of a team within an organization using partial modifications. |
| `list_team_members` | Retrieves a paginated list of members for a specified team within an organization, optionally filtered by role. |
| `invite_team_members` | Adds a member to a specific team within an organization using the API endpoint at "/v2/orgs/{org_id}/teams/{team_id}/members". |
| `get_team_member` | Retrieves information about a specific team member using the provided organization, team, and member identifiers. |
| `delete_team_member_from_team` | Removes a member from a specified team in an organization using the GitHub API. |
| `update_team_member` | Updates the membership details of a team member in an organization using the GitHub API. |
| `get_default_team_settings` | Retrieves the default team settings for an organization via the GitHub API. |
| `get_team_settings1` | Retrieves team settings for a specified team within an organization using the "GET" method. |
| `update_team_settings1` | Updates settings for a team within an organization using the GitHub API and returns a status message. |
