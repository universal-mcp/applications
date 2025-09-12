import os
from dotenv import load_dotenv
load_dotenv()

from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.agentr.integration import AgentrIntegration
from universal_mcp.applications.unipile import UnipileApp
from typing import Any, Optional

class ScraperApp(APIApplication):
    """
    Application for interacting with LinkedIn API.
    Provides a simplified interface for LinkedIn search operations.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize the ScraperApp.

        Args:
            integration: The integration configuration containing credentials and other settings.
                         It is expected that the integration provides the necessary credentials
                         for LinkedIn API access.
        """
        super().__init__(name="scraper", **kwargs)
        if self.integration:
            credentials = self.integration.get_credentials()
            api_key = credentials.get("SCRAPER_API")
            self.account_id = credentials.get("ACCOUNT_ID")
            self.integration = AgentrIntegration(name="unipile", api_key=api_key, base_url="https://staging-agentr-306776579029.asia-southeast1.run.app/")
            self._unipile_app = UnipileApp(integration=self.integration)
        else:
            self.account_id = None
            self._unipile_app = None
        
    def linkedin_post_search(
        self,
        category: str = "posts",
        api: str = "classic",
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        keywords: Optional[str] = None,
        sort_by: Optional[str] = None,
        date_posted: Optional[str] = None,
        content_type: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Performs a LinkedIn search for posts.

        Args:
            category: Type of search to perform (defaults to "posts").
            api: Which LinkedIn API to use - "classic" or "sales_navigator".
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            sort_by: How to sort the results, e.g., "relevance" or "date".
            date_posted: Filter posts by when they were posted.
            content_type: Filter by the type of content in the post. Example: "videos", "images", "live_videos", "collaborative_articles", "documents"

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, search, posts, api, scrapper, important
        """
        
        return self._unipile_app.search(
            account_id=self.account_id,
            category=category,
            api=api,
            cursor=cursor,
            limit=limit,
            keywords=keywords,
            sort_by=sort_by,
            date_posted=date_posted,
            content_type=content_type,
        )

    def linkedin_list_all_posts(
        self,
        identifier: str,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> dict[str, Any]:
        """
        Lists all LinkedIn posts for a given user  identifier

        Args:
            identifier: The entity's provider internal ID (LinkedIn ID).starts with ACo for users, while for companies it's a series of numbers.
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (1-100, though spec allows up to 250).

        Returns:
            A dictionary containing a list of post objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, list, user_posts, company_posts, content, api, important
        """
        
        return self._unipile_app.list_user_posts(
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
        Retrieves a specific LinkedIn user profile by its identifier.

        Args:
            identifier: Can be the provider's internal id OR the provider's public id of the requested user.
                       For example, for https://www.linkedin.com/in/manojbajaj95/, the identifier is "manojbajaj95".

        Returns:
            A dictionary containing the user's profile details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, profile, retrieve, get, api, important
        """
        
        return self._unipile_app.retrieve_profile(
            identifier=identifier,
            account_id=self.account_id,
        )

 
    def linkedin_list_post_comments(
        self,
        post_id: str,
        comment_id: Optional[str] = None,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> dict[str, Any]:
        """
        Lists all comments from a specific LinkedIn post. Can also list replies to a specific comment.

        Args:
            post_id: The social ID of the post. Example rn:li:activity:7342082869034393600
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
            self.linkedin_post_search,
            self.linkedin_list_all_posts,
            self.linkedin_retrieve_profile,
            self.linkedin_list_post_comments,
            ]
