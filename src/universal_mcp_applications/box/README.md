# BoxApp MCP Server

An MCP Server for the BoxApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the BoxApp API.


| Tool | Description |
|------|-------------|
| `get_authorize` | Authorize user |
| `post_oauth_token` | Request access token |
| `post_oauth_token_refresh` | Refresh access token |
| `post_oauth_revoke` | Revoke access token |
| `get_files_id` | Get file information |
| `post_files_id` | Restore file |
| `put_files_id` | Update file |
| `delete_files_id` | Delete file |
| `list_file_associations` | List file app item associations |
| `get_files_id_content` | Download file |
| `post_files_id_content` | Upload file version |
| `options_files_content` | Preflight check before upload |
| `post_files_content` | Upload file |
| `post_files_upload_sessions` | Create upload session |
| `post_files_id_upload_sessions` | Create upload session for existing file |
| `get_files_upload_sessions_id` | Get upload session |
| `put_files_upload_sessions_id` | Upload part of file |
| `delete_upload_session_by_id` | Remove upload session |
| `get_upload_session_parts` | List parts |
| `commit_upload_session` | Commit upload session |
| `post_files_id_copy` | Copy file |
| `get_files_id_thumbnail_id` | Get file thumbnail |
| `get_files_id_collaborations` | List file collaborations |
| `get_files_id_comments` | List file comments |
| `get_files_id_tasks` | List tasks on file |
| `get_files_id_trash` | Get trashed file |
| `delete_files_id_trash` | Permanently remove file |
| `get_files_id_versions` | List all file versions |
| `get_files_id_versions_id` | Get file version |
| `delete_files_id_versions_id` | Remove file version |
| `put_files_id_versions_id` | Restore file version |
| `post_files_id_versions_current` | Promote file version |
| `get_files_id_metadata` | List metadata instances on file |
| `get_file_security_classification_by_id` | Get classification on file |
| `update_file_security_classification` | Add classification to file |
| `put_update_file_security_classification` | Update classification on file |
| `delete_file_metadata` | Remove classification from file |
| `get_files_id_metadata_id_id` | Get metadata instance on file |
| `post_files_id_metadata_id_id` | Create metadata instance on file |
| `put_files_id_metadata_id_id` | Update metadata instance on file |
| `delete_files_id_metadata_id_id` | Remove metadata instance from file |
| `get_global_metadata` | List Box Skill cards on file |
| `post_file_metadata_global_box_skills_cards` | Create Box Skill cards on file |
| `update_file_metadata` | Update Box Skill cards on file |
| `delete_file_global_box_skills_cards` | Remove Box Skill cards from file |
| `get_files_id_watermark` | Get watermark on file |
| `put_files_id_watermark` | Apply watermark to file |
| `delete_files_id_watermark` | Remove watermark from file |
| `get_file_requests_id` | Get file request |
| `put_file_requests_id` | Update file request |
| `delete_file_requests_id` | Delete file request |
| `post_file_requests_id_copy` | Copy file request |
| `get_folders_id` | Get folder information |
| `post_folders_id` | Restore folder |
| `put_folders_id` | Update folder |
| `delete_folders_id` | Delete folder |
| `get_folder_app_item_associations` | List folder app item associations |
| `get_folders_id_items` | List items in folder |
| `post_folders` | Create folder |
| `post_folders_id_copy` | Copy folder |
| `get_folders_id_collaborations` | List folder collaborations |
| `get_folders_id_trash` | Get trashed folder |
| `delete_folders_id_trash` | Permanently remove folder |
| `get_folders_id_metadata` | List metadata instances on folder |
| `get_folder_security_classification` | Get classification on folder |
| `post_folder_metadata_security_classification` | Add classification to folder |
| `update_folder_security_classification` | Update classification on folder |
| `delete_security_classification_by_folder_id` | Remove classification from folder |
| `get_folders_id_metadata_id_id` | Get metadata instance on folder |
| `post_folders_id_metadata_id_id` | Create metadata instance on folder |
| `put_folders_id_metadata_id_id` | Update metadata instance on folder |
| `delete_folder_metadata` | Remove metadata instance from folder |
| `get_folders_trash_items` | List trashed items |
| `get_folders_id_watermark` | Get watermark for folder |
| `put_folders_id_watermark` | Apply watermark to folder |
| `delete_folders_id_watermark` | Remove watermark from folder |
| `get_folder_locks` | List folder locks |
| `post_folder_locks` | Create folder lock |
| `delete_folder_locks_id` | Delete folder lock |
| `get_metadata_templates` | Find metadata template by instance ID |
| `get_security_classification_schema` | List all classifications |
| `add_security_classification_schema` | Add classification |
| `update_security_classification_schema` | Update classification |
| `get_schema_template` | Get metadata template by name |
| `update_schema_template` | Update metadata template |
| `delete_metadata_template_schema` | Remove metadata template |
| `get_metadata_templates_id` | Get metadata template by ID |
| `get_metadata_templates_global` | List all global metadata templates |
| `get_metadata_templates_enterprise` | List all metadata templates for enterprise |
| `post_metadata_templates_schema` | Create metadata template |
| `create_metadata_template_classification` | Add initial classifications |
| `get_metadata_cascade_policies` | List metadata cascade policies |
| `post_metadata_cascade_policies` | Create metadata cascade policy |
| `get_metadata_cascade_policy_by_id` | Get metadata cascade policy |
| `delete_metadata_cascade_policy` | Remove metadata cascade policy |
| `apply_metadata_cascade_policy_by_id` | Force-apply metadata cascade policy to folder |
| `execute_metadata_query` | Query files/folders by metadata |
| `get_comments_id` | Get comment |
| `put_comments_id` | Update comment |
| `delete_comments_id` | Remove comment |
| `post_comments` | Create comment |
| `get_collaborations_id` | Get collaboration |
| `put_collaborations_id` | Update collaboration |
| `delete_collaborations_id` | Remove collaboration |
| `get_collaborations` | List pending collaborations |
| `post_collaborations` | Create collaboration |
| `get_search` | Search for content |
| `post_tasks` | Create task |
| `get_tasks_id` | Get task |
| `put_tasks_id` | Update task |
| `delete_tasks_id` | Remove task |
| `get_tasks_id_assignments` | List task assignments |
| `post_task_assignments` | Assign task |
| `get_task_assignments_id` | Get task assignment |
| `put_task_assignments_id` | Update task assignment |
| `delete_task_assignments_id` | Unassign task |
| `get_shared_items` | Find file for shared link |
| `get_files_id_get_shared_link` | Get shared link for file |
| `put_files_id_add_shared_link` | Add shared link to file |
| `update_file_shared_link` | Update shared link on file |
| `remove_shared_link_by_id` | Remove shared link from file |
| `get_shared_items_folders` | Find folder for shared link |
| `get_folders_id_get_shared_link` | Get shared link for folder |
| `put_folders_id_add_shared_link` | Add shared link to folder |
| `update_shared_linkfolder` | Update shared link on folder |
| `remove_shared_link_by_folder_id` | Remove shared link from folder |
| `post_web_links` | Create web link |
| `get_web_links_id` | Get web link |
| `post_web_links_id` | Restore web link |
| `put_web_links_id` | Update web link |
| `delete_web_links_id` | Remove web link |
| `get_web_links_id_trash` | Get trashed web link |
| `delete_web_links_id_trash` | Permanently remove web link |
| `get_shared_items_web_links` | Find web link for shared link |
| `get_shared_link_by_id` | Get shared link for web link |
| `update_web_link_shared_link` | Add shared link to web link |
| `update_shared_link` | Update shared link on web link |
| `remove_shared_link_by_web_link_id` | Remove shared link from web link |
| `get_shared_items_app_items` | Find app item for shared link |
| `get_users` | List enterprise users |
| `post_users` | Create user |
| `get_users_me` | Get current user |
| `post_users_terminate_sessions` | Create jobs to terminate users session |
| `get_users_id` | Get user |
| `put_users_id` | Update user |
| `delete_users_id` | Delete user |
| `get_users_id_avatar` | Get user avatar |
| `post_users_id_avatar` | Add or update user avatar |
| `delete_users_id_avatar` | Delete user avatar |
| `put_users_id_folders` | Transfer owned folders |
| `get_users_id_email_aliases` | List user's email aliases |
| `post_users_id_email_aliases` | Create email alias |
| `delete_email_alias_by_id` | Remove email alias |
| `get_users_id_memberships` | List user's groups |
| `post_invites` | Create user invite |
| `get_invites_id` | Get user invite status |
| `get_groups` | List groups for enterprise |
| `post_groups` | Create group |
| `post_groups_terminate_sessions` | Create jobs to terminate user group session |
| `get_groups_id` | Get group |
| `put_groups_id` | Update group |
| `delete_groups_id` | Remove group |
| `get_groups_id_memberships` | List members of group |
| `get_groups_id_collaborations` | List group collaborations |
| `post_group_memberships` | Add user to group |
| `get_group_memberships_id` | Get group membership |
| `put_group_memberships_id` | Update group membership |
| `delete_group_memberships_id` | Remove user from group |
| `get_webhooks` | List all webhooks |
| `post_webhooks` | Create webhook |
| `get_webhooks_id` | Get webhook |
| `put_webhooks_id` | Update webhook |
| `delete_webhooks_id` | Remove webhook |
| `put_skill_invocations_id` | Update all Box Skill cards on file |
| `options_events` | Get events long poll endpoint |
| `get_events` | List user and enterprise events |
| `get_collections` | List all collections |
| `get_collections_id_items` | List collection items |
| `get_collections_id` | Get collection by ID |
| `get_recent_items` | List recently accessed items |
| `get_retention_policies` | List retention policies |
| `post_retention_policies` | Create retention policy |
| `get_retention_policies_id` | Get retention policy |
| `put_retention_policies_id` | Update retention policy |
| `delete_retention_policies_id` | Delete retention policy |
| `get_retention_policy_assignments` | List retention policy assignments |
| `create_retention_policy_assignment` | Assign retention policy |
| `get_retention_policy_assignment_by_id` | Get retention policy assignment |
| `delete_retention_policy_assignment_by_id` | Remove retention policy assignment |
| `get_files_under_retention` | Get files under retention |
| `get_retention_policy_assignment_file_versions` | Get file versions under retention |
| `get_legal_hold_policies` | List all legal hold policies |
| `post_legal_hold_policies` | Create legal hold policy |
| `get_legal_hold_policies_id` | Get legal hold policy |
| `put_legal_hold_policies_id` | Update legal hold policy |
| `delete_legal_hold_policies_id` | Remove legal hold policy |
| `get_legal_hold_policy_assignments` | List legal hold policy assignments |
| `assign_legal_hold_policy` | Assign legal hold policy |
| `get_legal_hold_policy_assignment` | Get legal hold policy assignment |
| `delete_legal_hold_assignment` | Unassign legal hold policy |
| `get_files_on_hold_by_legl_hld_polcy_asgnmt_id` | List files with current file versions for legal hold policy assignment |
| `get_file_version_retentions` | List file version retentions |
| `get_legal_hold_file_versions_on_hold` | List previous file versions for legal hold policy assignment |
| `get_file_version_retentions_id` | Get retention on file |
| `get_legal_hold` | Get file version legal hold |
| `get_file_version_legal_holds` | List file version legal holds |
| `get_shield_information_barrier_by_id` | Get shield information barrier with specified ID |
| `change_shield_status` | Add changed status of shield information barrier with specified ID |
| `get_shield_information_barriers` | List shield information barriers |
| `create_shield_barriers` | Create shield information barrier |
| `get_shield_information_barrier_reports` | List shield information barrier reports |
| `generate_shield_report` | Create shield information barrier report |
| `get_shield_report_by_id` | Get shield information barrier report by ID |
| `get_shield_segment_by_id` | Get shield information barrier segment with specified ID |
| `delete_shield_inft_barrier_sgmt_by_id` | Delete shield information barrier segment |
| `update_shield_barrier_segment` | Update shield information barrier segment with specified ID |
| `get_shield_segments` | List shield information barrier segments |
| `create_shield_barrier_segments` | Create shield information barrier segment |
| `get_shield_infmt_barrier_sgmnt_member_by_id` | Get shield information barrier segment member by ID |
| `delete_shield_member` | Delete shield information barrier segment member by ID |
| `get_shield_infmt_barrier_sgmnt_members` | List shield information barrier segment members |
| `add_shield_members` | Create shield information barrier segment member |
| `get_shield_barrier_segment_restriction_by_id` | Get shield information barrier segment restriction by ID |
| `delete_shield_restriction` | Delete shield information barrier segment restriction by ID |
| `get_shield_infmt_barrier_sgmnt_restrictions` | List shield information barrier segment restrictions |
| `create_shield_restrictions` | Create shield information barrier segment restriction |
| `get_device_pinners_id` | Get device pin |
| `delete_device_pinners_id` | Remove device pin |
| `list_device_pins` | List enterprise device pins |
| `get_terms_of_services` | List terms of services |
| `post_terms_of_services` | Create terms of service |
| `get_terms_of_services_id` | Get terms of service |
| `put_terms_of_services_id` | Update terms of service |
| `get_tos_user_statuses` | List terms of service user statuses |
| `create_terms_of_service_statuses` | Create terms of service status for new user |
| `update_terms_of_service_user_status_by_id` | Update terms of service status for existing user |
| `list_collaboration_whitelist_entries` | List allowed collaboration domains |
| `create_collaboration_whitelist_entry` | Add domain to list of allowed collaboration domains |
| `get_whitelist_entry_by_id` | Get allowed collaboration domain |
| `delete_collaboration_whitelist_entry_by_id` | Remove domain from list of allowed collaboration domains |
| `list_whitelist_targets` | List users exempt from collaboration domain restrictions |
| `create_collaboration_whitelist_exempt_target` | Create user exemption from collaboration domain restrictions |
| `get_exempt_target_by_id` | Get user exempt from collaboration domain restrictions |
| `delete_collab_whitelist_exempt_target_by_id` | Remove user from list of users exempt from domain restrictions |
| `get_storage_policies` | List storage policies |
| `get_storage_policies_id` | Get storage policy |
| `get_storage_policy_assignments` | List storage policy assignments |
| `create_storage_policy_assignment` | Assign storage policy |
| `get_storage_policy_assignment` | Get storage policy assignment |
| `update_storage_policy_assignment` | Update storage policy assignment |
| `delete_storage_policy_assignment` | Unassign storage policy |
| `post_zip_downloads` | Create zip download |
| `get_zip_downloads_id_content` | Download zip archive |
| `get_zip_downloads_id_status` | Get zip download status |
| `post_sign_requests_id_cancel` | Cancel Box Sign request |
| `post_sign_requests_id_resend` | Resend Box Sign request |
| `get_sign_requests_id` | Get Box Sign request by ID |
| `get_sign_requests` | List Box Sign requests |
| `post_sign_requests` | Create Box Sign request |
| `get_workflows` | List workflows |
| `post_workflows_id_start` | Starts workflow based on request body |
| `get_sign_templates` | List Box Sign templates |
| `get_sign_templates_id` | Get Box Sign template by ID |
| `get_integration_mappings_slack` | List Slack integration mappings |
| `create_slack_mapping` | Create Slack integration mapping |
| `update_slack_integration_mapping_by_id` | Update Slack integration mapping |
| `delete_slack_mapping_by_id` | Delete Slack integration mapping |
| `get_integration_mappings_teams` | List Teams integration mappings |
| `create_integration_mapping_team` | Create Teams integration mapping |
| `update_integration_mapping_team` | Update Teams integration mapping |
| `delete_integration_mapping_by_id` | Delete Teams integration mapping |
| `post_ai_ask` | Ask question |
| `post_ai_text_gen` | Generate text |
| `get_ai_agent_default` | Get AI agent default configuration |
| `post_ai_extract` | Extract metadata (freeform) |
| `post_ai_extract_structured` | Extract metadata (structured) |
| `get_ai_agents` | List AI agents |
| `post_ai_agents` | Create AI agent |
| `put_ai_agents_id` | Update AI agent |
| `get_ai_agents_id` | Get AI agent by agent ID |
| `delete_ai_agents_id` | Delete AI agent |
| `post_docgen_templates_v` | Create Box Doc Gen template |
| `get_docgen_templates_v` | List Box Doc Gen templates |
| `delete_template_by_id` | Delete Box Doc Gen template |
| `get_docgen_template_by_id` | Get Box Doc Gen template by ID |
| `get_docgen_template_tags` | List all Box Doc Gen template tags in template |
| `get_docgen_jobs_id_v` | Get Box Doc Gen job by ID |
| `get_docgen_jobs_v` | List all Box Doc Gen jobs |
| `get_template_job` | Get list of all Box Doc Gen jobs for template |
| `get_batch_job_details` | Get Box Doc Gen jobs by batch ID |
| `post_docgen_batches_v` | Generate document using Box Doc Gen template |
| `get_shield_lists_v` | Get all shield lists in enterprise |
| `post_shield_lists_v` | Create shield list |
| `get_shield_lists_id_v` | Get single shield list by shield list id |
| `delete_shield_lists_id_v` | Delete single shield list by shield list id |
| `put_shield_lists_id_v` | Update shield list |
