---
name: hashnode
description: Base class for applications interacting with GraphQL APIs. Extends `BaseApplication` to facilitate interactions with services that provide a GraphQL endpoint. It manages a `gql.Client` for executing queries and mutations, handles authentication headers similarly to `APIApplication`, and provides dedicated methods for GraphQL operations. Attributes: name (str): The name of the application. base_url (str): The complete URL of the GraphQL endpoint. integration (Integration | None): An optional Integration object for managing authentication. _client (GraphQLClient | None): The internal `gql.Client` instance.
---

# Hashnode Integration

Base class for applications interacting with GraphQL APIs. Extends `BaseApplication` to facilitate interactions with services that provide a GraphQL endpoint. It manages a `gql.Client` for executing queries and mutations, handles authentication headers similarly to `APIApplication`, and provides dedicated methods for GraphQL operations. Attributes: name (str): The name of the application. base_url (str): The complete URL of the GraphQL endpoint. integration (Integration | None): An optional Integration object for managing authentication. _client (GraphQLClient | None): The internal `gql.Client` instance.

## Available Tools

| Tool | Description |
|------|-------------|
| `publish_post` | Publishes a post to Hashnode using the GraphQL API. |
| `create_draft` | Creates a draft post on Hashnode. |
| `publish_draft` | Publishes a draft post. |
| `get_me` | Fetches details about the authenticated user. |
| `get_publication` | Fetches details about a publication by host or ID. Only one of host or publication_id should be provided. |
| `list_posts` | Lists posts from a publication. |
| `get_post` | Fetches details of a single post by ID, or by slug and hostname. |
| `modify_post` | Modifies an existing post using the GraphQL API. |
| `delete_post` | Deletes a post using the GraphQL API. |
| `add_comment` | Adds a comment to a post using the GraphQL API. |
| `delete_comment` | Deletes a comment using the GraphQL API. |
| `get_user` | Fetches details about a user by username. |
