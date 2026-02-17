---
name: github
description: Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.
---

# Github Integration

Base class for applications interacting with RESTful HTTP APIs. Extends `BaseApplication` to provide functionalities specific to API-based integrations. This includes managing an `httpx.Client` for making HTTP requests, handling authentication headers, processing responses, and offering convenient methods for common HTTP verbs (GET, POST, PUT, DELETE, PATCH). Attributes: name (str): The name of the application. integration (Integration | None): An optional Integration object responsible for managing authentication and credentials. default_timeout (int): The default timeout in seconds for HTTP requests. base_url (str): The base URL for the API endpoint. This should be set by the subclass. _client (httpx.Client | None): The internal httpx client instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `star_repository` | Stars a GitHub repository for the authenticated user. This user-centric action takes the full repository name ('owner/repo') and returns a simple string message confirming the outcome, unlike other functions that list or create repository content like issues or pull requests. |
| `list_recent_commits` | Fetches and formats the 12 most recent commits from a repository. It returns a human-readable string summarizing each commit's hash, author, and message, providing a focused overview of recent code changes, unlike functions that list branches, issues, or pull requests. |
| `list_branches` | Fetches all branches for a specified GitHub repository and formats them into a human-readable string. This method is distinct from others like `search_issues`, as it returns a formatted list for display rather than raw JSON data for programmatic use. |
| `list_pull_requests` | Fetches pull requests for a repository, filtered by state (e.g., 'open'). It returns a formatted string summarizing each PR's details, distinguishing it from `get_pull_request` (single PR) and `search_issues` (raw issue data). |
| `search_issues` | Fetches issues from a GitHub repository using specified filters (state, assignee, labels) and pagination. It returns the raw API response as a list of dictionaries, providing detailed issue data for programmatic processing, distinct from other methods that return formatted strings. |
| `get_pull_request` | Fetches a specific pull request from a repository using its unique number. It returns a human-readable string summarizing the PR's title, creator, status, and description, unlike `list_pull_requests` which retrieves a list of multiple PRs. |
| `create_pull_request` | Creates a pull request between specified `head` and `base` branches, or converts an issue into a PR. Unlike read functions that return formatted strings, this write operation returns the raw API response as a dictionary, providing comprehensive data on the newly created pull request. |
| `create_issue` | Creates a new issue in a GitHub repository using a title, body, and optional labels. It returns a formatted confirmation string with the new issue's number and URL, differing from `update_issue` which modifies existing issues and `search_issues` which returns raw API data. |
| `update_issue` | Modifies an existing GitHub issue, identified by its number within a repository. It can update optional fields like title, body, or state and returns the raw API response as a dictionary, differentiating it from `create_issue` which makes new issues and returns a formatted string. |
| `list_repo_activities` | Fetches recent events for a GitHub repository and formats them into a human-readable string. It summarizes activities with actors and timestamps, providing a general event feed, unlike other `list_*` functions which retrieve specific resources like commits or issues. |
