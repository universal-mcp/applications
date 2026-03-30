# SmartleadApp MCP Server

An MCP Server for the SmartleadApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the SmartleadApp API.


| Tool | Description |
|------|-------------|
| `call_smartlead_api` | Dynamically call any Smartlead API endpoint. Use this for operations that don't have a specific tool built. |
| `list_campaigns` | List all campaigns. |
| `get_campaign` | Get campaign details by ID. |
| `create_campaign` | Create a new campaign. |
| `update_campaign_status` | Update the status of a campaign. |
| `update_campaign_schedule` | Adjusts the active sending schedule for a defined campaign, such as modifying the timezone, allowed days, and specific operating hours for email dispatch. |
| `update_campaign_settings` | Modifies the broader settings of an existing campaign, allowing you to update sending limits, stop conditions, tracking preferences, and AI ESP matching behaviors. |
| `get_campaign_sequences` | Fetch sequences of a campaign. |
| `save_campaign_sequence` | Save or update a campaign sequence. |
| `delete_campaign` | Permanently deletes a specified email campaign from the workspace. This action removes associated sequence data and tracking history. |
| `list_campaign_email_accounts` | List all email accounts assigned to a campaign. |
| `add_campaign_email_account` | Add email accounts to a campaign. |
| `remove_campaign_email_account` | Remove an email account from a campaign. |
| `get_lead_campaigns` | Fetch all campaigns that a specific lead is part of. |
| `list_email_accounts` | List all connected email accounts. |
| `create_email_account` | Connect a new email account (SMTP/IMAP) or save settings. |
| `update_email_account` | Updates the signature, daily sending limits, reply-to addresses, or custom tracking domains of a connected sender mailbox. |
| `get_email_account` | Get details for a specific email account by ID. |
| `configure_email_account_warmup` | Configure warmup settings for an email account. |
| `get_email_account_warmup_stats` | Retrieve warmup statistics for an email account. |
| `list_campaign_leads` | Retrieve leads within a specific campaign (supports pagination). |
| `get_lead_by_email` | Fetch a single lead by their email address. |
| `fetch_lead_categories` | Fetch lead categories available inside the system. |
| `add_leads_to_campaign` | Pushes a batch of new leads (prospects) into an active campaign, populating their custom variables and queueing them for outreach. |
| `update_lead` | Updates the core profile information (name, company, variables) of a lead horizontally across the entire global CRM. |
| `pause_lead_in_campaign` | Pause sequence sending for a lead. |
| `resume_lead_in_campaign` | Resume an actively paused sequence for a lead inside a campaign. |
| `delete_lead_from_campaign` | Permanently clears a lead from a campaign, erasing their sequence presence while keeping overall historical analytics intact. |
| `unsubscribe_lead_from_campaign` | Removes a lead from a specific campaign's active queue and marks them as unsubscribed for that campaign only. |
| `unsubscribe_lead_globally` | Permanently adds a lead to the workspace wide 'Do Not Contact' list, blocking them from receiving emails from any campaign. |
| `add_domain_block_list` | Add an email domain or singular target to block list routing rule. |
| `get_lead_message_history` | Fetch full thread history for a lead on a specific campaign. |
| `reply_to_lead_email_thread` | Sends an automated reply to the thread. |
| `export_campaign_leads` | Fetch campaign leads for CSV-friendly export structure. |
| `get_campaign_statistics` | Returns granular reporting values and statuses for a target campaign ID. |
| `get_campaign_analytics_by_date` | Fetch summary metrics split across a date constraint. |
| `get_campaign_analytics` | Pulls down lifetime analytical accumulations for a target scenario. |
| `get_global_analytics_overview` | System-level analytics roll-up detailing macro behavior results across all execution tracks. |
| `list_webhooks` | List all webhooks. |
| `create_webhook` | Registers a new global workspace webhook to stream payload events (clicks, opens, replies) to an external API. |
| `update_webhook` | Modifies the URL endpoint or the event triggering scope of an existing global workspace webhook. |
| `delete_webhook` | Permanently deletes a global workspace webhook, immediately stopping all event streaming to that endpoint. |
| `get_all_campaigns` | Fetches a comprehensive list of all email outreach campaigns configured within the Smartlead account. This is useful for retrieving campaign metadata such as active status, general settings, and schedule information across the entire workspace. |
| `get_campaign_by_id` | Retrieves the detailed configuration, tracking settings, and scheduling parameters for a specific email campaign identified by its unique campaign ID. |
| `update_campaign_settings` | Modifies the broader settings of an existing campaign, allowing you to update sending limits, stop conditions, tracking preferences, and AI ESP matching behaviors. |
| `update_campaign_schedule` | Adjusts the active sending schedule for a defined campaign, such as modifying the timezone, allowed days, and specific operating hours for email dispatch. |
| `delete_campaign` | Permanently deletes a specified email campaign from the workspace. This action removes associated sequence data and tracking history. |
| `update_campaign_sequences` | Overwrites or modifies the series of email sequences (steps, content threads, and wait delays) defined within a specific outreach campaign. |
| `add_email_accounts_to_campaign` | Links one or more configured sender email accounts to an active campaign, allowing them to participate in the dispatch pool. |
| `remove_email_accounts_from_campaign` | Detaches specific sender email accounts from a campaign, preventing them from sending any further emails on behalf of that campaign. |
| `create_subsequence_campaign` | Generates a subsequence (a follow-up branching sequence) tied to a parent campaign to handle specifically categorized lead replies. |
| `forward_campaign_email` | Forwards a specific email from a campaign thread to another email address, typically used for manual escalation or CRM dumping. |
| `reply_to_campaign_lead` | Dispatches a direct, manual email reply to a specific lead within the context of their existing campaign thread. |
| `send_test_email` | Dispatches a test email from the campaign's sequence to a designated inbox to verify formatting, variable injection, and deliverability. |
| `update_campaign_team_member` | Assigns or modifies the team member responsible for managing and overseeing a specific email campaign. |
| `add_leads_to_campaign` | Pushes a batch of new leads (prospects) into an active campaign, populating their custom variables and queueing them for outreach. |
| `get_bulk_lead_message_history` | Retrieves the complete historical messaging thread (emails sent, replies received) for multiple leads simultaneously within a campaign. |
| `update_campaign_lead_details` | Modifies the custom variables, firmographic data, or personal details of a specific lead residing within a campaign. |
| `update_lead_category_in_campaign` | Categorizes a lead based on their engagement (e.g., 'Interested', 'Do Not Contact', 'Meeting Booked') within a specific campaign. |
| `update_lead_email_account` | Overrides the round-robin sender assignment and locks a specific lead to be emailed exclusively from a designated email account. |
| `pause_campaign_lead` | Suspends all upcoming automated sequence emails for a specific lead within a campaign without completely removing them. |
| `resume_campaign_lead` | Re-activates a previously paused lead, allowing the campaign to continue sending them the next scheduled sequence steps. |
| `mark_lead_as_complete` | Manually flags a lead as having finished the campaign, preventing any further sequence steps from being dispatched to them. |
| `unsubscribe_lead_from_campaign` | Removes a lead from a specific campaign's active queue and marks them as unsubscribed for that campaign only. |
| `delete_lead_from_campaign` | Permanently clears a lead from a campaign, erasing their sequence presence while keeping overall historical analytics intact. |
| `create_update_campaign_webhook` | Configures a webhook endpoint specifically for a single campaign to listen for events like replies, opens, or link clicks. |
| `delete_campaign_webhook` | Removes a designated webhook configuration from a specific campaign. |
| `retrigger_campaign_webhooks` | Forces a manual replay of webhook payloads for a specific campaign if previous webhook deliveries failed or were disrupted. |
| `add_leads_to_campaign` | Pushes a batch of new leads (prospects) into an active campaign, populating their custom variables and queueing them for outreach. |
| `update_lead` | Updates the core profile information (name, company, variables) of a lead horizontally across the entire global CRM. |
| `delete_lead_from_campaign` | Permanently clears a lead from a campaign, erasing their sequence presence while keeping overall historical analytics intact. |
| `pause_lead` | Globally suspends a lead across all active campaigns they belong to, temporarily halting all outreach efforts to them. |
| `resume_lead` | Globally unpauses a lead, re-enabling email dispatch for any active campaigns they are enrolled in. |
| `unsubscribe_lead_globally` | Permanently adds a lead to the workspace wide 'Do Not Contact' list, blocking them from receiving emails from any campaign. |
| `create_lead_note` | Attaches a plain-text internal CRM note to a specific lead's profile for team collaboration and context sharing. |
| `create_lead_task` | Creates an actionable task or reminder tied to a specific lead inside the master inbox pipeline. |
| `create_tag` | Creates a new organizational tag within the workspace that can later be applied to leads, campaigns, or accounts. |
| `add_tags_to_lead` | Assigns one or more existing organizational tags to a specific lead's profile for segmentation and filtering. |
| `remove_tag_from_lead` | Strips a specific organizational tag from a lead's profile. |
| `create_lead_list` | Generates a new, empty static segment or list designed to group leads together logically before pushing them to campaigns. |
| `update_lead_list` | Renames or modifies the properties of an existing static lead list. |
| `delete_lead_list` | Deletes a static lead list. This does not delete the leads themselves, only the organizational grouping. |
| `import_leads_to_list` | Ingests a batch of new prospects into a specifically targeted static lead list. |
| `move_leads_between_lists` | Migrates a set of leads from one static lead list to another within the global CRM. |
| `push_leads_to_campaign` | Transfers all leads residing within a specified lead list directly into an active email campaign. |
| `assign_tags_to_lead_lists` | Applies categorical tags to an entire static lead list for enhanced workspace organization. |
| `add_smtp_email_account` | Connects a new sender mailbox to the workspace using raw SMTP and IMAP protocol credentials. |
| `add_oauth_email_account` | Connects a new sender mailbox to the workspace using modern OAuth2 authorization (Google Workspace, Microsoft 365). |
| `update_email_account` | Updates the signature, daily sending limits, reply-to addresses, or custom tracking domains of a connected sender mailbox. |
| `delete_email_account` | Permanently disconnects an email account from the workspace and removes it from all active campaigns. |
| `update_warmup_settings` | Configures the daily warmup volumes, reply rates, and ramp-up increments for a connected email account to build reputation. |
| `suspend_email_account` | Manually pauses an email account, preventing it from sending out campaign emails while keeping its configuration intact. |
| `unsuspend_email_account` | Reactivates a temporarily suspended email account so it can resume dispatching campaign emails. |
| `create_email_account_tag` | Creates an organizational tag specifically purposed for grouping and filtering sender email accounts. |
| `get_email_account_tags` | Retrieves the full list of tags that exist for email account segmentation. |
| `assign_tags_to_email_accounts` | Applies a specific category tag to an email account (e.g., applying 'Tier 1 Senders' to premium accounts). |
| `remove_tags_from_email_accounts` | Removes an assigned category tag from a specific sender email account. |
| `get_inbox_replies` | Fetches a stream of incoming prospect replies aggregated into the Master Inbox, optionally filtered by status or campaign. |
| `get_sent_emails` | Retrieves a log of all recent outbound emails dispatched across active campaigns from the Master Inbox perspective. |
| `get_assigned_to_me` | Fetches inbox threads and lead conversations that have been specifically delegated to the currently authenticated user. |
| `get_unread_replies` | Pulls exactly the threads in the Master Inbox that have not yet been marked as read by any team member. |
| `get_important_emails` | Retrieves inbox threads that have been artificially flagged or starred as high-priority. |
| `get_snoozed_emails` | Fetches the list of inbox threads that were temporarily snoozed and are awaiting their delayed re-appearance. |
| `get_scheduled_emails` | Retrieves emails that have been drafted inside the Master Inbox and scheduled to be dispatched at a later time. |
| `get_reminder_emails` | Fetches inbox items that have active follow-up reminders attached to them. |
| `get_archived_emails` | Pulls threads from the Master Inbox that have been successfully resolved and tucked away into the archive. |
| `get_custom_view_emails` | Retrieves inbox items conforming to a saved custom filter view configured by the user. |
| `get_inbox_item_by_id` | Fetches the precise conversation thread details and metadata for a specific interaction in the Master Inbox. |
| `get_untracked_replies` | Retrieves email replies that have hit connected mailboxes but could not be definitively matched to an active campaign lead. |
| `reply_to_email` | Dispatches a manual reply from the Master Inbox directly to a prospect's email thread. |
| `forward_email` | Forwards an existing Master Inbox thread to an external third-party email address. |
| `change_read_status` | Toggles whether an inbox thread shows as read or unread for the team. |
| `update_lead_category` | Classifies the lead's intent (e.g., 'Positive Reply', 'Meeting Booked') directly from the Master Inbox interface. |
| `update_lead_revenue` | Attaches a projected or closed dollar revenue amount to a lead after a successful inbox interaction. |
| `assign_team_member` | Delegates a specific Master Inbox conversation thread to a particular team member for handling. |
| `create_lead_task` | Creates an actionable task or reminder tied to a specific lead inside the master inbox pipeline. |
| `create_lead_note` | Attaches a plain-text internal CRM note to a specific lead's profile for team collaboration and context sharing. |
| `block_email_domains` | Adds an entire email domain to the global blocklist, preventing any future outreach to corporate addresses belonging to it. |
| `resume_paused_lead` | Quickly unpauses a lead directly from the Master Inbox so sequence emails can continue after a manual review. |
| `set_lead_reminder` | Attaches a time-based reminder to a Master Inbox thread to ensure the team follows up manually later. |
| `push_lead_to_subsequence` | Transitions a lead from their current active campaign directly into a separate follow-up subsequence via the Master Inbox. |
| `create_manual_placement_test` | Initiates a manual Smart Delivery spam placement test to analyze inbox vs spam folder landing percentages. |
| `create_automated_placement_test` | Schedules a recurring Smart Delivery automated placement test to monitor long-term sender reputation health. |
| `delete_tests_in_bulk` | Removes a batch of historical spam placement test reports from the Smart Delivery module. |
| `stop_automated_test` | Halts an ongoing recurring automated placement test from continuing its future scheduled dispatches. |
| `list_all_tests` | Retrieves the historical log of all spam placement tests performed within the workspace. |
| `provider_wise_report` | Fetches a deliverability breakdown showing inbox placement success split specifically by ESP (Google, Microsoft, Zoho). |
| `geo_wise_report` | Retrieves a geographical deliverability report highlighting spam placement across different global regions. |
| `spam_filter_report` | Fetches an analysis report checking domains against massive enterprise spam filters (Barracuda, Mimecast, Proofpoint). |
| `rdns_report` | Retrieves validation checks evaluating the Reverse DNS (rDNS/PTR) configuration of connected mail servers. |
| `create_folder` | Generates a navigational folder within Smart Delivery to organize bulk sender domains and accounts. |
| `delete_folder` | Deletes a designated organizational folder from the Smart Delivery view. |
| `auto_generate_mailboxes` | Utilizes the Smart Senders protocol to automatically purchase, configure, and warm up new sender domains and mailboxes. |
| `place_order` | Submits a financial transaction order to purchase customized domain infrastructural assets through Smart Senders. |
| `create_webhook` | Registers a new global workspace webhook to stream payload events (clicks, opens, replies) to an external API. |
| `update_webhook` | Modifies the URL endpoint or the event triggering scope of an existing global workspace webhook. |
| `delete_webhook` | Permanently deletes a global workspace webhook, immediately stopping all event streaming to that endpoint. |
| `verify_email` | Passes an email address through the internal utility verification layer to determine if the address is valid, risky, or invalid. |
| `send_single_email` | Transmits a singular, one-off transactional or direct email from a chosen sender account without needing a campaign. |
| `domain_block_list_management` | Retrieves or manipulates the master blocklist detailing all domains explicitly omitted from any system outreach. |
| `create_client` | Creates a distinct 'Client' grouping container inside the workspace to segregate campaigns and billing for agency users. |
| `update_client` | Modifies the name, constraints, or branding elements of an existing Client container. |
| `manage_client_api_keys` | Generates or revokes the specific sub-API keys delegated strictly to a defined Client workspace. |
| `search_contacts_api` | Queries the massive Smart Prospect B2B database to find net-new leads matching specific firmographic and demographic filters. |
| `get_contacts_api` | Retrieves the enriched profiles and details of B2B contacts that were successfully found and unlocked from Smart Prospect. |
| `fetch_contacts_api` | Initiates the backend credit-based unlock process to fetch and reveal verified email addresses for searched contacts. |
| `find_emails_api` | Submits a raw list of names and companies to algorithmically guess, verify, and return their correct B2B email addresses. |
| `review_contacts_api` | Allows parsing through the unlocked contact records from a previous Smart Prospect search run. |
| `save_search_api` | Persists a complex set of Smart Prospect B2B search filter parameters natively so the query can be tracked or re-run later. |
| `saved_searches_api` | Retrieves the list of memorized B2B prospect search configurations saved by the user. |
| `fetched_searches_api` | Pulls historical logs of previous Smart Prospect searches where lead credits were actively spent and emails were revealed. |
| `recent_searches_api` | Retrieves a lightweight audit log of the most heavily recent prospect queries executed across the workspace. |
| `update_saved_search_api` | Modifies the filter parameters of a previously persisted Smart Prospect search configuration. |
| `update_fetched_lead_api` | Edits the profile metadata of a lead that was natively sourced from the Smart Prospect database prior to campaign injection. |
| `search_analytics_api` | Retrieves reporting data surrounding the usage, unlock volume, and credit expenditure executed across the Smart Prospect module. |
| `reply_analytics_api` | Fetches analytics tracking the downstream reply rate and performance of leads specifically sourced from Smart Prospect. |
| `cities_api` | Provides a standardized list of identifiable city parameters universally matched by the Smart Prospect filtering engine. |
| `states_api` | Provides a standardized dictionary of state or regional parameters available for B2B geographical prospect filtering. |
| `countries_api` | Returns the complete array of ISO country parameters supported by the Smart Prospect engine. |
| `company_api` | Queries auto-complete data or firmographic profiles to match target companies during prospect building. |
| `domain_api` | Validates or searches for B2B company domains exclusively to find prospect matches working at those addresses. |
| `industries_api` | Provides the top-level macro industry categories (e.g., 'Software Development', 'Finance') supported by Smart Prospect. |
| `sub_industries_api` | Provides the highly granular micro-industry classifications available for hyper-focused prospect filtering. |
| `departments_api` | Returns the list of corporate department categories (e.g., 'Engineering', 'Marketing') to filter prospects by their team alignment. |
| `levels_api` | Retrieves the recognized corporate hierarchy seniority levels (e.g., 'C-Level', 'VP', 'Manager') for role-based targeting. |
| `job_title_api` | Queries the database for specific custom job title permutations aligned with known demographic records. |
| `head_counts_api` | Provides the structured company employee headcount brackets (e.g., '51-200', '1000+') supported for filtering. |
| `revenue_api` | Returns the structured corporate financial revenue brackets available for qualifying B2B targets. |
| `keywords_api` | Allows searching for highly specific context keywords embedded within the company descriptions or prospect bios. |
