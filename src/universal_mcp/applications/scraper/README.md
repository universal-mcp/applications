# ScraperApp MCP Server

An MCP Server for the ScraperApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ScraperApp API.


| Tool | Description |
|------|-------------|
| `linkedin_post_search` | Performs a general LinkedIn search for posts using keywords and filters like date and content type. It supports pagination and can utilize either the 'classic' or 'sales_navigator' API, searching broadly across the platform rather than fetching posts from a specific user's profile. |
| `linkedin_list_profile_posts` | Fetches a paginated list of all LinkedIn posts from a specific user or company profile using their unique identifier. This function retrieves content directly from a profile, unlike `linkedin_post_search` which finds posts across LinkedIn based on keywords and other filters. |
| `linkedin_retrieve_profile` | Retrieves a specific LinkedIn user's profile by their unique identifier, which can be an internal provider ID or a public username. This function simplifies data access by delegating the actual profile retrieval request to the integrated Unipile application, distinct from functions that list posts or comments. |
| `linkedin_list_post_comments` | Fetches comments for a specified LinkedIn post. If a `comment_id` is provided, it retrieves replies to that comment instead of top-level comments. This function supports pagination and specifically targets comments, unlike others in the class that search for or list entire posts. |
