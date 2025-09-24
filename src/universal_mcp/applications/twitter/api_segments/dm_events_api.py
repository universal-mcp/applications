from typing import Any

from .api_segment_base import APISegmentBase


class DmEventsApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def get_dm_events(
        self,
        max_results=None,
        pagination_token=None,
        event_types=None,
        dm_event_fields=None,
        expansions=None,
        media_fields=None,
        user_fields=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of direct message events, unlike `get_dm_events_by_id` which fetches a single event. Supports pagination, filtering by event type, and specifying which data fields to return for various objects to customize the API response.

        Args:
            max_results (integer): Limits the number of DM events returned in the response, with a default of 100 if not specified.
            pagination_token (string): Optional token used to specify the starting point for paginating the response of DM events.
            event_types (array): An optional array parameter specifying the types of events to retrieve, defaulting to ["MessageCreate", "ParticipantsLeave", "ParticipantsJoin"] if not provided. Example: "['MessageCreate', 'ParticipantsLeave']".
            dm_event_fields (array): A comma separated list of DmEvent fields to display. Example: "['attachments', 'created_at', 'dm_conversation_id', 'entities', 'event_type', 'id', 'participant_ids', 'referenced_tweets', 'sender_id', 'text']".
            expansions (array): A comma separated list of fields to expand. Example: "['attachments.media_keys', 'participant_ids', 'referenced_tweets.id', 'sender_id']".
            media_fields (array): A comma separated list of Media fields to display. Example: "['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics', 'organic_metrics', 'preview_image_url', 'promoted_metrics', 'public_metrics', 'type', 'url', 'variants', 'width']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Direct Messages
        """
        url = f"{self.main_app_client.base_url}/2/dm_events"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("event_types", event_types),
                ("dm_event.fields", dm_event_fields),
                ("expansions", expansions),
                ("media.fields", media_fields),
                ("user.fields", user_fields),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_dm_event(self, event_id) -> dict[str, Any]:
        """
        Deletes a specific Direct Message (DM) event identified by its unique ID. This function issues an authenticated HTTP DELETE request to the API to permanently remove the specified event, returning a confirmation of the deletion.

        Args:
            event_id (string): event_id

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Direct Messages
        """
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'.")
        url = f"{self.main_app_client.base_url}/2/dm_events/{event_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_dm_event_by_id(
        self,
        event_id,
        dm_event_fields=None,
        expansions=None,
        media_fields=None,
        user_fields=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """
        Fetches a specific Direct Message event using its unique ID. Optional parameters allow customizing the response by selecting specific fields for the event, media, users, and tweets, and by including expanded object details. This differs from `get_dm_events`, which retrieves a list of events.

        Args:
            event_id (string): event_id
            dm_event_fields (array): A comma separated list of DmEvent fields to display. Example: "['attachments', 'created_at', 'dm_conversation_id', 'entities', 'event_type', 'id', 'participant_ids', 'referenced_tweets', 'sender_id', 'text']".
            expansions (array): A comma separated list of fields to expand. Example: "['attachments.media_keys', 'participant_ids', 'referenced_tweets.id', 'sender_id']".
            media_fields (array): A comma separated list of Media fields to display. Example: "['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics', 'organic_metrics', 'preview_image_url', 'promoted_metrics', 'public_metrics', 'type', 'url', 'variants', 'width']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Direct Messages
        """
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'.")
        url = f"{self.main_app_client.base_url}/2/dm_events/{event_id}"
        query_params = {
            k: v
            for k, v in [
                ("dm_event.fields", dm_event_fields),
                ("expansions", expansions),
                ("media.fields", media_fields),
                ("user.fields", user_fields),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [self.get_dm_events, self.delete_dm_event, self.get_dm_event_by_id]
