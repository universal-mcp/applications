from dotenv import load_dotenv

load_dotenv()

from typing import Any, Literal

from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from universal_mcp.applications.unipile import UnipileApp


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
            self._unipile_app = UnipileApp(integration=self.integration)
        else:
            logger.warning("Integration not found")
            self.account_id = None
            self._unipile_app = None

    def linkedin_search(
        self,
        category: Literal["people", "companies", "posts", "jobs"],
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        date_posted: str | None = None,
        sort_by: str | None = None,
        minimum_salary_value: int | None = None,
    ) -> dict[str, Any]:
        """
        Performs a general LinkedIn search for posts, people, companies, or jobs using keywords and various filters. This function provides broad, keyword-based discovery across the platform, distinct from other methods that retrieve content from a specific user or company profile. It supports pagination and filtering criteria.
        
        Args:
            category: Type of search to perform - "people", "companies", "posts", or "jobs".
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            date_posted: Filter by when the post was posted (posts only).
            sort_by: How to sort the results (for posts and jobs).
            minimum_salary_value: The minimum salary to filter for (jobs only).
        
        Returns:
            A dictionary containing search results and pagination details.
        
        Raises:
            httpx.HTTPError: If the API request fails.
        
        Tags:
            linkedin, search, posts, people, companies, api, scrapper, important
        """
        return self._unipile_app.search(
            account_id=self.account_id,
            category=category,
            cursor=cursor,
            limit=limit,
            keywords=keywords,
            date_posted=date_posted,
            sort_by=sort_by,
            minimum_salary_value=minimum_salary_value,
        )

    def linkedin_list_profile_posts(
        self,
        identifier: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of all posts from a specific user or company profile using their unique identifier. This function retrieves content directly from a single profile, unlike the broader, keyword-based `linkedin_search` which searches across the entire LinkedIn platform.
        
        Args:
            identifier: The entity's provider internal ID (LinkedIn ID).starts with ACo for users, while for companies it's a series of numbers. You can get it in the results of linkedin_search.
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (1-100, though spec allows up to 250).
        
        Returns:
            A dictionary containing a list of post objects and pagination details.
        
        Raises:
            httpx.HTTPError: If the API request fails.
        
        Tags:
            linkedin, post, list, user_posts, company_posts, content, api, important
        """

        return self._unipile_app.list_profile_posts(
            identifier=identifier,
            account_id=self.account_id,
            cursor=cursor,
            limit=limit,
        )

    def linkedin_retrieve_profile(
        self,
        identifier: str,
    ) -> dict[str, Any]:
        """
        Retrieves a specific LinkedIn user's profile using their unique identifier (e.g., public username). Unlike other methods that list posts or comments, this function focuses on fetching the user's core profile data by delegating the request to the integrated Unipile application.
        
        Args:
            identifier: Use the id from linkedin_search results. It starts with ACo for users and is a series of numbers for companies.
        
        Returns:
            A dictionary containing the user's profile details.
        
        Raises:
            httpx.HTTPError: If the API request fails.
        
        Tags:
            linkedin, user, profile, retrieve, get, api, important
        """

        return self._unipile_app.retrieve_user_profile(
            identifier=identifier,
            account_id=self.account_id,
        )

    def linkedin_list_post_comments(
        self,
        post_id: str,
        comment_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of comments for a specified LinkedIn post. Providing a `comment_id` retrieves replies to that specific comment instead of top-level ones. This function exclusively targets post interactions, differentiating it from others that list posts or retrieve entire profiles.
        
        Args:
            post_id: The social ID of the post. Example urn:li:ugcPost:7386500271624896512
            comment_id: If provided, retrieves replies to this comment ID instead of top-level comments.
            cursor: Pagination cursor.
            limit: Number of comments to return.
        
        Returns:
            A dictionary containing a list of comment objects and pagination details.
        
        Raises:
            httpx.HTTPError: If the API request fails.
        
        Tags:
            linkedin, post, comment, list, content, api, important
        """

        return self._unipile_app.list_post_comments(
            post_id=post_id,
            account_id=self.account_id,
            comment_id=comment_id,
            cursor=cursor,
            limit=limit,
        )

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
