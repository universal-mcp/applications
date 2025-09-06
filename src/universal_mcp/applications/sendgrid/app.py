from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class SendgridApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="sendgrid", integration=integration, **kwargs)
        self.base_url = "https://api.sendgrid.com"

    def list_access_activity(self, limit=None) -> dict[str, Any]:
        """
        Retrieves activity settings using the specified limit, allowing for the optional specification of the user on whose behalf the request is made.

        Args:
            limit (integer): Specifies the maximum number of activity records to be returned in a single response page, with a default value of 20[3][1].

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Access Management, important
        """
        url = f"{self.base_url}/v3/access_settings/activity"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_allowed_ips(self, ids=None) -> dict[str, Any]:
        """
        Removes a user or IP address from the access whitelist for a resource and returns a 204 No Content response upon success.

        Args:
            ids (array): An array of the IDs of the IP address that you want to remove from your allow list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Access Management
        """
        request_body = {
            "ids": ids,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/access_settings/whitelist"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_allowed_ip(self) -> dict[str, Any]:
        """
        Retrieves the current list of whitelisted IP addresses for access settings.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Access Management
        """
        url = f"{self.base_url}/v3/access_settings/whitelist"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_ip_to_allow_list(self, ips=None) -> dict[str, Any]:
        """
        Adds IP addresses to a whitelist using the provided JSON payload in a POST request to the "/v3/access_settings/whitelist" endpoint.

        Args:
            ips (array): An array containing the IP(s) you want to allow.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Access Management
        """
        request_body = {
            "ips": ips,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/access_settings/whitelist"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_allowed_ip(self, rule_id) -> dict[str, Any]:
        """
        Deletes the specified whitelist access rule identified by rule_id and returns no content upon success.

        Args:
            rule_id (string): rule_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Access Management
        """
        if rule_id is None:
            raise ValueError("Missing required parameter 'rule_id'")
        url = f"{self.base_url}/v3/access_settings/whitelist/{rule_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_allowed_ip(self, rule_id) -> dict[str, Any]:
        """
        Retrieves the details of a specific whitelist rule by its identifier using the GET method.

        Args:
            rule_id (string): rule_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Access Management
        """
        if rule_id is None:
            raise ValueError("Missing required parameter 'rule_id'")
        url = f"{self.base_url}/v3/access_settings/whitelist/{rule_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_alert(self) -> list[Any]:
        """
        Retrieves a list of alerts using the GitHub API, returning a successful response with a status code of 200.

        Returns:
            list[Any]: API response data.

        Tags:
            Alerts, important
        """
        url = f"{self.base_url}/v3/alerts"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_alert(
        self, email_to=None, frequency=None, percentage=None, type=None
    ) -> dict[str, Any]:
        """
        Creates a new Dependabot alert for a repository using the GitHub REST API and returns a status indicating success or failure.

        Args:
            email_to (string): The email address the alert will be sent to.
        Example: test@example.com
            frequency (string): Required for stats_notification. How frequently the alert will be sent.
        Example: daily
            percentage (integer): Required for usage_limit. When this usage threshold is reached, the alert will be sent.
        Example: 90
            type (string): type

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        request_body = {
            "email_to": email_to,
            "frequency": frequency,
            "percentage": percentage,
            "type": type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/alerts"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_alert(self, alert_id) -> Any:
        """
        Deletes a specified alert by its ID using the GitHub API and returns a status code indicating success.

        Args:
            alert_id (string): alert_id

        Returns:
            Any: API response data.

        Tags:
            Alerts
        """
        if alert_id is None:
            raise ValueError("Missing required parameter 'alert_id'")
        url = f"{self.base_url}/v3/alerts/{alert_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_alert(self, alert_id) -> dict[str, Any]:
        """
        Retrieves a specific alert by its unique identifier from the API, returning the alert details in the response.

        Args:
            alert_id (string): alert_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if alert_id is None:
            raise ValueError("Missing required parameter 'alert_id'")
        url = f"{self.base_url}/v3/alerts/{alert_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_alert(
        self, alert_id, email_to=None, frequency=None, percentage=None
    ) -> dict[str, Any]:
        """
        Updates a specified Dependabot alert using the GitHub API and returns a status message.

        Args:
            alert_id (string): alert_id
            email_to (string): The new email address you want your alert to be sent to.
        Example: test@example.com
            frequency (string): The new frequency at which to send the stats_notification alert.
        Example: monthly
            percentage (integer): The new percentage threshold at which the usage_limit alert will be sent.
        Example: 90

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if alert_id is None:
            raise ValueError("Missing required parameter 'alert_id'")
        request_body = {
            "email_to": email_to,
            "frequency": frequency,
            "percentage": percentage,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/alerts/{alert_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_api_key(self, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of API keys using the "GET" method at the "/v3/api_keys" path, allowing for optional filtering by a specified limit and supporting authentication on behalf of another user.

        Args:
            limit (integer): Specifies the maximum number of API keys to return in the response.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            API Keys
        """
        url = f"{self.base_url}/v3/api_keys"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_api_key(self, name=None, scopes=None) -> dict[str, Any]:
        """
        Creates and returns a new API key for authenticating requests to the API, with optional specification of the user or context on behalf of whom the key is generated.

        Args:
            name (string): The name you will use to describe this API Key.
            scopes (array): The individual permissions that you are giving to this API Key.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            API Keys
        """
        request_body = {
            "name": name,
            "scopes": scopes,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/api_keys"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_api_key(self, api_key_id) -> Any:
        """
        Deletes an API key identified by the `api_key_id` parameter, returning a successful response without content if the operation is completed.

        Args:
            api_key_id (string): api_key_id

        Returns:
            Any: API response data.

        Tags:
            API Keys
        """
        if api_key_id is None:
            raise ValueError("Missing required parameter 'api_key_id'")
        url = f"{self.base_url}/v3/api_keys/{api_key_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_api_key(self, api_key_id) -> dict[str, Any]:
        """
        Retrieves details for a specific API key identified by `{api_key_id}` using the `GET` method.

        Args:
            api_key_id (string): api_key_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            API Keys
        """
        if api_key_id is None:
            raise ValueError("Missing required parameter 'api_key_id'")
        url = f"{self.base_url}/v3/api_keys/{api_key_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_api_key_name(self, api_key_id, name=None) -> dict[str, Any]:
        """
        Updates properties of an existing API key identified by `api_key_id` using patch operations to modify its configuration.

        Args:
            api_key_id (string): api_key_id
            name (string): The new name of the API Key.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            API Keys
        """
        if api_key_id is None:
            raise ValueError("Missing required parameter 'api_key_id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/api_keys/{api_key_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_api_key(self, api_key_id, name=None, scopes=None) -> dict[str, Any]:
        """
        Updates an API key identified by `{api_key_id}` using a JSON body, with optional support for operations on behalf of another entity.

        Args:
            api_key_id (string): api_key_id
            name (string): name
            scopes (array): scopes

        Returns:
            dict[str, Any]: API response data.

        Tags:
            API Keys
        """
        if api_key_id is None:
            raise ValueError("Missing required parameter 'api_key_id'")
        request_body = {
            "name": name,
            "scopes": scopes,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/api_keys/{api_key_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_asm_group(self, id=None) -> list[Any]:
        """
        Retrieves a list of all suppression groups associated with the specified account, optionally filtered by group ID, using the "GET" method at the "/v3/asm/groups" path.

        Args:
            id (integer): Specifies the unique identifier for the group you want to retrieve.

        Returns:
            list[Any]: API response data.

        Tags:
            Unsubscribe Groups
        """
        url = f"{self.base_url}/v3/asm/groups"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creat_asm_group(
        self, description=None, is_default=None, name=None
    ) -> dict[str, Any]:
        """
        Creates a new suppression group for an account, allowing you to manage unsubscribe behavior, using the SendGrid API and returning a status message.

        Args:
            description (string): A brief description of your suppression group. Required when creating a group.
            is_default (boolean): Indicates if you would like this to be your default suppression group.
            name (string): The name of your suppression group. Required when creating a group.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Unsubscribe Groups
        """
        request_body = {
            "description": description,
            "is_default": is_default,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/asm/groups"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_asm_group(self, group_id) -> dict[str, Any]:
        """
        Deletes an Active Directory group specified by its ID using the GitHub API and returns a successful response if the operation is completed without content.

        Args:
            group_id (string): group_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Unsubscribe Groups
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        url = f"{self.base_url}/v3/asm/groups/{group_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_asm_group(self, group_id) -> dict[str, Any]:
        """
        Retrieves a specific suppression group associated with a user using the Sendgrid API, returning its details.

        Args:
            group_id (string): group_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Unsubscribe Groups
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        url = f"{self.base_url}/v3/asm/groups/{group_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_asm_group(
        self, group_id, description=None, is_default=None, name=None
    ) -> dict[str, Any]:
        """
        Updates the settings or details of an ASM group identified by group_id using partial modifications via a PATCH request.

        Args:
            group_id (string): group_id
            description (string): A brief description of your suppression group. Required when creating a group.
            is_default (boolean): Indicates if you would like this to be your default suppression group.
            name (string): The name of your suppression group. Required when creating a group.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Unsubscribe Groups
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        request_body = {
            "description": description,
            "is_default": is_default,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/asm/groups/{group_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_suppression_from_asm_group(self, group_id) -> list[Any]:
        """
        Retrieves a list of email addresses that have been suppressed (unsubscribed) from a specific suppression group in SendGrid.

        Args:
            group_id (string): group_id

        Returns:
            list[Any]: API response data.

        Tags:
            Suppressions
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        url = f"{self.base_url}/v3/asm/groups/{group_id}/suppressions"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_suppression_to_asm_group(
        self, group_id, recipient_emails=None
    ) -> dict[str, Any]:
        """
        Adds one or more email addresses to the suppression list for a specified unsubscribe group, preventing future emails from being sent to those addresses under that group.

        Args:
            group_id (string): group_id
            recipient_emails (array): The array of email addresses to add or find.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Suppressions
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        request_body = {
            "recipient_emails": recipient_emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/asm/groups/{group_id}/suppressions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_suppression_from_asm_group(
        self, group_id, recipient_emails=None
    ) -> list[Any]:
        """
        Searches a suppression group for multiple suppressions using a list of email addresses and a group ID, returning matching suppressions.

        Args:
            group_id (string): group_id
            recipient_emails (array): The array of email addresses to add or find.

        Returns:
            list[Any]: API response data.

        Tags:
            Suppressions
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        request_body = {
            "recipient_emails": recipient_emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/asm/groups/{group_id}/suppressions/search"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_suppression_from_asm_group(self, group_id, email) -> Any:
        """
        Deletes an email address from a specific suppression group, removing it from that group's suppression list.

        Args:
            group_id (string): group_id
            email (string): email

        Returns:
            Any: API response data.

        Tags:
            Suppressions
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/asm/groups/{group_id}/suppressions/{email}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_asm_suppression(self) -> list[Any]:
        """
        Retrieves a list of suppressions from an ASM group using the SendGrid API.

        Returns:
            list[Any]: API response data.

        Tags:
            Suppressions
        """
        url = f"{self.base_url}/v3/asm/suppressions"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_global_suppression(self, recipient_emails=None) -> dict[str, Any]:
        """
        Adds one or more recipient email addresses to the global suppressions group, preventing them from receiving any emails from your account.

        Args:
            recipient_emails (array): The array of email addresses to add or find.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Global Suppressions
        """
        request_body = {
            "recipient_emails": recipient_emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/asm/suppressions/global"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_global_suppression(self, email) -> dict[str, Any]:
        """
        Removes the specified email address from the global suppression (global unsubscribe) list and returns no content upon successful deletion[1][3][4].

        Args:
            email (string): email

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Global Suppressions
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/asm/suppressions/global/{email}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_global_suppression(self, email) -> dict[str, Any]:
        """
        Retrieves information about a specific email address in the global suppression group using the SendGrid API.

        Args:
            email (string): email

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Global Suppressions
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/asm/suppressions/global/{email}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_asm_suppression(self, email) -> dict[str, Any]:
        """
        Retrieves a list of suppression groups from which a specified email address has been unsubscribed.

        Args:
            email (string): email

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Suppressions
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/asm/suppressions/{email}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_browser_stat(
        self,
        start_date,
        browsers=None,
        limit=None,
        offset=None,
        aggregated_by=None,
        end_date=None,
    ) -> list[Any]:
        """
        Retrieves statistical data for specified browsers, allowing filtering and pagination by date, browser name, and other query parameters.

        Args:
            start_date (string): The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.
            browsers (string): Specifies one or more browser names to filter statistics by, using a comma-separated string (e.g., "chrome,firefox,safari").
            limit (integer): The number of results to return.
            offset (integer): The point in the list to begin retrieving results.
            aggregated_by (string): How to group the statistics. Must be either "day", "week", or "month".
            end_date (string): The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

        Returns:
            list[Any]: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/browsers/stats"
        query_params = {
            k: v
            for k, v in [
                ("browsers", browsers),
                ("limit", limit),
                ("offset", offset),
                ("aggregated_by", aggregated_by),
                ("start_date", start_date),
                ("end_date", end_date),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_campaign(self, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves a list of campaigns with optional pagination and filtering by limit and offset, allowing operations on behalf of another entity.

        Args:
            limit (integer): Specifies the maximum number of campaigns to return in the response (defaults to 10).
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API, important
        """
        url = f"{self.base_url}/v3/campaigns"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign(
        self,
        categories=None,
        custom_unsubscribe_url=None,
        editor=None,
        html_content=None,
        ip_pool=None,
        list_ids=None,
        plain_content=None,
        segment_ids=None,
        sender_id=None,
        subject=None,
        suppression_group_id=None,
        title=None,
    ) -> dict[str, Any]:
        """
        Creates a new campaign resource using the provided JSON payload and returns a status code upon success or failure.

        Args:
            categories (array): The categories you would like associated to this campaign.
            custom_unsubscribe_url (string): This is the url of the custom unsubscribe page that you provide for customers to unsubscribe from your suppression groups.
            editor (string): editor
            html_content (string): The HTML of your marketing email.
            ip_pool (string): The pool of IPs that you would like to send this email from.
            list_ids (array): The IDs of the lists you are sending this campaign to. You can have both segment IDs and list IDs
            plain_content (string): The plain text content of your emails.
            segment_ids (array): The segment IDs that you are sending this list to. You can have both segment IDs and list IDs. Segments are limited to 10 segment IDs.
            sender_id (integer): The ID of the "sender" identity that you have created. Your recipients will see this as the "from" on your marketing emails.
            subject (string): The subject of your campaign that your recipients will see.
            suppression_group_id (integer): The suppression group that this marketing email belongs to, allowing recipients to opt-out of emails of this type.
            title (string): The display title of your campaign. This will be viewable by you in the Marketing Campaigns UI.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API
        """
        request_body = {
            "categories": categories,
            "custom_unsubscribe_url": custom_unsubscribe_url,
            "editor": editor,
            "html_content": html_content,
            "ip_pool": ip_pool,
            "list_ids": list_ids,
            "plain_content": plain_content,
            "segment_ids": segment_ids,
            "sender_id": sender_id,
            "subject": subject,
            "suppression_group_id": suppression_group_id,
            "title": title,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/campaigns"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_campaign(self, campaign_id) -> Any:
        """
        Deletes the specified campaign identified by campaign_id and returns a 204 No Content status on successful deletion.

        Args:
            campaign_id (string): campaign_id

        Returns:
            Any: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        url = f"{self.base_url}/v3/campaigns/{campaign_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign(self, campaign_id) -> dict[str, Any]:
        """
        Retrieves details for a specific campaign identified by its ID using the GET method.

        Args:
            campaign_id (string): campaign_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        url = f"{self.base_url}/v3/campaigns/{campaign_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_campaign(
        self,
        campaign_id,
        categories=None,
        html_content=None,
        plain_content=None,
        subject=None,
        title=None,
    ) -> dict[str, Any]:
        """
        Modifies a specific campaign by updating selected fields identified by the `{campaign_id}` using JSON data in the request body, returning a status response.

        Args:
            campaign_id (string): campaign_id
            categories (array): The categories you want to tag on this campaign.
            html_content (string): The HTML content of this campaign.
            plain_content (string): The plain content of this campaign.
            subject (string): The subject line for your campaign.
            title (string): The title of the campaign.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        request_body = {
            "categories": categories,
            "html_content": html_content,
            "plain_content": plain_content,
            "subject": subject,
            "title": title,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/campaigns/{campaign_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def un_schedule_campaign(self, campaign_id) -> Any:
        """
        Deletes the scheduled delivery of a campaign, returning a 204 (No Content) response if successful.

        Args:
            campaign_id (string): campaign_id

        Returns:
            Any: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        url = f"{self.base_url}/v3/campaigns/{campaign_id}/schedules"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_scheduled_campaign(self, campaign_id) -> dict[str, Any]:
        """
        Retrieves schedule details for a specified campaign using the "GET" method, optionally executed on behalf of another entity.

        Args:
            campaign_id (string): campaign_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        url = f"{self.base_url}/v3/campaigns/{campaign_id}/schedules"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_scheduled_campaign(self, campaign_id, send_at=None) -> dict[str, Any]:
        """
        Modifies the schedule of a campaign with the specified ID using a PATCH request, allowing partial updates to the schedule details.

        Args:
            campaign_id (string): campaign_id
            send_at (integer): send_at

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        request_body = {
            "send_at": send_at,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/campaigns/{campaign_id}/schedules"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_campaign(self, campaign_id, send_at=None) -> dict[str, Any]:
        """
        Creates a new schedule for a specified campaign using the POST method, accepting JSON-formatted data and returning a "201 Created" response upon successful creation.

        Args:
            campaign_id (string): campaign_id
            send_at (integer): The unix timestamp for the date and time you would like your campaign to be sent out.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        request_body = {
            "send_at": send_at,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/campaigns/{campaign_id}/schedules"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_campaign(self, campaign_id) -> dict[str, Any]:
        """
        Initiates a currently scheduled campaign using the provided campaign ID and returns a status message if successful.

        Args:
            campaign_id (string): campaign_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        url = f"{self.base_url}/v3/campaigns/{campaign_id}/schedules/now"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_test_campaign(self, campaign_id, to=None) -> dict[str, Any]:
        """
        Tests the schedule configuration for a specific campaign using the POST method and returns a status code, with the campaign identified by the provided campaign ID.

        Args:
            campaign_id (string): campaign_id
            to (string): The email address that should receive the test campaign.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Campaigns API
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'")
        request_body = {
            "to": to,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/campaigns/{campaign_id}/schedules/test"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_category_stat(
        self, start_date, categories, end_date=None, aggregated_by=None
    ) -> list[Any]:
        """
        Retrieves statistical data for specified categories within a date range, optionally aggregated by a given parameter.

        Args:
            start_date (string): **Start Date**: Required string parameter specifying the start date for retrieving category statistics, formatted as a date string.
            categories (string): Specifies one or more comma-separated category names for which statistics should be retrieved.
            end_date (string): The end_date query parameter specifies the optional ending date to filter category statistics up to that date.
            aggregated_by (string): Optionally specifies the field by which to aggregate statistics for the categories stats query, allowing for grouped results based on the specified field.

        Returns:
            list[Any]: API response data.

        Tags:
            Categories
        """
        url = f"{self.base_url}/v3/categories/stats"
        query_params = {
            k: v
            for k, v in [
                ("start_date", start_date),
                ("end_date", end_date),
                ("categories", categories),
                ("aggregated_by", aggregated_by),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_category_stat_sum(
        self,
        start_date,
        sort_by_metric=None,
        sort_by_direction=None,
        end_date=None,
        limit=None,
        offset=None,
        aggregated_by=None,
    ) -> dict[str, Any]:
        """
        Retrieves summary statistics for categories using the "GET" method, allowing filtering by date range, sorting, and aggregation options.

        Args:
            start_date (string): The start date of the period for which category statistics are retrieved, specified in string format, and required for the operation.
            sort_by_metric (string): Specifies the metric (default: "delivered") by which the sum statistics for categories will be sorted; optional parameter for the GET operation.
            sort_by_direction (string): Specifies the direction to sort results, with 'desc' as the default, allowing options for ascending or descending order.
            end_date (string): The end date of the time range for which category statistics should be calculated (inclusive), formatted as a string. If omitted, defaults to the current date or a system-defined value.
            limit (integer): Optional integer parameter to specify the maximum number of results to return, defaulting to 5.
            offset (integer): Determines the starting point for the data retrieval by excluding the first N items from the response, where N is the offset value.
            aggregated_by (string): Specifies the field or attribute by which the category statistics should be aggregated, such as by date, category group, or another relevant dimension.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Categories
        """
        url = f"{self.base_url}/v3/categories/stats/sums"
        query_params = {
            k: v
            for k, v in [
                ("sort_by_metric", sort_by_metric),
                ("sort_by_direction", sort_by_direction),
                ("start_date", start_date),
                ("end_date", end_date),
                ("limit", limit),
                ("offset", offset),
                ("aggregated_by", aggregated_by),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_client_stat(
        self, start_date, end_date=None, aggregated_by=None
    ) -> list[Any]:
        """
        Retrieves client statistics for a specified period, allowing aggregation options, using the "GET" method at the "/v3/clients/stats" endpoint.

        Args:
            start_date (string): The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.
            end_date (string): The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.
            aggregated_by (string): How to group the statistics. Must be either "day", "week", or "month".

        Returns:
            list[Any]: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/clients/stats"
        query_params = {
            k: v
            for k, v in [
                ("start_date", start_date),
                ("end_date", end_date),
                ("aggregated_by", aggregated_by),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_client_stat(
        self, client_type, start_date, end_date=None, aggregated_by=None
    ) -> list[Any]:
        """
        Get statistical data for a specified client type with optional filtering by date range and aggregation parameters.

        Args:
            client_type (string): client_type
            start_date (string): The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.
            end_date (string): The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.
            aggregated_by (string): How to group the statistics. Must be either "day", "week", or "month".

        Returns:
            list[Any]: API response data.

        Tags:
            Stats
        """
        if client_type is None:
            raise ValueError("Missing required parameter 'client_type'")
        url = f"{self.base_url}/v3/clients/{client_type}/stats"
        query_params = {
            k: v
            for k, v in [
                ("start_date", start_date),
                ("end_date", end_date),
                ("aggregated_by", aggregated_by),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_custom_field(self) -> dict[str, Any]:
        """
        Retrieves a list of custom fields from a contact database using the "GET" method, allowing for on-behalf-of parameters to specify the user making the request.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Custom Fields
        """
        url = f"{self.base_url}/v3/contactdb/custom_fields"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_custom_field(self, name=None, type=None) -> dict[str, Any]:
        """
        Creates a new custom field in the contact database using a POST request with a JSON body.

        Args:
            name (string): name
            type (string): type

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Custom Fields
        """
        request_body = {
            "name": name,
            "type": type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/contactdb/custom_fields"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_custom_field(self, custom_field_id) -> dict[str, Any]:
        """
        Removes the specified custom field from the contact database, returning appropriate status codes based on success or failure.

        Args:
            custom_field_id (string): custom_field_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Custom Fields
        """
        if custom_field_id is None:
            raise ValueError("Missing required parameter 'custom_field_id'")
        url = f"{self.base_url}/v3/contactdb/custom_fields/{custom_field_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_custom_field(self, custom_field_id) -> dict[str, Any]:
        """
        Retrieves the details of a specific custom field in the contact database, including its name, type, and other attributes.

        Args:
            custom_field_id (string): custom_field_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Custom Fields
        """
        if custom_field_id is None:
            raise ValueError("Missing required parameter 'custom_field_id'")
        url = f"{self.base_url}/v3/contactdb/custom_fields/{custom_field_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_contact_db_lists(self, items=None) -> Any:
        """
        Deletes a contact list in the contact database using the provided JSON body and returns a successful status without content if the operation is successful.

        Args:

        Returns:
            Any: API response data.

        Tags:
            Lists
        """
        # Use items array directly as request body
        url = f"{self.base_url}/v3/contactdb/lists"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_contact_db_list(self) -> dict[str, Any]:
        """
        Retrieves a list of all recipient lists from the contact database using the SendGrid API.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        url = f"{self.base_url}/v3/contactdb/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_contact_db_list(self, name=None) -> dict[str, Any]:
        """
        Creates a new contact list in the contact database and returns the created list resource.

        Args:
            name (string): name

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/contactdb/lists"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_contact_db_list(self, list_id, delete_contacts=None) -> Any:
        """
        Deletes a contact list identified by `{list_id}` in the contact database, optionally removing associated contacts if specified, and returns a status message.

        Args:
            list_id (string): list_id
            delete_contacts (boolean): If set to true, this query parameter deletes all contacts from the specified list when the list itself is deleted.

        Returns:
            Any: API response data.

        Tags:
            Lists
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'")
        url = f"{self.base_url}/v3/contactdb/lists/{list_id}"
        query_params = {
            k: v for k, v in [("delete_contacts", delete_contacts)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_contact_db_list(self, list_id) -> dict[str, Any]:
        """
        Retrieves details of a contact list specified by its ID using the "GET" method.

        Args:
            list_id (string): list_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'")
        url = f"{self.base_url}/v3/contactdb/lists/{list_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_contact_db_list(self, list_id, name=None) -> dict[str, Any]:
        """
        Updates specific properties of a contact list identified by {list_id} using a JSON Patch request.

        Args:
            list_id (string): list_id
            name (string): The new name for your list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/contactdb/lists/{list_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_recipients_from_contact_db_list(
        self, list_id, page=None, page_size=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of recipients for a specified contact list, allowing optional pagination via page and page size parameters.

        Args:
            list_id (string): list_id
            page (integer): The page query parameter specifies the page number of results to retrieve for paginated responses.
            page_size (integer): Optional integer parameter to specify the number of recipients returned per page for the list of recipients.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'")
        url = f"{self.base_url}/v3/contactdb/lists/{list_id}/recipients"
        query_params = {
            k: v for k, v in [("page", page), ("page_size", page_size)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_recipients_to_contact_db_list(self, list_id, items=None) -> Any:
        """
        Adds recipients to a specified contact list using the POST method and returns a success status upon creation.

        Args:
            list_id (string): list_id

        Returns:
            Any: API response data.

        Tags:
            Lists
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'")
        # Use items array directly as request body
        request_body = items
        url = f"{self.base_url}/v3/contactdb/lists/{list_id}/recipients"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_recipient_from_contact_db_list(self, list_id, recipient_id) -> Any:
        """
        Deletes a specific recipient from a contact list identified by list_id and recipient_id.

        Args:
            list_id (string): list_id
            recipient_id (string): recipient_id

        Returns:
            Any: API response data.

        Tags:
            Lists
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'")
        if recipient_id is None:
            raise ValueError("Missing required parameter 'recipient_id'")
        url = f"{self.base_url}/v3/contactdb/lists/{list_id}/recipients/{recipient_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_recipient_to_contact_db_list(self, list_id, recipient_id) -> Any:
        """
        Adds a recipient to a specific contact list by list ID and recipient ID.

        Args:
            list_id (string): list_id
            recipient_id (string): recipient_id

        Returns:
            Any: API response data.

        Tags:
            Lists
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'")
        if recipient_id is None:
            raise ValueError("Missing required parameter 'recipient_id'")
        url = f"{self.base_url}/v3/contactdb/lists/{list_id}/recipients/{recipient_id}"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_recipients(self, items=None) -> dict[str, Any]:
        """
        Deletes one or more recipients from the contact database according to the details provided in the JSON request body.

        Args:

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        # Use items array directly as request body
        url = f"{self.base_url}/v3/contactdb/recipients"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_recipient(self, page=None, page_size=None) -> dict[str, Any]:
        """
        Get a paginated list of recipients from the contact database.

        Args:
            page (integer): Specifies the page number for pagination in the response.
            page_size (integer): The number of recipients to return per page in the response, controlling the size of each paginated result set.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        url = f"{self.base_url}/v3/contactdb/recipients"
        query_params = {
            k: v for k, v in [("page", page), ("page_size", page_size)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_recipient(self, items=None) -> dict[str, Any]:
        """
        Updates a contact database recipient using the PATCH method with JSON content, allowing for partial modifications to an existing recipient's details.

        Args:

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        # Use items array directly as request body
        request_body = items
        url = f"{self.base_url}/v3/contactdb/recipients"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_recipient(self, items=None) -> dict[str, Any]:
        """
        Creates a new contact recipient in the contact database and returns the result, with the data provided in the request body.

        Args:

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        # Use items array directly as request body
        request_body = items
        url = f"{self.base_url}/v3/contactdb/recipients"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_billable(self) -> dict[str, Any]:
        """
        Retrieves the current count of billable recipients in the Marketing Campaigns contact database.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        url = f"{self.base_url}/v3/contactdb/recipients/billable_count"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_recipient_count(self) -> dict[str, Any]:
        """
        Retrieves the total count of recipients in the contact database.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        url = f"{self.base_url}/v3/contactdb/recipients/count"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_search_recipient(self, field_name=None) -> dict[str, Any]:
        """
        Retrieves recipients from SendGrid's contact database matching a specified field name using a GET request to allow filtering by custom recipient attributes.

        Args:
            field_name (string): **{field_name}:** An optional string parameter used in the query to filter or specify recipients during a search operation.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        url = f"{self.base_url}/v3/contactdb/recipients/search"
        query_params = {k: v for k, v in [("field_name", field_name)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_recipient(self, conditions=None, list_id=None) -> dict[str, Any]:
        """
        Searches recipients using segment conditions without creating a segment, allowing filters like equality, inequality, and containment, and returns a list of matching recipients.

        Args:
            conditions (array): The conditions by which this segment should be created.
            list_id (integer): list_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        request_body = {
            "conditions": conditions,
            "list_id": list_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/contactdb/recipients/search"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_recipient(self, recipient_id) -> dict[str, Any]:
        """
        Deletes a recipient from the contact database by the specified recipient ID and returns a status code indicating the outcome.

        Args:
            recipient_id (string): recipient_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        if recipient_id is None:
            raise ValueError("Missing required parameter 'recipient_id'")
        url = f"{self.base_url}/v3/contactdb/recipients/{recipient_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_recipient(self, recipient_id) -> dict[str, Any]:
        """
        Retrieves a single recipient from the contact database by ID using the SendGrid API.

        Args:
            recipient_id (string): recipient_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        if recipient_id is None:
            raise ValueError("Missing required parameter 'recipient_id'")
        url = f"{self.base_url}/v3/contactdb/recipients/{recipient_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_recipient_list(self, recipient_id) -> dict[str, Any]:
        """
        Retrieves a list of contact lists associated with a specific recipient identified by their recipient ID.

        Args:
            recipient_id (string): recipient_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        if recipient_id is None:
            raise ValueError("Missing required parameter 'recipient_id'")
        url = f"{self.base_url}/v3/contactdb/recipients/{recipient_id}/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_reserved_field(self) -> dict[str, Any]:
        """
        Retrieves a list of reserved field names in SendGrid's contact database that cannot be used for custom field names.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Custom Fields
        """
        url = f"{self.base_url}/v3/contactdb/reserved_fields"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_segment(self) -> dict[str, Any]:
        """
        Retrieves a list of all segments defined in the contact database using the SendGrid API.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Segments, important
        """
        url = f"{self.base_url}/v3/contactdb/segments"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_segment(
        self, conditions=None, list_id=None, name=None, recipient_count=None
    ) -> dict[str, Any]:
        """
        Creates a new segment in the contact database using a JSON payload.

        Args:
            conditions (array): The conditions for a recipient to be included in this segment.
            list_id (integer): The list id from which to make this segment. Not including this ID will mean your segment is created from the main contactdb rather than a list.
            name (string): The name of this segment.
            recipient_count (number): The count of recipients in this list. This is not included on creation of segments.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Segments
        """
        request_body = {
            "conditions": conditions,
            "list_id": list_id,
            "name": name,
            "recipient_count": recipient_count,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/contactdb/segments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_recipient_for_segment(
        self, segment_id, page=None, page_size=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of recipients for a specified contact database segment using pagination controls.

        Args:
            segment_id (string): segment_id
            page (integer): The "page" parameter is an integer used in the query string to specify the page number for paginating recipients within a segment.
            page_size (integer): The `page_size` parameter specifies the number of recipients to return per page for the segment with the given `segment_id`.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Segments
        """
        if segment_id is None:
            raise ValueError("Missing required parameter 'segment_id'")
        url = f"{self.base_url}/v3/contactdb/segments/{segment_id}/recipients"
        query_params = {
            k: v for k, v in [("page", page), ("page_size", page_size)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_status(self) -> dict[str, Any]:
        """
        Retrieves the status of current and recent contact export jobs from the SendGrid contact database.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Recipients
        """
        url = f"{self.base_url}/v3/contactdb/status"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_design(
        self, page_size=None, page_token=None, summary=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of design resources, supporting optional filtering by page size, page token, and summary mode.

        Args:
            page_size (integer): number of results to return
            page_token (string): token corresponding to a specific page of results, as provided by metadata
            summary (boolean): set to false to return all fields

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        url = f"{self.base_url}/v3/designs"
        query_params = {
            k: v
            for k, v in [
                ("page_size", page_size),
                ("page_token", page_token),
                ("summary", summary),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_design(
        self, editor=None, html_content=None, name=None, plain_content=None
    ) -> dict[str, Any]:
        """
        Creates a new design using the provided JSON data and returns a success response with a 201 status code upon successful creation.

        Args:
            editor (string): editor
            html_content (string): The HTML content of the Design.
            name (string): The name of the new design.
            plain_content (string): Plain text content of the Design.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        request_body = {
            "editor": editor,
            "html_content": html_content,
            "name": name,
            "plain_content": plain_content,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/designs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_pre_built_design(
        self, page_size=None, page_token=None, summary=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of pre-built designs using the "/v3/designs/pre-builts" endpoint, allowing for pagination and optional summarization of the results.

        Args:
            page_size (integer): number of results to return
            page_token (string): token corresponding to a specific page of results, as provided by metadata
            summary (boolean): set to false to return all fields

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        url = f"{self.base_url}/v3/designs/pre-builts"
        query_params = {
            k: v
            for k, v in [
                ("page_size", page_size),
                ("page_token", page_token),
                ("summary", summary),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_pre_built_design(self, id) -> dict[str, Any]:
        """
        Retrieves the details of a pre-built design by its ID using the "GET" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/designs/pre-builts/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_pre_built_design(self, id, editor=None, name=None) -> dict[str, Any]:
        """
        Creates or updates a pre-built design by ID using the provided data and returns a status response.

        Args:
            id (string): id
            editor (string): editor
            name (string): The name of the new design.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "editor": editor,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/designs/pre-builts/{id}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_design(self, id) -> dict[str, Any]:
        """
        Deletes a design resource identified by the specified ID using the DELETE method and returns a status code indicating success or failure.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/designs/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_design(self, id) -> dict[str, Any]:
        """
        Retrieves the details of a design by its ID using the "GET" method and returns a successful response if the design exists.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/designs/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_design(
        self,
        id,
        categories=None,
        generate_plain_content=None,
        html_content=None,
        name=None,
        plain_content=None,
        subject=None,
    ) -> dict[str, Any]:
        """
        Updates a specific design resource by modifying partial attributes identified by the `{id}` at the `/v3/designs/{id}` endpoint using JSON data in the request body.

        Args:
            id (string): id
            categories (array): The list of categories applied to the design
            generate_plain_content (boolean): If true, plain_content is always generated from html_content. If false, plain_content is not altered.
            html_content (string): The HTML content of the Design.
            name (string): Name of the Design.
            plain_content (string): Plain text content of the Design.
            subject (string): Subject of the Design.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "categories": categories,
            "generate_plain_content": generate_plain_content,
            "html_content": html_content,
            "name": name,
            "plain_content": plain_content,
            "subject": subject,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/designs/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_design(self, id, editor=None, name=None) -> dict[str, Any]:
        """
        Updates a design with the specified ID using the provided data and returns a successful creation response.

        Args:
            id (string): id
            editor (string): editor
            name (string): The name of the new design.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Designs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "editor": editor,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/designs/{id}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_device_stat(
        self, start_date, limit=None, offset=None, aggregated_by=None, end_date=None
    ) -> list[Any]:
        """
        Retrieves device statistics using the "GET" method, allowing for customization through parameters such as on behalf of, advanced query strings for limit and offset, aggregation, and start and end dates.

        Args:
            start_date (string): The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.
            limit (integer): The number of results to return.
            offset (integer): The point in the list to begin retrieving results.
            aggregated_by (string): How to group the statistics. Must be either "day", "week", or "month".
            end_date (string): The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

        Returns:
            list[Any]: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/devices/stats"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("aggregated_by", aggregated_by),
                ("start_date", start_date),
                ("end_date", end_date),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_engagement_quality_score(self, from_, to) -> dict[str, Any]:
        """
        Retrieves SendGrid Engagement Quality scores for a specified date range using the GET method.

        Args:
            from_ (string): Required start date of the engagement quality scores in string format. Example: '2006-01-02'.
            to (string): The "to" parameter specifies the end date for retrieving engagement quality scores in the format of a string, marking the last day of the range for which scores are returned. Example: '2006-01-02'.

        Returns:
            dict[str, Any]: 200 OK

        Tags:
            Engagement Quality
        """
        url = f"{self.base_url}/v3/engagementquality/scores"
        query_params = {k: v for k, v in [("from", from_), ("to", to)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_subuser_engagement_quality_score(
        self, date, limit=None, after_key=None
    ) -> dict[str, Any]:
        """
        Retrieves engagement quality scores for specified subusers, including overall scores and contributing metrics, using optional parameters for date range and pagination.

        Args:
            date (string): The date in YYYY-MM-DD format (UTC) for which you want to retrieve a SendGrid Engagement Quality score.
            limit (integer): Specifies the number of results to be returned by the API. This parameter can be used to limit the results returned or in combination with the `after_key` parameter to iterate through paginated results. Example: '750'.
            after_key (integer): Specifies which items to be returned by the API. When the `after_key` is specified, the API will return items beginning from the first item after the item specified. This parameter can be used in combination with `limit` to iterate through paginated results.

        Returns:
            dict[str, Any]: Example response

        Tags:
            Engagement Quality
        """
        url = f"{self.base_url}/v3/engagementquality/subusers/scores"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("date", date), ("after_key", after_key)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_geo_stat(
        self,
        start_date,
        country=None,
        limit=None,
        offset=None,
        aggregated_by=None,
        end_date=None,
    ) -> list[Any]:
        """
        Retrieves geographic statistics for a specified country using the GET method, allowing for advanced filtering by date range and aggregation options.

        Args:
            start_date (string): The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.
            country (string): Optional query string parameter to filter geographic statistics by a specific country.
            limit (integer): The number of results to return.
            offset (integer): The point in the list to begin retrieving results.
            aggregated_by (string): How to group the statistics. Must be either "day", "week", or "month".
            end_date (string): The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

        Returns:
            list[Any]: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/geo/stats"
        query_params = {
            k: v
            for k, v in [
                ("country", country),
                ("limit", limit),
                ("offset", offset),
                ("aggregated_by", aggregated_by),
                ("start_date", start_date),
                ("end_date", end_date),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_assigned_ip(self) -> list[Any]:
        """
        Retrieves a list of assigned IP addresses using the "GET" method at the "/v3/ips/assigned" path.

        Returns:
            list[Any]: API response data.

        Tags:
            IP Addresses
        """
        url = f"{self.base_url}/v3/ips/assigned"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_ip_pool(self) -> list[Any]:
        """
        Retrieves a list of IP pools using the "GET" method at the "/v3/ips/pools" path.

        Returns:
            list[Any]: API response data.

        Tags:
            IP Pools
        """
        url = f"{self.base_url}/v3/ips/pools"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_ip_to_ip_pool(self, pool_name, ip=None) -> dict[str, Any]:
        """
        Adds a new IP address to the specified IP pool.

        Args:
            pool_name (string): pool_name
            ip (string): The IP address that you want to add to the named pool.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Pools
        """
        if pool_name is None:
            raise ValueError("Missing required parameter 'pool_name'")
        request_body = {
            "ip": ip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/ips/pools/{pool_name}/ips"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_ip_from_ip_pool(self, pool_name, ip) -> dict[str, Any]:
        """
        Deletes the specified IP address from the given IP pool.

        Args:
            pool_name (string): pool_name
            ip (string): ip

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Pools
        """
        if pool_name is None:
            raise ValueError("Missing required parameter 'pool_name'")
        if ip is None:
            raise ValueError("Missing required parameter 'ip'")
        url = f"{self.base_url}/v3/ips/pools/{pool_name}/ips/{ip}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_remaining_ip_count(self) -> dict[str, Any]:
        """
        Retrieves the number of remaining IP addresses available for allocation.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Addresses
        """
        url = f"{self.base_url}/v3/ips/remaining"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_warm_up_ip(self) -> list[Any]:
        """
        Retrieves and returns data related to the IP warm-up process using the GET method at the "/v3/ips/warmup" path.

        Returns:
            list[Any]: API response data.

        Tags:
            IP Warmup
        """
        url = f"{self.base_url}/v3/ips/warmup"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def warm_up_ip(self, ip=None) -> list[Any]:
        """
        Initiates the warmup process for one or more IP addresses by submitting a request in JSON format and returns a success or not found response.

        Args:
            ip (string): The IP address that you want to begin warming up.

        Returns:
            list[Any]: API response data.

        Tags:
            IP Warmup
        """
        request_body = {
            "ip": ip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/ips/warmup"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def stop_ip_warm_up(self, ip_address) -> dict[str, Any]:
        """
        Removes the specified IP address from the warmup pool and returns no content upon successful deletion.

        Args:
            ip_address (string): ip_address

        Returns:
            dict[str, Any]: API response data.

        Tags:
            IP Warmup
        """
        if ip_address is None:
            raise ValueError("Missing required parameter 'ip_address'")
        url = f"{self.base_url}/v3/ips/warmup/{ip_address}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_warm_up_ip(self, ip_address) -> list[Any]:
        """
        Retrieves information about warming up a specific IP address using the GET method and returns a response based on the operation's success or failure.

        Args:
            ip_address (string): ip_address

        Returns:
            list[Any]: API response data.

        Tags:
            IP Warmup
        """
        if ip_address is None:
            raise ValueError("Missing required parameter 'ip_address'")
        url = f"{self.base_url}/v3/ips/warmup/{ip_address}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_mail_batch(self) -> dict[str, Any]:
        """
        Creates and submits a batch of emails in a single request, supporting optional delegation and returning a confirmation upon successful processing.

        Returns:
            dict[str, Any]: Batch ID success response.

        Tags:
            Mail Batch
        """
        url = f"{self.base_url}/v3/mail/batch"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_mail_batch(self, batch_id) -> dict[str, Any]:
        """
        Retrieves the status and details of a specific batch mail operation by its batch ID.

        Args:
            batch_id (string): batch_id

        Returns:
            dict[str, Any]: Batch ID success response.

        Tags:
            Mail Batch
        """
        if batch_id is None:
            raise ValueError("Missing required parameter 'batch_id'")
        url = f"{self.base_url}/v3/mail/batch/{batch_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_mail(
        self,
        asm=None,
        attachments=None,
        batch_id=None,
        categories=None,
        content=None,
        custom_args=None,
        from_=None,
        headers=None,
        ip_pool_name=None,
        mail_settings=None,
        personalizations=None,
        reply_to=None,
        reply_to_list=None,
        send_at=None,
        subject=None,
        template_id=None,
        tracking_settings=None,
    ) -> Any:
        """
        Sends an email using the specified mail service by transmitting the required data via the POST method at the "/v3/mail/send" endpoint.

        Args:
            asm (object): An object allowing you to specify how to handle unsubscribes. With SendGrid, an unsubscribe is the action an email recipient takes when they opt-out of receiving your messages. A suppression is the action you take as a sender to filter or suppress an unsubscribed address from your email send. From the perspective of the recipient, your suppression is the result of their unsubscribe. See [**Suppression Groups**](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-unsubscribe-groups/create-a-new-suppression-group) for more information.
            attachments (array): An array of objects where you can define any attachments to be included with the message. Each object contains a `content` property, which must be a Base64 encoded string of the attachment itself, and `type`, `filename`, `disposition`, and `content_id` properties that tell SendGrid how to handle the attachment.
            batch_id (string): An ID representing a batch of emails to be sent at the same time. Including a `batch_id` in your request allows you to include this email in that batch. It also enables you to cancel or pause the delivery of that batch. See the [Scheduled Sends API](https://sendgrid.com/docs/api-reference/) for more information about scheduling your email.
            categories (array): An array of category names assigned to this message. Categories allow you to group messages by categories you define. Categories should be used sparingly to create general groups that are relevant to you. Categories are not meant to be used to track individual mail sends. For more granular categorization and tracking, use the `custom_args` property. A category name cannot exceed 255 characters. See [**Working with Categories**](https://docs.sendgrid.com/for-developers/sending-email/categories) for more information.
            content (array): An array of objects, each containing a message body's content and [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types). You must specify at least one MIME type and may include multiple. To include more than one MIME type, add an object for each type to the array.
            custom_args (string): Values that are specific to the entire send that will be carried along with the email and its activity data. Substitutions will not be made on custom arguments, so any string that is assigned to this property will be assumed to be the custom argument that you would like to be used. This parameter is overridden by `custom_args` set at the personalizations level. Total `custom_args` size may not exceed 10,000 bytes.
            from_ (object): from
            headers (object): A collection of JSON property name and property value pairs allowing you to specify handling instructions for your email. You may not override the following headers: `x-sg-id`, `x-sg-eid`, `received`, `dkim-signature`, `Content-Type`, `Content-Transfer-Encoding`, `To`, `From`, `Subject`, `Reply-To`, `CC`, `BCC`.
            ip_pool_name (string): The IP Pool that you would like to send this email from. IP Pools allow you to group your dedicated Twilio SendGrid IP addresses in order to have more control over your deliverability. See [**IP Pools**](https://docs.sendgrid.com/ui/account-and-settings/ip-pools) for more information.
            mail_settings (object): A collection of different mail settings that you can use to specify how you would like this email to be handled. Mail settings provide extra functionality to your mail send. See [**Mail Settings**](https://docs.sendgrid.com/ui/account-and-settings/mail) for more information.
            personalizations (array): An array of messages and their metadata. Each object within the `personalizations` array can be thought of as a mail envelope—it defines who should receive an individual message and how that message should be handled. See [**Personalizations**](https://sendgrid.com/docs/for-developers/sending-email/personalizations/) for more information.
            reply_to (object): reply_to
            reply_to_list (array): An array of recipients to whom replies will be sent. Each object in this array must contain a recipient's email address. Each object in the array may optionally contain a recipient's name. You can use either the `reply_to` property or `reply_to_list` property but not both.
            send_at (integer): A [unix timestamp](https://en.wikipedia.org/wiki/Unix_time) allowing you to specify when your email should be sent. A send cannot be scheduled more than 72 hours in advance. This property may be overridden by the `send_at` property set at the personalizations level.
            subject (string): The global or _message level_ subject of your email. Subject lines set in personalizations objects will override this global subject line. See line length limits specified in [RFC 2822](https://www.rfc-editor.org/rfc/rfc2822#section-2.1.1) for guidance on subject line character limits.
            template_id (string): An email template ID. A template that contains a subject and content—either text or html—will override any subject and content values specified at the `personalizations` or message level. If a template ID begins with `d-`, it is a dynamic template and will work with the `dynamic_template_data` property. If the template ID does not begin with `d-`, it is a standard SendGrid template and will work with the `substitutions` property. See [**How to Send an Email with Dynamic Templates**](https://docs.sendgrid.com/ui/sending-email/how-to-send-an-email-with-dynamic-templates) for more information about working with templates.
            tracking_settings (object): Settings to determine how you would like to track the metrics of how your recipients interact with your email. See [**Tracking Settings**](https://docs.sendgrid.com/ui/account-and-settings/tracking) for more information.
                Example:
                ```json
                {
                  "asm": {
                    "group_id": 12345,
                    "groups_to_display": [
                      12345
                    ]
                  },
                  "attachments": [
                    {
                      "content": "PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KCiAgICA8aGVhZD4KICAgICAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCI+CiAgICAgICAgPG1ldGEgaHR0cC1lcXVpdj0iWC1VQS1Db21wYXRpYmxlIiBjb250ZW50PSJJRT1lZGdlIj4KICAgICAgICA8bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFsLXNjYWxlPTEuMCI+CiAgICAgICAgPHRpdGxlPkRvY3VtZW50PC90aXRsZT4KICAgIDwvaGVhZD4KCiAgICA8Ym9keT4KCiAgICA8L2JvZHk+Cgo8L2h0bWw+Cg==",
                      "disposition": "attachment",
                      "filename": "index.html",
                      "type": "text/html"
                    }
                  ],
                  "batch_id": "AsdFgHjklQweRTYuIopzXcVBNm0aSDfGHjklmZcVbNMqWert1znmOP2asDFjkl",
                  "categories": [
                    "cake",
                    "pie",
                    "baking"
                  ],
                  "from": {
                    "email": "orders@example.com",
                    "name": "Example Order Confirmation"
                  },
                  "ip_pool_name": "transactional email",
                  "mail_settings": {
                    "bypass_list_management": {
                      "enable": false
                    },
                    "footer": {
                      "enable": false
                    },
                    "sandbox_mode": {
                      "enable": false
                    }
                  },
                  "personalizations": [
                    {
                      "dynamic_template_data": {
                        "confirmation_number": "123abc456def789hij0",
                        "customer_name": "Alex",
                        "subject": "Hello, Alex"
                      },
                      "to": [
                        {
                          "email": "alex@example.com",
                          "name": "Alex"
                        },
                        {
                          "email": "bola@example.com",
                          "name": "Bola"
                        }
                      ]
                    }
                  ],
                  "reply_to": {
                    "email": "customer_service@example.com",
                    "name": "Example Customer Service Team"
                  },
                  "send_at": 1617260400,
                  "tempalte_id": "d-123abc456def789hij0klm123nop456qrs789tuv0xyz",
                  "tracking_settings": {
                    "click_tracking": {
                      "enable": true,
                      "enable_text": false
                    },
                    "open_tracking": {
                      "enable": true,
                      "substitution_tag": "%open-track%"
                    },
                    "subscription_tracking": {
                      "enable": false
                    }
                  }
                }
                ```

        Returns:
            Any: Accepted

        Tags:
            Mail Send
        """
        request_body = {
            "asm": asm,
            "attachments": attachments,
            "batch_id": batch_id,
            "categories": categories,
            "content": content,
            "custom_args": custom_args,
            "from": from_,
            "headers": headers,
            "ip_pool_name": ip_pool_name,
            "mail_settings": mail_settings,
            "personalizations": personalizations,
            "reply_to": reply_to,
            "reply_to_list": reply_to_list,
            "send_at": send_at,
            "subject": subject,
            "template_id": template_id,
            "tracking_settings": tracking_settings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/mail/send"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_mail_setting(self, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves mail settings using the GET method, allowing optional parameters for pagination and acting on behalf of another party.

        Args:
            limit (integer): Specifies the maximum number of mail settings records to return in a single response.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        url = f"{self.base_url}/v3/mail_settings"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_address_whitelist(self) -> dict[str, Any]:
        """
        Retrieves the current list of whitelisted email addresses for mail settings.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        url = f"{self.base_url}/v3/mail_settings/address_whitelist"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_address_whitelist(self, enabled=None, list=None) -> dict[str, Any]:
        """
        Modifies the email address whitelist settings using the PATCH method, accepting JSON payload updates at the "/v3/mail_settings/address_whitelist" endpoint.

        Args:
            enabled (boolean): Indicates if your email address whitelist is enabled.
            list (array): Either a single email address that you want whitelisted or a domain, for which all email addresses belonging to this domain will be whitelisted.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        request_body = {
            "enabled": enabled,
            "list": list,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/mail_settings/address_whitelist"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_bounce_purge(self) -> dict[str, Any]:
        """
        Retrieves the current bounce purge mail settings using the SendGrid API, which define how and when bounced email addresses are automatically removed from suppression lists.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        url = f"{self.base_url}/v3/mail_settings/bounce_purge"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_bounce_purge(
        self, enabled=None, hard_bounces=None, soft_bounces=None
    ) -> dict[str, Any]:
        """
        Updates the bounce purge mail settings by applying partial modifications to the resource using a JSON request body.

        Args:
            enabled (boolean): Indicates if the bounce purge mail setting is enabled.
            hard_bounces (integer): The number of days after which SendGrid will purge all contacts from your hard bounces suppression lists.
            soft_bounces (integer): The number of days after which SendGrid will purge all contacts from your soft bounces suppression lists.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        request_body = {
            "enabled": enabled,
            "hard_bounces": hard_bounces,
            "soft_bounces": soft_bounces,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/mail_settings/bounce_purge"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_footer(self) -> dict[str, Any]:
        """
        Retrieves the footer settings for mail using the specified parameters.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        url = f"{self.base_url}/v3/mail_settings/footer"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_footer(
        self, enabled=None, html_content=None, plain_content=None
    ) -> dict[str, Any]:
        """
        Updates the footer settings for mail using the PATCH method, allowing partial modifications to existing mail settings.

        Args:
            enabled (boolean): Indicates if the Footer mail setting is currently enabled.
            html_content (string): The custom HTML content of your email footer.
            plain_content (string): The plain text content of your email footer.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        request_body = {
            "enabled": enabled,
            "html_content": html_content,
            "plain_content": plain_content,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/mail_settings/footer"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_forward_bounce(self) -> dict[str, Any]:
        """
        Retrieves the current mail settings for forwarding bounced emails to a specified address.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        url = f"{self.base_url}/v3/mail_settings/forward_bounce"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_forward_bounce(self, email=None, enabled=None) -> dict[str, Any]:
        """
        Modifies mail settings for forwarding and bouncing using the "PATCH" method, updating specified fields in the resource located at "/v3/mail_settings/forward_bounce".

        Args:
            email (string): The email address that you would like your bounce reports forwarded to.
            enabled (boolean): Indicates if the bounce forwarding mail setting is enabled.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        request_body = {
            "email": email,
            "enabled": enabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/mail_settings/forward_bounce"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_forward_spam(self) -> dict[str, Any]:
        """
        Retrieves the current Forward Spam mail settings, including the enabled status and any email addresses designated to receive forwarded spam reports[2][3].

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        url = f"{self.base_url}/v3/mail_settings/forward_spam"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_forward_spam(self, email=None, enabled=None) -> dict[str, Any]:
        """
        Updates mail settings for spam forwarding using the "PATCH" method, allowing partial modifications to the existing configuration.

        Args:
            email (string): The email address where you would like the spam reports to be forwarded.
            enabled (boolean): Indicates if the Forward Spam setting is enabled.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        request_body = {
            "email": email,
            "enabled": enabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/mail_settings/forward_spam"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_template(self) -> dict[str, Any]:
        """
        Retrieves the current template mail settings for the specified account using the SendGrid API.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        url = f"{self.base_url}/v3/mail_settings/template"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_template(self, enabled=None, html_content=None) -> dict[str, Any]:
        """
        Updates the mail settings template using the PATCH method, allowing for partial modifications to the existing resource.

        Args:
            enabled (boolean): Indicates if you want to enable the legacy email template mail setting.
            html_content (string): The new HTML content for your legacy email template.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Mail Settings
        """
        request_body = {
            "enabled": enabled,
            "html_content": html_content,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/mail_settings/template"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_mailbox_provider_stat(
        self,
        start_date,
        mailbox_providers=None,
        limit=None,
        offset=None,
        aggregated_by=None,
        end_date=None,
    ) -> list[Any]:
        """
        Retrieves email statistics segmented by recipient mailbox provider, allowing for filtering by provider, date range, and aggregation type.

        Args:
            start_date (string): The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.
            mailbox_providers (string): Filter the statistics by one or more mailbox providers to retrieve email activity data specific to those providers.
            limit (integer): The number of results to return.
            offset (integer): The point in the list to begin retrieving results.
            aggregated_by (string): How to group the statistics. Must be either "day", "week", or "month".
            end_date (string): The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

        Returns:
            list[Any]: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/mailbox_providers/stats"
        query_params = {
            k: v
            for k, v in [
                ("mailbox_providers", mailbox_providers),
                ("limit", limit),
                ("offset", offset),
                ("aggregated_by", aggregated_by),
                ("start_date", start_date),
                ("end_date", end_date),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_contact(self, delete_all_contacts=None, ids=None) -> dict[str, Any]:
        """
        Deletes contacts in the marketing system using the specified IDs or clears all contacts if the "delete_all_contacts" parameter is set, returning status codes to indicate the outcome of the operation.

        Args:
            delete_all_contacts (string): Specifies whether to delete all contacts in the system when set to "true"; must be set explicitly to avoid accidental deletion of all contacts.
            ids (string): A comma-separated list of contact IDs to be deleted; if omitted, all contacts may be deleted (depending on API implementation).

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        url = f"{self.base_url}/v3/marketing/contacts"
        query_params = {
            k: v
            for k, v in [("delete_all_contacts", delete_all_contacts), ("ids", ids)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_contact(self) -> dict[str, Any]:
        """
        Retrieves a list of contacts from the marketing service, returning their details in the response.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        url = f"{self.base_url}/v3/marketing/contacts"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_contact(self, contacts=None, list_ids=None) -> dict[str, Any]:
        """
        Updates or adds marketing contact information by replacing the existing contact data with the provided JSON payload.

        Args:
            contacts (array): One or more contacts objects that you intend to upsert. Each contact needs to include at least one of `email`, `phone_number_id`, `external_id`, or `anonymous_id` as an identifier.
            list_ids (array): An array of List ID strings that this contact will be added to.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        request_body = {
            "contacts": contacts,
            "list_ids": list_ids,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/contacts"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_batched_contact(self, ids=None) -> dict[str, Any]:
        """
        Creates a batch of contacts in the marketing system using a JSON payload and returns a success status upon completion.

        Args:
            ids (array): ids

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        request_body = {
            "ids": ids,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/contacts/batch"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_export_contact(self) -> dict[str, Any]:
        """
        Retrieves a list or details of marketing contact exports using the "GET" method at the "/v3/marketing/contacts/exports" path.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        url = f"{self.base_url}/v3/marketing/contacts/exports"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def export_contact(
        self,
        file_type=None,
        list_ids=None,
        max_file_size=None,
        notifications=None,
        segment_ids=None,
    ) -> dict[str, Any]:
        """
        Exports contacts using a POST request to the "/v3/marketing/contacts/exports" endpoint, accepting JSON data in the request body.

        Args:
            file_type (string): file_type
            list_ids (array): IDs of the contact lists you want to export.
            max_file_size (integer): The maximum size of an export file in MB. Note that when this option is specified, multiple output files may be returned from the export.
            notifications (object): notifications
            segment_ids (array): IDs of the contact segments you want to export.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        request_body = {
            "file_type": file_type,
            "list_ids": list_ids,
            "max_file_size": max_file_size,
            "notifications": notifications,
            "segment_ids": segment_ids,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/contacts/exports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_export_contact(self, id) -> dict[str, Any]:
        """
        Retrieves the details of a specific marketing contacts export by its ID using the "GET" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/contacts/exports/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def import_contact(
        self, field_mappings=None, file_type=None, list_ids=None
    ) -> dict[str, Any]:
        """
        Imports or updates marketing contacts in bulk by replacing or creating the contact data using a JSON payload.

        Args:
            field_mappings (array): Import file header to reserved/custom field mapping.
            file_type (string): file_type
            list_ids (array): All contacts will be added to each of the specified lists.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        request_body = {
            "field_mappings": field_mappings,
            "file_type": file_type,
            "list_ids": list_ids,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/contacts/imports"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_import_contact(self, id) -> dict[str, Any]:
        """
        Retrieves details about a specific contact import operation by its ID using the "GET" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/contacts/imports/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_contact(self, query=None) -> dict[str, Any]:
        """
        Searches for contacts using a SendGrid API endpoint by sending a POST request with a JSON body containing a valid SGQL query, returning up to 50 contacts that match the search criteria.

        Args:
            query (string): An SGQL search string or other pattern.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        request_body = {
            "query": query,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/contacts/search"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_contact_by_email(
        self, anonymous_id=None, emails=None, external_id=None, phone_number_id=None
    ) -> dict[str, Any]:
        """
        Searches for marketing contacts by their email addresses via a POST request and returns matching contact records or error responses if the request is invalid.

        Args:
            anonymous_id (string): The contact's Anonymous ID.
            emails (array): One or more primary and/or alternate email addresses to search for in your Marketing Campaigns contacts.
            external_id (string): The contact's External ID.
            phone_number_id (string): The contact's Phone Number ID. This is required to be a valid phone number.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        request_body = {
            "anonymous_id": anonymous_id,
            "emails": emails,
            "external_id": external_id,
            "phone_number_id": phone_number_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/contacts/search/emails"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_contact_by_identifiers(
        self, identifier_type, identifiers=None
    ) -> dict[str, Any]:
        """
        Searches marketing contacts by a specified identifier type using a POST request with JSON payload and returns matching contact information.

        Args:
            identifier_type (string): identifier_type
            identifiers (array): One or more more identifier values to search for in your Marketing Campaigns contacts.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        if identifier_type is None:
            raise ValueError("Missing required parameter 'identifier_type'")
        request_body = {
            "identifiers": identifiers,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/contacts/search/identifiers/{identifier_type}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_contact_identifier(
        self, contact_id, identifier_type=None, identifier_value=None
    ) -> dict[str, Any]:
        """
        Deletes a contact identifier with the specified contact ID and returns a status indicating whether the operation was accepted or encountered errors.

        Args:
            contact_id (string): contact_id
            identifier_type (string): identifier_type
            identifier_value (string): The value of the identifier you want to remove from the contact.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        if contact_id is None:
            raise ValueError("Missing required parameter 'contact_id'")
        request_body = {
            "identifier_type": identifier_type,
            "identifier_value": identifier_value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/contacts/{contact_id}/identifiers"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_contact(self, id) -> dict[str, Any]:
        """
        Retrieves detailed information for a specified contact in the marketing contacts database.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Contacts
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/contacts/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_field_definition(self) -> dict[str, Any]:
        """
        Retrieves the definitions of marketing fields available for use in marketing-related API operations.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Custom Fields
        """
        url = f"{self.base_url}/v3/marketing/field_definitions"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_field_definition(self, field_type=None, name=None) -> dict[str, Any]:
        """
        Creates new custom field definitions for marketing purposes using the "POST" method at the "/v3/marketing/field_definitions" endpoint, accepting JSON-formatted data in the request body.

        Args:
            field_type (string): field_type
            name (string): name

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Custom Fields
        """
        request_body = {
            "field_type": field_type,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/field_definitions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_field_definition(self, custom_field_id) -> Any:
        """
        Deletes the specified marketing field definition by custom field ID and returns a 204 (No Content) on success or 404 (Not Found) if the resource does not exist.

        Args:
            custom_field_id (string): custom_field_id

        Returns:
            Any: API response data.

        Tags:
            Custom Fields
        """
        if custom_field_id is None:
            raise ValueError("Missing required parameter 'custom_field_id'")
        url = f"{self.base_url}/v3/marketing/field_definitions/{custom_field_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_field_definition(self, custom_field_id, name=None) -> dict[str, Any]:
        """
        Updates a specific custom field definition in the marketing system using the provided field ID and returns a status or error response.

        Args:
            custom_field_id (string): custom_field_id
            name (string): name

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Custom Fields
        """
        if custom_field_id is None:
            raise ValueError("Missing required parameter 'custom_field_id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/field_definitions/{custom_field_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_integration(self, ids) -> Any:
        """
        Deletes marketing integrations specified by the IDs provided in the request, returning no content upon successful deletion.

        Args:
            ids (array): A comma-separated list of integration IDs to delete.

        Returns:
            Any: Successful Operation

        Tags:
            External Integration Endpoints
        """
        url = f"{self.base_url}/v3/marketing/integrations"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_integrations_by_user(self) -> dict[str, Any]:
        """
        Retrieves a list of available marketing integrations and their API connection details.

        Returns:
            dict[str, Any]: Successful Operation

        Tags:
            External Integration Endpoints
        """
        url = f"{self.base_url}/v3/marketing/integrations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_integration(
        self, destination, filters, properties, label=None
    ) -> dict[str, Any]:
        """
        Creates a new marketing integration by accepting required JSON data and returns a confirmation on success or an error otherwise.

        Args:
            destination (string): destination
            filters (object): The configurable filters for SendGrid to destination email event forwarding.
            properties (object): The properties of an Integration required to send events to a specific third-party application.
            label (string): The nickname for the Integration.
                Example:
                ```json
                {
                  "destination": "Segment",
                  "filters": {
                    "email_events": [
                      "click",
                      "drop",
                      "open",
                      "processed",
                      "delivered"
                    ]
                  },
                  "label": "optional label",
                  "properties": {
                    "destination_region": "US",
                    "write_key": "a123456"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successful Operation

        Tags:
            External Integration Endpoints
        """
        request_body = {
            "destination": destination,
            "filters": filters,
            "label": label,
            "properties": properties,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/integrations"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_integration_by_id(self, id) -> dict[str, Any]:
        """
        Retrieves details about a specific marketing integration by its ID using the "GET" method at the path "/v3/marketing/integrations/{id}".

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Successful operation

        Tags:
            External Integration Endpoints
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/integrations/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_integration(
        self, id, destination=None, filters=None, label=None, properties=None
    ) -> dict[str, Any]:
        """
        Updates a marketing integration identified by its ID using the provided JSON Patch document.

        Args:
            id (string): id
            destination (string): destination
            filters (object): The configurable filters for SendGrid to destination email event forwarding.
            label (string): The nickname for the Integration. Example: 'My New Segment Integration!'.
            properties (object): The properties of an Integration required to send events to a specific third-party application.
                Example:
                ```json
                {
                  "destination": "Segment",
                  "filters": {
                    "email_events": [
                      "processed",
                      "open"
                    ]
                  },
                  "label": "Untitled Integration",
                  "properties": {
                    "destination_region": "US",
                    "write_key": "a123456"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successful Operation

        Tags:
            External Integration Endpoints
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "destination": destination,
            "filters": filters,
            "label": label,
            "properties": properties,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/integrations/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_marketing_segment(self, page_size=None, page_token=None) -> dict[str, Any]:
        """
        Retrieves a list of marketing lists, allowing pagination through optional parameters for page size and page token.

        Args:
            page_size (number): Specifies the maximum number of items to return per page in the response; defaults to 100 if not provided.
            page_token (string): Optional string parameter used to fetch the next page of results in a paginated response, allowing users to continue listing records beyond the initial set returned.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        url = f"{self.base_url}/v3/marketing/lists"
        query_params = {
            k: v
            for k, v in [("page_size", page_size), ("page_token", page_token)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_marketing_list(self, name=None) -> dict[str, Any]:
        """
        Creates a new marketing list for managing contacts in marketing campaigns using the SendGrid API.

        Args:
            name (string): Your name for your list

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/lists"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_marketing_list(self, id, delete_contacts=None) -> dict[str, Any]:
        """
        Deletes a specific marketing list using the provided ID and optionally deletes associated contacts if the `delete_contacts` query parameter is set to true.

        Args:
            id (string): id
            delete_contacts (boolean): Deletes contacts associated with the list if set to true; defaults to false.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/lists/{id}"
        query_params = {
            k: v for k, v in [("delete_contacts", delete_contacts)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_marketing_list(self, id, contact_sample=None) -> dict[str, Any]:
        """
        Retrieves details of a marketing list by its ID using the "GET" method, optionally filtering by contact sample if specified.

        Args:
            id (string): id
            contact_sample (boolean): Indicates whether to return a sample of contacts for the specified list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/lists/{id}"
        query_params = {
            k: v for k, v in [("contact_sample", contact_sample)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_marketing_list(self, id, name=None) -> dict[str, Any]:
        """
        Modifies a specific marketing list identified by its ID using the PATCH method, allowing for partial updates to the list's properties.

        Args:
            id (string): id
            name (string): Your name for your list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/lists/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_contact_count(self, id) -> dict[str, Any]:
        """
        Retrieves the total number of contacts in the specified marketing list.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/lists/{id}/contacts/count"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_makreting_segment(
        self, ids=None, parent_list_ids=None, no_parent_list_id=None
    ) -> dict[str, Any]:
        """
        Retrieves marketing segment data, version 2.0, allowing optional filtering by segment IDs, parent list IDs, and whether to exclude parent list IDs.

        Args:
            ids (array): A comma-separated list of segment IDs to filter the results.
            parent_list_ids (string): Optional string parameter to filter segments based on their parent list IDs.
            no_parent_list_id (boolean): Indicates whether to exclude the parent list ID from the response; defaults to false.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Segmenting Contacts V2
        """
        url = f"{self.base_url}/v3/marketing/segments/2.0"
        query_params = {
            k: v
            for k, v in [
                ("ids", ids),
                ("parent_list_ids", parent_list_ids),
                ("no_parent_list_id", no_parent_list_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def refresh_segment(self, segment_id, user_time_zone) -> dict[str, Any]:
        """
        Refreshes a specified marketing segment by its ID, ensuring that the segment is updated to reflect any changes in contact data or segment criteria.

        Args:
            segment_id (string): segment_id
            user_time_zone (string): The user's timezone. The timezone is used to reset the refresh count at midnight in the user's local time. Only [IANA time zone format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is accepted.

        Returns:
            dict[str, Any]: The refresh was accepted and a request was sent to process.

        Tags:
            Segmenting Contacts V2
        """
        if segment_id is None:
            raise ValueError("Missing required parameter 'segment_id'")
        request_body = {
            "user_time_zone": user_time_zone,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/segments/2.0/refresh/{segment_id}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_segment(self, segment_id) -> Any:
        """
        Deletes a marketing segment identified by the segment ID using the DELETE method, returning a status code indicating the outcome of the operation.

        Args:
            segment_id (string): segment_id

        Returns:
            Any: API response data.

        Tags:
            Segmenting Contacts V2
        """
        if segment_id is None:
            raise ValueError("Missing required parameter 'segment_id'")
        url = f"{self.base_url}/v3/marketing/segments/2.0/{segment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment(self, segment_id, contacts_sample=None) -> dict[str, Any]:
        """
        Retrieves details for a specific marketing segment, identified by its segment ID, with optional filtering by sampling contacts.

        Args:
            segment_id (string): segment_id
            contacts_sample (boolean): If true, includes a sample of contacts in the segment response.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Segmenting Contacts V2
        """
        if segment_id is None:
            raise ValueError("Missing required parameter 'segment_id'")
        url = f"{self.base_url}/v3/marketing/segments/2.0/{segment_id}"
        query_params = {
            k: v for k, v in [("contacts_sample", contacts_sample)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_segment(self, segment_id, name=None, query_dsl=None) -> dict[str, Any]:
        """
        Updates a marketing segment using the PATCH method, allowing partial modifications to the specified segment resource.

        Args:
            segment_id (string): segment_id
            name (string): Name of the segment.
            query_dsl (string): SQL query which will filter contacts based on the conditions provided

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Segmenting Contacts V2
        """
        if segment_id is None:
            raise ValueError("Missing required parameter 'segment_id'")
        request_body = {
            "name": name,
            "query_dsl": query_dsl,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/segments/2.0/{segment_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_sender(
        self,
        address=None,
        address_2=None,
        city=None,
        country=None,
        from_=None,
        nickname=None,
        reply_to=None,
        state=None,
        zip=None,
    ) -> dict[str, Any]:
        """
        Adds a new sender to the marketing senders list using the SendGrid API and returns a status code indicating the success or failure of the operation.

        Args:
            address (string): The physical address of the Sender.
            address_2 (string): Additional Sender address information.
            city (string): The city of the Sender.
            country (string): The country of the Sender.
            from_ (object): from
            nickname (string): A nickname for the Sender. Not used for sending.
            reply_to (object): reply_to
            state (string): The state of the Sender.
            zip (string): The zipcode of the Sender.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Senders
        """
        request_body = {
            "address": address,
            "address_2": address_2,
            "city": city,
            "country": country,
            "from": from_,
            "nickname": nickname,
            "reply_to": reply_to,
            "state": state,
            "zip": zip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/senders"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_sender(self, id) -> Any:
        """
        Deletes a marketing sender with the specified ID using the DELETE method, returning a successful response with no content if found, or an error if unauthorized or not found.

        Args:
            id (string): id

        Returns:
            Any: successfully deleted, no response in payload

        Tags:
            Senders
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/senders/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sender(self, id) -> dict[str, Any]:
        """
        Retrieves the details of a specific sender by ID using the GET method at the "/v3/marketing/senders/{id}" endpoint.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Senders
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/senders/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_sender(
        self,
        id,
        address=None,
        address_2=None,
        city=None,
        country=None,
        from_=None,
        nickname=None,
        reply_to=None,
        state=None,
        zip=None,
    ) -> dict[str, Any]:
        """
        Updates the properties of a marketing sender resource identified by the given ID using a PATCH request and returns the appropriate status code.

        Args:
            id (string): id
            address (string): The physical address of the Sender.
            address_2 (string): Additional Sender address information.
            city (string): The city of the Sender.
            country (string): The country of the Sender.
            from_ (object): from
            nickname (string): A nickname for the Sender. Not used for sending.
            reply_to (object): reply_to
            state (string): The state of the Sender.
            zip (string): The zipcode of the Sender.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Senders
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "address": address,
            "address_2": address_2,
            "city": city,
            "country": country,
            "from": from_,
            "nickname": nickname,
            "reply_to": reply_to,
            "state": state,
            "zip": zip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/senders/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def reset_sender_verification(self, id) -> Any:
        """
        Resends a verification email for a specified sender identity using the SendGrid API.

        Args:
            id (string): id

        Returns:
            Any: successfully posted, no response in payload

        Tags:
            Senders
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/senders/{id}/resend_verification"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_single_sends(self, ids=None) -> Any:
        """
        Deletes one or more Single Sends from SendGrid's marketing campaigns by ID, permanently removing them from the system.

        Args:
            ids (array): An array of Single Send IDs specifying which Single Sends to delete.

        Returns:
            Any: API response data.

        Tags:
            Single Sends
        """
        url = f"{self.base_url}/v3/marketing/singlesends"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_single_send(self, page_size=None, page_token=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of all Single Sends (one-time, non-automated email campaigns) with condensed details about each, allowing optional page size and token parameters for result pagination.

        Args:
            page_size (integer): Specifies the number of items to return per page in the response for the paginated list of single sends.
            page_token (string): A token provided in the API response to fetch the next page of results for paginated data, allowing you to continue retrieving subsequent records from the collection.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        url = f"{self.base_url}/v3/marketing/singlesends"
        query_params = {
            k: v
            for k, v in [("page_size", page_size), ("page_token", page_token)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_single_send(
        self, categories=None, email_config=None, name=None, send_at=None, send_to=None
    ) -> dict[str, Any]:
        """
        Creates a new single send email campaign using the provided request data.

        Args:
            categories (array): The categories to associate with this Single Send.
            email_config (object): email_config
            name (string): The name of the Single Send.
            send_at (string): Set this property to an ISO 8601 formatted date-time when you would like to send the Single Send. Please note that any `send_at` property value set with this endpoint will prepopulate the send date in the SendGrid user interface (UI). However, the Single Send will remain an unscheduled draft until it's updated with the [**Schedule Single Send**](https://docs.sendgrid.com/api-reference/single-sends/schedule-single-send) endpoint or SendGrid application UI. Additionally, the `now` keyword is a valid `send_at` value only when using the Schedule Single Send endpoint. Setting this property to `now` with this endpoint will cause an error.
            send_to (object): send_to

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        request_body = {
            "categories": categories,
            "email_config": email_config,
            "name": name,
            "send_at": send_at,
            "send_to": send_to,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/singlesends"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_category(self) -> dict[str, Any]:
        """
        Retrieves a list of the latest 1,000 unique categories associated with all Single Sends in ascending order.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        url = f"{self.base_url}/v3/marketing/singlesends/categories"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_single_send(
        self, page_size=None, page_token=None, categories=None, name=None, status=None
    ) -> dict[str, Any]:
        """
        Searches yielded no direct description of the specific "/v3/marketing/singlesends/search" POST operation, but based on standard REST API and endpoint conventions, this endpoint likely performs a search for single-send marketing campaigns using parameters such as pagination (page_size, page_token) provided in the query and a JSON request body.

        A concise summary for this API operation would be:

        "Searches and retrieves a paginated list of single-send marketing campaigns based on criteria specified in the JSON request body."

        Args:
            page_size (integer): Specifies the number of results to return per page in the search results for single sends.
            page_token (string): A token used to fetch the next page of results in a paginated API request; provide this token from the previous response to continue retrieving subsequent pages.
            categories (array): categories to associate with this Single Send, match any single send that has at least one of the categories
            name (string): leading and trailing wildcard search on name of the Single Send
            status (array): current status of the Single Send

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        request_body = {
            "categories": categories,
            "name": name,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/singlesends/search"
        query_params = {
            k: v
            for k, v in [("page_size", page_size), ("page_token", page_token)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_single_send(self, id) -> Any:
        """
        Deletes a single send marketing campaign identified by the specified ID using the DELETE method.

        Args:
            id (string): id

        Returns:
            Any: API response data.

        Tags:
            Single Sends
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/singlesends/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_single_send(self, id) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific Single Send using its ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/singlesends/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_single_send(
        self,
        id,
        categories=None,
        email_config=None,
        name=None,
        send_at=None,
        send_to=None,
    ) -> dict[str, Any]:
        """
        Modifies an existing single send resource by partially updating its properties using the PATCH method at the "/v3/marketing/singlesends/{id}" endpoint.

        Args:
            id (string): id
            categories (array): The categories to associate with this Single Send.
            email_config (object): email_config
            name (string): The name of the Single Send.
            send_at (string): Set this property to an ISO 8601 formatted date-time when you would like to send the Single Send. Please note that any `send_at` property value set with this endpoint will prepopulate the send date in the SendGrid user interface (UI). However, the Single Send will remain an unscheduled draft until it's updated with the [**Schedule Single Send**](https://docs.sendgrid.com/api-reference/single-sends/schedule-single-send) endpoint or SendGrid application UI. Additionally, the `now` keyword is a valid `send_at` value only when using the Schedule Single Send endpoint. Setting this property to `now` with this endpoint will cause an error.
            send_to (object): send_to

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "categories": categories,
            "email_config": email_config,
            "name": name,
            "send_at": send_at,
            "send_to": send_to,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/singlesends/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_single_send(self, id, name=None) -> dict[str, Any]:
        """
        Creates and returns a new single send email draft in the marketing automation system, optionally setting initial configurations such as send time and template data.

        Args:
            id (string): id
            name (string): The name of the duplicate Single Send. If you choose to leave the name field blank, your duplicate will be assigned the name of the Single Send it was copied from with the text 'Copy of ' prepended to it. The end of the new Single Send name, including 'Copy of ', will be trimmed if the name exceeds the character limit.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/singlesends/{id}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_scheduled_single_send(self, id) -> dict[str, Any]:
        """
        Deletes a scheduled Single Send using the provided Single Send ID, effectively canceling its future delivery.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/singlesends/{id}/schedule"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_single_send(self, id, send_at=None) -> dict[str, Any]:
        """
        Schedules a Single Send email campaign for future delivery by updating its schedule using the specified ID and returns a success status upon completion.

        Args:
            id (string): id
            send_at (string): The ISO 8601 time at which to send the Single Send. This must be in future or the string `now`. SendGrid [Mail Send](https://docs.sendgrid.com/api-reference/mail-send/mail-send) emails can be scheduled up to 72 hours in advance. However, this scheduling constraint does not apply to emails sent via [Marketing Campaigns](https://docs.sendgrid.com/ui/sending-email/how-to-send-email-with-marketing-campaigns/).

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Single Sends
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "send_at": send_at,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/singlesends/{id}/schedule"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_automation_stat(
        self, automation_ids=None, page_size=None, page_token=None
    ) -> dict[str, Any]:
        """
        Retrieves marketing automation statistics for specified automation IDs with support for pagination.

        Args:
            automation_ids (array): Array of automation IDs used to filter the statistics returned for the specified automations.
            page_size (integer): The number of elements you want returned on each page.
            page_token (string): The stats endpoints are paginated. To get the next page, call the passed `_metadata.next` URL. If `_metadata.prev` doesn't exist, you're at the first page. Similarly, if `_metadata.next` is not present, you're at the last page.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/marketing/stats/automations"
        query_params = {
            k: v
            for k, v in [
                ("automation_ids", automation_ids),
                ("page_size", page_size),
                ("page_token", page_token),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def export_automation_stat(self, ids=None, timezone=None) -> Any:
        """
        Exports marketing automation statistics based on the provided ids and timezone.

        Args:
            ids (array): An array of IDs to filter the export of automation marketing statistics.
            timezone (string): Specifies the timezone for exported automation statistics, defaulting to UTC.

        Returns:
            Any: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/marketing/stats/automations/export"
        query_params = {
            k: v for k, v in [("ids", ids), ("timezone", timezone)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_automation_stat(
        self,
        id,
        group_by=None,
        step_ids=None,
        aggregated_by=None,
        start_date=None,
        end_date=None,
        timezone=None,
        page_size=None,
        page_token=None,
    ) -> dict[str, Any]:
        """
        Retrieves detailed statistics for a specific automation identified by its ID, supporting filtering, grouping, date ranges, timezone selection, and pagination.

        Args:
            id (string): id
            group_by (array): Automations can have multiple steps. Including `step_id` as a `group_by` metric allows further granularity of stats.
            step_ids (array): Comma-separated list of `step_ids` that you want the link stats for.
            aggregated_by (string): Dictates how the stats are time-sliced. Currently, `"total"` and `"day"` are supported.
            start_date (string): Format: `YYYY-MM-DD`. If this parameter is included, the stats' start date is included in the search.
            end_date (string): Format: `YYYY-MM-DD`.If this parameter is included, the stats' end date is included in the search.
            timezone (string): [IANA Area/Region](https://en.wikipedia.org/wiki/Tz_database#Names_of_timezones) string representing the timezone in which the stats are to be presented, e.g., "America/Chicago".
            page_size (integer): The number of elements you want returned on each page.
            page_token (string): The stats endpoints are paginated. To get the next page, call the passed `_metadata.next` URL. If `_metadata.prev` doesn't exist, you're at the first page. Similarly, if `_metadata.next` is not present, you're at the last page.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Stats
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/stats/automations/{id}"
        query_params = {
            k: v
            for k, v in [
                ("group_by", group_by),
                ("step_ids", step_ids),
                ("aggregated_by", aggregated_by),
                ("start_date", start_date),
                ("end_date", end_date),
                ("timezone", timezone),
                ("page_size", page_size),
                ("page_token", page_token),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_click_tracking_stat(
        self, id, group_by=None, step_ids=None, page_size=None, page_token=None
    ) -> dict[str, Any]:
        """
        Retrieves and paginates statistics for links contained within a specified automation workflow, optionally grouped or filtered by step.

        Args:
            id (string): id
            group_by (array): Automations can have multiple steps. Including `step_id` as a `group_by` metric allows further granularity of stats.
            step_ids (array): Comma-separated list of `step_ids` that you want the link stats for.
            page_size (integer): The number of elements you want returned on each page.
            page_token (string): The stats endpoints are paginated. To get the next page, call the passed `_metadata.next` URL. If `_metadata.prev` doesn't exist, you're at the first page. Similarly, if `_metadata.next` is not present, you're at the last page.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Stats
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/stats/automations/{id}/links"
        query_params = {
            k: v
            for k, v in [
                ("group_by", group_by),
                ("step_ids", step_ids),
                ("page_size", page_size),
                ("page_token", page_token),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_single_send_stat(
        self, singlesend_ids=None, page_size=None, page_token=None
    ) -> dict[str, Any]:
        """
        Retrieves statistics for single sends identified by the specified IDs, with optional pagination.

        Args:
            singlesend_ids (array): An array of Single Send IDs to filter the statistics retrieved for the GET operation.
            page_size (integer): The number of elements you want returned on each page.
            page_token (string): The stats endpoints are paginated. To get the next page, call the passed `_metadata.next` URL. If `_metadata.prev` doesn't exist, you're at the first page. Similarly, if `_metadata.next` is not present, you're at the last page.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/marketing/stats/singlesends"
        query_params = {
            k: v
            for k, v in [
                ("singlesend_ids", singlesend_ids),
                ("page_size", page_size),
                ("page_token", page_token),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def export_single_send_stat(self, ids=None, timezone=None) -> Any:
        """
        Exports statistics for specified single sends in a downloadable format, with options to filter by IDs and set the timezone for timestamps.

        Args:
            ids (array): Specifies the array of single send IDs to include in the exported marketing stats report.
            timezone (string): Optional timezone for the exported data, defaulting to UTC, allowing specification in a format like "America/New_York" or similar IANA timezone codes.

        Returns:
            Any: API response data.

        Tags:
            Stats
        """
        url = f"{self.base_url}/v3/marketing/stats/singlesends/export"
        query_params = {
            k: v for k, v in [("ids", ids), ("timezone", timezone)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_single_send_stat(
        self,
        id,
        aggregated_by=None,
        start_date=None,
        end_date=None,
        timezone=None,
        page_size=None,
        page_token=None,
        group_by=None,
    ) -> dict[str, Any]:
        """
        Retrieves aggregated marketing statistics for a specific single send campaign, supporting filtering by date, timezone, pagination, and optional grouping.

        Args:
            id (string): id
            aggregated_by (string): Dictates how the stats are time-sliced. Currently, `"total"` and `"day"` are supported.
            start_date (string): Format: `YYYY-MM-DD`. If this parameter is included, the stats' start date is included in the search.
            end_date (string): Format: `YYYY-MM-DD`.If this parameter is included, the stats' end date is included in the search.
            timezone (string): [IANA Area/Region](https://en.wikipedia.org/wiki/Tz_database#Names_of_timezones) string representing the timezone in which the stats are to be presented, e.g., "America/Chicago".
            page_size (integer): The number of elements you want returned on each page.
            page_token (string): The stats endpoints are paginated. To get the next page, call the passed `_metadata.next` URL. If `_metadata.prev` doesn't exist, you're at the first page. Similarly, if `_metadata.next` is not present, you're at the last page.
            group_by (array): A/B Single Sends have multiple variation IDs and phase IDs. Including these additional fields allows further granularity of stats by these fields.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Stats
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/stats/singlesends/{id}"
        query_params = {
            k: v
            for k, v in [
                ("aggregated_by", aggregated_by),
                ("start_date", start_date),
                ("end_date", end_date),
                ("timezone", timezone),
                ("page_size", page_size),
                ("page_token", page_token),
                ("group_by", group_by),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_single_send_tracking_stat(
        self,
        id,
        page_size=None,
        page_token=None,
        group_by=None,
        ab_variation_id=None,
        ab_phase_id=None,
    ) -> dict[str, Any]:
        """
        Retrieves statistics for links in a single send campaign identified by {id}, allowing for pagination and filtering by group by, variation ID, and phase ID.

        Args:
            id (string): id
            page_size (integer): The number of elements you want returned on each page.
            page_token (string): The stats endpoints are paginated. To get the next page, call the passed `_metadata.next` URL. If `_metadata.prev` doesn't exist, you're at the first page. Similarly, if `_metadata.next` is not present, you're at the last page.
            group_by (array): A/B Single Sends have multiple variation IDs and phase IDs. Including these additional fields allows further granularity of stats by these fields.
            ab_variation_id (string): No description provided.
            ab_phase_id (string): No description provided.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Stats
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/marketing/stats/singlesends/{id}/links"
        query_params = {
            k: v
            for k, v in [
                ("page_size", page_size),
                ("page_token", page_token),
                ("group_by", group_by),
                ("ab_variation_id", ab_variation_id),
                ("ab_phase_id", ab_phase_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_test_marketing_email(
        self,
        custom_unsubscribe_url=None,
        emails=None,
        from_address=None,
        sender_id=None,
        suppression_group_id=None,
        template_id=None,
        version_id_override=None,
    ) -> dict[str, Any]:
        """
        Sends an email for marketing testing purposes using the provided JSON data and returns a success status when processed successfully.

        Args:
            custom_unsubscribe_url (string): A custom unsubscribe URL.
            emails (array): An array of email addresses you want to send the test message to.
            from_address (string): You can either specify this address or specify a verified sender ID.
            sender_id (integer): This ID must belong to a verified sender. Alternatively, you may supply a `from_address` email.
            suppression_group_id (integer): suppression_group_id
            template_id (string): The ID of the template that you would like to use. If you use a template that contains a subject and content (either text or HTML), then those values specified at the personalizations or message level will not be used.
            version_id_override (string):  You can override the active template with an alternative template version by passing the version ID in this field. If this field is blank, the active template version will be used.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Send Test Email
        """
        request_body = {
            "custom_unsubscribe_url": custom_unsubscribe_url,
            "emails": emails,
            "from_address": from_address,
            "sender_id": sender_id,
            "suppression_group_id": suppression_group_id,
            "template_id": template_id,
            "version_id_override": version_id_override,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/marketing/test/send_email"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_message(self, query, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of messages based on a query string, optionally limited by a specified number of results.

        Args:
            query (string): A string parameter used to filter or search messages in the GET operation at /v3/messages.
            limit (number): Specifies the maximum number of messages to return in the response, with a default value of 10.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Email Activity
        """
        url = f"{self.base_url}/v3/messages"
        query_params = {
            k: v for k, v in [("query", query), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def request_csv(self, query=None) -> dict[str, Any]:
        """
        Downloads messages using the provided query parameters and returns a successful response upon completion.

        Args:
            query (string): Optional search string to filter or specify criteria for downloading messages.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Email Activity
        """
        url = f"{self.base_url}/v3/messages/download"
        query_params = {k: v for k, v in [("query", query)] if v is not None}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def download_csv(self, download_uuid) -> dict[str, Any]:
        """
        Downloads a message file identified by the provided download UUID using the GET method.

        Args:
            download_uuid (string): download_uuid

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Email Activity
        """
        if download_uuid is None:
            raise ValueError("Missing required parameter 'download_uuid'")
        url = f"{self.base_url}/v3/messages/download/{download_uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_message(self, msg_id) -> dict[str, Any]:
        """
        Retrieves details of a specific message by its ID using the "GET" method at the "/v3/messages/{msg_id}" path.

        Args:
            msg_id (string): msg_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Email Activity
        """
        if msg_id is None:
            raise ValueError("Missing required parameter 'msg_id'")
        url = f"{self.base_url}/v3/messages/{msg_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_partner_setting(self, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of partner settings with support for limiting and offsetting results.

        Args:
            limit (integer): **limit** (integer): Specifies the maximum number of results to be included in the API response for the /v3/partner_settings GET operation.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Partner Settings
        """
        url = f"{self.base_url}/v3/partner_settings"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_account(self, offerings, profile=None) -> dict[str, Any]:
        """
        Creates a new partner account using the provided JSON data and returns a "201 Created" response upon success.

        Args:
            offerings (array): List of offering names to assign to account.
            profile (object): profile
                Example:
                ```json
                {
                  "offerings": [
                    {
                      "name": "org.ei.free.v1",
                      "quantity": 1,
                      "type": "package"
                    }
                  ],
                  "profile": {
                    "company_name": "Twilio SendGrid",
                    "company_website": "https://sendgrid.com",
                    "email": "test@test.com",
                    "first_name": "Sender",
                    "last_name": "Wiz",
                    "timezone": "Asia/Tokyo"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            Account
        """
        request_body = {
            "offerings": offerings,
            "profile": profile,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/partners/accounts"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_account(self, accountID) -> Any:
        """
        Deletes a partner account identified by the specified `accountID` using the DELETE method, returning a 204 status on success.

        Args:
            accountID (string): accountID

        Returns:
            Any: Account successfully deleted.

        Tags:
            Account
        """
        if accountID is None:
            raise ValueError("Missing required parameter 'accountID'")
        url = f"{self.base_url}/v3/partners/accounts/{accountID}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_account_offering(self, accountID) -> dict[str, Any]:
        """
        Retrieves a list of offerings associated with a specific partner account using the account ID.

        Args:
            accountID (string): accountID

        Returns:
            dict[str, Any]: OK

        Tags:
            Offering
        """
        if accountID is None:
            raise ValueError("Missing required parameter 'accountID'")
        url = f"{self.base_url}/v3/partners/accounts/{accountID}/offerings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_account_offering(self, accountID, offerings) -> dict[str, Any]:
        """
        Updates an existing offering for a specific account using the "PUT" method, sending the updated offering details in JSON format to the "/v3/partners/accounts/{accountID}/offerings" endpoint.

        Args:
            accountID (string): accountID
            offerings (array): List of offerings to assign to account.
                Example:
                ```json
                {
                  "offerings": [
                    {
                      "name": "org.ei.free.v1",
                      "quantity": 1,
                      "type": "package"
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            Offering
        """
        if accountID is None:
            raise ValueError("Missing required parameter 'accountID'")
        request_body = {
            "offerings": offerings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/partners/accounts/{accountID}/offerings"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def authenticate_account(self, accountID) -> Any:
        """
        Initiates a single sign-on (SSO) process for the specified partner account identified by accountID.

        Args:
            accountID (string): accountID

        Returns:
            Any: API response data.

        Tags:
            Account
        """
        if accountID is None:
            raise ValueError("Missing required parameter 'accountID'")
        url = f"{self.base_url}/v3/partners/accounts/{accountID}/sso"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_account_state(self, accountID) -> dict[str, Any]:
        """
        Retrieves the current state information of a partner account identified by the specified accountID.

        Args:
            accountID (string): accountID

        Returns:
            dict[str, Any]: OK

        Tags:
            Account State
        """
        if accountID is None:
            raise ValueError("Missing required parameter 'accountID'")
        url = f"{self.base_url}/v3/partners/accounts/{accountID}/state"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_account_state(self, accountID, state) -> Any:
        """
        Updates the state of a partner account using JSON data and returns a status code indicating success or failure.

        Args:
            accountID (string): accountID
            state (string): state

        Returns:
            Any: State successfully updated

        Tags:
            Account State
        """
        if accountID is None:
            raise ValueError("Missing required parameter 'accountID'")
        request_body = {
            "state": state,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/partners/accounts/{accountID}/state"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_offering(self) -> dict[str, Any]:
        """
        Retrieves a list of offerings for partners using the GET method at the "/v3/partners/offerings" path.

        Returns:
            dict[str, Any]: OK

        Tags:
            Offering
        """
        url = f"{self.base_url}/v3/partners/offerings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def erase_recipient_email_data(self, email_addresses) -> dict[str, Any]:
        """
        Initiates an erase job for recipients using the provided JSON data in the request body and returns a status message.

        Args:
            email_addresses (array): List of unique recipient email addresses whose PII will be erased. You may include a maximum of 5,000 addresses or a maximum payload size of 256Kb, whichever comes first.
                Example:
                ```json
                {
                  "email_addresses": [
                    "user1@example.com",
                    "user2@example.com"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: The request was accepted for processing

        Tags:
            Point Delete System
        """
        request_body = {
            "email_addresses": email_addresses,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/recipients/erasejob"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_scope(self) -> dict[str, Any]:
        """
        Retrieves a list of authentication scopes using the GitHub API.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Scopes
        """
        url = f"{self.base_url}/v3/scopes"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_scope_request(self, limit=None, offset=None) -> list[Any]:
        """
        Retrieves a list of scope requests using the "GET" method, allowing optional parameters for pagination and limit.

        Args:
            limit (integer): Specifies the maximum number of request records to return per API call, with a default value of 50.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.

        Returns:
            list[Any]: API response data.

        Tags:
            Scopes
        """
        url = f"{self.base_url}/v3/scopes/requests"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deny_scope_request(self, request_id) -> Any:
        """
        Deletes a scope request with the specified request ID using the GitHub API and returns a status message if successful.

        Args:
            request_id (string): request_id

        Returns:
            Any: API response data.

        Tags:
            Scopes
        """
        if request_id is None:
            raise ValueError("Missing required parameter 'request_id'")
        url = f"{self.base_url}/v3/scopes/requests/{request_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def approve_scope_request(self, request_id) -> dict[str, Any]:
        """
        Approves a pending scope request with the specified `request_id` using the GitHub API and returns a status message.

        Args:
            request_id (string): request_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Scopes
        """
        if request_id is None:
            raise ValueError("Missing required parameter 'request_id'")
        url = f"{self.base_url}/v3/scopes/requests/{request_id}/approve"
        query_params = {}
        response = self._patch(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_ip(
        self,
        ip=None,
        limit=None,
        after_key=None,
        before_key=None,
        is_leased=None,
        is_enabled=None,
        is_parent_assigned=None,
        pool=None,
        start_added_at=None,
        end_added_at=None,
        region=None,
        include_region=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of IP addresses based on specified query parameters, including filtering by lease status, enabled status, pool assignment, and other criteria.

        Args:
            ip (string): Specifies an IP address. The `ip` query parameter can be used to filter results by IP address.
            limit (integer): Specifies the number of results to be returned by the API. This parameter can be used in combination with the `before_key` or `after_key` parameters to iterate through paginated results.
            after_key (integer): Specifies which items to be returned by the API. When the `after_key` is specified, the API will return items beginning from the first item after the item specified. This parameter can be used in combination with `limit` to iterate through paginated results.
            before_key (string): Specifies which items to be returned by the API. When the `before_key` is specified, the API will return items beginning from the first item before the item specified. This parameter can be used in combination with `limit` to iterate through paginated results.
            is_leased (boolean): Indicates whether an IP address is leased from Twilio SendGrid. If `false`, the IP address is not a Twilio SendGrid IP; it is a customer's own IP that has been added to their Twilio SendGrid account.
            is_enabled (boolean): Indicates if the IP address is billed and able to send email. This parameter applies to non-Twilio SendGrid APIs that been added to your Twilio SendGrid account. This parameter's value is `null` for Twilio SendGrid IP addresses.
            is_parent_assigned (boolean): A parent must be assigned to an IP address before the parent can send mail from the IP and before the address can be assigned to an IP pool. Set this parameter value to true to allow the parent to send mail from the IP and make the IP eligible for IP pool assignment using the IP pool endpoints.
            pool (string): Specifies the unique ID for an IP Pool. When included, only IP addresses belonging to the specified Pool will be returned.
            start_added_at (integer): The `start_added_at` and `end_added_at` parameters are used to set a time window. IP addresses that were added to your account in the specified time window will be returned. The `start_added_at` parameter sets the beginning of the time window.
            end_added_at (integer): The `start_added_at` and `end_added_at` parameters are used to set a time window. IP addresses that were added to your account in the specified time window will be returned. The `end_added_at` parameter sets the end of the time window.
            region (string): Allowed values are `all`, `eu`, and `us`. If you provide a specific region, results will include all pools that have at least one IP in the filtered region. If `all`, pools with at least one IP (regardless of region) will be returned. If the `region` filter is not provided, the query returns all pools, including empty ones.
            include_region (boolean): Boolean indicating whether or not to return the IP Pool's region information in the response.

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        url = f"{self.base_url}/v3/send_ips/ips"
        query_params = {
            k: v
            for k, v in [
                ("ip", ip),
                ("limit", limit),
                ("after_key", after_key),
                ("before_key", before_key),
                ("is_leased", is_leased),
                ("is_enabled", is_enabled),
                ("is_parent_assigned", is_parent_assigned),
                ("pool", pool),
                ("start_added_at", start_added_at),
                ("end_added_at", end_added_at),
                ("region", region),
                ("include_region", include_region),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_ip(
        self,
        include_region=None,
        is_auto_warmup=None,
        is_parent_assigned=None,
        region=None,
        subusers=None,
    ) -> dict[str, Any]:
        """
        Submits a list of IP addresses using a JSON payload via the POST method to the "/v3/send_ips/ips" endpoint, returning a success status code upon completion.

        Args:
            include_region (boolean): Boolean indicating whether or not to return the IP address's region information in the response.
            is_auto_warmup (boolean): Indicates if the IP address is set to automatically [warmup](https://docs.sendgrid.com/ui/sending-email/warming-up-an-ip-address).
            is_parent_assigned (boolean): Indicates if a parent on the account is able to send email from the IP address.
            region (string): region
            subusers (array): An array of Subuser IDs the IP address will be assigned to.
                Example:
                ```json
                {
                  "is_auto_warmup": true,
                  "is_parent_assigned": true,
                  "subusers": [
                    "12345"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            IP Address Management
        """
        request_body = {
            "include_region": include_region,
            "is_auto_warmup": is_auto_warmup,
            "is_parent_assigned": is_parent_assigned,
            "region": region,
            "subusers": subusers,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/send_ips/ips"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ip(self, ip, include_region=None) -> dict[str, Any]:
        """
        Retrieves detailed information for a specified IP address, including assignment status, associated pools, and optional region details.

        Args:
            ip (string): ip
            include_region (boolean): Boolean indicating whether or not to return the IP Pool's region information in the response.

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        if ip is None:
            raise ValueError("Missing required parameter 'ip'")
        url = f"{self.base_url}/v3/send_ips/ips/{ip}"
        query_params = {
            k: v for k, v in [("include_region", include_region)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_ip(
        self, ip, is_auto_warmup=None, is_enabled=None, is_parent_assigned=None
    ) -> dict[str, Any]:
        """
        Partially updates the IP resource at the specified path "/v3/send_ips/ips/{ip}" using a JSON payload to modify specific properties.

        Args:
            ip (string): ip
            is_auto_warmup (boolean): Indicates if the IP address is set to automatically [warmup](https://docs.sendgrid.com/ui/sending-email/warming-up-an-ip-address).
            is_enabled (boolean): Indicates if the IP address is billed and able to send email. This parameter applies to non-Twilio SendGrid APIs that been added to your Twilio SendGrid account. This parameter's value is `null` for Twilio SendGrid IP addresses.
            is_parent_assigned (boolean): Indicates if a parent on the account is able to send email from the IP address.
                Example:
                ```json
                {
                  "is_auto_warmup": true,
                  "is_enabled": true,
                  "is_parent_assigned": true
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        if ip is None:
            raise ValueError("Missing required parameter 'ip'")
        request_body = {
            "is_auto_warmup": is_auto_warmup,
            "is_enabled": is_enabled,
            "is_parent_assigned": is_parent_assigned,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/send_ips/ips/{ip}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_sub_user_assigned_to_ip(
        self, ip, after_key=None, limit=None
    ) -> dict[str, Any]:
        """
        Retrieves information about subusers associated with a specified IP address, allowing optional filtering by a limit parameter.

        Args:
            ip (string): ip
            after_key (integer): Specifies which items to be returned by the API. When the `after_key` is specified, the API will return items beginning from the first item after the item specified. This parameter can be used in combination with `limit` to iterate through paginated results.
            limit (integer): Specifies the maximum number of subusers to return in the response for the given IP address.

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        if ip is None:
            raise ValueError("Missing required parameter 'ip'")
        url = f"{self.base_url}/v3/send_ips/ips/{ip}/subusers"
        query_params = {
            k: v
            for k, v in [("after_key", after_key), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_sub_users_to_ip(self, ip, subusers=None) -> dict[str, Any]:
        """
        Adds multiple subusers to a specific IP address in a single batch operation using the provided data in the request body.

        Args:
            ip (string): ip
            subusers (array): An array of Subuser IDs to be assigned to the specified IP address. All Subuser assignments must succeed.
                Example:
                ```json
                {
                  "subusers": [
                    "12345",
                    "67890"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        if ip is None:
            raise ValueError("Missing required parameter 'ip'")
        request_body = {
            "subusers": subusers,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/send_ips/ips/{ip}/subusers:batchAdd"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_sub_users_from_ip(self, ip, subusers=None) -> Any:
        """
        Deletes multiple subusers associated with a specified IP address in a single batch operation, supporting various response status codes including success (204), bad request (400), unauthorized (401), and server error (500).

        Args:
            ip (string): ip
            subusers (array): An array of Subuser IDs to be removed from the specified IP address.
                Example:
                ```json
                {
                  "subusers": [
                    "12345",
                    "67890"
                  ]
                }
                ```

        Returns:
            Any: No Content

        Tags:
            IP Address Management
        """
        if ip is None:
            raise ValueError("Missing required parameter 'ip'")
        request_body = {
            "subusers": subusers,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/send_ips/ips/{ip}/subusers:batchDelete"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_ip_pool(self, ips=None, name=None) -> dict[str, Any]:
        """
        Creates IP pools using a JSON payload and returns a successful creation status upon completion.

        Args:
            ips (array): An array of IP addresses to assign to the IP Pool. All assignments must succeed.
            name (string): The name to assign to the IP Pool. An IP Pool name cannot begin with a space or period.
                Example:
                ```json
                {
                  "ips": [
                    "127.0.0.1",
                    "127.0.0.2"
                  ],
                  "name": "transactional_pool"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            IP Address Management
        """
        request_body = {
            "ips": ips,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/send_ips/pools"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_ip_pool(self, poolid) -> Any:
        """
        Deletes a specific IP pool identified by the {poolid} using the DELETE method, returning a 204 No Content response upon successful deletion.

        Args:
            poolid (string): poolid

        Returns:
            Any: No Content

        Tags:
            IP Address Management
        """
        if poolid is None:
            raise ValueError("Missing required parameter 'poolid'")
        url = f"{self.base_url}/v3/send_ips/pools/{poolid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ip_pool(self, poolid, include_region=None) -> dict[str, Any]:
        """
        Retrieves details for a specified IP pool, including its name, ID, and a sample list of associated IP addresses[1].

        Args:
            poolid (string): poolid
            include_region (boolean): Boolean indicating whether or not to return the IP Pool's region information in the response.

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        if poolid is None:
            raise ValueError("Missing required parameter 'poolid'")
        url = f"{self.base_url}/v3/send_ips/pools/{poolid}"
        query_params = {
            k: v for k, v in [("include_region", include_region)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_ip_pool(self, poolid, name=None) -> dict[str, Any]:
        """
        Updates a specified IP pool using the provided JSON data and returns a status message.

        Args:
            poolid (string): poolid
            name (string): The name to assign to the IP Pool. An IP Pool name cannot begin with a space or period.
                Example:
                ```json
                {
                  "name": "marketing_pool"
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        if poolid is None:
            raise ValueError("Missing required parameter 'poolid'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/send_ips/pools/{poolid}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_ip_assigned_to_ip_pool(
        self, poolid, limit=None, after_key=None, include_region=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of IP addresses within a specified pool, optionally including region information and limited by a specified after key.

        Args:
            poolid (string): poolid
            limit (integer): Specifies the number of results to be returned by the API. This parameter can be used in combination with the `before_key` or `after_key` parameters to iterate through paginated results.
            after_key (integer): Specifies which items to be returned by the API. When the `after_key` is specified, the API will return items beginning from the first item after the item specified. This parameter can be used in combination with `limit` to iterate through paginated results.
            include_region (boolean): Boolean indicating whether or not to return the IP Pool's region information in the response.

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        if poolid is None:
            raise ValueError("Missing required parameter 'poolid'")
        url = f"{self.base_url}/v3/send_ips/pools/{poolid}/ips"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after_key", after_key),
                ("include_region", include_region),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_ips_to_ip_pool(self, poolid, ips=None) -> dict[str, Any]:
        """
        Adds multiple IP addresses to a pool using a batch operation via the POST method.

        Args:
            poolid (string): poolid
            ips (array): An array of IP addresses to assign to the specified IP Pool. All assignments must succeed.
                Example:
                ```json
                {
                  "ips": [
                    "127.0.0.1",
                    "127.0.0.2",
                    "127.0.0.3",
                    "127.0.0.4"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: OK

        Tags:
            IP Address Management
        """
        if poolid is None:
            raise ValueError("Missing required parameter 'poolid'")
        request_body = {
            "ips": ips,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/send_ips/pools/{poolid}/ips:batchAdd"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_ips_from_ip_pool(self, poolid, ips=None) -> Any:
        """
        Deletes multiple IP addresses in a specified pool using the POST method with a JSON body containing IP details and returns a status message based on the response codes 204, 400, 401, or 500.

        Args:
            poolid (string): poolid
            ips (array): An array of IP addresses to remove from the specified IP Pool.
                Example:
                ```json
                {
                  "ips": [
                    "127.0.0.1",
                    "127.0.0.2",
                    "127.0.0.3",
                    "127.0.0.4"
                  ]
                }
                ```

        Returns:
            Any: No Content

        Tags:
            IP Address Management
        """
        if poolid is None:
            raise ValueError("Missing required parameter 'poolid'")
        request_body = {
            "ips": ips,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/send_ips/pools/{poolid}/ips:batchDelete"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_sender(self) -> dict[str, Any]:
        """
        Retrieves a list of senders using the API endpoint at "/v3/senders" with the "GET" method, potentially operating on behalf of another entity.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Sender Identities
        """
        url = f"{self.base_url}/v3/senders"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_sso_certificate(
        self, enabled=None, integration_id=None, public_certificate=None
    ) -> dict[str, Any]:
        """
        Creates a new SSO certificate using the provided JSON data, enabling Single Sign-On configurations between an Identity Provider (IdP) and a service.

        Args:
            enabled (boolean): Indicates if the certificate is enabled.
            integration_id (string): An ID that matches a certificate to a specific IdP integration. This is the `id` returned by the "Get All SSO Integrations" endpoint.
            public_certificate (string): This public certificate allows SendGrid to verify that SAML requests it receives are signed by an IdP that it recognizes.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Certificates
        """
        request_body = {
            "enabled": enabled,
            "integration_id": integration_id,
            "public_certificate": public_certificate,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/sso/certificates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_sso_certificate(self, cert_id) -> dict[str, Any]:
        """
        Deletes a certificate with the specified ID from the system using the "DELETE" method, returning appropriate status codes based on the operation's success or failure.

        Args:
            cert_id (string): cert_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Certificates
        """
        if cert_id is None:
            raise ValueError("Missing required parameter 'cert_id'")
        url = f"{self.base_url}/v3/sso/certificates/{cert_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sso_certificate(self, cert_id) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific SSO certificate identified by the given certificate ID.

        Args:
            cert_id (string): cert_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Certificates
        """
        if cert_id is None:
            raise ValueError("Missing required parameter 'cert_id'")
        url = f"{self.base_url}/v3/sso/certificates/{cert_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_sso_certificate(
        self, cert_id, enabled=None, integration_id=None, public_certificate=None
    ) -> dict[str, Any]:
        """
        Updates an existing SSO certificate identified by its certificate ID and returns the updated certificate details in the response.

        Args:
            cert_id (string): cert_id
            enabled (boolean): Indicates whether or not the certificate is enabled.
            integration_id (string): An ID that matches a certificate to a specific IdP integration.
            public_certificate (string): This public certificate allows SendGrid to verify that SAML requests it receives are signed by an IdP that it recognizes.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Certificates
        """
        if cert_id is None:
            raise ValueError("Missing required parameter 'cert_id'")
        request_body = {
            "enabled": enabled,
            "integration_id": integration_id,
            "public_certificate": public_certificate,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/sso/certificates/{cert_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_sso_integration(self, si=None) -> list[Any]:
        """
        Retrieves Single Sign-On (SSO) integrations using the API, optionally filtering by a specified condition with the "si" query parameter.

        Args:
            si (boolean): Determines whether to include specific integration details, with true enabling the feature and false disabling it.

        Returns:
            list[Any]: API response data.

        Tags:
            SSO Settings
        """
        url = f"{self.base_url}/v3/sso/integrations"
        query_params = {k: v for k, v in [("si", si)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_sso_integration(
        self,
        completed_integration=None,
        enabled=None,
        entity_id=None,
        name=None,
        signin_url=None,
        signout_url=None,
    ) -> dict[str, Any]:
        """
        Creates a new Single Sign-On (SSO) integration using the provided details, returning a status message indicating the outcome of the operation.

        Args:
            completed_integration (boolean): Indicates if the integration is complete.
            enabled (boolean): Indicates if the integration is enabled.
            entity_id (string): An identifier provided by your IdP to identify Twilio SendGrid in the SAML interaction. This is called the "SAML Issuer ID" in the Twilio SendGrid UI.
            name (string): The name of your integration. This name can be anything that makes sense for your organization (eg. Twilio SendGrid)
            signin_url (string): The IdP's SAML POST endpoint. This endpoint should receive requests and initiate an SSO login flow. This is called the "Embed Link" in the Twilio SendGrid UI.
            signout_url (string): This URL is relevant only for an IdP-initiated authentication flow. If a user authenticates from their IdP, this URL will return them to their IdP when logging out.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Settings
        """
        request_body = {
            "completed_integration": completed_integration,
            "enabled": enabled,
            "entity_id": entity_id,
            "name": name,
            "signin_url": signin_url,
            "signout_url": signout_url,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/sso/integrations"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_sso_integration(self, id) -> Any:
        """
        Deletes a specified SSO integration and returns a successful status with no content upon completion.

        Args:
            id (string): id

        Returns:
            Any: API response data.

        Tags:
            SSO Settings
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/sso/integrations/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sso_integration(self, id, si=None) -> dict[str, Any]:
        """
        Retrieves details about a specific SSO integration identified by {id} using the GET method, with an optional query parameter "si" for additional filtering or inclusion.

        Args:
            id (string): id
            si (boolean): Indicates whether to perform a specific operation or enable a feature in the integration, with true enabling it and false disabling it.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Settings
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/sso/integrations/{id}"
        query_params = {k: v for k, v in [("si", si)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_sso_integration(
        self,
        id,
        si=None,
        completed_integration=None,
        enabled=None,
        entity_id=None,
        name=None,
        signin_url=None,
        signout_url=None,
    ) -> dict[str, Any]:
        """
        Updates an existing single sign-on integration identified by {id} at path "/v3/sso/integrations/{id}" using the "PATCH" method.

        Args:
            id (string): id
            si (boolean): A boolean query parameter indicating whether the specified condition is applied during the PATCH operation at /v3/sso/integrations/{id}.
            completed_integration (boolean): Indicates if the integration is complete.
            enabled (boolean): Indicates if the integration is enabled.
            entity_id (string): An identifier provided by your IdP to identify Twilio SendGrid in the SAML interaction. This is called the "SAML Issuer ID" in the Twilio SendGrid UI.
            name (string): The name of your integration. This name can be anything that makes sense for your organization (eg. Twilio SendGrid)
            signin_url (string): The IdP's SAML POST endpoint. This endpoint should receive requests and initiate an SSO login flow. This is called the "Embed Link" in the Twilio SendGrid UI.
            signout_url (string): This URL is relevant only for an IdP-initiated authentication flow. If a user authenticates from their IdP, this URL will return them to their IdP when logging out.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Settings
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "completed_integration": completed_integration,
            "enabled": enabled,
            "entity_id": entity_id,
            "name": name,
            "signin_url": signin_url,
            "signout_url": signout_url,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/sso/integrations/{id}"
        query_params = {k: v for k, v in [("si", si)] if v is not None}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_sso_integration_certificate(self, integration_id) -> list[Any]:
        """
        Retrieves information about certificates associated with a specific SSO integration identified by the `integration_id`.

        Args:
            integration_id (string): integration_id

        Returns:
            list[Any]: API response data.

        Tags:
            SSO Certificates
        """
        if integration_id is None:
            raise ValueError("Missing required parameter 'integration_id'")
        url = f"{self.base_url}/v3/sso/integrations/{integration_id}/certificates"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_sso_teammate(
        self,
        email=None,
        first_name=None,
        has_restricted_subuser_access=None,
        is_admin=None,
        last_name=None,
        persona=None,
        scopes=None,
        subuser_access=None,
    ) -> dict[str, Any]:
        """
        Adds team members using single sign-on (SSO) and returns a status message upon successful addition.

        Args:
            email (string): Set this property to the Teammate's email address. This email address will also function as the Teammate's username and must match the address assigned to the user in your IdP. This address cannot be changed after the Teammate is created.
            first_name (string): Set this property to the Teammate's first name.
            has_restricted_subuser_access (boolean): Set this property to `true` to give the Teammate permissions to operate only on behalf of a Subuser. This property value must be `true` if the `subuser_access` property is not empty. The `subuser_access` property determines which Subusers the Teammate may act on behalf of. If this property is set to `true`, you cannot specify individual `scopes`, assign a `persona`, or set `is_admin` to `true`—a Teammate cannot specify scopes for the parent account and have restricted Subuser access.
            is_admin (boolean): Set this property to `true` if the Teammate has admin permissions. You should not include the `scopes` or `persona` properties when setting the `is_admin` property to `true`—an admin will be allocated all scopes. See [**Teammate Permissions**](https://docs.sendgrid.com/ui/account-and-settings/teammate-permissions) for a complete list of scopes.
            last_name (string): Set this property to the Teammate's last name.
            persona (string): persona
            scopes (array): Add or remove permissions from a Teammate using this `scopes` property. See [**Teammate Permissions**](https://docs.sendgrid.com/ui/account-and-settings/teammate-permissions) for a complete list of available scopes. You should not include this propety in the request when using the `persona` property or when setting the `is_admin` property to `true`—assigning a `persona` or setting `is_admin` to `true` will allocate a group of permissions to the Teammate.
            subuser_access (array): Specify which Subusers the Teammate may access and act on behalf of with this property. If this property is populated, you must set the `has_restricted_subuser_access` property to `true`.
                Example:
                ```json
                {
                  "email": "jane_doe@example.com",
                  "first_name": "Jane",
                  "has_restricted_subuser_access": false,
                  "is_admin": true,
                  "last_name": "Doe"
                }
                ```

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Teammates
        """
        request_body = {
            "email": email,
            "first_name": first_name,
            "has_restricted_subuser_access": has_restricted_subuser_access,
            "is_admin": is_admin,
            "last_name": last_name,
            "persona": persona,
            "scopes": scopes,
            "subuser_access": subuser_access,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/sso/teammates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_sso_teammate(
        self,
        username,
        first_name=None,
        has_restricted_subuser_access=None,
        is_admin=None,
        last_name=None,
        persona=None,
        scopes=None,
        subuser_access=None,
    ) -> dict[str, Any]:
        """
        Updates the team membership or role of a specified user in a team using their username, supporting various permission checks and returning appropriate status codes.

        Args:
            username (string): username
            first_name (string): Set this property to the Teammate's first name.
            has_restricted_subuser_access (boolean): Set this property to `true` to give the Teammate permissions to operate only on behalf of a Subuser. This property value must be `true` if the `subuser_access` property is not empty. The `subuser_access` property determines which Subusers the Teammate may act on behalf of. If this property is set to `true`, you cannot specify individual `scopes`, assign a `persona`, or set `is_admin` to `true`—a Teammate cannot specify scopes for the parent account and have restricted Subuser access.
            is_admin (boolean): Set this property to `true` if the Teammate has admin permissions. You should not include the `scopes` or `persona` properties when setting the `is_admin` property to `true`—an admin will be allocated all scopes. See [**Teammate Permissions**](https://docs.sendgrid.com/ui/account-and-settings/teammate-permissions) for a complete list of scopes.
            last_name (string): Set this property to the Teammate's last name.
            persona (string): persona
            scopes (array): Add or remove permissions from a Teammate using this `scopes` property. See [**Teammate Permissions**](https://docs.sendgrid.com/ui/account-and-settings/teammate-permissions) for a complete list of available scopes. You should not include this propety in the request when using the `persona` property or when setting the `is_admin` property to `true`—assigning a `persona` or setting `is_admin` to `true` will allocate a group of permissions to the Teammate.
            subuser_access (array): Specify which Subusers the Teammate may access and act on behalf of with this property. If this property is populated, you must set the `has_restricted_subuser_access` property to `true`.
                Example:
                ```json
                {
                  "first_name": "Jane",
                  "has_restricted_subuser_access": false,
                  "is_admin": true,
                  "last_name": "Doe"
                }
                ```

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SSO Teammates
        """
        if username is None:
            raise ValueError("Missing required parameter 'username'")
        request_body = {
            "first_name": first_name,
            "has_restricted_subuser_access": has_restricted_subuser_access,
            "is_admin": is_admin,
            "last_name": last_name,
            "persona": persona,
            "scopes": scopes,
            "subuser_access": subuser_access,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/sso/teammates/{username}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_subuser(
        self, username=None, limit=None, region=None, include_region=None, offset=None
    ) -> list[Any]:
        """
        Retrieves a list of subusers for a given username, allowing filtering by region and customization of the response through pagination and optional inclusion of the region.

        Args:
            username (string): Filters the list of subusers to only include those with the specified username.
            limit (integer): Specifies the maximum number of results to return in the response for the GET operation at /v3/subusers.
            region (string): The "region" parameter is a string that filters results by geographic region, with a default value of "all" if not specified.
            include_region (boolean): Specifies whether to include region information with each returned subuser; defaults to false.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.

        Returns:
            list[Any]: API response data.

        Tags:
            Subusers
        """
        url = f"{self.base_url}/v3/subusers"
        query_params = {
            k: v
            for k, v in [
                ("username", username),
                ("limit", limit),
                ("region", region),
                ("include_region", include_region),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_subuser(
        self,
        email=None,
        include_region=None,
        ips=None,
        password=None,
        region=None,
        username=None,
    ) -> dict[str, Any]:
        """
        Creates a new subuser using the GitHub API and returns a response based on the request's outcome.

        Args:
            email (string): The email address of the subuser.
            include_region (boolean): A flag that determines if the Subuser's region should be returned in the response. (Regional email is in Public Beta and requires SendGrid Pro plan or above.)
            ips (array): The IP addresses that should be assigned to this subuser.
            password (string): The password this subuser will use when logging into SendGrid.
            region (string): region
            username (string): The username for this subuser.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subusers
        """
        request_body = {
            "email": email,
            "include_region": include_region,
            "ips": ips,
            "password": password,
            "region": region,
            "username": username,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/subusers"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_reputation(self, usernames=None) -> list[Any]:
        """
        Retrieves the reputation information for specified usernames using the GET method.

        Args:
            usernames (string): Filter the subusers' reputations by specifying one or more usernames in this query parameter.

        Returns:
            list[Any]: API response data.

        Tags:
            Subusers
        """
        url = f"{self.base_url}/v3/subusers/reputations"
        query_params = {k: v for k, v in [("usernames", usernames)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_stat(
        self,
        subusers,
        start_date,
        limit=None,
        offset=None,
        aggregated_by=None,
        end_date=None,
    ) -> list[Any]:
        """
        Retrieves statistical data for specified subusers within a defined time period, allowing for optional filtering by date range, aggregation method, and pagination control.

        Args:
            subusers (string): A required string parameter specifying which subusers to include in the statistics retrieval.
            start_date (string): Specifies the earliest date from which to retrieve subuser statistics, in a supported string format (e.g., YYYY-MM-DD).
            limit (integer): Specifies the maximum number of results to include in the response for the subuser statistics.
            offset (integer): Specifies the number of items to skip from the beginning of the collection when retrieving subuser statistics.
            aggregated_by (string): An optional string parameter to specify the field by which the statistics should be aggregated, allowing for grouped results.
            end_date (string): Optional query parameter to specify the end date for retrieving subuser statistics; should be in a string format.

        Returns:
            list[Any]: API response data.

        Tags:
            Subuser Statistics
        """
        url = f"{self.base_url}/v3/subusers/stats"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("aggregated_by", aggregated_by),
                ("subusers", subusers),
                ("start_date", start_date),
                ("end_date", end_date),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_monthly_stat(
        self,
        date,
        subuser=None,
        sort_by_metric=None,
        sort_by_direction=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves and returns monthly statistics for subusers, filterable by date and customizable with sorting, pagination, and subuser selection.

        Args:
            date (string): The date parameter specifies the month (in ISO 8601 format, e.g., "YYYY-MM") for which to retrieve monthly statistics for subusers.
            subuser (string): Specifies the subuser whose monthly statistics should be retrieved; if omitted, data for all subusers is returned.
            sort_by_metric (string): Optional string parameter to specify the metric by which to sort the subuser monthly statistics, with a default value of "delivered".
            sort_by_direction (string): Specifies the direction for sorting results, accepting string values like "asc" or "desc", with "desc" as the default.
            limit (integer): Limits the number of monthly statistics records returned in the response, with a default of 5 records.
            offset (integer): Specifies the starting point for retrieving monthly subuser statistics, excluding the first N items from the response.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subuser Statistics
        """
        url = f"{self.base_url}/v3/subusers/stats/monthly"
        query_params = {
            k: v
            for k, v in [
                ("date", date),
                ("subuser", subuser),
                ("sort_by_metric", sort_by_metric),
                ("sort_by_direction", sort_by_direction),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_stat_sum(
        self,
        start_date,
        sort_by_direction=None,
        end_date=None,
        limit=None,
        offset=None,
        aggregated_by=None,
        sort_by_metric=None,
    ) -> dict[str, Any]:
        """
        Retrieves summary statistics for subusers, allowing optional filtering by sort direction, start and end dates, data aggregation, and sorting metrics.

        Args:
            start_date (string): The start date for the statistics data to include, formatted as a string (e.g., "YYYY-MM-DD").
            sort_by_direction (string): Optional parameter to specify the direction of sorting for the results, accepting "asc" or "desc" with a default of "desc".
            end_date (string): The end_date query parameter specifies the optional ending date for filtering subuser statistics sums.
            limit (integer): Specifies the maximum number of results to return in the response, with a default value of 5.
            offset (integer): The "offset" parameter determines the starting point in the dataset by excluding the first N items from the response, allowing pagination of the resulting data.
            aggregated_by (string): Specify the dimension or field by which the subuser statistics should be aggregated in the query results.
            sort_by_metric (string): The metric by which to sort the summarized subuser statistics results; defaults to "delivered".

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subuser Statistics
        """
        url = f"{self.base_url}/v3/subusers/stats/sums"
        query_params = {
            k: v
            for k, v in [
                ("sort_by_direction", sort_by_direction),
                ("start_date", start_date),
                ("end_date", end_date),
                ("limit", limit),
                ("offset", offset),
                ("aggregated_by", aggregated_by),
                ("sort_by_metric", sort_by_metric),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_subuser(self, subuser_name) -> dict[str, Any]:
        """
        Deletes the specified subuser from the account, removing their access and related data.

        Args:
            subuser_name (string): subuser_name

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subusers
        """
        if subuser_name is None:
            raise ValueError("Missing required parameter 'subuser_name'")
        url = f"{self.base_url}/v3/subusers/{subuser_name}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_subuser(self, subuser_name, disabled=None) -> dict[str, Any]:
        """
        Updates properties of a specified subuser using a PATCH request with JSON data and returns a success status (204) or relevant error codes.

        Args:
            subuser_name (string): subuser_name
            disabled (boolean): Whether or not this subuser is disabled. `true` means disabled, `false` means enabled.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subusers
        """
        if subuser_name is None:
            raise ValueError("Missing required parameter 'subuser_name'")
        request_body = {
            "disabled": disabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/subusers/{subuser_name}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_subuser_credit(self, subuser_name) -> dict[str, Any]:
        """
        Retrieves the credits information for a specified subuser, identified by {subuser_name}, and returns the details in response.

        Args:
            subuser_name (string): subuser_name

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subusers
        """
        if subuser_name is None:
            raise ValueError("Missing required parameter 'subuser_name'")
        url = f"{self.base_url}/v3/subusers/{subuser_name}/credits"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_subuser_credit(
        self, subuser_name, type, reset_frequency=None, total=None
    ) -> dict[str, Any]:
        """
        Updates the credits of a subuser identified by `{subuser_name}` using a JSON payload.

        Args:
            subuser_name (string): subuser_name
            type (string): type
            reset_frequency (string): reset_frequency
            total (integer): Total number of credits to which the Subuser is to be reset. If `type` is `nonrecurring` then the Subuser's credits will be reset to `total` on a one-time basis. If `type` is `recurring` then the Subuser's credits will be reset to `total` every time a reset is scheduled in accordance with the `reset_frequency`. Do _not_ include `total` if you choose a reset `type` value of `unlimited`.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subusers
        """
        if subuser_name is None:
            raise ValueError("Missing required parameter 'subuser_name'")
        request_body = {
            "reset_frequency": reset_frequency,
            "total": total,
            "type": type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/subusers/{subuser_name}/credits"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_subuser_remaining_credit(
        self, subuser_name, allocation_update
    ) -> dict[str, Any]:
        """
        Updates the remaining credits for a specified subuser and returns status information.

        Args:
            subuser_name (string): subuser_name
            allocation_update (integer): The number of credits to add to or subtract from the current remaining credits for the Subuser. Use a positive number to increase the remaining credits or a negative number to reduce the remaining credits.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subusers
        """
        if subuser_name is None:
            raise ValueError("Missing required parameter 'subuser_name'")
        request_body = {
            "allocation_update": allocation_update,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/subusers/{subuser_name}/credits/remaining"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_subuser_ip(self, subuser_name, items=None) -> dict[str, Any]:
        """
        Updates the IP configuration for a specified subuser using the provided JSON data and returns a success status if the operation is successful.

        Args:
            subuser_name (string): subuser_name

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subusers
        """
        if subuser_name is None:
            raise ValueError("Missing required parameter 'subuser_name'")
        # Use items array directly as request body
        request_body = items
        url = f"{self.base_url}/v3/subusers/{subuser_name}/ips"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_subuser_monthly_stat(
        self,
        subuser_name,
        date,
        sort_by_metric=None,
        sort_by_direction=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves monthly statistics for a specified subuser using the "GET" method, allowing filtering by date and optional sorting and pagination parameters.

        Args:
            subuser_name (string): subuser_name
            date (string): Specifies the month (YYYY-MM) for which to retrieve monthly statistics for the specified subuser.
            sort_by_metric (string): Optional string parameter to specify the metric by which to sort the monthly statistics for a subuser, defaulting to "delivered" if not provided.
            sort_by_direction (string): sort_by_direction specifies the order direction for sorting the monthly statistics, with a default value of "desc" for descending order, and is optional in the query string.
            limit (integer): The `limit` parameter specifies the maximum number of monthly statistics records to return for the specified subuser, with a default value of 5.
            offset (integer): Specifies the number of items at the start of the list to skip before returning results, enabling pagination.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subuser Statistics
        """
        if subuser_name is None:
            raise ValueError("Missing required parameter 'subuser_name'")
        url = f"{self.base_url}/v3/subusers/{subuser_name}/stats/monthly"
        query_params = {
            k: v
            for k, v in [
                ("date", date),
                ("sort_by_metric", sort_by_metric),
                ("sort_by_direction", sort_by_direction),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_subuser_website_access(
        self, subuser_name, disabled=None
    ) -> dict[str, Any]:
        """
        Updates a subuser's website access using the GitHub API, returning a status message upon successful modification.

        Args:
            subuser_name (string): subuser_name
            disabled (boolean): Whether or not to disable website access to the Subuser. `true` means disabled, `false` means enabled.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Subuser Website Access
        """
        if subuser_name is None:
            raise ValueError("Missing required parameter 'subuser_name'")
        request_body = {
            "disabled": disabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/subusers/{subuser_name}/website_access"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_suppression_blocks(self, delete_all=None, emails=None) -> dict[str, Any]:
        """
        Removes a suppression block using the "DELETE" method at the "/v3/suppression/blocks" path, returning a successful response with no content.

        Args:
            delete_all (boolean): Indicates if you want to delete all blocked email addresses.
            emails (array): The specific blocked email addresses that you want to delete.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Blocks
        """
        request_body = {
            "delete_all": delete_all,
            "emails": emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/suppression/blocks"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_suppression_block(
        self, start_time=None, end_time=None, limit=None, offset=None, email=None
    ) -> list[Any]:
        """
        Retrieves a list of suppression blocks within a specified time range using optional pagination and partial matching parameters.

        Args:
            start_time (integer): start_time is a query parameter representing the earliest timestamp (in integer format) from which to retrieve suppression block records, typically specified as a Unix epoch time.
            end_time (integer): The end_time parameter specifies the maximum timestamp (as an integer) to filter suppression blocks up to that time in the query.
            limit (integer): `limit` sets the page size, i.e. maximum number of items from the list to be returned for a single API request. If omitted, the default page size is used. The maximum page size for this endpoint is 500 items per page.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.
            email (string): Specifies which records to return based on the records' associated email addresses. For example, `sales` returns records with email addresses that start with 'sales', such as `salesdepartment@example.com` or `sales@example.com`.  You can also use `%25` as a wildcard. For example, `%25market` returns records containing email addresses with the string 'market' anywhere in the email address, and `%25market%25tree` returns records containing email addresses with the string 'market' followed by the string 'tree'. Any reserved characters should be [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding#Reserved_characters), e.g., the `@` symbol should be encoded as `%40`.

        Returns:
            list[Any]: API response data.

        Tags:
            Blocks
        """
        url = f"{self.base_url}/v3/suppression/blocks"
        query_params = {
            k: v
            for k, v in [
                ("start_time", start_time),
                ("end_time", end_time),
                ("limit", limit),
                ("offset", offset),
                ("email", email),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_suppression_block(self, email) -> dict[str, Any]:
        """
        Removes the specified email address from the suppression block list and returns no content upon success.

        Args:
            email (string): email

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Blocks
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/suppression/blocks/{email}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_suppression_block(self, email) -> list[Any]:
        """
        Retrieves the block status of an email address using a GET request to the "/v3/suppression/blocks/{email}" endpoint.

        Args:
            email (string): email

        Returns:
            list[Any]: API response data.

        Tags:
            Blocks
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/suppression/blocks/{email}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_suppression_bounces(self, delete_all=None, emails=None) -> Any:
        """
        Removes bounce suppression records via DELETE, returning 204 No Content on success or 401 Unauthorized if not authenticated.

        Args:
            delete_all (boolean): This parameter allows you to delete **every** email in your bounce list. This should not be used with the emails parameter.
            emails (array): Delete multiple emails from your bounce list at the same time. This should not be used with the delete_all parameter.

        Returns:
            Any: API response data.

        Tags:
            Bounces
        """
        request_body = {
            "delete_all": delete_all,
            "emails": emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/suppression/bounces"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_suppression_bounces(
        self, start_time=None, end_time=None, limit=None, offset=None, email=None
    ) -> list[Any]:
        """
        Retrieves a paginated list of bounced email addresses and their details, optionally filtered by time range, email address, and other query parameters.

        Args:
            start_time (integer): Epoch timestamp in seconds specifying the start of the time range to filter bounce events.
            end_time (integer): Specifies the end time, in integer format, for filtering bounces in the GET operation at the "/v3/suppression/bounces" path. (Note: Typically, end times are specified in a date-time format. However, this description adheres to the provided type as "integer," which may require further context or conversion.)
            limit (integer): `limit` sets the page size, i.e. maximum number of items from the list to be returned for a single API request. If omitted, the default page size is used. The maximum page size for this endpoint is 500 items per page.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.
            email (string): Specifies which records to return based on the records' associated email addresses. For example, `sales` returns records with email addresses that start with 'sales', such as `salesdepartment@example.com` or `sales@example.com`.  You can also use `%25` as a wildcard. For example, `%25market` returns records containing email addresses with the string 'market' anywhere in the email address, and `%25market%25tree` returns records containing email addresses with the string 'market' followed by the string 'tree'. Any reserved characters should be [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding#Reserved_characters), e.g., the `@` symbol should be encoded as `%40`.

        Returns:
            list[Any]: API response data.

        Tags:
            Bounces
        """
        url = f"{self.base_url}/v3/suppression/bounces"
        query_params = {
            k: v
            for k, v in [
                ("start_time", start_time),
                ("end_time", end_time),
                ("limit", limit),
                ("offset", offset),
                ("email", email),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_suppression_bounces_classifications(
        self, start_date=None, end_date=None
    ) -> dict[str, Any]:
        """
        Retrieves email bounces by specific classification using the SendGrid API, allowing filtering by date range and classification types such as 'Content', 'Frequency or Volume Too High', 'Invalid Address', 'Mailbox Unavailable', 'Reputation', 'Technical Failure', and 'Unclassified'.

        Args:
            start_date (string): The `start_date` parameter filters results to include only bounce classifications that occurred on or after the specified date, formatted as a string in ISO 8601 format (YYYY-MM-DD).
            end_date (string): The "end_date" parameter is a string that specifies the end date for filtering bounce classifications in the API response.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Bounces
        """
        url = f"{self.base_url}/v3/suppression/bounces/classifications"
        query_params = {
            k: v
            for k, v in [("start_date", start_date), ("end_date", end_date)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_suppression_bounces_classifications(
        self, classification, start_date=None, end_date=None
    ) -> dict[str, Any]:
        """
        Retrieves bounces from the suppression list filtered by a specified classification and optional date range.

        Args:
            classification (string): classification
            start_date (string): Specifies the start date for filtering bounce classifications in the format of a string.
            end_date (string): The "end_date" parameter specifies the end date for filtering bounce classifications in the format "YYYY-MM-DD", typically using ISO 8601 standards for consistency and clarity.

        Returns:
            dict[str, Any]: 200 OK

        Tags:
            Bounces
        """
        if classification is None:
            raise ValueError("Missing required parameter 'classification'")
        url = f"{self.base_url}/v3/suppression/bounces/classifications/{classification}"
        query_params = {
            k: v
            for k, v in [("start_date", start_date), ("end_date", end_date)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_suppression_bounce(self, email) -> dict[str, Any]:
        """
        Deletes a suppression bounce entry for a specified email address.

        Args:
            email (string): email

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Bounces
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/suppression/bounces/{email}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_suppression_bounces(self, email) -> list[Any]:
        """
        Retrieves bounce suppression details for a specific email address from the suppression list.

        Args:
            email (string): email

        Returns:
            list[Any]: API response data.

        Tags:
            Bounces
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/suppression/bounces/{email}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_invalid_emails(self, delete_all=None, emails=None) -> dict[str, Any]:
        """
        Deletes a specified invalid email from suppression using the "DELETE" method and returns no content upon successful removal.

        Args:
            delete_all (boolean): Indicates if you want to remove all email address from the invalid emails list.
            emails (array): The list of specific email addresses that you want to remove.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Invalid Emails
        """
        request_body = {
            "delete_all": delete_all,
            "emails": emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/suppression/invalid_emails"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_invalid_email(
        self, start_time=None, end_time=None, limit=None, offset=None, email=None
    ) -> list[Any]:
        """
        Retrieves a list of invalid emails for suppression, optionally filtered by start and end time, email address, and pagination parameters.

        Args:
            start_time (integer): The `start_time` parameter is an integer specifying the earliest timestamp for filtering invalid email records in the response.
            end_time (integer): The end_time parameter in the query specifies the upper bound timestamp (as an integer) to limit the results to invalid emails reported before this time.
            limit (integer): `limit` sets the page size, i.e. maximum number of items from the list to be returned for a single API request. If omitted, the default page size is used. The maximum page size for this endpoint is 500 items per page.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.
            email (string): Email address to filter the invalid emails suppression list by.

        Returns:
            list[Any]: API response data.

        Tags:
            Invalid Emails
        """
        url = f"{self.base_url}/v3/suppression/invalid_emails"
        query_params = {
            k: v
            for k, v in [
                ("start_time", start_time),
                ("end_time", end_time),
                ("limit", limit),
                ("offset", offset),
                ("email", email),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_invalid_email(self, email) -> dict[str, Any]:
        """
        Deletes an invalid email from the suppression list at path "/v3/suppression/invalid_emails/{email}" using the DELETE method and returns a 204 No Content response.

        Args:
            email (string): email

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Invalid Emails
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/suppression/invalid_emails/{email}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_invalid_email(self, email) -> list[Any]:
        """
        Retrieves details about a specific invalid email address from the suppression list.

        Args:
            email (string): email

        Returns:
            list[Any]: API response data.

        Tags:
            Invalid Emails
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/suppression/invalid_emails/{email}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_spam_reports(self, delete_all=None, emails=None) -> dict[str, Any]:
        """
        Removes spam report records via a DELETE request to the specified endpoint, returning a 204 No Content response upon success.

        Args:
            delete_all (boolean): Indicates if you want to delete all email addresses on the spam report list.
            emails (array): A list of specific email addresses that you want to remove from the spam report list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Spam Reports
        """
        request_body = {
            "delete_all": delete_all,
            "emails": emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/suppression/spam_reports"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_spam_report(
        self, start_time=None, end_time=None, limit=None, offset=None, email=None
    ) -> list[Any]:
        """
        Retrieves a list of spam reports based on query parameters for start and end times, with optional filtering by pagination and email partial matching.

        Args:
            start_time (integer): The `start_time` parameter specifies the earliest timestamp, in integer format, for retrieving spam reports.
            end_time (integer): The "end_time" parameter specifies the end timestamp for retrieving spam reports, ensuring results do not exceed this time, typically in integer format representing seconds since the epoch.
            limit (integer): `limit` sets the page size, i.e. maximum number of items from the list to be returned for a single API request. If omitted, the default page size is used. The maximum page size for this endpoint is 500 items per page.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.
            email (string): Specifies which records to return based on the records' associated email addresses. For example, `sales` returns records with email addresses that start with 'sales', such as `salesdepartment@example.com` or `sales@example.com`.  You can also use `%25` as a wildcard. For example, `%25market` returns records containing email addresses with the string 'market' anywhere in the email address, and `%25market%25tree` returns records containing email addresses with the string 'market' followed by the string 'tree'. Any reserved characters should be [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding#Reserved_characters), e.g., the `@` symbol should be encoded as `%40`.

        Returns:
            list[Any]: API response data.

        Tags:
            Spam Reports
        """
        url = f"{self.base_url}/v3/suppression/spam_reports"
        query_params = {
            k: v
            for k, v in [
                ("start_time", start_time),
                ("end_time", end_time),
                ("limit", limit),
                ("offset", offset),
                ("email", email),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_spam_report(self, email) -> dict[str, Any]:
        """
        Deletes the specified email address from the spam reports suppression list and returns no content upon successful removal.

        Args:
            email (string): email

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Spam Reports
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/suppression/spam_reports/{email}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_spam_report(self, email) -> list[Any]:
        """
        Retrieves the spam report details for the specified email address from the suppression list.

        Args:
            email (string): email

        Returns:
            list[Any]: API response data.

        Tags:
            Spam Reports
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        url = f"{self.base_url}/v3/suppression/spam_reports/{email}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_global_suppression(
        self, start_time=None, end_time=None, limit=None, offset=None, email=None
    ) -> list[Any]:
        """
        Retrieves a paginated list of email addresses that were unsubscribed within a specified time range, optionally filtered by partial email match and supporting pagination parameters.

        Args:
            start_time (integer): Specifies the earliest timestamp (as an integer) to include in the response, filtering results to unsubscribes that occurred at or after this time.
            end_time (integer): Specifies the end time in seconds since the Unix epoch for filtering unsubscribe records, where results will not include data published after this timestamp.
            limit (integer): `limit` sets the page size, i.e. maximum number of items from the list to be returned for a single API request. If omitted, the default page size is used. The maximum page size for this endpoint is 500 items per page.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.
            email (string): Specifies which records to return based on the records' associated email addresses. For example, `sales` returns records with email addresses that start with 'sales', such as `salesdepartment@example.com` or `sales@example.com`.  You can also use `%25` as a wildcard. For example, `%25market` returns records containing email addresses with the string 'market' anywhere in the email address, and `%25market%25tree` returns records containing email addresses with the string 'market' followed by the string 'tree'. Any reserved characters should be [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding#Reserved_characters), e.g., the `@` symbol should be encoded as `%40`.

        Returns:
            list[Any]: API response data.

        Tags:
            Global Suppressions
        """
        url = f"{self.base_url}/v3/suppression/unsubscribes"
        query_params = {
            k: v
            for k, v in [
                ("start_time", start_time),
                ("end_time", end_time),
                ("limit", limit),
                ("offset", offset),
                ("email", email),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_teammate(self, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves a list of teammates using the specified parameters, including pagination options and the ability to act on behalf of another user.

        Args:
            limit (integer): Specifies the maximum number of teammates to include in the response, with a default value of 500.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teammates
        """
        url = f"{self.base_url}/v3/teammates"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def invite_teammate(self, email=None, is_admin=None, scopes=None) -> dict[str, Any]:
        """
        Creates a new teammate by sending a POST request to the "/v3/teammates" endpoint, accepting JSON content, and returns a 201 status upon successful creation.

        Args:
            email (string): New teammate's email
            is_admin (boolean): Set to true if teammate should be an admin user
            scopes (array): Set to specify list of scopes that teammate should have. Should be empty if teammate is an admin.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teammates
        """
        request_body = {
            "email": email,
            "is_admin": is_admin,
            "scopes": scopes,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/teammates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_pending_teammate(self) -> dict[str, Any]:
        """
        Retrieves a list of pending teammates using the GitHub API and returns a successful response with relevant details.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teammates
        """
        url = f"{self.base_url}/v3/teammates/pending"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_pending_teammate(self, token) -> Any:
        """
        Deletes a pending teammate invitation using the provided token, returning a 204 status if successful.

        Args:
            token (string): token

        Returns:
            Any: API response data.

        Tags:
            Teammates
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        url = f"{self.base_url}/v3/teammates/pending/{token}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def resend_teammate_invite(self, token) -> dict[str, Any]:
        """
        Resends a pending teammate invitation associated with the given token using the API.

        Args:
            token (string): token

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teammates
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        url = f"{self.base_url}/v3/teammates/pending/{token}/resend"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_subuser_by_template(self, teammate_name) -> dict[str, Any]:
        """
        Retrieves the list of Subusers and their available scopes that a specified Teammate can access and act on behalf of.

        Args:
            teammate_name (string): teammate_name

        Returns:
            dict[str, Any]: 200 Success

        Tags:
            Teammates
        """
        if teammate_name is None:
            raise ValueError("Missing required parameter 'teammate_name'")
        url = f"{self.base_url}/v3/teammates/{teammate_name}/subuser_access"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_teammate(self, username) -> Any:
        """
        Removes a teammate from a GitHub organization using the GitHub API and returns a status code indicating success or failure.

        Args:
            username (string): username

        Returns:
            Any: The Teammate was successfully deleted.

        Tags:
            Teammates
        """
        if username is None:
            raise ValueError("Missing required parameter 'username'")
        url = f"{self.base_url}/v3/teammates/{username}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_teammate(self, username) -> dict[str, Any]:
        """
        Retrieves information about a GitHub user's teammate with the specified username using the "GET" method.

        Args:
            username (string): username

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teammates
        """
        if username is None:
            raise ValueError("Missing required parameter 'username'")
        url = f"{self.base_url}/v3/teammates/{username}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_teammate(self, username, is_admin=None, scopes=None) -> dict[str, Any]:
        """
        Updates the details of a teammate identified by username within an organization using JSON-formatted data and supports acting on behalf of another user.

        Args:
            username (string): username
            is_admin (boolean): Set to True if this teammate should be promoted to an admin user. If True, scopes should be an empty array.
            scopes (array): Provide list of scopes that should be given to teammate. If specifying list of scopes, is_admin should be set to False.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teammates
        """
        if username is None:
            raise ValueError("Missing required parameter 'username'")
        request_body = {
            "is_admin": is_admin,
            "scopes": scopes,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/teammates/{username}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_template(self, generation=None, name=None) -> dict[str, Any]:
        """
        Creates a new template using the JSON data provided in the request body and returns a successful creation response with a 201 status code.

        Args:
            generation (string): generation
            name (string): The name for the new transactional template.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Templates
        """
        request_body = {
            "generation": generation,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/templates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_template(self, template_id) -> dict[str, Any]:
        """
        Deletes a template identified by the `template_id` in the `/v3/templates/{template_id}` path, returning a successful response with no content (204).

        Args:
            template_id (string): template_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'")
        url = f"{self.base_url}/v3/templates/{template_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template(self, template_id) -> dict[str, Any]:
        """
        Retrieves detailed information for the specified template identified by its template_id.

        Args:
            template_id (string): template_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'")
        url = f"{self.base_url}/v3/templates/{template_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_template(self, template_id, name=None) -> dict[str, Any]:
        """
        Creates a new resource related to a template identified by `{template_id}` using a JSON payload and returns a successful creation status with a 201 response code.

        Args:
            template_id (string): template_id
            name (string): The name for the new transactional template.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Templates
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/templates/{template_id}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_template_version(
        self,
        template_id,
        active=None,
        editor=None,
        generate_plain_content=None,
        html_content=None,
        name=None,
        plain_content=None,
        subject=None,
        test_data=None,
    ) -> dict[str, Any]:
        """
        Creates a new version for a specified template using the POST method and returns a 201 Created response upon success.

        Args:
            template_id (string): template_id
            active (integer): active
            editor (string): editor
            generate_plain_content (boolean): If true, plain_content is always generated from html_content. If false, plain_content is not altered.
            html_content (string): The HTML content of the version. Maximum of 1048576 bytes allowed.
            name (string): Name of the transactional template version.
            plain_content (string): Text/plain content of the transactional template version. Maximum of 1048576 bytes allowed.
            subject (string): Subject of the new transactional template version.
            test_data (string): For dynamic templates only, the mock json data that will be used for template preview and test sends.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Templates Versions
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'")
        request_body = {
            "active": active,
            "editor": editor,
            "generate_plain_content": generate_plain_content,
            "html_content": html_content,
            "name": name,
            "plain_content": plain_content,
            "subject": subject,
            "test_data": test_data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/templates/{template_id}/versions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_template_version(self, template_id, version_id) -> Any:
        """
        Deletes a specific version of a template identified by the provided template ID and version ID.

        Args:
            template_id (string): template_id
            version_id (string): version_id

        Returns:
            Any: API response data.

        Tags:
            Templates Versions
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'")
        if version_id is None:
            raise ValueError("Missing required parameter 'version_id'")
        url = f"{self.base_url}/v3/templates/{template_id}/versions/{version_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_version(self, template_id, version_id) -> dict[str, Any]:
        """
        Retrieves a specific version of a transactional template by its template ID and version ID using the SendGrid API.

        Args:
            template_id (string): template_id
            version_id (string): version_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Templates Versions
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'")
        if version_id is None:
            raise ValueError("Missing required parameter 'version_id'")
        url = f"{self.base_url}/v3/templates/{template_id}/versions/{version_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activate_template_version(self, template_id, version_id) -> dict[str, Any]:
        """
        Activates a specific version of a template by sending a POST request with the template and version IDs.

        Args:
            template_id (string): template_id
            version_id (string): version_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Templates Versions
        """
        if template_id is None:
            raise ValueError("Missing required parameter 'template_id'")
        if version_id is None:
            raise ValueError("Missing required parameter 'version_id'")
        url = (
            f"{self.base_url}/v3/templates/{template_id}/versions/{version_id}/activate"
        )
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tracking_setting(self) -> dict[str, Any]:
        """
        Retrieves the current tracking settings for an account using the SendGrid API.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        url = f"{self.base_url}/v3/tracking_settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_click_tracking_setting(self) -> dict[str, Any]:
        """
        Retrieves the current click tracking settings for the specified configuration using the "GET" method.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        url = f"{self.base_url}/v3/tracking_settings/click"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_click_tracking_setting(self, enabled=None) -> dict[str, Any]:
        """
        Updates the click tracking settings for email links using a PATCH request to the "/v3/tracking_settings/click" endpoint.

        Args:
            enabled (boolean): The setting you want to use for click tracking.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        request_body = {
            "enabled": enabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/tracking_settings/click"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_google_analytics_tracking_setting(self) -> dict[str, Any]:
        """
        Retrieves the Google Analytics tracking settings using the API.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        url = f"{self.base_url}/v3/tracking_settings/google_analytics"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_google_analytics_tracking_setting(
        self,
        enabled=None,
        utm_campaign=None,
        utm_content=None,
        utm_medium=None,
        utm_source=None,
        utm_term=None,
    ) -> dict[str, Any]:
        """
        Updates the Google Analytics tracking settings for the specified resource using the provided configuration.

        Args:
            enabled (boolean): Indicates if Google Analytics is enabled.
            utm_campaign (string): The name of the campaign.
            utm_content (string): Used to differentiate ads
            utm_medium (string): Name of the marketing medium (e.g. "Email").
            utm_source (string): Name of the referrer source.
            utm_term (string): Any paid keywords.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        request_body = {
            "enabled": enabled,
            "utm_campaign": utm_campaign,
            "utm_content": utm_content,
            "utm_medium": utm_medium,
            "utm_source": utm_source,
            "utm_term": utm_term,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/tracking_settings/google_analytics"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_open_tracking_setting(self) -> dict[str, Any]:
        """
        Retrieves the open tracking settings for the specified configuration using the "GET" method, optionally executed on behalf of another user.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        url = f"{self.base_url}/v3/tracking_settings/open"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_open_tracking_setting(self, enabled=None) -> dict[str, Any]:
        """
        Updates tracking settings for open events by sending a JSON payload to the specified endpoint, returning a successful status upon completion.

        Args:
            enabled (boolean): The new status that you want to set for open tracking.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        request_body = {
            "enabled": enabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/tracking_settings/open"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_subscription_tracking_setting(self) -> dict[str, Any]:
        """
        Retrieves the current subscription tracking settings for your SendGrid account, which control the inclusion of subscription management links in your emails. [1][2][3]

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        url = f"{self.base_url}/v3/tracking_settings/subscription"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_subscription_tracking_setting(
        self,
        enabled=None,
        html_content=None,
        landing=None,
        plain_content=None,
        replace=None,
        url=None,
    ) -> dict[str, Any]:
        """
        Modifies the tracking settings subscription using the PATCH method, allowing partial updates to specific fields of the resource at the "/v3/tracking_settings/subscription" path.

        Args:
            enabled (boolean): Indicates if subscription tracking is enabled.
            html_content (string): The information and HTML for your unsubscribe link.
            landing (string): The HTML that will be displayed on the page that your customers will see after clicking unsubscribe, hosted on SendGrid’s server.
            plain_content (string): The information in plain text for your unsubscribe link. You should have the “<% %>” tag in your content, otherwise the user will have no URL for unsubscribing.
            replace (string): Your custom defined replacement tag for your templates. Use this tag to place your unsubscribe content anywhere in your emailtemplate.
            url (string): The URL where you would like your users sent to unsubscribe.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Tracking
        """
        request_body = {
            "enabled": enabled,
            "html_content": html_content,
            "landing": landing,
            "plain_content": plain_content,
            "replace": replace,
            "url": url,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/tracking_settings/subscription"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_account(self) -> dict[str, Any]:
        """
        Retrieves information about the GitHub user account using the "GET /v3/user/account" method.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        url = f"{self.base_url}/v3/user/account"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_credit(self) -> dict[str, Any]:
        """
        Retrieves user credits information using the specified API endpoint.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        url = f"{self.base_url}/v3/user/credits"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_email(self) -> dict[str, Any]:
        """
        Retrieves a user's email address using the GET method, optionally acting on behalf of another user.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        url = f"{self.base_url}/v3/user/email"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_email(self, email=None) -> dict[str, Any]:
        """
        Updates a user's email address using the PUT method at the "/v3/user/email" endpoint, accepting a JSON body and returning a successful response upon completion.

        Args:
            email (string): The new email address that you would like to use for your account.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        request_body = {
            "email": email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/email"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_password(self, new_password=None, old_password=None) -> dict[str, Any]:
        """
        Updates the password for the authenticated user using the GitHub API.

        Args:
            new_password (string): The new password you would like to use for your account.
            old_password (string): The old password for your account.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        request_body = {
            "new_password": new_password,
            "old_password": old_password,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/password"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_profile(self) -> dict[str, Any]:
        """
        Retrieves the authenticated user's public and private profile information.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        url = f"{self.base_url}/v3/user/profile"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_profile(
        self,
        address=None,
        address2=None,
        city=None,
        company=None,
        country=None,
        first_name=None,
        last_name=None,
        phone=None,
        state=None,
        website=None,
        zip=None,
    ) -> dict[str, Any]:
        """
        Updates specific fields in the authenticated user's profile using partial modifications with a JSON request payload.

        Args:
            address (string): The street address for this user profile.
            address2 (string): An optional second line for the street address of this user profile.
            city (string): The city for the user profile.
            company (string): That company that this user profile is associated with.
            country (string): Th country of this user profile.
            first_name (string): The first name of the user.
            last_name (string): The last name of the user.
            phone (string): The phone number for the user.
            state (string): The state for this user.
            website (string): The website associated with this user.
            zip (string): The zip code for this user.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        request_body = {
            "address": address,
            "address2": address2,
            "city": city,
            "company": company,
            "country": country,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "state": state,
            "website": website,
            "zip": zip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/profile"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_scheduled_send(self) -> list[Any]:
        """
        Retrieves a list of all scheduled sends for a user using the specified API endpoint.

        Returns:
            list[Any]: API response data.

        Tags:
            Scheduled Sends
        """
        url = f"{self.base_url}/v3/user/scheduled_sends"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_scheduled_send(self, batch_id=None, status=None) -> dict[str, Any]:
        """
        Creates a new scheduled send for a user with the provided details and returns a status indicating the result of the operation.

        Args:
            batch_id (string): The batch ID is the identifier that your scheduled mail sends share.
            status (string): status

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Scheduled Sends
        """
        request_body = {
            "batch_id": batch_id,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/scheduled_sends"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_scheduled_send(self, batch_id) -> Any:
        """
        Deletes a scheduled send batch identified by the specified `batch_id` in the user's account, returning no content upon successful deletion.

        Args:
            batch_id (string): batch_id

        Returns:
            Any: API response data.

        Tags:
            Scheduled Sends
        """
        if batch_id is None:
            raise ValueError("Missing required parameter 'batch_id'")
        url = f"{self.base_url}/v3/user/scheduled_sends/{batch_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_scheduled_send(self, batch_id) -> list[Any]:
        """
        Retrieves details about a scheduled send operation for the specified batch ID.

        Args:
            batch_id (string): batch_id

        Returns:
            list[Any]: API response data.

        Tags:
            Scheduled Sends
        """
        if batch_id is None:
            raise ValueError("Missing required parameter 'batch_id'")
        url = f"{self.base_url}/v3/user/scheduled_sends/{batch_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_scheduled_send(self, batch_id, status=None) -> Any:
        """
        Updates a scheduled send batch by modifying specific fields using JSON Patch operations, returning a response code indicating the outcome of the update operation.

        Args:
            batch_id (string): batch_id
            status (string): status

        Returns:
            Any: API response data.

        Tags:
            Scheduled Sends
        """
        if batch_id is None:
            raise ValueError("Missing required parameter 'batch_id'")
        request_body = {
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/scheduled_sends/{batch_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_enforced_tls_setting(self) -> dict[str, Any]:
        """
        Retrieves the TLS enforcement settings for the user, including whether TLS is required for connections, and returns the current configuration.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Enforced TLS
        """
        url = f"{self.base_url}/v3/user/settings/enforced_tls"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_enforced_tls_setting(
        self, require_tls=None, require_valid_cert=None, version=None
    ) -> dict[str, Any]:
        """
        Updates the Enforced TLS settings for a user, specifying whether TLS support and a valid certificate are required for recipients, using the "PATCH" method.

        Args:
            require_tls (boolean): Indicates if you want to require your recipients to support TLS.
            require_valid_cert (boolean): Indicates if you want to require your recipients to have a valid certificate.
            version (number): version

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Enforced TLS
        """
        request_body = {
            "require_tls": require_tls,
            "require_valid_cert": require_valid_cert,
            "version": version,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/settings/enforced_tls"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_username(self) -> dict[str, Any]:
        """
        Retrieves the authenticated user's profile information, supporting requests made on behalf of another user.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        url = f"{self.base_url}/v3/user/username"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_username(self, username=None) -> dict[str, Any]:
        """
        Updates the username of the authenticated user with the provided new username data.

        Args:
            username (string): The new username you would like to use for your account.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Users API
        """
        request_body = {
            "username": username,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/username"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_event_webhook(
        self,
        bounce=None,
        click=None,
        deferred=None,
        delivered=None,
        dropped=None,
        enabled=None,
        friendly_name=None,
        group_resubscribe=None,
        group_unsubscribe=None,
        oauth_client_id=None,
        oauth_client_secret=None,
        oauth_token_url=None,
        open=None,
        processed=None,
        spam_report=None,
        unsubscribe=None,
        url=None,
    ) -> dict[str, Any]:
        """
        Configures event settings for user webhooks using the POST method, accepting JSON data in the request body.

        Args:
            bounce (boolean): Set this property to `true` to receive bounce events. A bounce occurs when a receiving server could not or would not accept a message.
            click (boolean): Set this property to `true` to receive click events. Click events occur when a recipient clicks on a link within the message. You must [enable Click Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#click-tracking) to receive this type of event.
            deferred (boolean): Set this property to `true` to receive deferred events. Deferred events occur when a recipient's email server temporarily rejects a message.
            delivered (boolean): Set this property to `true` to receive delivered events. Delivered events occur when a message has been successfully delivered to the receiving server.
            dropped (boolean): Set this property to `true` to receive dropped events. Dropped events occur when your message is not delivered by Twilio SendGrid. Dropped events are accomponied by a `reason` property, which indicates why the message was dropped. Reasons for a dropped message include: Invalid SMTPAPI header, Spam Content (if spam checker app enabled), Unsubscribed Address, Bounced Address, Spam Reporting Address, Invalid, Recipient List over Package Quota.
            enabled (boolean): Set this property to `true` to enable the Event Webhook or `false` to disable it.
            friendly_name (string): Optionally set this property to a friendly name for the Event Webhook. A friendly name may be assigned to each of your webhooks to help you differentiate them. The friendly name is for convenience only. You should use the webhook `id` property for any programmatic tasks.
            group_resubscribe (boolean): Set this property to `true` to receive group resubscribe events. Group resubscribes occur when recipients resubscribe to a specific [unsubscribe group](https://docs.sendgrid.com/ui/sending-email/create-and-manage-unsubscribe-groups) by updating their subscription preferences. You must [enable Subscription Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#subscription-tracking) to receive this type of event.
            group_unsubscribe (boolean): Set this property to `true` to receive group unsubscribe events. Group unsubscribes occur when recipients unsubscribe from a specific [unsubscribe group](https://docs.sendgrid.com/ui/sending-email/create-and-manage-unsubscribe-groups) either by direct link or by updating their subscription preferences. You must [enable Subscription Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#subscription-tracking) to receive this type of event.
            oauth_client_id (string): Set this property to the OAuth client ID that SendGrid will pass to your OAuth server or service provider to generate an OAuth access token. When passing data in this property, you must also include the `oauth_token_url` property.
            oauth_client_secret (string): Set this property to the OAuth client secret that SendGrid will pass to your OAuth server or service provider to generate an OAuth access token. This secret is needed only once to create an access token. SendGrid will store the secret, allowing you to update your client ID and Token URL without passing the secret to SendGrid again. When passing data in this field, you must also include the `oauth_client_id` and `oauth_token_url` properties.
            oauth_token_url (string): Set this property to the URL where SendGrid will send the OAuth client ID and client secret to generate an OAuth access token. This should be your OAuth server or service provider. When passing data in this field, you must also include the `oauth_client_id` property.
            open (boolean): Set this property to `true` to receive open events. Open events occur when a recipient has opened the HTML message. You must [enable Open Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#open-tracking) to receive this type of event.
            processed (boolean): Set this property to `true` to receive processed events. Processed events occur when a message has been received by Twilio SendGrid and the message is ready to be delivered.
            spam_report (boolean): Set this property to `true` to receive spam report events. Spam reports occur when recipients mark a message as spam.
            unsubscribe (boolean): Set this property to `true` to receive unsubscribe events. Unsubscribes occur when recipients click on a message's subscription management link. You must [enable Subscription Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#subscription-tracking) to receive this type of event.
            url (string): Set this property to the URL where you want the Event Webhook to send event data.
                Example:
                ```json
                {
                  "bounce": true,
                  "click": true,
                  "deferred": true,
                  "delivered": false,
                  "dropped": true,
                  "enabled": true,
                  "friendly_name": "Enagement Webhook",
                  "group_resubscribe": true,
                  "group_unsubscribe": true,
                  "oauth_client_id": "a835e7210bbb47edbfa71bdfc909b2d7",
                  "oauth_client_secret": "335a9b0c65324fd2a62e2953d4b158",
                  "oauth_token_url": "https://oauthservice.example.com",
                  "open": true,
                  "processed": false,
                  "spam_report": true,
                  "unsubscribe": true,
                  "url": "https://example.com/webhook-endpoint"
                }
                ```

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Event Webhook
        """
        request_body = {
            "bounce": bounce,
            "click": click,
            "deferred": deferred,
            "delivered": delivered,
            "dropped": dropped,
            "enabled": enabled,
            "friendly_name": friendly_name,
            "group_resubscribe": group_resubscribe,
            "group_unsubscribe": group_unsubscribe,
            "oauth_client_id": oauth_client_id,
            "oauth_client_secret": oauth_client_secret,
            "oauth_token_url": oauth_token_url,
            "open": open,
            "processed": processed,
            "spam_report": spam_report,
            "unsubscribe": unsubscribe,
            "url": url,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/webhooks/event/settings"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_event_webhook(self, include=None) -> dict[str, Any]:
        """
        Retrieves the configuration and settings for all user webhook events and their associated preferences.

        Args:
            include (string): Use this to include optional fields in the response payload. When this is set to `include=account_status_change`, the `account_status_change` field will be part of the response payload and set to `false` by default. See [Update an event webhook](https://docs.sendgrid.com/api-reference/webhooks/update-an-event-webhook) for enabling this webhook notification which lets you subscribe to account status change events related to compliance action taken by SendGrid.

        Returns:
            dict[str, Any]: Success

        Tags:
            Event Webhook
        """
        url = f"{self.base_url}/v3/user/webhooks/event/settings/all"
        query_params = {k: v for k, v in [("include", include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_signed_event_webhook(self, id) -> dict[str, Any]:
        """
        Retrieves the signed event settings for a specific webhook event identified by the provided ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Event Webhook
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/user/webhooks/event/settings/signed/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_signed_event_webhook(self, id, enabled=None) -> dict[str, Any]:
        """
        Updates the configuration settings for a signed event webhook identified by the given ID using the PATCH method and returns the updated settings.

        Args:
            id (string): id
            enabled (boolean): Enable or disable the webhook by setting this property to `true` or `false`, respectively.
                Example:
                ```json
                {
                  "enabled": true
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Event Webhook
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "enabled": enabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/webhooks/event/settings/signed/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_event_webhook(self, id) -> Any:
        """
        Removes the event webhook settings with the specified ID and returns no content (204) or not found (404) if the settings do not exist.

        Args:
            id (string): id

        Returns:
            Any: No Content

        Tags:
            Event Webhook
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/user/webhooks/event/settings/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_webhook(self, id, include=None) -> dict[str, Any]:
        """
        Retrieves the webhook event settings for a specific user by ID.

        Args:
            id (string): id
            include (string): Use this to include optional fields in the response payload. When this is set to `include=account_status_change`, the `account_status_change` field will be part of the response payload and set to `false` by default. See [Update an event webhook](https://docs.sendgrid.com/api-reference/webhooks/update-an-event-webhook) for enabling this webhook notification which lets you subscribe to account status change events related to compliance action taken by SendGrid.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Event Webhook
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/user/webhooks/event/settings/{id}"
        query_params = {k: v for k, v in [("include", include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_event_webhook(
        self,
        id,
        include=None,
        bounce=None,
        click=None,
        deferred=None,
        delivered=None,
        dropped=None,
        enabled=None,
        friendly_name=None,
        group_resubscribe=None,
        group_unsubscribe=None,
        oauth_client_id=None,
        oauth_client_secret=None,
        oauth_token_url=None,
        open=None,
        processed=None,
        spam_report=None,
        unsubscribe=None,
        url=None,
    ) -> dict[str, Any]:
        """
        Updates the configuration for a specific user webhook event setting using the PATCH method and the provided JSON data.

        Args:
            id (string): id
            include (string): Use this to include optional fields in the response payload. When this is set to `include=account_status_change`, the `account_status_change` field will be part of the response payload and set to `false` by default. See [Update an event webhook](https://docs.sendgrid.com/api-reference/webhooks/update-an-event-webhook) for enabling this webhook notification which lets you subscribe to account status change events related to compliance action taken by SendGrid.
            bounce (boolean): Set this property to `true` to receive bounce events. A bounce occurs when a receiving server could not or would not accept a message.
            click (boolean): Set this property to `true` to receive click events. Click events occur when a recipient clicks on a link within the message. You must [enable Click Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#click-tracking) to receive this type of event.
            deferred (boolean): Set this property to `true` to receive deferred events. Deferred events occur when a recipient's email server temporarily rejects a message.
            delivered (boolean): Set this property to `true` to receive delivered events. Delivered events occur when a message has been successfully delivered to the receiving server.
            dropped (boolean): Set this property to `true` to receive dropped events. Dropped events occur when your message is not delivered by Twilio SendGrid. Dropped events are accomponied by a `reason` property, which indicates why the message was dropped. Reasons for a dropped message include: Invalid SMTPAPI header, Spam Content (if spam checker app enabled), Unsubscribed Address, Bounced Address, Spam Reporting Address, Invalid, Recipient List over Package Quota.
            enabled (boolean): Set this property to `true` to enable the Event Webhook or `false` to disable it.
            friendly_name (string): Optionally set this property to a friendly name for the Event Webhook. A friendly name may be assigned to each of your webhooks to help you differentiate them. The friendly name is for convenience only. You should use the webhook `id` property for any programmatic tasks.
            group_resubscribe (boolean): Set this property to `true` to receive group resubscribe events. Group resubscribes occur when recipients resubscribe to a specific [unsubscribe group](https://docs.sendgrid.com/ui/sending-email/create-and-manage-unsubscribe-groups) by updating their subscription preferences. You must [enable Subscription Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#subscription-tracking) to receive this type of event.
            group_unsubscribe (boolean): Set this property to `true` to receive group unsubscribe events. Group unsubscribes occur when recipients unsubscribe from a specific [unsubscribe group](https://docs.sendgrid.com/ui/sending-email/create-and-manage-unsubscribe-groups) either by direct link or by updating their subscription preferences. You must [enable Subscription Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#subscription-tracking) to receive this type of event.
            oauth_client_id (string): Set this property to the OAuth client ID that SendGrid will pass to your OAuth server or service provider to generate an OAuth access token. When passing data in this property, you must also include the `oauth_token_url` property.
            oauth_client_secret (string): Set this property to the OAuth client secret that SendGrid will pass to your OAuth server or service provider to generate an OAuth access token. This secret is needed only once to create an access token. SendGrid will store the secret, allowing you to update your client ID and Token URL without passing the secret to SendGrid again. When passing data in this field, you must also include the `oauth_client_id` and `oauth_token_url` properties.
            oauth_token_url (string): Set this property to the URL where SendGrid will send the OAuth client ID and client secret to generate an OAuth access token. This should be your OAuth server or service provider. When passing data in this field, you must also include the `oauth_client_id` property.
            open (boolean): Set this property to `true` to receive open events. Open events occur when a recipient has opened the HTML message. You must [enable Open Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#open-tracking) to receive this type of event.
            processed (boolean): Set this property to `true` to receive processed events. Processed events occur when a message has been received by Twilio SendGrid and the message is ready to be delivered.
            spam_report (boolean): Set this property to `true` to receive spam report events. Spam reports occur when recipients mark a message as spam.
            unsubscribe (boolean): Set this property to `true` to receive unsubscribe events. Unsubscribes occur when recipients click on a message's subscription management link. You must [enable Subscription Tracking](https://docs.sendgrid.com/ui/account-and-settings/tracking#subscription-tracking) to receive this type of event.
            url (string): Set this property to the URL where you want the Event Webhook to send event data.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Event Webhook
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "bounce": bounce,
            "click": click,
            "deferred": deferred,
            "delivered": delivered,
            "dropped": dropped,
            "enabled": enabled,
            "friendly_name": friendly_name,
            "group_resubscribe": group_resubscribe,
            "group_unsubscribe": group_unsubscribe,
            "oauth_client_id": oauth_client_id,
            "oauth_client_secret": oauth_client_secret,
            "oauth_token_url": oauth_token_url,
            "open": open,
            "processed": processed,
            "spam_report": spam_report,
            "unsubscribe": unsubscribe,
            "url": url,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/webhooks/event/settings/{id}"
        query_params = {k: v for k, v in [("include", include)] if v is not None}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def test_event_webhook(
        self,
        id=None,
        oauth_client_id=None,
        oauth_client_secret=None,
        oauth_token_url=None,
        url=None,
    ) -> Any:
        """
        Sends a test event to the user's webhook endpoint to verify its functionality.

        Args:
            id (string): The ID of the Event Webhook you want to retrieve.
            oauth_client_id (string): The client ID Twilio SendGrid sends to your OAuth server or service provider to generate an OAuth access token. When passing data in this property, you must also include the `oauth_token_url` property.
            oauth_client_secret (string): The `oauth_client_secret` is needed only once to create an access token. SendGrid will store this secret, allowing you to update your Client ID and Token URL without passing the secret to SendGrid again. When passing data in this field, you must also include the `oauth_client_id` and `oauth_token_url` properties.
            oauth_token_url (string): The URL where Twilio SendGrid sends the Client ID and Client Secret to generate an access token. This should be your OAuth server or service provider. When passing data in this field, you must also include the `oauth_client_id` property.
            url (string): The URL where you would like the test notification to be sent.

        Returns:
            Any: No Content

        Tags:
            Event Webhook
        """
        request_body = {
            "id": id,
            "oauth_client_id": oauth_client_id,
            "oauth_client_secret": oauth_client_secret,
            "oauth_token_url": oauth_token_url,
            "url": url,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/webhooks/event/test"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_parse_setting(self) -> dict[str, Any]:
        """
        Retrieves and returns the settings for parsing webhooks in the user's webhooks configuration.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Parse Webhook
        """
        url = f"{self.base_url}/v3/user/webhooks/parse/settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_parse_setting(
        self, hostname=None, send_raw=None, spam_check=None, url=None
    ) -> dict[str, Any]:
        """
        Configures and parses webhook settings for a user using the POST method.

        Args:
            hostname (string): A specific and unique domain or subdomain that you have created to use exclusively to parse your incoming email. For example, `parse.yourdomain.com`.
            send_raw (boolean): Indicates if you would like SendGrid to post the original MIME-type content of your parsed email. When this parameter is set to `true`, SendGrid will send a JSON payload of the content of your email.
            spam_check (boolean): Indicates if you would like SendGrid to check the content parsed from your emails for spam before POSTing them to your domain.
            url (string): The public URL where you would like SendGrid to POST the data parsed from your email. Any emails sent with the given hostname provided (whose MX records have been updated to point to SendGrid) will be parsed and POSTed to this URL.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Parse Webhook
        """
        request_body = {
            "hostname": hostname,
            "send_raw": send_raw,
            "spam_check": spam_check,
            "url": url,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/webhooks/parse/settings"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_parse_setting(self, hostname) -> dict[str, Any]:
        """
        Deletes the parse webhook settings associated with the specified hostname for the authenticated user.

        Args:
            hostname (string): hostname

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Parse Webhook
        """
        if hostname is None:
            raise ValueError("Missing required parameter 'hostname'")
        url = f"{self.base_url}/v3/user/webhooks/parse/settings/{hostname}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_parse_setting(self, hostname) -> dict[str, Any]:
        """
        Retrieves the settings for parsing webhooks from a specified hostname using the GET method.

        Args:
            hostname (string): hostname

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Parse Webhook
        """
        if hostname is None:
            raise ValueError("Missing required parameter 'hostname'")
        url = f"{self.base_url}/v3/user/webhooks/parse/settings/{hostname}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_parse_setting(
        self, hostname, hostname_body=None, send_raw=None, spam_check=None, url=None
    ) -> dict[str, Any]:
        """
        Updates the settings for parsing webhooks for a specified hostname using the PATCH method, returning a status message upon success.

        Args:
            hostname (string): hostname
            hostname_body (string): A specific and unique domain or subdomain that you have created to use exclusively to parse your incoming email. For example, `parse.yourdomain.com`.
            send_raw (boolean): Indicates if you would like SendGrid to post the original MIME-type content of your parsed email. When this parameter is set to `true`, SendGrid will send a JSON payload of the content of your email.
            spam_check (boolean): Indicates if you would like SendGrid to check the content parsed from your emails for spam before POSTing them to your domain.
            url (string): The public URL where you would like SendGrid to POST the data parsed from your email. Any emails sent with the given hostname provided (whose MX records have been updated to point to SendGrid) will be parsed and POSTed to this URL.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Parse Webhook
        """
        if hostname is None:
            raise ValueError("Missing required parameter 'hostname'")
        request_body = {
            "hostname": hostname_body,
            "send_raw": send_raw,
            "spam_check": spam_check,
            "url": url,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/user/webhooks/parse/settings/{hostname}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_parse_static(
        self, start_date, limit=None, offset=None, aggregated_by=None, end_date=None
    ) -> list[Any]:
        """
        Retrieves statistical data for webhook parsing, allowing users to filter results by limit, offset, aggregation, and date range.

        Args:
            start_date (string): The start_date query parameter specifies the required starting date for filtering webhook parse statistics.
            limit (string): The limit query parameter specifies the maximum number of results to return in the response, controlling the page size for the data retrieved.
            offset (string): Excludes the first N items from the collection of parsed webhook stats, allowing pagination by specifying the starting position for the returned results.
            aggregated_by (string): Filter webhook parse statistics by the specified aggregation criterion (e.g., time interval or category).
            end_date (string): Optional end date for retrieving webhook parse statistics, defaults to the current date if not specified.

        Returns:
            list[Any]: API response data.

        Tags:
            Parse Webhook
        """
        url = f"{self.base_url}/v3/user/webhooks/parse/stats"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("aggregated_by", aggregated_by),
                ("start_date", start_date),
                ("end_date", end_date),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def validate_email(self, email=None, source=None) -> dict[str, Any]:
        """
        Validates the format and deliverability of an email address by submitting the email data in JSON format to the API.

        Args:
            email (string): The email address that you want to validate.
            source (string): A one-word classifier for where this validation originated.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Email Address Validation
        """
        request_body = {
            "email": email,
            "source": source,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/validations/email"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_validations_email_jobs(self) -> dict[str, Any]:
        """
        Retrieves a list of email validation jobs processed by the API.

        Returns:
            dict[str, Any]: The request was successful. The response contains a list of all of your Bulk Email Validation Jobs.

        Tags:
            Bulk Email Address Validation
        """
        url = f"{self.base_url}/v3/validations/email/jobs"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_email_job_for_verification(self, file_type=None) -> dict[str, Any]:
        """
        Updates an existing email job validation resource using a JSON payload at the "/v3/validations/email/jobs" endpoint and returns a status message upon successful modification.

        Args:
            file_type (string): file_type

        Returns:
            dict[str, Any]: The request was successful. The response contains the URI and headers where you will upload your email address list.

        Tags:
            Bulk Email Address Validation
        """
        request_body = {
            "file_type": file_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/validations/email/jobs"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_email_job_for_verification(self, job_id) -> dict[str, Any]:
        """
        Get the status and details of an email validation job by its job ID.

        Args:
            job_id (string): job_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Bulk Email Address Validation
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/v3/validations/email/jobs/{job_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_verified_sender(
        self, limit=None, lastSeenID=None, id=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of verified senders using the GET method, allowing optional filtering by limit, last seen ID, and specific ID.

        Args:
            limit (number): Specifies the maximum number of verified senders to return in the response.
            lastSeenID (number): The `lastSeenID` parameter filters the response to include only verified senders with an ID greater than the specified value.
            id (integer): The `id` parameter is an integer value used in the query string to specify the identifier for the verified sender being retrieved.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Sender Verification
        """
        url = f"{self.base_url}/v3/verified_senders"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("lastSeenID", lastSeenID), ("id", id)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_verified_sender(
        self,
        address=None,
        address2=None,
        city=None,
        country=None,
        from_email=None,
        from_name=None,
        nickname=None,
        reply_to=None,
        reply_to_name=None,
        state=None,
        zip=None,
    ) -> dict[str, Any]:
        """
        Creates a new verified sender using the provided details and returns a successful response upon creation.

        Args:
            address (string): address
            address2 (string): address2
            city (string): city
            country (string): country
            from_email (string): from_email
            from_name (string): from_name
            nickname (string): nickname
            reply_to (string): reply_to
            reply_to_name (string): reply_to_name
            state (string): state
            zip (string): zip

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Sender Verification
        """
        request_body = {
            "address": address,
            "address2": address2,
            "city": city,
            "country": country,
            "from_email": from_email,
            "from_name": from_name,
            "nickname": nickname,
            "reply_to": reply_to,
            "reply_to_name": reply_to_name,
            "state": state,
            "zip": zip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/verified_senders"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_verified_sender_domain(self) -> dict[str, Any]:
        """
        Retrieves a list of verified sender domains.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Sender Verification
        """
        url = f"{self.base_url}/v3/verified_senders/domains"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def resend_verified_sender(self, id) -> dict[str, Any]:
        """
        Resends a verification request for a specified verified sender using the POST method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Sender Verification
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/verified_senders/resend/{id}"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_verified_sender_steps_completed(self) -> dict[str, Any]:
        """
        Retrieves the completed steps associated with verified senders in the system.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Sender Verification
        """
        url = f"{self.base_url}/v3/verified_senders/steps_completed"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def verify_sender_token(self, token) -> Any:
        """
        Verifies a sender using the provided token and returns a successful response if valid.

        Args:
            token (string): token

        Returns:
            Any: API response data.

        Tags:
            Sender Verification
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        url = f"{self.base_url}/v3/verified_senders/verify/{token}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_verified_sender(self, id) -> dict[str, Any]:
        """
        Deletes a verified sender with the specified ID using the DELETE method and returns a successful response with a 204 status code if the operation is successful.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Sender Verification
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/verified_senders/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_verified_sender(
        self,
        id,
        address=None,
        address2=None,
        city=None,
        country=None,
        from_email=None,
        from_name=None,
        nickname=None,
        reply_to=None,
        reply_to_name=None,
        state=None,
        zip=None,
    ) -> dict[str, Any]:
        r"""
        Updates specific details of a verified sender identified by \{id\} using partial modifications.

        Args:
            id (string): id
            address (string): address
            address2 (string): address2
            city (string): city
            country (string): country
            from_email (string): from_email
            from_name (string): from_name
            nickname (string): nickname
            reply_to (string): reply_to
            reply_to_name (string): reply_to_name
            state (string): state
            zip (string): zip

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Sender Verification
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "address": address,
            "address2": address2,
            "city": city,
            "country": country,
            "from_email": from_email,
            "from_name": from_name,
            "nickname": nickname,
            "reply_to": reply_to,
            "reply_to_name": reply_to_name,
            "state": state,
            "zip": zip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/verified_senders/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def email_dns_record(
        self, domain_id=None, email=None, link_id=None, message=None
    ) -> Any:
        """
        Creates a new whitelabel DNS configuration for email by submitting the required details in JSON format.

        Args:
            domain_id (integer): The ID of your SendGrid domain record.
            email (string): The email address to send the DNS information to.
            link_id (integer): The ID of the branded link.
            message (string): A custom text block to include in the email body sent with the records.

        Returns:
            Any: API response data.

        Tags:
            Domain Authentication
        """
        request_body = {
            "domain_id": domain_id,
            "email": email,
            "link_id": link_id,
            "message": message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/dns/email"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_authenticated_domain(
        self, limit=None, offset=None, exclude_subusers=None, username=None, domain=None
    ) -> list[Any]:
        """
        Retrieves a list of whitelabel domains for the specified criteria, supporting optional filters by username, domain name, and excluding subusers.

        Args:
            limit (integer): The maximum number of whitelabel domains to return in the response for a single page.
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.
            exclude_subusers (boolean): Indicates whether to exclude domains associated with subusers from the list of retrieved domains.
            username (string): Specifies the username used to filter the whitelabel domains returned in the response.
            domain (string): The "domain" parameter is a string that specifies the domain to be queried for whitelabel domains.

        Returns:
            list[Any]: Success response

        Tags:
            Domain Authentication
        """
        url = f"{self.base_url}/v3/whitelabel/domains"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("exclude_subusers", exclude_subusers),
                ("username", username),
                ("domain", domain),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def authenticate_domain(
        self,
        automatic_security=None,
        custom_dkim_selector=None,
        custom_spf=None,
        default=None,
        domain=None,
        ips=None,
        region=None,
        subdomain=None,
        username=None,
    ) -> dict[str, Any]:
        """
        Creates a new whitelabeled domain using the provided JSON content in the request body, allowing for customized domain configurations.

        Args:
            automatic_security (boolean): Whether to allow SendGrid to manage your SPF records, DKIM keys, and DKIM key rotation.
            custom_dkim_selector (string): Add a custom DKIM selector. Accepts three letters or numbers.
            custom_spf (boolean): Specify whether to use a custom SPF or allow SendGrid to manage your SPF. This option is only available to authenticated domains set up for manual security.
            default (boolean): Whether to use this authenticated domain as the fallback if no authenticated domains match the sender's domain.
            domain (string): Domain being authenticated.
            ips (array): The IP addresses that will be included in the custom SPF record for this authenticated domain.
            region (string): The region of the domain. Allowed values are `global` and `eu`. The default value is `global`.
            subdomain (string): The subdomain to use for this authenticated domain.
            username (string): The username associated with this domain.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        request_body = {
            "automatic_security": automatic_security,
            "custom_dkim_selector": custom_dkim_selector,
            "custom_spf": custom_spf,
            "default": default,
            "domain": domain,
            "ips": ips,
            "region": region,
            "subdomain": subdomain,
            "username": username,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/domains"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_default_authenticated_domain(self, domain=None) -> list[Any]:
        """
        Retrieves the default domain for a whitelabel setup, optionally filtered by a specified domain.

        Args:
            domain (string): The "domain" parameter specifies the domain name to be used for the whitelabel domains default configuration.

        Returns:
            list[Any]: Success response

        Tags:
            Domain Authentication
        """
        url = f"{self.base_url}/v3/whitelabel/domains/default"
        query_params = {k: v for k, v in [("domain", domain)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def disassociate_authenticated_domain_from_user(
        self, username=None
    ) -> dict[str, Any]:
        """
        Removes a domain from the whitelist for the specified subuser and returns no content upon success.

        Args:
            username (string): The "username" query parameter is a string value that specifies the username of the subuser to be deleted from the whitelabel domain.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        url = f"{self.base_url}/v3/whitelabel/domains/subuser"
        query_params = {k: v for k, v in [("username", username)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_authenticated_domain_with_user(self, username) -> dict[str, Any]:
        """
        Get a list of whitelabel domains associated with a specified subuser by providing their username.

        Args:
            username (string): The username of the subuser to retrieve whitelist domain information for, passed as a required query parameter.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        url = f"{self.base_url}/v3/whitelabel/domains/subuser"
        query_params = {k: v for k, v in [("username", username)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_all_authenticated_domain_with_user(self, username) -> list[Any]:
        """
        Retrieves a list of all subusers associated with whitelabel domains for a specified username.

        Args:
            username (string): Required username to filter subusers.

        Returns:
            list[Any]: API response data.

        Tags:
            Domain Authentication
        """
        url = f"{self.base_url}/v3/whitelabel/domains/subuser/all"
        query_params = {k: v for k, v in [("username", username)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_authenticated_domain(self, domain_id) -> dict[str, Any]:
        """
        Deletes a whitelabel domain identified by `{domain_id}` using the DELETE method, returning a successful response with no content.

        Args:
            domain_id (string): domain_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        if domain_id is None:
            raise ValueError("Missing required parameter 'domain_id'")
        url = f"{self.base_url}/v3/whitelabel/domains/{domain_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_authenticated_domain(self, domain_id) -> dict[str, Any]:
        """
        Retrieves details about a specific whitelabeled domain identified by the provided domain ID.

        Args:
            domain_id (string): domain_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        if domain_id is None:
            raise ValueError("Missing required parameter 'domain_id'")
        url = f"{self.base_url}/v3/whitelabel/domains/{domain_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_authenticated_domain(
        self, domain_id, custom_spf=None, default=None
    ) -> list[Any]:
        """
        Updates the settings of an authenticated domain by modifying specified attributes using the PATCH method.

        Args:
            domain_id (string): domain_id
            custom_spf (boolean): Indicates whether to generate a custom SPF record for manual security.
            default (boolean): Indicates whether this is the default authenticated domain.

        Returns:
            list[Any]: Success response

        Tags:
            Domain Authentication
        """
        if domain_id is None:
            raise ValueError("Missing required parameter 'domain_id'")
        request_body = {
            "custom_spf": custom_spf,
            "default": default,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/domains/{domain_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def disassociate_subuser_from_domain(
        self, domain_id, username=None
    ) -> dict[str, Any]:
        """
        Deletes a specified subuser associated with a given whitelabel domain by domain ID and username.

        Args:
            domain_id (string): domain_id
            username (string): The username of the subuser to be deleted from the specified whitelabel domain.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        if domain_id is None:
            raise ValueError("Missing required parameter 'domain_id'")
        url = f"{self.base_url}/v3/whitelabel/domains/{domain_id}/subuser"
        query_params = {k: v for k, v in [("username", username)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def associate_subuser_with_domain(self, domain_id, username=None) -> dict[str, Any]:
        """
        Creates a subuser for the specified domain using the provided JSON data.

        Args:
            domain_id (string): domain_id
            username (string): Username to associate with the authenticated domain.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        if domain_id is None:
            raise ValueError("Missing required parameter 'domain_id'")
        request_body = {
            "username": username,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/domains/{domain_id}/subuser"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def associate_subuser_with_domain_multiple(
        self, domain_id, username=None
    ) -> dict[str, Any]:
        """
        Associates a specific authenticated domain with a subuser using the SendGrid API.

        Args:
            domain_id (string): domain_id
            username (string): Username to associate with the authenticated domain.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        if domain_id is None:
            raise ValueError("Missing required parameter 'domain_id'")
        request_body = {
            "username": username,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/domains/{domain_id}/subuser:add"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_ip_to_authenticated_domain(self, id, ip=None) -> dict[str, Any]:
        """
        Associates IP addresses with a specific authenticated domain using the POST method and returns a status message.

        Args:
            id (string): id
            ip (string): IP to associate with the domain. Used for manually specifying IPs for custom SPF.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "ip": ip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/domains/{id}/ips"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_ip_from_authenticated_domain(self, id, ip) -> dict[str, Any]:
        """
        Deletes an IP address associated with a specific domain in the whitelabel service.

        Args:
            id (string): id
            ip (string): ip

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if ip is None:
            raise ValueError("Missing required parameter 'ip'")
        url = f"{self.base_url}/v3/whitelabel/domains/{id}/ips/{ip}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def validate_authenticated_domain(self, id) -> dict[str, Any]:
        """
        Validates a domain with the specified ID for whitelabel purposes using the provided parameters.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Domain Authentication
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/whitelabel/domains/{id}/validate"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_reverse_dns(self, limit=None, offset=None, ip=None) -> list[Any]:
        """
        Get a list of whitelabel IP addresses with optional filtering by IP, pagination, and on-behalf-of user context.

        Args:
            limit (integer): Defines the maximum number of IP addresses to return in a single response for the GET operation at path "/v3/whitelabel/ips".
            offset (integer): The number of items in the list to skip over before starting to retrieve the items for the requested page. The default `offset` of `0` represents the beginning of the list, i.e. the start of the first page. To request the second page of the list, set the `offset` to the page size as determined by `limit`. Use multiples of the page size as your `offset` to request further consecutive pages. E.g. assume your page size is set to `10`. An `offset` of `10` requests the second page, an `offset` of `20` requests the third page and so on, provided there are sufficiently many items in your list.
            ip (string): Specifies the IP address to filter whitelabel IP results by in the request.

        Returns:
            list[Any]: API response data.

        Tags:
            Reverse DNS
        """
        url = f"{self.base_url}/v3/whitelabel/ips"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("offset", offset), ("ip", ip)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_up_reverse_dns(
        self, domain=None, ip=None, subdomain=None
    ) -> dict[str, Any]:
        """
        Adds IP addresses to a whitelist using the "POST" method at the "/v3/whitelabel/ips" path, allowing specified IP addresses to access certain resources.

        Args:
            domain (string): The root, or sending, domain that will be used to send message from the IP address.
            ip (string): The IP address for which you want to set up reverse DNS.
            subdomain (string): The subdomain that will be used to send emails from the IP address. This should be the same as the subdomain used to set up an authenticated domain.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Reverse DNS
        """
        request_body = {
            "domain": domain,
            "ip": ip,
            "subdomain": subdomain,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/ips"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_reverse_dns(self, id) -> dict[str, Any]:
        """
        Deletes the specified whitelabel IP address identified by its ID and returns a 204 No Content status upon successful removal.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Reverse DNS
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/whitelabel/ips/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_reverse_dns(self, id) -> dict[str, Any]:
        """
        Retrieves information about a specific whitelabel IP address identified by its ID using the "GET" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Reverse DNS
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/whitelabel/ips/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def validate_reverse_dns(self, id) -> dict[str, Any]:
        """
        Validates a specified IP address for whitelabeling using the POST method and returns a validation result.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Reverse DNS
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/whitelabel/ips/{id}/validate"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_branded_link(self, limit=None) -> list[Any]:
        """
        Retrieves a list of whitelabeled links, allowing optional filtering by a specified limit and execution on behalf of another entity.

        Args:
            limit (integer): Specifies the maximum number of whitelabel links to return in a single response.

        Returns:
            list[Any]: API response data.

        Tags:
            Link Branding
        """
        url = f"{self.base_url}/v3/whitelabel/links"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_branded_link(
        self, default=None, domain=None, region=None, subdomain=None
    ) -> dict[str, Any]:
        """
        Creates a new whitelabel link resource using the provided JSON payload and returns a 201 status code upon successful creation.

        Args:
            default (boolean): default
            domain (string): The root domain for the subdomain that you are creating the link branding for. This should match your FROM email address.
            region (string): region
            subdomain (string): The subdomain to create the link branding for. Must be different from the subdomain you used for authenticating your domain.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        request_body = {
            "default": default,
            "domain": domain,
            "region": region,
            "subdomain": subdomain,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/links"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_default_branded_link(self, domain=None) -> dict[str, Any]:
        """
        Retrieves the default whitelabel link for a specified domain using the "GET" method.

        Args:
            domain (string): The "domain" parameter is a string value used in the query to specify the domain for which default whitelabel links are retrieved.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        url = f"{self.base_url}/v3/whitelabel/links/default"
        query_params = {k: v for k, v in [("domain", domain)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def disassociate_branded_link_from_subuser(self, username) -> dict[str, Any]:
        """
        Deletes a subuser link for a specified whitelabel using the provided username and returns no content upon successful deletion.

        Args:
            username (string): Specifies the username of the subuser whose whitelabel link should be deleted.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        url = f"{self.base_url}/v3/whitelabel/links/subuser"
        query_params = {k: v for k, v in [("username", username)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_subuser_branded_link(self, username) -> dict[str, Any]:
        """
        Retrieves and provides information about a subuser in the context of whitelabel links using the "GET" method, requiring a username as a query parameter.

        Args:
            username (string): Specifies the username of the subuser for which the whitelabel links are retrieved.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        url = f"{self.base_url}/v3/whitelabel/links/subuser"
        query_params = {k: v for k, v in [("username", username)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_branded_link(self, id) -> dict[str, Any]:
        """
        Deletes a whitelabel link specified by the `{id}` parameter and returns a successful response without content.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/whitelabel/links/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_branded_link(self, id) -> dict[str, Any]:
        """
        Retrieves the details of a whitelabel link specified by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/whitelabel/links/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_branded_link(self, id, default=None) -> dict[str, Any]:
        """
        Partially updates a whitelabel link by ID using JSON data and returns a success response.

        Args:
            id (string): id
            default (boolean): default

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "default": default,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/links/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def validate_branded_link(self, id) -> dict[str, Any]:
        """
        Validates a specific whitelabel link by ID using the "POST" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/v3/whitelabel/links/{id}/validate"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def associate_branded_link_with_subuser(
        self, link_id, username=None
    ) -> dict[str, Any]:
        """
        Creates a new subuser link for the specified whitelabel link ID using a JSON request body and returns a success response.

        Args:
            link_id (string): link_id
            username (string): The username of the subuser account that you want to associate the branded link with.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Link Branding
        """
        if link_id is None:
            raise ValueError("Missing required parameter 'link_id'")
        request_body = {
            "username": username,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v3/whitelabel/links/{link_id}/subuser"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.list_access_activity,
            self.delete_allowed_ips,
            self.list_allowed_ip,
            self.add_ip_to_allow_list,
            self.delete_allowed_ip,
            self.get_allowed_ip,
            self.list_alert,
            self.create_alert,
            self.delete_alert,
            self.get_alert,
            self.update_alert,
            self.list_api_key,
            self.create_api_key,
            self.delete_api_key,
            self.get_api_key,
            self.update_api_key_name,
            self.update_api_key,
            self.list_asm_group,
            self.creat_asm_group,
            self.delete_asm_group,
            self.get_asm_group,
            self.update_asm_group,
            self.list_suppression_from_asm_group,
            self.add_suppression_to_asm_group,
            self.search_suppression_from_asm_group,
            self.delete_suppression_from_asm_group,
            self.list_asm_suppression,
            self.create_global_suppression,
            self.delete_global_suppression,
            self.get_global_suppression,
            self.get_asm_suppression,
            self.list_browser_stat,
            self.list_campaign,
            self.create_campaign,
            self.delete_campaign,
            self.get_campaign,
            self.update_campaign,
            self.un_schedule_campaign,
            self.get_scheduled_campaign,
            self.update_scheduled_campaign,
            self.schedule_campaign,
            self.send_campaign,
            self.send_test_campaign,
            self.list_category,
            self.list_category_stat,
            self.list_category_stat_sum,
            self.list_client_stat,
            self.get_client_stat,
            self.list_custom_field,
            self.create_custom_field,
            self.delete_custom_field,
            self.get_custom_field,
            self.delete_contact_db_lists,
            self.list_contact_db_list,
            self.create_contact_db_list,
            self.delete_contact_db_list,
            self.get_contact_db_list,
            self.update_contact_db_list,
            self.list_recipients_from_contact_db_list,
            self.add_recipients_to_contact_db_list,
            self.delete_recipient_from_contact_db_list,
            self.add_recipient_to_contact_db_list,
            self.delete_recipients,
            self.list_recipient,
            self.update_recipient,
            self.add_recipient,
            self.get_billable,
            self.list_recipient_count,
            self.list_search_recipient,
            self.search_recipient,
            self.delete_recipient,
            self.get_recipient,
            self.get_recipient_list,
            self.list_reserved_field,
            self.list_segment,
            self.delete_segment,
            self.list_recipient_for_segment,
            self.list_status,
            self.list_design,
            self.create_design,
            self.list_pre_built_design,
            self.get_pre_built_design,
            self.duplicate_pre_built_design,
            self.delete_design,
            self.get_design,
            self.update_design,
            self.duplicate_design,
            self.list_device_stat,
            self.list_engagement_quality_score,
            self.list_subuser_engagement_quality_score,
            self.list_geo_stat,
            self.list_ip,
            self.list_assigned_ip,
            self.add_ip_to_ip_pool,
            self.delete_ip_from_ip_pool,
            self.list_remaining_ip_count,
            self.list_warm_up_ip,
            self.warm_up_ip,
            self.stop_ip_warm_up,
            self.get_warm_up_ip,
            self.create_mail_batch,
            self.get_mail_batch,
            self.send_mail,
            self.list_mail_setting,
            self.list_address_whitelist,
            self.update_address_whitelist,
            self.list_bounce_purge,
            self.update_bounce_purge,
            self.list_footer,
            self.update_footer,
            self.list_forward_bounce,
            self.update_forward_bounce,
            self.list_forward_spam,
            self.update_forward_spam,
            self.list_mailbox_provider_stat,
            self.list_contact,
            self.update_contact,
            self.list_batched_contact,
            self.list_export_contact,
            self.export_contact,
            self.get_export_contact,
            self.import_contact,
            self.get_import_contact,
            self.search_contact,
            self.list_contact_by_email,
            self.get_contact_by_identifiers,
            self.delete_contact_identifier,
            self.get_contact,
            self.list_field_definition,
            self.create_field_definition,
            self.delete_field_definition,
            self.update_field_definition,
            self.delete_integration,
            self.get_integrations_by_user,
            self.add_integration,
            self.find_integration_by_id,
            self.update_integration,
            self.create_marketing_list,
            self.delete_marketing_list,
            self.get_marketing_list,
            self.update_marketing_list,
            self.delete_contact,
            self.list_contact_count,
            self.list_marketing_segment,
            self.create_segment,
            self.refresh_segment,
            self.update_segment,
            self.get_segment,
            self.list_sender,
            self.delete_sender,
            self.update_sender,
            self.delete_single_sends,
            self.list_single_send,
            self.create_single_send,
            self.search_single_send,
            self.delete_single_send,
            self.get_single_send,
            self.update_single_send,
            self.duplicate_single_send,
            self.delete_scheduled_single_send,
            self.schedule_single_send,
            self.list_automation_stat,
            self.export_automation_stat,
            self.get_automation_stat,
            self.list_click_tracking_stat,
            self.list_single_send_stat,
            self.export_single_send_stat,
            self.get_single_send_stat,
            self.list_single_send_tracking_stat,
            self.send_test_marketing_email,
            self.list_message,
            self.request_csv,
            self.download_csv,
            self.get_message,
            self.list_partner_setting,
            self.create_account,
            self.delete_account,
            self.list_account_offering,
            self.update_account_offering,
            self.authenticate_account,
            self.get_account_state,
            self.update_account_state,
            self.list_offering,
            self.erase_recipient_email_data,
            self.list_scope,
            self.list_scope_request,
            self.deny_scope_request,
            self.approve_scope_request,
            self.add_ip,
            self.get_ip,
            self.update_ip,
            self.list_sub_user_assigned_to_ip,
            self.add_sub_users_to_ip,
            self.delete_sub_users_from_ip,
            self.list_ip_pool,
            self.create_ip_pool,
            self.delete_ip_pool,
            self.get_ip_pool,
            self.update_ip_pool,
            self.list_ip_assigned_to_ip_pool,
            self.add_ips_to_ip_pool,
            self.delete_ips_from_ip_pool,
            self.create_sender,
            self.get_sender,
            self.reset_sender_verification,
            self.create_sso_certificate,
            self.delete_sso_certificate,
            self.get_sso_certificate,
            self.update_sso_certificate,
            self.list_sso_integration,
            self.create_sso_integration,
            self.delete_sso_integration,
            self.get_sso_integration,
            self.update_sso_integration,
            self.list_sso_integration_certificate,
            self.create_sso_teammate,
            self.update_sso_teammate,
            self.list_subuser,
            self.create_subuser,
            self.list_reputation,
            self.list_stat,
            self.list_monthly_stat,
            self.list_stat_sum,
            self.delete_subuser,
            self.update_subuser,
            self.get_subuser_credit,
            self.update_subuser_credit,
            self.update_subuser_remaining_credit,
            self.update_subuser_ip,
            self.list_subuser_monthly_stat,
            self.update_subuser_website_access,
            self.delete_suppression_blocks,
            self.list_suppression_block,
            self.delete_suppression_block,
            self.get_suppression_block,
            self.delete_suppression_bounces,
            self.list_suppression_bounces,
            self.list_suppression_bounces_classifications,
            self.get_suppression_bounces_classifications,
            self.delete_suppression_bounce,
            self.get_suppression_bounces,
            self.delete_invalid_emails,
            self.list_invalid_email,
            self.delete_invalid_email,
            self.get_invalid_email,
            self.delete_spam_reports,
            self.list_spam_report,
            self.delete_spam_report,
            self.get_spam_report,
            self.list_global_suppression,
            self.list_teammate,
            self.invite_teammate,
            self.list_pending_teammate,
            self.delete_pending_teammate,
            self.resend_teammate_invite,
            self.list_subuser_by_template,
            self.delete_teammate,
            self.get_teammate,
            self.update_teammate,
            self.list_template,
            self.create_template,
            self.delete_template,
            self.get_template,
            self.update_template,
            self.duplicate_template,
            self.create_template_version,
            self.delete_template_version,
            self.get_template_version,
            self.activate_template_version,
            self.list_tracking_setting,
            self.list_click_tracking_setting,
            self.update_click_tracking_setting,
            self.list_google_analytics_tracking_setting,
            self.update_google_analytics_tracking_setting,
            self.list_open_tracking_setting,
            self.update_open_tracking_setting,
            self.list_subscription_tracking_setting,
            self.update_subscription_tracking_setting,
            self.list_account,
            self.list_credit,
            self.list_email,
            self.update_email,
            self.update_password,
            self.list_profile,
            self.update_profile,
            self.list_scheduled_send,
            self.create_scheduled_send,
            self.delete_scheduled_send,
            self.get_scheduled_send,
            self.update_scheduled_send,
            self.list_enforced_tls_setting,
            self.update_enforced_tls_setting,
            self.list_username,
            self.update_username,
            self.create_event_webhook,
            self.list_event_webhook,
            self.get_signed_event_webhook,
            self.update_signed_event_webhook,
            self.delete_event_webhook,
            self.get_event_webhook,
            self.update_event_webhook,
            self.test_event_webhook,
            self.list_parse_setting,
            self.create_parse_setting,
            self.delete_parse_setting,
            self.get_parse_setting,
            self.update_parse_setting,
            self.list_parse_static,
            self.validate_email,
            self.get_validations_email_jobs,
            self.list_email_job_for_verification,
            self.get_email_job_for_verification,
            self.list_verified_sender,
            self.create_verified_sender,
            self.list_verified_sender_domain,
            self.resend_verified_sender,
            self.list_verified_sender_steps_completed,
            self.verify_sender_token,
            self.delete_verified_sender,
            self.update_verified_sender,
            self.email_dns_record,
            self.list_authenticated_domain,
            self.authenticate_domain,
            self.list_default_authenticated_domain,
            self.disassociate_authenticated_domain_from_user,
            self.list_authenticated_domain_with_user,
            self.list_all_authenticated_domain_with_user,
            self.delete_authenticated_domain,
            self.get_authenticated_domain,
            self.update_authenticated_domain,
            self.disassociate_subuser_from_domain,
            self.associate_subuser_with_domain,
            self.associate_subuser_with_domain_multiple,
            self.add_ip_to_authenticated_domain,
            self.delete_ip_from_authenticated_domain,
            self.validate_authenticated_domain,
            self.list_reverse_dns,
            self.set_up_reverse_dns,
            self.delete_reverse_dns,
            self.get_reverse_dns,
            self.validate_reverse_dns,
            self.list_branded_link,
            self.create_branded_link,
            self.list_default_branded_link,
            self.disassociate_branded_link_from_subuser,
            self.list_subuser_branded_link,
            self.delete_branded_link,
            self.get_branded_link,
            self.update_branded_link,
            self.validate_branded_link,
            self.associate_branded_link_with_subuser,
        ]
