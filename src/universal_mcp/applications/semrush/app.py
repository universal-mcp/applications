from typing import Any

from universal_mcp.applications.application import APIApplication
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

    def _build_params_and_get(self, report_type: str, **kwargs) -> dict[str, Any]:
        """
        Builds the parameters dictionary and makes a GET request to the Semrush API.
        """
        params = {
            "type": report_type,
            "key": self.api_key,
        }
        for key, value in kwargs.items():
            if value is not None:
                params[key] = value

        url = self.base_url
        if "analytics" in report_type:
            url = f"{self.base_url}/analytics/v1"

        response = self._get(url, params=params)
        return self._handle_response(response)

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_ad_history",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            display_date=display_date,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
            export_escape=export_escape,
            export_decode=export_decode,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_organic_unique",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            display_date=display_date,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
            export_escape=export_escape,
            export_decode=export_decode,
        )

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
            domain-search, important
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_organic",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            display_date=display_date,
            display_daily=display_daily,
            export_columns=export_columns,
            display_sort=display_sort,
            display_positions=display_positions,
            display_positions_type=display_positions_type,
            display_filter=display_filter,
            export_escape=export_escape,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_organic_subdomains",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            display_date=display_date,
            export_columns=export_columns,
            display_sort=display_sort,
            export_escape=export_escape,
            export_decode=export_decode,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_adwords",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            display_date=display_date,
            export_columns=export_columns,
            display_sort=display_sort,
            display_positions=display_positions,
            display_filter=display_filter,
            export_escape=export_escape,
            export_decode=export_decode,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_shopping",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
            export_escape=export_escape,
            export_decode=export_decode,
        )

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
        """
        if not domains:
            raise ValueError("Domains parameter is required")
        return self._build_params_and_get(
            "domain_domains",
            domains=domains,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            display_date=display_date,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
            export_escape=export_escape,
            export_decode=export_decode,
        )

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
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_sort=display_sort,
            display_limit=display_limit,
            display_offset=display_offset,
            display_filter=display_filter,
        )

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
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_overview_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_sort=display_sort,
            display_limit=display_limit,
            display_offset=display_offset,
            display_filter=display_filter,
        )

    def keyword_difficulty(
        self,
        phrase: str,
        database: str = "us",
        export_columns: str | None = None,
        export_escape: int | None = None,
    ) -> dict[str, Any]:
        """
        Get keyword difficulty data to estimate ranking difficulty for organic search terms.
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_kdi",
            phrase=phrase,
            database=database,
            export_columns=export_columns,
            export_escape=export_escape,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_adwords_unique",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
            export_escape=export_escape,
            export_decode=export_decode,
        )

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
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_anchors_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_sort=display_sort,
            display_limit=display_limit,
            display_offset=display_offset,
        )

    def authority_score_profile(self, target: str, target_type: str) -> dict[str, Any]:
        """
        Get distribution of referring domains by Authority Score from 0 to 100.
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_ascore_profile_analytics",
            target=target,
            target_type=target_type,
        )

    def batch_comparison(
        self,
        targets: list[str],
        target_types: list[str],
        export_columns: str | None = None,
    ) -> dict[str, Any]:
        """
        Compare backlink profiles and link-building progress across multiple competitors.
        """
        if not targets or not target_types:
            raise ValueError("Targets and target_types parameters are required")
        if len(targets) > 200:
            raise ValueError("Maximum 200 targets allowed")
        if len(targets) != len(target_types):
            raise ValueError(
                "Targets and target_types arrays must have the same length"
            )
        return self._build_params_and_get(
            "backlinks_comparison_analytics",
            targets=targets,
            target_types=target_types,
            export_columns=export_columns,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_these",
            phrase=phrase,
            database=database,
            export_escape=export_escape,
            export_decode=export_decode,
            display_date=display_date,
            export_columns=export_columns,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_fullsearch",
            phrase=phrase,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
        )

    def categories(
        self, target: str, target_type: str, export_columns: str | None = None
    ) -> dict[str, Any]:
        """
        Get list of categories that the queried domain belongs to with confidence ratings.
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_categories_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
        )

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
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_categories_profile_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_limit=display_limit,
            display_offset=display_offset,
        )

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
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_competitors_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_limit=display_limit,
            display_offset=display_offset,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_organic_organic",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            display_date=display_date,
            export_columns=export_columns,
            display_sort=display_sort,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_adwords_adwords",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            display_date=display_date,
            export_columns=export_columns,
            display_sort=display_sort,
        )

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
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_pages_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_sort=display_sort,
            display_limit=display_limit,
            display_offset=display_offset,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_adwords_historical",
            phrase=phrase,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            export_columns=export_columns,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_all",
            phrase=phrase,
            database=database,
            export_escape=export_escape,
            export_decode=export_decode,
            export_columns=export_columns,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_this",
            phrase=phrase,
            database=database,
            export_escape=export_escape,
            export_decode=export_decode,
            display_date=display_date,
            export_columns=export_columns,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_organic",
            phrase=phrase,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            display_date=display_date,
            export_columns=export_columns,
            positions_type=positions_type,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_adwords",
            phrase=phrase,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            display_date=display_date,
            export_columns=export_columns,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_questions",
            phrase=phrase,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_shopping_shopping",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            export_columns=export_columns,
            display_sort=display_sort,
        )

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
        """
        if not domain:
            raise ValueError("Domain parameter is required")
        return self._build_params_and_get(
            "domain_shopping_unique",
            domain=domain,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
        )

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
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_refdomains_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_sort=display_sort,
            display_limit=display_limit,
            display_offset=display_offset,
            display_filter=display_filter,
        )

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
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_geo_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_sort=display_sort,
            display_limit=display_limit,
            display_offset=display_offset,
        )

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
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
        return self._build_params_and_get(
            "phrase_related",
            phrase=phrase,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            export_columns=export_columns,
            display_sort=display_sort,
            display_filter=display_filter,
        )

    def tlds_distribution(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
    ) -> dict[str, Any]:
        """
        Get referring domain distribution by top-level domain (e.g., .com, .org, .net).
        """
        if not target or not target_type:
            raise ValueError("Target and target_type parameters are required")
        return self._build_params_and_get(
            "backlinks_tlds_profile_analytics",
            target=target,
            target_type=target_type,
            export_columns=export_columns,
            display_sort=display_sort,
            display_limit=display_limit,
            display_offset=display_offset,
        )

    def url_organic_search_keywords(
        self,
        url: str,
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
        Get keywords that bring users to a URL via Google's top 100 organic search results.
        """
        if not url:
            raise ValueError("URL parameter is required")
        return self._build_params_and_get(
            "url_organic",
            url=url,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            display_date=display_date,
            export_columns=export_columns,
            display_sort=display_sort,
        )

    def url_paid_search_keywords(
        self,
        url: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
    ) -> dict[str, Any]:
        """
        Get keywords that bring users to a URL via Google's paid search results.
        """
        if not url:
            raise ValueError("URL parameter is required")
        return self._build_params_and_get(
            "url_adwords",
            url=url,
            database=database,
            display_limit=display_limit,
            display_offset=display_offset,
            export_escape=export_escape,
            export_decode=export_decode,
            export_columns=export_columns,
            display_sort=display_sort,
        )

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
            self.tlds_distribution,
            self.url_organic_search_keywords,
            self.url_paid_search_keywords,
        ]
