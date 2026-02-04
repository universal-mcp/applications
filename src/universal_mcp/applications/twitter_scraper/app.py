import os
from typing import Any

from loguru import logger

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class TwitterScraperApp(APIApplication):
    """
    Application for scraping Twitter/X data using Apify actors.
    Provides tools to scrape tweets from Twitter lists.
    """

    ACTOR_ID = "fastcrawler~twitter-x-list-tweets-scraper-0-35-1k-pay-per-result"

    def __init__(self, integration: Integration = None, **kwargs: Any) -> None:
        super().__init__(name="twitter_scraper", integration=integration, **kwargs)
        self.base_url = "https://api.apify.com/v2"

    def _get_api_token(self) -> str:
        """Get the Apify API token from environment variable."""
        api_token = os.getenv("APIFY_API_TOKEN")
        if not api_token:
            logger.error("TwitterScraperApp: APIFY_API_TOKEN environment variable is not set.")
            raise ValueError("TwitterScraperApp: APIFY_API_TOKEN environment variable is required.")
        return api_token

    async def list_tweets_scraper(
        self,
        list_id: str,
        max_items: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Scrapes tweets from a Twitter/X list using the Apify actor.
        Runs the actor synchronously and returns the dataset items (tweets).

        Args:
            list_id: The Twitter list ID to scrape tweets from. Example: '1944053485882028279'
            max_items: Maximum number of tweets to retrieve. Example: 10

        Returns:
            list[dict[str, Any]]: A list of tweet objects containing tweet data from the specified list.

        Raises:
            ValueError: Raised when list_id is missing or integration is not configured.
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).

        Tags:
            twitter, scraper, tweets, list, apify, important
        """
        if not list_id:
            raise ValueError("Missing required parameter 'list_id'.")

        api_token = self._get_api_token()

        url = f"{self.base_url}/acts/{self.ACTOR_ID}/run-sync-get-dataset-items"

        params = {"token": api_token}

        body = {
            "list_id": list_id,
            "maxItems": max_items,
        }

        logger.debug(f"Running Apify actor {self.ACTOR_ID} with list_id={list_id}, maxItems={max_items}")

        response = await self._apost(url, data=body, params=params)
        return self._handle_response(response)

    def list_tools(self):
        """Returns list of available tools."""
        return [
            self.list_tweets_scraper,
        ]
