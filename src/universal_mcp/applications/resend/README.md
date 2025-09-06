# ResendApp MCP Server

An MCP Server for the ResendApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ResendApp API.


| Tool | Description |
|------|-------------|
| `send_email` | Sends an email to specified recipients using the Resend API. |
| `send_batch_emails` | Sends a batch of emails using the Resend API. |
| `get_email` | Retrieves a single email by its specified ID. |
| `update_scheduled_email` | Updates the scheduling of an email to a new time. |
| `cancel_scheduled_email` | Cancels a scheduled email using the provided email ID. |
| `create_domain` | Creates a new domain with the specified name. |
| `get_domain` | Retrieves a single domain by its ID. |
| `verify_domain` | Verifies an existing domain using the provided domain ID. |
| `update_domain` | Updates an existing domain's settings regarding open tracking, click tracking, and TLS enforcement. |
| `list_domains` | Retrieves a list of all domains for the authenticated user. |
| `remove_domain` | Removes an existing domain by its ID using the Resend API. |
| `create_api_key` | Creates a new API key for authenticating with Resend. |
| `list_api_keys` | Retrieves a list of all API keys available through the resend service. |
| `remove_api_key` | Removes an existing API key using the specified key ID. |
| `create_broadcast` | Creates a new broadcast to send to a specified audience. |
| `get_broadcast` | Retrieves a single broadcast by its ID. |
| `update_broadcast` | Updates a broadcast by modifying its HTML content and/or subject line. |
| `send_broadcast` | Starts sending a broadcast via the API. |
| `remove_broadcast` | Removes an existing broadcast with 'draft' status. |
| `list_broadcasts` | Retrieves a list of all available broadcasts using the configured API key. |
| `create_audience` | Creates a new audience (a list of contacts) with the specified name. |
| `get_audience` | Retrieves a single audience object from the API using the specified audience ID. |
| `remove_audience` | Removes an existing audience using the provided audience ID and returns the API response. |
| `list_audiences` | Retrieves a list of all audiences. |
| `create_contact` | Creates a contact within a specific audience. |
| `get_contact` | Retrieves a single contact from an audience by providing either a unique contact ID or an email address, ensuring exactly one identifier is given. |
| `update_contact` | Updates an existing contact, identified by ID or email, within a specified audience. |
| `remove_contact` | Removes a contact from an audience, identified by ID or email. |
| `list_contacts` | Lists all contacts from a specified audience. |
