from typing import Any

from .api_segment_base import APISegmentBase


class ListsApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def create_list(self, description=None, name=None, private=None) -> dict[str, Any]:
        """
        Creates a new list on X (formerly Twitter) with an optional name, description, and privacy setting. It sends a POST request to the `/2/lists` endpoint and returns the JSON data of the newly created list upon success.

        Args:
            description (string): description
            name (string): name
            private (boolean): private

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Lists, important
        """
        request_body_data = None
        request_body_data = {
            "description": description,
            "name": name,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/lists"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def delete_list(self, id) -> dict[str, Any]:
        """
        Permanently deletes a specific Twitter List identified by its unique ID. This function sends an authorized DELETE request to the API's `/2/lists/{id}` endpoint, returning a confirmation response upon successful removal. It is distinct from `list_remove_member`, which only removes a user from a list.

        Args:
            id (string): id

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
        url = f"{self.main_app_client.base_url}/2/lists/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_by_id(
        self, id, list_fields=None, expansions=None, user_fields=None
    ) -> dict[str, Any]:
        """
        Retrieves detailed information for a specific list by its ID. This function allows for response customization by specifying which list and user fields to return and supports expansions to include related objects like the owner's user data.

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
        url = f"{self.main_app_client.base_url}/2/lists/{id}"
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

    def update_list(
        self, id, description=None, name=None, private=None
    ) -> dict[str, Any]:
        """
        Modifies an existing Twitter list identified by its unique ID. This function updates the list's name, description, or privacy status by sending a PUT request to the API and returns the updated list data upon success.

        Args:
            id (string): id
            description (string): description
            name (string): name
            private (boolean): private

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
        request_body_data = {
            "description": description,
            "name": name,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/lists/{id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def get_list_followers(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves the users who follow a specific list, identified by its ID. Supports pagination and allows for the customization of returned user, tweet, and expansion fields to tailor the response data, differentiating it from fetching list members.

        Args:
            id (string): id
            max_results (integer): Specifies the maximum number of follower results to return, with a default value of 100.
            pagination_token (string): The pagination_token query parameter is an optional cursor used to retrieve the next page of results when paginating through the followers of a list.
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
        url = f"{self.main_app_client.base_url}/2/lists/{id}/followers"
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

    def list_get_members(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves users who are members of a specific Twitter list, identified by its ID. Unlike `list_get_followers`, this returns users explicitly added to the list, not subscribers. Supports pagination and customization of the returned user data fields to include expanded objects and specific details.

        Args:
            id (string): id
            max_results (integer): The maximum number of list members to return per page, defaulting to 100.
            pagination_token (string): Optional token used for cursor-based pagination, allowing retrieval of the next subset of members in the list.
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
        url = f"{self.main_app_client.base_url}/2/lists/{id}/members"
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

    def list_add_member(self, id, user_id=None) -> dict[str, Any]:
        """
        Adds a user to a specified Twitter list via a POST request to the `/2/lists/{id}/members` endpoint, requiring list and user IDs. This function modifies a list's membership, distinguishing it from `list_get_members` (retrieves) and its counterpart `list_remove_member` (deletes).

        Args:
            id (string): id
            user_id (string): Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. Example: '2244994945'.

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
        request_body_data = {"user_id": user_id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/lists/{id}/members"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def delete_list_member(self, id, user_id) -> dict[str, Any]:
        """
        Removes a specific user from a Twitter list. This function sends a DELETE request to the `/2/lists/{id}/members/{user_id}` API endpoint, requiring both the list ID and the user ID to perform the action and confirm the member's removal.

        Args:
            id (string): id
            user_id (string): user_id

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
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'.")
        url = f"{self.main_app_client.base_url}/2/lists/{id}/members/{user_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_tweets(
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
        Retrieves tweets from a specified Twitter List using its ID. Supports pagination and allows extensive customization of returned fields for tweets, users, media, and other entities. This function uniquely fetches the list's tweet timeline, distinguishing it from functions that retrieve list members or followers.

        Args:
            id (string): id
            max_results (integer): The maximum number of tweets to return per request, with a default value of 100.
            pagination_token (string): Optional query parameter used to request the next page of results by passing the `next_token` value from the previous response.
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
        url = f"{self.main_app_client.base_url}/2/lists/{id}/tweets"
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

    def list_tools(self):
        return [
            self.create_list,
            self.delete_list,
            self.get_list_by_id,
            self.update_list,
            self.get_list_followers,
            self.list_get_members,
            self.list_add_member,
            self.delete_list_member,
            self.get_list_tweets,
        ]
