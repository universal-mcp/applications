from typing import Any

from .api_segment_base import APISegmentBase


class DmConversationsApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def dm_conversation_id_create(
        self, conversation_type=None, message=None, participant_ids=None
    ) -> dict[str, Any]:
        """

        Creates a new group Direct Message conversation and sends an initial message to the specified participants.

        Args:
            conversation_type (string): The conversation type that is being created.
            message (string): message
            participant_ids (array): Participants for the DM Conversation.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Direct Messages
        """
        request_body_data = None
        request_body_data = {
            "conversation_type": conversation_type,
            "message": message,
            "participant_ids": participant_ids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/dm_conversations"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def get_dm_convo_with_patcpnts_id_dm_evnts(
        self,
        participant_id,
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

        Retrieves a list of direct message events for a conversation with a specific participant, allowing for optional filtering by event types and pagination.

        Args:
            participant_id (string): participant_id
            max_results (integer): The maximum number of direct message events to return in the response, with a default of 100.
            pagination_token (string): The opaque token used to retrieve the next page of direct message events in the conversation with the specified participant.
            event_types (array): An optional array parameter specifying the types of DM events to include, such as "MessageCreate", "ParticipantsLeave", and "ParticipantsJoin", with default values of "MessageCreate", "ParticipantsLeave", and "ParticipantsJoin". Example: "['MessageCreate', 'ParticipantsLeave']".
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
        if participant_id is None:
            raise ValueError("Missing required parameter 'participant_id'.")
        url = f"{self.main_app_client.base_url}/2/dm_conversations/with/{participant_id}/dm_events"
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

    def dm_conversation_with_user_event_id_create(
        self, participant_id, attachments=None, text=None
    ) -> dict[str, Any]:
        """

        Creates a new one-to-one Direct Message conversation with the specified participant or adds a message to an existing conversation using the X API.

        Args:
            participant_id (string): participant_id
            attachments (array): Attachments to a DM Event.
            text (string): Text of the message.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Direct Messages
        """
        if participant_id is None:
            raise ValueError("Missing required parameter 'participant_id'.")
        request_body_data = None
        request_body_data = {"attachments": attachments, "text": text}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/dm_conversations/with/{participant_id}/messages"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def dm_conversation_by_id_event_id_create(
        self, dm_conversation_id, attachments=None, text=None
    ) -> dict[str, Any]:
        """

        Creates a new Direct Message and adds it to an existing conversation specified by the provided dm_conversation_id.

        Args:
            dm_conversation_id (string): dm_conversation_id
            attachments (array): Attachments to a DM Event.
            text (string): Text of the message.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Direct Messages
        """
        if dm_conversation_id is None:
            raise ValueError("Missing required parameter 'dm_conversation_id'.")
        request_body_data = None
        request_body_data = {"attachments": attachments, "text": text}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/dm_conversations/{dm_conversation_id}/messages"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def get_dm_conversations_id_dm_events(
        self,
        id,
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

        Retrieves a list of direct message events for a specified conversation ID, allowing for optional filtering by event types and pagination.

        Args:
            id (string): id
            max_results (integer): Limits the number of DM events returned in the response, with a default value of 100, allowing users to customize the amount of data retrieved.
            pagination_token (string): Optional token used to paginate responses, specifying the resource to start fetching from for the next page of DM events.
            event_types (array): Filter the types of direct message events to return, such as message creation, participants joining, or leaving; defaults to ["MessageCreate","ParticipantsLeave","ParticipantsJoin"]. Example: "['MessageCreate', 'ParticipantsLeave']".
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
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/dm_conversations/{id}/dm_events"
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

    def list_tools(self):
        return [
            self.dm_conversation_id_create,
            self.get_dm_convo_with_patcpnts_id_dm_evnts,
            self.dm_conversation_with_user_event_id_create,
            self.dm_conversation_by_id_event_id_create,
            self.get_dm_conversations_id_dm_events,
        ]
