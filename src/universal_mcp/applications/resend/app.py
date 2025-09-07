from typing import Any

import resend
from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration


class ResendApp(APIApplication):
    def __init__(self, integration: Integration, **kwargs: Any) -> None:
        super().__init__(name="resend", integration=integration, **kwargs)
        self._api_key = None

    @property
    def api_key(self) -> str:
        if self._api_key is None:
            if not self.integration:
                raise NotAuthorizedError("Resend integration not configured.")
            credentials = self.integration.get_credentials()
            api_key = (
                credentials.get("api_key")
                or credentials.get("API_KEY")
                or credentials.get("apiKey")
            )
            if not api_key:
                raise NotAuthorizedError("Resend API key not found in credentials.")
            self._api_key = api_key
            resend.api_key = self._api_key
        return self._api_key

    def send_email(
        self,
        from_email: str,
        to_emails: list[str],
        subject: str,
        text: str,
    ) -> dict[str, Any]:
        """
        Sends an email to specified recipients using the Resend API.

        Args:
            from_email: The email address to send the email from in this format:- Ankit <ankit@agentr.dev>
            to_emails: A list of email addresses to send the email to.
            subject: The subject of the email.
            text: The text content of the email.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: If the email fails to send due to an API error.

        Tags:
            send, email, api, communication, important
        """
        self.api_key
        params: resend.Emails.SendParams = {
            "from": from_email,
            "to": to_emails,
            "subject": subject,
            "text": text,
        }
        try:
            email = resend.Emails.send(params)
            return email
        except Exception as e:
            raise ToolError(f"Failed to send email: {e}")

    def send_batch_emails(
        self,
        emails: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        Sends a batch of emails using the Resend API.

        Args:
            emails: A list of dictionaries containing parameters for individual emails, such as `from`, `to`, `subject`, `html`, and `text`.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: If the batch email sending fails or if the number of emails is not between 1 and 100.

        Tags:
            batch, send, emails, resend-api
        """
        self.api_key
        if not 1 <= len(emails) <= 100:
            raise ToolError(
                "The number of emails in a batch must be between 1 and 100."
            )
        params: list[resend.Emails.SendParams] = emails
        try:
            sent_emails_response = resend.Batch.send(params)
            return sent_emails_response
        except Exception as e:
            raise ToolError(f"Failed to send batch emails: {e}")

    def get_email(self, email_id: str) -> dict[str, Any]:
        """
        Retrieves a single email by its specified ID.

        Args:
            email_id: The unique identifier of the email to retrieve.

        Returns:
            A dictionary containing the details of the retrieved email.

        Raises:
            ToolError: Raised if the retrieval of the email fails due to an internal error.

        Tags:
            retrieve, email, management
        """
        self.api_key
        try:
            email = resend.Emails.get(email_id=email_id)
            return email
        except Exception as e:
            raise ToolError(f"Failed to retrieve email: {e}")

    def update_scheduled_email(
        self, email_id: str, scheduled_at: str
    ) -> dict[str, Any]:
        """
        Updates the scheduling of an email to a new time.

        Args:
            email_id: The ID of the email to update.
            scheduled_at: The new scheduled time in ISO 8601 format.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: If updating the scheduled email fails.

        Tags:
            update, email, async_job, management
        """
        self.api_key
        params: resend.Emails.UpdateParams = {
            "id": email_id,
            "scheduled_at": scheduled_at,
        }
        try:
            response = resend.Emails.update(params=params)
            return response
        except Exception as e:
            raise ToolError(f"Failed to update scheduled email: {e}")

    def cancel_scheduled_email(self, email_id: str) -> dict[str, Any]:
        """
        Cancels a scheduled email using the provided email ID.

        Args:
            email_id: The ID of the scheduled email to cancel.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: If canceling the scheduled email fails.

        Tags:
            cancel, email, management
        """
        self.api_key
        try:
            response = resend.Emails.cancel(email_id=email_id)
            return response
        except Exception as e:
            raise ToolError(f"Failed to cancel scheduled email: {e}")

    def create_domain(self, name: str) -> dict[str, Any]:
        """
        Creates a new domain with the specified name.

        Args:
            name: The name of the domain to create (e.g., 'example.com')

        Returns:
            A dictionary containing the created domain object and its details.

        Raises:
            ToolError: If the domain creation fails due to API errors or invalid input.

        Tags:
            create, domain, management, api, batch, important
        """
        self.api_key
        params: resend.Domains.CreateParams = {"name": name}
        try:
            domain = resend.Domains.create(params)
            return domain
        except Exception as e:
            raise ToolError(f"Failed to create domain: {e}")

    def get_domain(self, domain_id: str) -> dict[str, Any]:
        """
        Retrieves a single domain by its ID.

        Args:
            domain_id: The ID of the domain to retrieve.

        Returns:
            A dictionary containing the domain object.

        Raises:
            ToolError: Raised if the domain retrieval fails.

        Tags:
            retrieve, domain, management
        """
        self.api_key
        try:
            domain = resend.Domains.get(domain_id=domain_id)
            return domain
        except Exception as e:
            raise ToolError(f"Failed to retrieve domain: {e}")

    def verify_domain(self, domain_id: str) -> dict[str, Any]:
        """
        Verifies an existing domain using the provided domain ID.

        Args:
            domain_id: The ID of the domain to verify.

        Returns:
            A dictionary containing the response from the domain verification API.

        Raises:
            ToolError: If the domain verification process fails.

        Tags:
            verify, domain
        """
        self.api_key
        try:
            response = resend.Domains.verify(domain_id=domain_id)
            return response
        except Exception as e:
            raise ToolError(f"Failed to verify domain: {e}")

    def update_domain(
        self,
        domain_id: str,
        open_tracking: bool | None = None,
        click_tracking: bool | None = None,
        tls: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates an existing domain's settings regarding open tracking, click tracking, and TLS enforcement.

        Args:
            domain_id: The ID of the domain to update.
            open_tracking: Enable or disable open tracking.
            click_tracking: Enable or disable click tracking.
            tls: The TLS enforcement policy (enforced or opportunistic).

        Returns:
            A dictionary containing the updated domain object.

        Raises:
            ToolError: Raised if updating the domain fails.

        Tags:
            update, domain, management
        """
        self.api_key
        params: resend.Domains.UpdateParams = {"id": domain_id}
        if open_tracking is not None:
            params["open_tracking"] = open_tracking
        if click_tracking is not None:
            params["click_tracking"] = click_tracking
        if tls is not None:
            params["tls"] = tls
        try:
            updated_domain = resend.Domains.update(params)
            return updated_domain
        except Exception as e:
            raise ToolError(f"Failed to update domain: {e}")

    def list_domains(self) -> list[dict[str, Any]]:
        """
        Retrieves a list of all domains for the authenticated user.

        Returns:
            A list of dictionaries, each representing a domain.

        Raises:
            ToolError: If listing the domains fails.

        Tags:
            list, domains, important, management
        """
        self.api_key
        try:
            domains = resend.Domains.list()
            return domains
        except Exception as e:
            raise ToolError(f"Failed to list domains: {e}")

    def remove_domain(self, domain_id: str) -> dict[str, Any]:
        """
        Removes an existing domain by its ID using the Resend API.

        Args:
            domain_id: The unique identifier of the domain to be removed.

        Returns:
            A dictionary containing the response from the Resend API after attempting to remove the domain.

        Raises:
            ToolError: Raised if the operation to remove the domain fails, including if the API call encounters an error.

        Tags:
            remove, management, api, domain
        """
        self.api_key
        try:
            response = resend.Domains.remove(domain_id=domain_id)
            return response
        except Exception as e:
            raise ToolError(f"Failed to remove domain: {e}")

    def create_api_key(self, name: str) -> dict[str, Any]:
        """
        Creates a new API key for authenticating with Resend.

        Args:
            name: The name of the API key (e.g., 'Production').

        Returns:
            A dictionary containing the new API key object.

        Raises:
            ToolError: Raised if API key creation fails.

        Tags:
            create, api-key, authentication
        """
        self.api_key
        params: resend.ApiKeys.CreateParams = {"name": name}
        try:
            api_key_obj = resend.ApiKeys.create(params)
            return api_key_obj
        except Exception as e:
            raise ToolError(f"Failed to create API key: {e}")

    def list_api_keys(self) -> list[dict[str, Any]]:
        """
        Retrieves a list of all API keys available through the resend service.

        Args:
            None: This function takes no arguments.

        Returns:
            List of dictionaries, each representing an API key with associated details.

        Raises:
            ToolError: If there is a failure when attempting to list the API keys, typically due to an underlying exception from the resend API.

        Tags:
            list, api, important
        """
        self.api_key
        try:
            keys = resend.ApiKeys.list()
            return keys
        except Exception as e:
            raise ToolError(f"Failed to list API keys: {e}")

    def remove_api_key(self, api_key_id: str) -> dict[str, Any]:
        """
        Removes an existing API key using the specified key ID.

        Args:
            api_key_id: The ID of the API key to remove.

        Returns:
            A dictionary containing the response from the Resend API after removing the API key.

        Raises:
            ToolError: Raised if removing the API key fails, including any underlying errors.

        Tags:
            remove, api-key, management
        """
        self.api_key
        try:
            response = resend.ApiKeys.remove(api_key_id=api_key_id)
            return response
        except Exception as e:
            raise ToolError(f"Failed to remove API key: {e}")

    def create_broadcast(
        self,
        audience_id: str,
        from_email: str,
        subject: str,
        html: str,
    ) -> dict[str, Any]:
        """
        Creates a new broadcast to send to a specified audience.

        Args:
            audience_id: The ID of the audience to send the broadcast to.
            from_email: The sender's email address.
            subject: The subject line of the broadcast.
            html: The HTML content of the broadcast. Use {{{...}}} for merge tags.

        Returns:
            A dictionary containing the created broadcast object.

        Raises:
            ToolError: Raised if creating the broadcast fails due to an underlying exception.

        Tags:
            broadcast, email, important
        """
        self.api_key
        params: resend.Broadcasts.CreateParams = {
            "audience_id": audience_id,
            "from": from_email,
            "subject": subject,
            "html": html,
        }
        try:
            broadcast = resend.Broadcasts.create(params)
            return broadcast
        except Exception as e:
            raise ToolError(f"Failed to create broadcast: {e}")

    def get_broadcast(self, broadcast_id: str) -> dict[str, Any]:
        """
        Retrieves a single broadcast by its ID.

        Args:
            broadcast_id: The ID of the broadcast to retrieve.

        Returns:
            A dictionary containing the broadcast object.

        Raises:
            ToolError: Raised if retrieving the broadcast fails.

        Tags:
            retrieve, broadcast
        """
        self.api_key
        try:
            broadcast = resend.Broadcasts.get(id=broadcast_id)
            return broadcast
        except Exception as e:
            raise ToolError(f"Failed to retrieve broadcast: {e}")

    def update_broadcast(
        self,
        broadcast_id: str,
        html: str | None = None,
        subject: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates a broadcast by modifying its HTML content and/or subject line.

        Args:
            broadcast_id: The ID of the broadcast to update.
            html: The new HTML content for the broadcast.
            subject: The new subject line for the broadcast.

        Returns:
            A dictionary containing the updated broadcast object.

        Raises:
            ToolError: Raised if updating the broadcast fails or no update fields are provided.

        Tags:
            update, management, broadcast, api
        """
        self.api_key
        params: resend.Broadcasts.UpdateParams = {"id": broadcast_id}
        if html is not None:
            params["html"] = html
        if subject is not None:
            params["subject"] = subject
        if len(params) == 1:
            raise ToolError(
                "At least one field (e.g., html, subject) must be provided for the update."
            )
        try:
            updated_broadcast = resend.Broadcasts.update(params)
            return updated_broadcast
        except Exception as e:
            raise ToolError(f"Failed to update broadcast: {e}")

    def send_broadcast(
        self, broadcast_id: str, scheduled_at: str | None = None
    ) -> dict[str, Any]:
        """
        Starts sending a broadcast via the API.

        Args:
            broadcast_id: The ID of the broadcast to send.
            scheduled_at: The time to send the broadcast, e.g., 'in 1 min' or an ISO 8601 datetime.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: If sending the broadcast fails.

        Tags:
            broadcast, send, api, management
        """
        self.api_key
        params: resend.Broadcasts.SendParams = {"broadcast_id": broadcast_id}
        if scheduled_at:
            params["scheduled_at"] = scheduled_at
        try:
            response = resend.Broadcasts.send(params)
            return response
        except Exception as e:
            raise ToolError(f"Failed to send broadcast: {e}")

    def remove_broadcast(self, broadcast_id: str) -> dict[str, Any]:
        """
        Removes an existing broadcast with 'draft' status.

        Args:
            broadcast_id: The ID of the broadcast to remove.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: If removing the broadcast fails.

        Tags:
            remove, broadcast, api-management, draft-status
        """
        self.api_key
        try:
            response = resend.Broadcasts.remove(id=broadcast_id)
            return response
        except Exception as e:
            raise ToolError(f"Failed to remove broadcast: {e}")

    def list_broadcasts(self) -> list[dict[str, Any]]:
        """
        Retrieves a list of all available broadcasts using the configured API key.

        Returns:
            A list of dictionaries, each representing a broadcast with its attributes.

        Raises:
            ToolError: If listing broadcasts fails due to a connection, API, or other retrieval error.

        Tags:
            list, broadcast, api, management, important
        """
        self.api_key
        try:
            broadcasts = resend.Broadcasts.list()
            return broadcasts
        except Exception as e:
            raise ToolError(f"Failed to list broadcasts: {e}")

    def create_audience(self, name: str) -> dict[str, Any]:
        """
        Creates a new audience (a list of contacts) with the specified name.

        Args:
            name: The name of the audience (e.g., "Registered Users").

        Returns:
            A dictionary containing the created audience object.

        Raises:
            ToolError: If creating the audience fails due to an underlying error.

        Tags:
            create, audience, management, important
        """
        self.api_key
        params: resend.Audiences.CreateParams = {"name": name}
        try:
            audience = resend.Audiences.create(params)
            return audience
        except Exception as e:
            raise ToolError(f"Failed to create audience: {e}")

    def get_audience(self, audience_id: str) -> dict[str, Any]:
        """
        Retrieves a single audience object from the API using the specified audience ID.

        Args:
            audience_id: The unique identifier of the audience to retrieve.

        Returns:
            A dictionary containing all data for the requested audience object.

        Raises:
            ToolError: If retrieving the audience from the API fails, with a message describing the error.

        Tags:
            fetch, audience, management, api
        """
        self.api_key
        try:
            audience = resend.Audiences.get(id=audience_id)
            return audience
        except Exception as e:
            raise ToolError(f"Failed to retrieve audience: {e}")

    def remove_audience(self, audience_id: str) -> dict[str, Any]:
        """
        Removes an existing audience using the provided audience ID and returns the API response.

        Args:
            audience_id: The unique identifier of the audience to remove.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: Raised if removing the audience fails due to API error or other issues.

        Tags:
            remove, audience, management, api
        """
        self.api_key
        try:
            response = resend.Audiences.remove(id=audience_id)
            return response
        except Exception as e:
            raise ToolError(f"Failed to remove audience: {e}")

    def list_audiences(self) -> list[dict[str, Any]]:
        """
        Retrieves a list of all audiences.

        Returns:
            A list of dictionaries, each representing an audience.

        Raises:
            ToolError: Raised if listing the audiences fails due to an internal error.

        Tags:
            list, audiences, management, important
        """
        self.api_key
        try:
            audiences = resend.Audiences.list()
            return audiences
        except Exception as e:
            raise ToolError(f"Failed to list audiences: {e}")

    def create_contact(
        self,
        audience_id: str,
        email: str,
        first_name: str | None = None,
        last_name: str | None = None,
        unsubscribed: bool = False,
    ) -> dict[str, Any]:
        """
        Creates a contact within a specific audience.

        Args:
            audience_id: The ID of the audience to add the contact to.
            email: The email address of the contact.
            first_name: The contact's first name.
            last_name: The contact's last name.
            unsubscribed: The contact's subscription status.

        Returns:
            A dictionary containing the created contact's ID.

        Raises:
            ToolError: Raised if creating the contact fails.

        Tags:
            create, contact, management, important
        """
        self.api_key
        params: resend.Contacts.CreateParams = {
            "audience_id": audience_id,
            "email": email,
            "unsubscribed": unsubscribed,
        }
        if first_name:
            params["first_name"] = first_name
        if last_name:
            params["last_name"] = last_name
        try:
            contact = resend.Contacts.create(params)
            return contact
        except Exception as e:
            raise ToolError(f"Failed to create contact: {e}")

    def get_contact(
        self, audience_id: str, contact_id: str | None = None, email: str | None = None
    ) -> dict[str, Any]:
        """
        Retrieves a single contact from an audience by providing either a unique contact ID or an email address, ensuring exactly one identifier is given.

        Args:
            audience_id: The ID of the audience in which to search for the contact.
            contact_id: The unique ID of the contact, if available. Exactly one of 'contact_id' or 'email' must be provided.
            email: The email address of the contact, if available. Exactly one of 'contact_id' or 'email' must be provided.

        Returns:
            A dictionary containing the retrieved contact object, with details such as ID, email, and other contact attributes.

        Raises:
            ToolError: Raised if neither 'contact_id' nor 'email' is provided, if both are provided (ambiguous identifier), or if retrieval from the API fails.

        Tags:
            retrieve, contact, audience, management, api
        """
        self.api_key
        if not (contact_id or email) or (contact_id and email):
            raise ToolError("You must provide exactly one of 'contact_id' or 'email'.")
        params = {"audience_id": audience_id}
        if contact_id:
            params["id"] = contact_id
        if email:
            params["email"] = email
        try:
            contact = resend.Contacts.get(**params)
            return contact
        except Exception as e:
            raise ToolError(f"Failed to retrieve contact: {e}")

    def update_contact(
        self,
        audience_id: str,
        contact_id: str | None = None,
        email: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        unsubscribed: bool | None = None,
    ) -> dict[str, Any]:
        """
        Updates an existing contact, identified by ID or email, within a specified audience.

        Args:
            audience_id: The ID of the audience containing the contact.
            contact_id: The ID of the contact to update.
            email: The email of the contact to update.
            first_name: The new first name for the contact.
            last_name: The new last name for the contact.
            unsubscribed: The new subscription status for the contact.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: Raised if the update fails, if an identifier is missing, or if no update fields are provided.

        Tags:
            update, contact, management
        """
        self.api_key
        if not (contact_id or email) or (contact_id and email):
            raise ToolError(
                "You must provide exactly one of 'contact_id' or 'email' to identify the contact."
            )
        params: resend.Contacts.UpdateParams = {"audience_id": audience_id}
        if contact_id:
            params["id"] = contact_id
        if email:
            params["email"] = email
        if first_name is not None:
            params["first_name"] = first_name
        if last_name is not None:
            params["last_name"] = last_name
        if unsubscribed is not None:
            params["unsubscribed"] = unsubscribed
        if len(params) <= 2:  # Only audience_id and one identifier
            raise ToolError(
                "At least one field to update (e.g., first_name, unsubscribed) must be provided."
            )
        try:
            response = resend.Contacts.update(params)
            return response
        except Exception as e:
            raise ToolError(f"Failed to update contact: {e}")

    def remove_contact(
        self, audience_id: str, contact_id: str | None = None, email: str | None = None
    ) -> dict[str, Any]:
        """
        Removes a contact from an audience, identified by ID or email.

        Args:
            audience_id: The ID of the audience.
            contact_id: The ID of the contact to remove.
            email: The email of the contact to remove.

        Returns:
            A dictionary containing the response from the Resend API.

        Raises:
            ToolError: If contact removal fails, or if the contact identifier is missing or ambiguous.

        Tags:
            remove, contact-management, api-call
        """
        self.api_key
        if not (contact_id or email) or (contact_id and email):
            raise ToolError("You must provide exactly one of 'contact_id' or 'email'.")
        params = {"audience_id": audience_id}
        if contact_id:
            params["id"] = contact_id
        if email:
            params["email"] = email
        try:
            response = resend.Contacts.remove(**params)
            return response
        except Exception as e:
            raise ToolError(f"Failed to remove contact: {e}")

    def list_contacts(self, audience_id: str) -> list[dict[str, Any]]:
        """
        Lists all contacts from a specified audience.

        Args:
            audience_id: The ID of the audience whose contacts you want to list.

        Returns:
            A list of dictionaries, each representing a contact in the audience.

        Raises:
            ToolError: Raised if listing the contacts fails.

        Tags:
            list, contacts, management, important
        """
        self.api_key
        try:
            contacts = resend.Contacts.list(audience_id=audience_id)
            return contacts
        except Exception as e:
            raise ToolError(f"Failed to list contacts: {e}")

    def list_tools(self) -> list[callable]:
        return [
            self.send_email,
            self.send_batch_emails,
            self.get_email,
            self.update_scheduled_email,
            self.cancel_scheduled_email,
            self.create_domain,
            self.get_domain,
            self.verify_domain,
            self.update_domain,
            self.list_domains,
            self.remove_domain,
            self.create_api_key,
            self.list_api_keys,
            self.remove_api_key,
            self.create_broadcast,
            self.get_broadcast,
            self.update_broadcast,
            self.send_broadcast,
            self.remove_broadcast,
            self.list_broadcasts,
            self.create_audience,
            self.get_audience,
            self.remove_audience,
            self.list_audiences,
            self.create_contact,
            self.get_contact,
            self.update_contact,
            self.remove_contact,
            self.list_contacts,
        ]
