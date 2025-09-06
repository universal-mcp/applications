# HubspotApp MCP Server

An MCP Server for the HubspotApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the HubspotApp API.


| Tool | Description |
|------|-------------|
| `add_a_note` | Create a note in HubSpot with the given properties and associations. |
| `fetch_multiple_lists` | Fetch multiple lists in a single request by ILS list ID. The response will include the definitions of all lists that exist for the listIds provided. |
| `fetch_list_memberships` | Fetch the memberships of a list in order sorted by the recordId of the records in the list. |
| `create_list` | Create a new list in HubSpot with the specified object type, processing type, and name.  |
| `get_list_by_id` | Fetch a single list by ILS list ID. |
| `delete_list_by_id` | Delete a list by ILS list ID. Lists deleted through this endpoint can be restored for up to 90 days. After 90 days, the list is permanently purged and cannot be restored |
| `add_records_to_list` | Add the records provided to the list. Records that do not exist or that are already members of the list are ignored. |
| `remove_records_from_list` | Remove the records provided from the list. Records that are not members of the list are ignored. |
| `search_lists` | Search lists by list name or page through all lists by providing an empty query value. |
| `fetch_list_by_name` | Fetch a list by its name and object type ID. |
| `batch_read_emails` | Retrieves a batch of emails from a CRM system using the "POST" method allowing optional filtering by archived status, and returns the results in a multipart response. |
| `get_email_by_id` | Retrieves detailed information about a specific email object in a CRM system, allowing optional filtering by properties, associations, and archival status. |
| `delete_email_by_id` | Deletes an email object identified by the specified emailId from a CRM system. |
| `update_email_by_id` | Updates specific properties of an existing email record in the CRM by its emailId using a PATCH request with JSON data. |
| `merge_emails_post` | Merges email records using the provided JSON payload, utilizing OAuth2 or private app authentication to manage contact data in the CRM system. |
| `archive_emails_batch` | Archives a batch of emails by sending a POST request to the "/crm/v3/objects/emails/batch/archive" endpoint with a JSON payload containing the email IDs to be archived. |
| `create_emails_batch_post` | Creates a batch of email objects in the CRM using the POST method, requiring JSON content and authorization through OAuth2 or private apps. |
| `update_emails_batch` | Updates multiple email objects in a CRM system using a batch operation via the POST method, returning status messages for each update. |
| `delete_email_gdpr_data` | Deletes a contact and associated data from the CRM in compliance with GDPR guidelines using the provided JSON payload, requiring the "crm.objects.contacts.write" permission. |
| `list_emails_with_filters` | Retrieves a paginated list of email objects with optional filtering by properties, associations, and archival status from the CRM email records. |
| `create_email` | Creates an email object in the CRM using the POST method, allowing for the association of metadata with the email and requiring authentication via OAuth2 or private apps to access the necessary permissions. |
| `search_emails_post` | Searches for email objects in a CRM system using specific criteria, returning relevant results. |
| `batch_read_products_post` | Retrieves a batch of product records from the CRM using the POST method, optionally filtering by archived status, and returns the results in a multi-status response. |
| `get_product_by_id` | Retrieves detailed information about a specific product by its ID, allowing optional filtering by properties, properties with history, associations, and archived status. |
| `delete_product_by_id` | Deletes a product from the CRM using its product ID. |
| `patch_product_by_id` | Updates specified properties of a product identified by productId using a JSON PATCH request. |
| `merge_products` | Merges two or more product records in a CRM system using the POST method, allowing for the consolidation of data into a single, unified record. |
| `archive_products_batch_post` | Archives a batch of products by ID using the POST method, accepting JSON-formatted request bodies and returning a 204 status upon successful execution. |
| `create_products_batch` | Creates multiple product records in a single batch request within the CRM system. |
| `update_products_batch` | Updates multiple product records in a batch using the HubSpot CRM v3 API and returns a status response indicating success or partial failure. |
| `delete_product_gdpr_data` | Performs a GDPR-compliant deletion of product records in the CRM using the POST method, requiring a JSON request body and authentication. |
| `list_products` | Retrieves a list of products from a CRM system using the "GET" method, allowing for optional filtering and customization of the returned data based on parameters such as limit, after, properties, properties with history, associations, and archived status. |
| `create_product` | Creates a new product in the CRM product library to manage the collection of goods and services offered by the company. |
| `search_products` | Searches for products in a CRM using a POST request to the "/crm/v3/objects/products/search" endpoint, allowing for filtering and retrieval of product data in a JSON format. |
| `get_pipeline_by_id_for_type` | Retrieves details about a specific CRM pipeline by its ID and object type, providing information about the stages and records within that pipeline. |
| `update_pipeline` | Updates the details of a specified pipeline for a given CRM object type by replacing its properties using the provided JSON payload. |
| `delete_pipeline_by_id_and_type` | Deletes a pipeline by its ID and object type in the CRM system using the specified security permissions, optionally validating references and deal stage usages before deletion. |
| `patch_pipeline_by_object_type` | Updates a CRM pipeline by specifying the object type and pipeline ID, allowing modifications to its configuration with optional validation checks for references and deal stage usage before deletion. |
| `get_pipeline_audit_by_object_type` | Retrieves an audit of all changes to a specific pipeline in HubSpot CRM, based on the provided object type and pipeline ID. |
| `get_pipeline_stages_by_object_type` | Retrieves the list of stages within a specified pipeline for a given object type in the CRM system. |
| `create_pipeline_stage` | Creates a new stage in a specified CRM pipeline using the POST method, requiring the object type and pipeline ID, and a JSON-formatted request body. |
| `list_pipelines_by_type` | Retrieves a list of pipelines for a specified object type in the CRM, allowing for the management and inspection of pipelines relevant to that object type. |
| `create_pipeline_by_object_type` | Creates a new pipeline for the specified CRM object type with the provided pipeline details. |
| `get_pipeline_stage_by_id` | Retrieves detailed information about a specific stage within a given pipeline and object type in the CRM system. |
| `update_pipeline_stage_by_id` | Updates a specific stage in a CRM pipeline using the provided JSON data and returns a status message. |
| `delete_pipeline_stage_by_id` | Deletes a specific stage from a pipeline for the given object type in the CRM system. |
| `update_pipeline_stage` | Updates a specific stage in a CRM pipeline using a PATCH request to the "/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}" endpoint, requiring a JSON body with the necessary updates. |
| `batch_read_companies_post` | Reads a batch of companies by internal ID or unique property values using the HubSpot CRM API and returns the results in a JSON format. |
| `get_company_by_id` | Retrieves a specific company record by ID from the CRM system, optionally including additional properties, associations, and historical data, depending on the query parameters provided. |
| `delete_company_by_id` | Deletes a company by its ID using the DELETE method, requiring the company ID as a path parameter and authorization through OAuth2 or private apps with the "crm.objects.companies.write" permission. |
| `patch_company_by_id` | Updates a company in the CRM using the PATCH method, allowing partial modifications to the company's properties. |
| `merge_companies_post` | Merges two or more company records into a single unified record using the CRM API, requiring a JSON payload and appropriate write permissions. |
| `archive_companies_batch_post` | Archives a batch of companies using the HubSpot CRM API, requiring a JSON body and returning a 204 status on successful operation. |
| `create_companies_batch` | Creates multiple company records in batch using the HubSpot CRM API and returns a status message, requiring authorization via OAuth2 or private apps. |
| `update_companies_batch` | Updates multiple company records in a single request using the HubSpot CRM API. |
| `delete_company_gdpr_data` | Performs a GDPR-compliant deletion of a company record in the CRM, permanently removing the associated personal data. |
| `get_companies` | Retrieves a list of company records from a CRM system, allowing for filtering by properties, associations, and archived status. |
| `create_company` | Creates a new company record in the CRM system using the provided JSON data and returns a 201 status code upon successful creation. |
| `search_companies_post` | Searches for and retrieves company records and their associated properties in the CRM based on specified criteria. |
| `get_calling_app_settings` | Retrieves the calling settings for a specified application in HubSpot CRM using the provided app ID. |
| `update_calling_app_settings` | Configures calling settings for a specified application ID in the CRM using a POST request with a JSON body. |
| `delete_calling_app_settings_by_id` | Deletes the settings for a specified CRM application identified by `{appId}`, returning a successful response with no content if the operation is completed. |
| `update_calling_settings` | Updates specific settings for the calling extension of the specified application by applying partial modifications to its resource. |
| `get_calling_app_recording_settings` | Retrieves the recording settings for a calling extension with the specified `appId` in the HubSpot CRM. |
| `post_calling_app_recording_settings` | Configures call recording settings for a specific application ID in the CRM using a POST request to update the recording settings. |
| `update_recording_settings` | Modifies the recording settings for a specific CRM application using the provided JSON body. |
| `read_quotes_batch` | Reads a batch of quote objects by their internal IDs or unique property values, optionally including archived quotes, in a single POST request. |
| `get_quote_by_id` | Retrieves a specific sales quote by its ID, optionally including custom properties, property history, associations, and archived status, using the HubSpot CRM API. |
| `delete_quote_by_id` | Deletes a sales quote with the specified ID using the HubSpot CRM API, requiring "crm.objects.quotes.write" permission. |
| `update_quote` | Updates a quote object with the specified ID in the CRM system using partial modifications, requiring a JSON body with the changes and returning a status message upon success. |
| `merge_quotes` | Merges quote objects in a CRM system using the POST method, allowing for the integration of data from multiple quotes into a single unified quote. |
| `archive_quotes_batch` | Archives a batch of quotes by sending a POST request to the "/crm/v3/objects/quotes/batch/archive" endpoint, requiring a JSON body and authentication via OAuth2 or private apps with the "crm.objects.quotes.write" permission. |
| `create_quote_batch` | Creates a batch of sales quotes using the HubSpot CRM API, requiring a JSON body and returning a status message upon successful creation. |
| `update_quotes_batch` | Updates a batch of quote objects in the CRM system using a single POST request, returning a status code indicating success or partial failure. |
| `delete_quote_gdpr_data` | Performs a GDPR-compliant deletion of a quote object in the CRM system, permanently removing the associated personal data. |
| `get_quotes` | Retrieves a list of quotes from the CRM, allowing for optional filtering by limit, after, properties, properties with history, associations, and archived status. |
| `create_quote` | Creates a new quote in HubSpot using the CRM API and returns a status message upon successful creation. |
| `search_quotes` | Searches for quotes in a CRM system using specified criteria and returns the results, requiring authentication via OAuth2 or private apps with read permissions for quotes. |
| `batch_read_deals_post` | Reads a batch of deals from the CRM using the provided IDs and returns the specified properties, allowing for optional filtering by archived status. |
| `get_deal_by_id` | Retrieves a deal by its ID and returns its details, supporting optional parameters for specifying properties, associations, and archived status. |
| `delete_deal_by_id` | Deletes a specific deal by its ID from the CRM system. |
| `update_deal_by_id` | Updates an individual deal in the CRM by its record ID using the PATCH method. |
| `merge_deals` | Merges two or more deal records into a single master deal record, consolidating data and deleting duplicates in the CRM system. |
| `archive_deals_batch_post` | Archives a batch of deal records in the CRM by their IDs using the POST method. |
| `create_deals_batch` | Creates multiple deals in a CRM using a batch operation via the POST method, requiring a JSON body with deal data and appropriate permissions for writing deals. |
| `batch_update_deals` | Updates multiple deals in HubSpot CRM in a single operation using a POST request to "/crm/v3/objects/deals/batch/update", requiring a JSON body with deal identifiers and updates, and supports OAuth2 and private app authentication for the "crm.objects.deals.write" scope. |
| `post_deal_gdpr_delete` | Deletes a deal record in compliance with GDPR requirements using the provided JSON payload, requiring a valid OAuth2 or private app authentication with the necessary write permissions. |
| `list_deals` | Retrieves a list of CRM deal objects from HubSpot using the GET method, allowing optional filtering by parameters such as limit, after, properties, propertiesWithHistory, associations, and archived status. |
| `create_deal` | Creates a new deal object in the CRM using the HubSpot API, requiring a JSON payload and returning a status code indicating success. |
| `search_deals` | Searches and retrieves deal records in the CRM using filters and criteria provided in the request body. |
| `cancel_import_by_id` | Cancels an active import operation in a CRM system using the provided import ID. |
| `get_import_by_id` | Retrieves the status and details of a specific CRM import operation identified by the import ID. |
| `get_import_errors_by_id` | Retrieves a list of errors associated with a specific CRM import operation, using the import ID, and allows filtering by optional parameters such as "after" and "limit". |
| `get_schema_by_object_type` | Retrieves the schema definition for a specified CRM object type, including its properties and metadata. |
| `delete_schema_by_type` | Deletes the specified CRM object schema by its type, optionally including archived versions, to remove its definition from the system. |
| `patch_crm_schema_by_object_type` | Updates a custom CRM object schema in HubSpot using the PATCH method, allowing for partial modifications to the schema of a specified object type. |
| `create_object_type_association` | Creates a new association definition for the specified CRM object type to define relationships between that object and others. |
| `delete_schema_object_type_purge` | Purges a schema for a specific object type in the CRM system using the DELETE method, requiring the objectType as a path parameter and a custom write permission. |
| `delete_association_by_object_type_id` | Removes an association identified by the associationIdentifier from a CRM object schema of the specified objectType using the HubSpot API. |
| `list_schemas` | Retrieves a list of custom object schemas in the CRM, optionally filtering by archived status, using either legacy private apps or OAuth2 credentials for authentication. |
| `create_crm_schema` | Creates a new custom object schema in the CRM to define a new type of CRM record. |
| `archive_properties_batch_post` | Archives a batch of properties for a specified object type in CRM using a POST request. |
| `get_property_group` | Retrieves details of a specified property group for a given CRM object type. |
| `remove_property_group` | Deletes a property group identified by the given object type and group name from the CRM schema. |
| `update_property_group_by_identifier` | Modifies the properties of a specified group in a CRM object type using the PATCH method, requiring authentication and a JSON request body to update the group's properties. |
| `get_crm_property` | Retrieves the details of a specific property for a given CRM object type, optionally including archived properties and additional specified fields. |
| `delete_property_by_object_type` | Deletes a specified property of a given object type in the CRM system. |
| `patch_crm_property_by_name` | Updates the specified property of a given CRM object type by applying partial modifications using a JSON Patch request. |
| `batch_read_properties_by_object_type` | Performs a batch read operation on CRM properties for a specified object type using a POST request, returning the results in a batch format. |
| `create_batch_properties` | Creates multiple properties in batches for a specified object type in the CRM using a POST request to the "/crm/v3/properties/{objectType}/batch/create" endpoint. |
| `get_properties_by_object_type` | Retrieves a list of properties for a specified CRM object type using the HubSpot API, allowing for optional filtering by archived status and specific properties. |
| `create_property_schema` | Creates a new custom property for a specified CRM object type. |
| `get_property_groups_by_object_type` | Retrieves a list of groups for a specified object type in the CRM using the "GET" method at the path "/crm/v3/properties/{objectType}/groups". |
| `create_property_group` | Creates a new property group for the specified CRM object type to organize related properties within HubSpot records. |
| `get_owner_by_id` | Retrieves detailed information about a specific CRM owner by their ID using the HubSpot API. |
| `batch_create_timeline_events` | Creates multiple timeline events in a batch using the provided event templates and returns a response with the created events. |
| `get_timeline_event_template_by_id` | Retrieves a specific event template by its ID for an application in HubSpot CRM, using the provided app ID and event template ID. |
| `update_timeline_event_template_by_id` | Updates an existing event template in the HubSpot CRM timeline for a specific app, using the provided event template ID and app ID, and returns a status message. |
| `delete_event_template_by_id` | Deletes an event template with the specified `eventTemplateId` associated with the application identified by `appId` in a CRM system, returning a successful response with no content upon completion. |
| `create_event` | Creates a new timeline event in a CRM record based on an event template, adding custom event information to the timeline of a contact, company, or deal. |
| `create_token_template` | Creates a new token for an event template in the HubSpot CRM timeline using the provided JSON data. |
| `update_event_template_token` | Updates a specific token in an event template within a CRM timeline using the provided JSON data. |
| `delete_timeline_event_template_token` | Deletes a token by the specified name from an event template in the CRM timeline for a given application ID. |
| `get_timeline_event_detail_by_id` | Retrieves detailed information for a specific timeline event identified by its event template ID and event ID in the CRM. |
| `get_timeline_event_by_id` | Retrieves a specific timeline event by its event template ID and event ID, returning detailed information about that event in the CRM. |
| `get_timeline_event_templates_by_app_id` | Retrieves a list of event templates for a specified app ID in the HubSpot CRM API. |
| `create_timeline_event_template` | Creates a new event template for a specified application ID in HubSpot's CRM timeline using the provided JSON payload. |
| `get_timeline_event_render` | Retrieves and renders a specific timeline event from a CRM object using an event template and event ID, allowing for optional detailed rendering. |
| `batch_read_contacts_post` | Retrieves a batch of contacts from the CRM using the provided identifiers and properties, supporting optional filtering by archived status. |
| `get_contact_by_id` | Retrieves a contact by ID from the CRM, allowing for optional filtering by properties, properties with history, associations, and archived status. |
| `delete_contact_by_id` | Deletes a contact by its ID from the CRM system, permanently removing all associated content in compliance with GDPR, and requires the "crm.objects.contacts.write" permission. |
| `update_contact_by_id` | Updates an individual contact by its record ID using a PATCH request to the "/crm/v3/objects/contacts/{contactId}" endpoint, requiring a JSON body with the fields to be updated. |
| `merge_contacts` | Merges two or more duplicate contact records into a single record in the CRM system, retaining the most relevant data while discarding redundant information. |
| `archive_contacts_batch_post` | Archives a batch of contacts by ID using the HubSpot CRM API, returning a "204 No Content" response upon success. |
| `create_contacts_batch` | Creates a batch of contacts in HubSpot using the CRM API, requiring a JSON payload and OAuth2 or private app authentication. |
| `batch_update_contacts` | Updates multiple contact records in a single request by providing their IDs or unique property values, overwriting specified properties in batch. |
| `delete_contact_gdpr_data` | Permanently deletes a contact and all associated data from the CRM to comply with GDPR requirements. |
| `get_contacts` | Retrieves a list of contacts from a CRM system, allowing for optional filtering by limit, pagination, specific properties, property history, associations, and archived status. |
| `create_contact` | Creates a new contact in the CRM system using the provided JSON data and returns a successful creation response. |
| `search_contacts_post` | Searches for contact records in the CRM system based on specified criteria and returns matching contacts. |
| `batch_read_feedback_submissions` | Reads a batch of feedback submissions by sending a POST request, allowing for optional filtering by archived status, and returns the relevant data in JSON format. |
| `get_feedback_submission_by_id` | Retrieves detailed information about a specific feedback submission using its ID, with optional parameters to include properties, history, associations, and archived status. |
| `delete_feedback_submission_by_id` | Deletes a specific feedback submission identified by the provided `feedbackSubmissionId` from the CRM system. |
| `patch_feedback_submission_by_id` | Updates specific fields of a feedback submission by ID using partial modifications with a JSON request body. |
| `merge_feedback_submissions` | Merges feedback submission records using the POST method, requiring a JSON body and supporting OAuth2 and private apps for authentication. |
| `archive_feedback_submissions_batch` | Archives a batch of feedback submissions by ID using the HubSpot API and returns a status response with a 204 status code upon successful completion. |
| `create_feedback_submissions_batch` | Creates a batch of feedback submissions using the HubSpot API, allowing for the simultaneous creation of multiple feedback submissions. |
| `update_feedback_submissions_batch` | Updates multiple feedback submissions in batches using the HubSpot CRM API. |
| `post_feedback_submissions_gdpr_delete` | Permanently deletes feedback submissions and associated data to comply with GDPR regulations using the provided JSON body. |
| `get_feedback_submissions` | Retrieves a list of feedback submissions from HubSpot CRM, allowing for optional filtering by limit, pagination, specific properties, property history, associations, and archived status. |
| `create_feedback_submission` | Searches for feedback submissions using the HubSpot CRM API and returns relevant results. |
| `search_feedback_submissions` | Searches for feedback submissions in HubSpot CRM using the POST method, allowing developers to filter and retrieve specific feedback data. |
| `read_batch_objects` | Performs a batch read operation on CRM objects of the specified type, allowing for the retrieval of multiple records in a single request, with optional filtering by archived status. |
| `get_object_details` | Retrieves a specific CRM object record by its object type and ID, allowing for optional specification of properties, associations, and other query parameters. |
| `delete_object_by_id` | Deletes a specified CRM object of the given type and ID using the DELETE method. |
| `patch_object_by_id` | Updates a specific CRM object using the PATCH method by modifying its properties based on the provided JSON body. |
| `merge_objects` | Merges duplicate records of a specified object type into a single record using the provided JSON body. |
| `archive_batch_objects_by_type` | Archives a batch of objects of a specified type in CRM using the POST method, requiring a JSON body and returning a 204 status code upon successful archiving. |
| `batch_create_object_records` | Creates multiple records of a specified object type in a CRM system using a single POST request, supporting batch creation and returning a status message based on the outcome. |
| `update_batch_object` | Updates multiple records of a specified object type in a CRM system using a batch operation via the POST method. |
| `gdpr_delete_object` | Permanently deletes an object of the specified type from the CRM, adhering to GDPR guidelines for data removal, using the "POST" method with the object type specified in the path and additional details in the request body. |
| `list_objects_by_type` | Retrieves a list of records for a specified CRM object type with optional filtering, pagination, property selection, association inclusion, and archived status. |
| `create_object_by_type` | Creates a new object of the specified type in a CRM system using the provided JSON data, returning a status message upon successful creation. |
| `search_objects_by_type_post` | Searches for objects of a specified type within a CRM using the provided JSON payload, filtering by various criteria to return a list of matching objects. |
| `get_video_conferencing_settings_by_app_id` | Retrieves the video conferencing settings for a specific application identified by the provided appId using the HubSpot API. |
| `update_video_conferencing_settings_by_app_id` | Updates video conferencing settings for a specific application identified by its `appId` using the provided JSON data. |
| `delete_video_conf_settings_by_app_id` | Deletes the video conferencing settings for the specified app identified by the appId. |
| `batch_read_tickets_post` | Retrieves and formats a batch of tickets from HubSpot CRM using a POST request to the "/crm/v3/objects/tickets/batch/read" endpoint. |
| `get_ticket_by_id` | Retrieves a specific ticket record by ID from the CRM, optionally including specified properties, property history, associations, and archived status. |
| `delete_ticket_by_id` | Deletes a ticket by its ID using the CRM API. |
| `update_ticket` | Updates an individual ticket by its ID using the HubSpot CRM API, allowing modification of specific fields via a JSON payload. |
| `merge_tickets` | Merges two or more tickets into a single ticket in the CRM system using the POST method, allowing for the consolidation of related customer service requests. |
| `archive_tickets_batch_post` | Archives a batch of tickets by ID using the HubSpot API and returns a status message. |
| `create_tickets_batch` | Creates a batch of tickets in the CRM using the HubSpot API and returns a status message. |
| `update_tickets_batch` | Updates multiple tickets in a single request using the HubSpot CRM API, returning a status message indicating the success or partial success of the operation. |
| `delete_ticket_gdpr` | Permanently deletes a ticket and associated data in compliance with GDPR guidelines using the POST method. |
| `get_tickets` | Retrieves a list of tickets from the CRM, allowing for filtering by limit, after cursor, specific properties, properties with history, associations, and archived status. |
| `create_ticket` | Creates a new ticket object in the CRM using the HubSpot API, allowing for the management of customer service requests. |
| `search_tickets_post` | Searches and filters ticket records within the CRM system based on specified criteria, returning matching ticket results. |
| `batch_read_line_items_post` | Retrieves a batch of line items by internal ID or unique property values using the HubSpot CRM API. |
| `get_line_item_by_id` | Retrieves a specific line item by its ID from the CRM, optionally including additional properties, associations, and history, using the CRM API with appropriate permissions. |
| `delete_line_item_by_id` | Deletes a line item from HubSpot CRM using its ID, requiring the "crm.objects.line_items.write" permission. |
| `patch_line_item_by_id` | Updates properties of a specific line item in the CRM system using a partial JSON patch request. |
| `merge_line_items_post` | Merges duplicate line items into a single instance using the specified parameters via the POST method. |
| `archive_line_items_batch_post` | Archives a batch of line items by their IDs in the CRM using a POST request. |
| `create_line_items_batch` | Creates a batch of line items using the HubSpot API and returns a status message upon successful creation. |
| `batch_update_line_items` | Updates a batch of line items using their internal IDs or unique property values via the POST method, requiring authentication with the "crm.objects.line_items.write" scope. |
| `gdpr_delete_line_items` | Deletes line item records from the CRM to comply with GDPR requirements, using the POST method with OAuth2 or private app authentication. |
| `list_line_items` | Retrieves a paginated list of line items with optional filters for properties, associations, and archival status in the CRM. |
| `create_line_item` | Creates a new line item in HubSpot CRM using the POST method, allowing you to add products or services to deals and quotes. |
| `search_line_items` | Searches and retrieves line items and their associated properties in the CRM based on specified filter criteria. |
| `get_crm_imports` | Retrieves a list of CRM import operations using the HubSpot API, allowing optional filtering by date and limit on the number of results returned. |
| `create_crm_import` | Imports data into a HubSpot CRM using a POST request with a multipart/form-data payload, allowing bulk creation or update of records via uploaded files such as CSV or Excel. |
| `get_owners_list` | Retrieves a list of CRM owners using the "GET" method, allowing optional filtering by email, pagination, and archived status, and returns a response with owner details. |
| `get_association_types_by_object_types` | Retrieves the association types between two specified object types in HubSpot CRM using the "GET" method. |
| `get_marketing_campaigns` | Retrieves a list of marketing campaigns with optional filtering by name, sorting, and limiting results. |
| `create_marketing_campaigns` | Creates a new marketing campaign using the provided JSON data and returns a status message upon successful creation. |
| `batch_read_campaigns_post` | Retrieves a batch of campaign data from the marketing API, filtering by optional start and end dates and specifying properties to include, using JSON-formatted request body. |
| `update_campaigns_batch` | Updates multiple marketing campaigns in a batch using the POST method, requiring a JSON body and authentication via OAuth2 or private apps with "marketing.campaigns.read" permissions. |
| `get_campaign_metrics` | Retrieves campaign metrics for a specified campaign GUID, optionally filtering by start and end dates. |
| `get_campaign_asset_by_type` | Retrieves assets of a specified type for a given marketing campaign, supporting optional filtering by date range and pagination. |
| `archive_campaigns_batch` | Archives a batch of marketing campaigns using the HubSpot API, requiring a JSON request body and returning a 204 status upon successful completion. |
| `update_campaign_asset` | Updates a specific asset of a given type within a marketing campaign identified by campaignGuid. |
| `delete_campaign_asset_by_id` | Deletes a specific asset from a marketing campaign using the provided campaign GUID, asset type, and asset ID. |
| `get_campaign_revenue_report` | Retrieves revenue reports for a specific marketing campaign using the provided campaign GUID, with optional filtering by attribution model and date range. |
| `create_campaigns_batch` | Creates multiple marketing campaigns in a single operation using the "POST" method, accepting a JSON body with campaign details and returning a status message upon successful creation. |
| `get_campaign_budget_totals` | Retrieves the total budget details for a marketing campaign using the campaign's GUID. |
| `get_campaign_by_guid` | Retrieves detailed information about a specific marketing campaign identified by its campaignGuid, optionally filtered by date range and selected properties. |
| `delete_campaign_by_guid` | Deletes a marketing campaign using the provided campaign GUID and returns a 204 No Content response. |
| `patch_campaign_by_guid` | Updates specified properties of a marketing campaign identified by the campaignGuid using a JSON patch document. |
| `get_campaign_contacts_report_by_type` | Retrieves a report of contacts of a specified type for a marketing campaign, allowing optional filtering by start and end dates and pagination. |
| `list_email_statistics` | Retrieves email statistics for a specified time range and optional email IDs and properties using the GET method. |
| `create_ab_test_email_variation` | Creates a variation for an A/B test email using the POST method and returns a successful creation status. |
| `get_email_statistics_histogram` | Retrieves histogram statistics for marketing emails filtered by optional parameters such as interval, time range, and specific email IDs. |
| `get_email_ab_test_variation` | Retrieves the variation for an A/B test associated with a specific email by its ID using the GET method. |
| `reset_email_draft_by_id` | Resets the draft status of an email using the specified email ID. |
| `restore_email_revision_to_draft` | Restores a specified email revision to draft status by email ID and revision ID. |
| `get_email_draft_by_id` | Retrieves the draft of an email with the specified `{emailId}` using the marketing API. |
| `update_email_draft_by_id` | Updates a draft email identified by the specified emailId using the provided JSON data. |
| `get_email_revisions` | Get a list of revisions for a specified marketing email, optionally filtered by date range and limited in number. |
| `get_email_revision_by_id` | Retrieves a specific revision of an email identified by the provided email ID and revision ID using the GET method. |
| `clone_email` | Clones a marketing email using the POST method at the "/marketing/v3/emails/clone" endpoint, creating a duplicate email with the same properties as the original but with a unique ID. |
| `list_marketing_emails` | Retrieves a list of marketing emails with optional filtering, sorting, pagination, and inclusion of statistics. |
| `create_email_marketing_campaign` | Creates a new email resource in the marketing system using the provided JSON data and returns a success response upon creation. |
| `restore_email_revision` | Restores a specific email revision using the provided email ID and revision ID via the POST method. |
| `get_email_by_id_marketing` | Retrieves detailed information about a specific email by its ID, optionally including statistics, selected properties, and archived status. |
| `delete_email_by_id_marketing` | Deletes the specified marketing email by its emailId, optionally archiving it, and returns a 204 No Content status on success. |
| `patch_email_by_id` | Updates an email resource identified by `{emailId}` with partial modifications using JSON in the request body and optionally sets its archived status. |
