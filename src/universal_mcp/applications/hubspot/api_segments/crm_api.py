from typing import Any

from .api_segment_base import APISegmentBase


class CrmApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def batch_read_emails(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a batch of emails from a CRM system using the "POST" method allowing optional filtering by archived status, and returns the results in a multipart response.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Optional boolean query parameter to filter emails based on whether they are archived, defaulting to false if not specified.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_email_by_id(
        self,
        emailId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific email object in a CRM system, allowing optional filtering by properties, associations, and archival status.

        Args:
            emailId (string): emailId
            properties (array): Optional array parameter to specify the properties of the email object to retrieve; allows customization of the response to include only the required properties.
            propertiesWithHistory (array): A comma-separated list of properties for which to include both current values and their historical changes in the response.
            associations (array): An optional array parameter specifying the associations to be included in the response for the email object, allowing for the retrieval of related records.
            archived (boolean): Whether to include archived emails in the response; defaults to false.
            idProperty (string): Optional string parameter that specifies the ID property to be used for filtering or identification purposes in the context of the GET operation for retrieving email objects.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/{emailId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_email_by_id(self, emailId: str) -> Any:
        """

        Deletes an email object identified by the specified emailId from a CRM system.

        Args:
            emailId (string): emailId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/{emailId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_email_by_id(
        self, emailId: str, properties: dict[str, str], idProperty: str | None = None
    ) -> dict[str, Any]:
        """

        Updates specific properties of an existing email record in the CRM by its emailId using a PATCH request with JSON data.

        Args:
            emailId (string): emailId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Optional string parameter to specify the ID property for the email object, used in the PATCH operation to update specific email details.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/{emailId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_emails_post(
        self, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges email records using the provided JSON payload, utilizing OAuth2 or private app authentication to manage contact data in the CRM system.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_emails_batch(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of emails by sending a POST request to the "/crm/v3/objects/emails/batch/archive" endpoint with a JSON payload containing the email IDs to be archived.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_emails_batch_post(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates a batch of email objects in the CRM using the POST method, requiring JSON content and authorization through OAuth2 or private apps.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_emails_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates multiple email objects in a CRM system using a batch operation via the POST method, returning status messages for each update.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_email_gdpr_data(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Deletes a contact and associated data from the CRM in compliance with GDPR guidelines using the provided JSON payload, requiring the "crm.objects.contacts.write" permission.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_emails_with_filters(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a paginated list of email objects with optional filtering by properties, associations, and archival status from the CRM email records.

        Args:
            limit (integer): The "limit" parameter specifies the maximum number of email objects to return in the response, with a default value of 10.
            after (string): An optional string parameter used for pagination, indicating the cursor position after which to retrieve results, allowing for retrieval of subsequent pages of data.
            properties (array): Optional array of properties to include in the response for the email object, allowing for customization of returned data.
            propertiesWithHistory (array): Specifies an array of properties for which both current and historical values should be returned in the email object response.
            associations (array): An optional array parameter that specifies the associations to retrieve for the email objects, allowing for filtering or inclusion of related records.
            archived (boolean): Filter emails by archived status, where true includes only archived emails, and false includes only non-archived emails.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_email(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Creates an email object in the CRM using the POST method, allowing for the association of metadata with the email and requiring authentication via OAuth2 or private apps to access the necessary permissions.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_emails_post(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches for email objects in a CRM system using specific criteria, returning relevant results.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/emails/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_read_products_post(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a batch of product records from the CRM using the POST method, optionally filtering by archived status, and returns the results in a multi-status response.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived products in the batch read operation; defaults to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_product_by_id(
        self,
        productId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific product by its ID, allowing optional filtering by properties, properties with history, associations, and archived status.

        Args:
            productId (string): productId
            properties (array): Specifies an array of property names to include in the response, allowing you to request only the specific product properties you need.
            propertiesWithHistory (array): An optional array parameter that specifies which properties to include with their historical data in the response.
            associations (array): An optional array parameter to specify which associations to include in the response, such as related contacts or companies associated with the product.
            archived (boolean): Filter results to include archived products by setting this boolean parameter to true; defaults to false if not specified.
            idProperty (string): Optional string parameter to specify the property used for identifying products.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if productId is None:
            raise ValueError("Missing required parameter 'productId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/{productId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_product_by_id(self, productId: str) -> Any:
        """

        Deletes a product from the CRM using its product ID.

        Args:
            productId (string): productId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if productId is None:
            raise ValueError("Missing required parameter 'productId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/{productId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_product_by_id(
        self,
        productId: str,
        properties: dict[str, str],
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates specified properties of a product identified by productId using a JSON PATCH request.

        Args:
            productId (string): productId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): The idProperty query parameter specifies an optional custom property name to identify the product resource during the PATCH update operation.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if productId is None:
            raise ValueError("Missing required parameter 'productId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/{productId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_products(
        self, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges two or more product records in a CRM system using the POST method, allowing for the consolidation of data into a single, unified record.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_products_batch_post(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of products by ID using the POST method, accepting JSON-formatted request bodies and returning a 204 status upon successful execution.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_products_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates multiple product records in a single batch request within the CRM system.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_products_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates multiple product records in a batch using the HubSpot CRM v3 API and returns a status response indicating success or partial failure.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_product_gdpr_data(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Performs a GDPR-compliant deletion of product records in the CRM using the POST method, requiring a JSON request body and authentication.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_products(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of products from a CRM system using the "GET" method, allowing for optional filtering and customization of the returned data based on parameters such as limit, after, properties, properties with history, associations, and archived status.

        Args:
            limit (integer): The "limit" parameter specifies the maximum number of product objects to return in the response, with a default value of 10.
            after (string): Specifies a cursor for pagination, allowing retrieval of the next page of product results after the specified item.
            properties (array): Optional query parameter to specify the properties of the product object to be returned in the response; it is an array of property names.
            propertiesWithHistory (array): Optional array parameter that specifies the properties for which both current and historical values should be returned in the response.
            associations (array): Optional array parameter to specify associations to be retrieved for the products.
            archived (boolean): Filter products by their archived status; when true, only archived products are returned, otherwise only active products are listed (default is false).

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_product(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Creates a new product in the CRM product library to manage the collection of goods and services offered by the company.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_products(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches for products in a CRM using a POST request to the "/crm/v3/objects/products/search" endpoint, allowing for filtering and retrieval of product data in a JSON format.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/products/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_pipeline_by_id_for_type(
        self, objectType: str, pipelineId: str
    ) -> dict[str, Any]:
        """

        Retrieves details about a specific CRM pipeline by its ID and object type, providing information about the stages and records within that pipeline.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_pipeline(
        self,
        objectType: str,
        pipelineId: str,
        displayOrder: int,
        stages: list[dict[str, Any]],
        label: str,
        validateReferencesBeforeDelete: bool | None = None,
        validateDealStageUsagesBeforeDelete: bool | None = None,
    ) -> dict[str, Any]:
        """

        Updates the details of a specified pipeline for a given CRM object type by replacing its properties using the provided JSON payload.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            displayOrder (integer): The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '0'.
            stages (array): Pipeline stage inputs used to create the new or replacement pipeline. Example: "[{'label': 'In Progress', 'metadata': {'ticketState': 'OPEN'}, 'displayOrder': 0}, {'label': 'Done', 'metadata': {'ticketState': 'CLOSED'}, 'displayOrder': 1}]".
            label (string): A unique label used to organize pipelines in HubSpot's UI Example: 'My replaced pipeline'.
            validateReferencesBeforeDelete (boolean): If set to true, validates whether references exist before deleting the pipeline; defaults to false.
            validateDealStageUsagesBeforeDelete (boolean): Indicates whether to validate deal stage usages before deleting, preventing deletion if stages are in use.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        request_body_data = None
        request_body_data = {
            "displayOrder": displayOrder,
            "stages": stages,
            "label": label,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}"
        query_params = {
            k: v
            for k, v in [
                ("validateReferencesBeforeDelete", validateReferencesBeforeDelete),
                (
                    "validateDealStageUsagesBeforeDelete",
                    validateDealStageUsagesBeforeDelete,
                ),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_pipeline_by_id_and_type(
        self,
        objectType: str,
        pipelineId: str,
        validateReferencesBeforeDelete: bool | None = None,
        validateDealStageUsagesBeforeDelete: bool | None = None,
    ) -> Any:
        """

        Deletes a pipeline by its ID and object type in the CRM system using the specified security permissions, optionally validating references and deal stage usages before deletion.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            validateReferencesBeforeDelete (boolean): Determines whether to validate references before deleting the specified pipeline, defaulting to false if not provided.
            validateDealStageUsagesBeforeDelete (boolean): Determines whether to validate deal stage usages before deleting a pipeline, defaults to false.

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}"
        query_params = {
            k: v
            for k, v in [
                ("validateReferencesBeforeDelete", validateReferencesBeforeDelete),
                (
                    "validateDealStageUsagesBeforeDelete",
                    validateDealStageUsagesBeforeDelete,
                ),
            ]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_pipeline_by_object_type(
        self,
        objectType: str,
        pipelineId: str,
        validateReferencesBeforeDelete: bool | None = None,
        validateDealStageUsagesBeforeDelete: bool | None = None,
        archived: bool | None = None,
        displayOrder: int | None = None,
        label: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates a CRM pipeline by specifying the object type and pipeline ID, allowing modifications to its configuration with optional validation checks for references and deal stage usage before deletion.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            validateReferencesBeforeDelete (boolean): Determines whether to validate references before deleting, defaults to false if not provided.
            validateDealStageUsagesBeforeDelete (boolean): Whether to validate deal stage usages before deleting a pipeline, defaults to false.
            archived (boolean): Whether the pipeline is archived. This property should only be provided when restoring an archived pipeline. If it's provided in any other call, the request will fail and a `400 Bad Request` will be returned.
            displayOrder (integer): The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '0'.
            label (string): A unique label used to organize pipelines in HubSpot's UI Example: 'My updated pipeline'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        request_body_data = None
        request_body_data = {
            "archived": archived,
            "displayOrder": displayOrder,
            "label": label,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}"
        query_params = {
            k: v
            for k, v in [
                ("validateReferencesBeforeDelete", validateReferencesBeforeDelete),
                (
                    "validateDealStageUsagesBeforeDelete",
                    validateDealStageUsagesBeforeDelete,
                ),
            ]
            if v is not None
        }
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def get_pipeline_audit_by_object_type(
        self, objectType: str, pipelineId: str
    ) -> dict[str, Any]:
        """

        Retrieves an audit of all changes to a specific pipeline in HubSpot CRM, based on the provided object type and pipeline ID.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipeline Audits
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/audit"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_pipeline_stages_by_object_type(
        self, objectType: str, pipelineId: str
    ) -> dict[str, Any]:
        """

        Retrieves the list of stages within a specified pipeline for a given object type in the CRM system.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_pipeline_stage(
        self,
        objectType: str,
        pipelineId: str,
        metadata: dict[str, str],
        displayOrder: int,
        label: str,
    ) -> dict[str, Any]:
        """

        Creates a new stage in a specified CRM pipeline using the POST method, requiring the object type and pipeline ID, and a JSON-formatted request body.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            metadata (object): A JSON object containing properties that are not present on all object pipelines.

        For `deals` pipelines, the `probability` field is required (`{ "probability": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.

        For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`. Example: "{'ticketState': 'CLOSED'}".
            displayOrder (integer): The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '1'.
            label (string): A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline. Example: 'Done'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        request_body_data = None
        request_body_data = {
            "metadata": metadata,
            "displayOrder": displayOrder,
            "label": label,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_pipelines_by_type(self, objectType: str) -> dict[str, Any]:
        """

        Retrieves a list of pipelines for a specified object type in the CRM, allowing for the management and inspection of pipelines relevant to that object type.

        Args:
            objectType (string): objectType

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_pipeline_by_object_type(
        self,
        objectType: str,
        displayOrder: int,
        stages: list[dict[str, Any]],
        label: str,
    ) -> dict[str, Any]:
        """

        Creates a new pipeline for the specified CRM object type with the provided pipeline details.

        Args:
            objectType (string): objectType
            displayOrder (integer): The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '0'.
            stages (array): Pipeline stage inputs used to create the new or replacement pipeline. Example: "[{'label': 'In Progress', 'metadata': {'ticketState': 'OPEN'}, 'displayOrder': 0}, {'label': 'Done', 'metadata': {'ticketState': 'CLOSED'}, 'displayOrder': 1}]".
            label (string): A unique label used to organize pipelines in HubSpot's UI Example: 'My replaced pipeline'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            "displayOrder": displayOrder,
            "stages": stages,
            "label": label,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_pipeline_stage_by_id(
        self, objectType: str, pipelineId: str, stageId: str
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific stage within a given pipeline and object type in the CRM system.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            stageId (string): stageId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        if stageId is None:
            raise ValueError("Missing required parameter 'stageId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_pipeline_stage_by_id(
        self,
        objectType: str,
        pipelineId: str,
        stageId: str,
        metadata: dict[str, str],
        displayOrder: int,
        label: str,
    ) -> dict[str, Any]:
        """

        Updates a specific stage in a CRM pipeline using the provided JSON data and returns a status message.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            stageId (string): stageId
            metadata (object): A JSON object containing properties that are not present on all object pipelines.

        For `deals` pipelines, the `probability` field is required (`{ "probability": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.

        For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`. Example: "{'ticketState': 'CLOSED'}".
            displayOrder (integer): The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '1'.
            label (string): A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline. Example: 'Done'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        if stageId is None:
            raise ValueError("Missing required parameter 'stageId'.")
        request_body_data = None
        request_body_data = {
            "metadata": metadata,
            "displayOrder": displayOrder,
            "label": label,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_pipeline_stage_by_id(
        self, objectType: str, pipelineId: str, stageId: str
    ) -> Any:
        """

        Deletes a specific stage from a pipeline for the given object type in the CRM system.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            stageId (string): stageId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        if stageId is None:
            raise ValueError("Missing required parameter 'stageId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_pipeline_stage(
        self,
        objectType: str,
        pipelineId: str,
        stageId: str,
        metadata: dict[str, str],
        archived: bool | None = None,
        displayOrder: int | None = None,
        label: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates a specific stage in a CRM pipeline using a PATCH request to the "/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}" endpoint, requiring a JSON body with the necessary updates.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            stageId (string): stageId
            metadata (object): A JSON object containing properties that are not present on all object pipelines.

        For `deals` pipelines, the `probability` field is required (`{ "probability": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.

        For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`. Example: "{'ticketState': 'CLOSED'}".
            archived (boolean): Whether the pipeline is archived.
            displayOrder (integer): The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '1'.
            label (string): A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline. Example: 'Done'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        if stageId is None:
            raise ValueError("Missing required parameter 'stageId'.")
        request_body_data = None
        request_body_data = {
            "archived": archived,
            "metadata": metadata,
            "displayOrder": displayOrder,
            "label": label,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def batch_read_companies_post(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Reads a batch of companies by internal ID or unique property values using the HubSpot CRM API and returns the results in a JSON format.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): A boolean flag indicating whether to include archived companies in the batch read operation.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_company_by_id(
        self,
        companyId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a specific company record by ID from the CRM system, optionally including additional properties, associations, and historical data, depending on the query parameters provided.

        Args:
            companyId (string): companyId
            properties (array): Optional array parameter to specify the properties of the company object to be returned in the response, allowing for customization of the retrieved data.
            propertiesWithHistory (array): Specifies a comma-separated list of property names for which both the current and historical values should be returned in the response; if a company does not have a value for a property, it will not appear in the response[2].
            associations (array): An optional array parameter specifying the types of associations to include in the response for a company object.
            archived (boolean): When set to true, the archived parameter includes archived company records in the response; defaults to false if omitted.
            idProperty (string): Optional string parameter specifying the property to use as the ID for the companies object.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if companyId is None:
            raise ValueError("Missing required parameter 'companyId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/{companyId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_company_by_id(self, companyId: str) -> Any:
        """

        Deletes a company by its ID using the DELETE method, requiring the company ID as a path parameter and authorization through OAuth2 or private apps with the "crm.objects.companies.write" permission.

        Args:
            companyId (string): companyId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if companyId is None:
            raise ValueError("Missing required parameter 'companyId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/{companyId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_company_by_id(
        self,
        companyId: str,
        properties: dict[str, str],
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates a company in the CRM using the PATCH method, allowing partial modifications to the company's properties.

        Args:
            companyId (string): companyId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Optional query parameter to specify the property used for identifying the object, passed as a string value.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if companyId is None:
            raise ValueError("Missing required parameter 'companyId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/{companyId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_companies_post(
        self, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges two or more company records into a single unified record using the CRM API, requiring a JSON payload and appropriate write permissions.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_companies_batch_post(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of companies using the HubSpot CRM API, requiring a JSON body and returning a 204 status on successful operation.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_companies_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates multiple company records in batch using the HubSpot CRM API and returns a status message, requiring authorization via OAuth2 or private apps.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_companies_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates multiple company records in a single request using the HubSpot CRM API.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_company_gdpr_data(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Performs a GDPR-compliant deletion of a company record in the CRM, permanently removing the associated personal data.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_companies(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of company records from a CRM system, allowing for filtering by properties, associations, and archived status.

        Args:
            limit (integer): The maximum number of company records to return in the response, defaulting to 1 if not specified.
            after (string): The "after" query parameter is an optional string used for pagination to retrieve the next set of results after a specific cursor or record ID in the list of companies.
            properties (array): This optional query parameter allows you to specify an array of properties to be included in the response for companies retrieved via the GET operation.
            propertiesWithHistory (array): Specifies an array of company properties to include both current and historical data in the response.
            associations (array): An optional array parameter specifying the associations to include when retrieving company objects, allowing for the retrieval of related records.
            archived (boolean): Indicates whether to include archived companies in the response.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_company(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Creates a new company record in the CRM system using the provided JSON data and returns a 201 status code upon successful creation.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_companies_post(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches for and retrieves company records and their associated properties in the CRM based on specified criteria.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/companies/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_calling_app_settings(self, appId: str) -> dict[str, Any]:
        """

        Retrieves the calling settings for a specified application in HubSpot CRM using the provided app ID.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/calling/{appId}/settings"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_calling_app_settings(
        self,
        appId: str,
        name: str,
        url: str,
        supportsCustomObjects: bool | None = None,
        isReady: bool | None = None,
        width: int | None = None,
        height: int | None = None,
    ) -> dict[str, Any]:
        """

        Configures calling settings for a specified application ID in the CRM using a POST request with a JSON body.

        Args:
            appId (string): appId
            name (string): The name of your calling service to display to users. Example: 'HubPhone'.
            url (string): The URL to your phone/calling UI, built with the [Calling SDK](#). Example: 'https://www.example.com/hubspot/iframe'.
            supportsCustomObjects (boolean): When true, you are indicating that your service is compatible with engagement v2 service and can be used with custom objects. Example: 'True'.
            isReady (boolean): When true, your service will appear as an option under the *Call* action in contact records of connected accounts. Example: 'True'.
            width (integer): The target width of the iframe that will contain your phone/calling UI. Example: '200'.
            height (integer): The target height of the iframe that will contain your phone/calling UI. Example: '350'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            "supportsCustomObjects": supportsCustomObjects,
            "isReady": isReady,
            "name": name,
            "width": width,
            "url": url,
            "height": height,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/calling/{appId}/settings"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_calling_app_settings_by_id(self, appId: str) -> Any:
        """

        Deletes the settings for a specified CRM application identified by `{appId}`, returning a successful response with no content if the operation is completed.

        Args:
            appId (string): appId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/calling/{appId}/settings"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_calling_settings(
        self,
        appId: str,
        supportsCustomObjects: bool | None = None,
        isReady: bool | None = None,
        name: str | None = None,
        width: int | None = None,
        url: str | None = None,
        height: int | None = None,
    ) -> dict[str, Any]:
        """

        Updates specific settings for the calling extension of the specified application by applying partial modifications to its resource.

        Args:
            appId (string): appId
            supportsCustomObjects (boolean): When true, you are indicating that your service is compatible with engagement v2 service and can be used with custom objects.
            isReady (boolean): When true, your service will appear as an option under the *Call* action in contact records of connected accounts.
            name (string): The name of your calling service to display to users.
            width (integer): The target width of the iframe that will contain your phone/calling UI.
            url (string): The URL to your phone/calling UI, built with the [Calling SDK](#).
            height (integer): The target height of the iframe that will contain your phone/calling UI.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            "supportsCustomObjects": supportsCustomObjects,
            "isReady": isReady,
            "name": name,
            "width": width,
            "url": url,
            "height": height,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/calling/{appId}/settings"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def get_calling_app_recording_settings(self, appId: str) -> dict[str, Any]:
        """

        Retrieves the recording settings for a calling extension with the specified `appId` in the HubSpot CRM.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Recording_Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/calling/{appId}/settings/recording"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def post_calling_app_recording_settings(
        self, appId: str, urlToRetrieveAuthedRecording: str
    ) -> dict[str, Any]:
        """

        Configures call recording settings for a specific application ID in the CRM using a POST request to update the recording settings.

        Args:
            appId (string): appId
            urlToRetrieveAuthedRecording (string): urlToRetrieveAuthedRecording

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Recording_Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            "urlToRetrieveAuthedRecording": urlToRetrieveAuthedRecording
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/calling/{appId}/settings/recording"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_recording_settings(
        self, appId: str, urlToRetrieveAuthedRecording: str | None = None
    ) -> dict[str, Any]:
        """

        Modifies the recording settings for a specific CRM application using the provided JSON body.

        Args:
            appId (string): appId
            urlToRetrieveAuthedRecording (string): urlToRetrieveAuthedRecording

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Recording_Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            "urlToRetrieveAuthedRecording": urlToRetrieveAuthedRecording
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/calling/{appId}/settings/recording"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def read_quotes_batch(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Reads a batch of quote objects by their internal IDs or unique property values, optionally including archived quotes, in a single POST request.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived quotes in the batch read operation, defaults to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_quote_by_id(
        self,
        quoteId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a specific sales quote by its ID, optionally including custom properties, property history, associations, and archived status, using the HubSpot CRM API.

        Args:
            quoteId (string): quoteId
            properties (array): Optional array of properties to include in the response when retrieving a quote object, allowing for customization of the data returned.
            propertiesWithHistory (array): A comma-separated list of properties for which to return both current values and their historical changes in the response.
            associations (array): The "associations" query parameter specifies an optional array of association types to include related objects linked to the quote in the response.
            archived (boolean): Indicates whether to include archived quotes in the response, with a default value of `false`.
            idProperty (string): Optional string parameter to specify the property used for identification in the quotes object.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if quoteId is None:
            raise ValueError("Missing required parameter 'quoteId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/{quoteId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_quote_by_id(self, quoteId: str) -> Any:
        """

        Deletes a sales quote with the specified ID using the HubSpot CRM API, requiring "crm.objects.quotes.write" permission.

        Args:
            quoteId (string): quoteId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if quoteId is None:
            raise ValueError("Missing required parameter 'quoteId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/{quoteId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_quote(
        self, quoteId: str, properties: dict[str, str], idProperty: str | None = None
    ) -> dict[str, Any]:
        """

        Updates a quote object with the specified ID in the CRM system using partial modifications, requiring a JSON body with the changes and returning a status message upon success.

        Args:
            quoteId (string): quoteId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): The optional query parameter to specify a custom property name to use as the unique identifier for the quote object.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if quoteId is None:
            raise ValueError("Missing required parameter 'quoteId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/{quoteId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_quotes(
        self, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges quote objects in a CRM system using the POST method, allowing for the integration of data from multiple quotes into a single unified quote.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_quotes_batch(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of quotes by sending a POST request to the "/crm/v3/objects/quotes/batch/archive" endpoint, requiring a JSON body and authentication via OAuth2 or private apps with the "crm.objects.quotes.write" permission.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_quote_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates a batch of sales quotes using the HubSpot CRM API, requiring a JSON body and returning a status message upon successful creation.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_quotes_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates a batch of quote objects in the CRM system using a single POST request, returning a status code indicating success or partial failure.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_quote_gdpr_data(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Performs a GDPR-compliant deletion of a quote object in the CRM system, permanently removing the associated personal data.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_quotes(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of quotes from the CRM, allowing for optional filtering by limit, after, properties, properties with history, associations, and archived status.

        Args:
            limit (integer): Specifies the maximum number of quote objects to return in the response, with a default value of 10.
            after (string): Cursor for pagination; the string value to retrieve results after a specific record in the result set.
            properties (array): Optional array parameter to specify which properties of the quote object to include in the response.
            propertiesWithHistory (array): A comma-separated list of properties to include historical data in the response for the quote object.
            associations (array): An array of associations to include in the response, specifying the related CRM objects or activities to retrieve alongside the quotes.
            archived (boolean): Indicates whether to include archived quotes in the response, defaults to false.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_quote(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Creates a new quote in HubSpot using the CRM API and returns a status message upon successful creation.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_quotes(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches for quotes in a CRM system using specified criteria and returns the results, requiring authentication via OAuth2 or private apps with read permissions for quotes.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/quotes/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_read_deals_post(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Reads a batch of deals from the CRM using the provided IDs and returns the specified properties, allowing for optional filtering by archived status.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived deals in the batch read operation.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_deal_by_id(
        self,
        dealId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a deal by its ID and returns its details, supporting optional parameters for specifying properties, associations, and archived status.

        Args:
            dealId (string): dealId
            properties (array): Optional array of properties to include in the response for the specified deal.
            propertiesWithHistory (array): A comma-separated list of deal properties for which current and historical values should be returned in the response.
            associations (array): List of associations to include with the deal, such as contacts, companies, or products, allowing for retrieval of related objects.
            archived (boolean): Optional boolean parameter to indicate whether to include archived deals in the response.
            idProperty (string): Optional query parameter "idProperty" of type string, used to specify a custom property for filtering or retrieving specific data related to the deal.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if dealId is None:
            raise ValueError("Missing required parameter 'dealId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/{dealId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_deal_by_id(self, dealId: str) -> Any:
        """

        Deletes a specific deal by its ID from the CRM system.

        Args:
            dealId (string): dealId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if dealId is None:
            raise ValueError("Missing required parameter 'dealId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/{dealId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_deal_by_id(
        self, dealId: str, properties: dict[str, str], idProperty: str | None = None
    ) -> dict[str, Any]:
        """

        Updates an individual deal in the CRM by its record ID using the PATCH method.

        Args:
            dealId (string): dealId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Optional string parameter to specify the ID property for the deal object in the patch operation.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if dealId is None:
            raise ValueError("Missing required parameter 'dealId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/{dealId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_deals(self, objectIdToMerge: str, primaryObjectId: str) -> dict[str, Any]:
        """

        Merges two or more deal records into a single master deal record, consolidating data and deleting duplicates in the CRM system.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_deals_batch_post(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of deal records in the CRM by their IDs using the POST method.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_deals_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates multiple deals in a CRM using a batch operation via the POST method, requiring a JSON body with deal data and appropriate permissions for writing deals.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_update_deals(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates multiple deals in HubSpot CRM in a single operation using a POST request to "/crm/v3/objects/deals/batch/update", requiring a JSON body with deal identifiers and updates, and supports OAuth2 and private app authentication for the "crm.objects.deals.write" scope.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def post_deal_gdpr_delete(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Deletes a deal record in compliance with GDPR requirements using the provided JSON payload, requiring a valid OAuth2 or private app authentication with the necessary write permissions.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_deals(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of CRM deal objects from HubSpot using the GET method, allowing optional filtering by parameters such as limit, after, properties, propertiesWithHistory, associations, and archived status.

        Args:
            limit (integer): Specifies the maximum number of deals to return in the response, defaulting to 10.
            after (string): Cursor for pagination to retrieve results after a specific identifier in the list of deals.
            properties (array): Optional array of properties to include in the response for each deal, allowing for customization of the data retrieved.
            propertiesWithHistory (array): Optional array parameter specifying the deal properties for which historical values should be returned, reducing the maximum number of objects that can be read in a single request.
            associations (array): Optional array parameter that specifies the associations to include in the response for the retrieved deals.
            archived (boolean): Indicates whether to retrieve only archived deals, with true returning archived deals and false returning non-archived deals.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_deal(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Creates a new deal object in the CRM using the HubSpot API, requiring a JSON payload and returning a status code indicating success.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_deals(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches and retrieves deal records in the CRM using filters and criteria provided in the request body.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/deals/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def cancel_import_by_id(self, importId: str) -> dict[str, Any]:
        """

        Cancels an active import operation in a CRM system using the provided import ID.

        Args:
            importId (string): importId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if importId is None:
            raise ValueError("Missing required parameter 'importId'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/crm/v3/imports/{importId}/cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_import_by_id(self, importId: str) -> dict[str, Any]:
        """

        Retrieves the status and details of a specific CRM import operation identified by the import ID.

        Args:
            importId (string): importId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if importId is None:
            raise ValueError("Missing required parameter 'importId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/imports/{importId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_import_errors_by_id(
        self, importId: str, after: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """

        Retrieves a list of errors associated with a specific CRM import operation, using the import ID, and allows filtering by optional parameters such as "after" and "limit".

        Args:
            importId (string): importId
            after (string): Used to specify a cursor for pagination, indicating the position after which to retrieve the next set of error records.
            limit (integer): The "limit" parameter specifies the maximum number of error records to return in the response for the specified import ID.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Imports
        """
        if importId is None:
            raise ValueError("Missing required parameter 'importId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/imports/{importId}/errors"
        query_params = {
            k: v for k, v in [("after", after), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_schema_by_object_type(self, objectType: str) -> dict[str, Any]:
        """

        Retrieves the schema definition for a specified CRM object type, including its properties and metadata.

        Args:
            objectType (string): objectType

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.main_app_client.base_url}/crm/v3/schemas/{objectType}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_schema_by_type(
        self, objectType: str, archived: bool | None = None
    ) -> Any:
        """

        Deletes the specified CRM object schema by its type, optionally including archived versions, to remove its definition from the system.

        Args:
            objectType (string): objectType
            archived (boolean): A boolean query parameter indicating whether to operate on archived schemas, defaulting to false if not specified.

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.main_app_client.base_url}/crm/v3/schemas/{objectType}"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_crm_schema_by_object_type(
        self,
        objectType: str,
        description: str | None = None,
        secondaryDisplayProperties: list[str] | None = None,
        requiredProperties: list[str] | None = None,
        searchableProperties: list[str] | None = None,
        primaryDisplayProperty: str | None = None,
        restorable: bool | None = None,
        labels: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """

        Updates a custom CRM object schema in HubSpot using the PATCH method, allowing for partial modifications to the schema of a specified object type.

        Args:
            objectType (string): objectType
            description (string): description
            secondaryDisplayProperties (array): The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.
            requiredProperties (array): The names of properties that should be **required** when creating an object of this type. Example: "['my_object_property']".
            searchableProperties (array): Names of properties that will be indexed for this object type in by HubSpot's product search. Example: "['my_object_property']".
            primaryDisplayProperty (string): The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type. Example: 'my_object_property'.
            restorable (boolean): restorable
            labels (object): Singular and plural labels for the object. Used in CRM display. Example: "{'singular': 'My object', 'plural': 'My objects'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            "description": description,
            "secondaryDisplayProperties": secondaryDisplayProperties,
            "requiredProperties": requiredProperties,
            "searchableProperties": searchableProperties,
            "primaryDisplayProperty": primaryDisplayProperty,
            "restorable": restorable,
            "labels": labels,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/schemas/{objectType}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def create_object_type_association(
        self,
        objectType: str,
        fromObjectTypeId: str,
        toObjectTypeId: str,
        name: str | None = None,
    ) -> dict[str, Any]:
        """

        Creates a new association definition for the specified CRM object type to define relationships between that object and others.

        Args:
            objectType (string): objectType
            fromObjectTypeId (string): ID of the primary object type to link from. Example: '2-123456'.
            toObjectTypeId (string): ID of the target object type ID to link to. Example: 'contact'.
            name (string): A unique name for this association. Example: 'my_object_to_contact'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            "fromObjectTypeId": fromObjectTypeId,
            "name": name,
            "toObjectTypeId": toObjectTypeId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.main_app_client.base_url}/crm/v3/schemas/{objectType}/associations"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_schema_object_type_purge(self, objectType: str) -> Any:
        """

        Purges a schema for a specific object type in the CRM system using the DELETE method, requiring the objectType as a path parameter and a custom write permission.

        Args:
            objectType (string): objectType

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object_Schemas
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.main_app_client.base_url}/crm/v3/schemas/{objectType}/purge"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def delete_association_by_object_type_id(
        self, objectType: str, associationIdentifier: str
    ) -> Any:
        """

        Removes an association identified by the associationIdentifier from a CRM object schema of the specified objectType using the HubSpot API.

        Args:
            objectType (string): objectType
            associationIdentifier (string): associationIdentifier

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if associationIdentifier is None:
            raise ValueError("Missing required parameter 'associationIdentifier'.")
        url = f"{self.main_app_client.base_url}/crm/v3/schemas/{objectType}/associations/{associationIdentifier}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def list_schemas(self, archived: bool | None = None) -> dict[str, Any]:
        """

        Retrieves a list of custom object schemas in the CRM, optionally filtering by archived status, using either legacy private apps or OAuth2 credentials for authentication.

        Args:
            archived (boolean): Filter results by their archival status; when set to true, only archived schemas are returned, otherwise only active schemas (default is false).

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        url = f"{self.main_app_client.base_url}/crm/v3/schemas"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_crm_schema(
        self,
        requiredProperties: list[str],
        name: str,
        associatedObjects: list[str],
        properties: list[dict[str, Any]],
        labels: dict[str, Any],
        description: str | None = None,
        secondaryDisplayProperties: list[str] | None = None,
        searchableProperties: list[str] | None = None,
        primaryDisplayProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Creates a new custom object schema in the CRM to define a new type of CRM record.

        Args:
            requiredProperties (array): The names of properties that should be **required** when creating an object of this type. Example: "['my_object_property']".
            name (string): A unique name for this object. For internal use only. Example: 'my_object'.
            associatedObjects (array): Associations defined for this object type. Example: "['CONTACT']".
            properties (array): Properties defined for this object type. Example: "[{'name': 'my_object_property', 'label': 'My object property', 'isPrimaryDisplayLabel': True}]".
            labels (object): Singular and plural labels for the object. Used in CRM display. Example: "{'singular': 'My object', 'plural': 'My objects'}".
            description (string): description
            secondaryDisplayProperties (array): The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.
            searchableProperties (array): Names of properties that will be indexed for this object type in by HubSpot's product search.
            primaryDisplayProperty (string): The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type. Example: 'my_object_property'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        request_body_data = None
        request_body_data = {
            "description": description,
            "secondaryDisplayProperties": secondaryDisplayProperties,
            "requiredProperties": requiredProperties,
            "searchableProperties": searchableProperties,
            "primaryDisplayProperty": primaryDisplayProperty,
            "name": name,
            "associatedObjects": associatedObjects,
            "properties": properties,
            "labels": labels,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/schemas"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_properties_batch_post(
        self, objectType: str, inputs: list[dict[str, Any]]
    ) -> Any:
        """

        Archives a batch of properties for a specified object type in CRM using a POST request.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_property_group(self, objectType: str, groupName: str) -> dict[str, Any]:
        """

        Retrieves details of a specified property group for a given CRM object type.

        Args:
            objectType (string): objectType
            groupName (string): groupName

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if groupName is None:
            raise ValueError("Missing required parameter 'groupName'.")
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/groups/{groupName}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def remove_property_group(self, objectType: str, groupName: str) -> Any:
        """

        Deletes a property group identified by the given object type and group name from the CRM schema.

        Args:
            objectType (string): objectType
            groupName (string): groupName

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if groupName is None:
            raise ValueError("Missing required parameter 'groupName'.")
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/groups/{groupName}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_property_group_by_identifier(
        self,
        objectType: str,
        groupName: str,
        displayOrder: int | None = None,
        label: str | None = None,
    ) -> dict[str, Any]:
        """

        Modifies the properties of a specified group in a CRM object type using the PATCH method, requiring authentication and a JSON request body to update the group's properties.

        Args:
            objectType (string): objectType
            groupName (string): groupName
            displayOrder (integer): Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values. Example: '-1'.
            label (string): A human-readable label that will be shown in HubSpot. Example: 'My Property Group'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if groupName is None:
            raise ValueError("Missing required parameter 'groupName'.")
        request_body_data = None
        request_body_data = {"displayOrder": displayOrder, "label": label}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/groups/{groupName}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def get_crm_property(
        self,
        objectType: str,
        propertyName: str,
        archived: bool | None = None,
        properties: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves the details of a specific property for a given CRM object type, optionally including archived properties and additional specified fields.

        Args:
            objectType (string): objectType
            propertyName (string): propertyName
            archived (boolean): Optional boolean query parameter to filter results by archived status.
            properties (string): The "properties" query parameter specifies a comma-separated list of property names to include in the response for the given object type and property name, allowing you to customize which property details are returned.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if propertyName is None:
            raise ValueError("Missing required parameter 'propertyName'.")
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/{propertyName}"
        query_params = {
            k: v
            for k, v in [("archived", archived), ("properties", properties)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_property_by_object_type(self, objectType: str, propertyName: str) -> Any:
        """

        Deletes a specified property of a given object type in the CRM system.

        Args:
            objectType (string): objectType
            propertyName (string): propertyName

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if propertyName is None:
            raise ValueError("Missing required parameter 'propertyName'.")
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/{propertyName}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_crm_property_by_name(
        self,
        objectType: str,
        propertyName: str,
        description: str | None = None,
        groupName: str | None = None,
        hidden: bool | None = None,
        options: list[dict[str, Any]] | None = None,
        displayOrder: int | None = None,
        calculationFormula: str | None = None,
        label: str | None = None,
        type: str | None = None,
        fieldType: str | None = None,
        formField: bool | None = None,
    ) -> dict[str, Any]:
        """

        Updates the specified property of a given CRM object type by applying partial modifications using a JSON Patch request.

        Args:
            objectType (string): objectType
            propertyName (string): propertyName
            description (string): A description of the property that will be shown as help text in HubSpot.
            groupName (string): The name of the property group the property belongs to. Example: 'contactinformation'.
            hidden (boolean): If true, the property won't be visible and can't be used in HubSpot. Example: 'False'.
            options (array): A list of valid options for the property. Example: "[{'description': 'Choice number one', 'label': 'Option A', 'value': 'A', 'hidden': False, 'displayOrder': 1}, {'description': 'Choice number two', 'label': 'Option B', 'value': 'B', 'hidden': False, 'displayOrder': 2}]".
            displayOrder (integer): Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the Property to be displayed after any positive values. Example: '2'.
            calculationFormula (string): Represents a formula that is used to compute a calculated property.
            label (string): A human-readable property label that will be shown in HubSpot. Example: 'My Contact Property'.
            type (string): The data type of the property. Example: 'enumeration'.
            fieldType (string): Controls how the property appears in HubSpot. Example: 'select'.
            formField (boolean): Whether or not the property can be used in a HubSpot form. Example: 'True'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if propertyName is None:
            raise ValueError("Missing required parameter 'propertyName'.")
        request_body_data = None
        request_body_data = {
            "description": description,
            "groupName": groupName,
            "hidden": hidden,
            "options": options,
            "displayOrder": displayOrder,
            "calculationFormula": calculationFormula,
            "label": label,
            "type": type,
            "fieldType": fieldType,
            "formField": formField,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/{propertyName}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def batch_read_properties_by_object_type(
        self, objectType: str, archived: bool, inputs: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """

        Performs a batch read operation on CRM properties for a specified object type using a POST request, returning the results in a batch format.

        Args:
            objectType (string): objectType
            archived (boolean): archived
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"archived": archived, "inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/batch/read"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_batch_properties(
        self, objectType: str, inputs: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """

        Creates multiple properties in batches for a specified object type in the CRM using a POST request to the "/crm/v3/properties/{objectType}/batch/create" endpoint.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_properties_by_object_type(
        self,
        objectType: str,
        archived: bool | None = None,
        properties: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of properties for a specified CRM object type using the HubSpot API, allowing for optional filtering by archived status and specific properties.

        Args:
            objectType (string): objectType
            archived (boolean): A boolean query parameter indicating whether to include archived properties in the response.
            properties (string): Specifies a comma-separated list of property names to include in the response, allowing you to retrieve only certain properties for the object instead of all defaults.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}"
        query_params = {
            k: v
            for k, v in [("archived", archived), ("properties", properties)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_property_schema(
        self,
        objectType: str,
        label: str,
        type: str,
        groupName: str,
        name: str,
        fieldType: str,
        description: str | None = None,
        hidden: bool | None = None,
        displayOrder: int | None = None,
        formField: bool | None = None,
        referencedObjectType: str | None = None,
        options: list[dict[str, Any]] | None = None,
        calculationFormula: str | None = None,
        hasUniqueValue: bool | None = None,
        externalOptions: bool | None = None,
    ) -> dict[str, Any]:
        """

        Creates a new custom property for a specified CRM object type.

        Args:
            objectType (string): objectType
            label (string): A human-readable property label that will be shown in HubSpot. Example: 'My Contact Property'.
            type (string): The data type of the property. Example: 'enumeration'.
            groupName (string): The name of the property group the property belongs to. Example: 'contactinformation'.
            name (string): The internal property name, which must be used when referencing the property via the API.
            fieldType (string): Controls how the property appears in HubSpot. Example: 'select'.
            description (string): A description of the property that will be shown as help text in HubSpot.
            hidden (boolean): If true, the property won't be visible and can't be used in HubSpot. Example: 'False'.
            displayOrder (integer): Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property to be displayed after any positive values. Example: '2'.
            formField (boolean): Whether or not the property can be used in a HubSpot form. Example: 'True'.
            referencedObjectType (string): Should be set to 'OWNER' when 'externalOptions' is true, which causes the property to dynamically pull option values from the current HubSpot users.
            options (array): A list of valid options for the property. This field is required for enumerated properties. Example: "[{'description': 'Choice number one', 'label': 'Option A', 'value': 'A', 'hidden': False, 'displayOrder': 1}, {'description': 'Choice number two', 'label': 'Option B', 'value': 'B', 'hidden': False, 'displayOrder': 2}]".
            calculationFormula (string): Represents a formula that is used to compute a calculated property.
            hasUniqueValue (boolean): Whether or not the property's value must be unique. Once set, this can't be changed. Example: 'False'.
            externalOptions (boolean): Applicable only for 'enumeration' type properties.  Should be set to true in conjunction with a 'referencedObjectType' of 'OWNER'.  Otherwise false.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            "description": description,
            "hidden": hidden,
            "displayOrder": displayOrder,
            "label": label,
            "type": type,
            "formField": formField,
            "groupName": groupName,
            "referencedObjectType": referencedObjectType,
            "name": name,
            "options": options,
            "calculationFormula": calculationFormula,
            "hasUniqueValue": hasUniqueValue,
            "fieldType": fieldType,
            "externalOptions": externalOptions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_property_groups_by_object_type(self, objectType: str) -> dict[str, Any]:
        """

        Retrieves a list of groups for a specified object type in the CRM using the "GET" method at the path "/crm/v3/properties/{objectType}/groups".

        Args:
            objectType (string): objectType

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/groups"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_property_group(
        self, objectType: str, name: str, label: str, displayOrder: int | None = None
    ) -> dict[str, Any]:
        """

        Creates a new property group for the specified CRM object type to organize related properties within HubSpot records.

        Args:
            objectType (string): objectType
            name (string): The internal property group name, which must be used when referencing the property group via the API. Example: 'mypropertygroup'.
            label (string): A human-readable label that will be shown in HubSpot. Example: 'My Property Group'.
            displayOrder (integer): Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values. Example: '-1'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"name": name, "displayOrder": displayOrder, "label": label}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/properties/{objectType}/groups"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_owner_by_id(
        self,
        ownerId: str,
        idProperty: str | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific CRM owner by their ID using the HubSpot API.

        Args:
            ownerId (string): ownerId
            idProperty (string): Specifies the property to use for identifying owners, accepting values 'id' or 'userId', with 'id' as the default.
            archived (boolean): Whether to include archived owners in the response; defaults to false.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Owners
        """
        if ownerId is None:
            raise ValueError("Missing required parameter 'ownerId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/owners/{ownerId}"
        query_params = {
            k: v
            for k, v in [("idProperty", idProperty), ("archived", archived)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def batch_create_timeline_events(
        self, inputs: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """

        Creates multiple timeline events in a batch using the provided event templates and returns a response with the created events.

        Args:
            inputs (array): A collection of timeline events we want to create. Example: '[{'email': 'art3mis-pup@petspot.com', 'tokens': {'petAge': 3, 'petName': 'Art3mis', 'petColor': 'black'}, 'extraData': {'questions': [{'answer': 'Bark!', 'question': "Who's a good girl?"}, {'answer': 'Woof!', 'question': 'Do you wanna go on a walk?'}]}, 'timelineIFrame': {'url': 'https://my.petspot.com/pets/Art3mis', 'width': 600, 'height': 400, 'linkLabel': 'View Art3mis', 'headerLabel': 'Art3mis dog'}, 'eventTemplateId': '1001298'}, {'email': 'pocket-tiger@petspot.com', 'tokens': {'petAge': 3, 'petName': 'Pocket', 'petColor': 'yellow'}, 'extraData': {'questions': [{'answer': 'Purr...', 'question': "Who's a good kitty?"}, {'answer': 'Meow!', 'question': 'Will you stop playing with that?'}]}, 'timelineIFrame': {'url': 'https://my.petspot.com/pets/Pocket', 'width': 600, 'height': 400, 'linkLabel': 'View Pocket', 'headerLabel': 'Pocket Tiger'}, 'eventTemplateId': '1001298'}]'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Events
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/events/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_timeline_event_template_by_id(
        self, appId: str, eventTemplateId: str
    ) -> dict[str, Any]:
        """

        Retrieves a specific event template by its ID for an application in HubSpot CRM, using the provided app ID and event template ID.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_timeline_event_template_by_id(
        self,
        appId: str,
        eventTemplateId: str,
        name: str,
        tokens: list[dict[str, Any]],
        id: str,
        detailTemplate: str | None = None,
        headerTemplate: str | None = None,
    ) -> dict[str, Any]:
        """

                Updates an existing event template in the HubSpot CRM timeline for a specific app, using the provided event template ID and app ID, and returns a status message.

                Args:
                    appId (string): appId
                    eventTemplateId (string): eventTemplateId
                    name (string): The template name. Example: 'PetSpot Registration'.
                    tokens (array): A collection of tokens that can be used as custom properties on the event and to create fully fledged CRM objects. Example: "[{'name': 'petName', 'type': 'string', 'label': 'Pet Name', 'objectPropertyName': 'firstname'}, {'name': 'petAge', 'type': 'number', 'label': 'Pet Age'}, {'name': 'petColor', 'type': 'enumeration', 'label': 'Pet Color', 'options': [{'label': 'White', 'value': 'white'}, {'label': 'Black', 'value': 'black'}, {'label': 'Brown', 'value': 'brown'}, {'label': 'Yellow', 'value': 'yellow'}, {'label': 'Other', 'value': 'other'}]}]".
                    id (string): The template ID. Example: '1001298'.
                    detailTemplate (string): This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline when you expand the details. Example: 'Registration occurred at {{#formatDate timestamp}}{{/formatDate}}

        #### Questions
        {{#each extraData.questions}}
          **{{question}}**: {{answer}}
        {{/each}}

        EDIT'.
                    headerTemplate (string): This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline as a header. Example: 'Registered for [{{petName}}](https://my.petspot.com/pets/{{petName}})'.

                Returns:
                    dict[str, Any]: successful operation

                Raises:
                    HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

                Tags:
                    Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        request_body_data = None
        request_body_data = {
            "detailTemplate": detailTemplate,
            "name": name,
            "tokens": tokens,
            "id": id,
            "headerTemplate": headerTemplate,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_event_template_by_id(self, appId: str, eventTemplateId: str) -> Any:
        """

        Deletes an event template with the specified `eventTemplateId` associated with the application identified by `appId` in a CRM system, returning a successful response with no content upon completion.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def create_event(
        self,
        eventTemplateId: str,
        tokens: dict[str, str],
        extraData: dict[str, Any] | None = None,
        timelineIFrame: dict[str, Any] | None = None,
        domain: str | None = None,
        id: str | None = None,
        utk: str | None = None,
        email: str | None = None,
        objectId: str | None = None,
        timestamp: str | None = None,
    ) -> dict[str, Any]:
        """

        Creates a new timeline event in a CRM record based on an event template, adding custom event information to the timeline of a contact, company, or deal.

        Args:
            eventTemplateId (string): The event template ID. Example: '1001298'.
            tokens (object): A collection of token keys and values associated with the template tokens. Example: "{'petAge': 3, 'petName': 'Art3mis', 'petColor': 'black'}".
            extraData (object): Additional event-specific data that can be interpreted by the template's markdown. Example: '{'questions': [{'answer': 'Bark!', 'question': "Who's a good girl?"}, {'answer': 'Woof!', 'question': 'Do you wanna go on a walk?'}]}'.
            timelineIFrame (object): timelineIFrame Example: "{'linkLabel': 'View Art3mis', 'headerLabel': 'Art3mis dog', 'url': 'https://my.petspot.com/pets/Art3mis', 'width': 600, 'height': 400}".
            domain (string): The event domain (often paired with utk).
            id (string): Identifier for the event. This is optional, and we recommend you do not pass this in. We will create one for you if you omit this. You can also use `{{uuid}}` anywhere in the ID to generate a unique string, guaranteeing uniqueness.
            utk (string): Use the `utk` parameter to associate an event with a contact by `usertoken`. This is recommended if you don't know a user's email, but have an identifying user token in your cookie.
            email (string): The email address used for contact-specific events. This can be used to identify existing contacts, create new ones, or change the email for an existing contact (if paired with the `objectId`). Example: 'art3mis-pup@petspot.com'.
            objectId (string): The CRM object identifier. This is required for every event other than contacts (where utk or email can be used).
            timestamp (string): The time the event occurred. If not passed in, the curren time will be assumed. This is used to determine where an event is shown on a CRM object's timeline.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Events
        """
        request_body_data = None
        request_body_data = {
            "eventTemplateId": eventTemplateId,
            "extraData": extraData,
            "timelineIFrame": timelineIFrame,
            "domain": domain,
            "tokens": tokens,
            "id": id,
            "utk": utk,
            "email": email,
            "objectId": objectId,
            "timestamp": timestamp,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/events"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_token_template(
        self,
        appId: str,
        eventTemplateId: str,
        name: str,
        label: str,
        type: str,
        createdAt: str | None = None,
        options: list[dict[str, Any]] | None = None,
        objectPropertyName: str | None = None,
        updatedAt: str | None = None,
    ) -> dict[str, Any]:
        """

        Creates a new token for an event template in the HubSpot CRM timeline using the provided JSON data.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId
            name (string): The name of the token referenced in the templates. This must be unique for the specific template. It may only contain alphanumeric characters, periods, dashes, or underscores (. - _). Example: 'petType'.
            label (string): Used for list segmentation and reporting. Example: 'Pet Type'.
            type (string): The data type of the token. You can currently choose from [string, number, date, enumeration]. Example: 'enumeration'.
            createdAt (string): The date and time that the Event Template Token was created, as an ISO 8601 timestamp. Will be null if the template was created before Feb 18th, 2020. Example: '2020-02-12T20:58:26Z'.
            options (array): If type is `enumeration`, we should have a list of options to choose from. Example: "[{'label': 'Dog', 'value': 'dog'}, {'label': 'Cat', 'value': 'cat'}]".
            objectPropertyName (string): The name of the CRM object property. This will populate the CRM object property associated with the event. With enough of these, you can fully build CRM objects via the Timeline API. Example: 'customPropertyPetType'.
            updatedAt (string): The date and time that the Event Template Token was last updated, as an ISO 8601 timestamp. Will be null if the template was created before Feb 18th, 2020. Example: '2020-02-12T20:58:26Z'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Tokens
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        request_body_data = None
        request_body_data = {
            "createdAt": createdAt,
            "options": options,
            "name": name,
            "label": label,
            "objectPropertyName": objectPropertyName,
            "type": type,
            "updatedAt": updatedAt,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_event_template_token(
        self,
        appId: str,
        eventTemplateId: str,
        tokenName: str,
        label: str,
        options: list[dict[str, Any]] | None = None,
        objectPropertyName: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates a specific token in an event template within a CRM timeline using the provided JSON data.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId
            tokenName (string): tokenName
            label (string): Used for list segmentation and reporting. Example: 'petType edit'.
            options (array): If type is `enumeration`, we should have a list of options to choose from. Example: "[{'label': 'Dog', 'value': 'dog'}, {'label': 'Cat', 'value': 'cat'}, {'label': 'Bird', 'value': 'bird'}]".
            objectPropertyName (string): The name of the CRM object property. This will populate the CRM object property associated with the event. With enough of these, you can fully build CRM objects via the Timeline API.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Tokens
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if tokenName is None:
            raise ValueError("Missing required parameter 'tokenName'.")
        request_body_data = None
        request_body_data = {
            "options": options,
            "label": label,
            "objectPropertyName": objectPropertyName,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_timeline_event_template_token(
        self, appId: str, eventTemplateId: str, tokenName: str
    ) -> Any:
        """

        Deletes a token by the specified name from an event template in the CRM timeline for a given application ID.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId
            tokenName (string): tokenName

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Tokens
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if tokenName is None:
            raise ValueError("Missing required parameter 'tokenName'.")
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def get_timeline_event_detail_by_id(
        self, eventTemplateId: str, eventId: str
    ) -> dict[str, Any]:
        """

        Retrieves detailed information for a specific timeline event identified by its event template ID and event ID in the CRM.

        Args:
            eventTemplateId (string): eventTemplateId
            eventId (string): eventId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Events
        """
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if eventId is None:
            raise ValueError("Missing required parameter 'eventId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/events/{eventTemplateId}/{eventId}/detail"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_timeline_event_by_id(
        self, eventTemplateId: str, eventId: str
    ) -> dict[str, Any]:
        """

        Retrieves a specific timeline event by its event template ID and event ID, returning detailed information about that event in the CRM.

        Args:
            eventTemplateId (string): eventTemplateId
            eventId (string): eventId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Events
        """
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if eventId is None:
            raise ValueError("Missing required parameter 'eventId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/events/{eventTemplateId}/{eventId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_timeline_event_templates_by_app_id(self, appId: str) -> dict[str, Any]:
        """

        Retrieves a list of event templates for a specified app ID in the HubSpot CRM API.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/{appId}/event-templates"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_timeline_event_template(
        self,
        appId: str,
        name: str,
        tokens: list[dict[str, Any]],
        objectType: str,
        detailTemplate: str | None = None,
        headerTemplate: str | None = None,
    ) -> dict[str, Any]:
        """

                Creates a new event template for a specified application ID in HubSpot's CRM timeline using the provided JSON payload.

                Args:
                    appId (string): appId
                    name (string): The template name. Example: 'PetSpot Registration'.
                    tokens (array): A collection of tokens that can be used as custom properties on the event and to create fully fledged CRM objects. Example: "[{'name': 'petName', 'type': 'string', 'label': 'Pet Name'}, {'name': 'petAge', 'type': 'number', 'label': 'Pet Age'}, {'name': 'petColor', 'type': 'enumeration', 'label': 'Pet Color', 'options': [{'label': 'White', 'value': 'white'}, {'label': 'Black', 'value': 'black'}, {'label': 'Brown', 'value': 'brown'}, {'label': 'Other', 'value': 'other'}]}]".
                    objectType (string): The type of CRM object this template is for. [Contacts, companies, tickets, and deals] are supported. Example: 'contacts'.
                    detailTemplate (string): This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline when you expand the details. Example: 'Registration occurred at {{#formatDate timestamp}}{{/formatDate}}

        #### Questions
        {{#each extraData.questions}}
          **{{question}}**: {{answer}}
        {{/each}}'.
                    headerTemplate (string): This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline as a header. Example: 'Registered for [{{petName}}](https://my.petspot.com/pets/{{petName}})'.

                Returns:
                    dict[str, Any]: successful operation

                Raises:
                    HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

                Tags:
                    Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            "detailTemplate": detailTemplate,
            "name": name,
            "tokens": tokens,
            "headerTemplate": headerTemplate,
            "objectType": objectType,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/{appId}/event-templates"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_timeline_event_render(
        self, eventTemplateId: str, eventId: str, detail: bool | None = None
    ) -> Any:
        """

        Retrieves and renders a specific timeline event from a CRM object using an event template and event ID, allowing for optional detailed rendering.

        Args:
            eventTemplateId (string): eventTemplateId
            eventId (string): eventId
            detail (boolean): Specifies whether the response should include additional detailed information for the timeline event.

        Returns:
            Any: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Events
        """
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if eventId is None:
            raise ValueError("Missing required parameter 'eventId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/timeline/events/{eventTemplateId}/{eventId}/render"
        query_params = {k: v for k, v in [("detail", detail)] if v is not None}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def batch_read_contacts_post(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a batch of contacts from the CRM using the provided identifiers and properties, supporting optional filtering by archived status.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): A boolean query parameter indicating whether to include archived contacts in the batch read operation, defaulting to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_contact_by_id(
        self,
        contactId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a contact by ID from the CRM, allowing for optional filtering by properties, properties with history, associations, and archived status.

        Args:
            contactId (string): contactId
            properties (array): Array of contact property names to include in the response, allowing customization of which contact fields are returned.
            propertiesWithHistory (array): A comma-separated list of contact properties for which to return both current values and their full change history in the response.
            associations (array): Array of association types to include related object associations in the response.
            archived (boolean): Optional boolean parameter to include or exclude archived contacts; defaults to false.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if contactId is None:
            raise ValueError("Missing required parameter 'contactId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/{contactId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_contact_by_id(self, contactId: str) -> Any:
        """

        Deletes a contact by its ID from the CRM system, permanently removing all associated content in compliance with GDPR, and requires the "crm.objects.contacts.write" permission.

        Args:
            contactId (string): contactId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if contactId is None:
            raise ValueError("Missing required parameter 'contactId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/{contactId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_contact_by_id(
        self, contactId: str, properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Updates an individual contact by its record ID using a PATCH request to the "/crm/v3/objects/contacts/{contactId}" endpoint, requiring a JSON body with the fields to be updated.

        Args:
            contactId (string): contactId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if contactId is None:
            raise ValueError("Missing required parameter 'contactId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/{contactId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_contacts(
        self, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges two or more duplicate contact records into a single record in the CRM system, retaining the most relevant data while discarding redundant information.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_contacts_batch_post(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of contacts by ID using the HubSpot CRM API, returning a "204 No Content" response upon success.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_contacts_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates a batch of contacts in HubSpot using the CRM API, requiring a JSON payload and OAuth2 or private app authentication.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_update_contacts(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates multiple contact records in a single request by providing their IDs or unique property values, overwriting specified properties in batch.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_contact_gdpr_data(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Permanently deletes a contact and all associated data from the CRM to comply with GDPR requirements.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_contacts(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of contacts from a CRM system, allowing for optional filtering by limit, pagination, specific properties, property history, associations, and archived status.

        Args:
            limit (integer): Specifies the maximum number of contact records to return in the response, with a default value of 5.
            after (string): An optional string parameter used for pagination, specifying the cursor or identifier to retrieve results after a specific point, enabling the retrieval of subsequent pages of data in a large dataset.
            properties (array): Optional array parameter specifying the properties to include in the response for the contacts object.
            propertiesWithHistory (array): Optional array parameter to specify contact properties for which both current and historical values should be returned in the response.
            associations (array): An optional array of associations to retrieve for the contact object, allowing you to fetch related records or activities.
            archived (boolean): Include this boolean query parameter to specify whether to return only archived contacts; defaults to false.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_contact(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Creates a new contact in the CRM system using the provided JSON data and returns a successful creation response.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_contacts_post(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches for contact records in the CRM system based on specified criteria and returns matching contacts.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/contacts/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_read_feedback_submissions(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Reads a batch of feedback submissions by sending a POST request, allowing for optional filtering by archived status, and returns the relevant data in JSON format.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived feedback submissions in the batch read operation, with a default value of false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_feedback_submission_by_id(
        self,
        feedbackSubmissionId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific feedback submission using its ID, with optional parameters to include properties, history, associations, and archived status.

        Args:
            feedbackSubmissionId (string): feedbackSubmissionId
            properties (array): Specifies an array of properties to include in the response for the feedback submission, allowing selective retrieval of specific details.
            propertiesWithHistory (array): A comma-separated list of property names for which to return both current values and full historical changes in the response.
            associations (array): Optional array of associated object types to include with the feedback submission in the response.
            archived (boolean): Include this query parameter to specify whether to retrieve the archived version of the feedback submission; defaults to false if omitted.
            idProperty (string): Optional query parameter to specify the ID property for the feedback submission.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if feedbackSubmissionId is None:
            raise ValueError("Missing required parameter 'feedbackSubmissionId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_feedback_submission_by_id(self, feedbackSubmissionId: str) -> Any:
        """

        Deletes a specific feedback submission identified by the provided `feedbackSubmissionId` from the CRM system.

        Args:
            feedbackSubmissionId (string): feedbackSubmissionId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if feedbackSubmissionId is None:
            raise ValueError("Missing required parameter 'feedbackSubmissionId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_feedback_submission_by_id(
        self,
        feedbackSubmissionId: str,
        properties: dict[str, str],
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates specific fields of a feedback submission by ID using partial modifications with a JSON request body.

        Args:
            feedbackSubmissionId (string): feedbackSubmissionId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): The "idProperty" query parameter specifies the property name used to identify the feedback submission object for partial updates.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if feedbackSubmissionId is None:
            raise ValueError("Missing required parameter 'feedbackSubmissionId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_feedback_submissions(
        self, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges feedback submission records using the POST method, requiring a JSON body and supporting OAuth2 and private apps for authentication.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/merge"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_feedback_submissions_batch(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of feedback submissions by ID using the HubSpot API and returns a status response with a 204 status code upon successful completion.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_feedback_submissions_batch(
        self, inputs: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """

        Creates a batch of feedback submissions using the HubSpot API, allowing for the simultaneous creation of multiple feedback submissions.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_feedback_submissions_batch(
        self, inputs: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """

        Updates multiple feedback submissions in batches using the HubSpot CRM API.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def post_feedback_submissions_gdpr_delete(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Permanently deletes feedback submissions and associated data to comply with GDPR regulations using the provided JSON body.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_feedback_submissions(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of feedback submissions from HubSpot CRM, allowing for optional filtering by limit, pagination, specific properties, property history, associations, and archived status.

        Args:
            limit (integer): Maximum number of feedback submission records to return in the response, defaulting to 10 if not specified.
            after (string): The "after" query parameter is an optional string used as a paging cursor token to retrieve the next page of feedback submissions after a specified record in the GET /crm/v3/objects/feedback_submissions endpoint.
            properties (array): Optional array of properties to include in the response, allowing you to specify which fields of the feedback submissions to retrieve.
            propertiesWithHistory (array): A comma-separated list of properties for which to return both current values and their historical changes in the response.
            associations (array): Associations parameter specifies an array of association names to include in the response for the GET operation at the "/crm/v3/objects/feedback_submissions" path, allowing retrieval of related records.
            archived (boolean): Indicates whether to include archived feedback submissions in the response, defaulting to false.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_feedback_submission(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Searches for feedback submissions using the HubSpot CRM API and returns relevant results.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_feedback_submissions(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches for feedback submissions in HubSpot CRM using the POST method, allowing developers to filter and retrieve specific feedback data.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/feedback_submissions/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def read_batch_objects(
        self,
        objectType: str,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Performs a batch read operation on CRM objects of the specified type, allowing for the retrieval of multiple records in a single request, with optional filtering by archived status.

        Args:
            objectType (string): objectType
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived objects in the batch read operation; defaults to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_object_details(
        self,
        objectType: str,
        objectId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a specific CRM object record by its object type and ID, allowing for optional specification of properties, associations, and other query parameters.

        Args:
            objectType (string): objectType
            objectId (string): objectId
            properties (array): An optional array parameter that specifies the properties to include in the response for the specified CRM object.
            propertiesWithHistory (array): An optional array parameter specifying the properties for which both current and historical values should be returned in the response.
            associations (array): Optional array parameter to filter results by including or excluding specific associations related to the object.
            archived (boolean): Optional boolean query parameter indicating whether to include archived objects in the response.
            idProperty (string): The optional query parameter to specify a custom property name to use as the unique identifier instead of the default object ID.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if objectId is None:
            raise ValueError("Missing required parameter 'objectId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/{objectId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_object_by_id(self, objectType: str, objectId: str) -> Any:
        """

        Deletes a specified CRM object of the given type and ID using the DELETE method.

        Args:
            objectType (string): objectType
            objectId (string): objectId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if objectId is None:
            raise ValueError("Missing required parameter 'objectId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/{objectId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_object_by_id(
        self,
        objectType: str,
        objectId: str,
        properties: dict[str, str],
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates a specific CRM object using the PATCH method by modifying its properties based on the provided JSON body.

        Args:
            objectType (string): objectType
            objectId (string): objectId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Optional query parameter to specify a custom property name to use as the object identifier instead of the default ID.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if objectId is None:
            raise ValueError("Missing required parameter 'objectId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/{objectId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_objects(
        self, objectType: str, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges duplicate records of a specified object type into a single record using the provided JSON body.

        Args:
            objectType (string): objectType
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_batch_objects_by_type(
        self, objectType: str, inputs: list[dict[str, Any]]
    ) -> Any:
        """

        Archives a batch of objects of a specified type in CRM using the POST method, requiring a JSON body and returning a 204 status code upon successful archiving.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/batch/archive"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_create_object_records(
        self, objectType: str, inputs: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """

        Creates multiple records of a specified object type in a CRM system using a single POST request, supporting batch creation and returning a status message based on the outcome.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/batch/create"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_batch_object(
        self, objectType: str, inputs: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """

        Updates multiple records of a specified object type in a CRM system using a batch operation via the POST method.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/batch/update"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def gdpr_delete_object(
        self, objectType: str, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Permanently deletes an object of the specified type from the CRM, adhering to GDPR guidelines for data removal, using the "POST" method with the object type specified in the path and additional details in the request body.

        Args:
            objectType (string): objectType
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_objects_by_type(
        self,
        objectType: str,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of records for a specified CRM object type with optional filtering, pagination, property selection, association inclusion, and archived status.

        Args:
            objectType (string): objectType
            limit (integer): The "limit" parameter specifies the maximum number of objects to return in the response, with a default value of 10.
            after (string): The "after" query parameter is an optional string used for pagination to specify the cursor after which to return the next set of results.
            properties (array): Optional array parameter to specify which properties to include in the response for the GET operation at `/crm/v3/objects/{objectType}`.
            propertiesWithHistory (array): Optional array parameter to specify the properties for which both current and historical values should be returned in the response.
            associations (array): Filter to include specific association types when retrieving objects, provided as an optional array of association type identifiers in the query string.
            archived (boolean): Optional query parameter to filter results by archived status, defaulting to false.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_object_by_type(
        self,
        objectType: str,
        associations: list[dict[str, Any]],
        properties: dict[str, str],
    ) -> dict[str, Any]:
        """

        Creates a new object of the specified type in a CRM system using the provided JSON data, returning a status message upon successful creation.

        Args:
            objectType (string): objectType
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_objects_by_type_post(
        self,
        objectType: str,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches for objects of a specified type within a CRM using the provided JSON payload, filtering by various criteria to return a list of matching objects.

        Args:
            objectType (string): objectType
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/{objectType}/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_video_conferencing_settings_by_app_id(self, appId: str) -> dict[str, Any]:
        """

        Retrieves the video conferencing settings for a specific application identified by the provided appId using the HubSpot API.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/videoconferencing/settings/{appId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_video_conferencing_settings_by_app_id(
        self,
        appId: str,
        createMeetingUrl: str,
        userVerifyUrl: str | None = None,
        fetchAccountsUri: str | None = None,
        updateMeetingUrl: str | None = None,
        deleteMeetingUrl: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates video conferencing settings for a specific application identified by its `appId` using the provided JSON data.

        Args:
            appId (string): appId
            createMeetingUrl (string): The URL that HubSpot will send requests to create a new video conference. Example: 'https://example.com/create-meeting'.
            userVerifyUrl (string): The URL that HubSpot will use to verify that a user exists in the video conference application. Example: 'https://example.com/user-verify'.
            fetchAccountsUri (string): fetchAccountsUri
            updateMeetingUrl (string): The URL that HubSpot will send updates to existing meetings. Typically called when the user changes the topic or times of a meeting. Example: 'https://example.com/update-meeting'.
            deleteMeetingUrl (string): The URL that HubSpot will send notifications of meetings that have been deleted in HubSpot. Example: 'https://example.com/delete-meeting'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            "userVerifyUrl": userVerifyUrl,
            "fetchAccountsUri": fetchAccountsUri,
            "createMeetingUrl": createMeetingUrl,
            "updateMeetingUrl": updateMeetingUrl,
            "deleteMeetingUrl": deleteMeetingUrl,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/videoconferencing/settings/{appId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_video_conf_settings_by_app_id(self, appId: str) -> Any:
        """

        Deletes the video conferencing settings for the specified app identified by the appId.

        Args:
            appId (string): appId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/extensions/videoconferencing/settings/{appId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def batch_read_tickets_post(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves and formats a batch of tickets from HubSpot CRM using a POST request to the "/crm/v3/objects/tickets/batch/read" endpoint.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived tickets in the batch read operation, defaulting to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_ticket_by_id(
        self,
        ticketId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a specific ticket record by ID from the CRM, optionally including specified properties, property history, associations, and archived status.

        Args:
            ticketId (string): ticketId
            properties (array): An optional array parameter specifying the properties to include in the response for the ticket object.
            propertiesWithHistory (array): A query parameter that returns the specified properties of a ticket along with their version history.
            associations (array): An optional array parameter used to specify the types of associations to retrieve for the ticket, such as contacts or companies.
            archived (boolean): Indicates whether to include archived tickets in the response. Defaults to false.
            idProperty (string): Optional string parameter to specify the property that uniquely identifies a ticket in the CRM system.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if ticketId is None:
            raise ValueError("Missing required parameter 'ticketId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/{ticketId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_ticket_by_id(self, ticketId: str) -> Any:
        """

        Deletes a ticket by its ID using the CRM API.

        Args:
            ticketId (string): ticketId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if ticketId is None:
            raise ValueError("Missing required parameter 'ticketId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/{ticketId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_ticket(
        self,
        ticketId: str,
        properties: dict[str, str],
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates an individual ticket by its ID using the HubSpot CRM API, allowing modification of specific fields via a JSON payload.

        Args:
            ticketId (string): ticketId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): The idProperty query parameter specifies the name of the property to use as the unique identifier in the ticket update request; it is optional and of type string.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if ticketId is None:
            raise ValueError("Missing required parameter 'ticketId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/{ticketId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_tickets(
        self, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges two or more tickets into a single ticket in the CRM system using the POST method, allowing for the consolidation of related customer service requests.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_tickets_batch_post(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of tickets by ID using the HubSpot API and returns a status message.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_tickets_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates a batch of tickets in the CRM using the HubSpot API and returns a status message.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_tickets_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates multiple tickets in a single request using the HubSpot CRM API, returning a status message indicating the success or partial success of the operation.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_ticket_gdpr(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Permanently deletes a ticket and associated data in compliance with GDPR guidelines using the POST method.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_tickets(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of tickets from the CRM, allowing for filtering by limit, after cursor, specific properties, properties with history, associations, and archived status.

        Args:
            limit (integer): The "limit" parameter specifies the maximum number of tickets to return in the response, with a default value of 10.
            after (string): The "after" query parameter is an optional string used for pagination to specify the cursor or offset after which to return the next set of ticket results.
            properties (array): Optional query parameter to specify an array of properties to include in the response for the ticket objects, allowing for customization of the returned data.
            propertiesWithHistory (array): Optional array parameter to specify the properties for which both current and historical values should be returned in the response for the ticket object.
            associations (array): An optional array of association types to include related records linked to the ticket in the response.
            archived (boolean): Optional query parameter indicating whether to include archived tickets (true) or only non-archived tickets (false), defaulting to false.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_ticket(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Creates a new ticket object in the CRM using the HubSpot API, allowing for the management of customer service requests.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_tickets_post(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches and filters ticket records within the CRM system based on specified criteria, returning matching ticket results.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/tickets/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_read_line_items_post(
        self,
        propertiesWithHistory: list[str],
        inputs: list[dict[str, Any]],
        properties: list[str],
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a batch of line items by internal ID or unique property values using the HubSpot CRM API.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): A boolean flag indicating whether to include archived line items in the batch read operation, defaulting to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            "propertiesWithHistory": propertiesWithHistory,
            "idProperty": idProperty,
            "inputs": inputs,
            "properties": properties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/batch/read"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_line_item_by_id(
        self,
        lineItemId: str,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a specific line item by its ID from the CRM, optionally including additional properties, associations, and history, using the CRM API with appropriate permissions.

        Args:
            lineItemId (string): lineItemId
            properties (array): Optional array parameter to specify the properties of a line item to be returned in the response.
            propertiesWithHistory (array): A comma-separated list of property names to include their historical values in the response for the specified line item.
            associations (array): An optional query parameter specifying the associations to include in the response when retrieving a line item, represented as an array of association types.
            archived (boolean): Whether to include archived line items in the response; defaults to false when omitted.
            idProperty (string): Optional string parameter to specify the ID property for line items.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if lineItemId is None:
            raise ValueError("Missing required parameter 'lineItemId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/{lineItemId}"
        query_params = {
            k: v
            for k, v in [
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
                ("idProperty", idProperty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_line_item_by_id(self, lineItemId: str) -> Any:
        """

        Deletes a line item from HubSpot CRM using its ID, requiring the "crm.objects.line_items.write" permission.

        Args:
            lineItemId (string): lineItemId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if lineItemId is None:
            raise ValueError("Missing required parameter 'lineItemId'.")
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/{lineItemId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_line_item_by_id(
        self,
        lineItemId: str,
        properties: dict[str, str],
        idProperty: str | None = None,
    ) -> dict[str, Any]:
        """

        Updates properties of a specific line item in the CRM system using a partial JSON patch request.

        Args:
            lineItemId (string): lineItemId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Specifies which property uniquely identifies the line item for the PATCH operation; defaults to a standard ID if not provided.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if lineItemId is None:
            raise ValueError("Missing required parameter 'lineItemId'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/{lineItemId}"
        query_params = {k: v for k, v in [("idProperty", idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def merge_line_items_post(
        self, objectIdToMerge: str, primaryObjectId: str
    ) -> dict[str, Any]:
        """

        Merges duplicate line items into a single instance using the specified parameters via the POST method.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            "objectIdToMerge": objectIdToMerge,
            "primaryObjectId": primaryObjectId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/merge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_line_items_batch_post(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of line items by their IDs in the CRM using a POST request.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_line_items_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates a batch of line items using the HubSpot API and returns a status message upon successful creation.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_update_line_items(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates a batch of line items using their internal IDs or unique property values via the POST method, requiring authentication with the "crm.objects.line_items.write" scope.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {"inputs": inputs}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def gdpr_delete_line_items(
        self, objectId: str, idProperty: str | None = None
    ) -> Any:
        """

        Deletes line item records from the CRM to comply with GDPR requirements, using the POST method with OAuth2 or private app authentication.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {"idProperty": idProperty, "objectId": objectId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/gdpr-delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_line_items(
        self,
        limit: int | None = None,
        after: str | None = None,
        properties: list[str] | None = None,
        propertiesWithHistory: list[str] | None = None,
        associations: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a paginated list of line items with optional filters for properties, associations, and archival status in the CRM.

        Args:
            limit (integer): The "limit" parameter specifies the maximum number of line items to return in a response, with a default value of 10.
            after (string): The "after" query parameter is used for pagination to retrieve the next page of line items after the specified cursor or ID.
            properties (array): Optional array of properties to include in the response for line items; specify the properties you want to retrieve.
            propertiesWithHistory (array): Specifies an array of properties to include in the response with their historical values for line items.
            associations (array): A list of associations to include in the response for line items, allowing for retrieval of related objects.
            archived (boolean): Optional boolean parameter indicating whether to include archived line items in the response.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("after", after),
                ("properties", properties),
                ("propertiesWithHistory", propertiesWithHistory),
                ("associations", associations),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_line_item(
        self, associations: list[dict[str, Any]], properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Creates a new line item in HubSpot CRM using the POST method, allowing you to add products or services to deals and quotes.

        Args:
            associations (array): associations Example: [{'to': {'id': '101X'}, 'types': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 2}]}].
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"associations": associations, "properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_line_items(
        self,
        limit: int,
        after: str,
        sorts: list[str],
        properties: list[str],
        filterGroups: list[dict[str, Any]],
        query: str | None = None,
    ) -> dict[str, Any]:
        """

        Searches and retrieves line items and their associated properties in the CRM based on specified filter criteria.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "properties": properties,
            "filterGroups": filterGroups,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/crm/v3/objects/line_items/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_crm_imports(
        self,
        after: str | None = None,
        before: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of CRM import operations using the HubSpot API, allowing optional filtering by date and limit on the number of results returned.

        Args:
            after (string): Optional string parameter used to specify the cursor for pagination, allowing retrieval of the next page of results.
            before (string): The "before" query parameter specifies a cutoff point to filter and return only imports created before the given timestamp or identifier.
            limit (integer): Specifies the maximum number of items to return in the response for the import data.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        url = f"{self.main_app_client.base_url}/crm/v3/imports"
        query_params = {
            k: v
            for k, v in [("after", after), ("before", before), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_crm_import(
        self, files: bytes | None = None, importRequest: str | None = None
    ) -> dict[str, Any]:
        """

        Imports data into a HubSpot CRM using a POST request with a multipart/form-data payload, allowing bulk creation or update of records via uploaded files such as CSV or Excel.

        Args:
            files (file (e.g., open('path/to/file', 'rb'))): A list of files containing the data to import
            importRequest (string): JSON formatted metadata about the import. This includes a name for the import and the column mappings for each file. See the overview tab for more on the required format.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Core
        """
        request_body_data = None
        files_data = None
        request_body_data = {}
        files_data = {}
        if files is not None:
            files_data["files"] = files
        if importRequest is not None:
            request_body_data["importRequest"] = importRequest
        files_data = {k: v for k, v in files_data.items() if v is not None}
        if not files_data:
            files_data = None
        url = f"{self.main_app_client.base_url}/crm/v3/imports"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            files=files_data,
            params=query_params,
            content_type="multipart/form-data",
        )
        return self._handle_response(response)

    def get_owners_list(
        self,
        email: str | None = None,
        after: str | None = None,
        limit: int | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of CRM owners using the "GET" method, allowing optional filtering by email, pagination, and archived status, and returns a response with owner details.

        Args:
            email (string): An optional string parameter used to filter owners by their email address in the GET operation at the "/crm/v3/owners" path.
            after (string): **after**: Specifies a cursor for pagination, allowing retrieval of records that appear after the specified value in the result set.
            limit (integer): Specifies the maximum number of results to return in the response, with a default value of 100.
            archived (boolean): A boolean query parameter indicating whether to include archived owners in the response.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Owners
        """
        url = f"{self.main_app_client.base_url}/crm/v3/owners"
        query_params = {
            k: v
            for k, v in [
                ("email", email),
                ("after", after),
                ("limit", limit),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_association_types_by_object_types(
        self, fromObjectType: str, toObjectType: str
    ) -> dict[str, Any]:
        """

        Retrieves the association types between two specified object types in HubSpot CRM using the "GET" method.

        Args:
            fromObjectType (string): fromObjectType
            toObjectType (string): toObjectType

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Types
        """
        if fromObjectType is None:
            raise ValueError("Missing required parameter 'fromObjectType'.")
        if toObjectType is None:
            raise ValueError("Missing required parameter 'toObjectType'.")
        url = f"{self.main_app_client.base_url}/crm/v3/associations/{fromObjectType}/{toObjectType}/types"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.batch_read_emails,
            self.get_email_by_id,
            self.delete_email_by_id,
            self.update_email_by_id,
            self.merge_emails_post,
            self.archive_emails_batch,
            self.create_emails_batch_post,
            self.update_emails_batch,
            self.delete_email_gdpr_data,
            self.list_emails_with_filters,
            self.create_email,
            self.search_emails_post,
            self.batch_read_products_post,
            self.get_product_by_id,
            self.delete_product_by_id,
            self.patch_product_by_id,
            self.merge_products,
            self.archive_products_batch_post,
            self.create_products_batch,
            self.update_products_batch,
            self.delete_product_gdpr_data,
            self.list_products,
            self.create_product,
            self.search_products,
            self.get_pipeline_by_id_for_type,
            self.update_pipeline,
            self.delete_pipeline_by_id_and_type,
            self.patch_pipeline_by_object_type,
            self.get_pipeline_audit_by_object_type,
            self.get_pipeline_stages_by_object_type,
            self.create_pipeline_stage,
            self.list_pipelines_by_type,
            self.create_pipeline_by_object_type,
            self.get_pipeline_stage_by_id,
            self.update_pipeline_stage_by_id,
            self.delete_pipeline_stage_by_id,
            self.update_pipeline_stage,
            self.batch_read_companies_post,
            self.get_company_by_id,
            self.delete_company_by_id,
            self.patch_company_by_id,
            self.merge_companies_post,
            self.archive_companies_batch_post,
            self.create_companies_batch,
            self.update_companies_batch,
            self.delete_company_gdpr_data,
            self.get_companies,
            self.create_company,
            self.search_companies_post,
            self.get_calling_app_settings,
            self.update_calling_app_settings,
            self.delete_calling_app_settings_by_id,
            self.update_calling_settings,
            self.get_calling_app_recording_settings,
            self.post_calling_app_recording_settings,
            self.update_recording_settings,
            self.read_quotes_batch,
            self.get_quote_by_id,
            self.delete_quote_by_id,
            self.update_quote,
            self.merge_quotes,
            self.archive_quotes_batch,
            self.create_quote_batch,
            self.update_quotes_batch,
            self.delete_quote_gdpr_data,
            self.get_quotes,
            self.create_quote,
            self.search_quotes,
            self.batch_read_deals_post,
            self.get_deal_by_id,
            self.delete_deal_by_id,
            self.update_deal_by_id,
            self.merge_deals,
            self.archive_deals_batch_post,
            self.create_deals_batch,
            self.batch_update_deals,
            self.post_deal_gdpr_delete,
            self.list_deals,
            self.create_deal,
            self.search_deals,
            self.cancel_import_by_id,
            self.get_import_by_id,
            self.get_import_errors_by_id,
            self.get_schema_by_object_type,
            self.delete_schema_by_type,
            self.patch_crm_schema_by_object_type,
            self.create_object_type_association,
            self.delete_schema_object_type_purge,
            self.delete_association_by_object_type_id,
            self.list_schemas,
            self.create_crm_schema,
            self.archive_properties_batch_post,
            self.get_property_group,
            self.remove_property_group,
            self.update_property_group_by_identifier,
            self.get_crm_property,
            self.delete_property_by_object_type,
            self.patch_crm_property_by_name,
            self.batch_read_properties_by_object_type,
            self.create_batch_properties,
            self.get_properties_by_object_type,
            self.create_property_schema,
            self.get_property_groups_by_object_type,
            self.create_property_group,
            self.get_owner_by_id,
            self.batch_create_timeline_events,
            self.get_timeline_event_template_by_id,
            self.update_timeline_event_template_by_id,
            self.delete_event_template_by_id,
            self.create_event,
            self.create_token_template,
            self.update_event_template_token,
            self.delete_timeline_event_template_token,
            self.get_timeline_event_detail_by_id,
            self.get_timeline_event_by_id,
            self.get_timeline_event_templates_by_app_id,
            self.create_timeline_event_template,
            self.get_timeline_event_render,
            self.batch_read_contacts_post,
            self.get_contact_by_id,
            self.delete_contact_by_id,
            self.update_contact_by_id,
            self.merge_contacts,
            self.archive_contacts_batch_post,
            self.create_contacts_batch,
            self.batch_update_contacts,
            self.delete_contact_gdpr_data,
            self.get_contacts,
            self.create_contact,
            self.search_contacts_post,
            self.batch_read_feedback_submissions,
            self.get_feedback_submission_by_id,
            self.delete_feedback_submission_by_id,
            self.patch_feedback_submission_by_id,
            self.merge_feedback_submissions,
            self.archive_feedback_submissions_batch,
            self.create_feedback_submissions_batch,
            self.update_feedback_submissions_batch,
            self.post_feedback_submissions_gdpr_delete,
            self.get_feedback_submissions,
            self.create_feedback_submission,
            self.search_feedback_submissions,
            self.read_batch_objects,
            self.get_object_details,
            self.delete_object_by_id,
            self.patch_object_by_id,
            self.merge_objects,
            self.archive_batch_objects_by_type,
            self.batch_create_object_records,
            self.update_batch_object,
            self.gdpr_delete_object,
            self.list_objects_by_type,
            self.create_object_by_type,
            self.search_objects_by_type_post,
            self.get_video_conferencing_settings_by_app_id,
            self.update_video_conferencing_settings_by_app_id,
            self.delete_video_conf_settings_by_app_id,
            self.batch_read_tickets_post,
            self.get_ticket_by_id,
            self.delete_ticket_by_id,
            self.update_ticket,
            self.merge_tickets,
            self.archive_tickets_batch_post,
            self.create_tickets_batch,
            self.update_tickets_batch,
            self.delete_ticket_gdpr,
            self.get_tickets,
            self.create_ticket,
            self.search_tickets_post,
            self.batch_read_line_items_post,
            self.get_line_item_by_id,
            self.delete_line_item_by_id,
            self.patch_line_item_by_id,
            self.merge_line_items_post,
            self.archive_line_items_batch_post,
            self.create_line_items_batch,
            self.batch_update_line_items,
            self.gdpr_delete_line_items,
            self.list_line_items,
            self.create_line_item,
            self.search_line_items,
            self.get_crm_imports,
            self.create_crm_import,
            self.get_owners_list,
            self.get_association_types_by_object_types,
        ]
