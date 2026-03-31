from typing import Literal
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
                "Smartlead API key not found in integration credentials."
            )
        return api_key

    async def _aget_headers(self) -> dict[str, str]:
        return {}

    def _get_headers(self) -> dict[str, str]:
        return {}

    @asynccontextmanager
    async def get_async_client(self):  # type: ignore[override]
        api_key = await self._aget_api_key()
        async with httpx.AsyncClient(
            base_url=self.base_url,
            params={"api_key": api_key},
            timeout=self.default_timeout,
        ) as client:
            yield client

    @contextmanager
    def get_sync_client(self):  # type: ignore[override]
        api_key = self._get_api_key()
        with httpx.Client(
            base_url=self.base_url,
            params={"api_key": api_key},
            timeout=self.default_timeout,
        ) as client:
            yield client

    # ==================== Campaign Operations ====================

    async def list_campaigns(self,  client_id: Optional[int] = None, status: Optional[str] = None, limit: int = 100, offset: int = 0, include_tags: bool = False):
        """
        Retrieves a list of campaigns. Supports pagination, status filtering, and tags.

        Args:
            client_id: The client_id.
            status: The status.
            limit: The limit.
            offset: The offset.
            include_tags: The include_tags.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        params = {
            "include_tags": "true" if include_tags else "false",
            "client_id": client_id,
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        url = "/campaigns/"
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_campaign(self,  campaign_id: int):
        """
        Fetches the complete granular configuration and state of a specific campaign by its ID.

        Args:
            campaign_id: The campaign_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.

        Tags:
            smartlead, important
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_campaign(self,  name: str, client_id: Optional[int] = None, **kwargs):
        """
        Generates a brand new email campaign within the Smartlead account.

        Args:
            name: The name.
            client_id: The client_id.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        if not name: raise ValueError("Missing 'name'.")
        json_data = {"name": name, **kwargs}
        if client_id is not None:
            json_data["client_id"] = client_id
            
        url = "/campaigns/create"
        response = await self._apost(url, data=json_data)
        response.raise_for_status()
        return response.json()

    async def update_campaign_status(self,  campaign_id: int, status: Literal["START", "PAUSED", "STOPPED"]):
        """
        Transitions an existing campaign into a new operational state (e.g., START, PAUSED).

        Args:
            campaign_id: The campaign_id.
            status: The status.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        if campaign_id is None or not status: raise ValueError("Missing parameters.")
        url = f"/campaigns/{campaign_id}/status"
        # Fix: Smartlead uses POST for status updates, not PATCH.
        response = await self._apost(url, data={"status": status})
        response.raise_for_status()
        return response.json()

    async def update_campaign_schedule(self,  campaign_id: int, timezone: str, days: List[int], start_hour: str, end_hour: str, min_time_btw_emails: Optional[int] = None):
        """
        Adjusts the active sending windows for a campaign.

        Args:
            campaign_id: The campaign_id.
            timezone: The timezone.
            days: The days.
            start_hour: The start_hour.
            end_hour: The end_hour.
            min_time_btw_emails: The min_time_btw_emails.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/schedule"
        schedule_data: dict[str, Any] = {
            "timezone": timezone,
            "days": days,
            "start_hour": start_hour,
            "end_hour": end_hour,
        }
        if min_time_btw_emails is not None: schedule_data["min_time_btw_emails"] = min_time_btw_emails
            
        response = await self._apost(url, data={"schedule": schedule_data})
        response.raise_for_status()
        return response.json()

    async def update_campaign_settings(self,  campaign_id: int, **kwargs):
        """
        Updates general settings of an existing campaign (e.g., tracking, sending limit).

        Args:
            campaign_id: The campaign_id.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}/settings"
        response = await self._apost(url, data=kwargs)
        response.raise_for_status()
        return response.json()

    async def delete_campaign(self,  campaign_id: int):
        """
        Permanently destroys a campaign and all its associated data within the workspace.

        Args:
            campaign_id: The campaign_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        if campaign_id is None: raise ValueError("Missing 'campaign_id'.")
        url = f"/campaigns/{campaign_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    # ==================== Sequences / Email Interaction ====================

    async def get_campaign_sequences(self,  campaign_id: int):
        """
        Retrieves the ordered series of email steps (sequences) defined for a specific campaign.

        Args:
            campaign_id: The campaign_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/sequences"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def save_campaign_sequence(self,  campaign_id: int, sequence_data: dict[str, Any]):
        """
        Updates or completely overwrites the multi-step email sequence logic for a campaign.

        Args:
            campaign_id: The campaign_id.
            sequence_data: The sequence_data.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/sequences"
        response = await self._apost(url, data=sequence_data)
        response.raise_for_status()
        return response.json()

    async def create_campaign_subsequence(self,  campaign_id: int, sequence_id: int, subsequence_data: dict[str, Any]):
        """
        Creates an A/B test subsequence (variant) for a specific step.

        Args:
            campaign_id: The campaign_id.
            sequence_id: The sequence_id.
            subsequence_data: The subsequence_data.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        if not campaign_id or not sequence_id: raise ValueError("Missing IDs.")
        url = f"/campaigns/{campaign_id}/sequences/{sequence_id}/subsequences"
        response = await self._apost(url, data=subsequence_data)
        response.raise_for_status()
        return response.json()

    async def forward_campaign_email(self,  campaign_id: int, forward_data: dict[str, Any]):
        """
        Forwards an email thread for a lead in a campaign.

        Args:
            campaign_id: The campaign_id.
            forward_data: The forward_data.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/forward-email"
        response = await self._apost(url, data=forward_data)
        response.raise_for_status()
        return response.json()

    async def reply_campaign_email_thread(self,  campaign_id: int, reply_data: dict[str, Any]):
        """
        Replies to an ongoing email thread for a lead inside a campaign.

        Args:
            campaign_id: The campaign_id.
            reply_data: The reply_data.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/reply-email-thread"
        response = await self._apost(url, data=reply_data)
        response.raise_for_status()
        return response.json()

    async def send_campaign_test_email(self,  campaign_id: int, to_email: str, email_account_id: int):
        """
        Sends a test email to preview sequence logic before starting a campaign.

        Args:
            campaign_id: The campaign_id.
            to_email: The to_email.
            email_account_id: The email_account_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/send-test-email"
        response = await self._apost(url, data={"to_email": to_email, "email_account_id": email_account_id})
        response.raise_for_status()
        return response.json()

    # ==================== Accounts & Team ====================

    async def list_campaign_email_accounts(self,  campaign_id: int):
        """
        Identifies which sender email accounts are assigned to a campaign.

        Args:
            campaign_id: The campaign_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/email-accounts"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def add_campaign_email_account(self,  campaign_id: int, email_account_ids: List[int]):
        """
        Assigns new sender mailboxes to a campaign's round-robin pool.

        Args:
            campaign_id: The campaign_id.
            email_account_ids: The email_account_ids.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/email-accounts"
        response = await self._apost(url, data={"email_account_ids": email_account_ids})
        response.raise_for_status()
        return response.json()

    async def remove_campaign_email_account(self,  campaign_id: int, email_account_ids: List[int]):
        """
        Detaches specific sender mailboxes from a campaign.

        Args:
            campaign_id: The campaign_id.
            email_account_ids: The email_account_ids.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/email-accounts"
        async with self.get_async_client() as client:
            response = await client.request("DELETE", url, json={"email_account_ids": email_account_ids})
        response.raise_for_status()
        return response.json()

    async def update_campaign_team_member(self,  campaign_id: int, team_member_ids: List[int]):
        """
        Updates team member access/assignments for a campaign.

        Args:
            campaign_id: The campaign_id.
            team_member_ids: The team_member_ids.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/update-team-member"
        response = await self._apost(url, data={"team_member_ids": team_member_ids})
        response.raise_for_status()
        return response.json()

    # ==================== Lead Operations ====================

    async def add_leads_to_campaign(self,  campaign_id: int, leads: List[dict[str, Any]]):
        """
        Injects a set of new prospects into a campaign.

        Args:
            campaign_id: The campaign_id.
            leads: The leads.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads"
        response = await self._apost(url, data={"lead_list": leads})
        response.raise_for_status()
        return response.json()

    async def list_campaign_leads(self,  campaign_id: int, limit: int = 100, offset: int = 0):
        """
        Retrieves the prospects (leads) currently residing inside a specific campaign.

        Args:
            campaign_id: The campaign_id.
            limit: The limit.
            offset: The offset.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        params = {"limit": limit, "offset": offset}
        url = f"/campaigns/{campaign_id}/leads"
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_campaign_lead_by_id(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """
        Gets specific lead details inside a targeted campaign.

        Args:
            campaign_id: The campaign_id.
            lead_id: The lead_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/leads/{lead_id}/campaign-overview"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_campaign_lead_history(self,  campaign_id: int, lead_id: int):
        """
        Gets sequence and message history for a specific lead in a campaign.

        Args:
            campaign_id: The campaign_id.
            lead_id: The lead_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/message-history"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_campaign_leads_history_bulk(self,  campaign_id: int, lead_ids: list[int]):
        """
        Gets bulk history for specific leads within a campaign.

        Args:
            campaign_id: The ID of the campaign.
            lead_ids: A list of lead IDs to fetch history for.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/message-history-for-leads"
        response = await self._apost(url, data={"lead_ids": lead_ids})
        response.raise_for_status()
        return response.json()

    async def get_campaign_all_leads_activities(self, limit: int = 100, offset: int = 0, event_time_from: str | int | None = None, event_time_to: str | int | None = None):
        """
        Retrieves a global activity feed of events (clicks, opens, replies) across all campaigns.

        Args:
            limit: Max records to return (default 100).
            offset: Number of records to skip (default 0).
            event_time_from: Filter events after this ISO timestamp or Unix integer.
            event_time_to: Filter events before this ISO timestamp or Unix integer.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = "/campaigns/all-leads-activities"
        params: dict[str, Any] = {"limit": limit, "offset": offset}
        if event_time_from:
            params["event_time_from"] = event_time_from
        if event_time_to:
            params["event_time_to"] = event_time_to
            
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def update_campaign_lead(self,  campaign_id: int, lead_id: int, update_data: dict[str, Any]):
        """
        Updates specific lead data within the context of a single campaign.

        Args:
            campaign_id: The campaign_id.
            lead_id: The lead_id.
            update_data: The update_data.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads/{lead_id}"
        response = await self._apost(url, data=update_data)
        response.raise_for_status()
        return response.json()

    async def update_campaign_lead_category(self,  campaign_id: int, lead_id: int, category_id: int, pause_lead: bool = False):
        """
        Assign or change the category for a lead within a campaign (e.g., Interested).

        Args:
            campaign_id: The campaign_id.
            lead_id: The lead_id.
            category_id: The category_id.
            pause_lead: The pause_lead.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/category"
        response = await self._apost(url, data={"category_id": category_id, "pause_lead": pause_lead})
        response.raise_for_status()
        return response.json()

    async def update_campaign_lead_email_account(self,  campaign_id: int, lead_id: int, email_account_id: int, override_lead_email_account: bool = True):
        """
        Assigns or updates a dedicated sending email account for a lead in a campaign.

        Args:
            campaign_id: The ID of the campaign.
            lead_id: The Campaign Lead Map ID.
            email_account_id: The ID of the email account to assign.
            override_lead_email_account: Whether to override existing assignment (default True).

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = "/campaigns/update-lead-email-account"
        data = {
            "email_account_id": email_account_id,
            "email_campaign_id": campaign_id,
            "email_lead_id": lead_id,
            "override_lead_email_account": override_lead_email_account
        }
        response = await self._apost(url, data=data)
        response.raise_for_status()
        return response.json()

    async def pause_lead_in_campaign(self,  campaign_id: int, lead_id: int):
        """
        Temporarily halts outreach for a specific lead inside a campaign.

        Args:
            campaign_id: The campaign_id.
            lead_id: The lead_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/pause"
        response = await self._apost(url, data={})
        response.raise_for_status()
        return response.json()

    async def resume_lead_in_campaign(self,  campaign_id: int, lead_id: int):
        """
        Reactivates a previously paused lead within a targeted campaign.

        Args:
            campaign_id: The campaign_id.
            lead_id: The lead_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/resume"
        response = await self._apost(url, data={})
        response.raise_for_status()
        return response.json()

    async def mark_campaign_lead_complete(self,  campaign_id: int, lead_id: int):
        """
        Marks a lead as successfully completed for this specific campaign sequence.

        Args:
            campaign_id: The ID of the campaign.
            lead_id: The Campaign Lead Map ID.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/manual-complete"
        response = await self._apost(url, data={})
        response.raise_for_status()
        return response.json()

    async def unsubscribe_campaign_lead(self,  campaign_id: int, lead_id: int):
        """
        Unsubscribes a lead specifically from one individual campaign.

        Args:
            campaign_id: The campaign_id.
            lead_id: The lead_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads/{lead_id}/unsubscribe"
        response = await self._apost(url, data={})
        response.raise_for_status()
        return response.json()

    async def delete_campaign_lead(self,  campaign_id: int, lead_id: int):
        """
        Deletes a lead and its tracked history from a specific campaign.

        Args:
            campaign_id: The campaign_id.
            lead_id: The lead_id.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/campaigns/{campaign_id}/leads/{lead_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    # ==================== Global Helper Leads ====================
    
    async def get_lead_by_email(self,  email_address: str):
        """
        Searches for a specific prospect across the entire global Smartlead workspace using their email.

        Args:
            email_address: The email_address.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = "/leads/"
        response = await self._aget(url, params={"email": email_address})
        response.raise_for_status()
        return response.json()

    async def update_lead(self,  contact_id: int, update_data: dict[str, Any]):
        """
        Modifies a lead's profile data globally across all campaigns.

        Args:
            contact_id: The contact_id.
            update_data: The update_data.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = f"/leads/{contact_id}"
        response = await self._aput(url, data=update_data)
        response.raise_for_status()
        return response.json()

    async def unsubscribe_lead_globally(self,  email_address: str):
        """
        Adds a prospect's email address to the global unsubscribe/suppression list.

        Args:
            email_address: The email_address.

        Returns:
            dict: The API response data.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        url = "/leads/unsubscribe-globally"
        response = await self._apost(url, data={"email": email_address})
        response.raise_for_status()
        return response.json()

    def list_tools(self) -> List[Any]:
        """
        Exposes the comprehensive Smartlead toolset.
        All tools are professionally categorized and documented for agentic use.
        """
        return [
            # Campaigns Configuration & Core Operations
            self.list_campaigns,
            self.get_campaign,
            self.create_campaign,
            self.update_campaign_status,
            self.update_campaign_settings,
            self.update_campaign_schedule,
            self.delete_campaign,
            
            # Email Sequences & Messages
            self.get_campaign_sequences,
            self.save_campaign_sequence,
            self.create_campaign_subsequence,
            self.forward_campaign_email,
            self.reply_campaign_email_thread,
            self.send_campaign_test_email,

            # Mailbox & Team Management
            self.list_campaign_email_accounts,
            self.add_campaign_email_account,
            self.remove_campaign_email_account,
            self.update_campaign_team_member,
            
            # Leads Operations
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
            
            # Global Helpers
            self.get_lead_by_email,
            self.update_lead,
            self.unsubscribe_lead_globally,
        ]