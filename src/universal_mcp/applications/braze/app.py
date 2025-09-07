from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class BrazeApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="braze", integration=integration, **kwargs)
        self.base_url = "https://rest.iad-01.braze.com"

    def update_email_template(
        self,
        email_template_id: str | None = None,
        template_name: str | None = None,
        subject: str | None = None,
        body: str | None = None,
        plaintext_body: str | None = None,
        preheader: str | None = None,
        tags: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Update Email Template

        Args:
            email_template_id (string): email_template_id Example: 'email_template_id'.
            template_name (string): template_name Example: 'Weekly Newsletter'.
            subject (string): subject Example: "This Week's Styles".
            body (string): body Example: "Check out this week's digital lookbook to inspire your outfits. Take a look at https://www.braze.com/".
            plaintext_body (string): plaintext_body Example: 'This is the updated text within my email body and here is a link to https://www.braze.com/.'.
            preheader (string): preheader Example: 'We want you to have the best looks this Summer'.
            tags (array): tags Example: ['Tag1', 'Tag2'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates > Email Templates
        """
        request_body_data = None
        request_body_data = {
            "email_template_id": email_template_id,
            "template_name": template_name,
            "subject": subject,
            "body": body,
            "plaintext_body": plaintext_body,
            "preheader": preheader,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/templates/email/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def track_user_activity(
        self,
        attributes: list[dict[str, Any]] | None = None,
        events: list[dict[str, Any]] | None = None,
        purchases: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Track Users

        Args:
            attributes (array): attributes Example: [{'external_id': 'rachel_feinberg', 'string_attribute': 'fruit', 'boolean_attribute_1': True, 'integer_attribute': 25, 'array_attribute': ['banana', 'apple']}].
            events (array): events Example: [{'external_id': 'user_identifier', 'app_id': 'your_app_identifier', 'name': 'rented_movie', 'time': '2022-12-06T19:20:45+01:00', 'properties': {'release': {'studio': 'FilmStudio', 'year': '2022'}, 'cast': [{'name': 'Actor1'}, {'name': 'Actor2'}]}}, {'user_alias': {'alias_name': 'device123', 'alias_label': 'my_device_identifier'}, 'app_id': 'your_app_identifier', 'name': 'rented_movie', 'time': '2013-07-16T19:20:50+01:00'}].
            purchases (array): purchases Example: [{'external_id': 'user_identifier', 'app_id': 'your_app_identifier', 'product_id': 'product_name', 'currency': 'USD', 'price': 12.12, 'quantity': 6, 'time': '2017-05-12T18:47:12Z', 'properties': {'color': 'red', 'monogram': 'ABC', 'checkout_duration': 180, 'size': 'Large', 'brand': 'Backpack Locker'}}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User Data
        """
        request_body_data = None
        request_body_data = {
            "attributes": attributes,
            "events": events,
            "purchases": purchases,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/track"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_catalog_by_name(self, catalog_name: str) -> dict[str, Any]:
        """
        Delete Catalog

        Args:
            catalog_name (string): catalog_name

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Management > Synchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        url = f"{self.base_url}/catalogs/{catalog_name}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_catalogs(self) -> dict[str, Any]:
        """
        List Catalogs

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Management > Synchronous, important
        """
        url = f"{self.base_url}/catalogs"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_catalog(
        self, catalogs: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Create Catalog

        Args:
            catalogs (array): catalogs Example: [{'name': 'restaurants', 'description': 'My Restaurants', 'fields': [{'name': 'id', 'type': 'string'}]}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Management > Synchronous, important
        """
        request_body_data = None
        request_body_data = {
            "catalogs": catalogs,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/catalogs"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_catalog_item(self, catalog_name: str) -> dict[str, Any]:
        """
        Delete Multiple Catalog Items

        Args:
            catalog_name (string): catalog_name

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Asynchronous, important
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        url = f"{self.base_url}/catalogs/{catalog_name}/items"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def edit_catalog_item(
        self, catalog_name: str, items: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Edit Multiple Catalog Items

        Args:
            catalog_name (string): catalog_name
            items (array): items Example: [{'id': 'restaurant1'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Asynchronous, important
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        request_body_data = None
        request_body_data = {
            "items": items,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/catalogs/{catalog_name}/items"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_catalog_item(
        self, catalog_name: str, items: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Create Multiple Catalog Items

        Args:
            catalog_name (string): catalog_name
            items (array): items Example: [{'id': 'restaurant1', 'Name': 'Restaurant1', 'City': 'New York', 'Cuisine': 'American', 'Rating': 5, 'Loyalty_Program': True, 'Created_At': '2022-11-01T09:03:19.967+00:00'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Asynchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        request_body_data = None
        request_body_data = {
            "items": items,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/catalogs/{catalog_name}/items"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_catalog_items(
        self, catalog_name: str, items: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Update Catalog Item

        Args:
            catalog_name (string): catalog_name
            items (array): items Example: [{'Name': 'Restaurant', 'Loyalty_Program': False, 'Location': {'Latitude': 33.6112, 'Longitude': -117.8711}, 'Open_Time': '2021-09-03T09:03:19.967+00:00'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Asynchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        request_body_data = None
        request_body_data = {
            "items": items,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/catalogs/{catalog_name}/items"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_catalog_items(self, catalog_name: str) -> dict[str, Any]:
        """
        List Multiple Catalog Item Details

        Args:
            catalog_name (string): catalog_name

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Synchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        url = f"{self.base_url}/catalogs/{catalog_name}/items"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_catalog_item_by_id(
        self, catalog_name: str, item_id: str
    ) -> dict[str, Any]:
        """
        Delete a Catalog Item

        Args:
            catalog_name (string): catalog_name
            item_id (string): item_id

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Synchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'.")
        url = f"{self.base_url}/catalogs/{catalog_name}/items/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_item_detail(self, catalog_name: str, item_id: str) -> dict[str, Any]:
        """
        List Catalog Item Details

        Args:
            catalog_name (string): catalog_name
            item_id (string): item_id

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Synchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'.")
        url = f"{self.base_url}/catalogs/{catalog_name}/items/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_catalog_item_by_id(
        self,
        catalog_name: str,
        item_id: str,
        items: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Edit Catalog Items

        Args:
            catalog_name (string): catalog_name
            item_id (string): item_id
            items (array): items Example: [{'Name': 'Restaurant', 'Loyalty_Program': False, 'Open_Time': '2021-09-03T09:03:19.967+00:00'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Synchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'.")
        request_body_data = None
        request_body_data = {
            "items": items,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/catalogs/{catalog_name}/items/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def add_catalog_item_by_id(
        self,
        catalog_name: str,
        item_id: str,
        items: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Create Catalog Item

        Args:
            catalog_name (string): catalog_name
            item_id (string): item_id
            items (array): items Example: [{'Name': 'Restaurant1', 'City': 'New York', 'Cuisine': 'American', 'Rating': 5, 'Loyalty_Program': True, 'Created_At': '2022-11-01T09:03:19.967+00:00'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Synchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'.")
        request_body_data = None
        request_body_data = {
            "items": items,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/catalogs/{catalog_name}/items/{item_id}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_catalog_item(
        self,
        catalog_name: str,
        item_id: str,
        items: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Update Catalog Item

        Args:
            catalog_name (string): catalog_name
            item_id (string): item_id
            items (array): items Example: [{'Name': 'Restaurant', 'Loyalty_Program': False, 'Location': {'Latitude': 33.6112, 'Longitude': -117.8711}, 'Open_Time': '2021-09-03T09:03:19.967+00:00'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Catalogs > Catalog Items > Synchronous
        """
        if catalog_name is None:
            raise ValueError("Missing required parameter 'catalog_name'.")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'.")
        request_body_data = None
        request_body_data = {
            "items": items,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/catalogs/{catalog_name}/items/{item_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_hard_bounces(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        email: str | None = None,
    ) -> dict[str, Any]:
        """
        Query Hard Bounced Emails

        Args:
            start_date (string): (Optional*) String in YYYY-MM-DD format Start date of the range to retrieve hard bounces, must be earlier than `end_date`. This is treated as midnight in UTC time by the API. *You must provide either an `email` or a `start_date`, and an `end_date`. Example: '2019-01-01'.
            end_date (string): (Optional*) String in YYYY-MM-DD format String in YYYY-MM-DD format. End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API. *You must provide either an `email` or a `start_date`, and an `end_date`. Example: '2019-02-01'.
            limit (integer): (Optional) Integer Optional field to limit the number of results returned. Defaults to 100, maximum is 500. Example: '100'.
            offset (integer): (Optional) Integer Optional beginning point in the list to retrieve from. Example: '1'.
            email (string): (Optional*) String If provided, we will return whether or not the user has hard bounced. *You must provide either an `email` or a `start_date`, and an `end_date`. Example: 'example@braze.com'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email Lists & Addresses
        """
        url = f"{self.base_url}/email/hard_bounces"
        query_params = {
            k: v
            for k, v in [
                ("start_date", start_date),
                ("end_date", end_date),
                ("limit", limit),
                ("offset", offset),
                ("email", email),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_unsubscribes(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort_direction: str | None = None,
        email: str | None = None,
    ) -> dict[str, Any]:
        """
        Query List of Unsubscribed Email Addresses

        Args:
            start_date (string): (Optional*) String in YYYY-MM-DD format Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API. Example: '2020-01-01'.
            end_date (string): (Optional*) String in YYYY-MM-DD format End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API. Example: '2020-02-01'.
            limit (integer): (Optional) Integer Optional field to limit the number of results returned. Limit must be greater than 1. Defaults to 100, maximum is 500. Example: '1'.
            offset (integer): (Optional) Integer Optional beginning point in the list to retrieve from. Example: '1'.
            sort_direction (string): (Optional) String Pass in the value `asc` to sort unsubscribes from oldest to newest. Pass in `desc` to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest. Example: 'desc'.
            email (string): (Optional*) String If provided, we will return whether or not the user has unsubscribed. Example: 'example@braze.com'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email Lists & Addresses
        """
        url = f"{self.base_url}/email/unsubscribes"
        query_params = {
            k: v
            for k, v in [
                ("start_date", start_date),
                ("end_date", end_date),
                ("limit", limit),
                ("offset", offset),
                ("sort_direction", sort_direction),
                ("email", email),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_email_status(
        self, email: str | None = None, subscription_state: str | None = None
    ) -> dict[str, Any]:
        """
        Change Email Subscription Status

        Args:
            email (string): email Example: 'example@braze.com'.
            subscription_state (string): subscription_state Example: 'subscribed'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email Lists & Addresses
        """
        request_body_data = None
        request_body_data = {
            "email": email,
            "subscription_state": subscription_state,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/email/status"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def remove_bounced_email(self, email: str | None = None) -> dict[str, Any]:
        """
        Remove Hard Bounced Emails

        Args:
            email (string): email Example: 'example@braze.com'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email Lists & Addresses
        """
        request_body_data = None
        request_body_data = {
            "email": email,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/email/bounce/remove"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def remove_email_spam(self, email: str | None = None) -> dict[str, Any]:
        """
        Remove Email Addresses from Spam List

        Args:
            email (string): email Example: 'example@braze.com'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email Lists & Addresses
        """
        request_body_data = None
        request_body_data = {
            "email": email,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/email/spam/remove"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def add_email_to_blocklist(self, email: list[str] | None = None) -> dict[str, Any]:
        """
        Blocklist Email Addresses

        Args:
            email (array): email Example: ['blocklist_email1', 'blocklist_email2'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email Lists & Addresses
        """
        request_body_data = None
        request_body_data = {
            "email": email,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/email/blocklist"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def add_to_blacklist(self, email: list[str] | None = None) -> dict[str, Any]:
        """
        Blacklist Email Addresses

        Args:
            email (array): email Example: ['blacklist_email1', 'blacklist_email2'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email Lists & Addresses
        """
        request_body_data = None
        request_body_data = {
            "email": email,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/email/blacklist"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_campaign_data_series(
        self,
        campaign_id: str | None = None,
        length: int | None = None,
        ending_at: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Campaign Analytics

        Args:
            campaign_id (string): (Required) String See [campaign API identifier]( The `campaign_id` for API campaigns can be found at **Settings > Setup and Testing > API Keys** and the **Campaign Details** page within your dashboard, or you can use the [List campaigns endpoint]( Example: '{{campaign_identifier}}'.
            length (integer): (Required) Integer Max number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). Example: '7'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string) Date on which the data series should end. Defaults to time of the request. Example: '2020-06-28T23:59:59-5:00'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Campaign
        """
        url = f"{self.base_url}/campaigns/data_series"
        query_params = {
            k: v
            for k, v in [
                ("campaign_id", campaign_id),
                ("length", length),
                ("ending_at", ending_at),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_campaign_details(self, campaign_id: str | None = None) -> dict[str, Any]:
        """
        Export Campaign Details

        Args:
            campaign_id (string): (Required) String See [campaign API identifier]( The `campaign_id` for API campaigns can be found on the **Settings > Setup and Testing > API Keys** and the campaign details page within your dashboard, or you can use the [Campaign List Endpoint]( Example: '{{campaign_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Campaign
        """
        url = f"{self.base_url}/campaigns/details"
        query_params = {
            k: v for k, v in [("campaign_id", campaign_id)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_campaigns(
        self,
        page: int | None = None,
        include_archived: bool | None = None,
        sort_direction: str | None = None,
        last_edit_time_gt: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Campaign List

        Args:
            page (integer): (Optional) Integer The page of campaigns to return, defaults to 0 (returns the first set of up to 100).
            include_archived (boolean): (Optional) Boolean Whether or not to include archived campaigns, defaults to false.
            sort_direction (string): (Optional) String - Sort creation time from newest to oldest: pass in the value `desc`.
        - Sort creation time from oldest to newest: pass in the value `asc`. If `sort_direction` is not included, the default order is oldest to newest. Example: 'desc'.
            last_edit_time_gt (string): (Optional) Datetime ([ISO 8601]( string) Filters the results and only returns campaigns that were edited greater than the time provided till now. Format is `yyyy-MM-DDTHH:mm:ss`. Example: '2020-06-28T23:59:59-5:00'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Campaign
        """
        url = f"{self.base_url}/campaigns/list"
        query_params = {
            k: v
            for k, v in [
                ("page", page),
                ("include_archived", include_archived),
                ("sort_direction", sort_direction),
                ("last_edit.time[gt]", last_edit_time_gt),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_send_data_series(
        self,
        campaign_id: str | None = None,
        send_id: str | None = None,
        length: int | None = None,
        ending_at: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Send Analytics

        Args:
            campaign_id (string): (Required) String See [Campaign API identifier]( Example: '{{campaign_identifier}}'.
            send_id (string): (Required) String See [Send API identifier]( Example: '{{send_identifier}}'.
            length (integer): (Required) Integer Max number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). Example: '30'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string) Date on which the data series should end. Defaults to time of the request. Example: '2014-12-10T23:59:59-05:00'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Campaign
        """
        url = f"{self.base_url}/sends/data_series"
        query_params = {
            k: v
            for k, v in [
                ("campaign_id", campaign_id),
                ("send_id", send_id),
                ("length", length),
                ("ending_at", ending_at),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_canvas_data_series(
        self,
        canvas_id: str | None = None,
        ending_at: str | None = None,
        starting_at: str | None = None,
        length: int | None = None,
        include_variant_breakdown: bool | None = None,
        include_step_breakdown: bool | None = None,
        include_deleted_step_data: bool | None = None,
    ) -> dict[str, Any]:
        """
        Export Canvas Data Series Analytics

        Args:
            canvas_id (string): (Required) String See [Canvas API Identifier]( Example: '{{canvas_id}}'.
            ending_at (string): (Required) Datetime ([ISO 8601]( string) Date on which the data export should end. Defaults to time of the request. Example: '2018-05-30T23:59:59-5:00'.
            starting_at (string): (Optional*) Datetime ([ISO 8601]( string) Date on which the data export should begin. *Either `length` or `starting_at` is required. Example: '2018-05-28T23:59:59-5:00'.
            length (integer): (Optional*) String Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 14 (inclusive). *Either `length` or `starting_at` is required. Example: '10'.
            include_variant_breakdown (boolean): (Optional) Boolean Whether or not to include variant stats (defaults to false). Example: 'True'.
            include_step_breakdown (boolean): (Optional) Boolean Whether or not to include step stats (defaults to false). Example: 'True'.
            include_deleted_step_data (boolean): (Optional) Boolean Whether or not to include step stats for deleted steps (defaults to false). Example: 'True'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Canvas
        """
        url = f"{self.base_url}/canvas/data_series"
        query_params = {
            k: v
            for k, v in [
                ("canvas_id", canvas_id),
                ("ending_at", ending_at),
                ("starting_at", starting_at),
                ("length", length),
                ("include_variant_breakdown", include_variant_breakdown),
                ("include_step_breakdown", include_step_breakdown),
                ("include_deleted_step_data", include_deleted_step_data),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def fetch_canvas_data_summary(
        self,
        canvas_id: str | None = None,
        ending_at: str | None = None,
        starting_at: str | None = None,
        length: int | None = None,
        include_variant_breakdown: bool | None = None,
        include_step_breakdown: bool | None = None,
        include_deleted_step_data: bool | None = None,
    ) -> dict[str, Any]:
        """
        Export Canvas Data Analytics Summary

        Args:
            canvas_id (string): (Required) String See [Canvas API identifier]( Example: '{{canvas_id}}'.
            ending_at (string): (Required) Datetime ([ISO 8601]( string)
        Date on which the data export should end. Defaults to time of the request Example: '2018-05-30T23:59:59-5:00'.
            starting_at (string): (Optional*) Datetime ([ISO 8601]( string) Date on which the data export should begin. *Either `length` or `starting_at` is required. Example: '2018-05-28T23:59:59-5:00'.
            length (integer): (Optional*) Integer Max number of days before `ending_at` to include in the returned series. Must be between 1 and 14 (inclusive). *Either `length` or `starting_at` is required. Example: '5'.
            include_variant_breakdown (boolean): (Optional) Boolean Whether or not to include variant stats (defaults to false). Example: 'True'.
            include_step_breakdown (boolean): (Optional) Boolean Whether or not to include step stats (defaults to false). Example: 'True'.
            include_deleted_step_data (boolean): (Optional) Boolean Whether or not to include step stats for deleted steps (defaults to false). Example: 'True'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Canvas
        """
        url = f"{self.base_url}/canvas/data_summary"
        query_params = {
            k: v
            for k, v in [
                ("canvas_id", canvas_id),
                ("ending_at", ending_at),
                ("starting_at", starting_at),
                ("length", length),
                ("include_variant_breakdown", include_variant_breakdown),
                ("include_step_breakdown", include_step_breakdown),
                ("include_deleted_step_data", include_deleted_step_data),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_canvas_details(self, canvas_id: str | None = None) -> dict[str, Any]:
        """
        Export Canvas Details

        Args:
            canvas_id (string): (Required) String See [Canvas API Identifier]( Example: '{{canvas_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Canvas
        """
        url = f"{self.base_url}/canvas/details"
        query_params = {k: v for k, v in [("canvas_id", canvas_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_canvas(
        self,
        page: int | None = None,
        include_archived: bool | None = None,
        sort_direction: str | None = None,
        last_edit_time_gt: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Canvas List

        Args:
            page (integer): (Optional) Integer The page of Canvases to return, defaults to `0` (returns the first set of up to 100). Example: '1'.
            include_archived (boolean): (Optional) Boolean Whether or not to include archived Canvases, defaults to `false`.
            sort_direction (string): (Optional) String - Sort creation time from newest to oldest: pass in the value `desc`.
        - Sort creation time from oldest to newest: pass in the value `asc`. If `sort_direction` is not included, the default order is oldest to newest. Example: 'desc'.
            last_edit_time_gt (string): (Optional) Datetime ([ISO 8601]( string) Filters the results and only returns Canvases that were edited greater than the time provided till now. Format is `yyyy-MM-DDTHH:mm:ss`. Example: '2020-06-28T23:59:59-5:00'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Canvas
        """
        url = f"{self.base_url}/canvas/list"
        query_params = {
            k: v
            for k, v in [
                ("page", page),
                ("include_archived", include_archived),
                ("sort_direction", sort_direction),
                ("last_edit.time[gt]", last_edit_time_gt),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_events(self, page: int | None = None) -> dict[str, Any]:
        """
        Export Custom Events List

        Args:
            page (integer): (Optional) Integer The page of event names to return, defaults to 0 (returns the first set of up to 250). Example: '3'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Custom Events, important
        """
        url = f"{self.base_url}/events/list"
        query_params = {k: v for k, v in [("page", page)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def fetch_event_series_data(
        self,
        event: str | None = None,
        length: int | None = None,
        unit: str | None = None,
        ending_at: str | None = None,
        app_id: str | None = None,
        segment_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Custom Events Analytics

        Args:
            event (string): (Required) String The name of the custom event for which to return analytics. Example: 'event_name'.
            length (integer): (Required) Integer Maximum number of units (days or hours) before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). Example: '24'.
            unit (string): (Optional) String Unit of time between data points - can be `day` or `hour`, defaults to `day`. Example: 'hour'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string) Date on which the data series should end. Defaults to time of the request. Example: '2014-12-10T23:59:59-05:00'.
            app_id (string): (Optional) String App API identifier retrieved from **Settings > Setup and Testing > API Keys** to limit analytics to a specific app. Example: '{{app_identifier}}'.
            segment_id (string): (Optional) String See [Segment API identifier]( Segment ID indicating the analytics-enabled segment for which event analytics should be returned. Example: '{{segment_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Custom Events
        """
        url = f"{self.base_url}/events/data_series"
        query_params = {
            k: v
            for k, v in [
                ("event", event),
                ("length", length),
                ("unit", unit),
                ("ending_at", ending_at),
                ("app_id", app_id),
                ("segment_id", segment_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_new_user_kpi_series(
        self,
        length: int | None = None,
        ending_at: str | None = None,
        app_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Daily New Users by Date

        Args:
            length (integer): (Required) Integer Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). Example: '14'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string) Date on which the data series should end. Defaults to time of the request. Example: '2018-06-28T23:59:59-5:00'.
            app_id (string): (Optional) String App API identifier retrieved from **Settings > Setup and Testing > API Keys**. If excluded, results for all apps in workspace will be returned. Example: '{{app_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > KPI
        """
        url = f"{self.base_url}/kpi/new_users/data_series"
        query_params = {
            k: v
            for k, v in [
                ("length", length),
                ("ending_at", ending_at),
                ("app_id", app_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_daily_active_users_series(
        self,
        length: int | None = None,
        ending_at: str | None = None,
        app_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Daily Active Users by Date

        Args:
            length (integer): (Required) Integer Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). Example: '10'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string)
        Date on which the data series should end. Defaults to time of the request. Example: '2018-06-28T23:59:59-5:00'.
            app_id (string): (Optional) String App API identifier retrieved from **Settings > Setup and Testing > API Keys**. If excluded, results for all apps in workspace will be returned. Example: '{{app_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > KPI
        """
        url = f"{self.base_url}/kpi/dau/data_series"
        query_params = {
            k: v
            for k, v in [
                ("length", length),
                ("ending_at", ending_at),
                ("app_id", app_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_kpimau_data_series(
        self,
        length: int | None = None,
        ending_at: str | None = None,
        app_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Monthly Active Users for Last 30 Days

        Args:
            length (integer): (Required) Integer Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). Example: '7'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string) Date on which the data series should end. Defaults to time of the request. Example: '2018-06-28T23:59:59-05:00'.
            app_id (string): (Optional) String App API identifier retrieved from **Settings > Setup and Testing > API Keys**. If excluded, results for all apps in workspace will be returned. Example: '{{app_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > KPI
        """
        url = f"{self.base_url}/kpi/mau/data_series"
        query_params = {
            k: v
            for k, v in [
                ("length", length),
                ("ending_at", ending_at),
                ("app_id", app_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_kpi_uninstalls_data_series(
        self,
        length: int | None = None,
        ending_at: str | None = None,
        app_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Export KPIs for Daily App Uninstalls by Date

        Args:
            length (integer): (Required) Integer Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). Example: '14'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string) Date on which the data series should end. Defaults to time of the request. Example: '2018-06-28T23:59:59-5:00'.
            app_id (string): (Optional) String App API identifier retrieved from **Settings > Setup and Testing > API Keys**. If excluded, results for all apps in workspace will be returned. Example: '{{app_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > KPI
        """
        url = f"{self.base_url}/kpi/uninstalls/data_series"
        query_params = {
            k: v
            for k, v in [
                ("length", length),
                ("ending_at", ending_at),
                ("app_id", app_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_feed_data_series(
        self,
        card_id: str | None = None,
        length: int | None = None,
        unit: str | None = None,
        ending_at: str | None = None,
    ) -> dict[str, Any]:
        """
        Export News Feed Card Analytics

        Args:
            card_id (string): (Required) String See [Card API identifier]( The `card_id` for a given card can be found in the **Settings > Setup and Testing > API Keys** page and on the card details page within your dashboard, or you can use the [News Feed List Endpoint]( Example: '{{card_identifier}}'.
            length (integer): (Required) Integer Max number of units (days or hours) before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). Example: '14'.
            unit (string): (Optional) String Unit of time between data points. Can be `day` or `hour`, defaults to `day`. Example: 'day'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string) Date on which the data series should end. Defaults to time of the request. Example: '2018-06-28T23:59:59-5:00'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > News Feed
        """
        url = f"{self.base_url}/feed/data_series"
        query_params = {
            k: v
            for k, v in [
                ("card_id", card_id),
                ("length", length),
                ("unit", unit),
                ("ending_at", ending_at),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_feed_details(self, card_id: str | None = None) -> dict[str, Any]:
        """
        Export News Feed Cards Details

        Args:
            card_id (string): (Required) String See [Card API identifier]( The `card_id` for a given card can be found in the **Settings > Setup and Testing > API Keys** page and on the card details page within your dashboard, or you can use the [News Feed List Endpoint]( Example: '{{card_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > News Feed
        """
        url = f"{self.base_url}/feed/details"
        query_params = {k: v for k, v in [("card_id", card_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_feed(
        self,
        page: int | None = None,
        include_archived: bool | None = None,
        sort_direction: str | None = None,
    ) -> dict[str, Any]:
        """
        Export News Feed Cards List

        Args:
            page (integer): (Optional) Integer The page of cards to return, defaults to 0 (returns the first set of up to 100). Example: '1'.
            include_archived (boolean): (Optional) Boolean Whether or not to include archived cards, defaults to false. Example: 'True'.
            sort_direction (string): (Optional) String - Sort creation time from newest to oldest: pass in the value `desc`.
        - Sort creation time from oldest to newest: pass in the value `asc`. If `sort_direction` is not included, the default order is oldest to newest. Example: 'desc'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > News Feed
        """
        url = f"{self.base_url}/feed/list"
        query_params = {
            k: v
            for k, v in [
                ("page", page),
                ("include_archived", include_archived),
                ("sort_direction", sort_direction),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_products(self, page: int | None = None) -> dict[str, Any]:
        """
        Export Product IDs

        Args:
            page (integer): (Optional) Integer The page of your product list that you would like to view. Example: '1'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Purchases
        """
        url = f"{self.base_url}/purchases/product_list"
        query_params = {k: v for k, v in [("page", page)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_purchase_quantity_series(
        self,
        ending_at: str | None = None,
        length: int | None = None,
        unit: int | None = None,
        app_id: str | None = None,
        product: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Number of Purchases

        Args:
            ending_at (string): (Optional) Datetime (ISO 8601 string)
        Date on which the data series should end. Defaults to time of the request. Example: '2018-06-28T23:59:59-5:00'.
            length (integer): (Required) Integer
        Maximum number of days before ending_at to include in the returned series. Must be between 1 and 100 (inclusive). Example: '100'.
            unit (integer): (Optional) String
        Unit of time between data points. Can be `day` or `hour`, defaults to `day`. Example: '14'.
            app_id (string): (Optional) String
        App API identifier retrieved from the Settings > Setup and Testing > API Keys to limit analytics to a specific app. Example: '{{app_identifier}}'.
            product (string): (Optional) String
        Name of product to filter response by. If excluded, results for all apps will be returned. Example: 'name'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Purchases
        """
        url = f"{self.base_url}/purchases/quantity_series"
        query_params = {
            k: v
            for k, v in [
                ("ending_at", ending_at),
                ("length", length),
                ("unit", unit),
                ("app_id", app_id),
                ("product", product),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_purchases_revenue_series(
        self,
        ending_at: str | None = None,
        length: int | None = None,
        unit: int | None = None,
        app_id: str | None = None,
        product: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Revenue Data by Time

        Args:
            ending_at (string): (Optional) Datetime (ISO 8601 string)
        Date on which the data series should end. Defaults to time of the request. Example: '2018-06-28T23:59:59-5:00'.
            length (integer): (Required) Integer
        Maximum number of days before ending_at to include in the returned series. Must be between 1 and 100 (inclusive). Example: '100'.
            unit (integer): (Optional) String
        Unit of time between data points. Can be `day` or `hour`, defaults to `day`. Example: '14'.
            app_id (string): (Optional) String
        App API identifier retrieved from the Settings > Setup and Testing > API Keys to limit analytics to a specific app. Example: '{{app_identifier}}'.
            product (string): (Optional) String
        Name of product to filter response by. If excluded, results for all apps will be returned. Example: 'name'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Purchases
        """
        url = f"{self.base_url}/purchases/revenue_series"
        query_params = {
            k: v
            for k, v in [
                ("ending_at", ending_at),
                ("length", length),
                ("unit", unit),
                ("app_id", app_id),
                ("product", product),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_segments(
        self, page: int | None = None, sort_direction: str | None = None
    ) -> dict[str, Any]:
        """
        Export Segment List

        Args:
            page (integer): (Optional) Integer The page of segments to return, defaults to 0 (returns the first set of up to 100). Example: '1'.
            sort_direction (string): (Optional) String - Sort creation time from newest to oldest: pass in the value `desc`.
        - Sort creation time from oldest to newest: pass in the value `asc`. If `sort_direction` is not included, the default order is oldest to newest. Example: 'desc'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Segment
        """
        url = f"{self.base_url}/segments/list"
        query_params = {
            k: v
            for k, v in [("page", page), ("sort_direction", sort_direction)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_segments_data_series(
        self,
        segment_id: str | None = None,
        length: int | None = None,
        ending_at: str | None = None,
    ) -> dict[str, Any]:
        """
        Export Segment Analytics

        Args:
            segment_id (string): (Required) String See [Segment API identifier]( The `segment_id` for a given segment can be found in your **Settings > Setup and Testing > API Keys.** within your Braze account or you can use the [Segment List Endpoint]( Example: '{{segment_identifier}}'.
            length (integer): (Required) Integer Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 (inclusive). Example: '14'.
            ending_at (string): (Optional) Datetime ([ISO 8601]( string) Date on which the data series should end. Defaults to time of the request. Example: '2018-06-27T23:59:59-5:00'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Segment
        """
        url = f"{self.base_url}/segments/data_series"
        query_params = {
            k: v
            for k, v in [
                ("segment_id", segment_id),
                ("length", length),
                ("ending_at", ending_at),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_segment_details(self, segment_id: str | None = None) -> dict[str, Any]:
        """
        Export Segment Details

        Args:
            segment_id (string): (Required) String See [Segment API identifier]( The `segment_id` for a given segment can be found in your **Settings > Setup and Testing > API Keys** within your Braze account or you can use the [Segment List Endpoint]( Example: '{{segment_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Segment
        """
        url = f"{self.base_url}/segments/details"
        query_params = {k: v for k, v in [("segment_id", segment_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_sessions_data_series(
        self,
        length: int | None = None,
        unit: str | None = None,
        ending_at: str | None = None,
        app_id: str | None = None,
        segment_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Export App Sessions by Time

        Args:
            length (integer): (Required) Integer Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 (inclusive). Example: '14'.
            unit (string): (Optional) String Unit of time between data points. Can be `day` or `hour`, defaults to `day`. Example: 'day'.
            ending_at (string): (Optional) Datetime (ISO 8601 string) Date on which the data series should end. Defaults to time of the request. Example: '2018-06-28T23:59:59-5:00'.
            app_id (string): (Optional) String App API identifier retrieved from the **Settings > Setup and Testing > API Keys** to limit analytics to a specific app. Example: '{{app_identifier}}'.
            segment_id (string): (Required) String See [Segment API identifier]( Segment ID indicating the analytics-enabled segment for which sessions should be returned. Example: '{{segment_identifier}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Session Analytics
        """
        url = f"{self.base_url}/sessions/data_series"
        query_params = {
            k: v
            for k, v in [
                ("length", length),
                ("unit", unit),
                ("ending_at", ending_at),
                ("app_id", app_id),
                ("segment_id", segment_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def export_user_ids_by_post(
        self,
        external_ids: list[str] | None = None,
        user_aliases: list[dict[str, Any]] | None = None,
        device_id: str | None = None,
        braze_id: str | None = None,
        email_address: str | None = None,
        phone: str | None = None,
        fields_to_export: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Export User Profile by Identifier

        Args:
            external_ids (array): external_ids Example: ['user_identifier1', 'user_identifier2'].
            user_aliases (array): user_aliases Example: [{'alias_name': 'example_alias', 'alias_label': 'example_label'}].
            device_id (string): device_id Example: '1234567'.
            braze_id (string): braze_id Example: 'braze_identifier'.
            email_address (string): email_address Example: 'example@braze.com'.
            phone (string): phone Example: '+11112223333'.
            fields_to_export (array): fields_to_export Example: ['first_name', 'email', 'purchases'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Users
        """
        request_body_data = None
        request_body_data = {
            "external_ids": external_ids,
            "user_aliases": user_aliases,
            "device_id": device_id,
            "braze_id": braze_id,
            "email_address": email_address,
            "phone": phone,
            "fields_to_export": fields_to_export,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/export/ids"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def export_users_by_segment_post(
        self,
        segment_id: str | None = None,
        callback_endpoint: str | None = None,
        fields_to_export: list[str] | None = None,
        output_format: str | None = None,
    ) -> dict[str, Any]:
        """
        Export User Profile by Segment

        Args:
            segment_id (string): segment_id Example: 'segment_identifier'.
            callback_endpoint (string): callback_endpoint Example: 'example_endpoint'.
            fields_to_export (array): fields_to_export Example: ['first_name', 'email', 'purchases'].
            output_format (string): output_format Example: 'zip'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Users
        """
        request_body_data = None
        request_body_data = {
            "segment_id": segment_id,
            "callback_endpoint": callback_endpoint,
            "fields_to_export": fields_to_export,
            "output_format": output_format,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/export/segment"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def export_global_control_group_users(
        self,
        callback_endpoint: str | None = None,
        fields_to_export: list[str] | None = None,
        output_format: str | None = None,
    ) -> dict[str, Any]:
        """
        Export User Profile by Global Control Group

        Args:
            callback_endpoint (string): callback_endpoint Example: ''.
            fields_to_export (array): fields_to_export Example: ['email', 'braze_id'].
            output_format (string): output_format Example: 'zip'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Export > Users
        """
        request_body_data = None
        request_body_data = {
            "callback_endpoint": callback_endpoint,
            "fields_to_export": fields_to_export,
            "output_format": output_format,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/export/global_control_group"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_live_activity_message(
        self,
        app_id: str | None = None,
        activity_id: str | None = None,
        content_state: dict[str, Any] | None = None,
        end_activity: bool | None = None,
        dismissal_date: str | None = None,
        stale_date: str | None = None,
        notification: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update Live Activity

        Args:
            app_id (string): app_id Example: '{YOUR-APP-API-IDENTIFIER}'.
            activity_id (string): activity_id Example: 'live-activity-1'.
            content_state (object): content_state Example: {'teamOneScore': 2, 'teamTwoScore': 4}.
            end_activity (boolean): end_activity Example: False.
            dismissal_date (string): dismissal_date Example: '2023-02-28T00:00:00+0000'.
            stale_date (string): stale_date Example: '2023-02-27T16:55:49+0000'.
            notification (object): notification Example: {'alert': {'body': "It's halftime! Let's look at the scores", 'title': 'Halftime'}}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Live Activities
        """
        request_body_data = None
        request_body_data = {
            "app_id": app_id,
            "activity_id": activity_id,
            "content_state": content_state,
            "end_activity": end_activity,
            "dismissal_date": dismissal_date,
            "stale_date": stale_date,
            "notification": notification,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/messages/live_activity/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_scheduled_broadcasts(self, end_time: str | None = None) -> dict[str, Any]:
        """
        List Upcoming Scheduled Campaigns and Canvases

        Args:
            end_time (string): (Required) String in [ISO 8601]( format End date of the range to retrieve upcoming scheduled Campaigns and Canvases. This is treated as midnight in UTC time by the API. Example: '2018-09-01T00:00:00-04:00'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        url = f"{self.base_url}/messages/scheduled_broadcasts"
        query_params = {k: v for k, v in [("end_time", end_time)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_scheduled_message(
        self, schedule_id: str | None = None
    ) -> dict[str, Any]:
        """
        Delete Scheduled Messages

        Args:
            schedule_id (string): schedule_id Example: 'schedule_identifier'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "schedule_id": schedule_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/messages/schedule/delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def schedule_delete_canvas_trigger(
        self, canvas_id: str | None = None, schedule_id: str | None = None
    ) -> dict[str, Any]:
        """
        Delete Scheduled API-Triggered Canvases

        Args:
            canvas_id (string): canvas_id Example: 'canvas_identifier'.
            schedule_id (string): schedule_id Example: 'schedule_identifier'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "canvas_id": canvas_id,
            "schedule_id": schedule_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/canvas/trigger/schedule/delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_campaign_schedule(
        self, campaign_id: str | None = None, schedule_id: str | None = None
    ) -> dict[str, Any]:
        """
        Delete Scheduled API Triggered Campaigns

        Args:
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            schedule_id (string): schedule_id Example: 'schedule_identifier'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "campaign_id": campaign_id,
            "schedule_id": schedule_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/campaigns/trigger/schedule/delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_scheduled_message(
        self,
        broadcast: bool | None = None,
        external_user_ids: str | None = None,
        user_aliases: dict[str, Any] | None = None,
        segment_id: str | None = None,
        audience: dict[str, Any] | None = None,
        campaign_id: str | None = None,
        send_id: str | None = None,
        override_messaging_limits: bool | None = None,
        recipient_subscription_state: str | None = None,
        schedule: dict[str, Any] | None = None,
        messages: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create Scheduled Messages

        Args:
            broadcast (boolean): broadcast Example: False.
            external_user_ids (string): external_user_ids Example: 'external_user_identifiers'.
            user_aliases (object): user_aliases Example: {'alias_name': 'example_name', 'alias_label': 'example_label'}.
            segment_id (string): segment_id Example: 'segment_identifiers'.
            audience (object): audience Example: {'AND': [{'custom_attribute': {'custom_attribute_name': 'eye_color', 'comparison': 'equals', 'value': 'blue'}}, {'custom_attribute': {'custom_attribute_name': 'favorite_foods', 'comparison': 'includes_value', 'value': 'pizza'}}, {'OR': [{'custom_attribute': {'custom_attribute_name': 'last_purchase_time', 'comparison': 'less_than_x_days_ago', 'value': 2}}, {'push_subscription_status': {'comparison': 'is', 'value': 'opted_in'}}]}, {'email_subscription_status': {'comparison': 'is_not', 'value': 'subscribed'}}, {'last_used_app': {'comparison': 'after', 'value': '2019-07-22T13:17:55+0000'}}]}.
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            send_id (string): send_id Example: 'send_identifier'.
            override_messaging_limits (boolean): override_messaging_limits Example: False.
            recipient_subscription_state (string): recipient_subscription_state Example: 'subscribed'.
            schedule (object): schedule Example: {'time': '', 'in_local_time': True, 'at_optimal_time': True}.
            messages (object): messages Example: {'apple_push': {}, 'android_push': {}, 'windows_push': {}, 'windows8_push': {}, 'kindle_push': {}, 'web_push': {}, 'email': {}, 'webhook': {}, 'content_card': {}}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "broadcast": broadcast,
            "external_user_ids": external_user_ids,
            "user_aliases": user_aliases,
            "segment_id": segment_id,
            "audience": audience,
            "campaign_id": campaign_id,
            "send_id": send_id,
            "override_messaging_limits": override_messaging_limits,
            "recipient_subscription_state": recipient_subscription_state,
            "schedule": schedule,
            "messages": messages,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/messages/schedule/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_schedule(
        self,
        campaign_id: str | None = None,
        send_id: str | None = None,
        recipients: list[dict[str, Any]] | None = None,
        audience: dict[str, Any] | None = None,
        broadcast: bool | None = None,
        trigger_properties: dict[str, Any] | None = None,
        schedule: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Schedule API Triggered Campaigns

        Args:
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            send_id (string): send_id Example: 'send_identifier'.
            recipients (array): recipients Example: [{'user_alias': 'example_alias', 'external_user_id': 'external_user_identifier', 'trigger_properties': {}}].
            audience (object): audience Example: {'AND': [{'custom_attribute': {'custom_attribute_name': 'eye_color', 'comparison': 'equals', 'value': 'blue'}}, {'custom_attribute': {'custom_attribute_name': 'favorite_foods', 'comparison': 'includes_value', 'value': 'pizza'}}, {'OR': [{'custom_attribute': {'custom_attribute_name': 'last_purchase_time', 'comparison': 'less_than_x_days_ago', 'value': 2}}, {'push_subscription_status': {'comparison': 'is', 'value': 'opted_in'}}]}, {'email_subscription_status': {'comparison': 'is_not', 'value': 'subscribed'}}, {'last_used_app': {'comparison': 'after', 'value': '2019-07-22T13:17:55+0000'}}]}.
            broadcast (boolean): broadcast Example: False.
            trigger_properties (object): trigger_properties Example: {}.
            schedule (object): schedule Example: {'time': '', 'in_local_time': False, 'at_optimal_time': False}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "campaign_id": campaign_id,
            "send_id": send_id,
            "recipients": recipients,
            "audience": audience,
            "broadcast": broadcast,
            "trigger_properties": trigger_properties,
            "schedule": schedule,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/campaigns/trigger/schedule/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_schedule_trigger(
        self,
        canvas_id: str | None = None,
        recipients: list[dict[str, Any]] | None = None,
        audience: dict[str, Any] | None = None,
        broadcast: bool | None = None,
        canvas_entry_properties: dict[str, Any] | None = None,
        schedule: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Schedule API Triggered Canvases

        Args:
            canvas_id (string): canvas_id Example: 'canvas_identifier'.
            recipients (array): recipients Example: [{'user_alias': 'example_alias', 'external_user_id': 'external_user_identifier', 'trigger_properties': {}, 'canvas_entry_properties': {}}].
            audience (object): audience Example: {'AND': [{'custom_attribute': {'custom_attribute_name': 'eye_color', 'comparison': 'equals', 'value': 'blue'}}, {'custom_attribute': {'custom_attribute_name': 'favorite_foods', 'comparison': 'includes_value', 'value': 'pizza'}}, {'OR': [{'custom_attribute': {'custom_attribute_name': 'last_purchase_time', 'comparison': 'less_than_x_days_ago', 'value': 2}}, {'push_subscription_status': {'comparison': 'is', 'value': 'opted_in'}}]}, {'email_subscription_status': {'comparison': 'is_not', 'value': 'subscribed'}}, {'last_used_app': {'comparison': 'after', 'value': '2019-07-22T13:17:55+0000'}}]}.
            broadcast (boolean): broadcast Example: False.
            canvas_entry_properties (object): canvas_entry_properties Example: {}.
            schedule (object): schedule Example: {'time': '', 'in_local_time': False, 'at_optimal_time': False}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "canvas_id": canvas_id,
            "recipients": recipients,
            "audience": audience,
            "broadcast": broadcast,
            "canvas_entry_properties": canvas_entry_properties,
            "schedule": schedule,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/canvas/trigger/schedule/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def schedule_message_update(
        self,
        schedule_id: str | None = None,
        schedule: dict[str, Any] | None = None,
        messages: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update Scheduled Messages

        Args:
            schedule_id (string): schedule_id Example: 'schedule_identifier'.
            schedule (object): schedule Example: {'time': '2017-05-24T20:30:36Z'}.
            messages (object): messages Example: {'apple_push': {'alert': 'Updated Message!', 'badge': 1}, 'android_push': {'title': 'Updated title!', 'alert': 'Updated message!'}, 'sms': {'subscription_group_id': 'subscription_group_identifier', 'message_variation_id': 'message_variation_identifier', 'body': 'This is my SMS body.', 'app_id': 'app_identifier'}}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "schedule_id": schedule_id,
            "schedule": schedule,
            "messages": messages,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/messages/schedule/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_campaign_trigger_schedule(
        self,
        campaign_id: str | None = None,
        schedule_id: str | None = None,
        schedule: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update Scheduled API Triggered Campaigns

        Args:
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            schedule_id (string): schedule_id Example: 'schedule_identifier'.
            schedule (object): schedule Example: {'time': '2017-05-24T21:30:00Z', 'in_local_time': True}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "campaign_id": campaign_id,
            "schedule_id": schedule_id,
            "schedule": schedule,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/campaigns/trigger/schedule/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_canvas_trigger_schedule(
        self,
        canvas_id: str | None = None,
        schedule_id: str | None = None,
        schedule: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update Scheduled API Triggered Canvases

        Args:
            canvas_id (string): canvas_id Example: 'canvas_identifier'.
            schedule_id (string): schedule_id Example: 'schedule_identifier'.
            schedule (object): schedule Example: {'time': '2017-05-24T21:30:00Z', 'in_local_time': True}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Schedule Mesages
        """
        request_body_data = None
        request_body_data = {
            "canvas_id": canvas_id,
            "schedule_id": schedule_id,
            "schedule": schedule,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/canvas/trigger/schedule/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_send_by_id(
        self, campaign_id: str | None = None, send_id: str | None = None
    ) -> dict[str, Any]:
        """
        Create Send IDs For Message Send Tracking

        Args:
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            send_id (string): send_id Example: 'send_identifier'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Send Messages
        """
        request_body_data = None
        request_body_data = {
            "campaign_id": campaign_id,
            "send_id": send_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/sends/id/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def send_message(
        self,
        broadcast: str | None = None,
        external_user_ids: str | None = None,
        user_aliases: dict[str, Any] | None = None,
        segment_id: str | None = None,
        audience: dict[str, Any] | None = None,
        campaign_id: str | None = None,
        send_id: str | None = None,
        override_frequency_capping: str | None = None,
        recipient_subscription_state: str | None = None,
        messages: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Send Messages Immediately via API Only

        Args:
            broadcast (string): broadcast Example: 'false'.
            external_user_ids (string): external_user_ids Example: 'external_user_identifiers'.
            user_aliases (object): user_aliases Example: {'alias_name': 'example_name', 'alias_label': 'example_label'}.
            segment_id (string): segment_id Example: 'segment_identifier'.
            audience (object): audience Example: {'AND': [{'custom_attribute': {'custom_attribute_name': 'eye_color', 'comparison': 'equals', 'value': 'blue'}}, {'custom_attribute': {'custom_attribute_name': 'favorite_foods', 'comparison': 'includes_value', 'value': 'pizza'}}, {'OR': [{'custom_attribute': {'custom_attribute_name': 'last_purchase_time', 'comparison': 'less_than_x_days_ago', 'value': 2}}, {'push_subscription_status': {'comparison': 'is', 'value': 'opted_in'}}]}, {'email_subscription_status': {'comparison': 'is_not', 'value': 'subscribed'}}, {'last_used_app': {'comparison': 'after', 'value': '2019-07-22T13:17:55+0000'}}]}.
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            send_id (string): send_id Example: 'send_identifier'.
            override_frequency_capping (string): override_frequency_capping Example: 'false'.
            recipient_subscription_state (string): recipient_subscription_state Example: 'all'.
            messages (object): messages Example: {'android_push': '(optional, Android Push Object)', 'apple_push': '(optional, Apple Push Object)', 'content_card': '(optional, Content Card Object)', 'email': '(optional, Email Object)', 'kindle_push': '(optional, Kindle/FireOS Push Object)', 'web_push': '(optional, Web Push Object)', 'windows_phone8_push': '(optional, Windows Phone 8 Push Object)', 'windows_universal_push': '(optional, Windows Universal Push Object)'}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Send Messages
        """
        request_body_data = None
        request_body_data = {
            "broadcast": broadcast,
            "external_user_ids": external_user_ids,
            "user_aliases": user_aliases,
            "segment_id": segment_id,
            "audience": audience,
            "campaign_id": campaign_id,
            "send_id": send_id,
            "override_frequency_capping": override_frequency_capping,
            "recipient_subscription_state": recipient_subscription_state,
            "messages": messages,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/messages/send"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def send_campaign_transactional(
        self,
        campaign_id: str,
        external_send_id: str | None = None,
        trigger_properties: dict[str, Any] | None = None,
        recipient: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Send Transactional Email via API Triggered Delivery

        Args:
            campaign_id (string): campaign_id
            external_send_id (string): external_send_id Example: 'YOUR_BASE64_COMPATIBLE_ID'.
            trigger_properties (object): trigger_properties Example: {'example_string_property': 'YOUR_EXAMPLE_STRING', 'example_integer_property': 'YOUR_EXAMPLE_INTEGER'}.
            recipient (array): recipient Example: [{'external_user_id': 'TARGETED_USER_ID_STRING'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Send Messages
        """
        if campaign_id is None:
            raise ValueError("Missing required parameter 'campaign_id'.")
        request_body_data = None
        request_body_data = {
            "external_send_id": external_send_id,
            "trigger_properties": trigger_properties,
            "recipient": recipient,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/transactional/v1/campaigns/{campaign_id}/send"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def send_campaign_trigger(
        self,
        campaign_id: str | None = None,
        send_id: str | None = None,
        trigger_properties: dict[str, Any] | None = None,
        broadcast: bool | None = None,
        audience: dict[str, Any] | None = None,
        recipients: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Send Campaign Messages via API Triggered Delivery

        Args:
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            send_id (string): send_id Example: 'send_identifier'.
            trigger_properties (object): trigger_properties Example: {}.
            broadcast (boolean): broadcast Example: False.
            audience (object): audience Example: {'AND': [{'custom_attribute': {'custom_attribute_name': 'eye_color', 'comparison': 'equals', 'value': 'blue'}}, {'custom_attribute': {'custom_attribute_name': 'favorite_foods', 'comparison': 'includes_value', 'value': 'pizza'}}, {'OR': [{'custom_attribute': {'custom_attribute_name': 'last_purchase_time', 'comparison': 'less_than_x_days_ago', 'value': 2}}, {'push_subscription_status': {'comparison': 'is', 'value': 'opted_in'}}]}, {'email_subscription_status': {'comparison': 'is_not', 'value': 'subscribed'}}, {'last_used_app': {'comparison': 'after', 'value': '2019-07-22T13:17:55+0000'}}]}.
            recipients (array): recipients Example: [{'user_alias': {'alias_name': 'example_name', 'alias_label': 'example_label'}, 'external_user_id': 'external_user_identifier', 'trigger_properties': {}, 'send_to_existing_only': True, 'attributes': {'first_name': 'Alex'}}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Send Messages
        """
        request_body_data = None
        request_body_data = {
            "campaign_id": campaign_id,
            "send_id": send_id,
            "trigger_properties": trigger_properties,
            "broadcast": broadcast,
            "audience": audience,
            "recipients": recipients,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/campaigns/trigger/send"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def send_canvas_trigger_post(
        self,
        canvas_id: str | None = None,
        canvas_entry_properties: dict[str, Any] | None = None,
        broadcast: bool | None = None,
        audience: dict[str, Any] | None = None,
        recipients: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Send Canvas Messages via API Triggered Delivery

        Args:
            canvas_id (string): canvas_id Example: 'canvas_identifier'.
            canvas_entry_properties (object): canvas_entry_properties Example: {'product_name': 'shoes', 'product_price': 79.99}.
            broadcast (boolean): broadcast Example: False.
            audience (object): audience Example: {'AND': [{'custom_attribute': {'custom_attribute_name': 'eye_color', 'comparison': 'equals', 'value': 'blue'}}, {'custom_attribute': {'custom_attribute_name': 'favorite_foods', 'comparison': 'includes_value', 'value': 'pizza'}}, {'OR': [{'custom_attribute': {'custom_attribute_name': 'last_purchase_time', 'comparison': 'less_than_x_days_ago', 'value': 2}}, {'push_subscription_status': {'comparison': 'is', 'value': 'opted_in'}}]}, {'email_subscription_status': {'comparison': 'is_not', 'value': 'subscribed'}}, {'last_used_app': {'comparison': 'after', 'value': '2019-07-22T13:17:55+0000'}}]}.
            recipients (array): recipients Example: [{'user_alias': {'alias_name': 'example_name', 'alias_label': 'example_label'}, 'external_user_id': 'user_identifier', 'trigger_properties': {}, 'canvas_entry_properties': '', 'send_to_existing_only': True, 'attributes': {'first_name': 'Alex'}}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Messaging > Send Messages
        """
        request_body_data = None
        request_body_data = {
            "canvas_id": canvas_id,
            "canvas_entry_properties": canvas_entry_properties,
            "broadcast": broadcast,
            "audience": audience,
            "recipients": recipients,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/canvas/trigger/send"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_preference_center_url_by_user_id(
        self,
        PreferenceCenterExternalID: str,
        UserID: str,
        preference_center_api_id: str | None = None,
        external_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Generate Preference Center URL

        Args:
            PreferenceCenterExternalID (string): PreferenceCenterExternalID
            UserID (string): UserID
            preference_center_api_id (string): Identifies the unique API ID for the preference center resource, used to specify which preference center instance to query. Example: '{{preference_center_api_id}}'.
            external_id (string): (Required) String Example: '{{external_id}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Preference Center
        """
        if PreferenceCenterExternalID is None:
            raise ValueError("Missing required parameter 'PreferenceCenterExternalID'.")
        if UserID is None:
            raise ValueError("Missing required parameter 'UserID'.")
        url = f"{self.base_url}/preference_center_v1/{PreferenceCenterExternalID}/url/{UserID}"
        query_params = {
            k: v
            for k, v in [
                ("preference_center_api_id", preference_center_api_id),
                ("external_id", external_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_preferences(self) -> dict[str, Any]:
        """
        List Preference Centers

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Preference Center
        """
        url = f"{self.base_url}/preference_center/v1/list"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_preference_center_by_id(
        self, PreferenceCenterExternalID: str
    ) -> dict[str, Any]:
        """
        View Details for Preference Center

        Args:
            PreferenceCenterExternalID (string): PreferenceCenterExternalID

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Preference Center
        """
        if PreferenceCenterExternalID is None:
            raise ValueError("Missing required parameter 'PreferenceCenterExternalID'.")
        url = f"{self.base_url}/preference_center/v1/{PreferenceCenterExternalID}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_preference_center_by_id(
        self,
        PreferenceCenterExternalID: str,
        external_send_id: str | None = None,
        trigger_properties: dict[str, Any] | None = None,
        recipient: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Update Preference Center

        Args:
            PreferenceCenterExternalID (string): PreferenceCenterExternalID
            external_send_id (string): external_send_id Example: 'YOUR_BASE64_COMPATIBLE_ID'.
            trigger_properties (object): trigger_properties Example: {'example_string_property': 'YOUR_EXAMPLE_STRING', 'example_integer_property': 'YOUR_EXAMPLE_INTEGER'}.
            recipient (array): recipient Example: [{'external_user_id': 'TARGETED_USER_ID_STRING'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Preference Center
        """
        if PreferenceCenterExternalID is None:
            raise ValueError("Missing required parameter 'PreferenceCenterExternalID'.")
        request_body_data = None
        request_body_data = {
            "external_send_id": external_send_id,
            "trigger_properties": trigger_properties,
            "recipient": recipient,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/preference_center/v1/{PreferenceCenterExternalID}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_preference_center_entry(
        self,
        name: str | None = None,
        preference_center_title: str | None = None,
        preference_center_page_html: str | None = None,
        confirmation_page_html: str | None = None,
        state: str | None = None,
        options: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create Preference Center

        Args:
            name (string): name Example: 'string'.
            preference_center_title (string): preference_center_title Example: 'string'.
            preference_center_page_html (string): preference_center_page_html Example: 'string'.
            confirmation_page_html (string): confirmation_page_html Example: 'string'.
            state (string): state Example: 'active'.
            options (object): options Example: {'meta-viewport-content': 'string'}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Preference Center
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "preference_center_title": preference_center_title,
            "preference_center_page_html": preference_center_page_html,
            "confirmation_page_html": confirmation_page_html,
            "state": state,
            "options": options,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/preference_center/v1"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_user_by_id(self, id: str) -> dict[str, Any]:
        """
        Remove Dashboard User Account

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SCIM
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/scim/v2/Users/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_user_by_id(self, id: str) -> dict[str, Any]:
        """
        Look Up an Existing Dashboard User Account

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SCIM
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/scim/v2/Users/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_user_by_id(
        self,
        id: str,
        schemas: list[str] | None = None,
        name: dict[str, Any] | None = None,
        department: str | None = None,
        permissions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update Dashboard User Account

        Args:
            id (string): id
            schemas (array): schemas Example: ['urn:ietf:params:scim:schemas:core:2.0:User'].
            name (object): name Example: {'givenName': 'Test', 'familyName': 'User'}.
            department (string): department Example: 'finance'.
            permissions (object): permissions Example: {'companyPermissions': ['manage_company_settings'], 'appGroup': [{'appGroupName': 'Test App Group', 'appGroupPermissions': ['basic_access', 'send_campaigns_canvases'], 'team': [{'teamName': 'Test Team', 'teamPermissions': ['admin']}]}]}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SCIM
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "schemas": schemas,
            "name": name,
            "department": department,
            "permissions": permissions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/scim/v2/Users/{id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_users(self, filter: str | None = None) -> dict[str, Any]:
        """
        Search Existing Dashboard User by Email

        Args:
            filter (string): A string parameter used to filter the results of the GET operation by specifying conditions for user attributes, such as `userName`, `externalId`, or name fields. Example: '{userName@example.com}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SCIM, important
        """
        url = f"{self.base_url}/scim/v2/Users"
        query_params = {k: v for k, v in [("filter", filter)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_user(
        self,
        schemas: list[str] | None = None,
        userName: str | None = None,
        name: dict[str, Any] | None = None,
        department: str | None = None,
        permissions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create New Dashboard User Account

        Args:
            schemas (array): schemas Example: ['urn:ietf:params:scim:schemas:core:2.0:User'].
            userName (string): userName Example: 'user@test.com'.
            name (object): name Example: {'givenName': 'Test', 'familyName': 'User'}.
            department (string): department Example: 'finance'.
            permissions (object): permissions Example: {'companyPermissions': ['manage_company_settings'], 'appGroup': [{'appGroupName': 'Test App Group', 'appGroupPermissions': ['basic_access', 'send_campaigns_canvases'], 'team': [{'teamName': 'Test Team', 'teamPermissions': ['basic_access', 'export_user_data']}]}]}.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SCIM, important
        """
        request_body_data = None
        request_body_data = {
            "schemas": schemas,
            "userName": userName,
            "name": name,
            "department": department,
            "permissions": permissions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/scim/v2/Users"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_invalid_phone_numbers(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        phone_numbers: int | None = None,
    ) -> dict[str, Any]:
        """
        Query Invalid Phone Numbers

        Args:
            start_date (string): (Optional*) String in YYYY-MM-DD format Start date of the range to retrieve invalid phone numbers, must be earlier than `end_date`. This is treated as midnight in UTC time by the API. Example: '2018-09-01'.
            end_date (string): (Optional*) String in YYYY-MM-DD format End date of the range to retrieve invalid phone numbers. This is treated as midnight in UTC time by the API. Example: '2018-09-01'.
            limit (integer): (Optional) Integer
        Optional field to limit the number of results returned. Defaults to 100, maximum is 500. Example: '100'.
            offset (integer): (Optional) Integer
        Optional beginning point in the list to retrieve from. Example: '1'.
            phone_numbers (integer): (Optional*) Array of Strings in e.164 format
        If provided, we will return the phone number if it has been found to be invalid. Example: '12345678901'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SMS
        """
        url = f"{self.base_url}/sms/invalid_phone_numbers"
        query_params = {
            k: v
            for k, v in [
                ("start_date", start_date),
                ("end_date", end_date),
                ("limit", limit),
                ("offset", offset),
                ("phone_numbers", phone_numbers),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def remove_invalid_phone_numbers(
        self, phone_numbers: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Remove Invalid Phone Numbers

        Args:
            phone_numbers (array): phone_numbers Example: ['12183095514', '14255551212'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SMS
        """
        request_body_data = None
        request_body_data = {
            "phone_numbers": phone_numbers,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/sms/invalid_phone_numbers/remove"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_subscription_status(
        self,
        subscription_group_id: str | None = None,
        external_id: str | None = None,
        phone: str | None = None,
    ) -> dict[str, Any]:
        """
        List User's  Subscription Group Status - SMS

        Args:
            subscription_group_id (string): (Required) String The `id` of your subscription group. Example: '{{subscription_group_id}}'.
            external_id (string): (Required*) String The `external_id` of the user (must include at least one and at most 50 `external_ids`). When both an `external_id` and `phone` are submitted, only the external_id(s) provided will be applied to the result query. Example: '{{external_identifier}}'.
            phone (string): (Required*) String in [E.164]( format The phone number of the user (must include at least one phone number and at most 50 phone numbers). Example: '+11112223333'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Subscription Groups > SMS and WhatsApp
        """
        url = f"{self.base_url}/subscription/status/get"
        query_params = {
            k: v
            for k, v in [
                ("subscription_group_id", subscription_group_id),
                ("external_id", external_id),
                ("phone", phone),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_subscription_user_status(
        self,
        external_id: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        phone: str | None = None,
    ) -> dict[str, Any]:
        """
        List User's Subscription Group - SMS

        Args:
            external_id (string): (Required*) String The `external_id` of the user (must include at least one and at most 50 `external_ids`). Example: '{{external_id}}'.
            limit (integer): (Optional) Integer The limit on the maximum number of results returned. Default (and max) limit is 100. Example: '100'.
            offset (integer): (Optional) Integer Number of templates to skip before returning the rest of the templates that fit the search criteria. Example: '1'.
            phone (string): (Required*) String in [E.164]( format The phone number of the user. Must include at least one phone number (with a max of 50). Example: '+11112223333'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Subscription Groups > SMS and WhatsApp
        """
        url = f"{self.base_url}/subscription/user/status"
        query_params = {
            k: v
            for k, v in [
                ("external_id", external_id),
                ("limit", limit),
                ("offset", offset),
                ("phone", phone),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def set_subscription_status(
        self,
        subscription_group_id: str | None = None,
        subscription_state: str | None = None,
        external_id: str | None = None,
        phone: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Update User's Subscription Group Status - SMS

        Args:
            subscription_group_id (string): subscription_group_id Example: 'subscription_group_identifier'.
            subscription_state (string): subscription_state Example: 'unsubscribed'.
            external_id (string): external_id Example: 'external_identifier'.
            phone (array): phone Example: ['+12223334444', '+11112223333'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Subscription Groups > SMS and WhatsApp
        """
        request_body_data = None
        request_body_data = {
            "subscription_group_id": subscription_group_id,
            "subscription_state": subscription_state,
            "external_id": external_id,
            "phone": phone,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/subscription/status/set"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def set_subscription_status_post(
        self, subscription_groups: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Update User's Subscription Group Status V2

        Args:
            subscription_groups (array): subscription_groups Example: [{'subscription_group_id': 'subscription_group_identifier', 'subscription_state': 'subscribed', 'emails': ['example1@email.com', 'example2@email.com']}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Subscription Groups > SMS and WhatsApp
        """
        request_body_data = None
        request_body_data = {
            "subscription_groups": subscription_groups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/subscription/status/set"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_content_blocks(
        self,
        modified_after: str | None = None,
        modified_before: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """
        List Available Content Blocks

        Args:
            modified_after (string): (Optional) String in [ISO 8601]( Retrieve only content blocks updated at or after the given time. Example: '2020-01-01T01:01:01.000000'.
            modified_before (string): (Optional) String in [ISO 8601]( Retrieve only content blocks updated at or before the given time. Example: '2020-02-01T01:01:01.000000'.
            limit (integer): (Optional) Positive Number Maximum number of content blocks to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000. Example: '100'.
            offset (integer): (Optional) Positive Number Number of content blocks to skip before returning rest of the templates that fit the search criteria. Example: '1'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates > Content Blocks
        """
        url = f"{self.base_url}/content_blocks/list"
        query_params = {
            k: v
            for k, v in [
                ("modified_after", modified_after),
                ("modified_before", modified_before),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_info_content_block(
        self,
        content_block_id: str | None = None,
        include_inclusion_data: bool | None = None,
    ) -> dict[str, Any]:
        """
        See Content Block Information

        Args:
            content_block_id (string): (Required) String The content block identifier. You can find this by either listing content block information through an API call or going to **Settings > Setup and Testing > API Keys**, then scrolling to the bottom and searching for your content block API identifier. Example: '{{content_block_id}}'.
            include_inclusion_data (boolean): (Optional) Boolean When set to `true`, the API returns back the Message Variation API identifier of campaigns and Canvases where this content block is included, to be used in subsequent calls. The results exclude archived or deleted Campaigns or Canvases.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates > Content Blocks
        """
        url = f"{self.base_url}/content_blocks/info"
        query_params = {
            k: v
            for k, v in [
                ("content_block_id", content_block_id),
                ("include_inclusion_data", include_inclusion_data),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_content_block(
        self,
        name: str | None = None,
        description: str | None = None,
        content: str | None = None,
        state: str | None = None,
        tags: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Create Content Block

        Args:
            name (string): name Example: 'content_block'.
            description (string): description Example: 'This is my content block'.
            content (string): content Example: 'HTML content within block'.
            state (string): state Example: 'draft'.
            tags (array): tags Example: ['marketing'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates > Content Blocks, important
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "content": content,
            "state": state,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/content_blocks/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_content_block(
        self,
        content_block_id: str | None = None,
        name: str | None = None,
        description: str | None = None,
        content: str | None = None,
        state: str | None = None,
        tags: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Update Content Block

        Args:
            content_block_id (string): content_block_id Example: 'content_block_id'.
            name (string): name Example: 'content_block'.
            description (string): description Example: 'This is my content block'.
            content (string): content Example: 'HTML or text content within block'.
            state (string): state Example: 'draft'.
            tags (array): tags Example: ['marketing'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates > Content Blocks
        """
        request_body_data = None
        request_body_data = {
            "content_block_id": content_block_id,
            "name": name,
            "description": description,
            "content": content,
            "state": state,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/content_blocks/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_email_templates(
        self,
        modified_after: str | None = None,
        modified_before: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """
        List Available Email Templates

        Args:
            modified_after (string): (Optional) String in [ISO 8601]( Retrieve only templates updated at or after the given time. Example: '2020-01-01T01:01:01.000000'.
            modified_before (string): (Optional) String in [ISO 8601]( Retrieve only templates updated at or before the given time. Example: '2020-02-01T01:01:01.000000'.
            limit (integer): (Optional) Positive Number Maximum number of templates to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000. Example: '1'.
            offset (integer): (Optional) Positive Number Number of templates to skip before returning rest of the templates that fit the search criteria.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates > Email Templates
        """
        url = f"{self.base_url}/templates/email/list"
        query_params = {
            k: v
            for k, v in [
                ("modified_after", modified_after),
                ("modified_before", modified_before),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_email_template_info(
        self, email_template_id: str | None = None
    ) -> dict[str, Any]:
        """
        See Email Template Information

        Args:
            email_template_id (string): (Required) String See [email template's API identifier]( Example: '{{email_template_id}}'.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates > Email Templates
        """
        url = f"{self.base_url}/templates/email/info"
        query_params = {
            k: v for k, v in [("email_template_id", email_template_id)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_email_template(
        self,
        template_name: str | None = None,
        subject: str | None = None,
        body: str | None = None,
        plaintext_body: str | None = None,
        preheader: str | None = None,
        tags: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Create Email Template

        Args:
            template_name (string): template_name Example: 'email_template_name'.
            subject (string): subject Example: 'Welcome to my email template!'.
            body (string): body Example: 'This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.'.
            plaintext_body (string): plaintext_body Example: 'This is the text within my email body and here is a link to https://www.braze.com/.'.
            preheader (string): preheader Example: 'My preheader is pretty cool.'.
            tags (array): tags Example: ['Tag1', 'Tag2'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates > Email Templates
        """
        request_body_data = None
        request_body_data = {
            "template_name": template_name,
            "subject": subject,
            "body": body,
            "plaintext_body": plaintext_body,
            "preheader": preheader,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/templates/email/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def rename_external_id(
        self, external_id_renames: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Rename External ID

        Args:
            external_id_renames (array): external_id_renames Example: [{'current_external_id': 'existing_external_id', 'new_external_id': 'new_external_id'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User Data > External ID Migration
        """
        request_body_data = None
        request_body_data = {
            "external_id_renames": external_id_renames,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/external_ids/rename"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def remove_external_id(
        self, external_ids: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Remove External ID

        Args:
            external_ids (array): external_ids Example: ['existing_deprecated_external_id_string'].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User Data > External ID Migration
        """
        request_body_data = None
        request_body_data = {
            "external_ids": external_ids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/external_ids/remove"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_user_alias(
        self, alias_updates: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Update User Alias

        Args:
            alias_updates (array): alias_updates Example: [{'alias_label': 'example_alias_label', 'old_alias_name': 'example_old_alias_name', 'new_alias_name': 'example_new_alias_name'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User Data
        """
        request_body_data = None
        request_body_data = {
            "alias_updates": alias_updates,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/alias/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_user_alias_new(
        self, user_aliases: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Create New User Aliases

        Args:
            user_aliases (array): user_aliases Example: [{'external_id': 'external_identifier', 'alias_name': 'example_name', 'alias_label': 'example_label'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User Data
        """
        request_body_data = None
        request_body_data = {
            "user_aliases": user_aliases,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/alias/new"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_user(
        self,
        external_ids: list[str] | None = None,
        braze_ids: list[str] | None = None,
        user_aliases: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Delete Users

        Args:
            external_ids (array): external_ids Example: ['external_identifier1', 'external_identifier2'].
            braze_ids (array): braze_ids Example: ['braze_identifier1', 'braze_identifier2'].
            user_aliases (array): user_aliases Example: [{'alias_name': 'user_alias1', 'alias_label': 'alias_label1'}, {'alias_name': 'user_alias2', 'alias_label': 'alias_label2'}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User Data
        """
        request_body_data = None
        request_body_data = {
            "external_ids": external_ids,
            "braze_ids": braze_ids,
            "user_aliases": user_aliases,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def identify_user(
        self, aliases_to_identify: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Identify Users

        Args:
            aliases_to_identify (array): aliases_to_identify Example: [{'external_id': 'external_identifier', 'user_alias': {'alias_name': 'example_alias', 'alias_label': 'example_label'}}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User Data
        """
        request_body_data = None
        request_body_data = {
            "aliases_to_identify": aliases_to_identify,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/identify"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def merge_users_post(
        self, merge_updates: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Merge Users

        Args:
            merge_updates (array): merge_updates Example: [{'identifier_to_merge': {'external_id': 'old-user1'}, 'identifier_to_keep': {'external_id': 'current-user1'}}, {'identifier_to_merge': {'user_alias': {'alias_name': 'old-user2@example.com', 'alias_label': 'email'}}, 'identifier_to_keep': {'user_alias': {'alias_name': 'current-user2@example.com', 'alias_label': 'email'}}}].

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            User Data
        """
        request_body_data = None
        request_body_data = {
            "merge_updates": merge_updates,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/users/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_tools(self):
        return [
            self.update_email_template,
            self.track_user_activity,
            self.delete_catalog_by_name,
            self.list_catalogs,
            self.create_catalog,
            self.delete_catalog_item,
            self.edit_catalog_item,
            self.create_catalog_item,
            self.update_catalog_items,
            self.list_catalog_items,
            self.delete_catalog_item_by_id,
            self.get_item_detail,
            self.update_catalog_item_by_id,
            self.add_catalog_item_by_id,
            self.update_catalog_item,
            self.list_hard_bounces,
            self.list_unsubscribes,
            self.post_email_status,
            self.remove_bounced_email,
            self.remove_email_spam,
            self.add_email_to_blocklist,
            self.add_to_blacklist,
            self.get_campaign_data_series,
            self.get_campaign_details,
            self.list_campaigns,
            self.get_send_data_series,
            self.get_canvas_data_series,
            self.fetch_canvas_data_summary,
            self.get_canvas_details,
            self.list_canvas,
            self.list_events,
            self.fetch_event_series_data,
            self.list_new_user_kpi_series,
            self.get_daily_active_users_series,
            self.get_kpimau_data_series,
            self.get_kpi_uninstalls_data_series,
            self.get_feed_data_series,
            self.get_feed_details,
            self.list_feed,
            self.list_products,
            self.get_purchase_quantity_series,
            self.get_purchases_revenue_series,
            self.list_segments,
            self.get_segments_data_series,
            self.get_segment_details,
            self.get_sessions_data_series,
            self.export_user_ids_by_post,
            self.export_users_by_segment_post,
            self.export_global_control_group_users,
            self.update_live_activity_message,
            self.list_scheduled_broadcasts,
            self.delete_scheduled_message,
            self.schedule_delete_canvas_trigger,
            self.delete_campaign_schedule,
            self.create_scheduled_message,
            self.create_schedule,
            self.create_schedule_trigger,
            self.schedule_message_update,
            self.update_campaign_trigger_schedule,
            self.update_canvas_trigger_schedule,
            self.create_send_by_id,
            self.send_message,
            self.send_campaign_transactional,
            self.send_campaign_trigger,
            self.send_canvas_trigger_post,
            self.get_preference_center_url_by_user_id,
            self.list_preferences,
            self.get_preference_center_by_id,
            self.update_preference_center_by_id,
            self.create_preference_center_entry,
            self.delete_user_by_id,
            self.get_user_by_id,
            self.update_user_by_id,
            self.list_users,
            self.create_user,
            self.list_invalid_phone_numbers,
            self.remove_invalid_phone_numbers,
            self.get_subscription_status,
            self.get_subscription_user_status,
            self.set_subscription_status,
            self.set_subscription_status_post,
            self.list_content_blocks,
            self.get_info_content_block,
            self.create_content_block,
            self.update_content_block,
            self.list_email_templates,
            self.get_email_template_info,
            self.create_email_template,
            self.rename_external_id,
            self.remove_external_id,
            self.update_user_alias,
            self.create_user_alias_new,
            self.delete_user,
            self.identify_user,
            self.merge_users_post,
        ]
