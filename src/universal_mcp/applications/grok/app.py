import asyncio
from typing import Any, Optional

from loguru import logger
from pydantic import BaseModel

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class Engagement(BaseModel):
    likes: int
    reposts: int
    views: int


class Tweet(BaseModel):
    id: str
    date: str
    content: str
    url: str
    has_media: bool
    engagement: Engagement
    is_thread_reply: bool
    thread_parent_id: Optional[str] = None


class UserResults(BaseModel):
    username: str
    tweets: list[Tweet]


class Results(BaseModel):
    users: list[UserResults]


class GrokApp(APIApplication):
    """
    Grok (xAI) integration for AI-powered X/Twitter search and structured data extraction.
    Fetch recent tweets from X users and search X posts using Grok's real-time x_search tool.
    Leverages Grok's structured output parsing to return clean, type-safe tweet data.
    Ideal for social media monitoring, competitive research, influencer tracking, and X content analysis.
    """

    def __init__(self, integration: Integration = None, **kwargs: Any) -> None:
        super().__init__(name="grok", integration=integration, **kwargs)

    async def _get_client(self):
        """Instantiate an xAI client using credentials from the integration."""
        from xai_sdk import Client

        credentials = await self.integration.get_credentials_async()
        api_key = credentials.get("api_key")
        if not api_key:
            raise ValueError("api_key is missing from Grok integration credentials")
        return Client(api_key=api_key)

    async def get_user_tweets(
        self,
        usernames: list[str],
        max_tweets: int = 5,
        model: str = "grok-4-1-fast",
    ) -> list[dict[str, Any]]:
        """
        Fetches the most recent tweets from one or more X (Twitter) users using Grok's x_search tool.
        Returns structured tweet data including engagement metrics, media presence, and thread context.

        Args:
            usernames: List of X usernames to fetch tweets from (with or without @). Example: ['elonmusk', 'satyanadella']
            max_tweets: Maximum number of tweets to retrieve per user. Example: 5
            model: Grok model to use for structured extraction. Example: 'grok-4-1-fast'

        Returns:
            list[dict[str, Any]]: List of per-user results, each containing 'username' and a 'tweets' list.
                Each tweet has 'id', 'date', 'content', 'url', 'has_media', 'engagement' (likes/reposts/views),
                'is_thread_reply', and optionally 'thread_parent_id'.

        Raises:
            ValueError: Raised when usernames is empty or credentials are missing.

        Tags:
            grok, x, twitter, tweets, search, scraper, important
        """
        if not usernames:
            raise ValueError("Missing required parameter 'usernames'.")

        client = await self._get_client()

        handles = " and ".join(f"@{u.lstrip('@')}" for u in usernames)
        prompt = f"Get the last {max_tweets} tweets from {handles}"

        logger.debug(f"Fetching tweets for {handles} using model={model}")

        def _run() -> list[dict[str, Any]]:
            from xai_sdk.chat import user as xai_user
            from xai_sdk.tools import x_search

            chat = client.chat.create(model=model, tools=[x_search()])
            chat.append(xai_user(prompt))
            _, result = chat.parse(Results)
            return result.model_dump()["users"]

        return await asyncio.to_thread(_run)

    def list_tools(self):
        """Returns list of available tools."""
        return [
            self.get_user_tweets,
        ]
