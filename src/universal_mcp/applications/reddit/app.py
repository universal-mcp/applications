from typing import Any

import httpx
from loguru import logger

from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError
from universal_mcp.integrations import Integration


class RedditApp(APIApplication):
    def __init__(self, integration: Integration) -> None:
        super().__init__(name="reddit", integration=integration)
        self.base_api_url = "https://oauth.reddit.com"
        self.base_url = "https://oauth.reddit.com"

    def _post(self, url, data):
        try:
            headers = self._get_headers()
            response = httpx.post(url, headers=headers, data=data)
            response.raise_for_status()
            return response
        except NotAuthorizedError as e:
            logger.warning(f"Authorization needed: {e.message}")
            raise e
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                return e.response.text or "Rate limit exceeded. Please try again later."
            else:
                raise e
        except Exception as e:
            logger.error(f"Error posting {url}: {e}")
            raise e

    def _get_headers(self):
        if not self.integration:
            raise ValueError("Integration not configured for RedditApp")
        credentials = self.integration.get_credentials()
        if "access_token" not in credentials:
            logger.error("Reddit credentials found but missing 'access_token'.")
            raise ValueError("Invalid Reddit credentials format.")

        return {
            "Authorization": f"Bearer {credentials['access_token']}",
            "User-Agent": "agentr-reddit-app/0.1 by AgentR",
        }

    def get_subreddit_posts(
        self, subreddit: str, limit: int = 5, timeframe: str = "day"
    ) -> dict[str, Any]:
        """
        Fetches top posts from a given subreddit, filterable by time.

        Args:
            subreddit: The name of the subreddit (e.g., 'python', 'worldnews') without the 'r/' prefix
            limit: The maximum number of posts to return (default: 5, max: 100)
            timeframe: The time period for top posts. Valid options: 'hour', 'day', 'week', 'month', 'year', 'all' (default: 'day')

        Returns:
            A formatted string containing a numbered list of top posts, including titles, authors, scores, and URLs, or an error message if the request fails

        Raises:
            RequestException: When the HTTP request to the Reddit API fails
            JSONDecodeError: When the API response contains invalid JSON

        Tags:
            fetch, reddit, api, list, social-media, important, read-only
        """
        valid_timeframes = ["hour", "day", "week", "month", "year", "all"]
        if timeframe not in valid_timeframes:
            return f"Error: Invalid timeframe '{timeframe}'. Please use one of: {', '.join(valid_timeframes)}"
        if not 1 <= limit <= 100:
            return (
                f"Error: Invalid limit '{limit}'. Please use a value between 1 and 100."
            )
        url = f"{self.base_api_url}/r/{subreddit}/top"
        params = {"limit": limit, "t": timeframe}
        logger.info(
            f"Requesting top {limit} posts from r/{subreddit} for timeframe '{timeframe}'"
        )
        response = self._get(url, params=params)
        return self._handle_response(response)

    def search_subreddits(
        self, query: str, limit: int = 5, sort: str = "relevance"
    ) -> str:
        """
        Searches Reddit for subreddits matching a given query string and returns a formatted list of results including subreddit names, subscriber counts, and descriptions.

        Args:
            query: The text to search for in subreddit names and descriptions
            limit: The maximum number of subreddits to return, between 1 and 100 (default: 5)
            sort: The order of results, either 'relevance' or 'activity' (default: 'relevance')

        Returns:
            A formatted string containing a list of matching subreddits with their names, subscriber counts, and descriptions, or an error message if the search fails or parameters are invalid

        Raises:
            RequestException: When the HTTP request to Reddit's API fails
            JSONDecodeError: When the API response contains invalid JSON

        Tags:
            search, important, reddit, api, query, format, list, validation
        """
        valid_sorts = ["relevance", "activity"]
        if sort not in valid_sorts:
            return f"Error: Invalid sort option '{sort}'. Please use one of: {', '.join(valid_sorts)}"
        if not 1 <= limit <= 100:
            return (
                f"Error: Invalid limit '{limit}'. Please use a value between 1 and 100."
            )
        url = f"{self.base_api_url}/subreddits/search"
        params = {
            "q": query,
            "limit": limit,
            "sort": sort,
        }
        logger.info(
            f"Searching for subreddits matching '{query}' (limit: {limit}, sort: {sort})"
        )
        response = self._get(url, params=params)
        return self._handle_response(response)

    def get_post_flairs(self, subreddit: str):
        """
        Retrieves a list of available post flairs for a specified subreddit using the Reddit API.

        Args:
            subreddit: The name of the subreddit (e.g., 'python', 'worldnews') without the 'r/' prefix

        Returns:
            A list of dictionaries containing flair details if flairs exist, or a string message indicating no flairs are available

        Raises:
            RequestException: When the API request fails or network connectivity issues occur
            JSONDecodeError: When the API response contains invalid JSON data

        Tags:
            fetch, get, reddit, flair, api, read-only
        """
        url = f"{self.base_api_url}/r/{subreddit}/api/link_flair_v2"
        logger.info(f"Fetching post flairs for subreddit: r/{subreddit}")
        response = self._get(url)
        flairs = response.json()
        if not flairs:
            return f"No post flairs available for r/{subreddit}."
        return flairs

    def create_post(
        self,
        subreddit: str,
        title: str,
        kind: str = "self",
        text: str = None,
        url: str = None,
        flair_id: str = None,
    ):
        """
        Creates a new Reddit post in a specified subreddit with support for text posts, link posts, and image posts

        Args:
            subreddit: The name of the subreddit (e.g., 'python', 'worldnews') without the 'r/'
            title: The title of the post
            kind: The type of post; either 'self' (text post) or 'link' (link or image post)
            text: The text content of the post; required if kind is 'self'
            url: The URL of the link or image; required if kind is 'link'. Must end with valid image extension for image posts
            flair_id: The ID of the flair to assign to the post

        Returns:
            The JSON response from the Reddit API, or an error message as a string if the API returns an error

        Raises:
            ValueError: Raised when kind is invalid or when required parameters (text for self posts, url for link posts) are missing

        Tags:
            create, post, social-media, reddit, api, important
        """
        if kind not in ["self", "link"]:
            raise ValueError("Invalid post kind. Must be one of 'self' or 'link'.")
        if kind == "self" and not text:
            raise ValueError("Text content is required for text posts.")
        if kind == "link" and not url:
            raise ValueError("URL is required for link posts (including images).")
        data = {
            "sr": subreddit,
            "title": title,
            "kind": kind,
            "text": text,
            "url": url,
            "flair_id": flair_id,
        }
        data = {k: v for k, v in data.items() if v is not None}
        url_api = f"{self.base_api_url}/api/submit"
        logger.info(f"Submitting a new post to r/{subreddit}")
        response = self._post(url_api, data=data)
        response_json = response.json()
        if (
            response_json
            and "json" in response_json
            and "errors" in response_json["json"]
        ):
            errors = response_json["json"]["errors"]
            if errors:
                error_message = ", ".join(
                    [f"{code}: {message}" for code, message in errors]
                )
                return f"Reddit API error: {error_message}"
        return response_json

    def get_comment_by_id(self, comment_id: str) -> dict:
        """
        Retrieves a specific Reddit comment using its unique identifier.

        Args:
            comment_id: The full unique identifier of the comment (prefixed with 't1_', e.g., 't1_abcdef')

        Returns:
            A dictionary containing the comment data including attributes like author, body, score, etc. If the comment is not found, returns a dictionary with an error message.

        Raises:
            HTTPError: When the Reddit API request fails due to network issues or invalid authentication
            JSONDecodeError: When the API response cannot be parsed as valid JSON

        Tags:
            retrieve, get, reddit, comment, api, fetch, single-item, important
        """
        url = f"https://oauth.reddit.com/api/info.json?id={comment_id}"
        response = self._get(url)
        data = response.json()
        comments = data.get("data", {}).get("children", [])
        if comments:
            return comments[0]["data"]
        else:
            return {"error": "Comment not found."}

    def post_comment(self, parent_id: str, text: str) -> dict:
        """
        Posts a comment to a Reddit post or comment using the Reddit API

        Args:
            parent_id: The full ID of the parent comment or post (e.g., 't3_abc123' for a post, 't1_def456' for a comment)
            text: The text content of the comment to be posted

        Returns:
            A dictionary containing the Reddit API response with details about the posted comment

        Raises:
            RequestException: If the API request fails or returns an error status code
            JSONDecodeError: If the API response cannot be parsed as JSON

        Tags:
            post, comment, social, reddit, api, important
        """
        url = f"{self.base_api_url}/api/comment"
        data = {
            "parent": parent_id,
            "text": text,
        }
        logger.info(f"Posting comment to {parent_id}")
        response = self._post(url, data=data)
        return response.json()

    def edit_content(self, content_id: str, text: str) -> dict:
        """
        Edits the text content of an existing Reddit post or comment using the Reddit API

        Args:
            content_id: The full ID of the content to edit (e.g., 't3_abc123' for a post, 't1_def456' for a comment)
            text: The new text content to replace the existing content

        Returns:
            A dictionary containing the API response with details about the edited content

        Raises:
            RequestException: When the API request fails or network connectivity issues occur
            ValueError: When invalid content_id format or empty text is provided

        Tags:
            edit, update, content, reddit, api, important
        """
        url = f"{self.base_api_url}/api/editusertext"
        data = {
            "thing_id": content_id,
            "text": text,
        }
        logger.info(f"Editing content {content_id}")
        response = self._post(url, data=data)
        return response.json()

    def delete_content(self, content_id: str) -> dict:
        """
        Deletes a specified Reddit post or comment using the Reddit API.

        Args:
            content_id: The full ID of the content to delete (e.g., 't3_abc123' for a post, 't1_def456' for a comment)

        Returns:
            A dictionary containing a success message with the deleted content ID

        Raises:
            HTTPError: When the API request fails or returns an error status code
            RequestException: When there are network connectivity issues or API communication problems

        Tags:
            delete, content-management, api, reddit, important
        """
        url = f"{self.base_api_url}/api/del"
        data = {
            "id": content_id,
        }
        logger.info(f"Deleting content {content_id}")
        response = self._post(url, data=data)
        response.raise_for_status()
        return {"message": f"Content {content_id} deleted successfully."}

    def get_current_user_info(self) -> Any:
        """
        Get the current user's information.
        Returns:
            Any: API response data.

        Tags:
            users
        """
        url = f"{self.base_url}/api/v1/me"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_current_user_karma(self) -> Any:
        """
        Get the current user's karma.

        Returns:
            Any: API response data.

        Tags:
            account
        """
        url = f"{self.base_url}/api/v1/me/karma"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_post_comments_details(self, post_id: str) -> Any:
        """
        Get post details and comments like title, author, score, etc.

        Args:
            post_id (string): The Reddit post ID ( e.g. '1m734tx' for https://www.reddit.com/r/mcp/comments/1m734tx/comment/n4occ77/)

        Returns:
            Any: API response data containing post details and comments.

        Tags:
            listings, comments, posts, important
        """

        url = f"{self.base_url}/comments/{post_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_controversial_posts(
        self,
        after: str = None,
        before: str = None,
        count: int = None,
        limit: int = None,
        show: str = None,
        sr_detail: str = None,
    ) -> Any:
        """
        Retrieves a list of the most controversial posts across Reddit.

        Args:
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            show: Optional. The string "all" to show all posts.
            sr_detail: Optional. Expand subreddit details.

        Returns:
            Any: API response data containing a list of controversial posts.

        Tags:
            listings, posts, controversial, read-only
        """
        url = f"{self.base_url}/controversial"
        query_params = {
            k: v
            for k, v in [
                ("after", after),
                ("before", before),
                ("count", count),
                ("limit", limit),
                ("show", show),
                ("sr_detail", sr_detail),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_hot_posts(
        self,
        g: str = None,
        after: str = None,
        before: str = None,
        count: int = None,
        limit: int = None,
        show: str = None,
        sr_detail: str = None,
    ) -> Any:
        """
        Retrieves a list of the hottest posts across Reddit.

        Args:
            g: Optional. A geographical region to filter posts by (e.g., 'GLOBAL', 'US', 'GB').
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            show: Optional. The string "all" to show all posts.
            sr_detail: Optional. Expand subreddit details.

        Returns:
            Any: API response data containing a list of hot posts.

        Tags:
            listings, posts, hot, read-only
        """
        url = f"{self.base_url}/hot"
        query_params = {
            k: v
            for k, v in [
                ("g", g),
                ("after", after),
                ("before", before),
                ("count", count),
                ("limit", limit),
                ("show", show),
                ("sr_detail", sr_detail),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_new_posts(
        self,
        after: str = None,
        before: str = None,
        count: int = None,
        limit: int = None,
        show: str = None,
        sr_detail: str = None,
    ) -> Any:
        """
        Retrieves a list of the newest posts across Reddit.

        Args:
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            show: Optional. The string "all" to show all posts.
            sr_detail: Optional. Expand subreddit details.

        Returns:
            Any: API response data containing a list of new posts.

        Tags:
            listings, posts, new, read-only
        """
        url = f"{self.base_url}/new"
        query_params = {
            k: v
            for k, v in [
                ("after", after),
                ("before", before),
                ("count", count),
                ("limit", limit),
                ("show", show),
                ("sr_detail", sr_detail),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_subreddit_hot_posts(
        self,
        subreddit: str,
        g: str = None,
        after: str = None,
        before: str = None,
        count: int = None,
        limit: int = None,
        show: str = None,
        sr_detail: str = None,
    ) -> Any:
        """
        Retrieves a list of the hottest posts in a specified subreddit.

        Args:
            subreddit: The name of the subreddit (e.g., 'python', 'worldnews') without the 'r/' prefix.
            g: Optional. A geographical region to filter posts by (e.g., 'GLOBAL', 'US', 'GB').
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            show: Optional. The string "all" to show all posts.
            sr_detail: Optional. Expand subreddit details.

        Returns:
            Any: API response data containing a list of hot posts from the subreddit.

        Tags:
            listings, posts, subreddit, hot, read-only
        """
        if subreddit is None:
            raise ValueError("Missing required parameter 'subreddit'")
        url = f"{self.base_url}/r/{subreddit}/hot"
        query_params = {
            k: v
            for k, v in [
                ("g", g),
                ("after", after),
                ("before", before),
                ("count", count),
                ("limit", limit),
                ("show", show),
                ("sr_detail", sr_detail),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_subreddit_new_posts(
        self,
        subreddit: str,
        after: str = None,
        before: str = None,
        count: int = None,
        limit: int = None,
        show: str = None,
        sr_detail: str = None,
    ) -> Any:
        """
        Retrieves a list of the newest posts in a specified subreddit.

        Args:
            subreddit: The name of the subreddit (e.g., 'python', 'worldnews') without the 'r/' prefix.
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            show: Optional. The string "all" to show all posts.
            sr_detail: Optional. Expand subreddit details.

        Returns:
            Any: API response data containing a list of new posts from the subreddit.

        Tags:
            listings, posts, subreddit, new, read-only
        """
        if subreddit is None:
            raise ValueError("Missing required parameter 'subreddit'")
        url = f"{self.base_url}/r/{subreddit}/new"
        query_params = {
            k: v
            for k, v in [
                ("after", after),
                ("before", before),
                ("count", count),
                ("limit", limit),
                ("show", show),
                ("sr_detail", sr_detail),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_subreddit_top_posts(
        self,
        subreddit: str,
        after: str = None,
        before: str = None,
        count: int = None,
        limit: int = None,
        show: str = None,
        sr_detail: str = None,
    ) -> Any:
        """
        Retrieves a list of the top posts in a specified subreddit.

        Args:
            subreddit: The name of the subreddit (e.g., 'python', 'worldnews') without the 'r/' prefix.
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            show: Optional. The string "all" to show all posts.
            sr_detail: Optional. Expand subreddit details.

        Returns:
            Any: API response data containing a list of top posts from the subreddit.

        Tags:
            listings, posts, subreddit, top, read-only
        """
        if subreddit is None:
            raise ValueError("Missing required parameter 'subreddit'")
        url = f"{self.base_url}/r/{subreddit}/top"
        query_params = {
            k: v
            for k, v in [
                ("after", after),
                ("before", before),
                ("count", count),
                ("limit", limit),
                ("show", show),
                ("sr_detail", sr_detail),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_rising_posts(
        self,
        after: str = None,
        before: str = None,
        count: int = None,
        limit: int = None,
        show: str = None,
        sr_detail: str = None,
    ) -> Any:
        """
        Retrieves a list of the rising posts across Reddit.

        Args:
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            show: Optional. The string "all" to show all posts.
            sr_detail: Optional. Expand subreddit details.

        Returns:
            Any: API response data containing a list of rising posts.

        Tags:
            listings, posts, rising, read-only
        """
        url = f"{self.base_url}/rising"
        query_params = {
            k: v
            for k, v in [
                ("after", after),
                ("before", before),
                ("count", count),
                ("limit", limit),
                ("show", show),
                ("sr_detail", sr_detail),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_top_posts(
        self,
        after: str = None,
        before: str = None,
        count: int = None,
        limit: int = None,
        show: str = None,
        sr_detail: str = None,
    ) -> Any:
        """
        Retrieves a list of the top posts across Reddit.

        Args:
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            show: Optional. The string "all" to show all posts.
            sr_detail: Optional. Expand subreddit details.

        Returns:
            Any: API response data containing a list of top posts.

        Tags:
            listings, posts, top, read-only
        """
        url = f"{self.base_url}/top"
        query_params = {
            k: v
            for k, v in [
                ("after", after),
                ("before", before),
                ("count", count),
                ("limit", limit),
                ("show", show),
                ("sr_detail", sr_detail),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_reddit(
        self,
        after: str = None,
        before: str = None,
        category: str = None,
        count: int = None,
        include_facets: bool = None,
        limit: int = None,
        q: str = None,
        restrict_sr: bool = None,
        show: str = None,
        sort: str = None,
        sr_detail: str = None,
        t: str = None,
        type: str = None,
    ) -> Any:
        """
        Searches for posts, comments, and users across Reddit.

        Args:
            after: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results after.
            before: Optional. The fullname of a thing (e.g., 't3_xxxxxx') to return results before.
            category: Optional. A string no longer than 5 characters to filter by category.
            count: Optional. A positive integer (default: 0) for the number of items already seen in the listing.
            include_facets: Optional. Boolean value (true, false) to include facets in the search results.
            limit: Optional. The maximum number of items desired (default: 25, maximum: 100).
            q: Optional. The search query string, no longer than 512 characters.
            restrict_sr: Optional. Boolean value (true, false) to restrict search to a specific subreddit.
            show: Optional. The string "all" to show all results.
            sort: Optional. One of ('relevance', 'hot', 'top', 'new', 'comments') to sort results.
            sr_detail: Optional. Expand subreddit details.
            t: Optional. One of ('hour', 'day', 'week', 'month', 'year', 'all') to filter by time.
            type: Optional. A comma-separated list of result types ('sr', 'link', 'user').

        Returns:
            Any: API response data containing search results.

        Tags:
            search, reddit, posts, comments, users, read-only
        """
        url = f"{self.base_url}/search"
        query_params = {
            k: v
            for k, v in [
                ("after", after),
                ("before", before),
                ("category", category),
                ("count", count),
                ("include_facets", include_facets),
                ("limit", limit),
                ("q", q),
                ("restrict_sr", restrict_sr),
                ("show", show),
                ("sort", sort),
                ("sr_detail", sr_detail),
                ("t", t),
                ("type", type),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user_profile(self, username: str) -> Any:
        """
        Retrieves the profile information for a given Reddit user.

        Args:
            username: The username of the user to look up.

        Returns:
            A dictionary containing the user's profile data.

        Tags:
            users, profile, fetch
        """
        if username is None:
            raise ValueError("Missing required parameter 'username'")
        url = f"{self.base_url}/user/{username}/about"
        query_params = {k: v for k, v in [("username", username)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_subreddit_posts,
            self.search_subreddits,
            self.get_post_flairs,
            self.create_post,
            self.get_comment_by_id,
            self.post_comment,
            self.edit_content,
            self.delete_content,
            self.get_post_comments_details,
            self.get_current_user_info,
            self.get_current_user_karma,
            self.get_hot_posts,
            self.get_new_posts,
            self.get_top_posts,
            self.get_rising_posts,
            self.get_controversial_posts,
            self.get_subreddit_hot_posts,
            self.get_subreddit_new_posts,
            self.get_subreddit_top_posts,
            self.search_reddit,
            self.get_user_profile,
        ]
