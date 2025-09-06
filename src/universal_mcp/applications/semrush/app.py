from typing import Any

from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration


class SemrushApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """

    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="semrush", integration=integration, **kwargs)
        self.base_url = "https://api.semrush.com"
        self._api_key: str | None = None

    def _get_headers(self):
        if not self.integration:
            raise ValueError("Integration not found")
        credentials = self.integration.get_credentials()
        if "api_key" in credentials:
            self.api_key = credentials["api_key"]
        # Always return empty headers
        return {}

    @property
    def api_key(self):
        """Gets the API key by calling _get_headers and caches it."""
        if self._api_key:
            return self._api_key
        self._get_headers()
        return self._api_key

    @api_key.setter
    def api_key(self, value: str) -> None:
        """Sets the API key.

        Args:
            value (str): The API key to set.
        """
        self._api_key = value

    def domain_ad_history(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
    ) -> dict[str, Any]:
        """
        Get domain ad history data showing past ad copies, landing pages, and performance metrics over time.

        Args:
            domain (str): Unique name of the website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "tr_desc", "pc_asc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response

        Returns:
            Dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search, important
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_ad_history",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def domain_organic_pages(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
    ) -> dict[str, Any]:
        """
        Get unique pages of a domain that rank in Google's top 100 organic search results.

        Args:
            domain (str): Unique name of the website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "tr_desc", "pc_asc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_organic_unique",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def domain_organic_search_keywords(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        display_daily: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_positions: str | None = None,
        display_positions_type: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
    ) -> dict[str, Any]:
        """
        Get keywords that bring organic traffic to a domain via Google's top 100 search results.

        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" or "YYYYMMDD"
            display_daily (int, optional): Set to 1 for daily updates in last 31 days
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "po_asc", "tg_desc")
            display_positions (str, optional): Filter by position changes ("new", "lost", "rise", "fall")
            display_positions_type (str, optional): Position type ("organic", "all", "serp_features")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_organic",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_date is not None:
            params["display_date"] = display_date
        if display_daily is not None:
            params["display_daily"] = display_daily
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_positions is not None:
            params["display_positions"] = display_positions
        if display_positions_type is not None:
            params["display_positions_type"] = display_positions_type
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def domain_organic_subdomains(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
    ) -> dict[str, Any]:
        """
        Get subdomains of a domain that rank in Google's top 100 organic search results.

        Args:
            domain (str): Unique name of the website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "pc_asc", "tg_desc")
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_organic_subdomains",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def domain_paid_search_keywords(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_positions: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
    ) -> dict[str, Any]:
        """
        Get keywords that bring paid traffic to a domain via Google's paid search results.

        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "po_asc", "tg_desc")
            display_positions (str, optional): Filter by position changes ("new", "lost", "rise", "fall")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_adwords",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_positions is not None:
            params["display_positions"] = display_positions
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def domain_pla_search_keywords(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
    ) -> dict[str, Any]:
        """
        Get keywords that trigger a domain's product listing ads (PLA) in Google's paid search results.

        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "po_asc", "nq_desc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_shopping",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def domain_vs_domain(
        self,
        domains: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
    ) -> dict[str, Any]:
        """
        Compare up to five domains by common keywords, unique keywords, or search terms unique to the first domain.

        Args:
            domains (str): URL-encoded string containing domains in format: <sign>|<type>|<domain>
                          Examples:
                          - Shared keywords: "*|or|domain1|*|or|domain2|*|or|domain3"
                          - All keywords: "*|or|domain1|+|or|domain2|+|or|domain3"
                          - Unique keywords: "*|or|domain1|-|or|domain2|-|or|domain3"
                          - Untapped keywords: "*|or|domain2|+|or|domain3|-|or|domain1"
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "p0_asc", "p1_desc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domains:
            raise ValueError("Domains parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_domains",
            "key": self.api_key,
            "domains": domains,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def backlinks(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_filter: str | None = None,
    ) -> dict[str, Any]:
        """
        Get backlinks data for a domain, root domain, or URL.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "page_ascore_desc", "last_seen_asc")
            display_limit (int, optional): Number of results to return (max 1,000,000)
            display_offset (int, optional): Number of results to skip
            display_filter (str, optional): Filter criteria for columns

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_filter is not None:
            params["display_filter"] = display_filter

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def backlinks_overview(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_filter: str | None = None,
    ) -> dict[str, Any]:
        """
        Get backlinks overview summary including type, referring domains, and IP addresses.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order for results
            display_limit (int, optional): Number of results to return
            display_offset (int, optional): Number of results to skip
            display_filter (str, optional): Filter criteria for columns

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_overview",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_filter is not None:
            params["display_filter"] = display_filter

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def keyword_difficulty(
        self,
        phrase: str,
        database: str = "us",
        export_columns: str | None = None,
        export_escape: int | None = None,
    ) -> dict[str, Any]:
        """
        Get keyword difficulty data to estimate ranking difficulty for organic search terms.

        Args:
            phrase (str): Phrase (from 1 to 100 keywords separated by semicolons)
            database (str): Regional database (default: "us")
            export_columns (str, optional): Comma-separated list of columns to include
            export_escape (int, optional): Set to 1 to wrap columns in quotes

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis, important
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_kdi",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if export_escape is not None:
            params["export_escape"] = export_escape

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def ads_copies(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
    ) -> dict[str, Any]:
        """
        Get unique ad copies that appeared when a domain ranked in Google's paid search results.

        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "pc_asc", "pc_desc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_adwords_unique",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def anchors(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
    ) -> dict[str, Any]:
        """
        Get anchor texts used in backlinks leading to a domain, root domain, or URL.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "domains_num_desc", "backlinks_num_asc")
            display_limit (int, optional): Number of results to return (default: 10,000)
            display_offset (int, optional): Number of results to skip

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_anchors",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def authority_score_profile(self, target: str, target_type: str) -> dict[str, Any]:
        """
        Get distribution of referring domains by Authority Score from 0 to 100.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_ascore_profile",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def batch_comparison(
        self,
        targets: list[str],
        target_types: list[str],
        export_columns: str | None = None,
    ) -> dict[str, Any]:
        """
        Compare backlink profiles and link-building progress across multiple competitors.

        Args:
            targets (list[str]): Array of root domains, subdomains, or URLs to investigate (max 200)
            target_types (list[str]): Array of target types corresponding to targets (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing or invalid
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not targets:
            raise ValueError("Targets parameter is required")
        if not target_types:
            raise ValueError("Target_types parameter is required")
        if len(targets) > 200:
            raise ValueError("Maximum 200 targets allowed")
        if len(targets) != len(target_types):
            raise ValueError(
                "Targets and target_types arrays must have the same length"
            )

        # Build parameters dictionary
        params = {"type": "backlinks_comparison", "key": self.api_key}

        # Add targets and target_types as arrays
        for target in targets:
            params["targets[]"] = target
        for target_type in target_types:
            params["target_types[]"] = target_type

        if export_columns is not None:
            params["export_columns"] = export_columns

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def batch_keyword_overview(
        self,
        phrase: str,
        database: str = "us",
        export_escape: int | None = None,
        export_decode: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
    ) -> dict[str, Any]:
        """
        Get summary of up to 100 keywords including volume, CPC, competition level, and results count.

        Args:
            phrase (str): Keyword or keyword expression to investigate (up to 100 keywords separated by semicolons)
            database (str): Regional database (default: "us")
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_these",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def broad_match_keyword(
        self,
        phrase: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
    ) -> dict[str, Any]:
        """
        Get broad matches and alternate search queries for a keyword or keyword expression.

        Args:
            phrase (str): Keyword or keyword expression to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "nq_desc", "cp_asc")
            display_filter (str, optional): Filter criteria for columns

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_fullsearch",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def categories(
        self, target: str, target_type: str, export_columns: str | None = None
    ) -> dict[str, Any]:
        """
        Get list of categories that the queried domain belongs to with confidence ratings.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, subdomain, or url)
            export_columns (str, optional): Comma-separated list of columns to include

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_categories",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def categories_profile(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
    ) -> dict[str, Any]:
        """
        Get categories that referring domains belong to with domain counts for the queried domain.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_limit (int, optional): Number of results to return (default: 10,000)
            display_offset (int, optional): Number of results to skip

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_categories_profile",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def competitors(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
    ) -> dict[str, Any]:
        """
        Get domains that share a similar backlink profile with the analyzed domain.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_limit (int, optional): Number of results to return (default: 10,000)
            display_offset (int, optional): Number of results to skip

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_competitors",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def competitors_organic_search(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
    ) -> dict[str, Any]:
        """
        Get domain's competitors in organic search results with common keywords analysis.

        Args:
            domain (str): Unique name of the website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "np_desc", "cr_asc")

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_organic_organic",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def competitors_paid_search(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
    ) -> dict[str, Any]:
        """
        Get domain's competitors in paid search results with common keywords analysis.

        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "np_desc", "cr_asc")

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_adwords_adwords",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def indexed_pages(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
    ) -> dict[str, Any]:
        """
        Get indexed pages of the queried domain with backlink and response data.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "backlinks_num_desc", "backlinks_num_asc")
            display_limit (int, optional): Number of results to return (default: 10,000)
            display_offset (int, optional): Number of results to skip

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_pages",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def keyword_ads_history(
        self,
        phrase: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        export_columns: str | None = None,
    ) -> dict[str, Any]:
        """
        Get domains that have bid on a keyword in the last 12 months with their paid search positions.

        Args:
            phrase (str): Keyword or keyword expression to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            export_columns (str, optional): Comma-separated list of columns to include

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_adwords_historical",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if export_columns is not None:
            params["export_columns"] = export_columns

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def keyword_overview_all_databases(
        self,
        phrase: str,
        database: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        export_columns: str | None = None,
    ) -> dict[str, Any]:
        """
        Get keyword summary including volume, CPC, competition level, and results across all regional databases.

        Args:
            phrase (str): Keyword or keyword expression to investigate
            database (str, optional): Regional database (if not specified, uses all databases)
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            export_columns (str, optional): Comma-separated list of columns to include

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {"type": "phrase_all", "key": self.api_key, "phrase": phrase}

        if database is not None:
            params["database"] = database
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if export_columns is not None:
            params["export_columns"] = export_columns

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def keyword_overview_one_database(
        self,
        phrase: str,
        database: str = "us",
        export_escape: int | None = None,
        export_decode: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
    ) -> dict[str, Any]:
        """
        Get keyword summary including volume, CPC, competition level, and results for a specific database.

        Args:
            phrase (str): Keyword or keyword expression to investigate
            database (str): Regional database (default: "us")
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_this",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def organic_results(
        self,
        phrase: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        positions_type: str | None = None,
    ) -> dict[str, Any]:
        """
        Get domains ranking in Google's top 100 organic search results for a keyword.

        Args:
            phrase (str): Keyword or keyword expression to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            positions_type (str, optional): Position type ("organic" or "all")

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_organic",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if positions_type is not None:
            params["positions_type"] = positions_type

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def paid_results(
        self,
        phrase: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
    ) -> dict[str, Any]:
        """
        Get domains ranking in Google's paid search results for a keyword.

        Args:
            phrase (str): Keyword or keyword expression to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_adwords",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def phrase_questions(
        self,
        phrase: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
    ) -> dict[str, Any]:
        """
        Get phrase questions relevant to a queried term in a chosen database.

        Args:
            phrase (str): Keyword or keyword expression to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "nq_desc", "cp_asc")
            display_filter (str, optional): Filter criteria for columns

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_questions",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def pla_competitors(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
    ) -> dict[str, Any]:
        """
        Get domains competing against the requested domain in Google's Product Listing Ads (PLA).

        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "np_desc", "cr_asc")

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_shopping_shopping",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def pla_copies(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
    ) -> dict[str, Any]:
        """
        Get product listing ad (PLA) copies that appeared when a domain ranked in Google's paid search results.

        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "pr_desc", "pc_asc")
            display_filter (str, optional): Filter criteria for columns

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")

        # Build parameters dictionary
        params = {
            "type": "domain_shopping_unique",
            "key": self.api_key,
            "domain": domain,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def referring_domains(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_filter: str | None = None,
    ) -> dict[str, Any]:
        """
        Get domains pointing to the queried domain, root domain, or URL.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "domain_ascore_desc", "backlinks_num_asc")
            display_limit (int, optional): Number of results to return (default: 10,000)
            display_offset (int, optional): Number of results to skip
            display_filter (str, optional): Filter criteria for columns

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_refdomains",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_filter is not None:
            params["display_filter"] = display_filter

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def referring_domains_by_country(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
    ) -> dict[str, Any]:
        """
        Get referring domain distribution by country based on IP addresses.

        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "domains_num_desc", "backlinks_num_asc")
            display_limit (int, optional): Number of results to return (default: 10,000)
            display_offset (int, optional): Number of results to skip

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")

        # Build parameters dictionary
        params = {
            "type": "backlinks_geo",
            "key": self.api_key,
            "target": target,
            "target_type": target_type,
        }

        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset

        url = f"{self.base_url}/analytics/v1"
        response = self._get(url, params=params)

        return self._handle_response(response)

    def related_keywords(
        self,
        phrase: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
    ) -> dict[str, Any]:
        """
        Get extended list of related keywords, synonyms, and variations relevant to a queried term.

        Args:
            phrase (str): Keyword or keyword expression to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response, 1 for normal response
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "nq_desc", "cp_asc")
            display_filter (str, optional): Filter criteria for columns

        Returns:
            dict[str, Any]: API response data

        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")

        # Build parameters dictionary
        params = {
            "type": "phrase_related",
            "key": self.api_key,
            "phrase": phrase,
            "database": database,
        }

        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter

        response = self._get(self.base_url, params=params)

        return self._handle_response(response)

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [
            self.domain_ad_history,
            self.domain_organic_pages,
            self.domain_organic_search_keywords,
            self.domain_organic_subdomains,
            self.domain_paid_search_keywords,
            self.domain_pla_search_keywords,
            self.domain_vs_domain,
            self.backlinks,
            self.backlinks_overview,
            self.keyword_difficulty,
            self.ads_copies,
            self.anchors,
            self.authority_score_profile,
            self.batch_comparison,
            self.batch_keyword_overview,
            self.broad_match_keyword,
            self.categories,
            self.categories_profile,
            self.competitors,
            self.competitors_organic_search,
            self.competitors_paid_search,
            self.indexed_pages,
            self.keyword_ads_history,
            self.keyword_overview_all_databases,
            self.keyword_overview_one_database,
            self.organic_results,
            self.paid_results,
            self.phrase_questions,
            self.pla_competitors,
            self.pla_copies,
            self.referring_domains,
            self.referring_domains_by_country,
            self.related_keywords,
        ]
