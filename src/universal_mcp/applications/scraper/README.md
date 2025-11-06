# ScraperApp MCP Server

An MCP Server for the ScraperApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ScraperApp API.


| Tool | Description |
|------|-------------|
| `linkedin_list_profile_posts` | Fetches a paginated list of posts from a specific user or company profile using its provider ID. The `is_company` flag must specify the entity type. Unlike `linkedin_search_posts`, this function directly retrieves content from a known profile's feed instead of performing a global keyword search. |
| `linkedin_retrieve_profile` | Fetches a specific LinkedIn user's profile using their public or internal ID. Unlike `linkedin_search_people`, which discovers multiple users via keywords, this function targets and retrieves detailed data for a single, known individual based on a direct identifier. |
| `linkedin_list_post_comments` | Fetches a paginated list of comments for a specified LinkedIn post. It can retrieve either top-level comments or threaded replies if an optional `comment_id` is provided. This is a read-only operation, distinct from functions that search for posts or list user-specific content. |
| `linkedin_search_people` | Performs a paginated search for people on LinkedIn, distinct from searches for companies or jobs. It filters results using keywords, location, industry, and company, internally converting filter names like 'United States' into their required API IDs before making the request. |
| `linkedin_search_companies` | Executes a paginated LinkedIn search for companies, filtering by optional keywords, location, and industry. Unlike `linkedin_search_people` or `linkedin_search_jobs`, this function specifically sets the API search category to 'companies' to ensure that only company profiles are returned in the search results. |
| `linkedin_search_posts` | Performs a keyword-based search for LinkedIn posts, allowing results to be filtered by date and sorted by relevance. This function specifically queries the 'posts' category, distinguishing it from other search methods in the class that target people, companies, or jobs, and returns relevant content. |
| `linkedin_search_jobs` | Executes a LinkedIn search specifically for job listings using keywords and filters like region, industry, and minimum salary. Unlike other search functions targeting people or companies, this is specialized for job listings and converts friendly filter names (e.g., "United States") into their required API IDs. |
