# BillApp MCP Server

An MCP Server for the BillApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the BillApp API.


| Tool | Description |
|------|-------------|
| `list_customer_attachments` | Get list of customer attachments |
| `create_customer_attachment` | Upload customer attachment |
| `list_invoice_attachments` | Get list of invoice attachments |
| `create_invoice_attachment` | Upload invoice attachment |
| `list_vendor_attachments` | Get list of vendor attachments |
| `create_vendor_attachment` | Upload vendor attachment |
| `get_attachment` | Get attachment details |
| `list_bills` | Get list of bills |
| `create_bill` | Create a bill |
| `create_bulk_bills` | Create multiple bills |
| `get_bill` | Get bill details |
| `replace_bill` | Replace a bill |
| `update_bill` | Update a bill |
| `archive_bill` | Archive a bill |
| `restore_bill` | Restore an archived bill |
| `list_classification_accounting_classes` | Get list of accounting classes |
| `create_classification_accounting_class` | Create an accounting class |
| `bulk_create_classification_accounting_class` | Create multiple accounting classes |
| `bulk_update_classification_accounting_class` | Update multiple accounting classes |
| `bulk_archive_classification_accounting_class` | Archive multiple accounting classes |
| `bulk_restore_classification_accounting_class` | Restore multiple accounting classes |
| `get_classification_accounting_class` | Get accounting class details |
| `update_classification_accounting_class` | Update an accounting class |
| `archive_classification_accounting_class` | Archive an accounting class |
| `restore_classification_accounting_class` | Restore an archived accounting class |
| `list_classification_chart_of_accounts` | Get list of chart of accounts |
| `create_classification_chart_of_accounts` | Create a chart of accounts |
| `bulk_create_classification_chart_of_accounts` | Create multiple chart of accounts |
| `bulk_update_classification_chart_of_accounts` | Update multiple chart of accounts |
| `bulk_archive_classification_chart_of_accounts` | Archive mutliple chart of accounts |
| `bulk_restore_classification_chart_of_accounts` | Restore multiple chart of accounts |
| `get_classification_chart_of_accounts` | Get chart of accounts details |
| `update_classification_chart_of_accounts` | Update a chart of accounts |
| `archive_classification_chart_of_accounts` | Archive a chart of accounts |
| `restore_classification_chart_of_accounts` | Restore an archived chart of accounts |
| `list_classification_departments` | Get list of departments |
| `create_classification_department` | Create a department |
| `bulk_create_classification_department` | Create multiple departments |
| `bulk_update_classification_department` | Update multiple departments |
| `bulk_archive_classification_department` | Archive multiple departments |
| `bulk_restore_classification_department` | Restore multiple departments |
| `get_classification_department` | Get department details |
| `update_classification_department` | Update a department |
| `archive_classification_department` | Archive a department |
| `restore_classification_department` | Restore an archived department |
| `list_classification_employees` | Get list of employees |
| `create_classification_employee` | Create an employee |
| `bulk_create_classification_employee` | Create multiple employees |
| `bulk_update_classification_employee` | Update multiple employees |
| `bulk_archive_classification_employee` | Archive multiple employees |
| `bulk_restore_classification_employee` | Restore multiple employees |
| `get_classification_employee` | Get employee details |
| `update_classification_employee` | Update an employee |
| `archive_classification_employee` | Archive an employee |
| `restore_classification_employee` | Restore an archived employee |
| `list_classification_items` | Get list of items |
| `create_classification_item` | Create an item |
| `bulk_create_classification_item` | Create multiple items |
| `bulk_update_classification_item` | Update multiple items |
| `bulk_archive_classification_item` | Archive multiple items |
| `bulk_restore_classification_item` | Restore multiple items |
| `get_classification_item` | Get item details |
| `update_classification_item` | Update an item |
| `archive_classification_item` | Archive an item |
| `restore_classification_item` | Restore an archived item |
| `list_classification_jobs` | Get list of jobs |
| `create_classification_job` | Create a job |
| `bulk_create_classification_job` | Create multiple jobs |
| `bulk_update_classification_job` | Update multiple jobs |
| `bulk_archive_classification_job` | Archive multiple jobs |
| `bulk_restore_classification_job` | Restore multiple jobs |
| `get_classification_job` | Get job details |
| `update_classification_job` | Update a job |
| `archive_classification_job` | Archive a job |
| `restore_classification_job` | Restore an archived job |
| `list_classification_locations` | Get list of locations |
| `create_classification_location` | Create a location |
| `bulk_create_classification_location` | Create multiple locations |
| `bulk_update_classification_location` | Update multiple locations |
| `bulk_archive_classification_location` | Archive multiple locations |
| `bulk_restore_classification_location` | Restore multiple locations |
| `get_classification_location` | Get location details |
| `update_classification_location` | Update a location |
| `archive_classification_location` | Archive a location |
| `restore_classification_location` | Restore an archived location |
| `list_customers` | Get list of customers |
| `create_customer` | Create a customer |
| `get_customer` | Get customer details |
| `update_customer` | Update a customer |
| `archive_customer` | Archive a customer |
| `restore_customer` | Restore an archived customer |
| `list_documents` | Get list of documents |
| `create_bill_document` | Upload bill document |
| `upload_status` | Get document upload status |
| `get_document` | Get document details |
| `list_payable_apcards` | Get list of AP Cards |
| `list_bank_accounts` | Get list of bank accounts |
| `create_bank_account` | Create a bank account |
| `list_bank_account_users` | Get list of bank account users |
| `nominate_bank_account_user` | Nominate a bank account user |
| `archive_bank_account_user` | Archive a bank account user |
| `get_bank_account` | Get bank account details |
| `update_bank_account` | Update a bank account |
| `archive_bank_account` | Archive a bank account |
| `verify_bank_account` | Verify a bank account |
| `list_payable_card_accounts` | Get list of card accounts |
| `list_card_funding_purposes` | Get card funding purpose |
| `list_card_account_users` | Get list of card account users |
| `get_card_account` | Get card account details |
| `get_funding_account_permission` | Get funding account permissions |
| `get_health_check` | Check app health |
| `list_invoices` | Get list of invoices |
| `create_invoice` | Create an invoice |
| `record_invoice` | Record AR payment |
| `get_invoice` | Get invoice details |
| `replace_invoice` | Replace an invoice |
| `update_invoice` | Update an invoice |
| `archive_invoice` | Archive an invoice |
| `send_invoice` | Send an invoice |
| `restore_invoice` | Restore an archived invoice |
| `login` | API login |
| `get_session_info` | Get API session details |
| `logout` | API logout |
| `generate_challenge` | Generate MFA challenge |
| `validate_challenge` | Validate MFA challenge |
| `list_mfa_phones` | Get list of MFA phone numbers |
| `setup` | Add phone for MFA setup |
| `validate` | Validate phone for MFA setup |
| `step_up_session` | MFA step-up for API session |
| `search` | Search for an organization in the BILL networks |
| `accept_invitation` | Accept network invitation |
| `get_customer_invitation` | Get customer invitation status |
| `create_customer_invitation` | Invite a customer in the BILL network |
| `delete_customer_invitation` | Delete customer connection |
| `get_vendor_invitation` | Get vendor invitation status |
| `create_vendor_invitation` | Invite a vendor in the BILL network |
| `delete_vendor_invitation` | Delete vendor connection |
| `list_industries` | Get list of organization industries |
| `get_organization` | Get organization details |
| `update_organization` | Update an organization |
| `get_price_plan` | Get organization price plan details |
| `partner_login` | API partner login |
| `login_as_user` | API login as user |
| `list_partner_organizations` | Get list of organizations |
| `create_organization` | Create an organization |
| `create_phone` | Add phone for risk verification |
| `list_partner_user_roles` | Get list of user roles |
| `get_partner_user_role` | Get user role details |
| `list_partner_users` | Get list of users |
| `create_partner_user` | Create a user |
| `get_partner_user` | Get user details |
| `update_partner_user` | Update a user |
| `archive_partner_user` | Archive a user |
| `restore_partner_user` | Restore an archived user |
| `list_payments` | Get list of payments |
| `create_payment` | Create a payment |
| `create_bulk_payment` | Create a bulk payment |
| `list_payment_options` | Get list of vendor payment options |
| `get_payment` | Get payment details |
| `cancel_payment` | Cancel a payment |
| `get_check_image_data` | Get check image data |
| `void_payment` | Void a payment |
| `list_recurring_bills` | Get list of recurring bills |
| `create_recurring_bill` | Create a recurring bill |
| `get_recurring_bill` | Get recurring bill details |
| `replace_recurring_bill` | Replace a recurring bill |
| `update_recurring_bill` | Update a recurring bill |
| `archive_recurring_bill` | Archive a recurring bill |
| `restore_recurring_bill` | Restore an archived recurring bill |
| `get_vendor_audit_trail` | Get audit trail details for a vendor |
| `get_risk_verifications` | Get risk verification details |
| `initiate_risk_verifications` | Initiate risk verification for an organization |
| `get_risk_verification_phone` | Get phone status for risk verification |
| `create_risk_verification_phone` | Add phone for risk verification |
| `list_organization_user_roles` | Get list of user roles |
| `get_organization_user_role` | Get user role details |
| `list_budgets` | Get list of budgets |
| `create_budget` | Create a budget |
| `get_budget` | Get budget details |
| `delete_budget` | Delete a budget |
| `update_budget` | Update a budget |
| `list_budget_members` | Get list of members for a budget |
| `upsert_bulk_budget_users` | Update a list of budget members in a budget |
| `get_budget_member` | Get a single member for a budget |
| `upsert_budget_member` | Add a member to a budget or update an existing member of the budget |
| `delete_budget_member` | Delete a member from a budget |
| `list_cards` | Get list of cards |
| `create_budget_card` | Create a vendor card |
| `get_card` | Get card details |
| `delete_card` | Delete a card |
| `update_card` | Update a vendor card |
| `get_pan_jwt` | Get PAN JWT |
| `list_custom_fields` | Get list of custom fields |
| `create_custom_field` | Create custom field |
| `get_custom_field` | Get custom field details |
| `delete_custom_field` | Delete a custom field |
| `update_custom_field` | Update custom field details |
| `list_custom_field_values` | Get list of values for custom field |
| `create_custom_field_values` | Create custom field values |
| `delete_custom_field_value` | Delete custom field values |
| `get_custom_field_values` | Get custom field value |
| `list_reimbursements` | Get list of reimbursements |
| `create_reimbursement` | Create a reimbursement |
| `create_image_upload_url` | Create an image upload URL for a reimbursement. |
| `get_reimbursement` | Get reimbursement details |
| `delete_reimbursement` | Delete a reimbursement |
| `update_reimbursement` | Update a reimbursement |
| `approve_or_deny_reimbursement` | Approve or deny a reimbursement |
| `list_transactions` | Get list of transactions |
| `get_transaction` | Get transaction details |
| `update_transaction` | Update transaction |
| `list_transaction_custom_fields` | Get transaction custom field details |
| `update_transaction_custom_fields` | Update a custom field and values on a transaction |
| `list_transaction_custom_field_values` | Get transaction custom field value details |
| `list_users` | Get list of users |
| `create_user` | Create a user |
| `get_current_user` | Get current user details |
| `get_user` | Get user details |
| `delete_user` | Delete a user |
| `update_user` | Update a user |
| `list_organization_users` | Get list of users |
| `create_organization_user` | Create a user |
| `get_organization_user` | Get user details |
| `update_organization_user` | Update a user |
| `archive_organization_user` | Archive a user |
| `restore_organization_user` | Restore an archived user |
| `list_vendors` | Get list of vendors |
| `create_vendor` | Create a vendor |
| `create_bulk_vendor` | Create multiple vendors |
| `get_intl_config` | Get international payments configuration |
| `get_vendor` | Get vendor details |
| `update_vendor` | Update a vendor |
| `archive_vendor` | Archive a vendor |
| `get_vendor_bank_account` | Get vendor bank account details |
| `create_vendor_bank_account` | Create a vendor bank account |
| `delete_vendor_bank_account` | Delete a vendor bank account |
| `get_configuration_by_vendor_id` | Get vendor configuration |
| `restore_vendor` | Restore an archived vendor |
