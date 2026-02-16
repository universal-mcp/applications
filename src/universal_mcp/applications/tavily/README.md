---
name: tavily
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# Tavily Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `search_and_summarize` | Queries the Tavily API to perform a web search. It returns a direct AI-generated answer if available; otherwise, it provides a formatted summary of the top three search results, including their titles and snippets. |
