from typing import Any
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class TwitterApp(APIApplication):
    """Twitter API integration with essential day-to-day functions."""

    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="twitter", integration=integration, **kwargs)
        self.base_url = "https://api.twitter.com"

    @staticmethod
    def _prepare_params(params: dict) -> dict:
        """Convert list values to comma-separated strings for Twitter API."""
        prepared = {}
        for key, value in params.items():
            if isinstance(value, list):
                prepared[key] = ','.join(str(v) for v in value)
            else:
                prepared[key] = value
        return prepared

    # ==================== Tweet Operations ====================

    async def create_tweet(
        self,
        text: str = None,
        reply: dict = None,
        quote_tweet_id: str = None,
        media: dict = None,
        poll: dict = None,
        reply_settings: str = None,
    ) -> dict[str, Any]:
        """
        Posts a new tweet with text, media, polls, or as a reply/quote. Supports various tweet formats including replies, quotes, media attachments, and polls with customizable visibility settings.

        Args:
            text: The content of the Tweet. Example: 'Check out this amazing feature!'
            reply: Tweet information of the Tweet being replied to. Include 'in_reply_to_tweet_id' field.
            quote_tweet_id: ID of the tweet to quote. Example: '1346889436626259968'
            media: Media information being attached to the tweet. Include 'media_ids' array.
            poll: Poll options for a tweet with a poll. Include 'options' and 'duration_minutes'.
            reply_settings: Who can reply to the tweet. Options: 'mentionedUsers', 'following', or null for everyone.

        Returns:
            dict[str, Any]: Response containing the created tweet data including tweet ID.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            tweet, post, create, important
        """
        request_body_data = {
            "text": text,
            "reply": reply,
            "quote_tweet_id": quote_tweet_id,
            "media": media,
            "poll": poll,
            "reply_settings": reply_settings,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/2/tweets"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        response.raise_for_status()
        return response.json()

    async def delete_tweet(self, tweet_id: str) -> dict[str, Any]:
        """
        Permanently deletes a specific tweet by its unique ID on behalf of the authenticated user.
        This action cannot be undone and removes the tweet from all timelines.

        Args:
            tweet_id: The unique ID of the tweet to delete. Example: '1346889436626259968'

        Returns:
            dict[str, Any]: Confirmation response indicating successful deletion.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            tweet, delete, remove, important
        """
        if tweet_id is None:
            raise ValueError("Missing required parameter 'tweet_id'.")
        url = f"{self.base_url}/2/tweets/{tweet_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def get_tweet(
        self,
        tweet_id: str,
        tweet_fields: list = None,
        expansions: list = None,
        media_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves detailed information for a single tweet by its unique ID with customizable fields.
        Allows fetching tweet metrics, media details, author information, and more.

        Args:
            tweet_id: The unique ID of the tweet to retrieve. Example: '1346889436626259968'
            tweet_fields: Tweet fields to display. Example: ['created_at', 'public_metrics', 'text']
            expansions: Fields to expand. Example: ['author_id', 'attachments.media_keys']
            media_fields: Media fields to display. Example: ['url', 'preview_image_url', 'type']
            user_fields: User fields to display. Example: ['username', 'name', 'profile_image_url']

        Returns:
            dict[str, Any]: Detailed tweet data including requested fields and expansions.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            tweet, get, retrieve, important
        """
        if tweet_id is None:
            raise ValueError("Missing required parameter 'tweet_id'.")
        url = f"{self.base_url}/2/tweets/{tweet_id}"
        query_params = {
            k: v
            for k, v in [
                ("tweet.fields", tweet_fields),
                ("expansions", expansions),
                ("media.fields", media_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def search_recent_tweets(
        self,
        query: str,
        max_results: int = None,
        start_time: str = None,
        end_time: str = None,
        tweet_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Searches for tweets from the past seven days matching a specific query with filtering and pagination.
        Supports advanced Twitter search operators for precise results.
        NOTE: This endpoint requires elevated Twitter API access (Pro/Enterprise tier).

        Args:
            query: Search query string. Example: 'from:TwitterDev has:media -is:retweet'
            max_results: Maximum number of results to return (10-100). Default: 10
            start_time: Earliest timestamp for results. Example: '2021-02-01T18:40:40.000Z'
            end_time: Latest timestamp for results. Example: '2021-02-14T18:40:40.000Z'
            tweet_fields: Tweet fields to include. Example: ['created_at', 'public_metrics', 'author_id']
            user_fields: User fields to include. Example: ['username', 'name', 'verified']

        Returns:
            dict[str, Any]: Search results with matching tweets and pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            tweet, search, query, important, elevated_access_required
        """
        url = f"{self.base_url}/2/tweets/search/recent"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("max_results", max_results),
                ("start_time", start_time),
                ("end_time", end_time),
                ("tweet.fields", tweet_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    # ==================== User Operations ====================

    async def get_authenticated_user(
        self,
        user_fields: list = None,
        expansions: list = None,
        tweet_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves detailed information about the currently authenticated user making the API request.
        Returns profile data for the account whose credentials are being used.

        Args:
            user_fields: User fields to display. Example: ['created_at', 'description', 'public_metrics']
            expansions: Fields to expand. Example: ['pinned_tweet_id']
            tweet_fields: Tweet fields to display. Example: ['created_at', 'text']

        Returns:
            dict[str, Any]: Authenticated user's profile data and requested fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            user, profile, me, authenticated, important
        """
        url = f"{self.base_url}/2/users/me"
        query_params = {
            k: v
            for k, v in [
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def get_user_by_username(
        self,
        username: str,
        user_fields: list = None,
        expansions: list = None,
        tweet_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves detailed profile information for a specific user by their username (handle).
        Fetches public profile data and optionally includes pinned tweets and metrics.

        Args:
            username: Twitter username (handle) without the @ symbol. Example: 'TwitterDev'
            user_fields: User fields to display. Example: ['created_at', 'description', 'public_metrics']
            expansions: Fields to expand. Example: ['pinned_tweet_id']
            tweet_fields: Tweet fields to display. Example: ['created_at', 'public_metrics']

        Returns:
            dict[str, Any]: User profile data including requested fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            user, profile, lookup, important
        """
        if username is None:
            raise ValueError("Missing required parameter 'username'.")
        url = f"{self.base_url}/2/users/by/username/{username}"
        query_params = {
            k: v
            for k, v in [
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def get_user_by_id(
        self,
        user_id: str,
        user_fields: list = None,
        expansions: list = None,
        tweet_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves detailed profile information for a specific user by their unique user ID.
        Fetches public profile data and optionally includes pinned tweets and metrics.

        Args:
            user_id: Unique Twitter user ID. Example: '2244994945'
            user_fields: User fields to display. Example: ['created_at', 'description', 'public_metrics']
            expansions: Fields to expand. Example: ['pinned_tweet_id']
            tweet_fields: Tweet fields to display. Example: ['created_at', 'public_metrics']

        Returns:
            dict[str, Any]: User profile data including requested fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            user, profile, lookup, important
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/2/users/{user_id}"
        query_params = {
            k: v
            for k, v in [
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def search_users(
        self,
        query: str,
        max_results: int = None,
        user_fields: list = None,
        expansions: list = None,
    ) -> dict[str, Any]:
        """
        Searches for Twitter users matching a specific query string with pagination support.
        Finds users by username, display name, or bio keywords.
        NOTE: This endpoint requires elevated Twitter API access (Pro/Enterprise tier).

        Args:
            query: Search query to find users. Example: 'developer python'
            max_results: Maximum number of results to return (1-100). Default: 10
            user_fields: User fields to display. Example: ['description', 'public_metrics', 'verified']
            expansions: Fields to expand. Example: ['pinned_tweet_id']

        Returns:
            dict[str, Any]: List of matching users with their profile data.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            user, search, find, important, elevated_access_required
        """
        url = f"{self.base_url}/2/users/search"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("max_results", max_results),
                ("user.fields", user_fields),
                ("expansions", expansions),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    # ==================== Timeline Operations ====================

    async def get_user_tweets(
        self,
        user_id: str,
        max_results: int = None,
        exclude: list = None,
        start_time: str = None,
        end_time: str = None,
        tweet_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves tweets authored by a specific user in reverse chronological order with filtering options.
        Fetches original tweets, retweets, and replies based on exclude parameters.

        Args:
            user_id: The unique ID of the user. Example: '2244994945'
            max_results: Maximum number of results (5-100). Default: 10
            exclude: Tweet types to exclude. Example: ['retweets', 'replies']
            start_time: Earliest timestamp. Example: '2021-02-01T18:40:40.000Z'
            end_time: Latest timestamp. Example: '2021-02-14T18:40:40.000Z'
            tweet_fields: Tweet fields to include. Example: ['created_at', 'public_metrics']
            user_fields: User fields to include. Example: ['username', 'profile_image_url']

        Returns:
            dict[str, Any]: User's tweets with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            timeline, tweets, user, important
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/2/users/{user_id}/tweets"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("exclude", exclude),
                ("start_time", start_time),
                ("end_time", end_time),
                ("tweet.fields", tweet_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def get_user_mentions(
        self,
        user_id: str,
        max_results: int = None,
        start_time: str = None,
        end_time: str = None,
        tweet_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves tweets mentioning a specific user in reverse chronological order with time-based filtering.
        Finds all tweets that mention the user's @username.

        Args:
            user_id: The unique ID of the user. Example: '2244994945'
            max_results: Maximum number of results (5-100). Default: 10
            start_time: Earliest timestamp. Example: '2021-02-01T18:40:40.000Z'
            end_time: Latest timestamp. Example: '2021-02-14T18:40:40.000Z'
            tweet_fields: Tweet fields to include. Example: ['created_at', 'public_metrics', 'author_id']
            user_fields: User fields to include. Example: ['username', 'name']

        Returns:
            dict[str, Any]: Tweets mentioning the user with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            mentions, timeline, user, important
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/2/users/{user_id}/mentions"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("start_time", start_time),
                ("end_time", end_time),
                ("tweet.fields", tweet_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    # ==================== Social Interactions ====================

    async def like_tweet(self, tweet_id: str) -> dict[str, Any]:
        """
        Causes the authenticated user to like a specific tweet by its ID.
        Adds the tweet to the user's liked tweets and notifies the tweet author.

        Args:
            user_id: The unique ID of the user performing the like. Example: '2244994945'
            tweet_id: The unique ID of the tweet to like. Example: '1346889436626259968'

        Returns:
            dict[str, Any]: Confirmation response indicating the like was successful.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            like, favorite, engagement, important
        """
        
        user = await self.get_authenticated_user()
        user_id = user.get("data", {}).get("id")
        request_body_data = {"tweet_id": tweet_id}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/2/users/{user_id}/likes"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        response.raise_for_status()
        return response.json()

    async def unlike_tweet(self, tweet_id: str) -> dict[str, Any]:
        """
        Removes a like from a tweet on behalf of the authenticated user.
        Reverses a previous like action and removes the tweet from liked tweets.

        Args:
            user_id: The unique ID of the user removing the like. Example: '2244994945'
            tweet_id: The unique ID of the tweet to unlike. Example: '1346889436626259968'

        Returns:
            dict[str, Any]: Confirmation response indicating the unlike was successful.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            unlike, unfavorite, engagement, important
        """
        user = await self.get_authenticated_user()
        user_id = user.get("data", {}).get("id")
        url = f"{self.base_url}/2/users/{user_id}/likes/{tweet_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def get_liked_tweets(
        self,
        max_results: int = None,
        tweet_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves tweets liked by a specific user in reverse chronological order with pagination.
        Shows the user's like history with customizable field selections.

        Args:
            max_results: Maximum number of results (5-100). Default: 10
            tweet_fields: Tweet fields to include. Example: ['created_at', 'public_metrics', 'author_id']
            user_fields: User fields to include. Example: ['username', 'name']

        Returns:
            dict[str, Any]: List of liked tweets with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            likes, favorites, user, important
        """
        user = await self.get_authenticated_user()
        user_id = user.get("data", {}).get("id")
        url = f"{self.base_url}/2/users/{user_id}/liked_tweets"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("tweet.fields", tweet_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def retweet(self, tweet_id: str) -> dict[str, Any]:
        """
        Causes the authenticated user to retweet a specific tweet by its ID.
        Shares the tweet to the user's followers and appears on their timeline.

        Args:
            user_id: The unique ID of the user performing the retweet. Example: '2244994945'
            tweet_id: The unique ID of the tweet to retweet. Example: '1346889436626259968'

        Returns:
            dict[str, Any]: Confirmation response indicating the retweet was successful.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            retweet, share, engagement, important
        """
        user = await self.get_authenticated_user()
        user_id = user.get("data", {}).get("id")
        request_body_data = {"tweet_id": tweet_id}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/2/users/{user_id}/retweets"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        response.raise_for_status()
        return response.json()

    async def unretweet(self, tweet_id: str) -> dict[str, Any]:
        """
        Removes a retweet from the authenticated user's timeline.
        Reverses a previous retweet action and removes it from the user's profile.

        Args:
            user_id: The unique ID of the user removing the retweet. Example: '2244994945'
            tweet_id: The unique ID of the original tweet that was retweeted. Example: '1346889436626259968'

        Returns:
            dict[str, Any]: Confirmation response indicating the unretweet was successful.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            unretweet, undo, engagement, important
        """
        user = await self.get_authenticated_user()
        user_id = user.get("data", {}).get("id")
        url = f"{self.base_url}/2/users/{user_id}/retweets/{tweet_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def get_retweeters(
        self,
        tweet_id: str,
        max_results: int = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of users who retweeted a specific tweet with pagination support.
        Shows who amplified the tweet with customizable user field selections.

        Args:
            tweet_id: The unique ID of the tweet. Example: '1346889436626259968'
            max_results: Maximum number of results (1-100). Default: 100
            user_fields: User fields to include. Example: ['username', 'public_metrics', 'verified']

        Returns:
            dict[str, Any]: List of users who retweeted with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            retweet, users, engagement
        """
        if tweet_id is None:
            raise ValueError("Missing required parameter 'tweet_id'.")
        url = f"{self.base_url}/2/tweets/{tweet_id}/retweeted_by"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def get_liking_users(
        self,
        tweet_id: str,
        max_results: int = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of users who liked a specific tweet with pagination support.
        Shows who engaged with the tweet through likes with customizable user fields.

        Args:
            tweet_id: The unique ID of the tweet. Example: '1346889436626259968'
            max_results: Maximum number of results (1-100). Default: 100
            user_fields: User fields to include. Example: ['username', 'public_metrics', 'verified']

        Returns:
            dict[str, Any]: List of users who liked the tweet with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            like, users, engagement
        """
        if tweet_id is None:
            raise ValueError("Missing required parameter 'tweet_id'.")
        url = f"{self.base_url}/2/tweets/{tweet_id}/liking_users"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    # ==================== Follow Operations ====================

    async def follow_user(self, user_id: str, target_user_id: str) -> dict[str, Any]:
        """
        Causes the authenticated user to follow another user by their user ID.
        Creates a following relationship and adds the target to the user's following list.

        Args:
            user_id: The unique ID of the user performing the follow. Example: '2244994945'
            target_user_id: The unique ID of the user to follow. Example: '6253282'

        Returns:
            dict[str, Any]: Confirmation response with following status.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            follow, user, relationship, important
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        request_body_data = {"target_user_id": target_user_id}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/2/users/{user_id}/following"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        response.raise_for_status()
        return response.json()

    async def unfollow_user(self, user_id: str, target_user_id: str) -> dict[str, Any]:
        """
        Causes the authenticated user to unfollow another user by their user ID.
        Removes the following relationship and stops seeing their tweets in the timeline.

        Args:
            user_id: The unique ID of the user performing the unfollow. Example: '2244994945'
            target_user_id: The unique ID of the user to unfollow. Example: '6253282'

        Returns:
            dict[str, Any]: Confirmation response with unfollowing status.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            unfollow, user, relationship, important
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        if target_user_id is None:
            raise ValueError("Missing required parameter 'target_user_id'.")
        url = f"{self.base_url}/2/users/{user_id}/following/{target_user_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def get_followers(
        self,
        user_id: str,
        max_results: int = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of users who follow a specific user.
        Shows the user's follower base with customizable user field selections.
        NOTE: This endpoint requires elevated Twitter API access (Pro/Enterprise tier).

        Args:
            user_id: The unique ID of the user. Example: '2244994945'
            max_results: Maximum number of results (1-1000). Default: 100
            user_fields: User fields to include. Example: ['username', 'description', 'public_metrics']

        Returns:
            dict[str, Any]: List of followers with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            followers, users, relationship, important, elevated_access_required
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/2/users/{user_id}/followers"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def get_following(
        self,
        user_id: str,
        max_results: int = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of users that a specific user is following.
        Shows who the user follows with customizable user field selections.
        NOTE: This endpoint requires elevated Twitter API access (Pro/Enterprise tier).

        Args:
            user_id: The unique ID of the user. Example: '2244994945'
            max_results: Maximum number of results (1-1000). Default: 100
            user_fields: User fields to include. Example: ['username', 'description', 'public_metrics']

        Returns:
            dict[str, Any]: List of following users with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            following, users, relationship, important, elevated_access_required
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/2/users/{user_id}/following"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    # ==================== Direct Messages ====================

    async def send_dm(
        self,
        participant_id: str,
        text: str = None,
        attachments: list = None,
    ) -> dict[str, Any]:
        """
        Sends a direct message to a user by their participant ID.
        Creates a new one-on-one conversation or appends to an existing conversation.

        Args:
            participant_id: The unique ID of the user to message. Example: '2244994945'
            text: The text content of the direct message. Example: 'Hello, how are you?'
            attachments: Optional media attachments. Array of media objects with media_id.

        Returns:
            dict[str, Any]: Confirmation response with DM event details.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            dm, message, send, important
        """
        if participant_id is None:
            raise ValueError("Missing required parameter 'participant_id'.")
        request_body_data = {"attachments": attachments, "text": text}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/2/dm_conversations/with/{participant_id}/messages"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        response.raise_for_status()
        return response.json()

    async def get_dm_events(
        self,
        max_results: int = None,
        event_types: list = None,
        dm_event_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of direct message events for the authenticated user with pagination.
        Shows DM conversations with filtering by event type and customizable field selections.

        Args:
            max_results: Maximum number of results to return (1-100). Default: 100
            event_types: Event types to filter by. Example: ['MessageCreate', 'ParticipantsJoin']
            dm_event_fields: DM event fields to include. Example: ['created_at', 'text', 'sender_id']
            user_fields: User fields to include. Example: ['username', 'name', 'profile_image_url']

        Returns:
            dict[str, Any]: List of DM events with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            dm, messages, list, important
        """
        url = f"{self.base_url}/2/dm_events"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("event_types", event_types),
                ("dm_event.fields", dm_event_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    # ==================== Bookmarks ====================

    async def bookmark_tweet(self, user_id: str, tweet_id: str) -> dict[str, Any]:
        """
        Bookmarks a specific tweet for the authenticated user for later reference.
        Saves the tweet to the user's private bookmarks collection.

        Args:
            user_id: The unique ID of the user creating the bookmark. Example: '2244994945'
            tweet_id: The unique ID of the tweet to bookmark. Example: '1346889436626259968'

        Returns:
            dict[str, Any]: Confirmation response with bookmark status.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            bookmark, save, important
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        request_body_data = {"tweet_id": tweet_id}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/2/users/{user_id}/bookmarks"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        response.raise_for_status()
        return response.json()

    async def remove_bookmark(self, user_id: str, tweet_id: str) -> dict[str, Any]:
        """
        Removes a bookmarked tweet from the authenticated user's bookmarks collection.
        Reverses a previous bookmark action and removes the saved tweet.

        Args:
            user_id: The unique ID of the user removing the bookmark. Example: '2244994945'
            tweet_id: The unique ID of the bookmarked tweet to remove. Example: '1346889436626259968'

        Returns:
            dict[str, Any]: Confirmation response with unbookmark status.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            bookmark, remove, delete, important
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        if tweet_id is None:
            raise ValueError("Missing required parameter 'tweet_id'.")
        url = f"{self.base_url}/2/users/{user_id}/bookmarks/{tweet_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def get_bookmarks(
        self,
        user_id: str,
        max_results: int = None,
        tweet_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves all bookmarked tweets for the authenticated user with pagination support.
        Shows the user's saved tweets with customizable field selections.

        Args:
            user_id: The unique ID of the user. Example: '2244994945'
            max_results: Maximum number of results (1-100). Default: 100
            tweet_fields: Tweet fields to include. Example: ['created_at', 'public_metrics', 'author_id']
            user_fields: User fields to include. Example: ['username', 'name']

        Returns:
            dict[str, Any]: List of bookmarked tweets with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            bookmarks, saved, list, important
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.base_url}/2/users/{user_id}/bookmarks"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("tweet.fields", tweet_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    # ==================== Lists ====================

    async def create_list(
        self,
        name: str = None,
        description: str = None,
        private: bool = None,
    ) -> dict[str, Any]:
        """
        Creates a new Twitter list with customizable name, description, and privacy settings.
        Allows organizing users into curated groups for focused timelines.

        Args:
            name: The name of the list to create. Example: 'Tech Influencers'
            description: Optional description of the list. Example: 'Leading voices in technology'
            private: Whether the list should be private (true) or public (false). Default: false

        Returns:
            dict[str, Any]: The newly created list data including list ID.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            list, create, important
        """
        request_body_data = {"name": name, "description": description, "private": private}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/2/lists"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        response.raise_for_status()
        return response.json()

    async def get_list(
        self,
        list_id: str,
        list_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves detailed information for a specific Twitter list by its unique ID.
        Fetches list metadata including name, description, owner, and member count.

        Args:
            list_id: The unique ID of the list. Example: '84839422'
            list_fields: List fields to include. Example: ['description', 'member_count', 'follower_count']
            user_fields: Owner user fields to include. Example: ['username', 'name', 'verified']

        Returns:
            dict[str, Any]: List data with requested fields.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            list, get, retrieve, important
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'.")
        url = f"{self.base_url}/2/lists/{list_id}"
        query_params = {
            k: v
            for k, v in [
                ("list.fields", list_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    async def get_list_tweets(
        self,
        list_id: str,
        max_results: int = None,
        tweet_fields: list = None,
        user_fields: list = None,
    ) -> dict[str, Any]:
        """
        Retrieves tweets from a specific Twitter list's timeline in reverse chronological order.
        Shows tweets from all list members with pagination and customizable fields.

        Args:
            list_id: The unique ID of the list. Example: '84839422'
            max_results: Maximum number of results (1-100). Default: 100
            tweet_fields: Tweet fields to include. Example: ['created_at', 'public_metrics', 'author_id']
            user_fields: User fields to include. Example: ['username', 'name', 'verified']

        Returns:
            dict[str, Any]: List timeline tweets with pagination tokens.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            list, tweets, timeline, important
        """
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'.")
        url = f"{self.base_url}/2/lists/{list_id}/tweets"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("tweet.fields", tweet_fields),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        query_params = self._prepare_params(query_params) if query_params else {}
        response = await self._aget(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        """Returns list of available Twitter API tools for standard access level.

        Note: Some methods requiring elevated API access are not included here but
        remain available programmatically:
        - search_recent_tweets (requires elevated access)
        - search_users (requires elevated access)
        - get_followers (requires elevated access)
        - get_following (requires elevated access)
        """
        return [
            # Tweet Operations
            self.create_tweet,
            self.delete_tweet,
            self.get_tweet,
            # User Operations
            self.get_authenticated_user,
            self.get_user_by_username,
            self.get_user_by_id,
            # Timeline Operations
            self.get_user_tweets,
            self.get_user_mentions,
            # Social Interactions
            self.like_tweet,
            self.unlike_tweet,
            self.get_liked_tweets,
            self.retweet,
            self.unretweet,
            self.get_retweeters,
            self.get_liking_users,
            # Follow Operations
            self.follow_user,
            self.unfollow_user,
            # Direct Messages
            self.send_dm,
            self.get_dm_events,
            # Bookmarks
            self.bookmark_tweet,
            self.remove_bookmark,
            self.get_bookmarks,
            # Lists
            self.create_list,
            self.get_list,
            self.get_list_tweets,
        ]
