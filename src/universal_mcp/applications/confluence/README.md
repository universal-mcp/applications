# ConfluenceApp MCP Server

An MCP Server for the ConfluenceApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ConfluenceApp API.


| Tool | Description |
|------|-------------|
| `get_attachments` | Retrieves a list of attachments based on specified filters like sort order, cursor position, status, media type, filename, and limit, using the GET method. |
| `get_attachment_by_id` | Retrieves a specific attachment by ID with optional parameters to include labels, properties, operations, versions, collaborators, or specify a version. |
| `delete_attachment` | Deletes the specified attachment using its unique identifier and optionally purges it permanently. |
| `get_attachment_labels` | Retrieves labels associated with a specific attachment, optionally filtered by prefix, sorted, and paginated using cursor-based pagination. |
| `get_attachment_operations` | Retrieves operations associated with a specific attachment using its unique identifier. |
| `get_attachment_content_properties` | Retrieves properties of a specific attachment identified by `attachment-id`, with optional filtering, sorting, and pagination via query parameters. |
| `create_attachment_property` | Creates a new property for the specified attachment and returns the created property. |
| `get_attachment_content_properties_by_id` | Retrieves a specific property of an attachment using the provided attachment ID and property ID. |
| `update_attachment_property_by_id` | Updates a specific property for an attachment by its ID and returns the updated result. |
| `delete_attachment_property_by_id` | Deletes a specific property from an attachment using the DELETE method, identified by both the attachment ID and the property ID. |
| `get_attachment_versions` | Retrieves a list of versions for a specific attachment using the "id" parameter and supports query parameters for pagination and sorting. |
| `get_attachment_version_details` | Retrieves a specific version of an attachment file using the attachment ID and version number, returning the details of the specified version. |
| `get_attachment_comments` | Retrieves paginated footer comments for a specific attachment using query parameters for formatting, pagination, sorting, and version control. |
| `get_blog_posts` | Retrieves a list of blog posts using the "GET" method at the "/blogposts" endpoint, allowing filtering by parameters such as ID, space ID, sort order, status, title, and body format. |
| `create_blog_post` | Creates a new blog post using the POST method at the "/blogposts" endpoint, with an optional parameter to specify whether the post should be private. |
| `get_blog_post_by_id` | Retrieves a specific blog post by ID, allowing optional filtering by various parameters such as body format, draft status, and inclusion of additional metadata like labels, properties, and collaborators. |
| `update_blog_post` | Updates or creates a blog post with the specified ID and returns a status message. |
| `delete_blog_post` | Deletes a blog post with the specified ID using the DELETE method, with optional parameters to purge or manage draft status. |
| `get_blogpost_attachments` | Retrieves a list of attachments associated with a specific blog post, supporting filtering by status, media type, filename, and pagination via query parameters. |
| `get_custom_content_by_type_in_blog_post` | Retrieves custom content for a specific blog post using the "GET" method with options to filter by type, sort order, and other parameters. |
| `get_blog_post_labels` | Retrieves a list of labels associated with a specific blog post, filtered by prefix, sorted, and paginated based on provided query parameters. |
| `get_blog_post_like_count` | Retrieves the number of likes for a blog post using the specified ID via the GET method. |
| `get_blog_post_like_users` | Retrieves a paginated list of users who liked a specific blog post, using cursor-based pagination parameters. |
| `get_blogpost_content_properties` | Retrieves properties of a specific blog post identified by its ID, allowing optional filtering by key, sorting, and pagination using cursor and limit parameters. |
| `create_blogpost_property` | Adds custom properties to a specified blogpost and returns a success or error status. |
| `get_blogpost_content_properties_by_id` | Retrieves a specific property from a blog post using the provided blogpost and property IDs. |
| `update_blogpost_property_by_id` | Updates the specified property of a blog post using the provided identifiers and returns a status message. |
| `delete_blogpost_property_by_id` | Deletes a specific property from a blog post using the blog post ID and property ID. |
| `get_blog_post_operations` | Retrieves operations associated with a specific blog post identified by the provided ID using the GET method. |
| `get_blog_post_versions` | Retrieves a list of version history entries for a specific blog post, optionally paginated and sorted, with customizable response formatting. |
| `get_blog_post_version_details` | Retrieves a specific version of a blog post identified by its ID and version number using the GET method. |
| `convert_content_ids_to_content_types` | Converts content IDs to their corresponding types using a POST request and returns appropriate responses based on the conversion outcome. |
| `get_custom_content_by_type` | Retrieves custom content at the specified path "/custom-content" using the GET method, allowing for filtering by type, id, space-id, sort order, and pagination with optional cursor and limit parameters. |
| `create_custom_content` | Creates custom content via a POST request and returns appropriate status codes indicating success or specific errors. |
| `get_custom_content_by_id` | Retrieves custom content by a specified ID using the "GET" method, allowing optional formatting and inclusion of additional details such as labels, properties, operations, versions, and collaborators. |
| `update_custom_content` | Updates or replaces a custom content resource identified by the provided ID using the PUT method, returning various status responses based on the request's success or failure. |
| `delete_custom_content` | Deletes a custom content resource identified by its ID from the system, with an optional query parameter to specify whether to purge the content. |
| `get_custom_content_attachments` | Retrieves a list of attachments associated with custom content identified by the given ID, allowing for filtering by sort order, cursor, status, media type, filename, and limiting the number of results. |
| `get_custom_content_comments` | Retrieves a list of footer comments associated with a specific custom content item using the "GET" method, allowing for optional filtering by body format, cursor, limit, and sort order. |
| `get_custom_content_labels` | Retrieves labels for custom content with a specified ID, allowing filtering by prefix, sorting, and pagination using query parameters. |
| `get_custom_content_operations` | Retrieves operational details for a custom content item identified by its ID using the GET method. |
| `get_custom_content_content_properties` | Retrieves the properties associated with a specific custom content item by its ID, with optional filtering and pagination via query parameters. |
| `create_custom_content_property` | Adds or updates properties for a specified custom content item and returns the operation result. |
| `get_custom_content_content_properties_by_id` | Retrieves properties of a specific item identified by a custom content ID and property ID using the GET method. |
| `update_custom_content_property_by_id` | Updates a specific custom property of a custom content item in Confluence and returns the updated property. |
| `delete_custom_content_property_by_id` | Deletes a specified property from a custom content resource. |
| `get_labels` | Retrieves a list of labels using the "GET" method at the "/labels" endpoint, allowing filtering by label ID, prefix, sorting, and pagination via query parameters. |
| `get_label_attachments` | Retrieves a list of attachments associated with a label identified by the provided ID, allowing for sorting and pagination via query parameters. |
| `get_label_blog_posts` | Retrieves a list of blog posts associated with a specific label by ID, allowing optional filtering by space ID, body format, sorting, cursor pagination, and content limit, using the GET method. |
| `get_label_pages` | Retrieves a list of pages associated with a label identified by `{id}`, allowing filtering by space, body format, sorting, and pagination options. |
| `get_pages` | Retrieves a list of pages based on specified parameters such as ID, space ID, sort order, status, title, body format, cursor, and limit using the GET method at the "/pages" endpoint. |
| `create_page` | Creates a new page with optional query parameters to specify visibility (private/public), embedding, and root-level placement, returning appropriate status codes. |
| `get_page_by_id` | Retrieves a specific page by its ID, including optional details such as version history, labels, collaborators, and web resources based on query parameters. |
| `update_page` | Updates or creates a page resource at the specified ID and returns a status. |
| `delete_page` | Deletes a page specified by ID using the DELETE method, with optional purge and draft query parameters, returning a successful response if the operation is completed without providing content. |
| `get_page_attachments` | Retrieves a list of attachments for a page with the specified ID, allowing optional sorting, filtering, and pagination based on query parameters. |
| `get_custom_content_by_type_in_page` | Retrieves custom content for a page with the specified ID using the GET method, allowing filtering by type, sorting, pagination, and body format customization. |
| `get_page_labels` | Retrieves a list of labels for a page with the specified ID, optionally filtering by prefix, sorting, and paginating using cursor and limit parameters. |
| `get_page_like_count` | Retrieves the number of likes for a page identified by the given ID using the GET method. |
| `get_page_like_users` | Retrieves a list of users who have liked a page with the specified ID using the GET method, with optional parameters for pagination. |
| `get_page_operations` | Retrieves operations associated with a specific page based on the provided ID. |
| `get_page_content_properties` | Retrieves properties associated with a specific page using the Notion API and returns them based on query parameters like key, sort, cursor, and limit. |
| `create_page_property` | Updates properties for a page using the page ID provided in the path. |
| `get_page_content_properties_by_id` | Retrieves the properties of a specific page element using the page ID and property ID. |
| `update_page_property_by_id` | Updates a specific property for a given page using the provided path parameters and returns the operation status. |
| `delete_page_property_by_id` | Deletes a specific property from a specified page using the provided page-id and property-id as path parameters. |
| `get_page_versions` | Retrieves versions of a page identified by the specified ID, allowing optional filtering by body format, sorting, and pagination using cursor and limit parameters. |
| `create_whiteboard` | Creates a new whiteboard with optional privacy settings and returns the result. |
| `get_whiteboard_by_id` | Retrieves a specific whiteboard by ID, optionally including additional details such as collaborators, direct children, operations, and properties using query parameters. |
| `delete_whiteboard` | Deletes the specified whiteboard by its ID and moves it to the trash. |
| `get_whiteboard_content_properties` | Retrieves properties for a whiteboard with the specified ID, optionally filtering by key, sorting, and paginating results using a cursor and limit parameters. |
| `create_whiteboard_property` | Updates the properties of a specific whiteboard using the API at path "/whiteboards/{id}/properties" via the POST method. |
| `get_whiteboard_content_properties_by_id` | Retrieves a specific property from a designated whiteboard using the provided whiteboard and property identifiers. |
| `update_whiteboard_property_by_id` | Updates a specific property of a whiteboard using the "PUT" method, specifying the whiteboard and property IDs in the path. |
| `delete_whiteboard_property_by_id` | Deletes a specific property from a whiteboard by ID using the DELETE method. |
| `get_whiteboard_operations` | Retrieves a list of operations for a specific whiteboard identified by its ID using the GET method. |
| `get_whiteboard_ancestors` | Retrieves all ancestors for a specified whiteboard in top-to-bottom order, limited by the `limit` parameter, with minimal details returned for each ancestor. |
| `create_database` | Creates a new database (optionally with private access restrictions) and returns the operation result. |
| `get_database_by_id` | Retrieves a database by its ID and optionally includes additional details such as collaborators, direct children, operations, or properties using the specified query parameters. |
| `delete_database` | Deletes a database identified by its ID using the DELETE method, returning a success status of 204 if successful, or error statuses for unauthorized access, invalid requests, or if the database is not found. |
| `get_database_content_properties` | Retrieves the properties (columns) of a Notion database identified by its ID, supporting pagination and sorting via query parameters. |
| `create_database_property` | Creates a new property in a database using the specified database ID and returns the result. |
| `get_database_content_properties_by_id` | Retrieves specific property details from a designated database using the provided database and property identifiers. |
| `update_database_property_by_id` | Updates a specific property in a database by providing the database ID and property ID, using the PUT method to modify its schema or settings. |
| `delete_database_property_by_id` | Removes a specified property from a database and returns a confirmation response upon success. |
| `get_database_operations` | Retrieves and performs operations on a specific database by its identifier. |
| `get_database_ancestors` | Retrieves a list of ancestors for a database specified by its ID, returning them in top-to-bottom order, with optional filtering by a limit parameter. |
| `create_smart_link` | Creates or processes embedded content via the API and returns a status or the created resource. |
| `get_smart_link_by_id` | Retrieves an embed with the specified ID and optionally includes collaborators, direct children, operations, and properties based on query parameters. |
| `delete_smart_link` | Deletes an embed resource by ID and returns a success status upon removal. |
| `get_smart_link_content_properties` | Retrieves properties for an embed with the specified ID, allowing optional filtering by key, sorting, and pagination using query parameters. |
| `create_smart_link_property` | Creates or updates properties for a specific embed using the embed ID and returns the operation status. |
| `get_smart_link_content_properties_by_id` | Retrieves the properties of a specific embed using its embed ID and property ID. |
| `update_smart_link_property_by_id` | Updates a specific property of an embed using the provided embed ID and property ID. |
| `delete_smart_link_property_by_id` | Deletes a specific property from an embed identified by embed-id and property-id. |
| `get_smart_link_operations` | Retrieves the operations associated with a specific embed identified by {id}. |
| `get_smart_link_ancestors` | Retrieves a list of ancestors associated with a specified embed ID using a path parameter and an optional query limit. |
| `create_folder` | Creates a new folder within a specified parent folder using the POST method and returns details of the newly created folder. |
| `get_folder_by_id` | Retrieves a specific folder's details including its collaborators, direct children, operations, and properties based on the provided ID. |
| `delete_folder` | Deletes a folder by its ID using the DELETE method, returning a 204 status code upon successful removal. |
| `get_folder_content_properties` | Retrieves properties for a folder identified by the provided ID, allowing filtering by key and optional sorting, pagination, and limiting of results. |
| `create_folder_property` | Creates and updates properties for a specific folder identified by `{id}` using the "POST" method. |
| `get_folder_content_properties_by_id` | Retrieves a specific property associated with a folder using the folder ID and property ID. |
| `update_folder_property_by_id` | Updates a specific property of a folder by ID using the specified property identifier. |
| `delete_folder_property_by_id` | Deletes a specific property from a folder using the "DELETE" method by providing the folder ID and property ID in the request path. |
| `get_folder_operations` | Retrieves a list of available operations for a specific folder identified by its ID using the GET method. |
| `get_folder_ancestors` | Retrieves a flat list of a folder's ancestors starting from its parent up to the root folder. |
| `get_page_version_details` | Retrieves a specific version of a page using the provided page ID and version number. |
| `get_custom_content_versions` | Retrieves a paginated list of versions for a specific custom content item, supporting filtering, sorting, and format customization. |
| `get_custom_content_version_details` | Retrieves a specific version of custom content by its ID and version number using the "GET" method. |
| `get_spaces` | Retrieves a list of spaces filtered by criteria such as IDs, keys, type, status, labels, favorited status, and pagination parameters. |
| `create_space` | Creates a new space resource and returns a success response upon creation. |
| `get_space_by_id` | Retrieves a space's details by its ID, optionally including descriptions, icons, operations, properties, permissions, role assignments, and labels based on query parameters. |
| `get_blog_posts_in_space` | Retrieves a list of blog posts associated with a specific space, allowing filtering by status, title, and sorting options. |
| `get_space_labels` | Retrieves a list of labels for a specific space identified by its ID, allowing optional filtering by prefix, sorting, and pagination using query parameters. |
| `get_space_content_labels` | Retrieves a list of content labels for a specific space using the provided ID, with optional filtering by prefix, sorting, and pagination. |
| `get_custom_content_by_type_in_space` | Retrieves custom content for a specific space, allowing users to filter by type, cursor, and limit, with options for different body formats. |
| `get_space_operations` | Retrieves a list of operations for a specific space identified by the given ID using the provided API endpoint. |
| `get_pages_in_space` | Retrieves a list of pages for a specified space, allowing filtering by depth, sort order, status, title, body format, and pagination controls. |
| `get_space_properties` | Retrieves a list of properties for a specified space, optionally filtered by key, with pagination support via cursor and limit parameters. |
| `create_space_property` | Creates a new property for a specified space using the "POST" method, where the space is identified by the `{space-id}` path parameter. |
| `get_space_property_by_id` | Retrieves the specified property details for a space using the provided space and property identifiers. |
| `update_space_property_by_id` | Updates the specified property within a designated space and returns a success status upon completion. |
| `delete_space_property_by_id` | Deletes a property from a specified space using the provided space ID and property ID. |
| `get_space_permissions_assignments` | Retrieves the list of permissions assigned to a specific space, supporting pagination via cursor and limit parameters. |
| `get_available_space_permissions` | Retrieves space permissions with pagination support using cursor and limit parameters. |
| `get_available_space_roles` | Retrieves a list of space roles, filtered by space ID, role type, principal ID, and principal type, with options for pagination using a cursor and limit, returning relevant space role information. |
| `get_space_roles_by_id` | Retrieves space role assignments for a specified space ID, returning role-based permissions and user access details. |
| `get_space_role_assignments` | Retrieves role assignments for a specific space with optional filtering by role type, role ID, principal type, principal ID, and pagination controls. |
| `set_space_role_assignments` | Assigns a role to a specific space identified by the path parameter ID and returns the assignment status. |
| `get_page_footer_comments` | Retrieves comments from the footer section of a specific page identified by its ID, allowing for optional filtering by body format, status, sorting, cursor, and limit. |
| `get_page_inline_comments` | Retrieves a list of inline comments for a specific page, allowing customization by body format, status, resolution status, sorting, cursor, and limit, using the API at "/pages/{id}/inline-comments" via the GET method. |
| `get_blog_post_footer_comments` | Retrieves comments from the footer section of a specific blog post using the "GET" method, allowing for customizable output format and sorting options based on query parameters. |
| `get_blog_post_inline_comments` | Retrieves a list of inline comments associated with a specific blog post using the provided parameters for filtering and sorting. |
| `get_footer_comments` | Retrieves a list of comments for the footer, allowing customization through query parameters for body format, sorting, pagination with a cursor, and limiting the number of results. |
| `create_footer_comment` | Creates a new footer comment entry and returns a success status upon creation. |
| `get_footer_comment_by_id` | Retrieves information about a specific footer comment using the comment ID, with optional configurations for formatting and included metadata. |
| `update_footer_comment` | Updates a Confluence footer comment's content and returns a success response. |
| `delete_footer_comment` | Deletes a specific footer comment identified by its ID using the DELETE method, returning a 204 status code upon successful deletion. |
| `get_footer_comment_children` | Retrieves child comments for a specific footer comment with optional filtering, sorting, and pagination parameters. |
| `get_footer_like_count` | Retrieves the count of likes for a specific footer comment using the "GET" method at the "/footer-comments/{id}/likes/count" endpoint. |
| `get_footer_like_users` | Retrieves a list of users who have liked a specific comment with the given ID using the GET method, allowing for pagination through cursor and limit parameters. |
| `get_footer_comment_operations` | Retrieves the operations for a specific footer comment identified by the provided ID using the GET method. |
| `get_footer_comment_versions` | Retrieves and lists versions of a specific comment identified by `{id}` in the footer, allowing customization through query parameters such as format, sorting, and pagination. |
| `get_footer_comment_version_details` | Retrieves a specific version of a footer comment by its ID and version number. |
| `get_inline_comments` | Retrieves a paginated list of inline comments with optional parameters for body formatting, sorting, pagination (cursor), and result limit. |
| `create_inline_comment` | Creates inline comments on a specified line of a pull request file using the GitHub API and returns the created comment. |
| `get_inline_comment_by_id` | Retrieves the specified inline comment by ID, optionally including formatted content and associated metadata. |
| `update_inline_comment` | Updates an inline comment's content in a version control system using the specified comment identifier. |
| `delete_inline_comment` | Deletes an inline comment specified by its ID using the DELETE method and returns a successful status upon completion. |
| `get_inline_comment_children` | Retrieves a paginated list of child comments for a specific inline comment, supporting query parameters for formatting, sorting, and pagination. |
| `get_inline_like_count` | Retrieves the total number of likes for a specific inline comment using the API endpoint "/inline-comments/{id}/likes/count" via the GET method. |
| `get_inline_like_users` | Retrieves a list of users who have liked an inline comment with the specified ID, with optional pagination using cursor and limit parameters. |
| `get_inline_comment_operations` | Retrieves an inline comment by ID from a GitHub repository using the GitHub API. |
| `get_inline_comment_versions` | Retrieves version history for a specific inline comment, supporting pagination and body formatting options. |
| `get_inline_comment_version_details` | Retrieves a specific version of an inline comment by its ID and version number using the GET method. |
| `get_comment_content_properties` | Retrieves specific properties of a comment using its ID, optionally filtered by key, sorted, and paginated. |
| `create_comment_property` | Updates properties of a comment identified by the given "comment-id" using the specified API. |
| `get_comment_content_properties_by_id` | Retrieves the specified property of a comment using the provided comment ID and property ID. |
| `update_comment_property_by_id` | Updates the specified property of a comment using the provided path parameters and returns a status message. |
| `delete_comment_property_by_id` | Deletes a specific property from a comment using the provided `comment-id` and `property-id`, returning a status code upon successful deletion. |
| `get_tasks` | Retrieves a filtered list of tasks from a specified space, page, or blog post, allowing filtering by status, assignment, creation/due dates, and other criteria. |
| `get_task_by_id` | Retrieves a specific task by ID and optionally formats the response body based on the body-format query parameter. |
| `get_child_pages` | Retrieves a list of child pages for a given page, identified by the `{id}`, allowing optional filtering by cursor, limit, and sort order. |
| `get_child_custom_content` | Retrieves a list of child content items for a specified custom content item identified by `{id}`, allowing optional filtering by `cursor`, `limit`, and `sort` parameters. |
| `get_page_ancestors` | Retrieves the hierarchical ancestors of a specified Confluence page in top-to-bottom order, returning minimal page details with optional limit control. |
| `create_bulk_user_lookup` | Creates a bulk operation on user data using the POST method at the "/users-bulk" endpoint. |
| `check_access_by_email` | Checks user access by email using a POST request to the "/user/access/check-access-by-email" endpoint, returning relevant access information. |
| `invite_by_email` | Sends an email invitation to grant user access and returns a success or error status. |
| `get_data_policy_metadata` | Retrieves data policy metadata from a workspace using the Confluence Cloud REST API. |
| `get_data_policy_spaces` | Retrieves information about data policies affecting spaces, returning details on whether content is blocked for each space specified by query parameters like `ids`, `keys`, `sort`, `cursor`, and `limit`. |
| `get_classification_levels` | Retrieves a list of classification levels using the "GET" method at the "/classification-levels" path. |
| `get_space_default_classification_level` | Retrieves the default classification level for a specified space using its unique identifier. |
| `put_space_default_classification_level` | Updates the default classification level for a space with the specified ID using the "PUT" method via the API endpoint "/spaces/{id}/classification-level/default." |
| `delete_space_default_classification_level` | Removes the default classification level from a specified space identified by its ID. |
| `get_page_classification_level` | Retrieves the classification level for a specified page using the `GET` method, accepting a page ID and an optional status query parameter. |
| `put_page_classification_level` | Updates the classification level of a page with the specified ID using the PUT method. |
| `post_page_classification_level` | Resets the classification level for a specific page to the default, removing any custom classification settings. |
| `get_blog_post_classification_level` | Retrieves the classification level for a specific blog post identified by its ID using the GET method at the "/blogposts/{id}/classification-level" endpoint, allowing for optional filtering by status. |
| `put_blog_post_classification_level` | Updates the classification level of the blog post with the specified ID and returns a success status upon completion. |
| `post_blog_post_classification_level` | Resets the classification level for a specific blog post to the space's default level using the Confluence REST API. |
| `get_whiteboard_classification_level` | Retrieves the classification level of a specific whiteboard identified by its ID, returning relevant information if the request is successful. |
| `put_whiteboard_classification_level` | Updates the classification level for a specific whiteboard identified by its ID using the Confluence Cloud REST API. |
| `post_whiteboard_classification_level` | Resets the classification level for a specific whiteboard to the default space classification level using the Confluence Cloud REST API. |
| `get_database_classification_level` | Retrieves the classification level of a specific database by its unique identifier. |
| `put_database_classification_level` | Updates the classification level of a database identified by `{id}` using the PUT method. |
| `post_database_classification_level` | Resets the classification level for a specified database using a POST request and returns an empty response on success. |
