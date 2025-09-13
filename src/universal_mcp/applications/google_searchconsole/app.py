import logging
import urllib.parse
from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

logger = logging.getLogger(__name__)


class GoogleSearchconsoleApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="google_searchconsole", integration=integration, **kwargs)
        self.webmasters_base_url = "https://www.googleapis.com/webmasters/v3"
        self.searchconsole_base_url = "https://searchconsole.googleapis.com/v1"

    def delete_sitemap(self, siteUrl: str, feedpath: str) -> None:
        """
        Deletes a sitemap from a specified Google Search Console property. It targets the sitemap using the site's URL and the sitemap's `feedpath`, then issues an HTTP DELETE request. This action is distinct from `delete_site`, which removes the entire property, not just a sitemap.
        
        Args:
            siteUrl (str): The site's URL, including protocol (e.g. 'http://www.example.com/').
            feedpath (str): The URL of the sitemap to delete. Example: 'http://www.example.com/sitemap.xml'.
        
        Returns:
            None: If the request is successful.
        
        Tags:
            sitemap_management
        """
        # Encode URL parts used as path segments
        siteUrl_encoded = urllib.parse.quote(siteUrl, safe="")
        feedpath_encoded = urllib.parse.quote(feedpath, safe="")

        url = f"{self.webmasters_base_url}/sites/{siteUrl_encoded}/sitemaps/{feedpath_encoded}"
        response = self._delete(url)
        response.raise_for_status()

    def get_sitemap(self, siteUrl: str, feedpath: str) -> dict[str, Any]:
        """
        Retrieves detailed information for a single, specific sitemap using its full URL (`feedpath`). Unlike `list_sitemaps`, which fetches all sitemaps for a site, this function targets and returns one sitemap resource, providing its status, last processed date, and other API metadata.
        
        Args:
            siteUrl (str): The site's URL, including protocol (e.g. 'http://www.example.com/').
            feedpath (str): The URL of the sitemap to retrieve. Example: 'http://www.example.com/sitemap.xml'.
        
        Returns:
            Dict[str, Any]: Sitemap resource.
        
        Tags:
            sitemap_management
        """
        siteUrl_encoded = urllib.parse.quote(siteUrl, safe="")
        feedpath_encoded = urllib.parse.quote(feedpath, safe="")

        url = f"{self.webmasters_base_url}/sites/{siteUrl_encoded}/sitemaps/{feedpath_encoded}"
        response = self._get(url)
        response.raise_for_status()
        return response.json()

    def list_sitemaps(
        self, siteUrl: str, sitemapIndex: str | None = None
    ) -> dict[str, Any]:
        """
        Retrieves a list of sitemaps submitted for a specific site. Optionally, it can list the sitemaps contained within a specified sitemap index file instead of all sitemaps for the site. This contrasts with get_sitemap, which fetches a single sitemap's details.
        
        Args:
            siteUrl (str): The site's URL, including protocol (e.g. 'http://www.example.com/').
            sitemapIndex (Optional[str]): The URL of the sitemap index.
                                          Example: 'http://www.example.com/sitemap_index.xml'.
        
        Returns:
            Dict[str, Any]: List of sitemap resources.
        
        Tags:
            sitemap_management, important
        """
        siteUrl_encoded = urllib.parse.quote(siteUrl, safe="")
        url = f"{self.webmasters_base_url}/sites/{siteUrl_encoded}/sitemaps"

        query_params = {}
        if sitemapIndex is not None:
            query_params["sitemapIndex"] = sitemapIndex

        response = self._get(url, params=query_params if query_params else None)
        response.raise_for_status()
        return response.json()

    def submit_sitemap(self, siteUrl: str, feedpath: str) -> None:
        """
        Submits a sitemap to a specified Google Search Console site property. This function notifies Google of the sitemap's location for crawling via a PUT request. It is the primary action for adding or updating a sitemap, complementing `get_sitemap`, `list_sitemaps`, and `delete_sitemap`.
        
        Args:
            siteUrl (str): The site's URL, including protocol (e.g. 'http://www.example.com/').
            feedpath (str): The URL of the sitemap to submit. Example: 'http://www.example.com/sitemap.xml'.
        
        Returns:
            None: If the request is successful.
        
        Tags:
            sitemap_management
        """
        siteUrl_encoded = urllib.parse.quote(siteUrl, safe="")
        feedpath_encoded = urllib.parse.quote(feedpath, safe="")

        url = f"{self.webmasters_base_url}/sites/{siteUrl_encoded}/sitemaps/{feedpath_encoded}"
        # PUT requests for submitting/notifying often don't have a body.
        response = self._put(url, data=None)
        response.raise_for_status()

    # --- Sites ---

    def add_site(self, siteUrl: str) -> dict[str, Any]:
        """
        Adds a site to the user's Google Search Console account, which requires subsequent ownership verification. Upon success, it returns a dictionary containing the site resource. This method creates a new site entry, unlike `list_sites` which only retrieves existing ones.
        
        Args:
            siteUrl (str): The URL of the site to add. Example: 'http://www.example.com/'.
        
        Returns:
            Dict[str, Any]: Site resource upon successful addition.
        
        Tags:
            site_management, important
        """
        siteUrl_encoded = urllib.parse.quote(siteUrl, safe="")
        url = f"{self.webmasters_base_url}/sites/{siteUrl_encoded}"
        # This specific PUT for adding a site generally does not require a body;
        # the resource identifier is the siteUrl itself.
        # Google API docs state it returns a site resource.
        response = self._put(url, data=None)
        response.raise_for_status()
        return response.json()

    def delete_site(self, siteUrl: str) -> None:
        """
        Removes a website property from the user's Google Search Console account using its URL. This function sends a DELETE request to the API, distinguishing it from `delete_sitemap` which only removes a sitemap file rather than the entire site property from the user's management list.
        
        Args:
            siteUrl (str): The URL of the site to delete. Example: 'http://www.example.com/'.
        
        Returns:
            None: If the request is successful.
        
        Tags:
            site_management
        """
        siteUrl_encoded = urllib.parse.quote(siteUrl, safe="")
        url = f"{self.webmasters_base_url}/sites/{siteUrl_encoded}"
        response = self._delete(url)
        response.raise_for_status()

    def get_site(self, siteUrl: str) -> dict[str, Any]:
        """
        Retrieves the resource for a specific site property from Google Search Console, using its URL as an identifier. Unlike `list_sites`, which retrieves all user properties, this function fetches detailed information for a single, known site.
        
        Args:
            siteUrl (str): The site's URL, including protocol (e.g. 'http://www.example.com/').
        
        Returns:
            Dict[str, Any]: Site resource.
        
        Tags:
            site_management
        """
        siteUrl_encoded = urllib.parse.quote(siteUrl, safe="")
        url = f"{self.webmasters_base_url}/sites/{siteUrl_encoded}"
        response = self._get(url)
        response.raise_for_status()
        return response.json()

    def list_sites(self) -> dict[str, Any]:
        """
        Retrieves a list of all websites and domain properties the authenticated user can access in Google Search Console. Unlike `get_site`, which fetches a single property, this function returns a comprehensive overview of all managed sites associated with the user's account.
        
        Returns:
            Dict[str, Any]: List of site resources.
        
        Tags:
            site_management
        """
        url = f"{self.webmasters_base_url}/sites"
        response = self._get(url)
        response.raise_for_status()
        return response.json()

    # --- URL Inspection ---

    def inspect_url(
        self, inspectionUrl: str, siteUrl: str, languageCode: str | None = None
    ) -> dict[str, Any]:
        """
        Retrieves the Google Index status for a specified URL within a given Search Console property. This function queries the URL Inspection API to return detailed information about how Google sees the page, including its indexing eligibility and any detected issues.
        
        Args:
            inspectionUrl (str): The URL to inspect. Example: 'https://www.example.com/mypage'.
            siteUrl (str): The site URL (property) to inspect the URL under.
                           Must be a property in Search Console. Example: 'sc-domain:example.com' or 'https://www.example.com/'.
            languageCode (Optional[str]): Optional. The BCP-47 language code for the inspection. Example: 'en-US'.
        
        Returns:
            Dict[str, Any]: Inspection result containing details about the URL's indexing status.
        
        Tags:
            url_inspection, indexing
        """
        url = f"{self.searchconsole_base_url}/urlInspection/index:inspect"
        request_body: dict[str, Any] = {
            "inspectionUrl": inspectionUrl,
            "siteUrl": siteUrl,
        }
        if languageCode is not None:
            request_body["languageCode"] = languageCode

        # Assuming _post handles dict as JSON payload, similar to ExaApp
        response = self._post(url, data=request_body)
        response.raise_for_status()
        return response.json()

    # --- Search Analytics ---

    def query_search_analytics(
        self,
        siteUrl: str,
        startDate: str,
        endDate: str,
        dimensions: list[str] | None = None,
        dimensionFilterGroups: list[dict[str, Any]] | None = None,
        aggregationType: str | None = None,
        rowLimit: int | None = None,
        startRow: int | None = None,
        dataState: str | None = None,
        search_type: str | None = None,  # 'type' is a reserved keyword in Python
    ) -> dict[str, Any]:
        """
        Queries and retrieves search traffic data for a specified site within a given date range. Supports advanced filtering, grouping by various dimensions (e.g., query, page, device), and aggregation to customize the analytics report from the Google Search Console API.
        
        Args:
            siteUrl (str): The site's URL, including protocol (e.g. 'http://www.example.com/').
            startDate (str): Start date of the requested period in YYYY-MM-DD format.
            endDate (str): End date of the requested period in YYYY-MM-DD format.
            dimensions (Optional[List[str]]): List of dimensions to group the data by.
                Possible values: "date", "query", "page", "country", "device", "searchAppearance".
                Example: ["date", "query"].
            dimensionFilterGroups (Optional[List[Dict[str, Any]]]): Filter the results by dimensions.
                Example: [{
                    "groupType": "and",
                    "filters": [{
                        "dimension": "country",
                        "operator": "equals",
                        "expression": "USA"
                    }, {
                        "dimension": "device",
                        "operator": "equals",
                        "expression": "DESKTOP"
                    }]
                }]
            aggregationType (Optional[str]): How data is aggregated.
                Possible values: "auto", "byPage", "byProperty". Default is "auto".
            rowLimit (Optional[int]): The maximum number of rows to return. Default is 1000. Max 25000.
            startRow (Optional[int]): Zero-based index of the first row to return. Default is 0.
            dataState (Optional[str]): Whether to filter for fresh data or all data.
                Possible values: "all", "final". Default "all".
            search_type (Optional[str]): Filter by search type.
                Example: "web", "image", "video", "news", "discover", "googleNews".
                This corresponds to the 'type' parameter in the API.
        
        Returns:
            Dict[str, Any]: Search analytics data.
        
        Tags:
            search_analytics, reporting
        """
        siteUrl_encoded = urllib.parse.quote(siteUrl, safe="")
        url = (
            f"{self.webmasters_base_url}/sites/{siteUrl_encoded}/searchAnalytics/query"
        )

        request_body: dict[str, Any] = {
            "startDate": startDate,
            "endDate": endDate,
        }
        if dimensions is not None:
            request_body["dimensions"] = dimensions
        if dimensionFilterGroups is not None:
            request_body["dimensionFilterGroups"] = dimensionFilterGroups
        if aggregationType is not None:
            request_body["aggregationType"] = aggregationType
        if rowLimit is not None:
            request_body["rowLimit"] = rowLimit
        if startRow is not None:
            request_body["startRow"] = startRow
        if dataState is not None:
            request_body["dataState"] = dataState
        if search_type is not None:
            request_body["type"] = search_type  # API expects 'type'

        response = self._post(url, data=request_body)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_sitemap,
            self.list_sitemaps,
            self.submit_sitemap,
            self.delete_sitemap,
            self.get_site,
            self.list_sites,
            self.add_site,
            self.delete_site,
            self.inspect_url,
            self.query_search_analytics,
        ]
