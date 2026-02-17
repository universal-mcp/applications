---
name: serpapi
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# Serpapi Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `web_search` | Performs a general web search via SerpApi, defaulting to the 'google_light' engine. It accepts custom parameters, retrieves organic results, and formats them into a string with titles, links, and snippets. It also handles API authentication and raises `NotAuthorizedError` for credential-related issues. |
| `google_maps_search` | Executes a Google Maps search via SerpApi using a query, coordinates, or place ID. It enhances the results by adding a `google_maps_url` to each location, distinguishing it from `get_google_maps_reviews` which retrieves reviews for a known place. |
| `get_google_maps_reviews` | Fetches Google Maps reviews for a specific location via SerpApi using its unique `data_id`. This function uses the `google_maps_reviews` engine, unlike `google_maps_search` which finds locations. Results can be returned in a specified language, defaulting to English. |
