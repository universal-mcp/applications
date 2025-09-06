# SendgridApp MCP Server

An MCP Server for the SendgridApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the SendgridApp API.


| Tool | Description |
|------|-------------|
| `list_access_activity` | Retrieves activity settings using the specified limit, allowing for the optional specification of the user on whose behalf the request is made. |
| `delete_allowed_ips` | Removes a user or IP address from the access whitelist for a resource and returns a 204 No Content response upon success. |
| `list_allowed_ip` | Retrieves the current list of whitelisted IP addresses for access settings. |
| `add_ip_to_allow_list` | Adds IP addresses to a whitelist using the provided JSON payload in a POST request to the "/v3/access_settings/whitelist" endpoint. |
| `delete_allowed_ip` | Deletes the specified whitelist access rule identified by rule_id and returns no content upon success. |
| `get_allowed_ip` | Retrieves the details of a specific whitelist rule by its identifier using the GET method. |
| `list_alert` | Retrieves a list of alerts using the GitHub API, returning a successful response with a status code of 200. |
| `create_alert` | Creates a new Dependabot alert for a repository using the GitHub REST API and returns a status indicating success or failure. |
| `delete_alert` | Deletes a specified alert by its ID using the GitHub API and returns a status code indicating success. |
| `get_alert` | Retrieves a specific alert by its unique identifier from the API, returning the alert details in the response. |
| `update_alert` | Updates a specified Dependabot alert using the GitHub API and returns a status message. |
| `list_api_key` | Retrieves a list of API keys using the "GET" method at the "/v3/api_keys" path, allowing for optional filtering by a specified limit and supporting authentication on behalf of another user. |
| `create_api_key` | Creates and returns a new API key for authenticating requests to the API, with optional specification of the user or context on behalf of whom the key is generated. |
| `delete_api_key` | Deletes an API key identified by the `api_key_id` parameter, returning a successful response without content if the operation is completed. |
| `get_api_key` | Retrieves details for a specific API key identified by `{api_key_id}` using the `GET` method. |
| `update_api_key_name` | Updates properties of an existing API key identified by `api_key_id` using patch operations to modify its configuration. |
| `update_api_key` | Updates an API key identified by `{api_key_id}` using a JSON body, with optional support for operations on behalf of another entity. |
| `list_asm_group` | Retrieves a list of all suppression groups associated with the specified account, optionally filtered by group ID, using the "GET" method at the "/v3/asm/groups" path. |
| `creat_asm_group` | Creates a new suppression group for an account, allowing you to manage unsubscribe behavior, using the SendGrid API and returning a status message. |
| `delete_asm_group` | Deletes an Active Directory group specified by its ID using the GitHub API and returns a successful response if the operation is completed without content. |
| `get_asm_group` | Retrieves a specific suppression group associated with a user using the Sendgrid API, returning its details. |
| `update_asm_group` | Updates the settings or details of an ASM group identified by group_id using partial modifications via a PATCH request. |
| `list_suppression_from_asm_group` | Retrieves a list of email addresses that have been suppressed (unsubscribed) from a specific suppression group in SendGrid. |
| `add_suppression_to_asm_group` | Adds one or more email addresses to the suppression list for a specified unsubscribe group, preventing future emails from being sent to those addresses under that group. |
| `search_suppression_from_asm_group` | Searches a suppression group for multiple suppressions using a list of email addresses and a group ID, returning matching suppressions. |
| `delete_suppression_from_asm_group` | Deletes an email address from a specific suppression group, removing it from that group's suppression list. |
| `list_asm_suppression` | Retrieves a list of suppressions from an ASM group using the SendGrid API. |
| `create_global_suppression` | Adds one or more recipient email addresses to the global suppressions group, preventing them from receiving any emails from your account. |
| `delete_global_suppression` | Removes the specified email address from the global suppression (global unsubscribe) list and returns no content upon successful deletion[1][3][4]. |
| `get_global_suppression` | Retrieves information about a specific email address in the global suppression group using the SendGrid API. |
| `get_asm_suppression` | Retrieves a list of suppression groups from which a specified email address has been unsubscribed. |
| `list_browser_stat` | Retrieves statistical data for specified browsers, allowing filtering and pagination by date, browser name, and other query parameters. |
| `list_campaign` | Retrieves a list of campaigns with optional pagination and filtering by limit and offset, allowing operations on behalf of another entity. |
| `create_campaign` | Creates a new campaign resource using the provided JSON payload and returns a status code upon success or failure. |
| `delete_campaign` | Deletes the specified campaign identified by campaign_id and returns a 204 No Content status on successful deletion. |
| `get_campaign` | Retrieves details for a specific campaign identified by its ID using the GET method. |
| `update_campaign` | Modifies a specific campaign by updating selected fields identified by the `{campaign_id}` using JSON data in the request body, returning a status response. |
| `un_schedule_campaign` | Deletes the scheduled delivery of a campaign, returning a 204 (No Content) response if successful. |
| `get_scheduled_campaign` | Retrieves schedule details for a specified campaign using the "GET" method, optionally executed on behalf of another entity. |
| `update_scheduled_campaign` | Modifies the schedule of a campaign with the specified ID using a PATCH request, allowing partial updates to the schedule details. |
| `schedule_campaign` | Creates a new schedule for a specified campaign using the POST method, accepting JSON-formatted data and returning a "201 Created" response upon successful creation. |
| `send_campaign` | Initiates a currently scheduled campaign using the provided campaign ID and returns a status message if successful. |
| `send_test_campaign` | Tests the schedule configuration for a specific campaign using the POST method and returns a status code, with the campaign identified by the provided campaign ID. |
| `list_category` | Retrieves a list of the latest 1,000 unique categories associated with all Single Sends in ascending order. |
| `list_category_stat` | Retrieves statistical data for specified categories within a date range, optionally aggregated by a given parameter. |
| `list_category_stat_sum` | Retrieves summary statistics for categories using the "GET" method, allowing filtering by date range, sorting, and aggregation options. |
| `list_client_stat` | Retrieves client statistics for a specified period, allowing aggregation options, using the "GET" method at the "/v3/clients/stats" endpoint. |
| `get_client_stat` | Get statistical data for a specified client type with optional filtering by date range and aggregation parameters. |
| `list_custom_field` | Retrieves a list of custom fields from a contact database using the "GET" method, allowing for on-behalf-of parameters to specify the user making the request. |
| `create_custom_field` | Creates a new custom field in the contact database using a POST request with a JSON body. |
| `delete_custom_field` | Removes the specified custom field from the contact database, returning appropriate status codes based on success or failure. |
| `get_custom_field` | Retrieves the details of a specific custom field in the contact database, including its name, type, and other attributes. |
| `delete_contact_db_lists` | Deletes a contact list in the contact database using the provided JSON body and returns a successful status without content if the operation is successful. |
| `list_contact_db_list` | Retrieves a list of all recipient lists from the contact database using the SendGrid API. |
| `create_contact_db_list` | Creates a new contact list in the contact database and returns the created list resource. |
| `delete_contact_db_list` | Deletes a contact list identified by `{list_id}` in the contact database, optionally removing associated contacts if specified, and returns a status message. |
| `get_contact_db_list` | Retrieves details of a contact list specified by its ID using the "GET" method. |
| `update_contact_db_list` | Updates specific properties of a contact list identified by {list_id} using a JSON Patch request. |
| `list_recipients_from_contact_db_list` | Retrieves a list of recipients for a specified contact list, allowing optional pagination via page and page size parameters. |
| `add_recipients_to_contact_db_list` | Adds recipients to a specified contact list using the POST method and returns a success status upon creation. |
| `delete_recipient_from_contact_db_list` | Deletes a specific recipient from a contact list identified by list_id and recipient_id. |
| `add_recipient_to_contact_db_list` | Adds a recipient to a specific contact list by list ID and recipient ID. |
| `delete_recipients` | Deletes one or more recipients from the contact database according to the details provided in the JSON request body. |
| `list_recipient` | Get a paginated list of recipients from the contact database. |
| `update_recipient` | Updates a contact database recipient using the PATCH method with JSON content, allowing for partial modifications to an existing recipient's details. |
| `add_recipient` | Creates a new contact recipient in the contact database and returns the result, with the data provided in the request body. |
| `get_billable` | Retrieves the current count of billable recipients in the Marketing Campaigns contact database. |
| `list_recipient_count` | Retrieves the total count of recipients in the contact database. |
| `list_search_recipient` | Retrieves recipients from SendGrid's contact database matching a specified field name using a GET request to allow filtering by custom recipient attributes. |
| `search_recipient` | Searches recipients using segment conditions without creating a segment, allowing filters like equality, inequality, and containment, and returns a list of matching recipients. |
| `delete_recipient` | Deletes a recipient from the contact database by the specified recipient ID and returns a status code indicating the outcome. |
| `get_recipient` | Retrieves a single recipient from the contact database by ID using the SendGrid API. |
| `get_recipient_list` | Retrieves a list of contact lists associated with a specific recipient identified by their recipient ID. |
| `list_reserved_field` | Retrieves a list of reserved field names in SendGrid's contact database that cannot be used for custom field names. |
| `list_segment` | Retrieves a list of all segments defined in the contact database using the SendGrid API. |
| `delete_segment` | Deletes a marketing segment identified by the segment ID using the DELETE method, returning a status code indicating the outcome of the operation. |
| `list_recipient_for_segment` | Retrieves a list of recipients for a specified contact database segment using pagination controls. |
| `list_status` | Retrieves the status of current and recent contact export jobs from the SendGrid contact database. |
| `list_design` | Retrieves a paginated list of design resources, supporting optional filtering by page size, page token, and summary mode. |
| `create_design` | Creates a new design using the provided JSON data and returns a success response with a 201 status code upon successful creation. |
| `list_pre_built_design` | Retrieves a list of pre-built designs using the "/v3/designs/pre-builts" endpoint, allowing for pagination and optional summarization of the results. |
| `get_pre_built_design` | Retrieves the details of a pre-built design by its ID using the "GET" method. |
| `duplicate_pre_built_design` | Creates or updates a pre-built design by ID using the provided data and returns a status response. |
| `delete_design` | Deletes a design resource identified by the specified ID using the DELETE method and returns a status code indicating success or failure. |
| `get_design` | Retrieves the details of a design by its ID using the "GET" method and returns a successful response if the design exists. |
| `update_design` | Updates a specific design resource by modifying partial attributes identified by the `{id}` at the `/v3/designs/{id}` endpoint using JSON data in the request body. |
| `duplicate_design` | Updates a design with the specified ID using the provided data and returns a successful creation response. |
| `list_device_stat` | Retrieves device statistics using the "GET" method, allowing for customization through parameters such as on behalf of, advanced query strings for limit and offset, aggregation, and start and end dates. |
| `list_engagement_quality_score` | Retrieves SendGrid Engagement Quality scores for a specified date range using the GET method. |
| `list_subuser_engagement_quality_score` | Retrieves engagement quality scores for specified subusers, including overall scores and contributing metrics, using optional parameters for date range and pagination. |
| `list_geo_stat` | Retrieves geographic statistics for a specified country using the GET method, allowing for advanced filtering by date range and aggregation options. |
| `list_ip` | Retrieves a list of IP addresses based on specified query parameters, including filtering by lease status, enabled status, pool assignment, and other criteria. |
| `list_assigned_ip` | Retrieves a list of assigned IP addresses using the "GET" method at the "/v3/ips/assigned" path. |
| `add_ip_to_ip_pool` | Adds a new IP address to the specified IP pool. |
| `delete_ip_from_ip_pool` | Deletes the specified IP address from the given IP pool. |
| `list_remaining_ip_count` | Retrieves the number of remaining IP addresses available for allocation. |
| `list_warm_up_ip` | Retrieves and returns data related to the IP warm-up process using the GET method at the "/v3/ips/warmup" path. |
| `warm_up_ip` | Initiates the warmup process for one or more IP addresses by submitting a request in JSON format and returns a success or not found response. |
| `stop_ip_warm_up` | Removes the specified IP address from the warmup pool and returns no content upon successful deletion. |
| `get_warm_up_ip` | Retrieves information about warming up a specific IP address using the GET method and returns a response based on the operation's success or failure. |
| `create_mail_batch` | Creates and submits a batch of emails in a single request, supporting optional delegation and returning a confirmation upon successful processing. |
| `get_mail_batch` | Retrieves the status and details of a specific batch mail operation by its batch ID. |
| `send_mail` | Sends an email using the specified mail service by transmitting the required data via the POST method at the "/v3/mail/send" endpoint. |
| `list_mail_setting` | Retrieves mail settings using the GET method, allowing optional parameters for pagination and acting on behalf of another party. |
| `list_address_whitelist` | Retrieves the current list of whitelisted email addresses for mail settings. |
| `update_address_whitelist` | Modifies the email address whitelist settings using the PATCH method, accepting JSON payload updates at the "/v3/mail_settings/address_whitelist" endpoint. |
| `list_bounce_purge` | Retrieves the current bounce purge mail settings using the SendGrid API, which define how and when bounced email addresses are automatically removed from suppression lists. |
| `update_bounce_purge` | Updates the bounce purge mail settings by applying partial modifications to the resource using a JSON request body. |
| `list_footer` | Retrieves the footer settings for mail using the specified parameters. |
| `update_footer` | Updates the footer settings for mail using the PATCH method, allowing partial modifications to existing mail settings. |
| `list_forward_bounce` | Retrieves the current mail settings for forwarding bounced emails to a specified address. |
| `update_forward_bounce` | Modifies mail settings for forwarding and bouncing using the "PATCH" method, updating specified fields in the resource located at "/v3/mail_settings/forward_bounce". |
| `list_forward_spam` | Retrieves the current Forward Spam mail settings, including the enabled status and any email addresses designated to receive forwarded spam reports[2][3]. |
| `update_forward_spam` | Updates mail settings for spam forwarding using the "PATCH" method, allowing partial modifications to the existing configuration. |
| `list_mailbox_provider_stat` | Retrieves email statistics segmented by recipient mailbox provider, allowing for filtering by provider, date range, and aggregation type. |
| `list_contact` | Retrieves a list of contacts from the marketing service, returning their details in the response. |
| `update_contact` | Updates or adds marketing contact information by replacing the existing contact data with the provided JSON payload. |
| `list_batched_contact` | Creates a batch of contacts in the marketing system using a JSON payload and returns a success status upon completion. |
| `list_export_contact` | Retrieves a list or details of marketing contact exports using the "GET" method at the "/v3/marketing/contacts/exports" path. |
| `export_contact` | Exports contacts using a POST request to the "/v3/marketing/contacts/exports" endpoint, accepting JSON data in the request body. |
| `get_export_contact` | Retrieves the details of a specific marketing contacts export by its ID using the "GET" method. |
| `import_contact` | Imports or updates marketing contacts in bulk by replacing or creating the contact data using a JSON payload. |
| `get_import_contact` | Retrieves details about a specific contact import operation by its ID using the "GET" method. |
| `search_contact` | Searches for contacts using a SendGrid API endpoint by sending a POST request with a JSON body containing a valid SGQL query, returning up to 50 contacts that match the search criteria. |
| `list_contact_by_email` | Searches for marketing contacts by their email addresses via a POST request and returns matching contact records or error responses if the request is invalid. |
| `get_contact_by_identifiers` | Searches marketing contacts by a specified identifier type using a POST request with JSON payload and returns matching contact information. |
| `delete_contact_identifier` | Deletes a contact identifier with the specified contact ID and returns a status indicating whether the operation was accepted or encountered errors. |
| `get_contact` | Retrieves detailed information for a specified contact in the marketing contacts database. |
| `list_field_definition` | Retrieves the definitions of marketing fields available for use in marketing-related API operations. |
| `create_field_definition` | Creates new custom field definitions for marketing purposes using the "POST" method at the "/v3/marketing/field_definitions" endpoint, accepting JSON-formatted data in the request body. |
| `delete_field_definition` | Deletes the specified marketing field definition by custom field ID and returns a 204 (No Content) on success or 404 (Not Found) if the resource does not exist. |
| `update_field_definition` | Updates a specific custom field definition in the marketing system using the provided field ID and returns a status or error response. |
| `delete_integration` | Deletes marketing integrations specified by the IDs provided in the request, returning no content upon successful deletion. |
| `get_integrations_by_user` | Retrieves a list of available marketing integrations and their API connection details. |
| `add_integration` | Creates a new marketing integration by accepting required JSON data and returns a confirmation on success or an error otherwise. |
| `find_integration_by_id` | Retrieves details about a specific marketing integration by its ID using the "GET" method at the path "/v3/marketing/integrations/{id}". |
| `update_integration` | Updates a marketing integration identified by its ID using the provided JSON Patch document. |
| `create_marketing_list` | Creates a new marketing list for managing contacts in marketing campaigns using the SendGrid API. |
| `delete_marketing_list` | Deletes a specific marketing list using the provided ID and optionally deletes associated contacts if the `delete_contacts` query parameter is set to true. |
| `get_marketing_list` | Retrieves details of a marketing list by its ID using the "GET" method, optionally filtering by contact sample if specified. |
| `update_marketing_list` | Modifies a specific marketing list identified by its ID using the PATCH method, allowing for partial updates to the list's properties. |
| `delete_contact` | Deletes contacts in the marketing system using the specified IDs or clears all contacts if the "delete_all_contacts" parameter is set, returning status codes to indicate the outcome of the operation. |
| `list_contact_count` | Retrieves the total number of contacts in the specified marketing list. |
| `list_marketing_segment` | Retrieves a list of marketing lists, allowing pagination through optional parameters for page size and page token. |
| `create_segment` | Creates a new segment in the contact database using a JSON payload. |
| `refresh_segment` | Refreshes a specified marketing segment by its ID, ensuring that the segment is updated to reflect any changes in contact data or segment criteria. |
| `update_segment` | Updates a marketing segment using the PATCH method, allowing partial modifications to the specified segment resource. |
| `get_segment` | Retrieves details for a specific marketing segment, identified by its segment ID, with optional filtering by sampling contacts. |
| `list_sender` | Retrieves a list of senders using the API endpoint at "/v3/senders" with the "GET" method, potentially operating on behalf of another entity. |
| `delete_sender` | Deletes a marketing sender with the specified ID using the DELETE method, returning a successful response with no content if found, or an error if unauthorized or not found. |
| `update_sender` | Updates the properties of a marketing sender resource identified by the given ID using a PATCH request and returns the appropriate status code. |
| `delete_single_sends` | Deletes one or more Single Sends from SendGrid's marketing campaigns by ID, permanently removing them from the system. |
| `list_single_send` | Retrieves a paginated list of all Single Sends (one-time, non-automated email campaigns) with condensed details about each, allowing optional page size and token parameters for result pagination. |
| `create_single_send` | Creates a new single send email campaign using the provided request data. |
| `search_single_send` | Searches yielded no direct description of the specific "/v3/marketing/singlesends/search" POST operation, but based on standard REST API and endpoint conventions, this endpoint likely performs a search for single-send marketing campaigns using parameters such as pagination (page_size, page_token) provided in the query and a JSON request body. |
| `delete_single_send` | Deletes a single send marketing campaign identified by the specified ID using the DELETE method. |
| `get_single_send` | Retrieves detailed information about a specific Single Send using its ID. |
| `update_single_send` | Modifies an existing single send resource by partially updating its properties using the PATCH method at the "/v3/marketing/singlesends/{id}" endpoint. |
| `duplicate_single_send` | Creates and returns a new single send email draft in the marketing automation system, optionally setting initial configurations such as send time and template data. |
| `delete_scheduled_single_send` | Deletes a scheduled Single Send using the provided Single Send ID, effectively canceling its future delivery. |
| `schedule_single_send` | Schedules a Single Send email campaign for future delivery by updating its schedule using the specified ID and returns a success status upon completion. |
| `list_automation_stat` | Retrieves marketing automation statistics for specified automation IDs with support for pagination. |
| `export_automation_stat` | Exports marketing automation statistics based on the provided ids and timezone. |
| `get_automation_stat` | Retrieves detailed statistics for a specific automation identified by its ID, supporting filtering, grouping, date ranges, timezone selection, and pagination. |
| `list_click_tracking_stat` | Retrieves and paginates statistics for links contained within a specified automation workflow, optionally grouped or filtered by step. |
| `list_single_send_stat` | Retrieves statistics for single sends identified by the specified IDs, with optional pagination. |
| `export_single_send_stat` | Exports statistics for specified single sends in a downloadable format, with options to filter by IDs and set the timezone for timestamps. |
| `get_single_send_stat` | Retrieves aggregated marketing statistics for a specific single send campaign, supporting filtering by date, timezone, pagination, and optional grouping. |
| `list_single_send_tracking_stat` | Retrieves statistics for links in a single send campaign identified by {id}, allowing for pagination and filtering by group by, variation ID, and phase ID. |
| `send_test_marketing_email` | Sends an email for marketing testing purposes using the provided JSON data and returns a success status when processed successfully. |
| `list_message` | Retrieves a list of messages based on a query string, optionally limited by a specified number of results. |
| `request_csv` | Downloads messages using the provided query parameters and returns a successful response upon completion. |
| `download_csv` | Downloads a message file identified by the provided download UUID using the GET method. |
| `get_message` | Retrieves details of a specific message by its ID using the "GET" method at the "/v3/messages/{msg_id}" path. |
| `list_partner_setting` | Retrieves a paginated list of partner settings with support for limiting and offsetting results. |
| `create_account` | Creates a new partner account using the provided JSON data and returns a "201 Created" response upon success. |
| `delete_account` | Deletes a partner account identified by the specified `accountID` using the DELETE method, returning a 204 status on success. |
| `list_account_offering` | Retrieves a list of offerings associated with a specific partner account using the account ID. |
| `update_account_offering` | Updates an existing offering for a specific account using the "PUT" method, sending the updated offering details in JSON format to the "/v3/partners/accounts/{accountID}/offerings" endpoint. |
| `authenticate_account` | Initiates a single sign-on (SSO) process for the specified partner account identified by accountID. |
| `get_account_state` | Retrieves the current state information of a partner account identified by the specified accountID. |
| `update_account_state` | Updates the state of a partner account using JSON data and returns a status code indicating success or failure. |
| `list_offering` | Retrieves a list of offerings for partners using the GET method at the "/v3/partners/offerings" path. |
| `erase_recipient_email_data` | Initiates an erase job for recipients using the provided JSON data in the request body and returns a status message. |
| `list_scope` | Retrieves a list of authentication scopes using the GitHub API. |
| `list_scope_request` | Retrieves a list of scope requests using the "GET" method, allowing optional parameters for pagination and limit. |
| `deny_scope_request` | Deletes a scope request with the specified request ID using the GitHub API and returns a status message if successful. |
| `approve_scope_request` | Approves a pending scope request with the specified `request_id` using the GitHub API and returns a status message. |
| `add_ip` | Submits a list of IP addresses using a JSON payload via the POST method to the "/v3/send_ips/ips" endpoint, returning a success status code upon completion. |
| `get_ip` | Retrieves detailed information for a specified IP address, including assignment status, associated pools, and optional region details. |
| `update_ip` | Partially updates the IP resource at the specified path "/v3/send_ips/ips/{ip}" using a JSON payload to modify specific properties. |
| `list_sub_user_assigned_to_ip` | Retrieves information about subusers associated with a specified IP address, allowing optional filtering by a limit parameter. |
| `add_sub_users_to_ip` | Adds multiple subusers to a specific IP address in a single batch operation using the provided data in the request body. |
| `delete_sub_users_from_ip` | Deletes multiple subusers associated with a specified IP address in a single batch operation, supporting various response status codes including success (204), bad request (400), unauthorized (401), and server error (500). |
| `list_ip_pool` | Retrieves a list of IP pools using the "GET" method at the "/v3/ips/pools" path. |
| `create_ip_pool` | Creates IP pools using a JSON payload and returns a successful creation status upon completion. |
| `delete_ip_pool` | Deletes a specific IP pool identified by the {poolid} using the DELETE method, returning a 204 No Content response upon successful deletion. |
| `get_ip_pool` | Retrieves details for a specified IP pool, including its name, ID, and a sample list of associated IP addresses[1]. |
| `update_ip_pool` | Updates a specified IP pool using the provided JSON data and returns a status message. |
| `list_ip_assigned_to_ip_pool` | Retrieves a list of IP addresses within a specified pool, optionally including region information and limited by a specified after key. |
| `add_ips_to_ip_pool` | Adds multiple IP addresses to a pool using a batch operation via the POST method. |
| `delete_ips_from_ip_pool` | Deletes multiple IP addresses in a specified pool using the POST method with a JSON body containing IP details and returns a status message based on the response codes 204, 400, 401, or 500. |
| `create_sender` | Adds a new sender to the marketing senders list using the SendGrid API and returns a status code indicating the success or failure of the operation. |
| `get_sender` | Retrieves the details of a specific sender by ID using the GET method at the "/v3/marketing/senders/{id}" endpoint. |
| `reset_sender_verification` | Resends a verification email for a specified sender identity using the SendGrid API. |
| `create_sso_certificate` | Creates a new SSO certificate using the provided JSON data, enabling Single Sign-On configurations between an Identity Provider (IdP) and a service. |
| `delete_sso_certificate` | Deletes a certificate with the specified ID from the system using the "DELETE" method, returning appropriate status codes based on the operation's success or failure. |
| `get_sso_certificate` | Retrieves detailed information about a specific SSO certificate identified by the given certificate ID. |
| `update_sso_certificate` | Updates an existing SSO certificate identified by its certificate ID and returns the updated certificate details in the response. |
| `list_sso_integration` | Retrieves Single Sign-On (SSO) integrations using the API, optionally filtering by a specified condition with the "si" query parameter. |
| `create_sso_integration` | Creates a new Single Sign-On (SSO) integration using the provided details, returning a status message indicating the outcome of the operation. |
| `delete_sso_integration` | Deletes a specified SSO integration and returns a successful status with no content upon completion. |
| `get_sso_integration` | Retrieves details about a specific SSO integration identified by {id} using the GET method, with an optional query parameter "si" for additional filtering or inclusion. |
| `update_sso_integration` | Updates an existing single sign-on integration identified by {id} at path "/v3/sso/integrations/{id}" using the "PATCH" method. |
| `list_sso_integration_certificate` | Retrieves information about certificates associated with a specific SSO integration identified by the `integration_id`. |
| `create_sso_teammate` | Adds team members using single sign-on (SSO) and returns a status message upon successful addition. |
| `update_sso_teammate` | Updates the team membership or role of a specified user in a team using their username, supporting various permission checks and returning appropriate status codes. |
| `list_subuser` | Retrieves a list of subusers for a given username, allowing filtering by region and customization of the response through pagination and optional inclusion of the region. |
| `create_subuser` | Creates a new subuser using the GitHub API and returns a response based on the request's outcome. |
| `list_reputation` | Retrieves the reputation information for specified usernames using the GET method. |
| `list_stat` | Retrieves statistical data for specified subusers within a defined time period, allowing for optional filtering by date range, aggregation method, and pagination control. |
| `list_monthly_stat` | Retrieves and returns monthly statistics for subusers, filterable by date and customizable with sorting, pagination, and subuser selection. |
| `list_stat_sum` | Retrieves summary statistics for subusers, allowing optional filtering by sort direction, start and end dates, data aggregation, and sorting metrics. |
| `delete_subuser` | Deletes the specified subuser from the account, removing their access and related data. |
| `update_subuser` | Updates properties of a specified subuser using a PATCH request with JSON data and returns a success status (204) or relevant error codes. |
| `get_subuser_credit` | Retrieves the credits information for a specified subuser, identified by {subuser_name}, and returns the details in response. |
| `update_subuser_credit` | Updates the credits of a subuser identified by `{subuser_name}` using a JSON payload. |
| `update_subuser_remaining_credit` | Updates the remaining credits for a specified subuser and returns status information. |
| `update_subuser_ip` | Updates the IP configuration for a specified subuser using the provided JSON data and returns a success status if the operation is successful. |
| `list_subuser_monthly_stat` | Retrieves monthly statistics for a specified subuser using the "GET" method, allowing filtering by date and optional sorting and pagination parameters. |
| `update_subuser_website_access` | Updates a subuser's website access using the GitHub API, returning a status message upon successful modification. |
| `delete_suppression_blocks` | Removes a suppression block using the "DELETE" method at the "/v3/suppression/blocks" path, returning a successful response with no content. |
| `list_suppression_block` | Retrieves a list of suppression blocks within a specified time range using optional pagination and partial matching parameters. |
| `delete_suppression_block` | Removes the specified email address from the suppression block list and returns no content upon success. |
| `get_suppression_block` | Retrieves the block status of an email address using a GET request to the "/v3/suppression/blocks/{email}" endpoint. |
| `delete_suppression_bounces` | Removes bounce suppression records via DELETE, returning 204 No Content on success or 401 Unauthorized if not authenticated. |
| `list_suppression_bounces` | Retrieves a paginated list of bounced email addresses and their details, optionally filtered by time range, email address, and other query parameters. |
| `list_suppression_bounces_classifications` | Retrieves email bounces by specific classification using the SendGrid API, allowing filtering by date range and classification types such as 'Content', 'Frequency or Volume Too High', 'Invalid Address', 'Mailbox Unavailable', 'Reputation', 'Technical Failure', and 'Unclassified'. |
| `get_suppression_bounces_classifications` | Retrieves bounces from the suppression list filtered by a specified classification and optional date range. |
| `delete_suppression_bounce` | Deletes a suppression bounce entry for a specified email address. |
| `get_suppression_bounces` | Retrieves bounce suppression details for a specific email address from the suppression list. |
| `delete_invalid_emails` | Deletes a specified invalid email from suppression using the "DELETE" method and returns no content upon successful removal. |
| `list_invalid_email` | Retrieves a list of invalid emails for suppression, optionally filtered by start and end time, email address, and pagination parameters. |
| `delete_invalid_email` | Deletes an invalid email from the suppression list at path "/v3/suppression/invalid_emails/{email}" using the DELETE method and returns a 204 No Content response. |
| `get_invalid_email` | Retrieves details about a specific invalid email address from the suppression list. |
| `delete_spam_reports` | Removes spam report records via a DELETE request to the specified endpoint, returning a 204 No Content response upon success. |
| `list_spam_report` | Retrieves a list of spam reports based on query parameters for start and end times, with optional filtering by pagination and email partial matching. |
| `delete_spam_report` | Deletes the specified email address from the spam reports suppression list and returns no content upon successful removal. |
| `get_spam_report` | Retrieves the spam report details for the specified email address from the suppression list. |
| `list_global_suppression` | Retrieves a paginated list of email addresses that were unsubscribed within a specified time range, optionally filtered by partial email match and supporting pagination parameters. |
| `list_teammate` | Retrieves a list of teammates using the specified parameters, including pagination options and the ability to act on behalf of another user. |
| `invite_teammate` | Creates a new teammate by sending a POST request to the "/v3/teammates" endpoint, accepting JSON content, and returns a 201 status upon successful creation. |
| `list_pending_teammate` | Retrieves a list of pending teammates using the GitHub API and returns a successful response with relevant details. |
| `delete_pending_teammate` | Deletes a pending teammate invitation using the provided token, returning a 204 status if successful. |
| `resend_teammate_invite` | Resends a pending teammate invitation associated with the given token using the API. |
| `list_subuser_by_template` | Retrieves the list of Subusers and their available scopes that a specified Teammate can access and act on behalf of. |
| `delete_teammate` | Removes a teammate from a GitHub organization using the GitHub API and returns a status code indicating success or failure. |
| `get_teammate` | Retrieves information about a GitHub user's teammate with the specified username using the "GET" method. |
| `update_teammate` | Updates the details of a teammate identified by username within an organization using JSON-formatted data and supports acting on behalf of another user. |
| `list_template` | Retrieves the current template mail settings for the specified account using the SendGrid API. |
| `create_template` | Creates a new template using the JSON data provided in the request body and returns a successful creation response with a 201 status code. |
| `delete_template` | Deletes a template identified by the `template_id` in the `/v3/templates/{template_id}` path, returning a successful response with no content (204). |
| `get_template` | Retrieves detailed information for the specified template identified by its template_id. |
| `update_template` | Updates the mail settings template using the PATCH method, allowing for partial modifications to the existing resource. |
| `duplicate_template` | Creates a new resource related to a template identified by `{template_id}` using a JSON payload and returns a successful creation status with a 201 response code. |
| `create_template_version` | Creates a new version for a specified template using the POST method and returns a 201 Created response upon success. |
| `delete_template_version` | Deletes a specific version of a template identified by the provided template ID and version ID. |
| `get_template_version` | Retrieves a specific version of a transactional template by its template ID and version ID using the SendGrid API. |
| `activate_template_version` | Activates a specific version of a template by sending a POST request with the template and version IDs. |
| `list_tracking_setting` | Retrieves the current tracking settings for an account using the SendGrid API. |
| `list_click_tracking_setting` | Retrieves the current click tracking settings for the specified configuration using the "GET" method. |
| `update_click_tracking_setting` | Updates the click tracking settings for email links using a PATCH request to the "/v3/tracking_settings/click" endpoint. |
| `list_google_analytics_tracking_setting` | Retrieves the Google Analytics tracking settings using the API. |
| `update_google_analytics_tracking_setting` | Updates the Google Analytics tracking settings for the specified resource using the provided configuration. |
| `list_open_tracking_setting` | Retrieves the open tracking settings for the specified configuration using the "GET" method, optionally executed on behalf of another user. |
| `update_open_tracking_setting` | Updates tracking settings for open events by sending a JSON payload to the specified endpoint, returning a successful status upon completion. |
| `list_subscription_tracking_setting` | Retrieves the current subscription tracking settings for your SendGrid account, which control the inclusion of subscription management links in your emails. [1][2][3] |
| `update_subscription_tracking_setting` | Modifies the tracking settings subscription using the PATCH method, allowing partial updates to specific fields of the resource at the "/v3/tracking_settings/subscription" path. |
| `list_account` | Retrieves information about the GitHub user account using the "GET /v3/user/account" method. |
| `list_credit` | Retrieves user credits information using the specified API endpoint. |
| `list_email` | Retrieves a user's email address using the GET method, optionally acting on behalf of another user. |
| `update_email` | Updates a user's email address using the PUT method at the "/v3/user/email" endpoint, accepting a JSON body and returning a successful response upon completion. |
| `update_password` | Updates the password for the authenticated user using the GitHub API. |
| `list_profile` | Retrieves the authenticated user's public and private profile information. |
| `update_profile` | Updates specific fields in the authenticated user's profile using partial modifications with a JSON request payload. |
| `list_scheduled_send` | Retrieves a list of all scheduled sends for a user using the specified API endpoint. |
| `create_scheduled_send` | Creates a new scheduled send for a user with the provided details and returns a status indicating the result of the operation. |
| `delete_scheduled_send` | Deletes a scheduled send batch identified by the specified `batch_id` in the user's account, returning no content upon successful deletion. |
| `get_scheduled_send` | Retrieves details about a scheduled send operation for the specified batch ID. |
| `update_scheduled_send` | Updates a scheduled send batch by modifying specific fields using JSON Patch operations, returning a response code indicating the outcome of the update operation. |
| `list_enforced_tls_setting` | Retrieves the TLS enforcement settings for the user, including whether TLS is required for connections, and returns the current configuration. |
| `update_enforced_tls_setting` | Updates the Enforced TLS settings for a user, specifying whether TLS support and a valid certificate are required for recipients, using the "PATCH" method. |
| `list_username` | Retrieves the authenticated user's profile information, supporting requests made on behalf of another user. |
| `update_username` | Updates the username of the authenticated user with the provided new username data. |
| `create_event_webhook` | Configures event settings for user webhooks using the POST method, accepting JSON data in the request body. |
| `list_event_webhook` | Retrieves the configuration and settings for all user webhook events and their associated preferences. |
| `get_signed_event_webhook` | Retrieves the signed event settings for a specific webhook event identified by the provided ID using the GET method. |
| `update_signed_event_webhook` | Updates the configuration settings for a signed event webhook identified by the given ID using the PATCH method and returns the updated settings. |
| `delete_event_webhook` | Removes the event webhook settings with the specified ID and returns no content (204) or not found (404) if the settings do not exist. |
| `get_event_webhook` | Retrieves the webhook event settings for a specific user by ID. |
| `update_event_webhook` | Updates the configuration for a specific user webhook event setting using the PATCH method and the provided JSON data. |
| `test_event_webhook` | Sends a test event to the user's webhook endpoint to verify its functionality. |
| `list_parse_setting` | Retrieves and returns the settings for parsing webhooks in the user's webhooks configuration. |
| `create_parse_setting` | Configures and parses webhook settings for a user using the POST method. |
| `delete_parse_setting` | Deletes the parse webhook settings associated with the specified hostname for the authenticated user. |
| `get_parse_setting` | Retrieves the settings for parsing webhooks from a specified hostname using the GET method. |
| `update_parse_setting` | Updates the settings for parsing webhooks for a specified hostname using the PATCH method, returning a status message upon success. |
| `list_parse_static` | Retrieves statistical data for webhook parsing, allowing users to filter results by limit, offset, aggregation, and date range. |
| `validate_email` | Validates the format and deliverability of an email address by submitting the email data in JSON format to the API. |
| `get_validations_email_jobs` | Retrieves a list of email validation jobs processed by the API. |
| `list_email_job_for_verification` | Updates an existing email job validation resource using a JSON payload at the "/v3/validations/email/jobs" endpoint and returns a status message upon successful modification. |
| `get_email_job_for_verification` | Get the status and details of an email validation job by its job ID. |
| `list_verified_sender` | Retrieves a list of verified senders using the GET method, allowing optional filtering by limit, last seen ID, and specific ID. |
| `create_verified_sender` | Creates a new verified sender using the provided details and returns a successful response upon creation. |
| `list_verified_sender_domain` | Retrieves a list of verified sender domains. |
| `resend_verified_sender` | Resends a verification request for a specified verified sender using the POST method. |
| `list_verified_sender_steps_completed` | Retrieves the completed steps associated with verified senders in the system. |
| `verify_sender_token` | Verifies a sender using the provided token and returns a successful response if valid. |
| `delete_verified_sender` | Deletes a verified sender with the specified ID using the DELETE method and returns a successful response with a 204 status code if the operation is successful. |
| `update_verified_sender` | Updates specific details of a verified sender identified by \{id\} using partial modifications. |
| `email_dns_record` | Creates a new whitelabel DNS configuration for email by submitting the required details in JSON format. |
| `list_authenticated_domain` | Retrieves a list of whitelabel domains for the specified criteria, supporting optional filters by username, domain name, and excluding subusers. |
| `authenticate_domain` | Creates a new whitelabeled domain using the provided JSON content in the request body, allowing for customized domain configurations. |
| `list_default_authenticated_domain` | Retrieves the default domain for a whitelabel setup, optionally filtered by a specified domain. |
| `disassociate_authenticated_domain_from_user` | Removes a domain from the whitelist for the specified subuser and returns no content upon success. |
| `list_authenticated_domain_with_user` | Get a list of whitelabel domains associated with a specified subuser by providing their username. |
| `list_all_authenticated_domain_with_user` | Retrieves a list of all subusers associated with whitelabel domains for a specified username. |
| `delete_authenticated_domain` | Deletes a whitelabel domain identified by `{domain_id}` using the DELETE method, returning a successful response with no content. |
| `get_authenticated_domain` | Retrieves details about a specific whitelabeled domain identified by the provided domain ID. |
| `update_authenticated_domain` | Updates the settings of an authenticated domain by modifying specified attributes using the PATCH method. |
| `disassociate_subuser_from_domain` | Deletes a specified subuser associated with a given whitelabel domain by domain ID and username. |
| `associate_subuser_with_domain` | Creates a subuser for the specified domain using the provided JSON data. |
| `associate_subuser_with_domain_multiple` | Associates a specific authenticated domain with a subuser using the SendGrid API. |
| `add_ip_to_authenticated_domain` | Associates IP addresses with a specific authenticated domain using the POST method and returns a status message. |
| `delete_ip_from_authenticated_domain` | Deletes an IP address associated with a specific domain in the whitelabel service. |
| `validate_authenticated_domain` | Validates a domain with the specified ID for whitelabel purposes using the provided parameters. |
| `list_reverse_dns` | Get a list of whitelabel IP addresses with optional filtering by IP, pagination, and on-behalf-of user context. |
| `set_up_reverse_dns` | Adds IP addresses to a whitelist using the "POST" method at the "/v3/whitelabel/ips" path, allowing specified IP addresses to access certain resources. |
| `delete_reverse_dns` | Deletes the specified whitelabel IP address identified by its ID and returns a 204 No Content status upon successful removal. |
| `get_reverse_dns` | Retrieves information about a specific whitelabel IP address identified by its ID using the "GET" method. |
| `validate_reverse_dns` | Validates a specified IP address for whitelabeling using the POST method and returns a validation result. |
| `list_branded_link` | Retrieves a list of whitelabeled links, allowing optional filtering by a specified limit and execution on behalf of another entity. |
| `create_branded_link` | Creates a new whitelabel link resource using the provided JSON payload and returns a 201 status code upon successful creation. |
| `list_default_branded_link` | Retrieves the default whitelabel link for a specified domain using the "GET" method. |
| `disassociate_branded_link_from_subuser` | Deletes a subuser link for a specified whitelabel using the provided username and returns no content upon successful deletion. |
| `list_subuser_branded_link` | Retrieves and provides information about a subuser in the context of whitelabel links using the "GET" method, requiring a username as a query parameter. |
| `delete_branded_link` | Deletes a whitelabel link specified by the `{id}` parameter and returns a successful response without content. |
| `get_branded_link` | Retrieves the details of a whitelabel link specified by its ID using the GET method. |
| `update_branded_link` | Partially updates a whitelabel link by ID using JSON data and returns a success response. |
| `validate_branded_link` | Validates a specific whitelabel link by ID using the "POST" method. |
| `associate_branded_link_with_subuser` | Creates a new subuser link for the specified whitelabel link ID using a JSON request body and returns a success response. |
