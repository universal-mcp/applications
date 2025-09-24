from typing import Any

from .api_segment_base import APISegmentBase


class MarketingApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def get_marketing_campaigns(
        self,
        sort: str | None = None,
        after: str | None = None,
        limit: int | None = None,
        name: str | None = None,
        properties: list[str] | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of marketing campaigns with optional filtering by name, sorting, and limiting results.

        Args:
            sort (string): Optional query parameter to specify sorting criteria for the returned campaigns, allowing sorting by one or more fields in ascending or descending order.
            after (string): Optional parameter to specify a string value for filtering campaigns that occur after a certain point in time.
            limit (integer): The maximum number of campaign records to return in the response.
            name (string): Optional string parameter to filter campaigns by name.
            properties (array): An optional array of campaign property names to include in the response for filtering or detailed retrieval.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Search
        """
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns"
        query_params = {
            k: v
            for k, v in [
                ("sort", sort),
                ("after", after),
                ("limit", limit),
                ("name", name),
                ("properties", properties),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_marketing_campaigns(self, properties: dict[str, str]) -> dict[str, Any]:
        """

        Creates a new marketing campaign using the provided JSON data and returns a status message upon successful creation.

        Args:
            properties (object): properties

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def batch_read_campaigns_post(
        self,
        inputs: list[dict[str, Any]],
        startDate: str | None = None,
        endDate: str | None = None,
        properties: list[str] | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a batch of campaign data from the marketing API, filtering by optional start and end dates and specifying properties to include, using JSON-formatted request body.

        Args:
            inputs (array): inputs
            startDate (string): Optional string parameter to specify the start date for filtering campaigns in the batch read operation.
            endDate (string): Optional query parameter specifying the end date to filter campaigns up to that date in string format.
            properties (array): Optional array of properties to include in the response for the batch read operation.

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
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/batch/read"
        query_params = {
            k: v
            for k, v in [
                ("startDate", startDate),
                ("endDate", endDate),
                ("properties", properties),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_campaigns_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Updates multiple marketing campaigns in a batch using the POST method, requiring a JSON body and authentication via OAuth2 or private apps with "marketing.campaigns.read" permissions.

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
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/batch/update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_campaign_metrics(
        self,
        campaignGuid: str,
        startDate: str | None = None,
        endDate: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves campaign metrics for a specified campaign GUID, optionally filtering by start and end dates.

        Args:
            campaignGuid (string): campaignGuid
            startDate (string): The optional startDate query parameter specifies the beginning date for retrieving campaign metrics in the report.
            endDate (string): Optional date parameter specifying the end date for fetching campaign metrics, formatted as a string.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/metrics"
        query_params = {
            k: v
            for k, v in [("startDate", startDate), ("endDate", endDate)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_campaign_asset_by_type(
        self,
        campaignGuid: str,
        assetType: str,
        after: str | None = None,
        limit: str | None = None,
        startDate: str | None = None,
        endDate: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves assets of a specified type for a given marketing campaign, supporting optional filtering by date range and pagination.

        Args:
            campaignGuid (string): campaignGuid
            assetType (string): assetType
            after (string): An optional string parameter used to specify a cursor for pagination, indicating the starting point for retrieving assets after a specific position.
            limit (string): Optional string parameter to specify the maximum number of items to return in the response.
            startDate (string): Optional start date filter for retrieving campaign assets, specified in string format.
            endDate (string): Optional date string to specify the end date for filtering campaign assets.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Asset
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if assetType is None:
            raise ValueError("Missing required parameter 'assetType'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}"
        query_params = {
            k: v
            for k, v in [
                ("after", after),
                ("limit", limit),
                ("startDate", startDate),
                ("endDate", endDate),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def archive_campaigns_batch(self, inputs: list[dict[str, Any]]) -> Any:
        """

        Archives a batch of marketing campaigns using the HubSpot API, requiring a JSON request body and returning a 204 status upon successful completion.

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
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/batch/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_campaign_asset(
        self, campaignGuid: str, assetType: str, assetId: str
    ) -> Any:
        """

        Updates a specific asset of a given type within a marketing campaign identified by campaignGuid.

        Args:
            campaignGuid (string): campaignGuid
            assetType (string): assetType
            assetId (string): assetId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Asset
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if assetType is None:
            raise ValueError("Missing required parameter 'assetType'.")
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_campaign_asset_by_id(
        self, campaignGuid: str, assetType: str, assetId: str
    ) -> Any:
        """

        Deletes a specific asset from a marketing campaign using the provided campaign GUID, asset type, and asset ID.

        Args:
            campaignGuid (string): campaignGuid
            assetType (string): assetType
            assetId (string): assetId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Asset
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if assetType is None:
            raise ValueError("Missing required parameter 'assetType'.")
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def get_campaign_revenue_report(
        self,
        campaignGuid: str,
        attributionModel: str | None = None,
        startDate: str | None = None,
        endDate: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves revenue reports for a specific marketing campaign using the provided campaign GUID, with optional filtering by attribution model and date range.

        Args:
            campaignGuid (string): campaignGuid
            attributionModel (string): Specifies the attribution model to use for calculating revenue in the report, determining which marketing channels or touchpoints receive credit for conversions.
            startDate (string): The startDate query parameter specifies the optional beginning date to filter the revenue report data for the campaign.
            endDate (string): The endDate query parameter specifies the optional end date to filter the revenue report data for the campaign.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/revenue"
        query_params = {
            k: v
            for k, v in [
                ("attributionModel", attributionModel),
                ("startDate", startDate),
                ("endDate", endDate),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_campaigns_batch(self, inputs: list[dict[str, Any]]) -> dict[str, Any]:
        """

        Creates multiple marketing campaigns in a single operation using the "POST" method, accepting a JSON body with campaign details and returning a status message upon successful creation.

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
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/batch/create"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_campaign_budget_totals(self, campaignGuid: str) -> dict[str, Any]:
        """

        Retrieves the total budget details for a marketing campaign using the campaign's GUID.

        Args:
            campaignGuid (string): campaignGuid

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Budget
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/budget/totals"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_campaign_by_guid(
        self,
        campaignGuid: str,
        startDate: str | None = None,
        endDate: str | None = None,
        properties: list[str] | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific marketing campaign identified by its campaignGuid, optionally filtered by date range and selected properties.

        Args:
            campaignGuid (string): campaignGuid
            startDate (string): The optional startDate query parameter specifies the beginning date to filter campaign data for the GET /marketing/v3/campaigns/{campaignGuid} operation.
            endDate (string): Optional date parameter to filter campaigns by end date, specified in ISO 8601 format.
            properties (array): Optional array of properties to include in the response for the specified campaign.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}"
        query_params = {
            k: v
            for k, v in [
                ("startDate", startDate),
                ("endDate", endDate),
                ("properties", properties),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_campaign_by_guid(self, campaignGuid: str) -> Any:
        """

        Deletes a marketing campaign using the provided campaign GUID and returns a 204 No Content response.

        Args:
            campaignGuid (string): campaignGuid

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_campaign_by_guid(
        self, campaignGuid: str, properties: dict[str, str]
    ) -> dict[str, Any]:
        """

        Updates specified properties of a marketing campaign identified by the campaignGuid using a JSON patch document.

        Args:
            campaignGuid (string): campaignGuid
            properties (object): properties

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        request_body_data = None
        request_body_data = {"properties": properties}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def get_campaign_contacts_report_by_type(
        self,
        campaignGuid: str,
        contactType: str,
        startDate: str | None = None,
        endDate: str | None = None,
        limit: int | None = None,
        after: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a report of contacts of a specified type for a marketing campaign, allowing optional filtering by start and end dates and pagination.

        Args:
            campaignGuid (string): campaignGuid
            contactType (string): contactType
            startDate (string): Optional query parameter specifying the start date for filtering reports in the format of a string, allowing users to narrow down the data based on a specific date range.
            endDate (string): Optional query parameter to specify the end date for filtering the campaign contact report data.
            limit (integer): The "limit" parameter, an optional integer, specifies the maximum number of records to return in the response for the contacts report.
            after (string): Optional string parameter to specify a filter for retrieving contacts after a specific date or identifier.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if contactType is None:
            raise ValueError("Missing required parameter 'contactType'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/contacts/{contactType}"
        query_params = {
            k: v
            for k, v in [
                ("startDate", startDate),
                ("endDate", endDate),
                ("limit", limit),
                ("after", after),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_email_statistics(
        self,
        startTimestamp: str | None = None,
        endTimestamp: str | None = None,
        emailIds: list[int] | None = None,
        property: str | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves email statistics for a specified time range and optional email IDs and properties using the GET method.

        Args:
            startTimestamp (string): Optional query parameter to specify the start timestamp for filtering email statistics.
            endTimestamp (string): Optional end timestamp in string format to filter email statistics up to a specific point in time.
            emailIds (array): Optional array of email IDs to filter statistics; allows retrieving specific email campaign statistics.
            property (string): An optional string parameter used in the query to specify additional properties for filtering or customizing the email statistics list.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Statistics
        """
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/statistics/list"
        query_params = {
            k: v
            for k, v in [
                ("startTimestamp", startTimestamp),
                ("endTimestamp", endTimestamp),
                ("emailIds", emailIds),
                ("property", property),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_ab_test_email_variation(
        self, variationName: str, contentId: str
    ) -> dict[str, Any]:
        """

        Creates a variation for an A/B test email using the POST method and returns a successful creation status.

        Args:
            variationName (string): variationName
            contentId (string): ID of the object to test. Example: '7'.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_VNext_Emails
        """
        request_body_data = None
        request_body_data = {"variationName": variationName, "contentId": contentId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/ab-test/create-variation"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_email_statistics_histogram(
        self,
        interval: str | None = None,
        startTimestamp: str | None = None,
        endTimestamp: str | None = None,
        emailIds: list[int] | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves histogram statistics for marketing emails filtered by optional parameters such as interval, time range, and specific email IDs.

        Args:
            interval (string): The "interval" parameter specifies the time interval for dividing email statistics into buckets, with options including YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, QUARTER_HOUR, MINUTE, and SECOND.
            startTimestamp (string): The optional query parameter specifying the start timestamp to filter email statistics in the histogram data.
            endTimestamp (string): Optional end timestamp for the histogram data, specified as a string.
            emailIds (array): Optional query parameter to specify one or more email IDs for which to retrieve histogram statistics.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Statistics
        """
        url = (
            f"{self.main_app_client.base_url}/marketing/v3/emails/statistics/histogram"
        )
        query_params = {
            k: v
            for k, v in [
                ("interval", interval),
                ("startTimestamp", startTimestamp),
                ("endTimestamp", endTimestamp),
                ("emailIds", emailIds),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_email_ab_test_variation(self, emailId: str) -> dict[str, Any]:
        """

        Retrieves the variation for an A/B test associated with a specific email by its ID using the GET method.

        Args:
            emailId (string): emailId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/ab-test/get-variation"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def reset_email_draft_by_id(self, emailId: str) -> Any:
        """

        Resets the draft status of an email using the specified email ID.

        Args:
            emailId (string): emailId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        url = (
            f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/draft/reset"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_email_revision_to_draft(
        self, emailId: str, revisionId: str
    ) -> dict[str, Any]:
        """

        Restores a specified email revision to draft status by email ID and revision ID.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_email_draft_by_id(self, emailId: str) -> dict[str, Any]:
        """

        Retrieves the draft of an email with the specified `{emailId}` using the marketing API.

        Args:
            emailId (string): emailId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/draft"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_email_draft_by_id(
        self,
        emailId: str,
        rssData: dict[str, Any] | None = None,
        subject: str | None = None,
        testing: dict[str, Any] | None = None,
        publishDate: str | None = None,
        language: str | None = None,
        businessUnitId: str | None = None,
        content: dict[str, Any] | None = None,
        webversion: dict[str, Any] | None = None,
        archived: bool | None = None,
        subscriptionDetails: dict[str, Any] | None = None,
        activeDomain: str | None = None,
        name: str | None = None,
        campaign: str | None = None,
        from_: dict[str, Any] | None = None,
        state: str | None = None,
        to: dict[str, Any] | None = None,
        subcategory: str | None = None,
        sendOnPublish: bool | None = None,
    ) -> dict[str, Any]:
        """

                Updates a draft email identified by the specified emailId using the provided JSON data.

                Args:
                    emailId (string): emailId
                    rssData (object): RSS related data if it is a blog or rss email.
                    subject (string): The subject of the email. Example: 'My subject'.
                    testing (object): AB testing related data. This property is only returned for AB type emails.
                    publishDate (string): The date and time the email is scheduled for, in ISO8601 representation. This is only used in local time or scheduled emails. Example: '2023-11-30T18:44:20.387Z'.
                    language (string): language
                    businessUnitId (string): businessUnitId
                    content (object): Data structure representing the content of the email. Example: {'flexAreas': {'main': {'boxed': False, 'isSingleColumnFullWidth': False, 'sections': [{'columns': [{'id': 'column_1606761806181_0', 'widgets': ['module_160676180617911'], 'width': 12}], 'id': 'section_1606761806181', 'style': {'backgroundColor': '', 'backgroundType': 'CONTENT'}}, {'columns': [{'id': 'column-0-1', 'widgets': ['module-0-1-1'], 'width': 12}], 'id': 'section-0', 'style': {'backgroundType': 'CONTENT', 'paddingBottom': '40px', 'paddingTop': '40px'}}, {'columns': [{'id': 'column-1-1', 'widgets': ['module-1-1-1'], 'width': 12}], 'id': 'section-1', 'style': {'backgroundColor': '', 'backgroundType': 'CONTENT', 'paddingBottom': '0px', 'paddingTop': '0px'}}]}}, 'plainTextVersion': 'This is custom! View in browser ({{view_as_page_url}})

        Hello {{ contact.firstname }},

        Plain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.

        Every email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.

        Link text

        Now it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.

        All the best,

        Your full name

        Your job title

        Other contact information

        {{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}

        Unsubscribe ({{unsubscribe_link_all}})

        Manage preferences ({{unsubscribe_link}})', 'styleSettings': {}, 'widgets': {'module-0-1-1': {'body': {'css_class': 'dnd-module', 'html': '<p style="margin-bottom:10px;">Hello {{ contact.firstname }},<br><br>Plain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.</p><p style="margin-bottom:10px;">Every email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.</p><p style="margin-bottom:10px;"><a target="_blank" rel="noopener">Link text</a></p><p style="margin-bottom:10px;">Now it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.</p><p style="margin-bottom:10px;">All the best,<br>Your full name<br>Your job title<br>Other contact information</p>', 'i18nKey': 'richText.plainText', 'path': '@hubspot/rich_text', 'schema_version': 2}, 'child_css': {}, 'css': {}, 'id': 'module-0-1-1', 'module_id': 1155639, 'name': 'module-0-1-1', 'order': 2, 'styles': {}, 'type': 'module'}, 'module-1-1-1': {'body': {'align': 'center', 'css_class': 'dnd-module', 'font': {'color': '#23496d', 'font': 'Arial, sans-serif', 'size': {'units': 'px', 'value': 12}}, 'link_font': {'color': '#00a4bd', 'font': 'Helvetica,Arial,sans-serif', 'size': {'units': 'px', 'value': 12}, 'styles': {'bold': False, 'italic': False, 'underline': True}}, 'path': '@hubspot/email_footer', 'schema_version': 2, 'unsubscribe_link_type': 'both'}, 'child_css': {}, 'css': {}, 'id': 'module-1-1-1', 'module_id': 2869621, 'name': 'module-1-1-1', 'order': 3, 'styles': {}, 'type': 'module'}, 'module_160676180617911': {'body': {'font': {'color': '#00a4bd', 'font': 'Arial, sans-serif', 'size': {'units': 'px', 'value': 12}, 'styles': {'bold': False, 'italic': False, 'underline': True}}, 'hs_enable_module_padding': False, 'hs_wrapper_css': {}}, 'child_css': {}, 'css': {}, 'id': 'module_160676180617911', 'module_id': 2794854, 'name': 'module_160676180617911', 'styles': {}, 'type': 'module'}, 'preview_text': {'body': {'value': ''}, 'child_css': {}, 'css': {}, 'id': 'preview_text', 'label': 'Preview Text <span class=help-text>This will be used as the preview text that displays in some email clients</span>', 'name': 'preview_text', 'order': 0, 'styles': {}, 'type': 'text'}}}.
                    webversion (object): webversion Example: {'expiresAt': '2020-11-30T18:44:20.387Z', 'metaDescription': '', 'redirectToPageId': 0, 'redirectToUrl': 'http://www.example.org'}.
                    archived (boolean): Determines if the email is archived or not. Example: False.
                    subscriptionDetails (object): Data structure representing the subscription fields of the email. Example: {'officeLocationId': '5449392956'}.
                    activeDomain (string): The active domain of the email. Example: 'test.hs-sites.com'.
                    name (string): The name of the email, as displayed on the email dashboard. Example: 'My subject'.
                    campaign (string): The ID of the campaign this email is associated to. Example: '1b7f51a6-33c1-44d6-ba28-fe81f655dced'.
                    from_ (object): Data structure representing the from fields on the email. Example: {'fromName': 'Bruce Wayne', 'replyTo': 'test@hubspot.com'}.
                    state (string): The email state. Example: 'DRAFT'.
                    to (object): Data structure representing the to fields of the email. Example: {'contactIds': {}, 'contactLists': {'exclude': [1], 'include': [5]}, 'suppressGraymail': True}.
                    subcategory (string): The email subcategory. Example: 'batch'.
                    sendOnPublish (boolean): Determines whether the email will be sent immediately on publish. Example: True.

                Returns:
                    dict[str, Any]: successful operation

                Raises:
                    HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

                Tags:
                    Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        request_body_data = {
            "rssData": rssData,
            "subject": subject,
            "testing": testing,
            "publishDate": publishDate,
            "language": language,
            "businessUnitId": businessUnitId,
            "content": content,
            "webversion": webversion,
            "archived": archived,
            "subscriptionDetails": subscriptionDetails,
            "activeDomain": activeDomain,
            "name": name,
            "campaign": campaign,
            "from": from_,
            "state": state,
            "to": to,
            "subcategory": subcategory,
            "sendOnPublish": sendOnPublish,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/draft"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def get_email_revisions(
        self,
        emailId: str,
        after: str | None = None,
        before: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """

        Get a list of revisions for a specified marketing email, optionally filtered by date range and limited in number.

        Args:
            emailId (string): emailId
            after (string): The "after" query parameter specifies a cursor or token to retrieve email revisions created after a certain point, enabling pagination of results.
            before (string): Filter the email revisions to include only those created before the specified timestamp or identifier.
            limit (integer): The "limit" parameter specifies the maximum number of revisions to return in the response when retrieving revisions for a specific email.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/revisions"
        query_params = {
            k: v
            for k, v in [("after", after), ("before", before), ("limit", limit)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_email_revision_by_id(self, emailId: str, revisionId: str) -> dict[str, Any]:
        """

        Retrieves a specific revision of an email identified by the provided email ID and revision ID using the GET method.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def clone_email(self, id: str, cloneName: str | None = None) -> dict[str, Any]:
        """

        Clones a marketing email using the POST method at the "/marketing/v3/emails/clone" endpoint, creating a duplicate email with the same properties as the original but with a unique ID.

        Args:
            id (string): ID of the email to be cloned.
            cloneName (string): Name of the cloned email.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Public_VNext_Emails
        """
        request_body_data = None
        request_body_data = {"cloneName": cloneName, "id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/clone"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_marketing_emails(
        self,
        createdAt: str | None = None,
        createdAfter: str | None = None,
        createdBefore: str | None = None,
        updatedAt: str | None = None,
        updatedAfter: str | None = None,
        updatedBefore: str | None = None,
        sort: list[str] | None = None,
        after: str | None = None,
        limit: int | None = None,
        includeStats: bool | None = None,
        type: str | None = None,
        isPublished: bool | None = None,
        includedProperties: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of marketing emails with optional filtering, sorting, pagination, and inclusion of statistics.

        Args:
            createdAt (string): Optional query parameter specifying the creation date of emails to filter results, formatted as a string.
            createdAfter (string): Filter emails created after a specific date and time, specified in ISO 8601 format.
            createdBefore (string): Filter results to include only emails created before the specified date and time.
            updatedAt (string): Filter emails to include only those updated at or after the specified date and time.
            updatedAfter (string): Filter emails to include only those updated after the specified date and time.
            updatedBefore (string): Optional query parameter to filter emails updated before a specified date and time.
            sort (array): Specifies an array of fields to sort the email results by, allowing clients to customize the order of returned data.
            after (string): Optional string parameter to filter emails by retrieving only those sent after the specified date or time.
            limit (integer): Specifies the maximum number of email records to return in the response.
            includeStats (boolean): Indicates whether to include email statistics in the response; defaults to false if not specified.
            type (string): Optional query parameter to filter emails by type, with possible values including various email categories such as AB_EMAIL, BATCH_EMAIL, and others.
            isPublished (boolean): Indicates whether to include only published emails in the response; accepts boolean values (true or false).
            includedProperties (array): Optional array parameter to specify additional properties to include in the response for the GET operation at "/marketing/v3/emails/".
            archived (boolean): Filter emails by their archived status; set to true to return only archived emails, or false to exclude archived emails.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/"
        query_params = {
            k: v
            for k, v in [
                ("createdAt", createdAt),
                ("createdAfter", createdAfter),
                ("createdBefore", createdBefore),
                ("updatedAt", updatedAt),
                ("updatedAfter", updatedAfter),
                ("updatedBefore", updatedBefore),
                ("sort", sort),
                ("after", after),
                ("limit", limit),
                ("includeStats", includeStats),
                ("type", type),
                ("isPublished", isPublished),
                ("includedProperties", includedProperties),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_email_marketing_campaign(
        self,
        name: str,
        feedbackSurveyId: str | None = None,
        rssData: dict[str, Any] | None = None,
        subject: str | None = None,
        testing: dict[str, Any] | None = None,
        publishDate: str | None = None,
        language: str | None = None,
        businessUnitId: str | None = None,
        content: dict[str, Any] | None = None,
        webversion: dict[str, Any] | None = None,
        archived: bool | None = None,
        subscriptionDetails: dict[str, Any] | None = None,
        activeDomain: str | None = None,
        campaign: str | None = None,
        from_: dict[str, Any] | None = None,
        state: str | None = None,
        to: dict[str, Any] | None = None,
        subcategory: str | None = None,
        sendOnPublish: bool | None = None,
    ) -> dict[str, Any]:
        """

                Creates a new email resource in the marketing system using the provided JSON data and returns a success response upon creation.

                Args:
                    name (string): The name of the email, as displayed on the email dashboard. Example: 'My subject'.
                    feedbackSurveyId (string): The ID of the feedback survey linked to the email.
                    rssData (object): RSS related data if it is a blog or rss email.
                    subject (string): The subject of the email. Example: 'My subject'.
                    testing (object): AB testing related data. This property is only returned for AB type emails.
                    publishDate (string): The date and time the email is scheduled for, in ISO8601 representation. This is only used in local time or scheduled emails. Example: '2023-11-30T18:44:20.387Z'.
                    language (string): language
                    businessUnitId (string): businessUnitId
                    content (object): Data structure representing the content of the email. Example: {'flexAreas': {'main': {'boxed': False, 'isSingleColumnFullWidth': False, 'sections': [{'columns': [{'id': 'column_1606761806181_0', 'widgets': ['module_160676180617911'], 'width': 12}], 'id': 'section_1606761806181', 'style': {'backgroundColor': '', 'backgroundType': 'CONTENT'}}, {'columns': [{'id': 'column-0-1', 'widgets': ['module-0-1-1'], 'width': 12}], 'id': 'section-0', 'style': {'backgroundType': 'CONTENT', 'paddingBottom': '40px', 'paddingTop': '40px'}}, {'columns': [{'id': 'column-1-1', 'widgets': ['module-1-1-1'], 'width': 12}], 'id': 'section-1', 'style': {'backgroundColor': '', 'backgroundType': 'CONTENT', 'paddingBottom': '0px', 'paddingTop': '0px'}}]}}, 'plainTextVersion': 'This is custom! View in browser ({{view_as_page_url}})

        Hello {{ contact.firstname }},

        Plain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.

        Every email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.

        Link text

        Now it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.

        All the best,

        Your full name

        Your job title

        Other contact information

        {{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}

        Unsubscribe ({{unsubscribe_link_all}})

        Manage preferences ({{unsubscribe_link}})', 'styleSettings': {}, 'widgets': {'module-0-1-1': {'body': {'css_class': 'dnd-module', 'html': '<p style="margin-bottom:10px;">Hello {{ contact.firstname }},<br><br>Plain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.</p><p style="margin-bottom:10px;">Every email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.</p><p style="margin-bottom:10px;"><a target="_blank" rel="noopener">Link text</a></p><p style="margin-bottom:10px;">Now it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.</p><p style="margin-bottom:10px;">All the best,<br>Your full name<br>Your job title<br>Other contact information</p>', 'i18nKey': 'richText.plainText', 'path': '@hubspot/rich_text', 'schema_version': 2}, 'child_css': {}, 'css': {}, 'id': 'module-0-1-1', 'module_id': 1155639, 'name': 'module-0-1-1', 'order': 2, 'styles': {}, 'type': 'module'}, 'module-1-1-1': {'body': {'align': 'center', 'css_class': 'dnd-module', 'font': {'color': '#23496d', 'font': 'Arial, sans-serif', 'size': {'units': 'px', 'value': 12}}, 'link_font': {'color': '#00a4bd', 'font': 'Helvetica,Arial,sans-serif', 'size': {'units': 'px', 'value': 12}, 'styles': {'bold': False, 'italic': False, 'underline': True}}, 'path': '@hubspot/email_footer', 'schema_version': 2, 'unsubscribe_link_type': 'both'}, 'child_css': {}, 'css': {}, 'id': 'module-1-1-1', 'module_id': 2869621, 'name': 'module-1-1-1', 'order': 3, 'styles': {}, 'type': 'module'}, 'module_160676180617911': {'body': {'font': {'color': '#00a4bd', 'font': 'Arial, sans-serif', 'size': {'units': 'px', 'value': 12}, 'styles': {'bold': False, 'italic': False, 'underline': True}}, 'hs_enable_module_padding': False, 'hs_wrapper_css': {}}, 'child_css': {}, 'css': {}, 'id': 'module_160676180617911', 'module_id': 2794854, 'name': 'module_160676180617911', 'styles': {}, 'type': 'module'}, 'preview_text': {'body': {'value': ''}, 'child_css': {}, 'css': {}, 'id': 'preview_text', 'label': 'Preview Text <span class=help-text>This will be used as the preview text that displays in some email clients</span>', 'name': 'preview_text', 'order': 0, 'styles': {}, 'type': 'text'}}}.
                    webversion (object): webversion Example: {'expiresAt': '2020-11-30T18:44:20.387Z', 'metaDescription': '', 'redirectToPageId': 0, 'redirectToUrl': 'http://www.example.org'}.
                    archived (boolean): Determines if the email is archived or not. Example: False.
                    subscriptionDetails (object): Data structure representing the subscription fields of the email. Example: {'officeLocationId': '5449392956'}.
                    activeDomain (string): The active domain of the email. Example: 'test.hs-sites.com'.
                    campaign (string): The ID of the campaign this email is associated to. Example: '1b7f51a6-33c1-44d6-ba28-fe81f655dced'.
                    from_ (object): Data structure representing the from fields on the email. Example: {'fromName': 'Bruce Wayne', 'replyTo': 'test@hubspot.com'}.
                    state (string): The email state. Example: 'DRAFT'.
                    to (object): Data structure representing the to fields of the email. Example: {'contactIds': {}, 'contactLists': {'exclude': [1], 'include': [5]}, 'suppressGraymail': True}.
                    subcategory (string): The email subcategory. Example: 'batch'.
                    sendOnPublish (boolean): Determines whether the email will be sent immediately on publish. Example: True.

                Returns:
                    dict[str, Any]: successful operation

                Raises:
                    HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

                Tags:
                    Marketing Emails
        """
        request_body_data = None
        request_body_data = {
            "feedbackSurveyId": feedbackSurveyId,
            "rssData": rssData,
            "subject": subject,
            "testing": testing,
            "publishDate": publishDate,
            "language": language,
            "businessUnitId": businessUnitId,
            "content": content,
            "webversion": webversion,
            "archived": archived,
            "subscriptionDetails": subscriptionDetails,
            "activeDomain": activeDomain,
            "name": name,
            "campaign": campaign,
            "from": from_,
            "state": state,
            "to": to,
            "subcategory": subcategory,
            "sendOnPublish": sendOnPublish,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_email_revision(self, emailId: str, revisionId: str) -> Any:
        """

        Restores a specific email revision using the provided email ID and revision ID via the POST method.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_email_by_id_marketing(
        self,
        emailId: str,
        includeStats: bool | None = None,
        includedProperties: list[str] | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific email by its ID, optionally including statistics, selected properties, and archived status.

        Args:
            emailId (string): emailId
            includeStats (boolean): Optionally includes email statistics in the response when set to true.
            includedProperties (array): An optional array parameter to specify which email properties should be included in the response, allowing customization of the returned data.
            archived (boolean): Optional boolean parameter to indicate whether to include archived emails in the response.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}"
        query_params = {
            k: v
            for k, v in [
                ("includeStats", includeStats),
                ("includedProperties", includedProperties),
                ("archived", archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_email_by_id_marketing(
        self, emailId: str, archived: bool | None = None
    ) -> Any:
        """

        Deletes the specified marketing email by its emailId, optionally archiving it, and returns a 204 No Content status on success.

        Args:
            emailId (string): emailId
            archived (boolean): Optional boolean parameter to indicate whether archived emails should be considered during the deletion operation.

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def patch_email_by_id(
        self,
        emailId: str,
        archived: bool | None = None,
        rssData: dict[str, Any] | None = None,
        subject: str | None = None,
        testing: dict[str, Any] | None = None,
        publishDate: str | None = None,
        language: str | None = None,
        businessUnitId: str | None = None,
        content: dict[str, Any] | None = None,
        webversion: dict[str, Any] | None = None,
        archived_body: bool | None = None,
        subscriptionDetails: dict[str, Any] | None = None,
        activeDomain: str | None = None,
        name: str | None = None,
        campaign: str | None = None,
        from_: dict[str, Any] | None = None,
        state: str | None = None,
        to: dict[str, Any] | None = None,
        subcategory: str | None = None,
        sendOnPublish: bool | None = None,
    ) -> dict[str, Any]:
        """

                Updates an email resource identified by `{emailId}` with partial modifications using JSON in the request body and optionally sets its archived status.

                Args:
                    emailId (string): emailId
                    archived (boolean): Indicates whether the email should be marked as archived, with true meaning archived and false meaning not archived, during the PATCH operation.
                    rssData (object): RSS related data if it is a blog or rss email.
                    subject (string): The subject of the email. Example: 'My subject'.
                    testing (object): AB testing related data. This property is only returned for AB type emails.
                    publishDate (string): The date and time the email is scheduled for, in ISO8601 representation. This is only used in local time or scheduled emails. Example: '2023-11-30T18:44:20.387Z'.
                    language (string): language
                    businessUnitId (string): businessUnitId
                    content (object): Data structure representing the content of the email. Example: {'flexAreas': {'main': {'boxed': False, 'isSingleColumnFullWidth': False, 'sections': [{'columns': [{'id': 'column_1606761806181_0', 'widgets': ['module_160676180617911'], 'width': 12}], 'id': 'section_1606761806181', 'style': {'backgroundColor': '', 'backgroundType': 'CONTENT'}}, {'columns': [{'id': 'column-0-1', 'widgets': ['module-0-1-1'], 'width': 12}], 'id': 'section-0', 'style': {'backgroundType': 'CONTENT', 'paddingBottom': '40px', 'paddingTop': '40px'}}, {'columns': [{'id': 'column-1-1', 'widgets': ['module-1-1-1'], 'width': 12}], 'id': 'section-1', 'style': {'backgroundColor': '', 'backgroundType': 'CONTENT', 'paddingBottom': '0px', 'paddingTop': '0px'}}]}}, 'plainTextVersion': 'This is custom! View in browser ({{view_as_page_url}})

        Hello {{ contact.firstname }},

        Plain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.

        Every email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.

        Link text

        Now it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.

        All the best,

        Your full name

        Your job title

        Other contact information

        {{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}

        Unsubscribe ({{unsubscribe_link_all}})

        Manage preferences ({{unsubscribe_link}})', 'styleSettings': {}, 'widgets': {'module-0-1-1': {'body': {'css_class': 'dnd-module', 'html': '<p style="margin-bottom:10px;">Hello {{ contact.firstname }},<br><br>Plain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.</p><p style="margin-bottom:10px;">Every email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.</p><p style="margin-bottom:10px;"><a target="_blank" rel="noopener">Link text</a></p><p style="margin-bottom:10px;">Now it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.</p><p style="margin-bottom:10px;">All the best,<br>Your full name<br>Your job title<br>Other contact information</p>', 'i18nKey': 'richText.plainText', 'path': '@hubspot/rich_text', 'schema_version': 2}, 'child_css': {}, 'css': {}, 'id': 'module-0-1-1', 'module_id': 1155639, 'name': 'module-0-1-1', 'order': 2, 'styles': {}, 'type': 'module'}, 'module-1-1-1': {'body': {'align': 'center', 'css_class': 'dnd-module', 'font': {'color': '#23496d', 'font': 'Arial, sans-serif', 'size': {'units': 'px', 'value': 12}}, 'link_font': {'color': '#00a4bd', 'font': 'Helvetica,Arial,sans-serif', 'size': {'units': 'px', 'value': 12}, 'styles': {'bold': False, 'italic': False, 'underline': True}}, 'path': '@hubspot/email_footer', 'schema_version': 2, 'unsubscribe_link_type': 'both'}, 'child_css': {}, 'css': {}, 'id': 'module-1-1-1', 'module_id': 2869621, 'name': 'module-1-1-1', 'order': 3, 'styles': {}, 'type': 'module'}, 'module_160676180617911': {'body': {'font': {'color': '#00a4bd', 'font': 'Arial, sans-serif', 'size': {'units': 'px', 'value': 12}, 'styles': {'bold': False, 'italic': False, 'underline': True}}, 'hs_enable_module_padding': False, 'hs_wrapper_css': {}}, 'child_css': {}, 'css': {}, 'id': 'module_160676180617911', 'module_id': 2794854, 'name': 'module_160676180617911', 'styles': {}, 'type': 'module'}, 'preview_text': {'body': {'value': ''}, 'child_css': {}, 'css': {}, 'id': 'preview_text', 'label': 'Preview Text <span class=help-text>This will be used as the preview text that displays in some email clients</span>', 'name': 'preview_text', 'order': 0, 'styles': {}, 'type': 'text'}}}.
                    webversion (object): webversion Example: {'expiresAt': '2020-11-30T18:44:20.387Z', 'metaDescription': '', 'redirectToPageId': 0, 'redirectToUrl': 'http://www.example.org'}.
                    archived_body (boolean): Determines if the email is archived or not. Example: False.
                    subscriptionDetails (object): Data structure representing the subscription fields of the email. Example: {'officeLocationId': '5449392956'}.
                    activeDomain (string): The active domain of the email. Example: 'test.hs-sites.com'.
                    name (string): The name of the email, as displayed on the email dashboard. Example: 'My subject'.
                    campaign (string): The ID of the campaign this email is associated to. Example: '1b7f51a6-33c1-44d6-ba28-fe81f655dced'.
                    from_ (object): Data structure representing the from fields on the email. Example: {'fromName': 'Bruce Wayne', 'replyTo': 'test@hubspot.com'}.
                    state (string): The email state. Example: 'DRAFT'.
                    to (object): Data structure representing the to fields of the email. Example: {'contactIds': {}, 'contactLists': {'exclude': [1], 'include': [5]}, 'suppressGraymail': True}.
                    subcategory (string): The email subcategory. Example: 'batch'.
                    sendOnPublish (boolean): Determines whether the email will be sent immediately on publish. Example: True.

                Returns:
                    dict[str, Any]: successful operation

                Raises:
                    HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

                Tags:
                    Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        request_body_data = {
            "rssData": rssData,
            "subject": subject,
            "testing": testing,
            "publishDate": publishDate,
            "language": language,
            "businessUnitId": businessUnitId,
            "content": content,
            "webversion": webversion,
            "archived": archived_body,
            "subscriptionDetails": subscriptionDetails,
            "activeDomain": activeDomain,
            "name": name,
            "campaign": campaign,
            "from": from_,
            "state": state,
            "to": to,
            "subcategory": subcategory,
            "sendOnPublish": sendOnPublish,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/marketing/v3/emails/{emailId}"
        query_params = {k: v for k, v in [("archived", archived)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.get_marketing_campaigns,
            self.create_marketing_campaigns,
            self.batch_read_campaigns_post,
            self.update_campaigns_batch,
            self.get_campaign_metrics,
            self.get_campaign_asset_by_type,
            self.archive_campaigns_batch,
            self.update_campaign_asset,
            self.delete_campaign_asset_by_id,
            self.get_campaign_revenue_report,
            self.create_campaigns_batch,
            self.get_campaign_budget_totals,
            self.get_campaign_by_guid,
            self.delete_campaign_by_guid,
            self.patch_campaign_by_guid,
            self.get_campaign_contacts_report_by_type,
            self.list_email_statistics,
            self.create_ab_test_email_variation,
            self.get_email_statistics_histogram,
            self.get_email_ab_test_variation,
            self.reset_email_draft_by_id,
            self.restore_email_revision_to_draft,
            self.get_email_draft_by_id,
            self.update_email_draft_by_id,
            self.get_email_revisions,
            self.get_email_revision_by_id,
            self.clone_email,
            self.list_marketing_emails,
            self.create_email_marketing_campaign,
            self.restore_email_revision,
            self.get_email_by_id_marketing,
            self.delete_email_by_id_marketing,
            self.patch_email_by_id,
        ]
