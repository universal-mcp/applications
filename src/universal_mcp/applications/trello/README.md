# TrelloApp MCP Server

An MCP Server for the TrelloApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the TrelloApp API.


| Tool | Description |
|------|-------------|
| `get_actions_id` | Get an Action |
| `put_actions_id` | Update an Action |
| `delete_actions_id` | Delete an Action |
| `get_actions_id_field` | Get a specific field on an Action |
| `get_actions_id_board` | Get the Board for an Action |
| `get_actions_id_card` | Get the Card for an Action |
| `get_actions_id_list` | Get the List for an Action |
| `get_actions_id_member` | Get the Member of an Action |
| `get_actions_id_membercreator` | Get the Member Creator of an Action |
| `get_actions_id_organization` | Get the Organization of an Action |
| `put_actions_id_text` | Update a Comment Action |
| `get_actions_idaction_reactions` | Get Action's Reactions |
| `create_reaction_to_action` | Create Reaction for Action |
| `get_action_reaction_by_id` | Get Action's Reaction |
| `delete_reaction_by_id_action` | Delete Action's Reaction |
| `get_action_reactions_summary` | List Action's summary of Reactions |
| `applications_key_compliance` | Get Application's compliance data |
| `get_batch` | Batch Requests |
| `get_boards_id_memberships` | Get Memberships of a Board |
| `get_boards_id` | Get a Board |
| `put_boards_id` | Update a Board |
| `delete_boards_id` | Delete a Board |
| `get_boards_id_field` | Get a field on a Board |
| `get_boards_id_actions` | Get Actions of a Board |
| `get_boards_id_boardstars` | Get boardStars on a Board |
| `boards_id_checklists` | Get Checklists on a Board |
| `get_boards_id_cards` | Get Cards on a Board |
| `get_boards_id_cards_filter` | Get filtered Cards on a Board |
| `get_boards_id_customfields` | Get Custom Fields for Board |
| `get_boards_id_labels` | Get Labels on a Board |
| `post_boards_id_labels` | Create a Label on a Board |
| `get_boards_id_lists` | Get Lists on a Board |
| `post_boards_id_lists` | Create a List on a Board |
| `get_boards_id_lists_filter` | Get filtered Lists on a Board |
| `get_boards_id_members` | Get the Members of a Board |
| `put_boards_id_members` | Invite Member to Board via email |
| `put_boards_id_members_idmember` | Add a Member to a Board |
| `boardsidmembersidmember` | Remove Member from Board |
| `update_membership` | Update Membership of Member on a Board |
| `update_board_email_position` | Update emailPosition Pref on a Board |
| `update_board_my_prefs_id_email_list` | Update idEmailList Pref on a Board |
| `update_board_sidebar_pref` | Update showSidebar Pref on a Board |
| `update_board_sidebar_act_pref` | Update showSidebarActivity Pref on a Board |
| `update_board_sidebar_actions` | Update showSidebarBoardActions Pref on a Board |
| `update_board_prefs_show_members` | Update showSidebarMembers Pref on a Board |
| `post_boards` | Create a Board |
| `generate_calendar_key` | Create a calendarKey for a Board |
| `generate_board_email_key` | Create a emailKey for a Board |
| `post_boards_id_idtags` | Create a Tag for a Board |
| `post_boards_id_markedasviewed` | Mark Board as viewed |
| `get_boards_id_boardplugins` | Get Enabled Power-Ups on Board |
| `post_boards_id_boardplugins` | Enable a Power-Up on a Board |
| `delete_boards_id_boardplugins` | Disable a Power-Up on a Board |
| `get_board_id_plugins` | Get Power-Ups on a Board |
| `post_cards` | Create a new Card |
| `get_cards_id` | Get a Card |
| `put_cards_id` | Update a Card |
| `delete_cards_id` | Delete a Card |
| `get_cards_id_field` | Get a field on a Card |
| `get_cards_id_actions` | Get Actions on a Card |
| `get_cards_id_attachments` | Get Attachments on a Card |
| `post_cards_id_attachments` | Create Attachment On Card |
| `get_attachment_by_id` | Get an Attachment on a Card |
| `delete_attachment_by_id` | Delete an Attachment on a Card |
| `get_cards_id_board` | Get the Board the Card is on |
| `get_cards_id_checkitemstates` | Get checkItems on a Card |
| `get_cards_id_checklists` | Get Checklists on a Card |
| `post_cards_id_checklists` | Create Checklist on a Card |
| `check_card_item` | Get checkItem on a Card |
| `update_card_check_item` | Update a checkItem on a Card |
| `delete_card_check_item` | Delete checkItem on a Card |
| `get_cards_id_list` | Get the List of a Card |
| `get_cards_id_members` | Get the Members of a Card |
| `get_cards_id_membersvoted` | Get Members who have voted on a Card |
| `cardsidmembersvoted` | Add Member vote to Card |
| `get_cards_id_plugindata` | Get pluginData on a Card |
| `get_cards_id_stickers` | Get Stickers on a Card |
| `post_cards_id_stickers` | Add a Sticker to a Card |
| `get_card_sticker` | Get a Sticker on a Card |
| `delete_sticker_by_id` | Delete a Sticker on a Card |
| `update_card_sticker_by_id_sticker` | Update a Sticker on a Card |
| `update_card_action_comment` | Update Comment Action on a Card |
| `delete_comment_action` | Delete a comment on a Card |
| `update_card_custom_field_item` | Update Custom Field item on Card |
| `put_cards_idcard_customfields` | Update Multiple Custom Field items on Card |
| `get_cards_id_customfielditems` | Get Custom Field Items for a Card |
| `post_cards_id_actions_comments` | Add a new comment to a Card |
| `post_cards_id_idlabels` | Add a Label to a Card |
| `post_cards_id_idmembers` | Add a Member to a Card |
| `post_cards_id_labels` | Create a new Label on a Card |
| `mark_notifications_read` | Mark a Card's Notifications as read |
| `delete_card_id_label_by_id` | Remove a Label from a Card |
| `delete_id_idmembers_idmember` | Remove a Member from a Card |
| `delete_card_voter` | Remove a Member's Vote on a Card |
| `update_check_item` | Update Checkitem on Checklist on Card |
| `delete_checklist_by_id` | Delete a Checklist on a Card |
| `post_checklists` | Create a Checklist |
| `get_checklists_id` | Get a Checklist |
| `put_checlists_id` | Update a Checklist |
| `delete_checklists_id` | Delete a Checklist |
| `get_checklists_id_field` | Get field on a Checklist |
| `put_checklists_id_field` | Update field on a Checklist |
| `get_checklists_id_board` | Get the Board the Checklist is on |
| `get_checklists_id_cards` | Get the Card a Checklist is on |
| `get_checklists_id_checkitems` | Get Checkitems on a Checklist |
| `post_checklists_id_checkitems` | Create Checkitem on Checklist |
| `get_check_item_detail` | Get a Checkitem on a Checklist |
| `delete_checklist_item_by_id` | Delete Checkitem from Checklist |
| `post_customfields` | Create a new Custom Field on a Board |
| `get_customfields_id` | Get a Custom Field |
| `put_customfields_id` | Update a Custom Field definition |
| `delete_customfields_id` | Delete a Custom Field definition |
| `get_customfields_id_options` | Add Option to Custom Field dropdown |
| `post_customfields_id_options` | Get Options of Custom Field drop down |
| `get_custom_field_option_by_id` | Get Option of Custom Field dropdown |
| `delete_custom_field_option` | Delete Option of Custom Field dropdown |
| `emoji` | List available Emoji |
| `get_enterprises_id` | Get an Enterprise |
| `get_enterprises_id_auditlog` | Get auditlog data for an Enterprise |
| `get_enterprises_id_admins` | Get Enterprise admin Members |
| `get_enterprises_id_signupurl` | Get signupUrl for Enterprise |
| `get_users_id` | Get Users of an Enterprise |
| `get_enterprises_id_members` | Get Members of Enterprise |
| `get_member_details` | Get a Member of Enterprise |
| `get_organization_transfer` | Get whether an organization can be transferred to an enterprise. |
| `list_enterprise_transferrables_by_org_ids` | Get a bulk list of organizations that can be transferred to an enterprise. |
| `bulk_join_enterprise_requests` | Decline enterpriseJoinRequests from one organization or a bulk list of organizations. |
| `list_claimable_orgs` | Get ClaimableOrganizations of an Enterprise |
| `get_pending_organizations` | Get PendingOrganizations of an Enterprise |
| `post_enterprises_id_tokens` | Create an auth Token for an Enterprise. |
| `put_enterprise_organizations_by_id` | Transfer an Organization to an Enterprise. |
| `update_enterprise_member_licensed` | Update a Member's licensed status |
| `deactivate_member` | Deactivate a Member of an Enterprise. |
| `update_admin_member` | Update Member to be admin of Enterprise |
| `delete_enterprise_admin_by_id` | Remove a Member as admin from Enterprise. |
| `delete_organization_by_id_and_org_id` | Delete an Organization from an Enterprise. |
| `get_bulk_organizations_by_ids` | Bulk accept a set of organizations to an Enterprise. |
| `get_labels_id` | Get a Label |
| `put_labels_id` | Update a Label |
| `delete_labels_id` | Delete a Label |
| `put_labels_id_field` | Update a field on a label |
| `post_labels` | Create a Label |
| `get_lists_id` | Get a List |
| `put_lists_id` | Update a List |
| `post_lists` | Create a new List |
| `post_lists_id_archiveallcards` | Archive all Cards in List |
| `post_lists_id_moveallcards` | Move all Cards in List |
| `put_lists_id_closed` | Archive or unarchive a list |
| `put_id_idboard` | Move List to Board |
| `put_lists_id_field` | Update a field on a List |
| `get_lists_id_actions` | Get Actions for a List |
| `get_lists_id_board` | Get the Board a List is on |
| `get_lists_id_cards` | Get Cards in a List |
| `get_members_id` | Get a Member |
| `put_members_id` | Update a Member |
| `get_members_id_field` | Get a field on a Member |
| `get_members_id_actions` | Get a Member's Actions |
| `get_board_backgrounds_by_id` | Get Member's custom Board backgrounds |
| `create_board_background` | Upload new boardBackground for Member |
| `get_member_board_backgrounds` | Get a boardBackground of a Member |
| `update_board_background` | Update a Member's custom Board background |
| `delete_board_background_by_id` | Delete a Member's custom Board background |
| `get_members_id_boardstars` | Get a Member's boardStars |
| `post_members_id_boardstars` | Create Star for Board |
| `get_board_star_by_id` | Get a boardStar of Member |
| `update_board_star_position` | Update the position of a boardStar of Member |
| `delete_board_star` | Delete Star for Board |
| `get_members_id_boards` | Get Boards that Member belongs to |
| `get_members_id_boardsinvited` | Get Boards the Member has been invited to |
| `get_members_id_cards` | Get Cards the Member is on |
| `get_custom_board_backgrounds_by_id` | Get a Member's custom Board Backgrounds |
| `set_custom_board_backgrounds` | Create a new custom Board Background |
| `get_custom_board_backgrounds_by_id_back` | Get custom Board Background of Member |
| `update_member_custom_board_background` | Update custom Board Background of Member |
| `delete_custom_background_by_id` | Delete custom Board Background of Member |
| `get_members_id_customemoji` | Get a Member's customEmojis |
| `post_members_id_customemoji` | Create custom Emoji for Member |
| `membersidcustomemojiidemoji` | Get a Member's custom Emoji |
| `get_members_id_customstickers` | Get Member's custom Stickers |
| `post_members_id_customstickers` | Create custom Sticker for Member |
| `get_member_custom_sticker_by_id` | Get a Member's custom Sticker |
| `delete_member_custom_sticker_by_id` | Delete a Member's custom Sticker |
| `get_members_id_notifications` | Get Member's Notifications |
| `get_members_id_organizations` | Get Member's Organizations |
| `get_member_organizations_invited` | Get Organizations a Member has been invited to |
| `get_members_id_savedsearches` | Get Member's saved searched |
| `post_members_id_savedsearches` | Create saved Search for Member |
| `get_saved_searches_by_id` | Get a saved search |
| `update_member_saved_search` | Update a saved search |
| `delete_saved_search` | Delete a saved search |
| `get_members_id_tokens` | Get Member's Tokens |
| `membersidavatar` | Create Avatar for Member |
| `post_member_one_time_messages_dismissed` | Dismiss a message for Member |
| `get_member_notifications_channel_settings` | Get a Member's notification channel settings |
| `update_notification_channel_settings` | Update blocked notification keys of Member on a channel |
| `get_member_notification_channel_settings` | Get blocked notification keys of Member on this channel |
| `update_member_notification_channel_settings` | Update blocked notification keys of Member on a channel |
| `update_notification_settings` | Update blocked notification keys of Member on a channel |
| `get_notifications_id` | Get a Notification |
| `put_notifications_id` | Update a Notification's read status |
| `get_notifications_id_field` | Get a field of a Notification |
| `post_notifications_all_read` | Mark all Notifications as read |
| `put_notifications_id_unread` | Update Notification's read status |
| `get_notifications_id_board` | Get the Board a Notification is on |
| `get_notifications_id_card` | Get the Card a Notification is on |
| `get_notifications_id_list` | Get the List a Notification is on |
| `notificationsidmember` | Get the Member a Notification is about (not the creator) |
| `get_member_creator_details` | Get the Member who created the Notification |
| `get_notification_org` | Get a Notification's associated Organization |
| `post_organizations` | Create a new Organization |
| `get_organizations_id` | Get an Organization |
| `put_organizations_id` | Update an Organization |
| `delete_organizations_id` | Delete an Organization |
| `get_organizations_id_field` | Get field on Organization |
| `get_organizations_id_actions` | Get Actions for Organization |
| `get_organizations_id_boards` | Get Boards in an Organization |
| `post_organizations_id_exports` | Create Export for Organizations |
| `get_organizations_id_exports` | Retrieve Organization's Exports |
| `get_organizations_id_members` | Get the Members of an Organization |
| `put_organizations_id_members` | Update an Organization's Members |
| `get_organization_memberships` | Get Memberships of an Organization |
| `get_membership_details` | Get a Membership of an Organization |
| `get_organization_plugin_data_by_id` | Get the pluginData Scoped to Organization |
| `get_organizations_id_tags` | Get Tags of an Organization |
| `post_organizations_id_tags` | Create a Tag in Organization |
| `update_member_type` | Update a Member of an Organization |
| `remove_organization_member` | Remove a Member from an Organization |
| `deactivate_member_org` | Deactivate or reactivate a member of an Organization |
| `post_organizations_id_logo` | Update logo for an Organization |
| `delete_organizations_id_logo` | Delete Logo for Organization |
| `delete_organization_member_all` | Remove a Member from an Organization and all Organization Boards |
| `delete_associated_domain` | Remove the associated Google Apps domain from a Workspace |
| `delete_org_invite_restrict_by_id` | Delete the email domain restriction on who can be invited to the Workspace |
| `delete_organization_tag_by_id_tag` | Delete an Organization's Tag |
| `get_guests_by_board` | Get Organizations new billable guests |
| `get_plugins_id` | Get a Plugin |
| `put_plugins_id` | Update a Plugin |
| `post_plugins_idplugin_listing` | Create a Listing for Plugin |
| `get_member_privacy_compliance` | Get Plugin's Member privacy compliance |
| `update_plugin_listing` | Updating Plugin's Listing |
| `get_search` | Search Trello |
| `get_search_members` | Search for Members |
| `get_tokens_token` | Get a Token |
| `get_tokens_token_member` | Get Token's Member |
| `get_tokens_token_webhooks` | Get Webhooks for Token |
| `post_tokens_token_webhooks` | Create Webhooks for Token |
| `get_webhook_by_id` | Get a Webhook belonging to a Token |
| `delete_webhook_by_id` | Delete a Webhook created by Token |
| `tokenstokenwebhooks` | Update a Webhook created by Token |
| `delete_token` | Delete a Token |
| `post_webhooks` | Create a Webhook |
| `get_webhooks_id` | Get a Webhook |
| `put_webhooks_id` | Update a Webhook |
| `delete_webhooks_id` | Delete a Webhook |
| `webhooksidfield` | Get a field on a Webhook |
