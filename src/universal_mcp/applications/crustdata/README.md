---
name: crustdata
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# Crustdata Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `screen_companies` | Screens companies based on specified metrics, filters, sorting, and pagination parameters, and returns the result as a JSON-compatible dictionary. |
| `get_headcount_timeseries` | Retrieve headcount timeseries data from the data lab endpoint using the provided filters, pagination, and sorting options. |
| `get_headcount_by_facet_timeseries` | Retrieves headcount timeseries data aggregated by specified facets using provided filters and sorting options. |
| `get_funding_milestone_timeseries` | Retrieves a time series of funding milestone data based on specified filters, pagination, and sorting options. |
| `get_decision_makers` | Retrieves decision makers based on specified filters and parameters. |
| `get_web_traffic` | Retrieves web traffic data based on provided filters, pagination, and sorting criteria. |
| `get_investor_portfolio` | Retrieves the investment portfolio information for a specified investor. |
| `get_job_listings` | Retrieves job listings data based on specified parameters. |
| `search_persons` | Submits a search request for persons associated with a given asynchronous job and returns the search results as a dictionary. |
| `search_companies` | Searches for companies using specified filters and pagination parameters. |
| `enrich_person` | Retrieves enriched person data from LinkedIn profile using the provided profile URL, enrichment mode, and requested fields. |
| `enrich_company` | Retrieves enriched company data using the provided company domain and enrichment mode. |
| `get_linked_in_posts` | Fetches LinkedIn posts for a specified company using its LinkedIn URL. |
| `search_linked_in_posts` | Searches LinkedIn posts using the provided keyword and filters, returning the search results as a dictionary. |
