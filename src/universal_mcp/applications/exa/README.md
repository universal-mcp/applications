# ExaApp MCP Server

An MCP Server for the ExaApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ExaApp API.


| Tool | Description |
|------|-------------|
| `search_with_filters` | Executes a query against the Exa API's `/search` endpoint, returning a list of results. This function supports extensive filtering by search type, category, domains, publication dates, and specific text content to refine the search query and tailor the API's response. |
| `find_similar_by_url` | Finds web pages semantically similar to a given URL. Unlike the `search` function, which uses a text query, this method takes a specific link and returns a list of related results, with options to filter by domain, publication date, and content. |
| `fetch_page_content` | Retrieves and processes content from a list of URLs, returning full text, summaries, or highlights. Unlike the search function which finds links, this function fetches the actual page content, with optional support for live crawling to get the most up-to-date information. |
| `answer` | Retrieves a direct, synthesized answer for a given query by calling the Exa `/answer` API endpoint. Unlike `search`, which returns web results, this function provides a conclusive response. It supports streaming, including source text, and selecting a search model. |
