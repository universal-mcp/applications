from contextlib import asynccontextmanager, contextmanager
from typing import Any, List, Optional

import httpx
from loguru import logger

from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError
from universal_mcp.integrations import Integration


class SmartleadApp(APIApplication):
    """
    Application for interacting with the Smartlead cold email automation platform.

    Manages campaigns, email accounts, leads, master inbox, analytics, and more.

    Authentication uses the Smartlead API key passed as a `?api_key=` query
    parameter on every request (not an Authorization header). The key is
    retrieved from the configured Integration and injected at the HTTP-client
    level so individual tool methods stay clean.
    """

    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="smartlead", integration=integration, **kwargs)
        self.base_url = "https://server.smartlead.ai/api/v1"

    # ------------------------------------------------------------------
    # Authentication helpers
    # ------------------------------------------------------------------

    async def _aget_api_key(self) -> str:
        """Retrieve the Smartlead API key from the configured integration asynchronously."""
        if not self.integration:
            raise NotAuthorizedError("No integration configured for SmartleadApp.")
        credentials = await self.integration.get_credentials_async()
        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )
        if not api_key:
            raise NotAuthorizedError(
                "Smartlead API key not found in integration credentials. "
                "Please set your API key via the integration."
            )
        return api_key

    def _get_api_key(self) -> str:
        """Retrieve the Smartlead API key from the configured integration synchronously."""
        if not self.integration:
            raise NotAuthorizedError("No integration configured for SmartleadApp.")
        credentials = self.integration.get_credentials()
        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )
        if not api_key:
            raise NotAuthorizedError(
                "Smartlead API key not found in integration credentials. "
                "Please set your API key via the integration."
            )
        return api_key

    # Smartlead uses api_key as a query param – no Authorization header needed.
    async def _aget_headers(self) -> dict[str, str]:
        return {}

    def _get_headers(self) -> dict[str, str]:
        return {}

    @asynccontextmanager
    async def get_async_client(self):  # type: ignore[override]
        """Async httpx client with the Smartlead api_key injected as a default query param."""
        api_key = await self._aget_api_key()
        async with httpx.AsyncClient(
            base_url=self.base_url,
            params={"api_key": api_key},
            timeout=self.default_timeout,
        ) as client:
            yield client

    @contextmanager
    def get_sync_client(self):  # type: ignore[override]
        """Sync httpx client with the Smartlead api_key injected as a default query param."""
        api_key = self._get_api_key()
        with httpx.Client(
            base_url=self.base_url,
            params={"api_key": api_key},
            timeout=self.default_timeout,
        ) as client:
            yield client

    # ==================== Campaign Operations ====================

    async def list_campaigns(self, client_id: Optional[int] = None, include_tags: bool = False) -> List[dict[str, Any]]:
        """
        Retrieves a comprehensive list of all cold email campaigns configured within the workspace. 
        Supports filtering by specific Client IDs for agency users and optional tag inclusion for better context.

        Args:
            client_id: Optional. Filter campaigns belonging specifically to this Client ID. Example: 12345
            include_tags: When true, the response includes organizational tags attached to each campaign. Default: False.

        Returns:
            List[dict]: A list containing campaign objects with metadata (status, name, timestamps).

        Raises:
            HTTPStatusError: If the API request fails.

        Tags:
            campaigns, read, list, important
        """
        params = {
            "include_tags": "true" if include_tags else "false",
            "client_id": client_id
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        url = "/campaigns/"
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_campaign(self, campaign_id: int) -> dict[str, Any]:
        """
        Fetches the complete granular configuration and state of a specific campaign by its ID.
        Includes delivery tracking settings, stop-lead parameters, and internal campaign metadata.

        Args:
            campaign_id: The unique numerical ID of the target campaign. Example: 45678

        Returns:
            dict: Detailed campaign object structure.

        Raises:
            ValueError: If campaign_id is missing.
            HTTPStatusError: If the campaign is not found or the API request fails.

        Tags:
            campaigns, read, specific, important
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'.")
        url = f"/campaigns/{campaign_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_campaign(self, name: str, **kwargs) -> dict[str, Any]:
        """
        Generates a brand new email campaign within the Smartlead account. You can optionally include
        sending limits, tracking settings, and advanced stop-lead configurations within the payload.

        Args:
            name: Human-readable identifier for the new campaign. Example: 'Outbound Sales - Q3 Focus'
            **kwargs: Flexible key-value pairs for advanced settings (e.g. min_time_btwn_emails: 5).

        Returns:
            dict: The newly created campaign object including its generated ID.

        Raises:
            ValueError: If a campaign name is not provided.
            HTTPStatusError: If campaign creation is rejected by the server.

        Tags:
            campaigns, create, important
        """
        if not name:
             raise ValueError("Missing required parameter 'name'.")
        json_data = {"name": name, **kwargs}
        url = "/campaigns/create"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def update_campaign_status(self, campaign_id: int, status: str) -> dict[str, Any]:
        """
        Transitions an existing campaign into a new operational state (e.g., active, paused, or archived).
        Essential for controlling outreach flow based on system triggers or manual oversight.

        Args:
            campaign_id: The unique numerical ID of the campaign to update. Example: 45678
            status: Target state for the campaign. Allowed: 'ACTIVE', 'PAUSED', 'STOPPED', 'ARCHIVED', 'DRAFTED'.

        Returns:
            dict: Confirmation object indicating the successful status shift.

        Raises:
            ValueError: If campaign_id or status is missing.
            HTTPStatusError: If the status transition is invalid or the request fails.

        Tags:
            campaigns, update, status, important
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        if not status: raise ValueError("Missing 'status'.")
        url = f"/campaigns/{campaign_id}/status"
        response = await self._apatch(url, data={"status": status})
        response.raise_for_status()
        return response.json()

    async def update_campaign_schedule(self, campaign_id: int, scheduler_cron_value: dict[str, Any]) -> dict[str, Any]:
        """
        Adjusts the active sending windows for a campaign. Use this to ensure outreach matches
        the recipient's timezone and your team's operational hours.

        Args:
            campaign_id: The unique ID of the campaign. Example: 45678
            scheduler_cron_value: Dictionary containing 'tz' (e.g. 'Europe/London'), 'days' (e.g. [1,2,3]), 'startHour' (e.g. '09:00'), and 'endHour' (e.g. '17:00').

        Returns:
            dict: Success response indicating the new schedule is active.

        Raises:
            ValueError: If required scheduling data is missing.

        Tags:
            campaigns, update, schedule
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/schedule"
        response = await self._apost(url, data=scheduler_cron_value)
        response.raise_for_status()
        return response.json()

    async def get_campaign_sequences(self, campaign_id: int) -> List[dict[str, Any]]:
        """
        Retrieves the ordered series of email steps (sequences) defined for a specific campaign.
        Includes wait times, subject lines, and body content for each sequential touchpoint.

        Args:
            campaign_id: Numerical ID of the campaign context. Example: 45678

        Returns:
            List[dict]: Array of sequence step objects in chronological order.

        Tags:
            campaigns, sequences, read
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/sequences"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def save_campaign_sequence(self, campaign_id: int, sequence_data: dict[str, Any]) -> dict[str, Any]:
        """
        Updates or completely overwrites the multi-step email sequence logic for a campaign.
        Ideal for refreshing copy or adjusting follow-up delays based on campaign performance.

        Args:
            campaign_id: Target campaign identifier. Example: 45678
            sequence_data: Comprehensive object containing the full sequence arrays and step details.

        Returns:
            dict: Response confirming the new sequence has been enrolled into the campaign.

        Tags:
            campaigns, sequences, update
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/sequences"
        response = await self._apost(url, data=sequence_data)
        response.raise_for_status()
        return response.json()

    async def list_campaign_email_accounts(self, campaign_id: int) -> List[dict[str, Any]]:
        """
        Identifies exactly which sender email accounts are currently assigned to deliver emails
        for a targeted outreach campaign.

        Args:
            campaign_id: The ID of the campaign to audit. Example: 45678

        Returns:
            List[dict]: A list of sender accounts participating in the campaign.

        Tags:
            campaigns, accounts, read
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/email-accounts"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def add_campaign_email_account(self, campaign_id: int, email_account_ids: List[int]) -> dict[str, Any]:
        """
        Assigns new sender mailboxes to a campaign's round-robin pool. Increasing the number
        of email accounts allows for higher total daily send volumes across more IP addresses.

        Args:
            campaign_id: Target campaign ID. Example: 45678
            email_account_ids: Numeric IDs of the email accounts to attach. Example: [101, 102]

        Returns:
            dict: Success confirmation for the mailbox assignment.

        Tags:
            campaigns, accounts, update
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/email-accounts"
        response = await self._apost(url, data={"email_account_ids": email_account_ids})
        response.raise_for_status()
        return response.json()

    async def remove_campaign_email_account(self, campaign_id: int, email_account_ids: List[int]) -> dict[str, Any]:
        """
        Detaches specific sender mailboxes from a campaign. Useful when moving mailboxes between
        campaigns or removing poor performers from a high-stakes outreach track.

        Args:
            campaign_id: Target campaign ID.
            email_account_ids: Numeric IDs of the email accounts to detach. Example: [101]

        Returns:
            dict: Confirmation that the accounts have been unlinked.

        Tags:
            campaigns, accounts, delete
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/email-accounts"
        async with self.get_async_client() as client:
            response = await client.request("DELETE", url, json={"email_account_ids": email_account_ids})
        response.raise_for_status()
        return response.json()

    async def delete_campaign(self, campaign_id: int) -> dict[str, Any]:
        """
        Permanently destroys a campaign and all its associated data within the workspace.
        Warning: This action is destructive and removes all sequence history and tracking stats.

        Args:
            campaign_id: The ID of the campaign to eliminate. Example: 45678

        Returns:
            dict: Success response confirming removal.

        Tags:
            campaigns, delete
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def update_campaign_settings(self, campaign_id: int, **kwargs) -> dict[str, Any]:
        """Updates general settings of an existing campaign."""
        url = f"/campaigns/{campaign_id}"
        response = await self._apost(url, data=kwargs)
        response.raise_for_status()
        return response.json()

    async def create_campaign_subsequence(self, campaign_id: int, subsequence_data: dict[str, Any]) -> dict[str, Any]:
        """Creates a subsequence for conditional branching in a campaign."""
        url = f"/campaigns/{campaign_id}/subsequences"
        response = await self._apost(url, data=subsequence_data)
        response.raise_for_status()
        return response.json()

    async def forward_campaign_email(self, campaign_id: int, forward_data: dict[str, Any]) -> dict[str, Any]:
        """Forwards a specific email from a campaign."""
        url = f"/campaigns/{campaign_id}/forward-email"
        response = await self._apost(url, data=forward_data)
        response.raise_for_status()
        return response.json()

    async def reply_campaign_email_thread(self, campaign_id: int, reply_data: dict[str, Any]) -> dict[str, Any]:
        """Replies to a specific email thread within a campaign context."""
        url = f"/campaigns/{campaign_id}/reply-email"
        response = await self._apost(url, data=reply_data)
        response.raise_for_status()
        return response.json()

    async def send_campaign_test_email(self, campaign_id: int, test_data: dict[str, Any]) -> dict[str, Any]:
        """Sends a test email for a specific campaign to verify layout and variables."""
        url = f"/campaigns/{campaign_id}/test-email"
        response = await self._apost(url, data=test_data)
        response.raise_for_status()
        return response.json()

    async def update_campaign_team_member(self, campaign_id: int, team_data: dict[str, Any]) -> dict[str, Any]:
        """Updates team member assignments and permissions for a campaign."""
        url = f"/campaigns/{campaign_id}/team-members"
        response = await self._apost(url, data=team_data)
        response.raise_for_status()
        return response.json()

    async def create_lead_list(self, name: str) -> dict[str, Any]:
        """Creates a new static lead list for organizational grouping."""
        url = "/lead-lists"
        response = await self._apost(url, data={"name": name})
        response.raise_for_status()
        return response.json()

    async def get_all_lead_lists(self) -> List[dict[str, Any]]:
        """Fetches all lead lists existing within the workspace."""
        url = "/lead-lists"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_lead_list_by_id(self, list_id: int) -> dict[str, Any]:
        """Retrieves the full configuration and details of a specific lead list."""
        url = f"/lead-lists/{list_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def update_lead_list(self, list_id: int, name: str) -> dict[str, Any]:
        """Updates the name or properties of a lead list."""
        url = f"/lead-lists/{list_id}"
        response = await self._aput(url, data={"name": name})
        response.raise_for_status()
        return response.json()

    async def delete_lead_list(self, list_id: int) -> dict[str, Any]:
        """Deletes a lead list (removes grouping, does not delete leads)."""
        url = f"/lead-lists/{list_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def import_leads_to_list(self, list_id: int, leads: List[dict[str, Any]]) -> dict[str, Any]:
        """Injects a batch of lead objects directly into a designated lead list."""
        url = f"/lead-lists/{list_id}/leads"
        response = await self._apost(url, data={"leads": leads})
        response.raise_for_status()
        return response.json()

    async def push_leads_between_lists(self, source_list_id: int, target_list_id: int) -> dict[str, Any]:
        """Moves or copies leads from one static list to another."""
        url = "/lead-lists/push"
        response = await self._apost(url, data={"source_list_id": source_list_id, "target_list_id": target_list_id})
        response.raise_for_status()
        return response.json()

    async def push_lead_list_to_campaign(self, list_id: int, campaign_id: int) -> dict[str, Any]:
        """Enrolls an entire static lead list into an active campaign."""
        url = f"/lead-lists/{list_id}/campaigns"
        response = await self._apost(url, data={"campaign_id": campaign_id})
        response.raise_for_status()
        return response.json()

    async def assign_tags_to_lead_list(self, list_id: int, tag_ids: List[int]) -> dict[str, Any]:
        """Bulk assigns workspace tags to all leads inside a specific list."""
        url = f"/lead-lists/{list_id}/tags"
        response = await self._apost(url, data={"tag_ids": tag_ids})
        response.raise_for_status()
        return response.json()
    # ==================== Lead Operations ====================

    async def list_campaign_leads(self, campaign_id: int, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """
        Retrieves the prospects (leads) currently residing inside a specific campaign. Supports
        pagination to handle large lead batches effectively.

        Args:
            campaign_id: The campaign to query. Example: 45678
            limit: Maximum number of leads to return per page. Default: 100.
            offset: The starting record index. Default: 0.

        Returns:
            dict: Paginated lead objects with their current categorization and status.

        Tags:
            leads, read, list, important
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        params = {"limit": limit, "offset": offset}
        url = f"/campaigns/{campaign_id}/leads"
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_lead_by_email(self, email_address: str) -> dict[str, Any]:
        """
        Searches for a specific prospect across the entire global Smartlead workspace using 
        their unique email address. Use this to check lead enrichment or status before campaign enrollment.

        Args:
            email_address: The email address of the lead. Example: 'prospect@example.com'

        Returns:
            dict: The lead's profile, including custom variables and enrollment history.

        Tags:
            leads, read, specific
        """
        if not email_address: raise ValueError("Missing 'email_address'.")
        url = "/leads/"
        response = await self._aget(url, params={"email": email_address})
        response.raise_for_status()
        return response.json()

    async def add_leads_to_campaign(self, campaign_id: int, leads: List[dict[str, Any]]) -> dict[str, Any]:
        """
        Injects a set of new prospects into a campaign. Each prospect can include custom
        variables (like {{first_name}} or {{company}}) that personalize the email template on dispatch.

        Args:
            campaign_id: The campaign where leads should be added.
            leads: List of lead objects containing 'email', 'first_name', and other personalization variables.

        Returns:
            dict: Summary of the import operation results.

        Tags:
            leads, create, import, important
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/leads"
        response = await self._apost(url, data={"lead_list": leads})
        response.raise_for_status()
        return response.json()

    async def update_lead(self, contact_id: int, update_data: dict[str, Any]) -> dict[str, Any]:
        """
        Modifies a lead's profile data globally. This updates their core variables and 
        contact information for all campaigns they are currently part of.

        Args:
            contact_id: The unique ID of the contact/lead. Example: 998877
            update_data: Dictionary of fields to update (e.g. {'first_name': 'NewName'}).

        Returns:
            dict: The updated lead object record.

        Tags:
            leads, update
        """
        if contact_id is None: raise ValueError("Missing 'contact_id'.")
        url = f"/leads/{contact_id}"
        response = await self._aput(url, data=update_data)
        response.raise_for_status()
        return response.json()

    async def pause_lead_in_campaign(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """
        Temporarily halts outreach for a specific lead inside a single targeted campaign 
        without affecting their status in other campaigns or global lists.

        Args:
            campaign_id: ID of the campaign.
            lead_id: ID of the lead to pause.

        Returns:
            dict: Confirmation for the pause operation.

        Tags:
            leads, update, status
        """
        if not campaign_id or not lead_id: raise ValueError("Missing IDs.")
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/pause"
        response = await self._apost(url)
        response.raise_for_status()
        return response.json()

    async def resume_lead_in_campaign(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """
        Reactivates a previously paused lead within a targeted campaign, allowing their 
        next scheduled sequence step to be added back to the sending queue.

        Args:
            campaign_id: ID of the campaign context.
            lead_id: ID of the lead to reactivate.

        Returns:
            dict: Success confirmation for resuming outreach.

        Tags:
            leads, update, status
        """
        if not campaign_id or not lead_id: raise ValueError("Missing IDs.")
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/resume"
        response = await self._apost(url)
        response.raise_for_status()
        return response.json()

    async def unsubscribe_lead_globally(self, email_address: str) -> dict[str, Any]:
        """
        Adds a prospect's email address to the global unsubscribe/suppression list.
        This prevents them from being contacted by ANY current or future campaign in your account.

        Args:
            email_address: The prospect's email to block globally.

        Returns:
            dict: Summary of the global blocklist operation.

        Tags:
            leads, suppression, important
        """
        if not email_address: raise ValueError("Missing 'email_address'.")
        url = "/leads/unsubscribe-globally"
        response = await self._apost(url, data={"email": email_address})
        response.raise_for_status()
        return response.json()

    async def get_campaign_lead_by_id(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """Gets specific lead details inside a targeted campaign."""
        url = f"/campaigns/{campaign_id}/leads/{lead_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_campaign_lead_history(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """Gets sequence and message history for a specific lead in a campaign."""
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/history"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_campaign_leads_history_bulk(self, campaign_id: int) -> List[dict[str, Any]]:
        """Gets bulk history for all leads within a specific campaign."""
        url = f"/campaigns/{campaign_id}/leads-history"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_campaign_all_leads_activities(self, campaign_id: int) -> List[dict[str, Any]]:
        """Retrieves an activity feed of events (clicks, opens, replies) for campaign leads."""
        url = f"/campaigns/{campaign_id}/leads-activities"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def update_campaign_lead(self, campaign_id: int, lead_id: int, update_data: dict[str, Any]) -> dict[str, Any]:
        """Updates specific lead data within the context of a single campaign."""
        url = f"/campaigns/{campaign_id}/leads/{lead_id}"
        response = await self._apost(url, data=update_data)
        response.raise_for_status()
        return response.json()

    async def update_campaign_lead_category(self, campaign_id: int, lead_id: int, category_id: int) -> dict[str, Any]:
        """Updates the categorization status (e.g. interested) of a lead in a campaign."""
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/category"
        response = await self._apost(url, data={"category_id": category_id})
        response.raise_for_status()
        return response.json()

    async def update_campaign_lead_email_account(self, campaign_id: int, lead_id: int, email_account_id: int) -> dict[str, Any]:
        """Assigns or rotates the specific sender email account assigned to a lead."""
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/email-account"
        response = await self._apost(url, data={"email_account_id": email_account_id})
        response.raise_for_status()
        return response.json()

    async def mark_campaign_lead_complete(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """Marks a lead's sequence as complete within a campaign."""
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/complete"
        response = await self._apost(url)
        response.raise_for_status()
        return response.json()

    async def unsubscribe_campaign_lead(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """Unsubscribes a lead from a specific campaign only."""
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/unsubscribe"
        response = await self._apost(url)
        response.raise_for_status()
        return response.json()

    async def delete_campaign_lead(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """Removes a lead from a campaign completely."""
        url = f"/campaigns/{campaign_id}/leads/{lead_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def create_lead_note(self, lead_id: int, note: str) -> dict[str, Any]:
        """
        Attaches a internal text note to a specific lead profile. Use this to track 
        manual touchpoints or internal observations.

        Args:
            lead_id: ID of the prospect.
            note: The text content of the note.

        Returns:
            dict: The created note object.

        Tags:
            leads, update, note
        """
        if not lead_id or not note: raise ValueError("Missing parameters.")
        url = f"/leads/{lead_id}/notes"
        response = await self._apost(url, data={"note": note})
        response.raise_for_status()
        return response.json()

    async def create_lead_task(self, lead_id: int, title: str, due_date: Optional[str] = None) -> dict[str, Any]:
        """
        Assigns a manual follow-up task related to a specific lead.

        Args:
            lead_id: ID of the lead.
            title: Human-readable task description.
            due_date: Optional ISO timestamp for the task deadline.

        Returns:
            dict: The created task object.

        Tags:
            leads, update, task
        """
        if not lead_id or not title: raise ValueError("Missing parameters.")
        json_data = {"title": title, "due_date": due_date}
        url = f"/leads/{lead_id}/tasks"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def get_lead_message_history(self, lead_id: int) -> List[dict[str, Any]]:
        """
        Retrieves the complete chronological record of all emails sent to and received 
        from a specific lead across all campaigns.

        Args:
            lead_id: Numerical ID of the lead.

        Returns:
            List[dict]: Array of historical message objects.

        Tags:
            leads, read, history
        """
        if lead_id is None: raise ValueError("Missing 'lead_id'.")
        url = f"/leads/{lead_id}/message-history"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def export_campaign_leads(self, campaign_id: int) -> dict[str, Any]:
        """
        Triggers a CSV export of all leads within a specific campaign.
        The API typically returns a download link or confirmation.

        Args:
            campaign_id: ID of the campaign to export.

        Returns:
            dict: Export status and download URI.

        Tags:
            leads, export
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/export-leads"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()


    async def get_leads_by_campaign(self, campaign_id: int) -> List[dict[str, Any]]:
        """Retrieves a global list of leads filtered by their campaign assignment."""
        url = "/leads/"
        response = await self._aget(url, params={"campaign_id": campaign_id})
        response.raise_for_status()
        return response.json()

    async def add_lead_to_campaign_globally(self, lead_id: int, campaign_id: int) -> dict[str, Any]:
        """Enrolls an existing global lead into a specific campaign."""
        url = f"/leads/{lead_id}/campaigns"
        response = await self._apost(url, data={"campaign_id": campaign_id})
        response.raise_for_status()
        return response.json()

    async def delete_lead_globally(self, lead_id: int) -> dict[str, Any]:
        """Permanently deletes a lead globally from the workspace."""
        url = f"/leads/{lead_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def pause_lead_globally(self, lead_id: int) -> dict[str, Any]:
        """Pauses a lead across all active campaigns simultaneously."""
        url = f"/leads/{lead_id}/pause"
        response = await self._apost(url)
        response.raise_for_status()
        return response.json()

    async def resume_lead_globally(self, lead_id: int) -> dict[str, Any]:
        """Resumes outreach for a lead globally."""
        url = f"/leads/{lead_id}/resume"
        response = await self._apost(url)
        response.raise_for_status()
        return response.json()

    async def get_lead_categories(self) -> List[dict[str, Any]]:
        """Retrieves all lead categorization labels available in the workspace."""
        url = "/leads/categories"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_lead_activities(self, lead_id: int) -> List[dict[str, Any]]:
        """Fetches the global activity stream for a specific lead."""
        url = f"/leads/{lead_id}/activities"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()


    async def get_all_lead_notes(self, lead_id: int) -> List[dict[str, Any]]:
        """Retrieves all internal notes attached to a prospect."""
        url = f"/leads/{lead_id}/notes"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_all_lead_tasks(self, lead_id: int) -> List[dict[str, Any]]:
        """Retrieves all follow-up tasks assigned to a specific lead."""
        url = f"/leads/{lead_id}/tasks"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()


    # ==================== Email Account Operations ====================

    async def list_email_accounts(self, tag: Optional[str] = None) -> List[dict[str, Any]]:
        """
        Retrieves all connected sender mailboxes across the workspace. Essential for monitoring 
        the status, deliverability, and rotation health of your sending infrastructure.

        Args:
            tag: Optional. Filter results by an organizational account tag.

        Returns:
            List[dict]: A list of email account objects including health and configuration data.

        Tags:
            accounts, read, list, important
        """
        params = {"tag": tag} if tag else {}
        url = "/email-accounts/"
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def create_email_account(self, email: str, **kwargs) -> dict[str, Any]:
        """
        Integrates a new sender mailbox (SMTP/IMAP) into the platform. Requires standard 
        host, port, and security credentials for outbound email and reply tracking.

        Args:
            email: The fully qualified email address to connect. Example: 'sender@domain.com'
            **kwargs: Connection details like from_name, smtp_host, smtp_port, user_password, etc.

        Returns:
            dict: The newly created email account resource object.

        Tags:
            accounts, create
        """
        if not email: raise ValueError("Missing 'email'.")
        json_data = {"email": email, **kwargs}
        url = "/email-accounts/create"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def get_email_account_warmup_stats(self, email_account_id: int) -> dict[str, Any]:
        """
        Fetches reporting data for an account's deliverability warmup process, showing daily 
        outbound vs reply volume across the warmup network.

        Args:
            email_account_id: numeric ID of the connected account.

        Returns:
            dict: Warmup performance metrics including day-by-day logs.

        Tags:
            accounts, warmup, read
        """
        if email_account_id is None: raise ValueError("Missing ID.")
        url = f"/email-accounts/{email_account_id}/warmup-stats"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    # ==================== Master Inbox Operations ====================

    async def get_unread_replies(self, limit: int = 50) -> List[dict[str, Any]]:
        """
        Retrieves the the most recent email thread replies across all campaigns that have not 
        yet been marked as read. Use this to power real-time engagement monitors.

        Args:
            limit: Number of unread items to fetch. Default: 50.

        Returns:
            List[dict]: Array of Master Inbox thread objects.

        Tags:
            inbox, replies, read, important
        """
        url = "/master-inbox/unread-replies"
        response = await self._aget(url, params={"limit": limit})
        response.raise_for_status()
        return response.json()

    async def get_sent_emails(self, limit: int = 50, offset: int = 0) -> List[dict[str, Any]]:
        """
        Retrieves a log of outbound emails dispatched across all campaigns.
        Provides visibility into the sent items for auditing or conversation tracking.

        Args:
            limit: Maximum items to retrieve. Default: 50.
            offset: Record index to start from. Default: 0.

        Returns:
            List[dict]: A historical list of sent email objects.

        Tags:
            inbox, sent, read
        """
        url = "/master-inbox/sent-emails"
        response = await self._aget(url, params={"limit": limit, "offset": offset})
        response.raise_for_status()
        return response.json()

    async def get_important_emails(self, limit: int = 50) -> List[dict[str, Any]]:
        """
        Fetches threads that have been flagged as important by the user or team members
        within the Master Inbox.

        Args:
            limit: Maximum items to fetch. Default: 50.

        Returns:
            List[dict]: List of high-priority conversation threads.

        Tags:
            inbox, important, read
        """
        url = "/master-inbox/important-emails"
        response = await self._aget(url, params={"limit": limit})
        response.raise_for_status()
        return response.json()

    async def get_archived_emails(self, limit: int = 50) -> List[dict[str, Any]]:
        """
        Pulls threads that have been moved to the archive, indicating they are resolved
        or concluded from a sales perspective.

        Args:
            limit: Maximum items to fetch. Default: 50.

        Returns:
            List[dict]: List of archived conversation threads.

        Tags:
            inbox, archived, read
        """
        url = "/master-inbox/archived-emails"
        response = await self._aget(url, params={"limit": limit})
        response.raise_for_status()
        return response.json()

    async def get_unread_count(self) -> dict[str, Any]:
        """
        Retrieves the exact numeric count of unread email threads in the Master Inbox.

        Returns:
            dict: Object containing the unread count integer.

        Tags:
            inbox, read, analytics
        """
        url = "/master-inbox/unread-count"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_snoozed_emails(self, limit: int = 50) -> List[dict[str, Any]]:
        """
        Retrieves inbox threads that have been temporarily snoozed and are awaiting 
        their scheduled re-appearance in the primary view.

        Args:
            limit: Maximum items to fetch. Default: 50.

        Returns:
            List[dict]: Array of snoozed thread objects.

        Tags:
            inbox, snoozed, read
        """
        url = "/master-inbox/snoozed-emails"
        response = await self._aget(url, params={"limit": limit})
        response.raise_for_status()
        return response.json()

    async def get_untracked_replies(self, limit: int = 50) -> List[dict[str, Any]]:
        """
        Retrieves replies that have hit connected mailboxes but could not be 
        definitively matched to an active campaign lead.

        Args:
            limit: Maximum items to fetch.

        Returns:
            List[dict]: Array of untracked response objects.

        Tags:
            inbox, untracked, read
        """
        url = "/master-inbox/untracked-replies"
        response = await self._aget(url, params={"limit": limit})
        response.raise_for_status()
        return response.json()

    async def get_inbox_item_by_id(self, message_id: str) -> dict[str, Any]:
        """
        Fetches the complete conversation thread and metadata for a specific item 
        identified within the Master Inbox.

        Args:
            message_id: Unique identifier for the inbox thread.

        Returns:
            dict: The thread's full content and history.

        Tags:
            inbox, read, specific
        """
        if not message_id: raise ValueError("Missing 'message_id'.")
        url = f"/master-inbox/{message_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def reply_to_email(self, email_account_id: int, message_id: str, reply_text: str) -> dict[str, Any]:
        """
        Sends a manual reply directly from the Master Inbox context. This is ideal for answering 
        prospect questions and managing sales conversations through the API.

        Args:
            email_account_id: The ID of the sender account to use for the reply.
            message_id: The ID of the parent email thread to reply to.
            reply_text: The plaintext or HTML content of the reply message.

        Returns:
            dict: Confirmation that the reply has been successfully transmitted.

        Tags:
            inbox, replies, create, important
        """
        if not all([email_account_id, message_id, reply_text]):
             raise ValueError("Missing required reply parameters.")
        json_data = {
            "email_account_id": email_account_id,
            "message_id": message_id,
            "reply_text": reply_text
        }
        url = "/master-inbox/reply"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def forward_email(self, message_id: str, forward_to_email: str) -> dict[str, Any]:
        """
        Forwards a message thread from the Master Inbox to an external email address.
        Useful for escalation or sharing context with non-system users.

        Args:
            message_id: The thread identifier.
            forward_to_email: Resulting destination address.

        Returns:
            dict: Success confirmation for the forwarding action.

        Tags:
            inbox, create, forward
        """
        if not message_id or not forward_to_email: raise ValueError("Missing parameters.")
        json_data = {"message_id": message_id, "forward_to_email": forward_to_email}
        url = "/master-inbox/forward"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def change_read_status(self, message_id: str, is_read: bool) -> dict[str, Any]:
        """
        Toggles the read/unread state of a specific message thread in the Master Inbox.

        Args:
            message_id: The ID of the message thread.
            is_read: Boolean indicating the target status (true for read, false for unread).

        Returns:
            dict: Confirmation for the status change.

        Tags:
            inbox, update, status
        """
        if not message_id: raise ValueError("Missing 'message_id'.")
        url = "/master-inbox/read-status"
        response = await self._apost(url, data={"message_id": message_id, "is_read": is_read})
        response.raise_for_status()
        return response.json()

    async def update_lead_category(self, campaign_id: int, lead_id: int, category_id: int) -> dict[str, Any]:
        """
        Classifies a lead into a specific category (e.g., 'Positive Reply', 'Meeting Booked') 
        directly from the inbox context. Essential for triggering global lead logic.

        Args:
            campaign_id: ID of the campaign.
            lead_id: ID of the prospect.
            category_id: Numerical ID of the category.

        Returns:
            dict: Response confirming the classification update.

        Tags:
            inbox, leads, update, category
        """
        if not campaign_id or not lead_id or category_id is None: raise ValueError("Missing parameters.")
        json_data = {"campaign_id": campaign_id, "lead_id": lead_id, "category_id": category_id}
        url = "/master-inbox/update-lead-category"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def update_lead_revenue(self, lead_id: int, revenue_amount: float) -> dict[str, Any]:
        """
        Attaches a projected or closed dollar value to a specific lead. 
        Highly useful for tracking ROI and attribution within the Master Inbox.

        Args:
            lead_id: ID of the prospect.
            revenue_amount: The dollar amount (e.g. 1500.00).

        Returns:
            dict: Updated lead object with revenue data.

        Tags:
            inbox, leads, update, revenue
        """
        if not lead_id or revenue_amount is None: raise ValueError("Missing parameters.")
        url = "/master-inbox/update-revenue"
        response = await self._apost(url, data={"lead_id": lead_id, "revenue": revenue_amount})
        response.raise_for_status()
        return response.json()

    async def assign_team_member(self, message_id: str, user_id: int) -> dict[str, Any]:
        """
        Delegates a Master Inbox conversation to a specific team member for follow-up and management.

        Args:
            message_id: The thread identifier.
            user_id: ID of the target team member.

        Returns:
            dict: Confirmation for the assignment.

        Tags:
            inbox, update, team
        """
        if not message_id or user_id is None: raise ValueError("Missing parameters.")
        url = "/master-inbox/assign-member"
        response = await self._apost(url, data={"message_id": message_id, "user_id": user_id})
        response.raise_for_status()
        return response.json()

    async def block_email_domains(self, domains: List[str]) -> dict[str, Any]:
        """
        Adds one or more entire email domains to the workspace-wide blocklist. 
        Outreach will be permanently disabled for any current or future leads matching these domains.

        Args:
            domains: List of domains to block (e.g., ['competitor.com', 'invalid.org']).

        Returns:
            dict: Summary of the blocking operation.

        Tags:
            inbox, suppression, blocklist
        """
        if not domains: raise ValueError("Missing 'domains'.")
        url = "/master-inbox/block-domains"
        response = await self._apost(url, data={"domains": domains})
        response.raise_for_status()
        return response.json()

    async def set_lead_reminder(self, message_id: str, reminder_time: str) -> dict[str, Any]:
        """
        Attaches a time-based reminder to a specific Master Inbox thread to ensure 
        manual follow-up at a later date.

        Args:
            message_id: The ID of the inbox thread.
            reminder_time: ISO timestamp for the reminder.

        Returns:
            dict: Success confirmation for the reminder.

        Tags:
            inbox, update, reminder
        """
        if not message_id or not reminder_time: raise ValueError("Missing parameters.")
        url = "/master-inbox/set-reminder"
        response = await self._apost(url, data={"message_id": message_id, "reminder_time": reminder_time})
        response.raise_for_status()
        return response.json()

    # ==================== Smart Delivery & Tests ====================

    async def create_manual_placement_test(self, email_account_ids: List[int]) -> dict[str, Any]:
        """
        Initiates a manual Smart Delivery placement test to analyze where sender emails are landing.
        Tests for inbox placement across various ISPs (Gmail, Outlook, etc.).

        Args:
            email_account_ids: Array of account IDs to test.

        Returns:
            dict: The initialized test metadata.

        Tags:
            delivery, test, placement
        """
        if not email_account_ids: raise ValueError("Missing 'email_account_ids'.")
        url = "/smart-delivery/placement-test"
        response = await self._apost(url, data={"email_account_ids": email_account_ids})
        response.raise_for_status()
        return response.json()

    async def list_all_tests(self) -> List[dict[str, Any]]:
        """
        Retrieves a historical log of all deliverability and placement tests performed 
        within the workspace.

        Returns:
            List[dict]: historical test objects.

        Tags:
            delivery, test, read
        """
        url = "/smart-delivery/placement-tests"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def geo_wise_report(self, test_id: int) -> dict[str, Any]:
        """
        Fetches a geographically segmented deliverability report for a specific placement test.
        Ideal for identifying region-specific spam filters or routing issues.

        Args:
            test_id: The ID of the placement test.

        Returns:
            dict: Deep analysis of placement by global region.

        Tags:
            delivery, analytics, geo
        """
        if test_id is None: raise ValueError("Missing 'test_id'.")
        url = f"/smart-delivery/geo-report/{test_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def provider_wise_report(self, test_id: int) -> dict[str, Any]:
        """
        Analyzes test placement by email provider (ISP). Identify precisely which providers 
        are flagging your senders as spam (e.g., Gmail vs Zoho).

        Args:
            test_id: The target placement test ID.

        Returns:
            dict: Provider-specific deliverability percentages.

        Tags:
            delivery, analytics, provider
        """
        if test_id is None: raise ValueError("Missing 'test_id'.")
        url = f"/smart-delivery/provider-report/{test_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    # ==================== Smart Senders (Infrastructure) ====================

    async def auto_generate_mailboxes(self, domain_count: int, mailbox_per_domain: int) -> dict[str, Any]:
        """
        Utilizes Smart Senders to automatically purchase, configure, and warm up new sender 
        domains and mailboxes. A high-level automation for scaling infrastructure.

        Args:
            domain_count: Number of new domains to register.
            mailbox_per_domain: Number of mailboxes to create on each new domain.

        Returns:
            dict: Initialization summary of the infrastructure generation task.

        Tags:
            infrastructure, create, automated
        """
        json_data = {"domain_count": domain_count, "mailbox_per_domain": mailbox_per_domain}
        url = "/smart-senders/auto-generate"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def place_order(self, order_details: dict[str, Any]) -> dict[str, Any]:
        """
        Submits a custom order for domain or mailbox assets through the Smart Senders marketplace.

        Args:
            order_details: Dictionary containing 'type', 'quantity', and 'preferences'.

        Returns:
            dict: Order confirmation and tracking ID.

        Tags:
            infrastructure, create, order
        """
        url = "/smart-senders/order"
        response = await self._apost(url, data=order_details)
        response.raise_for_status()
        return response.json()

    async def get_orders(self) -> List[dict[str, Any]]:
        """
        Retrieves the historical log of all infrastructure orders (domains/mailboxes) 
        placed via Smart Senders.

        Returns:
            List[dict]: Array of order tracking objects.

        Tags:
            infrastructure, read, list
        """
        url = "/smart-senders/orders"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    # ==================== Webhooks & Tags ====================

    async def list_webhooks(self) -> List[dict[str, Any]]:
        """
        Fetches all workspace-level webhooks configured to stream event data like link clicks or replies.

        Returns:
            List[dict]: A list of webhook configuration objects.

        Tags:
            webhooks, read, list
        """
        url = "/webhooks/"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_webhook(self, target_url: str, event_types: List[str]) -> dict[str, Any]:
        """
        Registers a new workspace-wide webhook to stream events to an external system.

        Args:
            target_url: Destination URL for POST payloads.
            event_types: list of events to subscribe to (e.g., ['REPLY', 'LINK_CLICK']).

        Returns:
            dict: The created webhook configuration.

        Tags:
            webhooks, create
        """
        if not target_url or not event_types: raise ValueError("Missing parameters.")
        url = "/webhooks/"
        response = await self._apost(url, data={"url": target_url, "events": event_types})
        response.raise_for_status()
        return response.json()

    async def delete_webhook(self, webhook_id: int) -> dict[str, Any]:
        """
        Permanently removes a global workspace webhook.

        Args:
            webhook_id: Unique ID of the webhook configuration.

        Returns:
            dict: Confirmation of successful deletion.

        Tags:
            webhooks, delete
        """
        if webhook_id is None: raise ValueError("Missing 'webhook_id'.")
        url = f"/webhooks/{webhook_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def create_tag(self, name: str, color_code: Optional[str] = None) -> dict[str, Any]:
        """
        Creates a new organizational tag in the workspace for segmenting leads, 
        campaigns, or email accounts.

        Args:
            name: Human-readable tag name. Example: 'VIP Client'
            color_code: Optional HEX color code. Example: '#FF5733'

        Returns:
            dict: The created tag object.

        Tags:
            workspace, tags, create
        """
        if not name: raise ValueError("Missing 'name'.")
        url = "/tags/"
        response = await self._apost(url, data={"name": name, "color": color_code})
        response.raise_for_status()
        return response.json()

    async def add_tags_to_lead(self, lead_id: int, tag_ids: List[int]) -> dict[str, Any]:
        """
        Assigns multiple existing tags to a specific lead for advanced filtering 
        and segmentation.

        Args:
            lead_id: ID of the prospect.
            tag_ids: List of tag numerical IDs.

        Returns:
            dict: Success confirmation for the tag assignment.

        Tags:
            leads, tags, update
        """
        if not lead_id or not tag_ids: raise ValueError("Missing parameters.")
        url = f"/leads/{lead_id}/tags"
        response = await self._apost(url, data={"tag_ids": tag_ids})
        response.raise_for_status()
        return response.json()

    async def list_tags(self) -> List[dict[str, Any]]:
        """
        Retrieves all organizational tags defined within the workspace.

        Returns:
            List[dict]: Array of tag objects.

        Tags:
            workspace, tags, read
        """
        url = "/tags/"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    # ==================== Smart Prospect (B2B Database) ====================

    async def search_contacts_api(self, filters: dict[str, Any], limit: int = 20) -> dict[str, Any]:
        """
        Searches the massive Smart Prospect B2B database to find net-new leads matching 
        specific firmographic and demographic filters (industry, revenue, job title, etc.).

        Args:
            filters: Complex dictionary of search criteria (e.g., {'industries': ['SaaS'], 'job_titles': ['CEO']}).
            limit: Number of results to return per page. Default: 20.

        Returns:
            dict: search results containing contact metadata (names, titles, companies).

        Tags:
            prospecting, search, important
        """
        url = "/smart-prospect/search"
        response = await self._apost(url, params={"limit": limit}, data=filters)
        response.raise_for_status()
        return response.json()

    async def fetch_contacts_api(self, contact_ids: List[int]) -> dict[str, Any]:
        """
        Initiates the credit-based unlock process for a list of searched contacts. 
        Reveals verified B2B email addresses for the targeted prospects.

        Args:
            contact_ids: list of IDs from a previous search result.

        Returns:
            dict: Summary of the reveal operation and credit expenditure.

        Tags:
            prospecting, unlock, important
        """
        if not contact_ids: raise ValueError("Missing 'contact_ids'.")
        url = "/smart-prospect/fetch-contacts"
        response = await self._apost(url, data={"contact_ids": contact_ids})
        response.raise_for_status()
        return response.json()

    async def save_search_api(self, search_name: str, filters: dict[str, Any]) -> dict[str, Any]:
        """
        Persists a complex set of search filters natively so the query can be re-run 
        or monitored for new leads later.

        Args:
            search_name: Human-readable name for the saved filter set.
            filters: The exact filter dictionary to save.

        Returns:
            dict: The saved search configuration object.

        Tags:
            prospecting, search, save
        """
        if not search_name or not filters: raise ValueError("Missing parameters.")
        json_data = {"name": search_name, "filters": filters}
        url = "/smart-prospect/save-search"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def get_saved_searches_api(self) -> List[dict[str, Any]]:
        """
        Retrieves the list of memorized B2B prospect search configurations saved by the user.

        Returns:
            List[dict]: Array of saved search objects.

        Tags:
            prospecting, search
        """
        url = "/smart-prospect/saved-searches"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_recent_searches_api(self) -> List[dict[str, Any]]:
        """
        Retrieves a lightweight audit log of the most recent prospect queries across the workspace.

        Returns:
            List[dict]: Array of recent search activities.

        Tags:
            prospecting, search
        """
        url = "/smart-prospect/recent-searches"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def find_emails_api(self, contact_details: List[dict[str, Any]]) -> dict[str, Any]:
        """
        Submits a raw list of names and companies to algorithmically guess and verify B2B email addresses.

        Args:
            contact_details: List of objects containing 'first_name', 'last_name', and 'domain' or 'company_name'.

        Returns:
            dict: The verified email addresses and confidence scores.

        Tags:
            prospecting, enrichment
        """
        url = "/smart-prospect/find-emails"
        response = await self._apost(url, data={"contacts": contact_details})
        response.raise_for_status()
        return response.json()

    async def get_industries_api(self) -> List[dict[str, Any]]:
        """
        Retrieves the macro industry categories supported by the Smart Prospect filtering engine.

        Returns:
            List[dict]: Array of industry metadata objects.

        Tags:
            prospecting, filters, metadata
        """
        url = "/smart-prospect/industries"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_departments_api(self) -> List[str]:
        """
        Returns the list of corporate department categories used to filter prospects.

        Returns:
            List[str]: Array of department strings.

        Tags:
            prospecting, filters, metadata
        """
        url = "/smart-prospect/departments"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_revenue_api(self) -> List[str]:
        """
        Returns the corporate financial revenue brackets available for qualifying B2B targets.

        Returns:
            List[str]: Array of revenue bracket strings.

        Tags:
            prospecting, filters, metadata
        """
        url = "/smart-prospect/revenue-brackets"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_levels_api(self) -> List[str]:
        """
        Retrieves the recognized corporate seniority levels (e.g., 'C-Level', 'VP').

        Returns:
            List[str]: Array of seniority level strings.

        Tags:
            prospecting, filters, metadata
        """
        url = "/smart-prospect/seniority-levels"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_countries_api(self) -> List[str]:
        """
        Returns the complete array of ISO country parameters supported for search.

        Returns:
            List[str]: List of country names or codes.

        Tags:
            prospecting, filters, metadata
        """
        url = "/smart-prospect/countries"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_head_counts_api(self) -> List[str]:
        """
        Provides the company employee headcount brackets supported for filtering.

        Returns:
            List[str]: List of headcount range strings.

        Tags:
            prospecting, filters, metadata
        """
        url = "/smart-prospect/headcount-ranges"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_company_api(self, query: str) -> List[dict[str, Any]]:
        """
        Queries the database for company profiles matching a specific string.

        Args:
            query: The company name or partial string.

        Returns:
            List[dict]: Matching company objects.

        Tags:
            prospecting, filters, search
        """
        if not query: raise ValueError("Missing 'query'.")
        url = "/smart-prospect/companies"
        response = await self._aget(url, params={"q": query})
        response.raise_for_status()
        return response.json()

    async def get_job_title_api(self) -> List[str]:
        """
        Queries the Smart Prospect database for a list of recognized job titles.

        Returns:
            List[str]: Array of job title strings.

        Tags:
            prospecting, filters, metadata
        """
        url = "/smart-prospect/job-titles"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def search_analytics_api(self) -> dict[str, Any]:
        """
        Retrieves usage analytics and credit expenditure statistics for Smart Prospect.

        Returns:
            dict: Reporting data on search volume and successful reveals.

        Tags:
            prospecting, analytics, read
        """
        url = "/smart-prospect/analytics"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    # ==================== Discovery & Tooling ====================

    def list_tools(self) -> List[Any]:
        """
        Exposes the comprehensive Smartlead toolset.
        All tools are professionally categorized and documented for agentic use.
        """
        return [
            # Campaigns
            self.list_campaigns,
            self.get_campaign,
            self.create_campaign,
            self.update_campaign_status,
            self.update_campaign_settings,
            self.update_campaign_schedule,
            self.get_campaign_sequences,
            self.save_campaign_sequence,
            self.create_campaign_subsequence,
            self.list_campaign_email_accounts,
            self.add_campaign_email_account,
            self.remove_campaign_email_account,
            self.forward_campaign_email,
            self.reply_campaign_email_thread,
            self.send_campaign_test_email,
            self.update_campaign_team_member,
            self.delete_campaign,
            
            # Campaign Leads
            self.add_leads_to_campaign,
            self.list_campaign_leads,
            self.get_campaign_lead_by_id,
            self.get_campaign_lead_history,
            self.get_campaign_leads_history_bulk,
            self.get_campaign_all_leads_activities,
            self.update_campaign_lead,
            self.update_campaign_lead_category,
            self.update_campaign_lead_email_account,
            self.pause_lead_in_campaign,
            self.resume_lead_in_campaign,
            self.mark_campaign_lead_complete,
            self.unsubscribe_campaign_lead,
            self.delete_campaign_lead,
            self.export_campaign_leads,
            
            # Global Leads
            self.get_lead_by_email,
            self.get_leads_by_campaign,
            self.add_lead_to_campaign_globally,
            self.update_lead,
            self.delete_lead_globally,
            self.pause_lead_globally,
            self.resume_lead_globally,
            self.unsubscribe_lead_globally,
            self.get_lead_categories,
            self.get_lead_activities,
            self.get_lead_message_history,

            # Lead Notes & Tasks
            self.create_lead_note,
            self.get_all_lead_notes,
            self.create_lead_task,
            self.get_all_lead_tasks,

            # Lead Lists
            self.create_lead_list,
            self.get_all_lead_lists,
            self.get_lead_list_by_id,
            self.update_lead_list,
            self.delete_lead_list,
            self.import_leads_to_list,
            self.push_leads_between_lists,
            self.push_lead_list_to_campaign,
            self.assign_tags_to_lead_list,
            
            # Email Accounts
            self.list_email_accounts,
            self.create_email_account,
            self.get_email_account_warmup_stats,
            
            # Master Inbox
            self.get_unread_replies,
            self.get_sent_emails,
            self.get_important_emails,
            self.get_archived_emails,
            self.get_unread_count,
            self.get_snoozed_emails,
            self.get_untracked_replies,
            self.get_inbox_item_by_id,
            self.reply_to_email,
            self.forward_email,
            self.change_read_status,
            self.update_lead_category,
            self.update_lead_revenue,
            self.assign_team_member,
            self.block_email_domains,
            self.set_lead_reminder,
            
            # Smart Delivery
            self.create_manual_placement_test,
            self.list_all_tests,
            self.geo_wise_report,
            self.provider_wise_report,
            
            # Smart Senders
            self.auto_generate_mailboxes,
            self.place_order,
            self.get_orders,
            
            # Webhooks
            self.list_webhooks,
            self.create_webhook,
            self.delete_webhook,
            
            # Tags
            self.create_tag,
            self.add_tags_to_lead,
            self.list_tags,
            
            # Smart Prospect (B2B Database)
            self.search_contacts_api,
            self.fetch_contacts_api,
            self.save_search_api,
            self.get_saved_searches_api,
            self.get_recent_searches_api,
            self.find_emails_api,
            self.get_industries_api,
            self.get_departments_api,
            self.get_revenue_api,
            self.get_levels_api,
            self.get_countries_api,
            self.get_head_counts_api,
            self.get_company_api,
            self.get_job_title_api,
            self.search_analytics_api,        
        ]
