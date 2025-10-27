import os
from dotenv import load_dotenv

load_dotenv()

from typing import Any, Literal

from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from universal_mcp.applications.linkedin import LinkedinApp


class ScraperApp(APIApplication):
    """
    Application for interacting with LinkedIn API.
    Provides a simplified interface for LinkedIn search operations.
    """

    def __init__(self, integration: Integration, **kwargs: Any) -> None:
        super().__init__(name="scraper", integration=integration, **kwargs)
        if self.integration:
            credentials = self.integration.get_credentials()
            self.account_id = credentials.get("account_id")
        else:
            logger.warning("Integration not found")
            self.account_id = None

    @property
    def base_url(self) -> str:
        if not self._base_url:
            unipile_dsn = os.getenv("UNIPILE_DSN")
            if not unipile_dsn:
                logger.error(
                    "UnipileApp: UNIPILE_DSN environment variable is not set."
                )
                raise ValueError(
                    "UnipileApp: UNIPILE_DSN environment variable is required."
                )
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
        if not self.integration:
            logger.warning(
                "UnipileApp: No integration configured, returning empty headers."
            )
            return {}

        api_key = os.getenv("UNIPILE_API_KEY")
        if not api_key:
            logger.error(
                "UnipileApp: API key not found in integration credentials for Unipile."
            )
            return {  # Or return minimal headers if some calls might not need auth (unlikely for Unipile)
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
            }

        logger.debug("UnipileApp: Using X-Api-Key for authentication.")
        return {
            "x-api-key": api_key,
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",  # Often good practice for APIs
        }

    def linkedin_search(
        self,
        category: Literal["people", "companies", "posts", "jobs"],
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        date_posted: Literal["past_day", "past_week", "past_month"] | None = None,
        sort_by: Literal["relevance", "date"] = "relevance",
        minimum_salary_value: int = 40,
    ) -> dict[str, Any]:
        """
        Performs a comprehensive LinkedIn search for people, companies, posts, or jobs using keywords.
        Supports pagination and targets either the classic or Sales Navigator API for posts.
        For people, companies, and jobs, it uses the classic API.

        Args:
            category: Type of search to perform. Valid values are "people", "companies", "posts", or "jobs".
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            date_posted: Filter by when the post was posted (posts only). Valid values are "past_day", "past_week", or "past_month".
            sort_by: How to sort the results (for posts and jobs). Valid values are "relevance" or "date".
            minimum_salary_value: The minimum salary to filter for (jobs only).

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
            ValueError: If the category is empty.

        Tags:
            linkedin, search, people, companies, posts, jobs, api, important
        """
        if not category:
            raise ValueError("Category cannot be empty.")

        url = f"{self.base_url}/api/v1/linkedin/search"

        params: dict[str, Any] = {"account_id": self.account_id}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit

        payload: dict[str, Any] = {"api": "classic", "category": category}

        if keywords:
            payload["keywords"] = keywords

        if category == "posts":
            if date_posted:
                payload["date_posted"] = date_posted
            if sort_by:
                payload["sort_by"] = sort_by

        elif category == "jobs":
            payload["minimum_salary"] = {
                "currency": "USD",
                "value": minimum_salary_value,
            }
            if sort_by:
                payload["sort_by"] = sort_by

        response = self._post(url, params=params, data=payload)
        return self._handle_response(response)

    def linkedin_list_profile_posts(
        self,
        identifier: str,  # User or Company provider internal ID
        cursor: str | None = None,
        limit: int | None = None,  # 1-100 (spec says max 250)
        is_company: bool | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of posts from a specific user or company profile using their provider ID. An authorizing `account_id` is required, and the `is_company` flag must specify the entity type, distinguishing this from `retrieve_post` which fetches a single post by its own ID.

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
        params: dict[str, Any] = {"account_id": self.account_id}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        if is_company is not None:
            params["is_company"] = is_company

        response = self._get(url, params=params)
        return response.json()

    def linkedin_retrieve_profile(self, identifier: str) -> dict[str, Any]:
        """
        Retrieves a specific LinkedIn user's profile using their public or internal ID. Unlike `retrieve_own_profile`, which fetches the authenticated user's details, this function targets and returns data for any specified third-party user profile on the platform.

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
        params: dict[str, Any] = {"account_id": self.account_id}
        response = self._get(url, params=params)
        return self._handle_response(response)

    def linkedin_list_post_comments(
        self,
        post_id: str,
        comment_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Fetches comments for a specific post. Providing an optional `comment_id` retrieves threaded replies instead of top-level comments. This read-only operation contrasts with `create_post_comment`, which publishes new comments, and `list_content_reactions`, which retrieves 'likes'.

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
        params: dict[str, Any] = {"account_id": self.account_id}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = str(limit)
        if comment_id:
            params["comment_id"] = comment_id

        response = self._get(url, params=params)
        return response.json()

    def list_tools(self):
        """
        Returns a list of available tools/functions in this application.

        Returns:
            A list of functions that can be used as tools.
        """
        return [
            self.linkedin_search,
            self.linkedin_list_profile_posts,
            self.linkedin_retrieve_profile,
            self.linkedin_list_post_comments,
        ]
