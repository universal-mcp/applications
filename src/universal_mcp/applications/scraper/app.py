import os
from dotenv import load_dotenv

load_dotenv()
from typing import Any, Literal
from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class ScraperApp(APIApplication):
    """
    Application for interacting with LinkedIn API.
    Provides a simplified interface for LinkedIn search operations.
    """

    def __init__(self, integration: Integration, **kwargs: Any) -> None:
        super().__init__(name="scraper", integration=integration, **kwargs)
        self._account_id = None

    async def _get_account_id(self) -> str | None:
        if self._account_id:
            return self._account_id
        if self.integration:
            credentials = await self.integration.get_credentials_async()
            self._account_id = credentials.get("account_id")
        else:
            logger.warning("Integration not found")
        return self._account_id

    @property
    def base_url(self) -> str:
        if not self._base_url:
            unipile_dsn = os.getenv("UNIPILE_DSN")
            if not unipile_dsn:
                logger.error("UnipileApp: UNIPILE_DSN environment variable is not set.")
                raise ValueError("UnipileApp: UNIPILE_DSN environment variable is required.")
            self._base_url = f"https://{unipile_dsn}"
        return self._base_url

    @base_url.setter
    def base_url(self, base_url: str) -> None:
        self._base_url = base_url
        logger.info(f"UnipileApp: Base URL set to {self._base_url}")

    def _get_headers(self) -> dict[str, str]:
        """
        Get the headers for Unipile API requests.
        Overrides the base class method to use X-Api-Key.
        """
        api_key = os.getenv("UNIPILE_API_KEY")
        if not api_key:
            logger.error("UnipileApp: API key not found in integration credentials for Unipile.")
            return {"Content-Type": "application/json", "Cache-Control": "no-cache"}
        logger.debug("UnipileApp: Using X-Api-Key for authentication.")
        return {"x-api-key": api_key, "Content-Type": "application/json", "Cache-Control": "no-cache"}

    async def _aget_headers(self) -> dict[str, str]:
        """
        Get the headers for Unipile API requests asynchronously.
        Overrides the base class method to use X-Api-Key.
        """
        return self._get_headers()

    async def _aget_search_parameter_id(self, param_type: str, keywords: str) -> str:
        """
        Retrieves the ID for a given LinkedIn search parameter by its name.

        Args:
            param_type: The type of parameter to search for (e.g., "LOCATION", "COMPANY").
            keywords: The name of the parameter to find (e.g., "United States").

        Returns:
            The corresponding ID for the search parameter.

        Raises:
            ValueError: If no exact match for the keywords is found.
            httpx.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/api/v1/linkedin/search/parameters"
        params = {"account_id": await self._get_account_id(), "keywords": keywords, "type": param_type}
        response = await self._aget(url, params=params)
        results = self._handle_response(response)
        items = results.get("items", [])
        if items:
            return items[0]["id"]
        raise ValueError(f'Could not find a matching ID for {param_type}: "{keywords}"')

    async def linkedin_list_profile_posts(
        self, identifier: str, cursor: str | None = None, limit: int | None = None, is_company: bool | None = None
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of posts from a specific user or company profile using its provider ID. The `is_company` flag must specify the entity type. Unlike `linkedin_search_posts`, this function directly retrieves content from a known profile's feed instead of performing a global keyword search.

        Args:
            identifier: The entity's provider internal ID (LinkedIn ID).
            cursor: Pagination cursor.
            limit: Number of items to return (1-100, as per Unipile example, though spec allows up to 250).
            is_company: Boolean indicating if the identifier is for a company.

        Returns:
            A dictionary containing a list of post objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, list, user_posts, company_posts, content, api, important
        """
        url = f"{self.base_url}/api/v1/users/{identifier}/posts"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        if is_company is not None:
            params["is_company"] = is_company
        response = await self._aget(url, params=params)
        return response.json()

    async def linkedin_retrieve_profile(self, identifier: str) -> dict[str, Any]:
        """
        Fetches a specific LinkedIn user's profile using their public or internal ID. Unlike `linkedin_search_people`, which discovers multiple users via keywords, this function targets and retrieves detailed data for a single, known individual based on a direct identifier.

        Args:
            identifier: Can be the provider's internal id OR the provider's public id of the requested user.For example, for https://www.linkedin.com/in/manojbajaj95/, the identifier is "manojbajaj95".

        Returns:
            A dictionary containing the user's profile details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, profile, retrieve, get, api, important
        """
        url = f"{self.base_url}/api/v1/users/{identifier}"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def linkedin_list_post_comments(
        self, post_id: str, comment_id: str | None = None, cursor: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of comments for a specified LinkedIn post. It can retrieve either top-level comments or threaded replies if an optional `comment_id` is provided. This is a read-only operation, distinct from functions that search for posts or list user-specific content.

        Args:
            post_id: The social ID of the post.
            comment_id: If provided, retrieves replies to this comment ID instead of top-level comments.
            cursor: Pagination cursor.
            limit: Number of comments to return. (OpenAPI spec shows type string, passed as string if provided).

        Returns:
            A dictionary containing a list of comment objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, comment, list, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/{post_id}/comments"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = str(limit)
        if comment_id:
            params["comment_id"] = comment_id
        response = await self._aget(url, params=params)
        return response.json()

    async def linkedin_search_people(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        location: str | None = None,
        industry: str | None = None,
        company: str | None = None,
    ) -> dict[str, Any]:
        """
        Performs a paginated search for people on LinkedIn, distinct from searches for companies or jobs. It filters results using keywords, location, industry, and company, internally converting filter names like 'United States' into their required API IDs before making the request.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            location: The geographical location to filter people by (e.g., "United States").
            industry: The industry to filter people by.(e.g., "Software Development".)
            company: The company to filter people by.(e.g., "Google".)

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/api/v1/linkedin/search"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        payload: dict[str, Any] = {"api": "classic", "category": "people"}
        if keywords:
            payload["keywords"] = keywords
        if location:
            location_id = await self._aget_search_parameter_id("LOCATION", location)
            payload["location"] = [location_id]
        if industry:
            industry_id = await self._aget_search_parameter_id("INDUSTRY", industry)
            payload["industry"] = [industry_id]
        if company:
            company_id = await self._aget_search_parameter_id("COMPANY", company)
            payload["company"] = [company_id]
        response = await self._apost(url, params=params, data=payload)
        return self._handle_response(response)

    async def linkedin_search_companies(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        location: str | None = None,
        industry: str | None = None,
    ) -> dict[str, Any]:
        """
        Executes a paginated LinkedIn search for companies, filtering by optional keywords, location, and industry. Unlike `linkedin_search_people` or `linkedin_search_jobs`, this function specifically sets the API search category to 'companies' to ensure that only company profiles are returned in the search results.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            location: The geographical location to filter companies by (e.g., "United States").
            industry: The industry to filter companies by.(e.g., "Software Development".)

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/api/v1/linkedin/search"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        payload: dict[str, Any] = {"api": "classic", "category": "companies"}
        if keywords:
            payload["keywords"] = keywords
        if location:
            location_id = await self._aget_search_parameter_id("LOCATION", location)
            payload["location"] = [location_id]
        if industry:
            industry_id = await self._aget_search_parameter_id("INDUSTRY", industry)
            payload["industry"] = [industry_id]
        response = await self._apost(url, params=params, data=payload)
        return self._handle_response(response)

    async def linkedin_search_posts(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        date_posted: Literal["past_day", "past_week", "past_month"] | None = None,
        sort_by: Literal["relevance", "date"] = "relevance",
    ) -> dict[str, Any]:
        """
        Performs a keyword-based search for LinkedIn posts, allowing results to be filtered by date and sorted by relevance. This function specifically queries the 'posts' category, distinguishing it from other search methods in the class that target people, companies, or jobs, and returns relevant content.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            date_posted: Filter by when the post was posted.
            sort_by: How to sort the results.

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/api/v1/linkedin/search"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        payload: dict[str, Any] = {"api": "classic", "category": "posts"}
        if keywords:
            payload["keywords"] = keywords
        if date_posted:
            payload["date_posted"] = date_posted
        if sort_by:
            payload["sort_by"] = sort_by
        response = await self._apost(url, params=params, data=payload)
        return self._handle_response(response)

    async def linkedin_search_jobs(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        region: str | None = None,
        sort_by: Literal["relevance", "date"] = "relevance",
        minimum_salary_value: Literal[40, 60, 80, 100, 120, 140, 160, 180, 200] = 40,
        industry: str | None = None,
    ) -> dict[str, Any]:
        """
        Executes a LinkedIn search specifically for job listings using keywords and filters like region, industry, and minimum salary. Unlike other search functions targeting people or companies, this is specialized for job listings and converts friendly filter names (e.g., "United States") into their required API IDs.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            region: The geographical region to filter jobs by (e.g., "United States").
            sort_by: How to sort the results.(e.g., "relevance" or "date".)
            minimum_salary_value: The minimum salary to filter for. Allowed values are 40, 60, 80, 100, 120, 140, 160, 180, 200.
            industry: The industry to filter jobs by. (e.g., "Software Development".)

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
            ValueError: If the specified location is not found.
        """
        url = f"{self.base_url}/api/v1/linkedin/search"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        payload: dict[str, Any] = {
            "api": "classic",
            "category": "jobs",
            "minimum_salary": {"currency": "USD", "value": minimum_salary_value},
        }
        if keywords:
            payload["keywords"] = keywords
        if sort_by:
            payload["sort_by"] = sort_by
        if region:
            location_id = await self._aget_search_parameter_id("LOCATION", region)
            payload["region"] = location_id
        if industry:
            industry_id = await self._aget_search_parameter_id("INDUSTRY", industry)
            payload["industry"] = [industry_id]
        response = await self._apost(url, params=params, data=payload)
        return self._handle_response(response)

    def list_tools(self):
        """
        Returns a list of available tools/functions in this application.

        Returns:
            A list of functions that can be used as tools.
        """
        return [
            self.linkedin_list_profile_posts,
            self.linkedin_retrieve_profile,
            self.linkedin_list_post_comments,
            self.linkedin_search_people,
            self.linkedin_search_companies,
            self.linkedin_search_posts,
            self.linkedin_search_jobs,
        ]
