from typing import Any

from .api_segment_base import APISegmentBase


class UsersApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def find_users_by_id(
        self, ids, user_fields=None, expansions=None, tweet_fields=None
    ) -> dict[str, Any]:
        """

        Retrieves information about one or more users specified by their IDs, allowing for customization with user fields and expansions.

        Args:
            ids (array): A required query parameter specifying an array of user IDs to retrieve information for multiple users in a single request. Example: '2244994945,6253282,12'.
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        url = f"{self.main_app_client.base_url}/2/users"
        query_params = {
            k: v
            for k, v in [
                ("ids", ids),
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_users_by_username(
        self, usernames, user_fields=None, expansions=None, tweet_fields=None
    ) -> dict[str, Any]:
        """

        Retrieves information about one or more users specified by their usernames using the Twitter API, allowing optional specification of additional user fields and expansions.

        Args:
            usernames (array): Required array of usernames to filter users by. Example: 'TwitterDev,TwitterAPI'.
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        url = f"{self.main_app_client.base_url}/2/users/by"
        query_params = {
            k: v
            for k, v in [
                ("usernames", usernames),
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_user_by_username(
        self, username, user_fields=None, expansions=None, tweet_fields=None
    ) -> dict[str, Any]:
        """

        Retrieves information about a user specified by their username, optionally including additional fields and expansions, using the "GET" method with authentication.

        Args:
            username (string): username
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if username is None:
            raise ValueError("Missing required parameter 'username'.")
        url = f"{self.main_app_client.base_url}/2/users/by/username/{username}"
        query_params = {
            k: v
            for k, v in [
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_compliance_stream(
        self, partition, backfill_minutes=None, start_time=None, end_time=None
    ) -> Any:
        """

        Streams compliance data for users using the "GET" method, supporting optional backfill minutes, start and end times, and requiring a partition parameter.

        Args:
            partition (integer): The "partition" parameter is a required integer query parameter that determines which partition of the compliance stream data to retrieve.
            backfill_minutes (integer): Optional integer parameter to specify the number of minutes of missed data to recover after a disconnection; valid values are between 1 and 5 minutes.
            start_time (string): Optional start time in string format for filtering the compliance stream. Example: '2021-02-01T18:40:40.000Z'.
            end_time (string): Optional end time for filtering the compliance stream data, specified as a string. Example: '2021-02-01T18:40:40.000Z'.

        Returns:
            Any: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Compliance
        """
        url = f"{self.main_app_client.base_url}/2/users/compliance/stream"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
                ("start_time", start_time),
                ("end_time", end_time),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_my_user(
        self, user_fields=None, expansions=None, tweet_fields=None
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about the authenticated user, including optional expansions and fields for user and tweet data.

        Args:
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        url = f"{self.main_app_client.base_url}/2/users/me"
        query_params = {
            k: v
            for k, v in [
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_user_by_query(
        self,
        query,
        max_results=None,
        next_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Searches for users using a query string, returning a list of matching users with optional fields for user details, expansions, and related tweet fields.

        Args:
            query (string): Search query to filter users based on specific criteria. Example: 'someXUser'.
            max_results (integer): Maximum number of results to return in the search query, with a default of 100.
            next_token (string): The token used for pagination to retrieve the next set of user search results.
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        url = f"{self.main_app_client.base_url}/2/users/search"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("max_results", max_results),
                ("next_token", next_token),
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_user_by_id(
        self, id, user_fields=None, expansions=None, tweet_fields=None
    ) -> dict[str, Any]:
        """

        Retrieves information about a user specified by their ID, with optional parameters for specifying additional user fields, expansions, and tweet fields.

        Args:
            id (string): id
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}"
        query_params = {
            k: v
            for k, v in [
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_blocking(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of user objects that are blocked by the specified user ID, allowing for additional fields and expansions to be specified.

        Args:
            id (string): id
            max_results (integer): Limits the number of user blocking records returned in the response, with no default value set and requiring an integer input.
            pagination_token (string): The pagination_token query parameter is an optional opaque string token used to retrieve the next page of results when paginating through a user's blocked accounts.
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/blocking"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_id_bookmarks(
        self,
        id,
        max_results=None,
        pagination_token=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of bookmarks for a user with the specified ID, allowing optional pagination and customization of returned fields.

        Args:
            id (string): id
            max_results (integer): The "max_results" parameter, an optional integer query parameter with a default value of 2, limits the number of bookmark results returned when retrieving a user's bookmarks via the GET operation at "/2/users/{id}/bookmarks".
            pagination_token (string): The pagination_token query parameter is an optional token used to retrieve the next page of results in a paginated response for the user's bookmarks.
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['article.cover_media', 'article.media_entities', 'attachments.media_keys', 'attachments.media_source_tweet', 'attachments.poll_ids', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'entities.note.mentions.username', 'referenced_tweets.id', 'referenced_tweets.id.author_id', 'author_screen_name']".
            media_fields (array): A comma separated list of Media fields to display. Example: "['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics', 'organic_metrics', 'preview_image_url', 'promoted_metrics', 'public_metrics', 'type', 'url', 'variants', 'width']".
            poll_fields (array): A comma separated list of Poll fields to display. Example: "['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            place_fields (array): A comma separated list of Place fields to display. Example: "['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Bookmarks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/bookmarks"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("tweet.fields", tweet_fields),
                ("expansions", expansions),
                ("media.fields", media_fields),
                ("poll.fields", poll_fields),
                ("user.fields", user_fields),
                ("place.fields", place_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_users_id_bookmarks(self, id, tweet_id) -> dict[str, Any]:
        """

        Adds bookmarks for a specified user using the provided JSON data and returns a successful response upon completion.

        Args:
            id (string): id
            tweet_id (string): Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. Example: '1346889436626259968'.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Bookmarks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {"tweet_id": tweet_id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/users/{id}/bookmarks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def users_id_bookmarks_delete(self, id, tweet_id) -> dict[str, Any]:
        """

        Deletes a bookmarked tweet for a specified user using the "DELETE" method.

        Args:
            id (string): id
            tweet_id (string): tweet_id

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Bookmarks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if tweet_id is None:
            raise ValueError("Missing required parameter 'tweet_id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/bookmarks/{tweet_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_followed_lists(
        self,
        id,
        max_results=None,
        pagination_token=None,
        list_fields=None,
        expansions=None,
        user_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of Twitter lists followed by a specified user, with optional parameters for pagination, list fields, and user fields.

        Args:
            id (string): id
            max_results (integer): Specifies the maximum number of followed lists to return per page, with a default value of 100.
            pagination_token (string): The pagination_token query parameter is an optional token used to retrieve the next page of results in a paginated response for followed lists.
            list_fields (array): A comma separated list of List fields to display. Example: "['created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private']".
            expansions (array): A comma separated list of fields to expand. Example: "['owner_id']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/followed_lists"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("list.fields", list_fields),
                ("expansions", expansions),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_follow(self, id, list_id=None) -> dict[str, Any]:
        """

        Adds a Twitter user to a list of followed lists using the Twitter API and returns a status message.

        Args:
            id (string): id
            list_id (string): The unique identifier of this List. Example: '1146654567674912769'.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {"list_id": list_id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/users/{id}/followed_lists"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def list_user_unfollow(self, id, list_id) -> dict[str, Any]:
        """

        Deletes the specified list followed by the user identified by the given user ID and list ID.

        Args:
            id (string): id
            list_id (string): list_id

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/followed_lists/{list_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_followers(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of users who follow a specified user using the Twitter API, with optional parameters for result pagination and additional user or tweet fields.

        Args:
            id (string): id
            max_results (integer): The maximum number of follower results to return in the response.
            pagination_token (string): An optional token used for pagination to continue retrieving followers from a specific point in the dataset.
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/followers"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_following(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of users followed by the specified user ID, allowing optional parameters to customize the response with additional user fields, expansions, and tweet fields.

        Args:
            id (string): id
            max_results (integer): Optional parameter to limit the number of results returned in the response for the GET operation at "/2/users/{id}/following", specified as an integer.
            pagination_token (string): An opaque token used for pagination, allowing the retrieval of the next batch of results when navigating through a large dataset of users that the specified user is following.
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/following"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_follow(self, id, target_user_id=None) -> dict[str, Any]:
        """

        Follows another user on behalf of the current user using the Twitter API, returning a status message indicating whether the action was successful.

        Args:
            id (string): id
            target_user_id (string): Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. Example: '2244994945'.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {"target_user_id": target_user_id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/users/{id}/following"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def users_id_liked_tweets(
        self,
        id,
        max_results=None,
        pagination_token=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of tweets liked by the specified user, supporting pagination and optional expansions and fields for tweets, users, media, polls, and places.

        Args:
            id (string): id
            max_results (integer): Optional integer parameter to limit the number of liked tweets returned in the response.
            pagination_token (string): The pagination_token query parameter is an optional opaque string token used to fetch the next page of results in the user's liked tweets timeline.
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['article.cover_media', 'article.media_entities', 'attachments.media_keys', 'attachments.media_source_tweet', 'attachments.poll_ids', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'entities.note.mentions.username', 'referenced_tweets.id', 'referenced_tweets.id.author_id', 'author_screen_name']".
            media_fields (array): A comma separated list of Media fields to display. Example: "['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics', 'organic_metrics', 'preview_image_url', 'promoted_metrics', 'public_metrics', 'type', 'url', 'variants', 'width']".
            poll_fields (array): A comma separated list of Poll fields to display. Example: "['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            place_fields (array): A comma separated list of Place fields to display. Example: "['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/liked_tweets"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("tweet.fields", tweet_fields),
                ("expansions", expansions),
                ("media.fields", media_fields),
                ("poll.fields", poll_fields),
                ("user.fields", user_fields),
                ("place.fields", place_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_like(self, id, tweet_id=None) -> dict[str, Any]:
        """

        Creates a new like for a user's content using the provided user ID and returns a status message.

        Args:
            id (string): id
            tweet_id (string): Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. Example: '1346889436626259968'.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {"tweet_id": tweet_id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/users/{id}/likes"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def users_id_unlike(self, id, tweet_id) -> dict[str, Any]:
        """

        Deletes a user's like on a specific tweet using the provided user ID and tweet ID, requiring OAuth2UserToken with "like.write," "tweet.read," and "users.read" permissions.

        Args:
            id (string): id
            tweet_id (string): tweet_id

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if tweet_id is None:
            raise ValueError("Missing required parameter 'tweet_id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/likes/{tweet_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user_list_memberships(
        self,
        id,
        max_results=None,
        pagination_token=None,
        list_fields=None,
        expansions=None,
        user_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of memberships for a specified user using their ID, allowing for optional filtering by maximum results and pagination, and returns the membership details.

        Args:
            id (string): id
            max_results (integer): The maximum number of membership results to return, defaulting to 100 if not specified.
            pagination_token (string): An optional token used for pagination to navigate through the list of memberships for a user, typically provided in the response of a previous request.
            list_fields (array): A comma separated list of List fields to display. Example: "['created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private']".
            expansions (array): A comma separated list of fields to expand. Example: "['owner_id']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/list_memberships"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("list.fields", list_fields),
                ("expansions", expansions),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_mentions(
        self,
        id,
        since_id=None,
        until_id=None,
        max_results=None,
        pagination_token=None,
        start_time=None,
        end_time=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves the timeline of tweets that mention the user associated with the provided ID, allowing for customization with parameters such as since and until IDs, pagination tokens, and various field expansions.

        Args:
            id (string): id
            since_id (string): Optional parameter to return results with an ID greater than (i.e., more recent than) the specified ID. Example: '1346889436626259968'.
            until_id (string): Optional identifier to fetch mentions until this specific user ID. Example: '1346889436626259968'.
            max_results (integer): Limits the number of mention items returned in the response.
            pagination_token (string): Optional token used for pagination, allowing continuation from a specific point in the list of mentions.
            start_time (string): Optional start time in string format to filter mentions. Example: '2021-02-01T18:40:40.000Z'.
            end_time (string): Optional end time filter for retrieving user mentions, specified in a string format. Example: '2021-02-14T18:40:40.000Z'.
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['article.cover_media', 'article.media_entities', 'attachments.media_keys', 'attachments.media_source_tweet', 'attachments.poll_ids', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'entities.note.mentions.username', 'referenced_tweets.id', 'referenced_tweets.id.author_id', 'author_screen_name']".
            media_fields (array): A comma separated list of Media fields to display. Example: "['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics', 'organic_metrics', 'preview_image_url', 'promoted_metrics', 'public_metrics', 'type', 'url', 'variants', 'width']".
            poll_fields (array): A comma separated list of Poll fields to display. Example: "['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            place_fields (array): A comma separated list of Place fields to display. Example: "['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/mentions"
        query_params = {
            k: v
            for k, v in [
                ("since_id", since_id),
                ("until_id", until_id),
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("start_time", start_time),
                ("end_time", end_time),
                ("tweet.fields", tweet_fields),
                ("expansions", expansions),
                ("media.fields", media_fields),
                ("poll.fields", poll_fields),
                ("user.fields", user_fields),
                ("place.fields", place_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_muting(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of users muted by the specified user using the Twitter API with optional filtering by max results, pagination token, user fields, user expansions, tweet fields, and returns the response upon authorization with the required "mute.read," "tweet.read," and "users.read" scopes.

        Args:
            id (string): id
            max_results (integer): The "max_results" parameter limits the number of results returned in the response for the GET operation at "/2/users/{id}/muting", with a default value of 100.
            pagination_token (string): The token to retrieve the next page of results when paginating through muted users; omit to start from the first page.
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/muting"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("user.fields", user_fields),
                ("expansions", expansions),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_mute(self, id, target_user_id=None) -> dict[str, Any]:
        """

        Mutes a user identified by their ID using the API, requiring a POST request with appropriate OAuth2 credentials.

        Args:
            id (string): id
            target_user_id (string): Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. Example: '2244994945'.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {"target_user_id": target_user_id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/users/{id}/muting"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def list_user_owned_lists(
        self,
        id,
        max_results=None,
        pagination_token=None,
        list_fields=None,
        expansions=None,
        user_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of Twitter Lists owned by the specified user, supporting optional pagination and field expansions.

        Args:
            id (string): id
            max_results (integer): Maximum number of owned lists to return in the response; defaults to 100 if not specified.
            pagination_token (string): An optional token used for pagination, allowing users to fetch subsequent pages of results for the owned lists of a specified user.
            list_fields (array): A comma separated list of List fields to display. Example: "['created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private']".
            expansions (array): A comma separated list of fields to expand. Example: "['owner_id']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/owned_lists"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("list.fields", list_fields),
                ("expansions", expansions),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_pinned_lists(
        self, id, list_fields=None, expansions=None, user_fields=None
    ) -> dict[str, Any]:
        """

        Retrieves the pinned Lists of a specified user by their user ID, returning detailed information about each pinned List.

        Args:
            id (string): id
            list_fields (array): A comma separated list of List fields to display. Example: "['created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private']".
            expansions (array): A comma separated list of fields to expand. Example: "['owner_id']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/pinned_lists"
        query_params = {
            k: v
            for k, v in [
                ("list.fields", list_fields),
                ("expansions", expansions),
                ("user.fields", user_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_pin(self, id, list_id) -> dict[str, Any]:
        """

        Creates a pinned list for a user identified by {id} using JSON data and OAuth2UserToken or UserToken authentication.

        Args:
            id (string): id
            list_id (string): The unique identifier of this List. Example: '1146654567674912769'.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {"list_id": list_id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/users/{id}/pinned_lists"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def list_user_unpin(self, id, list_id) -> dict[str, Any]:
        """

        Deletes a specified pinned list from a user's account by user ID and list ID.

        Args:
            id (string): id
            list_id (string): list_id

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if list_id is None:
            raise ValueError("Missing required parameter 'list_id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/pinned_lists/{list_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_retweets(self, id, tweet_id=None) -> dict[str, Any]:
        """

        Retweets a post using the X API on behalf of a specified user, requiring authentication with OAuth2UserToken and appropriate permissions.

        Args:
            id (string): id
            tweet_id (string): Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. Example: '1346889436626259968'.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {"tweet_id": tweet_id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/users/{id}/retweets"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def users_id_unretweets(self, id, source_tweet_id) -> dict[str, Any]:
        """

        Undoes a retweet of a specified tweet by a user using the Twitter API v2, requiring OAuth authentication and user permissions.

        Args:
            id (string): id
            source_tweet_id (string): source_tweet_id

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if source_tweet_id is None:
            raise ValueError("Missing required parameter 'source_tweet_id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/retweets/{source_tweet_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_timeline(
        self,
        id,
        since_id=None,
        until_id=None,
        max_results=None,
        pagination_token=None,
        exclude=None,
        start_time=None,
        end_time=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a user's reverse chronological timeline, returning tweets in the order they were posted, with optional filtering by time range, tweet IDs, and additional metadata fields.

        Args:
            id (string): id
            since_id (string): The `since_id` parameter specifies the smallest ID of the statuses to be returned, retrieving the newest statuses first, but it may not return all statuses if there are too many between the newest and the specified ID. Example: '791775337160081409'.
            until_id (string): Optional ID to retrieve timelines up to this user ID in reverse chronological order. Example: '1346889436626259968'.
            max_results (integer): **max_results**: Optional integer parameter specifying the maximum number of results to return for the GET operation.
            pagination_token (string): Optional token used to paginate the response, specifying the point to start retrieving resources from in the reverse chronological timeline.
            exclude (array): A query parameter to specify an array of fields or properties to exclude from the response. Example: "['replies', 'retweets']".
            start_time (string): Optional start time parameter to filter timelines by specifying the earliest date and time for which entries should be included. Example: '2021-02-01T18:40:40.000Z'.
            end_time (string): The end_time query parameter specifies the optional timestamp that defines the upper bound (latest) for filtering tweets in the reverse chronological timeline of a user. Example: '2021-02-14T18:40:40.000Z'.
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['article.cover_media', 'article.media_entities', 'attachments.media_keys', 'attachments.media_source_tweet', 'attachments.poll_ids', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'entities.note.mentions.username', 'referenced_tweets.id', 'referenced_tweets.id.author_id', 'author_screen_name']".
            media_fields (array): A comma separated list of Media fields to display. Example: "['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics', 'organic_metrics', 'preview_image_url', 'promoted_metrics', 'public_metrics', 'type', 'url', 'variants', 'width']".
            poll_fields (array): A comma separated list of Poll fields to display. Example: "['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            place_fields (array): A comma separated list of Place fields to display. Example: "['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/timelines/reverse_chronological"
        query_params = {
            k: v
            for k, v in [
                ("since_id", since_id),
                ("until_id", until_id),
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("exclude", exclude),
                ("start_time", start_time),
                ("end_time", end_time),
                ("tweet.fields", tweet_fields),
                ("expansions", expansions),
                ("media.fields", media_fields),
                ("poll.fields", poll_fields),
                ("user.fields", user_fields),
                ("place.fields", place_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_tweets(
        self,
        id,
        since_id=None,
        until_id=None,
        max_results=None,
        pagination_token=None,
        exclude=None,
        start_time=None,
        end_time=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of tweets for a user with the specified ID, allowing optional filtering by tweet ID range, result count, pagination token, excluded fields, and time range, using the "GET" method.

        Args:
            id (string): id
            since_id (string): Returns only Tweets with IDs greater than (more recent than) the specified ID, allowing retrieval of Tweets posted after that ID. Example: '791775337160081409'.
            until_id (string): Returns tweets with IDs less than (older than) the specified until_id, limiting results to tweets posted before that ID. Example: '1346889436626259968'.
            max_results (integer): Specifies the maximum number of tweets to return per GET request for a user's tweets, with this parameter being optional and of type integer.
            pagination_token (string): Optional token used for pagination to continue retrieving results from a previous query.
            exclude (array): A query parameter to exclude specific properties from the response; accepts an array of property names to omit. Example: "['replies', 'retweets']".
            start_time (string): The start_time query parameter is an optional ISO 8601 timestamp string used to specify the earliest time from which to retrieve tweets for the user. Example: '2021-02-01T18:40:40.000Z'.
            end_time (string): Optional query parameter to filter tweets by specifying the end time, in string format, for retrieving tweets before this time. Example: '2021-02-14T18:40:40.000Z'.
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['article.cover_media', 'article.media_entities', 'attachments.media_keys', 'attachments.media_source_tweet', 'attachments.poll_ids', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'entities.note.mentions.username', 'referenced_tweets.id', 'referenced_tweets.id.author_id', 'author_screen_name']".
            media_fields (array): A comma separated list of Media fields to display. Example: "['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics', 'organic_metrics', 'preview_image_url', 'promoted_metrics', 'public_metrics', 'type', 'url', 'variants', 'width']".
            poll_fields (array): A comma separated list of Poll fields to display. Example: "['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            place_fields (array): A comma separated list of Place fields to display. Example: "['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/users/{id}/tweets"
        query_params = {
            k: v
            for k, v in [
                ("since_id", since_id),
                ("until_id", until_id),
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("exclude", exclude),
                ("start_time", start_time),
                ("end_time", end_time),
                ("tweet.fields", tweet_fields),
                ("expansions", expansions),
                ("media.fields", media_fields),
                ("poll.fields", poll_fields),
                ("user.fields", user_fields),
                ("place.fields", place_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_unfollow(self, source_user_id, target_user_id) -> dict[str, Any]:
        """

        Unfollows a target user by deleting the follow relationship between the source user and the target user using the "DELETE" method.

        Args:
            source_user_id (string): source_user_id
            target_user_id (string): target_user_id

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if source_user_id is None:
            raise ValueError("Missing required parameter 'source_user_id'.")
        if target_user_id is None:
            raise ValueError("Missing required parameter 'target_user_id'.")
        url = f"{self.main_app_client.base_url}/2/users/{source_user_id}/following/{target_user_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_id_unmute(self, source_user_id, target_user_id) -> dict[str, Any]:
        """

        Unmutes a target user using the "DELETE" method on the "/2/users/{source_user_id}/muting/{target_user_id}" path, reversing the mute action applied by the source user to the target user.

        Args:
            source_user_id (string): source_user_id
            target_user_id (string): target_user_id

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        if source_user_id is None:
            raise ValueError("Missing required parameter 'source_user_id'.")
        if target_user_id is None:
            raise ValueError("Missing required parameter 'target_user_id'.")
        url = f"{self.main_app_client.base_url}/2/users/{source_user_id}/muting/{target_user_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.find_users_by_id,
            self.find_users_by_username,
            self.find_user_by_username,
            self.get_users_compliance_stream,
            self.find_my_user,
            self.search_user_by_query,
            self.find_user_by_id,
            self.users_id_blocking,
            self.get_users_id_bookmarks,
            self.post_users_id_bookmarks,
            self.users_id_bookmarks_delete,
            self.user_followed_lists,
            self.list_user_follow,
            self.list_user_unfollow,
            self.users_id_followers,
            self.users_id_following,
            self.users_id_follow,
            self.users_id_liked_tweets,
            self.users_id_like,
            self.users_id_unlike,
            self.get_user_list_memberships,
            self.users_id_mentions,
            self.users_id_muting,
            self.users_id_mute,
            self.list_user_owned_lists,
            self.list_user_pinned_lists,
            self.list_user_pin,
            self.list_user_unpin,
            self.users_id_retweets,
            self.users_id_unretweets,
            self.users_id_timeline,
            self.users_id_tweets,
            self.users_id_unfollow,
            self.users_id_unmute,
        ]
