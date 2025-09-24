from typing import Any

from .api_segment_base import APISegmentBase


class UsersApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def get_users_by_ids(
        self, ids, user_fields=None, expansions=None, tweet_fields=None
    ) -> dict[str, Any]:
        """
        Retrieves detailed information for multiple users in a single API request, specified by a list of their unique IDs. Unlike `find_user_by_id`, which fetches a single user, this function performs a bulk lookup and allows for response customization with optional fields and expansions.

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

    def get_users_by_usernames(
        self, usernames, user_fields=None, expansions=None, tweet_fields=None
    ) -> dict[str, Any]:
        """
        Fetches public data for a batch of users specified by their usernames. This function supports retrieving multiple users in a single request, unlike `find_user_by_username`. It allows for data customization through optional fields and expansions.

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
        Retrieves detailed information for a single user specified by their username, with options to include additional user, tweet, and expansion fields. This differs from `find_users_by_username`, which fetches data for multiple users in a single request.

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
        Streams real-time user compliance events, such as account deletions or suspensions, from a specified data partition. Allows for backfilling missed data after a disconnection and filtering the event stream by a specific time range for targeted data retrieval.

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

    def get_authenticated_user(
        self, user_fields=None, expansions=None, tweet_fields=None
    ) -> dict[str, Any]:
        """
        Retrieves detailed information about the authenticated user making the request. Optional parameters allow for customizing the returned user and tweet data fields and including expanded objects. This differs from other 'find' functions as it requires no ID or username.

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

    def search_users_by_query(
        self,
        query,
        max_results=None,
        next_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Searches for users matching a specific query string. Supports pagination and allows customizing the response by specifying which user, tweet, and expansion fields to include in the results, providing a flexible way to discover users.

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
        Retrieves detailed information for a single user specified by their unique ID. This function allows for response customization using optional fields and expansions. It differs from `find_users_by_id`, which fetches data for multiple users in a single request.

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

    def list_blocked_users(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of users blocked by a specified user ID. The response can be customized by specifying additional fields for users, tweets, and expansions to tailor the returned data objects.

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

    def list_user_bookmarks(
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
        Retrieves a paginated list of tweets bookmarked by a specified user. Allows extensive customization of the response data by specifying tweet, media, user, and place fields, as well as object expansions.

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

    def bookmark_tweet(self, id, tweet_id) -> dict[str, Any]:
        """
        Bookmarks a specific tweet for a user. This action adds the tweet, identified by `tweet_id`, to the bookmarks of the user specified by their unique `id`, making a POST request to the bookmarks endpoint.

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

    def remove_bookmark(self, id, tweet_id) -> dict[str, Any]:
        """
        Deletes a bookmarked tweet for a specified user. This action requires both the user's ID and the tweet's ID to target the correct bookmark for removal via an API DELETE request. It is the inverse of `post_users_id_bookmarks`.

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

    def get_user_followed_lists(
        self,
        id,
        max_results=None,
        pagination_token=None,
        list_fields=None,
        expansions=None,
        user_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of Twitter Lists that a specified user follows. Identified by user ID, this function allows response customization with optional parameters for pagination, expansions, and specific list or user fields to include in the results.

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

    def follow_list(self, id, list_id=None) -> dict[str, Any]:
        """
        Causes a specified user to follow a particular Twitter List. It sends a POST request to the `/users/{id}/followed_lists` endpoint with the list's ID. This contrasts with `user_followed_lists`, which retrieves the lists a user already follows, and `list_user_unfollow`, which removes a list.

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

    def unfollow_list(self, id, list_id) -> dict[str, Any]:
        """
        Causes a user, specified by their ID, to unfollow a particular Twitter List, identified by its list ID. This action sends a DELETE request to the API, removing the follow relationship between the user and the list.

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

    def get_user_followers(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of users who follow a specified user ID. The response can be customized with optional parameters to control the number of results, expand related objects, and specify which user or tweet fields to return.

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

    def get_following_by_user_id(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of users followed by a specific user ID. The response can be customized by requesting additional user fields, tweet fields, and data expansions to include more detailed information about the followed accounts.

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

    def follow_user(self, id, target_user_id=None) -> dict[str, Any]:
        """
        Causes a source user, specified by `id`, to follow a target user (`target_user_id`). It sends a POST request to the `/2/users/{id}/following` endpoint to create the follow relationship, distinct from `users_id_following` which retrieves a list of followed users.

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

    def get_liked_tweets_by_user(
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
        Fetches a list of tweets liked by a specified user ID. This function supports pagination and allows for extensive customization of the returned data, including expansions and specific fields for tweets, media, users, polls, and places.

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

    def like_tweet(self, id, tweet_id=None) -> dict[str, Any]:
        """
        Causes a user, specified by `id`, to like a tweet, specified by `tweet_id`. This function sends a POST request to add a like, contrasting with `users_id_unlike` which removes a like and `users_id_liked_tweets` which retrieves a list of liked tweets.

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

    def unlike_tweet(self, id, tweet_id) -> dict[str, Any]:
        """
        Removes a like from a tweet on behalf of an authenticated user. This function identifies the specific like to be deleted using the user's ID and the tweet's ID, then sends a corresponding DELETE request to the Twitter API.

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
        Retrieves all Twitter Lists of which a specific user is a member. Supports pagination and allows for response customization by specifying which list fields, user fields, and expansions to return, differentiating it from functions that get followed, owned, or pinned lists.

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

    def get_user_mentions(
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
        Retrieves a timeline of tweets mentioning a specified user, identified by their ID. Allows for pagination and filtering by time or tweet ID, with options to customize the returned data fields for tweets, users, media, and other entities.

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

    def get_muted_users(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of users muted by a specific user, identified by ID. Supports pagination and allows for customizing the returned data, including user fields, expansions, and tweet fields, to tailor the response.

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

    def mute_user(self, id, target_user_id=None) -> dict[str, Any]:
        """
        Mutes a target user on behalf of an authenticated user. This action requires the authenticated user's ID and the target user's ID. It differs from `users_id_unmute` (which unmutes) and `users_id_muting` (which lists muted users) by performing the actual mute operation via POST request.

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

    def get_user_owned_lists(
        self,
        id,
        max_results=None,
        pagination_token=None,
        list_fields=None,
        expansions=None,
        user_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves all Twitter Lists owned by a specified user ID. Supports pagination and custom data fields for detailed results. This function fetches lists created by the user, distinguishing it from methods that retrieve lists the user follows (`user_followed_lists`) or has pinned (`list_user_pinned_lists`).

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

    def get_user_pinned_lists(
        self, id, list_fields=None, expansions=None, user_fields=None
    ) -> dict[str, Any]:
        """
        Retrieves the collection of lists pinned by a specific user, identified by their ID. Optional parameters allow for customizing the returned list and user data fields, and including expansions. This is distinct from fetching lists a user follows or owns.

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

    def pin_list(self, id, list_id) -> dict[str, Any]:
        """
        Pins a specified list to a user's profile via a POST request, using the user and list IDs. This creates a new pin, differing from `list_user_unpin` which removes a pin and `list_user_pinned_lists` which retrieves all of a user's currently pinned lists.

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

    def unpin_list(self, id, list_id) -> dict[str, Any]:
        """
        Unpins a specific list from a user's profile, identified by their user ID and the list's ID. This action sends a DELETE request to the API, removing the specified list from the user's collection of pinned lists.

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

    def create_retweet(self, id, tweet_id=None) -> dict[str, Any]:
        """
        Causes a user, identified by `id`, to retweet a specific tweet. This action sends a POST request to the `/2/users/{id}/retweets` endpoint, requiring the `tweet_id` of the tweet to be retweeted. It is the opposite of the `users_id_unretweets` function, which deletes a retweet.

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

    def delete_retweet(self, id, source_tweet_id) -> dict[str, Any]:
        """
        Removes a retweet for a specified user by sending a DELETE request to the Twitter API. It requires the user's ID and the ID of the original tweet that was retweeted to successfully undo the action.

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

    def get_user_tweet_timeline(
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
        Retrieves tweets from a user's timeline in reverse chronological order. Supports filtering by time or tweet ID, pagination, and excluding replies or retweets. Optional parameters allow for expanding returned data with additional tweet, user, and media fields.

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

    def get_tweets_by_user_id(
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
        Retrieves tweets authored by a specific user, identified by their ID. Supports pagination and filtering by time range, allowing response customization to exclude replies or retweets. This fetches tweets composed by the user, unlike the more general `users_id_timeline` function which includes retweets.

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

    def unfollow_user(self, source_user_id, target_user_id) -> dict[str, Any]:
        """
        Causes a specified user (`source_user_id`) to unfollow another user (`target_user_id`). This function sends a DELETE API request to remove the follow relationship, requiring both user IDs to successfully complete the action.

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

    def unmute_user(self, source_user_id, target_user_id) -> dict[str, Any]:
        """
        Allows an authenticated user (source) to unmute another user (target). This action removes the specified target user from the source user's mute list, reversing a previous mute action.

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
            self.get_users_by_ids,
            self.get_users_by_usernames,
            self.find_user_by_username,
            self.get_users_compliance_stream,
            self.get_authenticated_user,
            self.search_users_by_query,
            self.find_user_by_id,
            self.list_blocked_users,
            self.list_user_bookmarks,
            self.bookmark_tweet,
            self.remove_bookmark,
            self.get_user_followed_lists,
            self.follow_list,
            self.unfollow_list,
            self.get_user_followers,
            self.get_following_by_user_id,
            self.follow_user,
            self.get_liked_tweets_by_user,
            self.like_tweet,
            self.unlike_tweet,
            self.get_user_list_memberships,
            self.get_user_mentions,
            self.get_muted_users,
            self.mute_user,
            self.get_user_owned_lists,
            self.get_user_pinned_lists,
            self.pin_list,
            self.unpin_list,
            self.create_retweet,
            self.delete_retweet,
            self.get_user_tweet_timeline,
            self.get_tweets_by_user_id,
            self.unfollow_user,
            self.unmute_user,
        ]
