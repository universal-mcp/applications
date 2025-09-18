# SerpapiApp MCP Server

An MCP Server for the SerpapiApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the SerpapiApp API.


| Tool | Description |
|------|-------------|
| `web_search` | Performs a general web search via SerpApi, defaulting to the 'google_light' engine. It accepts custom parameters, retrieves organic results, and formats them into a string with titles, links, and snippets. It also handles API authentication and raises `NotAuthorizedError` for credential-related issues. |
| `google_maps_search` | Executes a Google Maps search via SerpApi using a query, coordinates, or place ID. It enhances the results by adding a `google_maps_url` to each location, distinguishing it from `get_google_maps_reviews` which retrieves reviews for a known place. |
| `get_google_maps_reviews` | Fetches Google Maps reviews for a specific location via SerpApi using its unique `data_id`. This function uses the `google_maps_reviews` engine, unlike `google_maps_search` which finds locations. Results can be returned in a specified language, defaulting to English. |
