# ApolloApp MCP Server

An MCP Server for the ApolloApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ApolloApp API.


| Tool | Description |
|------|-------------|
| `people_enrichment` | Matches a person based on provided identifying information such as name, email, organization, or LinkedIn URL, with options to reveal personal emails and phone numbers. |
| `bulk_people_enrichment` | Performs a bulk match operation on people data using a POST request to the "/people/bulk_match" endpoint, accepting query parameters to control the reveal of personal emails and phone numbers, and optionally specifying a webhook URL, with the request body containing JSON data. |
| `organization_enrichment` | Retrieves enriched organization data for a company specified by its domain name. |
| `bulk_organization_enrichment` | Enriches multiple organizations in bulk by submitting an array of domain names and returns detailed company profiles in a single request. |
| `people_search` | Searches for people matching specified criteria including titles, locations, seniorities, organization details, and keywords, returning paginated results. |
| `organization_search` | Searches mixed companies based on various criteria such as employee ranges, locations, revenue range, technology usage, keyword tags, organization names, and IDs, supporting pagination. |
| `organization_jobs_postings` | Retrieves a paginated list of job postings for a specified organization using the "GET" method, allowing optional pagination parameters for page and items per page. |
| `create_an_account` | Creates a new account resource using the provided query parameters such as name, domain, owner ID, account stage ID, phone, and raw address. |
| `update_an_account` | Updates an account identified by `{account_id}` with specified parameters such as `name`, `domain`, `owner_id`, `account_stage_id`, `raw_address`, and `phone`, returning a status message upon successful modification. |
| `search_for_accounts` | Searches for accounts based on organization name, account stage IDs, sorting, and pagination parameters, returning matching results. |
| `update_account_stage` | Updates multiple account records in bulk by their specified IDs, assigning each to the given account stage ID. |
| `update_account_ownership` | Updates the owners of multiple accounts by assigning a specified owner ID to the given list of account IDs. |
| `list_account_stages` | Retrieves a list of account stages. |
| `create_a_contact` | Creates a new contact with specified details such as name, organization, contact information, and labels. |
| `update_a_contact` | Updates or replaces the details of a specific contact identified by contact_id using the provided parameters as new values for the contact record. |
| `search_for_contacts` | Searches contacts based on keywords, contact stage IDs, sorting, and pagination parameters, returning a filtered and sorted list of contacts. |
| `update_contact_stage` | Updates the stage of multiple contacts by specifying their IDs and the new contact stage ID via a POST request. |
| `update_contact_ownership` | Updates the owners of specified contacts by assigning a new owner ID to the provided list of contact IDs. |
| `list_contact_stages` | Retrieves a list of all available contact stage IDs from the Apollo account[2][4]. |
| `create_deal` | Creates a new opportunity with specified details such as name, owner, account, amount, stage, and closed date. |
| `list_all_deals` | Searches and retrieves a paginated list of opportunities with optional sorting by a specified field. |
| `update_deal` | Updates specific fields of an opportunity resource identified by opportunity_id using a PATCH request[2][4][5]. |
| `list_deal_stages` | Retrieves a list of opportunity stages representing the different phases in the sales pipeline. |
| `add_contacts_to_sequence` | Adds specified contact IDs to an email campaign sequence, configuring how and when emails are sent to each contact and supporting various filtering options. |
| `update_contact_status_sequence` | Posts a request to remove or stop specified contact IDs from given emailer campaign IDs based on the selected mode. |
| `create_task` | Creates multiple tasks in bulk with specified user, contact IDs, priority, due date, type, status, and optional note parameters. |
| `search_tasks` | Searches for tasks using specified parameters and returns a paginated list of results, allowing users to sort by a field and filter by open factor names. |
| `get_a_list_of_users` | Searches for users with optional pagination parameters to specify the page number and number of results per page. |
| `get_a_list_of_email_accounts` | Retrieves a list of all available email accounts and their summary information. |
| `get_a_list_of_all_liststags` | Retrieves a list of labels. |
| `get_a_list_of_all_custom_fields` | Retrieves a list of all typed custom fields configured in the system. |
| `view_deal` | View Deal by opportunity_id |
| `search_for_sequences` | Search for Sequences by name |
