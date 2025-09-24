from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration

import resend


class ResendApp(APIApplication):
    def __init__(self, integration: Integration, **kwargs: Any) -> None:
        super().__init__(name="resend", integration=integration, **kwargs)
        self._api_key = None

    @property
    def api_key(self) -> str:
        """
        A property that lazily retrieves, validates, and caches the Resend API key from integration credentials. On first access, it configures the `resend` library, raising an error if authentication fails. This ensures the application is authenticated for all subsequent API calls within the class.
        """
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
        Sends a single email with a specified subject and text body to a list of recipients via the Resend API. Unlike `send_batch_emails`, which processes multiple distinct emails at once, this function is designed for dispatching one individual email composition per API call.

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
        Sends multiple emails (1-100) in a single API request. Unlike the `send_email` function which handles a single message, this accepts a list of email objects for efficient, high-volume delivery. It validates that the batch size is within the allowed limits before making the API call.

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

    def retrieve_email_by_id(self, email_id: str) -> dict[str, Any]:
        """
        Retrieves the details and status of a single email from the Resend API using its unique identifier. This function allows for looking up a specific email that has already been sent or scheduled, distinct from functions that initiate sending.

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

    def reschedule_email(self, email_id: str, scheduled_at: str) -> dict[str, Any]:
        """
        Modifies the delivery time for a specific, previously scheduled email using its ID. It updates the `scheduled_at` attribute to a new ISO 8601 formatted time, effectively rescheduling its dispatch. This differs from `cancel_scheduled_email`, which permanently stops the send.

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
        Cancels a previously scheduled email using its unique ID, preventing it from being sent. This function calls the Resend API's cancellation endpoint, returning a confirmation response. It is distinct from `update_scheduled_email`, which reschedules the email instead of stopping its transmission.

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
        Registers a new sending domain with the Resend service using the provided name. This is a prerequisite for sending emails from your own domain and returns a dictionary containing details of the new domain object, which can then be verified and managed with other domain-related functions.

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
        Retrieves the details of a specific domain from the Resend API using its unique ID. Unlike `list_domains`, which fetches all domains, this function targets a single record and returns a dictionary containing the domain's properties, like its verification status and tracking settings.

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
        Triggers the verification process for a registered domain using its unique ID. This action is crucial for authorizing the domain to send emails via Resend and returns an API response containing the verification status and necessary DNS records to complete the process.

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

    def update_domain_settings(
        self,
        domain_id: str,
        open_tracking: bool | None = None,
        click_tracking: bool | None = None,
        tls: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates settings for a specific domain identified by its ID. This function can modify configurations like open and click tracking, and TLS enforcement. It returns the updated domain object from the API, raising a ToolError if the update fails. Only the provided settings are modified.

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
        Fetches a complete list of all domains registered with the Resend account. Unlike `get_domain`, which retrieves a single domain by ID, this provides a comprehensive overview of all configured domains for management and verification tasks.

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
        Permanently removes a specific domain from the Resend account using its unique ID. This function makes an authenticated API call to delete the domain, distinguishing it from retrieval (`get_domain`) or modification (`update_domain`) operations, and raises an error if the process fails.

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
        Creates a new API key for authenticating with the Resend service, identified by a specified name. It returns a dictionary containing the new key object, including the generated token required for subsequent API requests.

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
        Retrieves a list of all API keys for the authenticated Resend account. This read-only operation allows for auditing and viewing existing credentials, contrasting with `create_api_key` and `remove_api_key` which are used to add or delete keys.

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
        Deletes a specific Resend API key identified by its unique ID. This function, part of the key management suite alongside `create_api_key` and `list_api_keys`, returns an API confirmation response or raises a `ToolError` if the operation fails.

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

    def register_broadcast(
        self,
        audience_id: str,
        from_email: str,
        subject: str,
        html: str,
    ) -> dict[str, Any]:
        """
        Registers a new email broadcast campaign for a specific audience using the Resend API. This function creates the broadcast object but does not send it; use the `send_broadcast` function to dispatch the created campaign to the audience.

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
        Retrieves a specific broadcast's complete details, including its status and content, by its unique ID. Unlike `list_broadcasts` which retrieves all broadcasts, this function targets a single entry for inspection.

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
        Updates the HTML content and/or subject of an existing broadcast, identified by its ID. Requires that at least one modifiable field (html or subject) is provided. This function alters a broadcast's content, differing from `send_broadcast` which triggers its delivery.

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

    def send_or_schedule_broadcast(
        self, broadcast_id: str, scheduled_at: str | None = None
    ) -> dict[str, Any]:
        """
        Initiates the delivery of a pre-existing broadcast, identified by its ID, to its target audience. The broadcast can be sent immediately or scheduled for a future time via the optional `scheduled_at` parameter. It returns the API response upon execution.

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

    def remove_draft_broadcast(self, broadcast_id: str) -> dict[str, Any]:
        """
        Deletes a broadcast from the Resend service using its unique ID. This action is restricted to broadcasts that have a 'draft' status and have not been sent, returning the API's response upon successful removal or raising an error if the operation fails.

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
        Retrieves a list of all broadcasts associated with the authenticated account. Unlike `get_broadcast` which fetches a single item by ID, this function returns a list of dictionaries, each containing the attributes of a specific broadcast. Raises a `ToolError` on API failure.

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
        Creates a new audience, a named list for contacts, within the Resend service. This function requires a name for the audience and returns a dictionary representing the newly created object, enabling subsequent management of contacts within that specific list.

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
        Retrieves the details of a single audience using its unique ID. This provides a targeted lookup for one audience, distinct from `list_audiences` which fetches all available audiences in the account.

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
        Deletes a specific audience from the Resend service using its unique identifier. This function wraps the Resend API's remove operation, returning the API's response. Unlike `remove_contact`, which targets individuals, this function removes the entire contact list defined by the audience ID.

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
        Retrieves a complete list of all audiences from the Resend account. It returns a list of dictionaries, with each containing the details of a specific audience. This function is distinct from `get_audience`, which fetches a single audience by its ID.

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
        Creates a new contact with a given email, optional name, and subscription status, adding it to a specific audience. This function populates audience lists, differing from `update_contact` which modifies existing entries, and requires a valid `audience_id` to function.

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
        Fetches a single contact's details from a specified audience by its unique ID or email address. The function requires exactly one identifier for the lookup, raising an error if the identifier is missing, ambiguous, or if the API call fails.

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
        Updates an existing contact's details (e.g., name, subscription status) within a specific audience. The contact is identified by its unique ID or email address. This function validates inputs and returns the Resend API response, raising a ToolError on failure or if arguments are invalid.

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
        Removes a contact from a specified audience. The contact must be identified by either its unique ID or email address, but not both. Raises an error if the identifier is missing, ambiguous, or if the API call to the Resend service fails.

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
        Retrieves a complete list of contacts belonging to a specific audience, identified by its unique ID. This function returns all contacts within the audience, unlike `get_contact` which retrieves only a single contact by its ID or email.

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
            self.retrieve_email_by_id,
            self.reschedule_email,
            self.cancel_scheduled_email,
            self.create_domain,
            self.get_domain,
            self.verify_domain,
            self.update_domain_settings,
            self.list_domains,
            self.remove_domain,
            self.create_api_key,
            self.list_api_keys,
            self.remove_api_key,
            self.register_broadcast,
            self.get_broadcast,
            self.update_broadcast,
            self.send_or_schedule_broadcast,
            self.remove_draft_broadcast,
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
