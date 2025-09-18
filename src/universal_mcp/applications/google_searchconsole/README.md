# GoogleSearchconsoleApp MCP Server

An MCP Server for the GoogleSearchconsoleApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the GoogleSearchconsoleApp API.


| Tool | Description |
|------|-------------|
| `get_sitemap` | Retrieves detailed information for a single sitemap from a specified Google Search Console property. Unlike `list_sitemaps` which fetches all sitemaps, this function targets one sitemap by its URL (`feedpath`) to return its resource details, including status and last processed date. |
| `list_sitemaps` | Retrieves a list of sitemaps for a specific site property. It can optionally list sitemaps contained within a specified sitemap index file. This function contrasts with `get_sitemap`, which fetches details for only a single, specified sitemap rather than a collection. |
| `submit_sitemap` | Submits a sitemap to a specified Google Search Console property using its URL (feedpath). It notifies Google to crawl the sitemap's location, complementing other sitemap management functions (`list_sitemaps`, `delete_sitemap`) by adding or updating a sitemap's registration for a given site. |
| `delete_sitemap` | Deletes a specific sitemap from a Google Search Console property using its URL (`feedpath`). This function is distinct from `delete_site`, which removes the entire site property, not just a single sitemap file. It issues an HTTP DELETE request to the specified API endpoint. |
| `get_site` | Retrieves detailed information for a specific site property from Google Search Console using its URL. Unlike `list_sites`, which fetches all properties associated with the user's account, this function targets and returns the resource for a single, known site. |
| `list_sites` | Retrieves all websites and domain properties the authenticated user manages in Google Search Console. While `get_site` fetches a single, specific property, this function returns a comprehensive list of all sites linked to the user's account, providing a complete overview of managed properties. |
| `add_site` | Adds a site property to the user's Google Search Console account using its URL. This action requires subsequent ownership verification. Unlike `list_sites`, which only retrieves existing properties, this function creates a new entry and returns the corresponding site resource upon successful creation. |
| `delete_site` | Removes a website property from the user's Google Search Console account using its URL. Unlike `delete_sitemap`, which only targets a sitemap file, this function deletes the entire site property, revoking management access and removing it from the user's list of managed sites. |
| `inspect_url` | Retrieves the Google Index status for a specified URL within a given Search Console property. This function queries the URL Inspection API to return detailed information about how Google sees the page, including its indexing eligibility and any detected issues. |
| `query_search_analytics` | Queries and retrieves search traffic data for a specified site within a given date range. Supports advanced filtering, grouping by various dimensions (e.g., query, page, device), and aggregation to customize the analytics report from the Google Search Console API. |
