from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class CalendlyApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="calendly", integration=integration, **kwargs)
        self.base_url = "https://api.calendly.com"

    def list_event_invitees(
        self, uuid, status=None, sort=None, email=None, page_token=None, count=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of invitees for a specific scheduled event, identified by its UUID. The results can be filtered by invitee status or email, sorted by creation date, and the list size can be controlled using pagination parameters.

        Args:
            uuid (string): uuid
            status (string): Indicates if the invitee "canceled" or still "active" Example: 'active'.
            sort (string): Order results by the **created_at** field and direction specified: ascending ("asc") or descending ("desc") Example: 'created_at:asc'.
            email (string): Indicates if the results should be filtered by email address Example: '<email>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.

        Returns:
            dict[str, Any]: OK

        Tags:
            scheduled_events, {uuid}, invitees, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/scheduled_events/{uuid}/invitees"
        query_params = {
            k: v
            for k, v in [
                ("status", status),
                ("sort", sort),
                ("email", email),
                ("page_token", page_token),
                ("count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_scheduled_event(self, uuid) -> dict[str, Any]:
        """
        Retrieves the details for a specific scheduled event using its unique identifier (UUID). This targets a single event instance, differentiating it from `list_events` which fetches a collection of events and `get_event_type` which retrieves an event template.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            scheduled_events, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/scheduled_events/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_invitee(self, event_uuid, invitee_uuid) -> dict[str, Any]:
        """
        Fetches detailed information for a single invitee associated with a specific scheduled event. It uses both the event's UUID and the invitee's UUID to uniquely identify and retrieve the correct record, distinguishing it from `list_event_invitees` which returns a collection.

        Args:
            event_uuid (string): event_uuid
            invitee_uuid (string): invitee_uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            scheduled_events, {event_uuid}, invitees1, {invitee_uuid}
        """
        if event_uuid is None:
            raise ValueError("Missing required parameter 'event_uuid'")
        if invitee_uuid is None:
            raise ValueError("Missing required parameter 'invitee_uuid'")
        url = f"{self.base_url}/scheduled_events/{event_uuid}/invitees/{invitee_uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_scheduled_events(
        self,
        user=None,
        organization=None,
        invitee_email=None,
        status=None,
        sort=None,
        min_start_time=None,
        max_start_time=None,
        page_token=None,
        count=None,
        group=None,
    ) -> dict[str, Any]:
        """
        Fetches a list of scheduled events, offering extensive filtering by user, organization, invitee email, status, and time range. Supports pagination and sorting, providing a flexible method to query specific event data from the Calendly API.

        Args:
            user (string): Return events that are scheduled with the user associated with this URI Example: '<uri>'.
            organization (string): Return events that are scheduled with the organization associated with this URI Example: '<uri>'.
            invitee_email (string): Return events that are scheduled with the invitee associated with this email address Example: '<email>'.
            status (string): Whether the scheduled event is `active` or `canceled` Example: 'active'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values.
        Supported fields are: start_time.
        Sort direction is specified as: asc, desc. Example: '<string>'.
            min_start_time (string): Include events with start times after this time (sample time format: "2020-01-02T03:04:05.678123Z"). This time should use the UTC timezone. Example: '<string>'.
            max_start_time (string): Include events with start times prior to this time (sample time format: "2020-01-02T03:04:05.678123Z"). This time should use the UTC timezone. Example: '<string>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.
            group (string): Return events that are scheduled with the group associated with this URI Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            scheduled_events, important
        """
        url = f"{self.base_url}/scheduled_events"
        query_params = {
            k: v
            for k, v in [
                ("user", user),
                ("organization", organization),
                ("invitee_email", invitee_email),
                ("status", status),
                ("sort", sort),
                ("min_start_time", min_start_time),
                ("max_start_time", max_start_time),
                ("page_token", page_token),
                ("count", count),
                ("group", group),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_type(self, uuid) -> dict[str, Any]:
        """
        Retrieves the full details of a specific event type, such as its name, duration, and scheduling rules, by providing its unique identifier (UUID). It fetches a single resource, unlike list_user_sevent_types which retrieves a collection.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            event_types, {uuid}1
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/event_types/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_event_types(
        self,
        active=None,
        organization=None,
        user=None,
        user_availability_schedule=None,
        sort=None,
        admin_managed=None,
        page_token=None,
        count=None,
    ) -> dict[str, Any]:
        """
        Retrieves a collection of event types from the `/event_types` endpoint. Results can be filtered by user, organization, or status, and the list supports sorting and pagination for controlled data retrieval.

        Args:
            active (string): Return only active event types if true, only inactive if false, or all event types if this parameter is omitted. Example: '<boolean>'.
            organization (string): View available personal, team, and organization event types associated with the organization's URI. Example: '<uri>'.
            user (string): View available personal, team, and organization event types associated with the user's URI. Example: '<uri>'.
            user_availability_schedule (string): Used in conjunction with `user` parameter, returns a filtered list of Event Types that use the given primary availability schedule. Example: '<uri>'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values.Supported fields are: name, position, created_at, updated_at. Sort direction is specified as: asc, desc. Example: 'name:asc'.
            admin_managed (string): Return only admin managed event types if true, exclude admin managed event types if false, or include all event types if this parameter is omitted. Example: '<boolean>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.

        Returns:
            dict[str, Any]: OK

        Tags:
            event_types
        """
        url = f"{self.base_url}/event_types"
        query_params = {
            k: v
            for k, v in [
                ("active", active),
                ("organization", organization),
                ("user", user),
                ("user_availability_schedule", user_availability_schedule),
                ("sort", sort),
                ("admin_managed", admin_managed),
                ("page_token", page_token),
                ("count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user(self, uuid) -> dict[str, Any]:
        """
        Retrieves the details of a specific user identified by their unique identifier (UUID). This differs from `get_current_user`, which fetches the profile of the currently authenticated user.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            users, {uuid}12
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/users/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_current_user(self) -> dict[str, Any]:
        """
        Retrieves profile information for the currently authenticated user by querying the `/users/me` endpoint. This function requires no parameters, unlike `get_user` which fetches a specific user by their UUID.

        Returns:
            dict[str, Any]: OK

        Tags:
            users, me, important
        """
        url = f"{self.base_url}/users/me"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_organization_invitations(
        self, uuid, count=None, page_token=None, sort=None, email=None, status=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of invitations for a specific organization, identified by its UUID. It allows optional filtering by email and status (e.g., pending, accepted) and sorting. This function fetches a collection of invitations, unlike `get_organization_invitation` which retrieves a single one.

        Args:
            uuid (string): uuid
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            sort (string): Order results by the field name and direction specified (ascending or descending). Returns multiple sets of results in a comma-separated list. Example: 'created_at:asc'.
            email (string): Indicates if the results should be filtered by email address Example: '<email>'.
            status (string): Indicates if the results should be filtered by status ("pending", "accepted", or "declined") Example: 'accepted'.

        Returns:
            dict[str, Any]: OK

        Tags:
            organizations, {uuid}123, invitations
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organizations/{uuid}/invitations"
        query_params = {
            k: v
            for k, v in [
                ("count", count),
                ("page_token", page_token),
                ("sort", sort),
                ("email", email),
                ("status", status),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_organization_invitation(self, uuid, email=None) -> dict[str, Any]:
        """
        Invites a user via email to join a specific organization, identified by the organization's UUID. This function creates a new pending invitation, distinguishing it from functions that list, retrieve, or revoke existing invitations.

        Args:
            uuid (string): uuid
            email (string): email
                Example:
                ```json
                {
                  "email": "<email>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            organizations, {uuid}123, invitations
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "email": email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizations/{uuid}/invitations"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_invitation(self, org_uuid, uuid) -> dict[str, Any]:
        """
        Retrieves the details of a single, specific invitation within an organization. It requires both the organization's unique identifier (`org_uuid`) and the invitation's unique identifier (`uuid`) for the lookup.

        Args:
            org_uuid (string): org_uuid
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            organizations, {org_uuid}, invitations1, {uuid}1234
        """
        if org_uuid is None:
            raise ValueError("Missing required parameter 'org_uuid'")
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organizations/{org_uuid}/invitations/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def revoke_user_organization_invitation(self, org_uuid, uuid) -> Any:
        """
        Revokes a specific user's invitation to an organization, identified by the organization and invitation UUIDs. This action permanently deletes the pending invitation, preventing it from being accepted.

        Args:
            org_uuid (string): org_uuid
            uuid (string): uuid

        Returns:
            Any: No Content

        Tags:
            organizations, {org_uuid}, invitations1, {uuid}1234
        """
        if org_uuid is None:
            raise ValueError("Missing required parameter 'org_uuid'")
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organizations/{org_uuid}/invitations/{uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_membership(self, uuid) -> dict[str, Any]:
        """
        Fetches the details of a specific organization membership using its unique identifier (UUID). Unlike `list_organization_memberships`, this function retrieves a single membership record rather than a collection.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            organization_memberships, {uuid}12345
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organization_memberships/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_organization_membership(self, uuid) -> Any:
        """
        Deletes an organization membership by its unique UUID, effectively removing the associated user from the organization. This function is the destructive counterpart to `get_organization_membership` and acts on active members, not pending invitations.

        Args:
            uuid (string): uuid

        Returns:
            Any: No Content

        Tags:
            organization_memberships, {uuid}12345
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organization_memberships/{uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_organization_memberships(
        self, page_token=None, count=None, email=None, organization=None, user=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of organization memberships. The results can be filtered by user, organization, or email address to narrow down the search for specific members within one or more organizations.

        Args:
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.
            email (string): Indicates if the results should be filtered by email address Example: '<email>'.
            organization (string): Indicates if the results should be filtered by organization Example: '<uri>'.
            user (string): Indicates if the results should be filtered by user Example: '<uri>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            organization_memberships
        """
        url = f"{self.base_url}/organization_memberships"
        query_params = {
            k: v
            for k, v in [
                ("page_token", page_token),
                ("count", count),
                ("email", email),
                ("organization", organization),
                ("user", user),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_subscription(self, webhook_uuid) -> dict[str, Any]:
        """
        Fetches detailed information for a single webhook subscription using its unique identifier (UUID). Unlike `list_webhook_subscriptions`, which returns a collection, this function retrieves one specific subscription's configuration and status.

        Args:
            webhook_uuid (string): webhook_uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            webhook_subscriptions, {webhook_uuid}
        """
        if webhook_uuid is None:
            raise ValueError("Missing required parameter 'webhook_uuid'")
        url = f"{self.base_url}/webhook_subscriptions/{webhook_uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_webhook_subscription(self, webhook_uuid) -> Any:
        """
        Deletes a specific webhook subscription using its unique `webhook_uuid`. This function sends a DELETE request to the Calendly API to permanently remove the subscription, stopping all future event notifications. It raises an error if the deletion fails.

        Args:
            webhook_uuid (string): webhook_uuid

        Returns:
            Any: No Content

        Tags:
            webhook_subscriptions, {webhook_uuid}
        """
        if webhook_uuid is None:
            raise ValueError("Missing required parameter 'webhook_uuid'")
        url = f"{self.base_url}/webhook_subscriptions/{webhook_uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_webhook_subscriptions(
        self,
        organization=None,
        user=None,
        page_token=None,
        count=None,
        sort=None,
        scope=None,
    ) -> dict[str, Any]:
        """
        Retrieves a collection of webhook subscriptions for a given scope (organization or user). Supports filtering, sorting, and pagination to browse multiple subscriptions, unlike functions like `get_webhook_subscription` which fetches a single subscription by its unique ID.

        Args:
            organization (string): (Required) Indicates if the results should be filtered by organization Example: '<uri>'.
            user (string): Indicates if the results should be filtered by user. This parameter is only required if the `scope` parameter is set to `user`. Example: '<uri>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values.
        Supported fields are: created_at.
        Sort direction is specified as: asc, desc. Example: '<string>'.
            scope (string): (Required) Filter the list by organization or user Example: 'user'.

        Returns:
            dict[str, Any]: OK

        Tags:
            webhook_subscriptions
        """
        url = f"{self.base_url}/webhook_subscriptions"
        query_params = {
            k: v
            for k, v in [
                ("organization", organization),
                ("user", user),
                ("page_token", page_token),
                ("count", count),
                ("sort", sort),
                ("scope", scope),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_webhook_subscription(
        self,
        events=None,
        group=None,
        organization=None,
        scope=None,
        signing_key=None,
        url=None,
        user=None,
    ) -> dict[str, Any]:
        """
        Creates a Calendly webhook subscription for specified events. It requires a callback URL, the scope (e.g., organization, user), and the list of events to monitor, registering the webhook via a POST request to the API.

        Args:
            events (array): events Example: "['invitee.canceled', 'routing_form_submission.created']".
            group (string): group Example: '<uri>'.
            organization (string): organization Example: '<uri>'.
            scope (string): scope Example: 'organization'.
            signing_key (string): signing_key Example: '<string>'.
            url (string): url Example: '<uri>'.
            user (string): user
                Example:
                ```json
                {
                  "events": [
                    "invitee.canceled",
                    "routing_form_submission.created"
                  ],
                  "group": "<uri>",
                  "organization": "<uri>",
                  "scope": "organization",
                  "signing_key": "<string>",
                  "url": "<uri>",
                  "user": "<uri>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            webhook_subscriptions
        """
        request_body = {
            "events": events,
            "group": group,
            "organization": organization,
            "scope": scope,
            "signing_key": signing_key,
            "url": url,
            "user": user,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/webhook_subscriptions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_limited_use_scheduling_link(
        self, max_event_count=None, owner=None, owner_type=None
    ) -> dict[str, Any]:
        """
        Generates a unique, limited-use scheduling link for a specific owner, such as an event type. The link is valid for a specified maximum number of bookings, after which it expires.

        Args:
            max_event_count (number): max_event_count Example: '1'.
            owner (string): owner Example: '<uri>'.
            owner_type (string): owner_type
                Example:
                ```json
                {
                  "max_event_count": 1,
                  "owner": "<uri>",
                  "owner_type": "EventType"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            scheduling_links
        """
        request_body = {
            "max_event_count": max_event_count,
            "owner": owner,
            "owner_type": owner_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/scheduling_links"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def request_invitee_data_deletion(self, emails=None) -> dict[str, Any]:
        """
        Submits an asynchronous data deletion request for one or more invitees, identified by their email addresses, to comply with privacy regulations. This action permanently removes invitee information from the system.

        Args:
            emails (array): emails
                Example:
                ```json
                {
                  "emails": [
                    "<email>",
                    "<email>"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: Accepted

        Tags:
            data_compliance, deletion, invitees12
        """
        request_body = {
            "emails": emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/data_compliance/deletion/invitees"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def request_scheduled_event_data_deletion(
        self, end_time=None, start_time=None
    ) -> dict[str, Any]:
        """
        For data compliance, submits an asynchronous request to delete scheduled event data within a specified `start_time` and `end_time`. This targets events by time range, unlike `delete_invitee_data` which targets specific individuals.

        Args:
            end_time (string): end_time Example: '<dateTime>'.
            start_time (string): start_time
                Example:
                ```json
                {
                  "end_time": "<dateTime>",
                  "start_time": "<dateTime>"
                }
                ```

        Returns:
            dict[str, Any]: Accepted

        Tags:
            data_compliance, deletion, events
        """
        request_body = {
            "end_time": end_time,
            "start_time": start_time,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/data_compliance/deletion/events"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_invitee_no_show(self, uuid) -> dict[str, Any]:
        """
        Retrieves the details for a specific 'no-show' record associated with an invitee, identified by its unique ID (UUID). This function fetches a single record, unlike create_invitee_no_show which creates one.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            invitee_no_shows, {uuid}123456
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/invitee_no_shows/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def revoke_invitee_no_show(self, uuid) -> Any:
        """
        Deletes an invitee's 'no-show' record using its unique UUID. This operation revokes the no-show status previously assigned to an invitee, effectively undoing the action of `create_invitee_no_show`.

        Args:
            uuid (string): uuid

        Returns:
            Any: No Content

        Tags:
            invitee_no_shows, {uuid}123456
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/invitee_no_shows/{uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def mark_invitee_as_no_show(self, invitee=None) -> dict[str, Any]:
        """
        Marks a specific invitee as a 'no-show' by creating a no-show record. It requires the invitee's URI and sends a POST request to the `/invitee_no_shows` endpoint, returning the details of the newly created entry.

        Args:
            invitee (string): invitee
                Example:
                ```json
                {
                  "invitee": "<uri>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            invitee_no_shows
        """
        request_body = {
            "invitee": invitee,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/invitee_no_shows"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_group_by_id(self, uuid) -> dict[str, Any]:
        """
        Retrieves the details of a specific group by its unique identifier (UUID). Unlike `list_groups`, which returns multiple group records, this function fetches information for a single group.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            groups, {uuid}1234567
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/groups/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_groups(
        self, organization=None, page_token=None, count=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of groups associated with a specific organization. The result set can be controlled using pagination parameters for the page token and the number of items to return per page.

        Args:
            organization (string): (Required) Return groups that are associated with the organization associated with this URI Example: '<string>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.

        Returns:
            dict[str, Any]: OK

        Tags:
            groups
        """
        url = f"{self.base_url}/groups"
        query_params = {
            k: v
            for k, v in [
                ("organization", organization),
                ("page_token", page_token),
                ("count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_group_relationship(self, uuid) -> dict[str, Any]:
        """
        Retrieves the details of a specific group relationship, which connects an owner (like a user or invitation) to a group, by its unique identifier (UUID). This differs from `list_group_relationships` which fetches a list.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            group_relationships, {uuid}12345678
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/group_relationships/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_group_relationships(
        self, count=None, page_token=None, organization=None, owner=None, group=None
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of group relationships. The results can be filtered by organization, owner, or a specific group to refine the search and control the returned data set.

        Args:
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            organization (string): Indicates the results should be filtered by organization Example: '<uri>'.
            owner (string): Indicates the results should be filtered by owner <br>
        One Of: - Organization Membership URI - ` - Organization Invitation URI - ` Example: '<uri>'.
            group (string): Indicates the results should be filtered by group Example: '<uri>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            group_relationships
        """
        url = f"{self.base_url}/group_relationships"
        query_params = {
            k: v
            for k, v in [
                ("count", count),
                ("page_token", page_token),
                ("organization", organization),
                ("owner", owner),
                ("group", group),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_routing_form(self, uuid) -> dict[str, Any]:
        """
        Retrieves the details of a specific routing form using its unique identifier (UUID). This is distinct from `list_routing_forms`, which fetches a collection, and from functions that retrieve form submissions.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            routing_forms, {uuid}123456789
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/routing_forms/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_routing_forms(
        self, organization=None, count=None, page_token=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of routing forms for a specified organization. This function supports pagination using a page token, sorting by creation date, and limiting the number of results returned per request, distinguishing it from `get_routing_form` which fetches a single item.

        Args:
            organization (string): (Required) View organization routing forms associated with the organization's URI. Example: '<uri>'.
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values. Supported fields are: created_at. Sort direction is specified as: asc, desc. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            routing_forms
        """
        url = f"{self.base_url}/routing_forms"
        query_params = {
            k: v
            for k, v in [
                ("organization", organization),
                ("count", count),
                ("page_token", page_token),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_routing_form_submission(self, uuid) -> dict[str, Any]:
        """
        Fetches details for a single routing form submission using its unique identifier (UUID). It queries the `/routing_form_submissions/{uuid}` endpoint, distinct from `list_routing_form_submissions` which retrieves multiple submissions.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            routing_form_submissions, {uuid}12345678910
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/routing_form_submissions/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_routing_form_submissions(
        self, form=None, count=None, page_token=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of submissions associated with a specific routing form. The results can be sorted by creation date and navigated using count and page_token parameters.

        Args:
            form (string): (Required) View routing form submissions associated with the routing form's URI. Example: '<uri>'.
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values. Supported fields are: created_at. Sort direction is specified as: asc, desc. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            routing_form_submissions
        """
        url = f"{self.base_url}/routing_form_submissions"
        query_params = {
            k: v
            for k, v in [
                ("form", form),
                ("count", count),
                ("page_token", page_token),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_event_type_available_times(
        self, event_type=None, start_time=None, end_time=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of concrete, bookable time slots for a specific event type within a defined start and end time. It provides specific availability, distinct from functions that list a user's general busy times or configured schedules.

        Args:
            event_type (string): (Required) The uri associated with the event type Example: '<uri>'.
            start_time (string): (Required) Start time of the requested availability range. Example: '<string>'.
            end_time (string): (Required) End time of the requested availability range. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            event_type_available_times
        """
        url = f"{self.base_url}/event_type_available_times"
        query_params = {
            k: v
            for k, v in [
                ("event_type", event_type),
                ("start_time", start_time),
                ("end_time", end_time),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_activity_log_entries(
        self,
        organization=None,
        search_term=None,
        actor=None,
        sort=None,
        min_occurred_at=None,
        max_occurred_at=None,
        page_token=None,
        count=None,
        namespace=None,
        action=None,
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of activity log entries for an organization. Allows advanced filtering by actor, time range, search term, namespace, and action, with support for custom sorting and pagination to refine the results.

        Args:
            organization (string): (Required) Return activity log entries from the organization associated with this URI Example: '<uri>'.
            search_term (string): Filters entries based on the search term. Supported operators: - `|` - to allow filtering by one term or another. Example: `this | that` - `+` - to allow filtering by one term and another. Example: `this + that` - `"` - to allow filtering by an exact search term. Example: `"email@website.com"` - `-` - to omit specific terms from results. Example: `Added -User` - `()` - to allow specifying precedence during a search. Example: `(this + that) OR (person + place)` - `*` - to allow prefix searching. Example `*@other-website.com` Example: '<string>'.
            actor (string): Return entries from the user(s) associated with the provided URIs Example: '<uri>,<uri>'.
            sort (string): Order results by the specified field and direction. List of {field}:{direction} values. Example: 'occurred_at:desc'.
            min_occurred_at (string): Include entries that occurred after this time (sample time format: "2020-01-02T03:04:05.678Z"). This time should use the UTC timezone. Example: '<dateTime>'.
            max_occurred_at (string): Include entries that occurred prior to this time (sample time format: "2020-01-02T03:04:05.678Z"). This time should use the UTC timezone. Example: '<dateTime>'.
            page_token (string): The token to pass to get the next portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.
            namespace (string): The categories of the entries Example: '<string>,<string>'.
            action (string): The action(s) associated with the entries Example: '<string>,<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            activity_log_entries
        """
        url = f"{self.base_url}/activity_log_entries"
        query_params = {
            k: v
            for k, v in [
                ("organization", organization),
                ("search_term", search_term),
                ("actor", actor),
                ("sort", sort),
                ("min_occurred_at", min_occurred_at),
                ("max_occurred_at", max_occurred_at),
                ("page_token", page_token),
                ("count", count),
                ("namespace", namespace),
                ("action", action),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_shareable_link(
        self,
        availability_rule=None,
        duration=None,
        end_date=None,
        event_type=None,
        hide_location=None,
        location_configurations=None,
        max_booking_time=None,
        name=None,
        period_type=None,
        start_date=None,
    ) -> dict[str, Any]:
        """
        Creates a custom, shareable scheduling link by defining properties like availability rules, event duration, and location. This generates a unique booking link tailored to specific settings, differing from standard event types or single-use links.

        Args:
            availability_rule (object): availability_rule
            duration (string): duration Example: '<integer>'.
            end_date (string): end_date Example: '<date>'.
            event_type (string): event_type Example: '<uri>'.
            hide_location (string): hide_location Example: '<boolean>'.
            location_configurations (array): location_configurations Example: "[{'additional_info': '<string>', 'kind': 'ask_invitee', 'location': '<string>', 'phone_number': '<string>', 'position': '<integer>'}, {'additional_info': '<string>', 'kind': 'microsoft_teams_conference', 'location': '<string>', 'phone_number': '<string>', 'position': '<integer>'}]".
            max_booking_time (string): max_booking_time Example: '<integer>'.
            name (string): name Example: '<string>'.
            period_type (string): period_type Example: 'fixed'.
            start_date (string): start_date
                Example:
                ```json
                {
                  "availability_rule": {
                    "rules": [
                      {
                        "date": "<date>",
                        "intervals": [
                          {
                            "from": "87:41",
                            "to": "67:37"
                          },
                          {
                            "from": "37:88",
                            "to": "18:71"
                          }
                        ],
                        "type": "date",
                        "wday": "wednesday"
                      },
                      {
                        "date": "<date>",
                        "intervals": [
                          {
                            "from": "56:49",
                            "to": "38:81"
                          },
                          {
                            "from": "65:67",
                            "to": "87:67"
                          }
                        ],
                        "type": "wday",
                        "wday": "tuesday"
                      }
                    ],
                    "timezone": "<string>"
                  },
                  "duration": "<integer>",
                  "end_date": "<date>",
                  "event_type": "<uri>",
                  "hide_location": "<boolean>",
                  "location_configurations": [
                    {
                      "additional_info": "<string>",
                      "kind": "ask_invitee",
                      "location": "<string>",
                      "phone_number": "<string>",
                      "position": "<integer>"
                    },
                    {
                      "additional_info": "<string>",
                      "kind": "microsoft_teams_conference",
                      "location": "<string>",
                      "phone_number": "<string>",
                      "position": "<integer>"
                    }
                  ],
                  "max_booking_time": "<integer>",
                  "name": "<string>",
                  "period_type": "fixed",
                  "start_date": "<date>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            shares
        """
        request_body = {
            "availability_rule": availability_rule,
            "duration": duration,
            "end_date": end_date,
            "event_type": event_type,
            "hide_location": hide_location,
            "location_configurations": location_configurations,
            "max_booking_time": max_booking_time,
            "name": name,
            "period_type": period_type,
            "start_date": start_date,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/shares"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_busy_times(
        self, user=None, start_time=None, end_time=None
    ) -> dict[str, Any]:
        """
        Fetches a user's busy time intervals within a specified date range, including all scheduled events. This helps determine actual unavailability, differing from `list_user_availability_schedules` which retrieves a user's general working hours.

        Args:
            user (string): (Required) The uri associated with the user Example: '<uri>'.
            start_time (string): (Required) Start time of the requested availability range Example: '<string>'.
            end_time (string): (Required) End time of the requested availability range Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            user_busy_times
        """
        url = f"{self.base_url}/user_busy_times"
        query_params = {
            k: v
            for k, v in [
                ("user", user),
                ("start_time", start_time),
                ("end_time", end_time),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user_availability_schedule(self, uuid) -> dict[str, Any]:
        """
        Retrieves a specific user availability schedule by its unique identifier (UUID). It fetches a single schedule resource, unlike `list_user_availability_schedules`, which returns all schedules associated with a user.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            user_availability_schedules, {uuid}1234567891011
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/user_availability_schedules/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_schedules_for_user(self, user=None) -> dict[str, Any]:
        """
        Retrieves all availability schedules for a specified user via their URI. Unlike `get_user_availability_schedule`, which fetches a single schedule by its UUID, this function returns a collection of all schedules defining a user's availability intervals.

        Args:
            user (string): (Required) A URI reference to a user Example: '<uri>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            user_availability_schedules
        """
        url = f"{self.base_url}/user_availability_schedules"
        query_params = {k: v for k, v in [("user", user)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_event_type_memberships(
        self, event_type=None, count=None, page_token=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of all user memberships (hosts) for a specific event type. It requires the event type's URI and allows for navigating through results using `count` and `page_token` parameters, returning the membership objects.

        Args:
            event_type (string): (Required) The uri associated with the event type Example: '<uri>'.
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            event_type_memberships
        """
        url = f"{self.base_url}/event_type_memberships"
        query_params = {
            k: v
            for k, v in [
                ("event_type", event_type),
                ("count", count),
                ("page_token", page_token),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_one_off_event_type(
        self,
        co_hosts=None,
        date_setting=None,
        duration=None,
        host=None,
        location=None,
        name=None,
        timezone=None,
    ) -> dict[str, Any]:
        """
        Creates a unique, non-reusable event type for a single, ad-hoc meeting. It defines event details like host, co-hosts, duration, and location, distinguishing it from standard, reusable event types.

        Args:
            co_hosts (array): co_hosts Example: "['<uri>', '<uri>']".
            date_setting (object): date_setting
            duration (string): duration Example: '<number>'.
            host (string): host Example: '<uri>'.
            location (object): location
            name (string): name Example: '<string>'.
            timezone (string): timezone
                Example:
                ```json
                {
                  "co_hosts": [
                    "<uri>",
                    "<uri>"
                  ],
                  "date_setting": {
                    "value": "reference ./models/date_setting/DateRange.yaml not found in the OpenAPI spec"
                  },
                  "duration": "<number>",
                  "host": "<uri>",
                  "location": {
                    "value": "reference ./models/adhoc-locations/CustomLocation.yaml not found in the OpenAPI spec"
                  },
                  "name": "<string>",
                  "timezone": "<string>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            one_off_event_types
        """
        request_body = {
            "co_hosts": co_hosts,
            "date_setting": date_setting,
            "duration": duration,
            "host": host,
            "location": location,
            "name": name,
            "timezone": timezone,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/one_off_event_types"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sample_webhook_data(
        self, event=None, organization=None, user=None, scope=None
    ) -> dict[str, Any]:
        """
        Fetches a sample webhook data payload for a specified event, organization, and scope. This helps developers preview the JSON structure for a webhook notification, facilitating testing and integration without needing to trigger a live event.

        Args:
            event (string): (Required) Example: 'invitee.created'.
            organization (string): (Required) Example: '<uri>'.
            user (string): Specifies the user identifier or name for filtering or retrieving specific data in the response. Example: '<uri>'.
            scope (string): (Required) Example: 'user'.

        Returns:
            dict[str, Any]: OK

        Tags:
            sample_webhook_data
        """
        url = f"{self.base_url}/sample_webhook_data"
        query_params = {
            k: v
            for k, v in [
                ("event", event),
                ("organization", organization),
                ("user", user),
                ("scope", scope),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.list_event_invitees,
            self.get_scheduled_event,
            self.get_event_invitee,
            self.list_scheduled_events,
            self.get_event_type,
            self.list_event_types,
            self.get_user,
            self.get_current_user,
            self.list_organization_invitations,
            self.create_organization_invitation,
            self.get_organization_invitation,
            self.revoke_user_organization_invitation,
            self.get_organization_membership,
            self.delete_organization_membership,
            self.list_organization_memberships,
            self.get_webhook_subscription,
            self.delete_webhook_subscription,
            self.list_webhook_subscriptions,
            self.create_webhook_subscription,
            self.create_limited_use_scheduling_link,
            self.request_invitee_data_deletion,
            self.request_scheduled_event_data_deletion,
            self.get_invitee_no_show,
            self.revoke_invitee_no_show,
            self.mark_invitee_as_no_show,
            self.get_group_by_id,
            self.list_groups,
            self.get_group_relationship,
            self.list_group_relationships,
            self.get_routing_form,
            self.list_routing_forms,
            self.get_routing_form_submission,
            self.get_routing_form_submissions,
            self.list_event_type_available_times,
            self.list_activity_log_entries,
            self.create_shareable_link,
            self.list_user_busy_times,
            self.get_user_availability_schedule,
            self.list_schedules_for_user,
            self.list_event_type_memberships,
            self.create_one_off_event_type,
            self.get_sample_webhook_data,
        ]
