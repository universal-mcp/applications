# WhatsappBusinessApp MCP Server

An MCP Server for the WhatsappBusinessApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the WhatsappBusinessApp API.


| Tool | Description |
|------|-------------|
| `get_analytics` | Retrieves details of a specified WhatsApp Business Account (WABA) with customizable fields using the GET method. |
| `get_credit_lines` | Retrieves the extended credit lines available for a specified business account using its ID. |
| `get_business_account` | Retrieves information about a business account using the specified API version and business account ID, optionally filtering the response fields via a query parameter. |
| `get_commerce_settings` | Retrieves the commerce settings configured for a specific WhatsApp Business phone number. |
| `set_or_update_commerce_settings` | Updates WhatsApp Business commerce settings (cart availability and catalog visibility) for a specific business phone number. |
| `upload_file` | Uploads a file using the specified API version and application ID, with optional query parameters for file length and type, and returns a successful status message upon completion. |
| `resume_session` | Initiates a session using the provided SESSION_ID and file offset specified in the header, supporting further session-related operations via the POST method at the "/{api-version}/<SESSION_ID>" endpoint. |
| `get_business_phone_number` | Retrieves details for a specific business phone number ID using query parameters to specify returned fields. |
| `get_all_business_phone_numbers` | Retrieves a list of phone numbers associated with a specific WhatsApp Business Account (WABA), allowing for filtering and customization of the response fields. |
| `get_qr_code` | Retrieves a message linked to a specific QR code for a business phone number using the GET method via the API. |
| `delete_qr_code` | Deletes a specific WhatsApp Business QR code using the provided QR code ID and returns a success message if the operation is completed successfully. |
| `get_all_qr_codes_default_fields` | Retrieves a list of message QR code deep links associated with a business phone number, filtered by specified fields and QR code identifiers. |
| `create_qr_code` | Creates a WhatsApp Business QR code with a predefined message and returns the generated code details. |
| `get_template_by_id_default_fields` | Retrieves a template using the specified template ID from the API version path. |
| `edit_template` | Creates or processes a resource using the specified template ID based on the API version and returns a successful status upon completion. |
| `get_template_by_name_default_fields` | Retrieves a list of WhatsApp message templates associated with a specific WhatsApp Business Account using the "GET" method, allowing filtering by template name. |
| `create_message_template` | Creates a new WhatsApp message template for a business account, allowing businesses to send standardized messages to customers. |
| `delete_template_by_name` | Deletes WhatsApp message templates by name (all languages) or specific ID using query parameters and returns a success status. |
| `get_subscribed_apps` | Retrieves a list of apps subscribed to webhooks for a WhatsApp Business Account using the GET method. |
| `subscribe_app_to_waba_swebhooks` | Subscribes an app to webhooks for a WhatsApp Business Account (WABA) using the POST method at the `/subscribed_apps` endpoint, allowing the app to receive updates and notifications from the WABA. |
| `unsubscribe_apps_by_waba_id` | Unsubscribes an app from webhook notifications for a WhatsApp Business Account. |
| `get_all_shared_wabas` | Retrieves information about WhatsApp Business accounts associated with a business client, using the specified business account ID and API version. |
| `get_all_owned_wabas` | Retrieves a list of WhatsApp Business Accounts owned by or shared with the specified business account using a GET request to the given endpoint. |
