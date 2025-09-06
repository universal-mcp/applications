# ShopifyApp MCP Server

An MCP Server for the ShopifyApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ShopifyApp API.


| Tool | Description |
|------|-------------|
| `get_access_scopes` | Retrieves the list of OAuth access scopes (permissions) granted to an application using the Shopify Admin REST API. |
| `get_storefront_tokens` | Retrieves a list of storefront access tokens, which are used to authenticate requests to the Shopify Storefront API, allowing access to data such as products and checkout functionality. |
| `create_storefront_token` | Creates a Shopify Storefront API access token for client-side GraphQL requests, enabling access to store data like products, collections, and checkout. |
| `delete_storefront_access_token` | Deletes a storefront access token and returns a success status upon completion. |
| `retrieves_alist_of_reports` | Retrieves reports data for specified parameters, such as IDs, limit, and date ranges, using the GET method. |
| `creates_anew_report` | Submits a report generation request and returns a success status upon creation. |
| `retrieves_asingle_report` | Retrieves a report by its ID using the specified API version and optionally includes additional fields in the response. |
| `updates_areport` | Updates or replaces a specific report resource at the specified report ID in JSON format using the PUT method. |
| `deletes_areport` | Deletes the specified report using the DELETE method and returns a successful status upon completion. |
| `get_application_charges` | Retrieves a list of application charges in JSON format, allowing filtering by specific fields and starting from a given ID. |
| `creates_an_application_charge` | Creates a new application charge through the API, returning a success response upon creation or an error if validation fails. |
| `retrieves_an_application_charge` | Retrieves details of a specific application charge transaction using specified fields from the Stripe Connect API. |
| `activates_an_application_charge` | Activates a previously created application charge using the specified ID and returns a success status upon completion. |
| `retrieves_all_application_credits` | Retrieves a list of application credits issued to merchants through the Shopify API, allowing optional field filtering via query parameters. |
| `creates_an_application_credit` | Issues application credits to merchants, which can be used towards future app purchases in Shopify, using the POST method at "/admin/api/{api_version}/application_credits.json". |
| `get_application_credit_by_id` | Retrieves a specific application credit from Shopify's admin API, including optional field filtering parameters. |
| `get_recurring_charges` | Retrieves a list of recurring application charges with optional filtering by ID and field selection. |
| `create_recurring_charge` | Creates a new recurring application charge using the API, handling the setup and management of periodic billing. |
| `retrieves_asingle_charge` | Retrieves details for a specific recurring application charge by ID using the "GET" method, optionally including additional fields specified in the query parameters. |
| `delete_recurring_charge` | Cancels an existing recurring application charge for a Shopify store. |
| `activate_recurring_charge` | Activates a recurring application charge using the API and returns a status message in response. |
| `update_recurring_charge_custom` | Updates a Shopify recurring application charge's properties and returns the modified charge details. |
| `retrieves_alist_of_usage_charges` | Retrieves usage charges for a specific recurring application charge via the Shopify Admin API, filtering results based on specified fields. |
| `creates_ausage_charge` | Creates a usage-based charge on a recurring billing subscription and returns the charge details upon success. |
| `retrieves_asingle_chargeone` | Retrieves a specific usage charge associated with a recurring application charge for tracking and billing purposes. |
| `list_customer_addresses` | Retrieves a list of customer addresses associated with a specific customer ID. |
| `creates_anew_address_for_acustomer` | Creates a new address for a specified customer using the POST method. |
| `get_single_customer_address` | Retrieves a specific customer address using the provided customer ID and address ID, returning details about the address. |
| `update_customer_address_by_id` | Updates an existing customer address using the HTTP PUT method at a specified API path, returning a successful status message upon completion. |
| `delete_customer_address` | Deletes a customer's address specified by the customer ID and address ID using a DELETE request. |
| `set_customer_address` | Updates an existing address for a specified customer using the PUT method, returning a status message upon successful completion. |
| `set_default_address_by_id` | Sets the specified address as the default for the customer. |
| `retrieves_alist_of_customers` | Retrieves a list of customers with optional filtering by IDs, creation/update timestamps, and field selection. |
| `creates_acustomer` | Creates a new customer resource using the API and returns a status message upon successful creation. |
| `search_customers` | Searches customer records using specified filters, sorting options, and field selections, returning matching results in a structured format. |
| `retrieves_asingle_customer` | Retrieves a customer's details in JSON format using the specified API version and customer ID, with optional fields specified via the query parameters. |
| `updates_acustomer` | Updates or replaces the customer resource at the specified ID and returns the updated entity. |
| `deletes_acustomer` | Deletes a customer's data permanently using the "DELETE" method at the specified API path, immediately canceling any active subscriptions and preventing further operations. |
| `generate_activation_url` | Generates and returns an account activation URL for a customer via Shopify's API, enabling direct access to activation without manual intervention. |
| `send_customer_invite` | Sends an invitation to a specified customer using the "POST" method. |
| `retrieves_acount_of_customers` | Retrieves the count of customers using the specified API version. |
| `get_customer_orders` | Retrieves a list of orders for a specified customer using the "GET" method via the API endpoint "/admin/api/{api_version}/customers/{customer_id}/orders.json". |
| `list_customer_saved_searches` | Retrieves a list of customer-saved searches in JSON format, allowing for optional filtering by limit, since_id, and specific fields. |
| `creates_acustomer_saved_search` | Creates a new customer saved search entry via the specified API version and returns an empty response on success or validation errors. |
| `get_customer_saved_searches_count` | Retrieves a count of customer saved searches with optional filtering by creation time using the "since_id" parameter. |
| `get_customer_saved_search_by_id` | Retrieves a customer saved search by ID using the Shopify API, optionally specifying fields to include in the response. |
| `updates_acustomer_saved_search` | Updates a customer's saved search identified by the `{customer_saved_search_id}` at the specified `{api_version}`, allowing modifications to its details. |
| `deletes_acustomer_saved_search` | Deletes a specified customer saved search using its unique identifier and returns a success status upon completion. |
| `get_customers_by_saved_search` | Retrieves a list of customers associated with a specific customer saved search, allowing for optional filtering by order, limited results, and customizable fields. |
| `retrieves_alist_of_discount_codes` | Retrieves discount codes associated with a specific price rule using the specified API version. |
| `creates_adiscount_code` | Creates a discount code associated with a specific price rule in Shopify and returns the created resource. |
| `retrieves_asingle_discount_code` | Retrieves information about a specific discount code for a given price rule using the API. |
| `updates_an_existing_discount_code` | Updates an existing discount code associated with a specified price rule in Shopify, allowing merchants to modify the discount code details within the defined price rule. |
| `deletes_adiscount_code` | Deletes a specific discount code associated with a price rule. |
| `lookup_discount_codes` | Retrieves discount code information using the "GET" method at the "/admin/api/{api_version}/discount_codes/lookup.json" endpoint. |
| `post_price_rule_batch` | Applies batch operations to a specific price rule using the POST method, allowing for efficient management of price rules in bulk. |
| `get_price_rule_batch` | Retrieves a batch of price rule details for a specific batch and price rule ID using the specified API version. |
| `get_discount_codes` | Retrieves a list of discount codes associated with a specific batch under a price rule using the "GET" method. |
| `retrieves_alist_of_price_rules` | Retrieves a paginated list of price rules with optional filters for time ranges, usage, and creation/modification dates. |
| `creates_aprice_rule` | Creates a new price rule using the POST method, enabling the management of pricing configurations for specific products or customer groups at the specified API endpoint. |
| `retrieves_asingle_price_rule` | Retrieves a specific price rule's details including entitlements, prerequisites, and discount conditions from the store's pricing system. |
| `updates_an_existing_aprice_rule` | Updates a price rule configuration for a specific ID using the Shopify Admin REST API. |
| `remove_an_existing_pricerule` | Deletes a specified price rule with the provided ID using the "DELETE" method, returning a successful response with a 204 status code. |
| `retrieves_acount_of_all_price_rules` | Retrieves the total count of price rules configured in the system. |
| `retrieves_alist_of_events` | Retrieves a filtered list of administrative events with parameters for date ranges, pagination, and field selection. |
| `retrieves_asingle_event` | Retrieves event details in JSON format from the admin API for a specified event ID and API version with optional field filtering. |
| `retrieves_acount_of_events` | Retrieves the count of events using the "GET" method, allowing filtering by creation date range via "created_at_min" and "created_at_max" query parameters. |
| `retrieves_alist_of_webhooks` | Retrieves a list of webhooks in JSON format, allowing filtering by address, creation and update times, specific fields, limit, and topic, using the "GET" method. |
| `create_anew_webhook` | Creates a new webhook subscription for event notifications from the admin API. |
| `receive_acount_of_all_webhooks` | Retrieves the count of webhooks for a specified address and topic using the GET method. |
| `receive_asingle_webhook` | Retrieves a specific webhook's details in JSON format using the specified API version and webhook ID from the admin API. |
| `modify_an_existing_webhook` | Updates the specified webhook's configuration using the provided data and returns a success status upon completion. |
| `remove_an_existing_webhook` | Deletes a webhook identified by its ID using the DELETE method, effectively removing the webhook endpoint. |
| `retrieves_alist_of_inventory_items` | Retrieves a list of inventory items with support for filtering by IDs and limiting results. |
| `get_inventory_item_by_id` | Retrieves inventory item details using the API at the specified version, returning information for the specified inventory item ID. |
| `updates_an_existing_inventory_item` | Updates an inventory item with the specified ID by modifying its characteristics or details using the PUT method at the "/admin/api/{api_version}/inventory_items/{inventory_item_id}.json" endpoint. |
| `get_inventory_levels` | Retrieves inventory level information for specified inventory items and locations using the "GET" method, allowing for filtering by item IDs, location IDs, and update time, and returns the data in JSON format. |
| `delete_inventory_levels` | Deletes inventory levels from the system and returns a success status without content. |
| `adjust_inventory_level` | Adjusts the inventory level for a specific item at a location using a relative quantity change. |
| `connect_inventory_levels` | Connects inventory levels to a specified location or system and returns a success status upon creation. |
| `set_inventory_level` | Updates inventory levels for specific items and returns a success status. |
| `retrieves_alist_of_locations` | Retrieves a list of locations accessible through the admin API and returns them in JSON format. |
| `get_location_by_id` | Retrieves the details of a specific location by its ID from the admin API. |
| `retrieves_acount_of_locations` | Retrieves the count of locations in JSON format using the specified API version. |
| `get_inventory_level` | Retrieves the current inventory levels for products at a specified store location using the GET method and returns this information in JSON format. |
| `list_marketing_events` | Retrieves a paginated list of marketing events using the specified limit and offset parameters. |
| `creates_amarketing_event` | Creates a marketing event using the specified API version and returns a status message upon successful creation. |
| `get_marketing_events_count` | Retrieves the total count of marketing events matching specified criteria using filtering parameters. |
| `retrieves_asingle_marketing_event` | Retrieves the details of a specific marketing event by its ID from the Shopify API. |
| `updates_amarketing_event` | Updates a marketing event's details via the specified marketing_event_id and returns a success status upon completion. |
| `deletes_amarketing_event` | Deletes a specific marketing event using its unique identifier and returns a success status upon removal. |
| `create_marketing_event_engagement` | Creates an engagement record for a specified marketing event using the POST method. |
| `get_metafields` | Retrieves a list of metafields across all resources with optional filters like namespace, key, value type, and date ranges. |
| `create_metafields` | Creates a new metafield entry in Shopify's system for storing custom data associated with various resources. |
| `get_metafield_count` | Retrieves the count of metafields for a specified resource using the "GET" method at the "/admin/api/{api_version}/metafields/count.json" endpoint. |
| `get_metafield_by_id_json` | Retrieves a specific metafield by its ID using the Shopify API, allowing for optional filtering of returned fields. |
| `updates_ametafield` | Updates an existing metafield's data in Shopify via the specified API endpoint. |
| `deletes_ametafield_by_its_id` | Deletes a metafield by its ID using the Shopify API, removing the specified metafield's data from a store. |
| `list_blog_articles_by_params` | Retrieves a list of articles from a specified blog using the GET method with optional filtering by parameters such as creation date, publication status, author, and tags. |
| `creates_an_article_for_ablog` | Creates a new article in the specified blog using the Blogger API and returns the created article on success. |
| `get_article_count` | Retrieves the count of articles in a specific blog with optional time-based and status filters. |
| `receive_asingle_article` | Retrieves a specific article from a blog by its ID, returning the requested fields in the response. |
| `updates_an_article` | Updates an article in a blog using the "PUT" method, replacing the existing resource with a new representation at the specified API path. |
| `deletes_an_article` | Deletes a specific article from a blog using the provided blog and article identifiers and returns a success status upon completion. |
| `get_authors` | Retrieves a list of article authors in JSON format using the specified API version. |
| `retrieves_alist_of_all_article_tags` | Retrieves article tags with optional parameters for limiting results and filtering by popularity. |
| `get_theme_assets_json` | Retrieves a list of theme assets for a specified theme in Shopify using the GET method at the "/admin/api/{api_version}/themes/{theme_id}/assets.json" endpoint, optionally filtering the response by fields specified in the query parameters. |
| `update_theme_asset` | Updates or creates theme assets in Shopify stores using the Asset REST API, enabling modification of theme files like Liquid templates or CSS. |
| `deletes_an_asset_from_atheme` | Deletes a theme asset in a Shopify store using the "DELETE" method at the specified API path, returning a status message based on the outcome of the deletion request. |
| `retrieve_alist_of_all_blogs` | Retrieves a list of blogs with configurable filters (limit, handle, etc.) and optional field selection in the specified API version. |
| `create_anew_blog` | Creates a new blog using the API at "/admin/api/{api_version}/blogs.json" with the "POST" method, returning a status indicating success or failure. |
| `receive_acount_of_all_blogs` | Retrieves the count of blogs using the "GET" method at the specified API endpoint. |
| `receive_asingle_blog` | Retrieves a blog with the specified ID and optional fields using the "GET" method. |
| `modify_an_existing_blog` | Updates or replaces an entire blog entry at the specified blog ID using the provided data and returns a success status. |
| `remove_an_existing_blog` | Deletes a blog with the specified ID using the DELETE method via the API endpoint "/admin/api/{api_version}/blogs/{blog_id}.json" and returns a successful status message if the operation is completed. |
| `retrieves_alist_of_comments` | Retrieves a list of comments with filtering by date ranges, status, and field selection parameters via a GET request. |
| `creates_acomment_for_an_article` | Creates comments through an administrative API endpoint. |
| `retrieves_acount_of_comments` | Retrieves the count of comments filtered by creation, update, and publication timestamps or status using specific query parameters. |
| `retrieves_asingle_comment_by_its_id` | Retrieves a specific comment's details by its ID in the GitHub API, supporting optional field filtering. |
| `updates_acomment_of_an_article` | Updates a comment identified by `{comment_id}` using the "PUT" method, enabling modifications to existing comments in a structured API environment. |
| `marks_acomment_as_spam` | Marks a comment as spam in the admin system and returns a success status. |
| `marks_acomment_as_not_spam` | Marks a comment as not spam in the admin API and returns a success status. |
| `approves_acomment` | Approves a specified comment via a POST request and returns a success status upon approval. |
| `removes_acomment` | Removes a comment via the API, identified by its ID, using a POST request at the specified path. |
| `restore_comment` | Restores a deleted comment using the specified API version and returns a success status. |
| `retrieves_alist_of_pages` | Retrieves a list of pages in JSON format using the Shopify API, allowing filtering by parameters such as limit, title, handle, creation and update dates, and publication status. |
| `create_anew_page` | Creates a new page in the Shopify admin using the POST method and returns a status message. |
| `retrieves_apage_count` | Retrieves the count of pages in a Shopify store based on specified criteria such as title, creation date, update date, publication date, and publication status using the GET method. |
| `retrieves_asingle_page_by_its_id` | Retrieves a specific page's details from the admin API, filtered by the requested fields, and returns the structured data in JSON format. |
| `updates_apage` | Updates a specific page with the given ID using the PUT method, replacing its existing content with new data. |
| `deletes_apage` | Deletes a page identified by the given page ID using the DELETE method, returning a status message upon successful deletion. |
| `retrieves_alist_of_url_redirects` | Retrieves a list of redirects in JSON format using the "GET" method at the "/admin/api/{api_version}/redirects.json" endpoint, allowing filtering by parameters such as limit, since_id, path, target, and fields. |
| `creates_aredirect` | Creates a new URL redirect using the API, returning a successful response with a status code of 201 upon completion, or an error response with a status code of 422 if validation fails. |
| `retrieves_acount_of_url_redirects` | Retrieves the count of redirects for a specified path using the GET method at "/admin/api/{api_version}/redirects/count.json". |
| `retrieves_asingle_redirect` | Retrieves details of a specific redirect ID in JSON format, allowing optional field selection via query parameters. |
| `updates_an_existing_redirect` | Updates or replaces a specific redirect resource identified by `{redirect_id}` using the REST API, returning a status message if successful. |
| `deletes_aredirect` | Deletes a specific URL redirect identified by the provided `redirect_id`, removing the associated redirection rule from the system. |
| `retrieves_alist_of_all_script_tags` | Retrieves a list of script tags using the Shopify API, allowing filtering by parameters such as creation and update times, source URL, and specific fields. |
| `creates_anew_script_tag` | Creates a script tag for loading remote JavaScript into a storefront or checkout page via the Shopify Admin API. |
| `retrieves_acount_of_all_script_tags` | Retrieves the count of script tags using the "GET" method, with an optional query parameter "src" to refine the request. |
| `retrieves_asingle_script_tag` | Retrieves a script tag by its ID using the API, allowing for optional specification of fields to include in the response. |
| `updates_ascript_tag` | Updates a script tag by its ID using the PUT method and returns a successful response with a status code of 200. |
| `deletes_ascript_tag` | Deletes a specified script tag from a Shopify store using the provided script tag ID. |
| `retrieves_alist_of_themes` | Retrieves a list of store themes (including active, unpublished, and legacy themes) with optional field filtering via query parameters. |
| `creates_atheme` | Creates a new theme in a Shopify store via the Admin API, returning a success status on creation or validation errors. |
| `retrieves_asingle_theme` | Retrieves detailed information about a specific theme by ID from the Shopify admin, including customizable fields. |
| `modify_an_existing_theme` | Updates a theme resource by replacing or modifying it using the provided JSON data. |
| `remove_an_existing_theme` | Deletes a specified theme and returns a success status upon completion. |
| `retrieves_acount_of_checkouts` | Retrieves the count of checkouts using the "GET" method at "/admin/api/{api_version}/checkouts/count.json", allowing filtering by parameters such as since_id, creation date, update date, and status. |
| `get_checkouts` | Retrieves a list of checkouts with optional filters like date ranges, status, and pagination controls. |
| `creates_acheckout` | Creates a new checkout session for processing payments and managing order details. |
| `retrieves_alist_of_draft_orders` | Retrieves a list of draft orders from a Shopify store, allowing specification of fields, limits, and filters by ID, status, and update time, using the GET method. |
| `create_anew_draftorder` | Creates a new draft order in a Shopify store, allowing merchants to generate provisional sales transactions for custom or wholesale purchases, manage inventory, and facilitate secure payment processing when the order is finalized. |
| `receive_asingle_draftorder` | Retrieves a specific draft order by its ID using the GET method, allowing optional filtering by specific fields to customize the response. |
| `modify_an_existing_draftorder` | Updates a specific draft order using the Shopify Draft Order API, allowing for modifications such as changing products, quantities, or applying discounts. |
| `remove_an_existing_draftorder` | Deletes a draft order specified by its ID using the DELETE method, removing it from the system. |
| `receive_acount_of_all_draftorders` | Retrieves the count of draft orders matching specified conditions, such as status, update time, and since ID, using the Shopify API. |
| `send_an_invoice` | Sends an email invoice for a specified draft order using the Shopify Admin API. |
| `complete_adraft_order` | Completes a Shopify draft order via the API, converting it into a finalized order and returning the result. |
| `get_order_risks` | Retrieves the risk assessment details for a specific order using the "GET" method. |
| `creates_an_order_risk_for_an_order` | Submits a fraud risk assessment for an order to Shopify's deprecated legacy API, returning a 201 status upon creation. |
| `get_order_risk_by_id` | Retrieves a specific risk associated with an order using the specified API version. |
| `updates_an_order_risk` | Updates or replaces a specific risk associated with an order in the system using the PUT method. |
| `deletes_an_order_risk_for_an_order` | Deletes a specific risk associated with an order using the API endpoint at "/admin/api/{api_version}/orders/{order_id}/risks/{risk_id}.json" via the DELETE method. |
| `retrieves_alist_of_orders` | Retrieves a list of Shopify orders using the "GET" method at "/admin/api/{api_version}/orders.json," allowing for filtering by various criteria such as order IDs, creation and update times, status, and more. |
| `creates_an_order` | Creates a new order in a Shopify store using the Admin API, returning a response with a status code based on the operation's success or failure. |
| `retrieves_aspecific_order` | Retrieves details for a specific order using the specified API version and order ID in the admin API. |
| `updates_an_order` | Updates an existing order or creates a new one at the specified order ID using the PUT method. |
| `deletes_an_order` | Deletes a specified order using the provided order ID, returning a successful status if the operation is completed. |
| `retrieves_an_order_count` | Retrieves the count of orders from a Shopify store with optional filters for date ranges, status, and fulfillment/financial states. |
| `closes_an_order` | Closes a specified order in the admin API by its ID using the specified API version and returns a success status. |
| `re_opens_aclosed_order` | Opens an order with the specified ID using the POST method and returns a successful response upon completion. |
| `cancels_an_order` | Cancels a specified order using a POST request and returns status codes for success (200) or invalid request (422). |
| `list_order_refunds` | Retrieves a list of refunds for a specified order, allowing optional filtering by the number of results, specific fields, and currency. |
| `creates_arefund` | Creates a refund for an order using the specified order ID, allowing merchants to process partial or full refunds through the API. |
| `retrieves_aspecific_refund` | Retrieves a specific refund associated with an order by its ID, allowing customization of the response with optional fields and currency settings. |
| `calculates_arefund` | Calculates refund amounts for an order, including line items, shipping, and taxes, based on specified criteria. |
| `retrieves_alist_of_transactions` | Retrieves a list of transactions for a specified order using the Shopify API, optionally filtered by since_id, specified fields, and currency. |
| `creates_atransaction_for_an_order` | Creates a new transaction for a specified order using the Shopify Admin API and returns the result with a 201 Created status. |
| `get_order_transactions_count` | Retrieves the transaction count for a specific order using the "GET" method. |
| `retrieves_aspecific_transaction` | Retrieves a specific transaction from an order, optionally filtering response fields and currency format using query parameters. |
| `retrieves_alist_of_gift_cards` | Retrieves a list of gift cards in JSON format, allowing filtering by status, limiting the number of results, specifying a starting point with an ID, and selecting specific fields for the response. |
| `creates_agift_card` | Creates a new gift card and returns the created resource with a 201 status code. |
| `retrieves_asingle_gift_card` | Retrieves information about a specific gift card using the provided gift card ID. |
| `updates_an_existing_gift_card` | Updates the details of a specific gift card using the PUT method at the "/admin/api/{api_version}/gift_cards/{gift_card_id}.json" endpoint. |
| `retrieves_acount_of_gift_cards` | Retrieves the count of gift cards filtered by status using the Shopify Admin REST API. |
| `disables_agift_card` | Deactivates a gift card and invalidates its remaining balance via a POST request. |
| `searches_for_gift_cards` | Retrieves a list of gift cards matching specified criteria such as search query, order, limit, and requested fields. |
| `retrieves_alist_of_all_users` | Retrieves a list of users in the system as JSON data using the "GET" method. |
| `retrieves_asingle_user` | Retrieves a specific user's details from the administrative API in JSON format for the specified API version and user ID. |
| `get_current_user` | Retrieves the current authenticated user's details in the specified API version. |
| `retrieves_alist_of_collects` | Retrieves a list of data collections in JSON format, allowing filtering by limit, since_id, and specific fields. |
| `create_collects_post` | Creates a new collection in a store using the POST method, returning a status message upon successful creation or an error response if the request is invalid. |
| `get_collect_details` | Retrieves a specific collect entry from the Shopify admin API, returning JSON data with fields optionally filtered by the request. |
| `removes_aproduct_from_acollection` | Deletes a specific collect entry by ID using the specified API version and returns a success status. |
| `retrieves_acount_of_collects` | Retrieves the count of collections using the GET method at the specified API endpoint "/admin/api/{api_version}/collects/count.json". |
| `retrieves_asingle_collection` | Retrieves information about a specific collection using the "GET" method, allowing optional filtering through the "fields" query parameter. |
| `list_collection_products` | Retrieves a list of products from a specific collection using the "GET" method, allowing optional filtering by a limit parameter. |
| `list_custom_collections` | Retrieves a paginated list of custom collections (manually curated product groupings) with optional filtering by parameters like IDs, titles, product associations, and publication status. |
| `creates_acustom_collection` | Creates a new custom collection in a Shopify store using the API, allowing merchants to group products together for easier navigation. |
| `get_custom_collections_count` | Retrieves a count of custom collections in a Shopify store, optionally filtered by title, product association, or publication timestamps. |
| `get_custom_collection_by_id` | Retrieves a specific custom collection and optionally includes specified fields in the response, using the Shopify API. |
| `update_custom_collection_by_id` | Updates an existing custom collection by replacing it with the new data provided in the request body, allowing modifications to its attributes such as title and collected products. |
| `deletes_acustom_collection` | Deletes a custom product collection in Shopify using the specified collection ID. |
| `receive_alist_of_all_product_images` | Retrieves a list of product images for a specified product using the "GET" method at the "/admin/api/{api_version}/products/{product_id}/images.json" path, allowing optional filters by "since_id" and customizable fields. |
| `create_anew_product_image` | Creates and manages product images by uploading new images for a specified product using the POST method. |
| `get_product_image_count` | Retrieves the count of product images associated with a specific product using the GET method, optionally filtering by a since_id parameter. |
| `receive_asingle_product_image` | Retrieves a specific product image by ID with optional field selection for the API version. |
| `modify_an_existing_product_image` | Updates an existing product image specified by the product ID and image ID using the PUT method, allowing for modifications to image attributes such as source or metadata. |
| `remove_an_existing_product_image` | Deletes a specific product image identified by the `image_id` from a product specified by the `product_id` using the HTTP DELETE method. |
| `list_product_variants` | Retrieves a list of product variants for a specified product with optional pagination, currency display, and field filtering. |
| `create_anew_product_variant` | Creates a new product variant within a specified product using the POST method, returning a successful response when the variant is added. |
| `get_product_variant_count` | Retrieves the count of variants for a specific product in Shopify's inventory. |
| `receive_asingle_product_variant` | Retrieves variant details using the specified API version and variant ID, optionally filtering by specified fields. |
| `modify_an_existing_product_variant` | Updates the variant with the specified ID in the API, replacing its current state with the data provided in the request body. |
| `remove_an_existing_product_variant` | Deletes a product variant using the Shopify Admin API. |
| `retrieves_alist_of_products` | Retrieves a list of products from a Shopify store using the Admin API, allowing for filtering based on parameters such as product IDs, title, vendor, and creation or publication dates. |
| `creates_anew_product` | Creates a new product in Shopify via the REST Admin API and returns the product details upon successful creation. |
| `retrieves_acount_of_products` | Retrieves the count of products in a Shopify store using the specified API version, allowing optional filtering by vendor, product type, collection ID, creation date, update date, publication date, and publication status. |
| `retrieves_asingle_product` | Retrieves product details in JSON format for a specified product using the "GET" method, allowing optional filtering by specifying fields via query parameters. |
| `updates_aproduct` | Replaces an entire product entry in the admin system with a new version, returning a success status upon completion. |
| `deletes_aproduct` | Deletes a product along with its associated variants and media from the system using the provided product ID. |
| `list_smart_collections` | Retrieves a list of smart collections from a Shopify store, allowing for filtering by various parameters such as IDs, titles, product IDs, and publication status. |
| `creates_asmart_collection` | Creates a new Shopify smart collection with automated product inclusion rules and returns the collection details upon successful creation. |
| `count_smart_collections` | Retrieves a count of smart collections in a Shopify store, optionally filtered by title, product ID, update or publication dates, and publication status. |
| `get_smart_collection` | Retrieves a smart collection by its ID using the Shopify API, optionally specifying fields to include in the response. |
| `update_smart_collection` | Updates a specific smart collection's configuration and rules via the Shopify Admin API, returning a success status on completion. |
| `removes_asmart_collection` | Deletes the specified smart collection and returns a successful response upon completion. |
| `update_smart_collection_order` | Updates the sort order of products in a Shopify smart collection and returns a success status upon completion. |
| `completes_acheckout` | Completes a checkout process for a specified token, returning an Accepted status upon successful submission. |
| `retrieves_acheckout` | Checks the status of a checkout using a provided token via the GET method. |
| `modifies_an_existing_checkout` | Updates a checkout using the provided token, supporting HTTP responses for successful updates (200), successful processing without immediate completion (202), and invalid request data (422). |
| `retrieves_alist_of_shipping_rates` | Retrieves shipping rates for a specified checkout token via the API, returning available options in JSON format. |
| `get_collection_listings` | Retrieves a list of collection listings in JSON format using the "GET" method, optionally limited by a specified number of entries. |
| `get_product_ids` | Retrieves a list of product IDs for a specified collection listing, optionally limited by a query parameter, using the GET method. |
| `get_collection_listing` | Retrieves details of a specific collection listing in the admin API. |
| `update_collection_listing_by_id` | Updates the specified collection listing resource by replacing its entire representation at the specified ID, returning a success response upon completion. |
| `delete_collection_listing_by_id` | Deletes a collection listing with the specified ID using the DELETE method. |
| `create_session` | Creates a new user session using the Shopify API at the specified path, enabling secure interactions between the client and server. |
| `get_checkout_payments_list` | Retrieves payment details from a specific checkout session using the provided token, returning relevant payment information in JSON format. |
| `creates_anew_payment` | Creates a payment for a checkout session using the provided token, returning a status response upon completion. |
| `retrieves_asingle_payment` | Retrieves the details of a specific payment associated with a checkout using the Checkout.com API. |
| `get_checkout_payment_count_by_token` | Retrieves the count of payments for a specified checkout using the "GET" method, returning the result in JSON format. |
| `list_product_listings` | Retrieves a list of product listings with filtering options such as product identifiers, collection, update timestamps, and handles. |
| `list_product_ids` | Retrieves a list of product IDs from product listings with optional limit parameter. |
| `get_product_listings_count` | Retrieves the total count of product listings available in the system. |
| `get_product_listing` | Retrieves a specific product listing by ID using the GET method, returning details about the product listing. |
| `update_product_listing_by_id` | Updates a product listing by fully replacing its data at the specified path, using the PUT method. |
| `delete_product_listing_by_id` | Deletes a specific product listing by ID using the specified API version. |
| `get_feedback_resource` | Retrieves feedback data for a specific resource via the Admin API. |
| `create_anew_resourcefeedback` | Submits resource feedback for review and processing, returning status codes for success, conflicts, or validation errors. |
| `get_assigned_orders` | Retrieves fulfillment orders assigned to specific locations and filtered by assignment status using query parameters. |
| `sends_acancellation_request` | Sends a cancellation request to the fulfillment service for a specific fulfillment order, allowing the cancellation process to be initiated. |
| `accepts_acancellation_request` | Accepts a cancellation request for a fulfillment order via a POST request to the specified endpoint. |
| `rejects_acancellation_request` | Rejects a cancellation request for a Shopify fulfillment order and returns the updated fulfillment order details. |
| `list_carrier_services` | Retrieves a list of carrier services from a Shopify store, providing access to shipping options and real-time shipping rates for integration with third-party shipping providers. |
| `creates_acarrier_service` | Creates a custom carrier service in Shopify, enabling third-party shipping rate integration via a callback URL. |
| `retrieves_asingle_carrier_service` | Retrieves detailed information for a specific carrier service configured to provide real-time shipping rates via Shopify's shipping API. |
| `updates_acarrier_service` | Updates a specific carrier service with the provided ID using the "PUT" method in the Shopify API. |
| `deletes_acarrier_service` | Deletes an existing carrier service by ID and returns a success status upon completion. |
| `get_order_fulfillments` | Retrieves a list of fulfillments for a specific order with optional filtering by creation/update timestamps and pagination parameters. |
| `create_anew_fulfillment` | Creates a new fulfillment for an order, typically used to confirm shipment or pickup of items to complete the order process. |
| `get_fulfill_order_fulfillments` | Retrieves fulfillment information for a specific fulfillment order by its ID using the Shopify API. |
| `get_order_fulfillment_count` | Retrieves the count of fulfillments for a specific order based on optional date filters for creation and update times using the GET method. |
| `receive_asingle_fulfillment` | Retrieves a specific fulfillment for an order using the Shopify Admin API, returning fulfillment details in the response. |
| `modify_an_existing_fulfillment` | Updates a specific fulfillment order in Shopify's admin API for order processing. |
| `create_fulfillment` | Creates a new fulfillment record for an order using the Shopify API, allowing for the inclusion of details such as tracking numbers and shipment status updates. |
| `update_fulfillment_tracking` | Updates tracking information for a fulfillment using the provided tracking details via a POST request. |
| `complete_afulfillment` | Completes a fulfillment for a specific order in the Shopify API, marking it as processed and returning a success confirmation. |
| `post_order_fulfillment_open` | Opens a fulfillment for a specific order using the POST method, allowing the order to transition from a pending or scheduled state to being actively fulfilled. |
| `cancel_fulfillment` | Cancels a specific fulfillment by submitting a request to the endpoint "/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/cancel.json" using the POST method. |
| `cancels_afulfillment` | Cancels a fulfillment order identified by the `{fulfillment_id}` using the `POST` method, returning a status message indicating the outcome of the cancellation operation. |
| `get_fulfillment_event_by_id` | Retrieves a list of fulfillment events associated with a specific fulfillment ID within an order using the Shopify API. |
| `creates_afulfillment_event` | Creates a new fulfillment event for a specified order and fulfillment, allowing tracking and updating of the fulfillment status. |
| `get_fulfillment_event` | Retrieves a specific event by ID for a fulfillment within an order using the "GET" method. |
| `deletes_afulfillment_event` | Deletes a specific fulfillment event associated with a fulfillment in an order using the Shopify API, removing its tracking information. |
| `get_fulfillment_orders` | Retrieves a list of fulfillment orders associated with a specific order, including fulfillment details and status. |
| `get_fulfillment_order_by_id` | Retrieves detailed information about a specific fulfillment order in Shopify, including its status and associated order items. |
| `cancel_afulfillment_order` | Cancels a fulfillment order using the "POST" method at the specified endpoint, allowing for the termination of fulfillment attempts for the associated order. |
| `close_fulfillment_order` | Closes a fulfillment order via the Shopify Admin API and returns a success status upon completion. |
| `move_fulfillment_order_post` | Moves fulfillment order line items to a new location and returns the updated fulfillment order details. |
| `sends_afulfillment_request` | Submits a fulfillment request for a specified fulfillment order, allowing for the management and processing of order line items through a fulfillment service. |
| `accepts_afulfillment_request` | Accepts a fulfillment request for a specific fulfillment order, transitioning the order status to processing. |
| `rejects_afulfillment_request` | Rejects a fulfillment request for a specified fulfillment order, preventing any associated line items from being fulfilled. |
| `list_fulfillment_services` | Retrieves a list of fulfillment services available to a merchant using the Shopify API. |
| `create_anew_fulfillmentservice` | Registers a new fulfillment service using the Shopify API, allowing third-party warehouses to prepare and ship orders on behalf of store owners. |
| `get_fulfillment_service` | Retrieves details of a specific fulfillment service, including its configuration and operational settings, within the Shopify admin API. |
| `update_fulfillment_service` | Updates a Shopify fulfillment service's configuration, including tracking support and inventory management settings. |
| `delete_fulfillment_service_by_id` | Deletes a specified fulfillment service from the Shopify admin and returns a success status upon removal. |
| `get_fulfillment_locations` | Retrieves a list of eligible locations where fulfillment order items can be moved for potential fulfillment, sorted alphabetically by location name. |
| `return_the_current_balance` | Retrieves the current account balance for Shopify Payments, reflecting transactions not yet included in a payout. |
| `return_alist_of_all_disputes` | Retrieves a list of Shopify Payments disputes based on specified parameters, such as ID, status, and initiation date, using the GET method at the "/admin/api/{api_version}/shopify_payments/disputes.json" endpoint. |
| `return_asingle_dispute` | Retrieves information about a specific dispute related to Shopify Payments using the provided dispute ID. |
| `return_alist_of_all_payouts` | Retrieves a list of Shopify Payments payouts, which represent the movement of money from a merchant's Shopify Payments balance to their bank account, based on specified parameters like date range and payout status. |
| `return_asingle_payout` | Retrieves details of a specific Shopify Payments payout using the payout ID and API version. |
| `list_shopify_balance_txs` | Retrieves Shopify Payments balance transactions associated with payouts, filtered by parameters like payout ID, status, or test mode. |
| `receive_alist_of_all_countries` | Retrieves country data based on specified parameters such as since_id and fields, returning details in JSON format. |
| `creates_acountry` | Creates a new country entry via the Shopify Admin REST API and returns a success status upon creation. |
| `retrieves_acount_of_countries` | Retrieves country list data in JSON format using a GET request. |
| `retrieves_aspecific_county` | Retrieves country details by ID with optional field filtering. |
| `updates_an_existing_country` | Updates or creates a country resource at a specified ID using the "PUT" method, allowing for full replacement or creation of the country data. |
| `remove_an_existing_country` | Deletes a specified country from the system using the DELETE method at the "/admin/api/{api_version}/countries/{country_id}.json" endpoint. |
| `get_currencies` | Retrieves a list of supported currencies with their metadata using the specified API version. |
| `get_policies_admin_api` | Retrieves policy configurations in JSON format from the specified API version path using a GET request. |
| `get_provinces_by_country_id` | Retrieves a list of provinces for a specific country using query parameters like `since_id` and `fields` to filter or format the response. |
| `get_country_provinces_count` | Retrieves the total count of provinces for a specified country using the GET method. |
| `get_province_detail_by_id` | Retrieves province details for a specific country using the specified API version and includes optional field selection. |
| `update_province_by_id_json` | Updates a specific province's details for a given country via the Shopify Admin REST API and returns a success status upon completion. |
| `retrieves_the_shop_sconfiguration` | Retrieves shop information in JSON format using the specified API version via the "GET" method at the "/admin/api/{api_version}/shop.json" endpoint, allowing optional specification of fields to include in the response. |
| `list_tender_transactions` | Retrieves a list of tender transactions with optional filtering by processing time, order, and pagination parameters. |
