# SemanticscholarApp MCP Server

An MCP Server for the SemanticscholarApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the SemanticscholarApp API.


| Tool | Description |
|------|-------------|
| `post_graph_get_authors` | Creates a batch of authors using the provided JSON data in the request body, optionally specifying fields to include in the response via a query parameter. |
| `get_graph_get_author_search` | Searches for authors based on a query string with optional pagination and field selection parameters. |
| `get_graph_get_author` | Retrieves the profile information for a specific author identified by the `author_id` and returns it with optional fields specified in the `fields` query parameter. |
| `get_graph_get_author_papers` | Retrieves a paginated list of papers authored by the specified author, with optional field selection. |
| `get_graph_get_paper_autocomplete` | Provides an autocomplete suggestion list based on a required query string parameter. |
| `post_graph_get_papers` | Creates a batch of papers using JSON data in the request body and optionally specifies fields to include in the response. |
| `get_graph_paper_relevance_search` | Searches for academic papers using the "GET" method at the "/paper/search" endpoint, allowing filtering by query, publication types, open access PDF availability, citation count, publication date or year, venue, fields of study, and pagination parameters. |
| `get_graph_paper_bulk_search` | Retrieves bulk search results of academic papers based on various query parameters such as keywords, fields of study, publication types, and sorting criteria. |
| `get_graph_paper_title_search` | Searches for matching papers based on specified query parameters, such as query string, fields, publication types, open access status, citation count, publication date, year, venue, and fields of study, using the "GET" method. |
| `get_graph_get_paper` | Retrieves details of a paper by its ID, optionally specifying fields to include in the response. |
| `get_graph_get_paper_authors` | Retrieves a list of authors for a specific paper identified by the `paper_id`, allowing optional parameters for offset, limit, and fields to customize the response. |
| `get_graph_get_paper_citations` | Retrieves a list of citations for a specific paper, identified by its paper ID, with optional parameters for offset, limit, and fields. |
| `get_graph_get_paper_references` | Retrieves references for a specific paper by its ID using the "GET" method and allows optional filtering by offset, limit, and fields for customizable output. |
| `get_snippet_search` | Retrieves a list of search results based on a specified query string, optionally limited by a user-defined number of results, using the "GET" method at the "/snippet/search" endpoint. |
