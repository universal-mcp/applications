# KlaviyoApp MCP Server

An MCP Server for the KlaviyoApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the KlaviyoApp API.


| Tool | Description |
|------|-------------|
| `create_client_review` | Creates a new client review, requiring a company ID as a query parameter and a revision in the request header. |
| `get_accounts` | Retrieves account information using the GET method, allowing optional filtering by specific account fields and requiring a revision header, returning a successful response with the requested data if available. |
| `get_account` | Retrieves detailed information about a specific account identified by `{id}` with optional filtering by `fields[account]` and version control via the `revision` header. |
| `get_campaigns` | Retrieve a list of campaigns using optional filtering, sorting, and inclusion parameters, with the option to specify fields for campaign messages, campaigns, and tags. |
| `create_campaign` | Creates a new campaign using specified parameters, returning appropriate status codes for success (201), client errors (400), or server issues (500). |
| `get_campaign` | Retrieves detailed information about a campaign by its ID, allowing for selective field inclusion and revision specification through query parameters and headers. |
| `delete_campaign` | Deletes a specific campaign by its ID, requiring a revision header and returning 204 No Content on success, with 400 and 500 for client and server errors, respectively. |
| `update_campaign` | The **PATCH** operation at **"/api/campaigns/{id}"** partially updates a campaign resource identified by `{id}`, with the revision specified in the header, returning a successful response if the update is applied correctly. |
| `get_campaign_recipient_estimation` | Retrieves a campaign recipient estimation by ID with optional fields filtering via query parameters and revision tracking through headers. |
| `create_campaign_clone` | Clones a campaign, accepting a revision header and returning appropriate status codes (201 Created, 400 Bad Request, 500 Internal Server Error). |
| `get_tags_for_campaign` | This API operation retrieves tags for a campaign by ID using the GET method, allowing optional filtering by specific fields and versioning through a revision header. |
| `get_tag_ids_for_campaign` | This API operation retrieves the relationships between a campaign, identified by its ID, and associated tags, returning the relevant tag information. |
| `get_messages_for_campaign` | Retrieves campaign messages associated with a specific campaign ID, allowing optional field selection and resource inclusion via query parameters, with support for header-based versioning. |
| `get_message_ids_for_campaign` | Retrieves the relationships between the specified campaign and its associated messages using the "revision" header parameter for versioning. |
| `get_campaign_message` | This API operation uses the "GET" method to retrieve a campaign message by its ID, allowing for customizable field selection via query parameters and revision specification in the header. |
| `update_campaign_message` | The **PATCH** operation at "/api/campaign-messages/{id}" partially updates a campaign message by applying specified changes, using a revision header to ensure data consistency. |
| `assign_template_to_campaign_message` | Creates a new campaign message template assignment, requiring a revision header parameter, returning HTTP 201 on success or 400/500 for client/server errors. |
| `get_campaign_for_campaign_message` | Retrieves the campaign associated with a specific campaign message ID, optionally filtering returned campaign fields via query parameter and supporting revision tracking via header. |
| `get_campaign_id_for_campaign_message` | Retrieves the relationship between a campaign message and its associated campaign by making a GET request to the "/api/campaign-messages/{id}/relationships/campaign" endpoint, optionally specifying a revision in the header. |
| `get_template_for_campaign_message` | Retrieves the template details for a campaign message specified by the provided ID, allowing optional filtering of response fields and specifying a revision via the header. |
| `get_template_id_for_campaign_message` | Retrieves the template relationship associated with a specific campaign message, identified by its ID, with an optional revision header parameter for version control. |
| `get_image_for_campaign_message` | Retrieves the image associated with a campaign message by ID, allowing optional filtering by image fields and specifying a revision in the request header. |
| `get_image_id_for_campaign_message` | Retrieves the image relationship for a campaign message with the specified ID, optionally filtered by a header revision parameter. |
| `update_image_for_campaign_message` | Updates the image relationship for a campaign message by replacing the existing related image with a new one using the provided revision for concurrency control. |
| `get_campaign_send_job` | Retrieves a specific campaign send job by ID, supporting optional query parameters for field selection and header-based revision control. |
| `cancel_campaign_send` | The **PATCH** operation at path "/api/campaign-send-jobs/{id}" partially updates a campaign send job by applying specific changes, requiring a revision in the header, and returns a successful response without content if modified successfully (204), or error codes for invalid requests (400) or server errors (500). |
| `get_campaign_recipient_estimation_job` | Retrieves details of a specific campaign recipient estimation job by its ID with optional field selection and revision header. |
| `send_campaign` | Submits a campaign send job for asynchronous processing of a message dispatch, with a required API version header parameter. |
| `refresh_campaign_recipient_estimation` | Submits a request to create and initiate a campaign recipient estimation job, requiring a revision header and returning 202 Accepted, 400 Bad Request, or 500 Internal Server Error responses. |
| `get_catalog_items` | This API operation retrieves a list of catalog items, allowing for customizable fields, filtering, sorting, and pagination, with optional inclusion of related resources and version control through a revision header. |
| `create_catalog_item` | Creates a new catalog item entry with optional revision control through header parameters, returning success (201), client error (400), or server error (500) status codes. |
| `get_catalog_item` | The **GET /api/catalog-items/{id}** operation retrieves a specific catalog item by its ID, allowing for customizable field selection via query parameters and inclusion of additional resources, while requiring revision information in the header. |
| `delete_catalog_item` | Deletes a catalog item by its ID, requiring a revision parameter in the header, and returns a successful response with a 204 status if the operation is completed without issues. |
| `update_catalog_item` | Updates a catalog item by its ID with partial modifications, requiring a revision header and returning success (200), bad request (400), or server error (500) status codes. |
| `get_bulk_create_catalog_items_jobs` | The "/api/catalog-item-bulk-create-jobs" API operation using the "GET" method retrieves a list of catalog item bulk create jobs, allowing for filtering, pagination, and customization of returned fields based on provided parameters. |
| `bulk_create_catalog_items` | Submits a request to create multiple catalog items asynchronously via bulk processing. |
| `get_bulk_create_catalog_items_job` | This API operation retrieves a catalog item bulk creation job by its ID, allowing optional fields and included resources to be specified for detailed job information. |
| `get_bulk_update_catalog_items_jobs` | Retrieves a list of catalog item bulk update jobs with optional filtering, cursor-based pagination, and field selection. |
| `bulk_update_catalog_items` | Creates a bulk update job for catalog items, accepting header-based revision control and returning asynchronous responses including 202 Accepted, 400 Bad Request, and 500 Internal Server Error status codes. |
| `get_bulk_update_catalog_items_job` | Retrieves the status and details of a specific catalog item bulk update job, including optional related items and field filtering via query parameters. |
| `get_bulk_delete_catalog_items_jobs` | Retrieves a list of catalog item bulk delete jobs with optional field filtering, pagination, and revision header support. |
| `bulk_delete_catalog_items` | Creates a bulk delete job for catalog items with a specified revision header, returning 202 on success, 400 for bad requests, or 500 for server errors. |
| `get_bulk_delete_catalog_items_job` | Retrieve a catalog item bulk delete job by its job ID, allowing for the inspection of job details such as status and progress, with optional filtering of returned fields and specification of a revision. |
| `get_items_for_catalog_category` | Retrieve a list of items within a specified catalog category by ID, allowing optional filtering, sorting, and inclusion of additional details. |
| `get_category_ids_for_catalog_item` | The API operation at path "/api/catalog-items/{id}/relationships/categories" using the "GET" method retrieves the category relationships for a specific catalog item identified by its ID, allowing filtering, pagination, and sorting of the results, with optional revision specification in the header. |
| `add_categories_to_catalog_item` | Adds a relationship between the specified catalog item and one or more categories using the provided revision header. |
| `remove_categories_from_catalog_item` | Deletes a relationship between a catalog item, identified by `{id}`, and its categories, requiring a revision provided in the header for validation. |
| `update_categories_for_catalog_item` | This API operation updates the categories relationship for a catalog item by applying partial modifications using the PATCH method, requiring a revision header to ensure data consistency. |
| `get_catalog_variants` | Retrieves all catalog variants with optional filtering, sorting, pagination, and field selection parameters. |
| `create_catalog_variant` | Creates a new catalog variant with the provided data, requiring a revision header and returning status codes for success (201), client errors (400), and server errors (500). |
| `get_catalog_variant` | Retrieves a catalog variant by ID with optional field filtering and revision header support. |
| `delete_catalog_variant` | Deletes a catalog variant by its ID using a specified header revision, returning status codes for success (204), client error (400), or server error (500). |
| `update_catalog_variant` | Updates a catalog variant's partial data using a revision header and returns the updated result upon success. |
| `get_create_variants_jobs` | Retrieves a catalog variant bulk create job by ID, supporting optional filtering, pagination, and field selection in the response. |
| `bulk_create_catalog_variants` | The **POST /api/catalog-variant-bulk-create-jobs** operation creates a job to bulk create catalog variants, accepting up to 100 variants per request, with a required "revision" header for versioning. |
| `get_create_variants_job` | Retrieve details of a specific catalog variant bulk creation job by its ID, supporting optional field selection, inclusion of related resources, and requiring a revision header. |
| `get_update_variants_jobs` | The **GET** operation at "/api/catalog-variant-bulk-update-jobs" retrieves a list of catalog variant bulk update jobs, allowing users to filter results by specific fields and pagination options. |
| `bulk_update_catalog_variants` | Creates a catalog variant bulk update job to process batch updates for multiple product variants. |
| `get_update_variants_job` | The API operation defined at path "/api/catalog-variant-bulk-update-jobs/{job_id}" using the "GET" method retrieves details about a specific catalog variant bulk update job, allowing optional specification of fields to include and related objects. |
| `get_delete_variants_jobs` | The API operation at path "/api/catalog-variant-bulk-delete-jobs" using the "GET" method retrieves information about catalog variant bulk delete jobs, allowing filtering and pagination, and providing specific fields of the job based on query parameters. |
| `bulk_delete_catalog_variants` | Creates a bulk delete job for catalog variants, accepting up to 100 variants per request, with header parameter "revision" and returning 202, 400, or 500 status codes. |
| `get_delete_variants_job` | Retrieve a specific catalog variant bulk delete job's status and details by its job ID, supporting optional field filtering via query parameters and API version control through headers. |
| `get_variants_for_catalog_item` | Retrieves a catalog item's variants with optional filtering, sorting, pagination, and field selection. |
| `get_variant_ids_for_catalog_item` | Retrieves variant relationships for a catalog item with optional filtering, pagination, and sorting parameters. |
| `get_catalog_categories` | The "/api/catalog-categories" API operation using the "GET" method retrieves a list of catalog categories, allowing filtering, sorting, and pagination through query parameters, while also supporting revision specification via a header. |
| `create_catalog_category` | Creates a new catalog category using specified parameters, returning a 201 status code on successful creation. |
| `get_catalog_category` | Retrieves a specific catalog category by ID with optional field selection and revision header. |
| `delete_catalog_category` | Deletes a catalog category identified by its ID, accepting an optional revision header, and returns a successful response with a 204 status code if executed correctly. |
| `update_catalog_category` | Patches a catalog category with the specified ID, allowing partial updates while requiring a revision header for version control. |
| `get_create_categories_jobs` | Retrieves a list of catalog category bulk creation jobs with support for filtering, field selection, pagination via cursor, and revision headers. |
| `bulk_create_catalog_categories` | Create bulk jobs for catalog category creation, tracking progress via asynchronous processing. |
| `get_create_categories_job` | The **`GET /api/catalog-category-bulk-create-jobs/{job_id}`** operation retrieves a specific catalog category bulk create job by its job ID, optionally including related resources such as categories based on the provided query parameters. |
| `get_update_categories_jobs` | The API operation at "/api/catalog-category-bulk-update-jobs" using the "GET" method retrieves details of catalog category bulk update jobs, allowing for customization through query parameters such as fields, filters, and pagination, while also accepting a revision header. |
| `bulk_update_catalog_categories` | This API operation initiates a bulk update job for catalog categories, allowing for the modification of multiple categories simultaneously, with an optional revision header for version control. |
| `get_update_categories_job` | Retrieve the status and details of a specific catalog category bulk update job by its ID, supporting optional inclusion of related resources and field filtering. |
| `get_delete_categories_jobs` | Retrieves a list of catalog category bulk delete jobs based on specified fields, filters, and pagination, with an optional revision header. |
| `bulk_delete_catalog_categories` | Creates a catalog category bulk delete job to delete a batch of categories, accepting up to 100 per request and requiring a revision header. |
| `get_delete_categories_job` | Retrieves the status and details of a specific catalog category bulk delete job using the provided job ID, with optional field filtering and API version control. |
| `get_item_ids_for_catalog_category` | Retrieves a list of items related to a specific catalog category with options to filter, sort, and paginate the results. |
| `add_items_to_catalog_category` | This API operation creates a new relationship between a specified catalog category and items using the POST method, requiring a revision header, and returns a 204 No Content response upon success. |
| `remove_items_from_catalog_category` | Deletes the relationship between a catalog category and its associated items, identified by the category ID provided in the path, and returns a successful response with no content upon completion. |
| `update_items_for_catalog_category` | This API operation updates the items relationship of a catalog category with the specified ID using the PATCH method, requiring a revision header to ensure atomic updates, and returns a 204 No Content response upon success. |
| `get_categories_for_catalog_item` | Retrieves categories associated with a catalog item by ID, allowing for query customization via fields, filters, pagination, sorting, and revision specification. |
| `create_back_in_stock_subscription` | The POST operation at the "/api/back-in-stock-subscriptions" path creates a new back-in-stock subscription, requiring a "revision" header, and returns a 202 response upon success or error responses for bad requests or internal server errors. |
| `create_client_subscription` | Creates a subscription for a client, requiring a company_id query parameter and revision header while returning a 202 Accepted status upon successful request. |
| `create_or_update_client_push_token` | Registers a push token for a client by sending a POST request to "/client/push-tokens," which requires a "company_id" query parameter and a "revision" header, returning a 202 status on success. |
| `unregister_client_push_token` | Unregisters a client's push token by accepting a company ID as a query parameter and requiring a revision header, returning status codes for successful acceptance (202), client errors (400), or server errors (500). |
| `create_client_event` | Creates an event for a client by submitting the event details via the POST method, requiring a `company_id` query parameter and a `revision` header. |
| `create_or_update_client_profile` | Creates client profiles with required company_id in query parameters and revision header, returning status codes for accepted (202), bad request (400), and server error (500). |
| `bulk_create_client_events` | Creates multiple client events in bulk using a POST request, requiring a company ID as a query parameter and a revision in the request header. |
| `create_client_back_in_stock_subscription` | Subscribe a customer to receive back-in-stock notifications for a product via POST request, requiring company ID and revision header, with responses indicating acceptance (202), invalid parameters (400), or server errors (500). |
| `get_coupons` | The API operation at "/api/coupons" using the "GET" method retrieves coupon data based on optional query parameters for selecting fields and pagination, with an additional header option for specifying the revision. |
| `create_coupon` | Creates a new coupon with a specified revision, returning a successful creation response or error messages for invalid requests or internal server errors. |
| `get_coupon` | This API operation, located at `/api/coupons/{id}`, uses the GET method to retrieve details of a specific coupon based on its ID, allowing optional filtering by specifying coupon fields in the query and providing a revision in the headers. |
| `delete_coupon` | Deletes a coupon by ID, returning a 204 status code on success, and requires a revision header; error responses include 400 for invalid requests and 500 for server errors. |
| `update_coupon` | Updates partial coupon data using the specified revision header, returning 200 for success, 400 for invalid requests, or 500 for errors. |
| `get_coupon_codes` | This API operation retrieves a list of coupon codes using the GET method at the "/api/coupon-codes" path, supporting filters and pagination through query parameters such as fields, filter, include, and page cursor, with a required revision header. |
| `create_coupon_code` | Create a new coupon code by sending a POST request to "/api/coupon-codes", optionally specifying a revision in the request headers. |
| `get_coupon_code` | Retrieves details of a coupon code by ID, allowing optional specification of fields to include and related resources via query parameters. |
| `delete_coupon_code` | Deletes a coupon code with the specified ID, returning a 204 No Content response upon successful deletion, with optional revision information provided in the request headers. |
| `update_coupon_code` | Updates a coupon code's properties using a partial modification request, supporting conditional updates via the revision header. |
| `get_bulk_create_coupon_code_jobs` | Retrieves a list of bulk coupon code creation jobs, allowing for filtering, pagination, and specification of fields to include in the response. |
| `bulk_create_coupon_codes` | This API operation creates bulk jobs for coupon code creation via a POST request to the "/api/coupon-code-bulk-create-jobs" endpoint, requiring a revision header, and returns success with a 202 status code or error responses for bad requests (400) and internal server errors (500). |
| `get_bulk_create_coupon_codes_job` | Retrieves information about a specific coupon code bulk create job by ID, allowing optional filtering of fields and inclusion of related data. |
| `get_coupon_for_coupon_code` | This API operation retrieves a coupon associated with a specific coupon code by its ID, allowing optional filtering of coupon fields and specifying a revision via header. |
| `get_coupon_id_for_coupon_code` | Retrieves the relationship details of a specific coupon code identified by its ID. |
| `get_coupon_codes_for_coupon` | Retrieves coupon codes associated with a specific coupon ID, supporting optional filtering, field selection, and pagination via cursor-based navigation. |
| `get_coupon_code_ids_for_coupon` | This API operation retrieves the relationships between a coupon and its associated coupon codes, allowing for filtering and pagination with optional revision information provided in the request header. |
| `request_profile_deletion` | Initiates an asynchronous data privacy deletion job with optional revision control via header parameter. |
| `get_events` | Retrieves a filtered list of events with customizable fields, pagination, sorting, and related resources. |
| `create_event` | Create a new event by sending a POST request to the `/api/events` endpoint, which includes a `revision` header and returns success with a 202 status code, or error responses for bad requests (400) or internal server errors (500). |
| `get_event` | Retrieves a specific event by its ID, with optional filtering for fields and inclusion of related data. |
| `bulk_create_events` | Creates a batch of events asynchronously via a bulk job with a version-controlled header (revision) and returns status codes for acceptance (202), invalid requests (400), or server errors (500). |
| `get_metric_for_event` | This API operation retrieves event metric details by ID using a GET request to "/api/events/{id}/metric," allowing specification of metric fields via query parameters and requiring a revision header. |
| `get_metric_id_for_event` | This API operation retrieves a specific relationship between an event and a metric by ID using a GET request to the "/api/events/{id}/relationships/metric" path, with the ability to specify a revision via a header parameter. |
| `get_profile_for_event` | This API operation retrieves a profile associated with a specific event by its ID, allowing optional specification of additional fields and profile fields, while also accepting a revision header. |
| `get_profile_id_for_event` | Retrieves the profile relationship data for the specified event ID. |
| `get_flows` | Retrieves flows with optional query parameters for field filtering, pagination, sorting, and inclusion of related resources, supporting cursor-based pagination and custom header-based revision tracking. |
| `create_flow` | Creates a new flow resource, supporting optional query parameters for additional flow fields and header-based revision tracking, returning HTTP 201 on success. |
| `get_flow` | Retrieves a flow by ID with optional filtering by additional fields, flow actions, flow details, tags, and includes, using a specified revision from the header. |
| `delete_flow` | Deletes the flow with the specified ID, requiring a revision header, and returns a 204 (No Content) on success, with 400 and 500 codes for client errors and server failures. |
| `update_flow_status` | Updates a specific flow by ID using partial modifications, requiring a revision header. |
| `get_flow_action` | Retrieves a specific flow action by ID, optionally including additional fields and related resources, with support for revision tracking via a header. |
| `get_flow_message` | Retrieves a specific flow message by ID with optional filtering (fields selection) and related resource inclusion (include parameter). |
| `get_actions_for_flow` | Retrieves flow actions for a specific flow with filtering, pagination, and field selection capabilities. |
| `get_action_ids_for_flow` | The API operation at "/api/flows/{id}/relationships/flow-actions" using the "GET" method retrieves relationships associated with flow actions for a specific flow ID, allowing filtering, pagination, and sorting of results. |
| `get_tags_for_flow` | Retrieves the tags associated with a specific flow identified by its ID, allowing optional filtering of tag fields and requiring a revision header. |
| `get_tag_ids_for_flow` | Retrieves the tag relationships associated with a specific flow ID, requiring a revision header parameter, and returns success (200), client error (400), or server error (500) responses. |
| `get_flow_for_flow_action` | Retrieves the flow details associated with a specific flow action by ID, allowing optional filtering of flow fields and specifying a revision via headers. |
| `get_flow_id_for_flow_action` | Retrieves relationships for a specific flow action identified by `{id}`, requiring a `revision` header and returning responses for successful retrieval, bad requests, or server errors. |
| `get_messages_for_flow_action` | This API operation, accessible via GET method at the "/api/flow-actions/{id}/flow-messages" path, retrieves flow messages associated with a specific flow action identified by "id," allowing customization through query parameters for fields, filtering, pagination, and sorting, with additional revision details provided in the header. |
| `get_message_ids_for_flow_action` | Retrieves a list of flow messages associated with the specified flow action, supporting pagination, filtering, sorting, and optional revision header. |
| `get_action_for_flow_message` | Retrieves a flow action for a specific flow message by ID, allowing optional filtering by fields and revision, returning a successful response or error codes for bad requests or server errors. |
| `get_action_id_for_flow_message` | Retrieves the relationships between a flow message, identified by `{id}`, and a flow action, allowing for the inspection of how flow messages are associated with actions, with optional revision filtering via the `revision` header. |
| `get_template_for_flow_message` | The `/api/flow-messages/{id}/template` operation retrieves a template for a flow message by its ID using the GET method, allowing optional filtering of template fields via query parameters and specifying revisions through headers. |
| `get_template_id_for_flow_message` | Retrieves the relationship details associated with a template for a specific flow message, identified by `{id}`, with optional filtering by revision specified in the header. |
| `get_forms` | The "GET /api/forms" operation retrieves a list of forms based on provided query parameters such as fields, filters, pagination, and sorting, with an optional revision header, returning a successful response with a 200 status code. |
| `get_form` | Retrieves a specific form using its ID, supporting optional query parameters for field filtering, includes, and a revision header. |
| `get_form_version` | Retrieves a specific form version by ID using the GET method, allowing optional filtering by form-version fields and revision headers. |
| `get_versions_for_form` | Retrieves paginated form versions for a specific form with filtering, sorting, field selection, and pagination options. |
| `get_version_ids_for_form` | This API operation retrieves the relationships between a form and its versions via a GET request to "/api/forms/{id}/relationships/form-versions," allowing filtering, pagination, and sorting of results. |
| `get_form_for_form_version` | Retrieves the specified form version's form details, with optional field filtering via `fields[form]` query parameter and revision tracking via `revision` header. |
| `get_form_id_for_form_version` | Retrieves the relationship details of a specified form version by its ID using the provided revision header. |
| `get_images` | The **GET /api/images** operation retrieves image resources based on optional query parameters for filtering, pagination, sorting, and specific fields, with the option to include a revision header. |
| `upload_image_from_url` | Creates a new image resource with the specified revision, returning a successful creation response if valid, or error responses for invalid requests or server issues. |
| `get_image` | Retrieves a specific image by ID, allowing optional query parameter "fields[image]" and a required revision header, returning data if successful or error responses for bad requests or internal server errors. |
| `update_image` | The PATCH method at "/api/images/{id}" allows for partial updates of an image resource by specifying changes in the request body, with the revision tracked via a header parameter. |
| `get_lists` | The API operation at "/api/lists" using the "GET" method retrieves a list of items based on specified query parameters for fields, filters, sorting, and pagination, with optional headers for revision control. |
| `create_list` | The POST operation at "/api/lists" creates a new list resource, returning a 201 status upon success, and accepts a `revision` parameter in the request header. |
| `get_list` | Retrieves a specific list by ID with customizable response fields, optional related resources to include, and support for specifying data revisions via headers. |
| `delete_list` | Deletes the specified list by ID when the correct revision header is provided, returning HTTP 204 for successful deletion, or 400/500 for invalid requests or server errors. |
| `update_list` | Updates a list resource partially by applying modifications to the specified fields at the path "/api/lists/{id}", requiring a revision header for concurrent version control. |
| `get_tags_for_list` | This API operation retrieves the tags associated with a list specified by its ID, allowing optional filtering of specific fields and revision information via query and header parameters, respectively. |
| `get_tag_ids_for_list` | Retrieves the relationships between a specified list and its associated tags. |
| `get_profiles_for_list` | Retrieves a list of profiles associated with the specified list ID, allowing optional filtering, sorting, and pagination, with customizable fields and revision tracking. |
| `get_profile_ids_for_list` | This API operation retrieves the profiles related to a list identified by `{id}`, allowing for filtering, pagination, sorting, and revision specification via query parameters and headers. |
| `add_profiles_to_list` | Creates a relationship between a specified list and one or more profiles using a POST request with an optional revision header, returning a 204 on success, 400 for client errors, and 500 for server errors. |
| `remove_profiles_from_list` | Deletes the relationship between the specified list and associated profiles using a revision header, returning status codes for success, bad request, and server errors. |
| `get_flows_triggered_by_list` | Retrieves flow triggers for a specific list by ID, supporting optional filtering by flow fields and specifying a revision in the request header. |
| `get_ids_for_flows_triggered_by_list` | Retrieves the flow triggers associated with a specific list using the provided ID, including revision header parameter, and returns status codes for success (200), client errors (400), or server issues (500). |
| `get_metrics` | Retrieves paginated metrics data with optional field filtering, resource inclusion, and cursor-based pagination, requiring a revision header. |
| `get_metric` | Retrieves specific metric data by ID, allowing optional filtering by flow and metric fields, inclusion of additional data, and specification of a revision via a header. |
| `get_metric_property` | Retrieves a metric property by ID, allowing optional filtering of fields and inclusion of additional data through query parameters, with support for revision specification via a header. |
| `query_metric_aggregates` | Posts a request to the "/api/metric-aggregates" endpoint, requiring a "revision" header, to aggregate metrics, returning a successful response if valid or error responses for bad requests or server errors. |
| `get_flows_triggered_by_metric` | Retrieves flow trigger details for a specified metric ID, supporting filtering via query parameters and optional header-based versioning. |
| `get_ids_for_flows_triggered_by_metric` | This API operation retrieves the flow triggers associated with a specific metric identified by `{id}`, allowing for the inspection of triggers configured for that metric. |
| `get_properties_for_metric` | Retrieves properties of a specific metric by ID, supporting query-based field filtering and custom headers for revision management. |
| `get_property_ids_for_metric` | Retrieves the relationships of metric properties associated with a specific metric by ID, with the option to specify a revision via the request header. |
| `get_metric_for_metric_property` | Retrieves a specific metric property by ID, allowing filtering via query parameters and supporting revision headers for conditional requests. |
| `get_metric_id_for_metric_property` | Retrieves the relationships of a metric property identified by {id} through the "GET" method, supporting a "revision" header parameter with response codes indicating success (200), client errors (400), and server errors (500). |
| `get_profiles` | Retrieves profiles with support for field filtering, pagination, sorting, and custom filtering via query parameters. |
| `create_profile` | Creates a new profile with additional fields passed via query parameters and custom header for revision control, returning success (201), client error (400), or server error (500) status codes. |
| `get_profile` | Retrieves a specific profile by ID with customizable field selection through query parameters for enhanced data filtering. |
| `update_profile` | Updates specific fields of a profile identified by {id} using a partial payload, with optional query parameters for additional fields and a revision header for concurrency control. |
| `get_bulk_suppress_profiles_jobs` | The GET operation at the "/api/profile-suppression-bulk-create-jobs" path retrieves a list of bulk profile suppression jobs, allowing for filtering, sorting, and pagination of the results through query parameters. |
| `bulk_suppress_profiles` | Creates a bulk suppression job for profiles to prevent email communication via the Klaviyo API. |
| `get_bulk_suppress_profiles_job` | Retrieve the status and details of a bulk profile suppression job by its ID, including optional field filtering and revision header support. |
| `get_bulk_unsuppress_profiles_jobs` | Retrieves a paginated list of bulk profile suppression deletion jobs with optional filtering, sorting, and field selection. |
| `bulk_unsuppress_profiles` | Creates a bulk job to suppress and/or delete profiles asynchronously, returning a 202 Accepted status upon successful initiation. |
| `get_bulk_unsuppress_profiles_job` | Retrieves the status and details of a bulk profile suppression deletion job using specified query fields and header revision. |
| `create_or_update_profile` | The "POST /api/profile-import" operation imports profiles, accepting optional query parameters like "additional-fields[profile]" and requiring a "revision" header, with responses indicating success (200 or 201), bad requests (400), or internal server errors (500). |
| `merge_profiles` | The API operation at "/api/profile-merge" using the "POST" method merges user profiles, integrating data from a source profile into a destination profile, with the source profile being deleted upon successful completion, and requires a revision header for version control. |
| `create_or_update_push_token` | This API operation creates a new resource by posting to the "/api/push-tokens" endpoint, accepting a revision parameter in the request header, and returns a 202 response upon successful creation, with error responses for invalid requests or server errors. |
| `get_lists_for_profile` | This API operation retrieves a list associated with a specific profile identified by `{id}`, allowing optional filtering of fields via the `fields[list]` query parameter and specifying a revision via the `revision` header. |
| `get_list_ids_for_profile` | Retrieves the lists associated with a specified profile ID via header-based version control. |
| `get_segments_for_profile` | This API operation retrieves profile segment information for a specified profile ID, allowing for the selection of specific segment fields via query parameters and the specification of a revision in the request header. |
| `get_segment_ids_for_profile` | Retrieves the associated segments of a specific profile, requiring a revision header, and returns a 200 status on success with potential 400 or 500 error responses. |
| `get_bulk_import_profiles_jobs` | The GET operation on `/api/profile-bulk-import-jobs` retrieves and filters paginated bulk profile import job records with customizable sorting, field selection, and cursor-based pagination. |
| `bulk_import_profiles` | The POST operation at "/api/profile-bulk-import-jobs" creates a new bulk profile import job, allowing for the creation or update of multiple profiles, with a revision specified in the header. |
| `get_bulk_import_profiles_job` | Retrieves the status and details of a specific bulk profile import job, including optional field selection and resource inclusion via query parameters. |
| `get_list_for_bulk_import_profiles_job` | Retrieves profile lists associated with a specific bulk import job ID, allowing field filtering via query parameters and including a revision header. |
| `get_list_ids_for_bulk_import_profiles_job` | This API operation retrieves the relationships between a specific bulk profile import job and its associated lists, allowing the caller to fetch related list data using a GET request on the "/api/profile-bulk-import-jobs/{id}/relationships/lists" endpoint. |
| `get_profiles_for_bulk_import_profiles_job` | The API operation defined at path "/api/profile-bulk-import-jobs/{id}/profiles" using the "GET" method retrieves a list of profiles associated with a specific bulk import job, allowing for pagination and customization of returned fields. |
| `get_profile_ids_for_bulk_import_profiles_job` | Retrieves a paginated list of profile relationships associated with a specific bulk import job using cursor-based pagination query parameters. |
| `get_errors_for_bulk_import_profiles_job` | Retrieves a paginated list of import errors for a specific bulk import job, supporting optional filtering and pagination parameters. |
| `bulk_subscribe_profiles` | Subscribes one or more profiles to email/SMS marketing lists in bulk, handling consent and double opt-in where applicable. |
| `bulk_unsubscribe_profiles` | Initiates a bulk unsubscribe job to remove multiple profiles from email subscriptions asynchronously. |
| `query_campaign_values` | Creates a campaign values report, accepting a page cursor as a query parameter and a revision in the request header, returning data if successful. |
| `query_flow_values` | This API operation, using the POST method at "/api/flow-values-reports", allows users to generate reports by providing a page cursor in the query and a revision in the header, with potential responses indicating success (200) or error conditions (400, 500). |
| `query_flow_series` | This API operation at "/api/flow-series-reports" utilizes the POST method to create a flow series report, allowing clients to specify pagination with the "page_cursor" query parameter and specify a revision via the "revision" header, with responses for successful execution (200), bad request (400), and internal server error (500). |
| `query_form_values` | Submits form values report data with a specified revision header. |
| `query_form_series` | This API operation, exposed at the "/api/form-series-reports" path using the "POST" method, allows users to generate or submit form series reports, specifying a revision via a header parameter, and returns responses indicating success, bad request, or internal server error. |
| `query_segment_values` | Creates a report on segment values using a POST request to the "/api/segment-values-reports" endpoint, which requires a revision header and returns a report upon successful execution. |
| `query_segment_series` | The POST operation at the "/api/segment-series-reports" path generates segment series reports, requiring a revision number provided in the header, and returns successful reports with a 200 status code or error messages for invalid requests (400) or server issues (500). |
| `get_reviews` | Retrieves review data with optional filtering, pagination, sorting, and field selection parameters for events and reviews. |
| `get_review` | The "/api/reviews/{id}" API endpoint uses the GET method to retrieve a specific review by its ID, allowing optional query parameters for selecting fields and specifying additional data to include, with support for a revision header. |
| `update_review` | This API operation uses the PATCH method at the "/api/reviews/{id}" path to partially update a review by applying specific changes while maintaining the integrity of unchanged fields, requiring a revision header for processing. |
| `get_segments` | Use this API endpoint to retrieve a list of segments, allowing you to filter the results by various criteria and customize the output with specific fields and sorting options. |
| `create_segment` | Creates a new segment with the specified configuration, returning the created resource upon success. |
| `get_segment` | Retrieve a segment by its ID, optionally including additional fields, flows, segment details, tags, and related data, with support for specifying a revision in the request header. |
| `delete_segment` | Deletes the specified segment by ID, requiring a revision header, and returns a 204 for success, 400 for invalid requests, or 500 for server errors. |
| `update_segment` | The PATCH method at "/api/segments/{id}" allows partial updates to a segment resource, enabling modifications of specific fields while leaving others unchanged, with an optional revision header for version control. |
| `get_tags_for_segment` | Retrieves tags for a segment by ID, allowing optional filtering by specific tag fields and accepting a revision in the request header. |
| `get_tag_ids_for_segment` | Retrieves the relationships and associated tags for a specific segment identified by its ID, including any revision header information. |
| `get_profiles_for_segment` | Retrieves a paginated list of profiles associated with a specific segment, supporting filtering, sorting, and field selection. |
| `get_profile_ids_for_segment` | This API operation retrieves the profiles related to a segment with the specified ID using a GET method, allowing for filtering, pagination, sorting, and revision specification through query and header parameters. |
| `get_flows_triggered_by_segment` | Retrieves flow triggers for a segment by ID, optionally filtering by specific flow fields and providing a revision in the header. |
| `get_ids_for_flows_triggered_by_segment` | Retrieves the associated flow triggers linked to a specific segment by its ID, supporting a custom revision header for version control. |
| `get_tags` | Retrieves a list of tags filtered, sorted, and paginated via query parameters while supporting selective field inclusion and specific API revisions via headers. |
| `create_tag` | Creates a new tag resource using the provided data, requiring a revision header and returning HTTP status codes for success (201), client errors (400), or server issues (500). |
| `get_tag` | Retrieves a specific tag by ID with optional query parameters for field selection, included resources, and a header for revision control. |
| `delete_tag` | Deletes the specified tag by ID, requiring a revision header, with responses indicating success (204 No Content), bad request (400), or server error (500). |
| `update_tag` | Updates the specified tag (ID: {id}) with partial modifications using the revision header for conflict detection, returning 204 on success. |
| `get_flow_ids_for_tag` | Retrieves the associated flow resources linked to the specified tag ID, using the provided revision header for version control. |
| `tag_flows` | The API operation at path "/api/tags/{id}/relationships/flows" using the "POST" method creates a new relationship between a tag and a flow, optionally specifying a revision in the header. |
| `remove_tag_from_flows` | Deletes the relationship between the specified tag and associated flows, returning a 204 No Content response upon successful deletion. |
| `get_campaign_ids_for_tag` | This API operation retrieves relationships between a tag with the specified ID and campaigns, using the GET method at the path "/api/tags/{id}/relationships/campaigns". |
| `tag_campaigns` | Creates a relationship between the specified tag and campaign(s) using the "revision" header for concurrency control. |
| `remove_tag_from_campaigns` | The API operation defined at `/api/tags/{id}/relationships/campaigns` using the `DELETE` method removes the relationship between a tag with the specified ID and associated campaigns, requiring a `revision` header and returning a successful response with a 204 status code if completed correctly. |
| `get_list_ids_for_tag` | Retrieves the relationship details for lists associated with a specified tag ID, requiring a revision header parameter. |
| `tag_lists` | Creates a new relationship between a specified tag and lists using the provided header revision. |
| `remove_tag_from_lists` | Deletes the relationship between a tag with the specified ID and its associated lists, requiring a revision header. |
| `get_segment_ids_for_tag` | Retrieves a list of relationships between a tag identified by `{id}` and segments, with the option to specify a revision in the request header. |
| `tag_segments` | Creates a relationship between a tag identified by `{id}` and one or more segments, using the specified revision from the request header. |
| `remove_tag_from_segments` | Removes tag associations with one or more segments by specifying the tag ID in the path and segment relationships in the request body. |
| `get_tag_group_for_tag` | Retrieves the details of a tag group associated with the specified tag ID, allowing field selection via query parameters and revision specification via headers. |
| `get_tag_group_id_for_tag` | Retrieves the tag-group relationship details for the specified tag ID, including optional revision header parameters. |
| `get_tag_groups` | Retrieves a list of tag groups with optional filtering, sorting, pagination via cursor, field selection, and revision headers, returning appropriate status responses. |
| `create_tag_group` | Creates a new tag group with the specified revision header, returning a 201 response on successful creation or appropriate error codes (400/500) for failures. |
| `get_tag_group` | Retrieves a tag group by ID, allowing optional filtering by specific fields and including a revision header, returning a successful response with a 200 status code. |
| `delete_tag_group` | Deletes a tag group by its ID, with the revision specified in the request header, returning success if the operation completes without errors. |
| `update_tag_group` | Updates the specified tag group by ID using partial modifications, requiring a revision header and returning 200, 400, or 500 status codes. |
| `get_tags_for_tag_group` | This API operation retrieves a list of tags associated with a specific tag group, identified by `{id}`, allowing optional filtering by specific tag fields via the `fields[tag]` query parameter, with support for specifying a revision in the request header. |
| `get_tag_ids_for_tag_group` | This GET operation retrieves the relationships between a specific tag group and its associated tags, identified by the provided `{id}` in the path, with an optional `revision` header for additional context. |
| `get_templates` | Retrieves template resources with optional filtering, sorting, pagination, and field selection. |
| `create_template` | Creates a new template with the specified revision, returning a successful response if created or error responses for bad requests or server failures. |
| `get_template` | The API operation defined at the path "/api/templates/{id}" using the "GET" method retrieves a specific template by its ID, optionally specifying fields to include and a revision in the headers, returning a successful response with HTTP status 200. |
| `delete_template` | Deletes a template by ID with optional revision header, returning 204 on success or 400/500 for client/server errors. |
| `update_template` | Updates a template's properties using partial modifications with a specified revision header, returning 200 on success. |
| `render_template` | Renders a template using the specified revision header, returning success (201) or error status (400/500). |
| `clone_template` | Creates a new template by cloning an existing one, requiring a revision header parameter and returning success (201), bad request (400), or server error (500) responses. |
| `get_all_universal_content` | This API operation uses the GET method at the "/api/template-universal-content" path to retrieve template universal content data, allowing filtering and sorting with optional parameters for fields, filter, pagination, and sorting, while requiring a revision in the header. |
| `create_universal_content` | Generates universal content templates with optional revision control in headers, returning success (201) or error codes (400, 500). |
| `get_universal_content` | This API operation retrieves a template with universal content specified by the `{id}` using the GET method, allowing optional filtering by specific fields and specifying a revision in the header. |
| `delete_universal_content` | Deletes the specified universal content item by ID, requiring a revision header, and returns 204 No Content upon successful deletion. |
| `update_universal_content` | The PATCH operation at "/api/template-universal-content/{id}" partially updates a template's content by specifying specific changes in the request body, with the revision specified in the header, returning a successful response or error based on the request's validity. |
| `get_tracking_settings` | Retrieves all tracking settings in an account with optional pagination and field filtering support. |
| `get_tracking_setting` | Retrieves tracking settings by ID with optional field selection and revision header support. |
| `update_tracking_setting` | PATCH /api/tracking-settings/{id} partially updates a specific tracking setting by ID, requiring a revision in the header, and may return a successful response or error codes based on input validity and server status. |
| `get_webhooks` | Retrieves webhooks with optional field selection, included resources, and revision headers. |
| `create_webhook` | The "/api/webhooks" endpoint supports the "POST" method to create a new webhook, requiring a revision header, and returns a successful creation response with a 201 status code, or error responses for bad requests (400) or internal server errors (500). |
| `get_webhook` | Retrieves a webhook by its ID using a GET request, allowing optional filtering by specifying fields and includes, with support for revision tracking via a header. |
| `delete_webhook` | Deletes a webhook resource identified by its ID, returning a 204 No Content response upon successful deletion, with optional revision information provided in the headers, and error responses for invalid requests or server errors. |
| `update_webhook` | Updates the webhook resource identified by {id} using partial modifications, requiring a revision header and returning appropriate status codes for success (200), client errors (400), or server errors (500). |
| `get_webhook_topics` | Retrieves webhook topics with an optional revision header parameter, returning 200, 400, or 500 status codes. |
| `get_webhook_topic` | Retrieves a webhook topic by its ID using the GET method, supporting revision information via a header parameter, and returns responses for successful retrieval (200), bad requests (400), and internal server errors (500). |
