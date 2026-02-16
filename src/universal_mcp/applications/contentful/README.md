---
name: contentful
description: Base class for applications interacting with GraphQL APIs. Extends `BaseApplication` to facilitate interactions with services that provide a GraphQL endpoint. It manages a `gql.Client` for executing queries and mutations, handles authentication headers similarly to `APIApplication`, and provides dedicated methods for GraphQL operations. Attributes: name (str): The name of the application. base_url (str): The complete URL of the GraphQL endpoint. integration (Integration | None): An optional Integration object for managing authentication. _client (GraphQLClient | None): The internal `gql.Client` instance.
---

# Contentful Integration

Base class for applications interacting with GraphQL APIs. Extends `BaseApplication` to facilitate interactions with services that provide a GraphQL endpoint. It manages a `gql.Client` for executing queries and mutations, handles authentication headers similarly to `APIApplication`, and provides dedicated methods for GraphQL operations. Attributes: name (str): The name of the application. base_url (str): The complete URL of the GraphQL endpoint. integration (Integration | None): An optional Integration object for managing authentication. _client (GraphQLClient | None): The internal `gql.Client` instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `get_entry` | Fetches a single entry of a specified content type by its ID. (See original docstring for details) |
| `get_entries_collection` | Fetches a collection of entries of a specified content type. (See original docstring for details) |
| `get_asset` | Fetches a single asset by its ID. (See original docstring for details) |
| `get_assets_collection` | Fetches a collection of assets. (See original docstring for details) |
| `execute_graphql_query` | Executes an arbitrary GraphQL query against the configured Contentful space/environment. |
