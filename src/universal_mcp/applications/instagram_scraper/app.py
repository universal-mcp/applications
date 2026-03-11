from typing import Any

from loguru import logger

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class InstagramScraperApp(APIApplication):
    """
    Application for scraping Instagram data using Apify actors.
    Provides tools to scrape Instagram posts from Instagram accounts.
    """

    ACTOR_ID = "apify~instagram-post-scraper"

    def __init__(self, integration: Integration = None, **kwargs: Any) -> None:
        super().__init__(name="instagram_scraper", integration=integration, **kwargs)
        self.base_url = "https://api.apify.com/v2"

    async def _get_api_token(self) -> str:
        """Get the Apify API token from environment variable."""
        credentials = await self.integration.get_credentials_async()
        api_token = credentials.get("token")
        if not api_token:
            raise ValueError("token is missing")
        return api_token

    async def instagram_posts_scraper(
        self,
        username: list[str],
        results_limit: int = 15,
        skip_pinned_posts: bool = False,
        data_detail_level: str = "basicData",
    ) -> list[dict[str, Any]]:
        """
        Scrapes Instagram posts from specified accounts.

        Args:
            username: List of Instagram usernames to scrape posts from. Example: ['airesearches']
            results_limit: Maximum number of posts to retrieve per account. Example: 15
            skip_pinned_posts: Whether to skip pinned posts. Example: False
            data_detail_level: Level of detail for returned data. Example: 'basicData'

        Returns:
            list[dict[str, Any]]: A list of post objects containing Instagram post data from the specified accounts.

        Raises:
            ValueError: Raised when username is missing or integration is not configured.
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).

        Tags:
            instagram, scraper, posts, apify, important
        """
        if not username:
            raise ValueError("Missing required parameter 'username'.")

        api_token = await self._get_api_token()

        url = f"{self.base_url}/acts/{self.ACTOR_ID}/run-sync-get-dataset-items"

        params = {"token": api_token}

        body = {
            "dataDetailLevel": data_detail_level,
            "resultsLimit": results_limit,
            "skipPinnedPosts": skip_pinned_posts,
            "username": username,
        }

        logger.debug(f"Running Apify actor {self.ACTOR_ID} with username={username}, resultsLimit={results_limit}")

        response = await self._apost(url, data=body, params=params)
        return self._handle_response(response)

    def list_tools(self):
        """Returns list of available tools."""
        return [
            self.instagram_posts_scraper,
        ]
