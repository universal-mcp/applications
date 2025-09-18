# WhatsappBusinessApp MCP Server

An MCP Server for the WhatsappBusinessApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the WhatsappBusinessApp API.


| Tool | Description |
|------|-------------|
| `get_whatsapp_business_account` | Fetches customizable data, primarily analytics, for a specific WhatsApp Business Account (WABA) using its ID. The `fields` parameter allows detailed queries, including date ranges and granularity for metrics like message volume, to refine the returned data. |
| `get_business_account_credit_lines` | Retrieves the extended credit lines for a specified business account ID. This function fetches billing information by querying the `/extendedcredits` endpoint, returning financial details such as available credit for platform services. |
| `get_business_account` | Fetches details for a specific Meta Business Account using its ID. This function retrieves the core account object, unlike others that get associated resources like owned/shared WhatsApp Business Accounts (WABAs) or credit lines for the same ID. The response payload can be customized using the 'fields' parameter. |
| `get_commerce_settings` | Retrieves the commerce settings, such as cart availability and catalog visibility, for a specific WhatsApp Business phone number. This function reads the current configuration, contrasting with `set_or_update_commerce_settings` which modifies them. |
| `update_commerce_settings` | Updates the commerce settings for a specific business phone number by enabling or disabling cart functionality and catalog visibility. This function differentiates from `get_commerce_settings` by using a POST request to modify data, rather than retrieving it. |
| `create_upload_session` | Initiates a resumable upload session by providing file metadata (size, type). This function creates an upload session ID and is the first of a two-step process for uploading media, preceding the actual data transfer performed by `resume_session`. |
| `upload_file_to_session` | Continues a media file upload by sending file data to an existing session. This function is the second step in the upload process, following `upload_file`, which creates the session and provides the required session ID. |
| `get_business_phone_number` | Retrieves details for a specific WhatsApp Business phone number by its unique ID. The optional `fields` parameter allows for customizing the response to include only desired data, differentiating it from `get_all_business_phone_numbers`, which retrieves a list of all numbers for a WABA. |
| `list_waba_phone_numbers` | Fetches a list of phone numbers for a specified WhatsApp Business Account (WABA). This function allows for result filtering and customizable field selection, distinguishing it from `get_business_phone_number` which retrieves a single number by its unique ID. |
| `get_qr_code_by_id` | Retrieves the details of a single QR code, such as its pre-filled message, by its unique ID for a specific business phone number. It fetches a specific code, distinguishing it from `get_all_qr_codes_default_fields` which retrieves a list of codes. |
| `delete_qr_code_by_id` | Deletes a specific WhatsApp message QR code by its ID for a given business phone number. The function sends a DELETE request to the Graph API's `message_qrdls` endpoint to remove the specified QR code. |
| `list_qr_codes` | Retrieves a list of QR codes for a business phone number. This function allows optional filtering by a specific QR code identifier and customization of the fields returned in the response, such as the image format. |
| `create_qr_code` | Generates a WhatsApp Business QR code for a specific phone number. This function allows setting a prefilled message for user convenience and can optionally include a custom identifier. It returns the details of the newly created QR code upon successful generation. |
| `get_template_by_id` | Retrieves a specific WhatsApp message template by its unique identifier. Unlike `get_template_by_name`, which searches within a business account, this function directly fetches a single template resource. Note: The function signature is missing the required `template_id` parameter to build a valid URL. |
| `update_template_by_id` | Updates an existing WhatsApp message template, identified by its ID within the request URL. This function modifies the template's category, components, language, and name by submitting new data via a POST request, returning the API response upon successful completion. |
| `get_message_templates` | Retrieves message templates for a specific WhatsApp Business Account (WABA). It can list all templates or, if a name is provided, filter for an exact match. This differs from `get_template_by_id_default_fields`, which fetches a single template by its unique ID. |
| `create_message_template` | Creates a new message template for a specified WhatsApp Business Account (WABA). This function sends a POST request with the template's name, language, category, and structural components, enabling the creation of standardized, reusable messages. |
| `delete_message_template` | Deletes a message template from a WhatsApp Business Account. Templates can be targeted for deletion by providing either a template name, which deletes all language versions, or a specific template ID (`hsm_id`). |
| `get_subscribed_apps` | Retrieves a list of all applications subscribed to receive webhook notifications for a given WhatsApp Business Account (WABA). This function provides a read-only view of current webhook subscriptions, complementing the functions for subscribing and unsubscribing apps. |
| `subscribe_app_to_webhooks` | Subscribes an application to a specific WhatsApp Business Account's (WABA) webhooks using its ID. This enables the app to receive real-time event notifications, differentiating it from functions that list or remove subscriptions. |
| `unsubscribe_app_from_waba` | Removes the webhook subscription for the calling app from a specified WhatsApp Business Account (WABA), stopping it from receiving notifications. This function complements `get_subscribed_apps` and `subscribe_app_to_waba_swebhooks` by handling the deletion of a subscription. |
| `get_all_client_wabas` | Retrieves all client WhatsApp Business Accounts (WABAs) associated with a specific business account ID. It's used by Solution Partners to list WABAs they manage for other businesses, distinguishing them from accounts they directly own (`get_all_owned_wabas`). |
| `get_all_owned_wabas` | Retrieves a list of all WhatsApp Business Accounts (WABAs) directly owned by a specified business account. This is distinct from `get_all_shared_wabas`, which fetches WABAs shared with clients, providing specific access to owned assets instead of associated ones. |
