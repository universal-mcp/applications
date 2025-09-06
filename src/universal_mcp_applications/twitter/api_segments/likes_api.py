from typing import Any

from .api_segment_base import APISegmentBase


class LikesApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def get_likes_compliance_stream(
        self, backfill_minutes=None, start_time=None, end_time=None
    ) -> Any:
        """

        Streams compliance-related likes data using the GET method, allowing optional filtering by backfill minutes and time range.

        Args:
            backfill_minutes (integer): Specifies the number of minutes of missed data to recover in case of a disconnection, allowing retrieval of up to five minutes of past data.
            start_time (string): The optional start_time query parameter specifies the earliest timestamp from which to retrieve compliance stream data. Example: '2021-02-01T18:40:40.000Z'.
            end_time (string): Optional end time to filter the compliance stream, specified as a string. Example: '2021-02-01T18:40:40.000Z'.

        Returns:
            Any: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Compliance
        """
        url = f"{self.main_app_client.base_url}/2/likes/compliance/stream"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("start_time", start_time),
                ("end_time", end_time),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def likes_firehose_stream(
        self,
        partition,
        backfill_minutes=None,
        start_time=None,
        end_time=None,
        like_with_tweet_author_fields=None,
        expansions=None,
        user_fields=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Streams a real-time firehose of likes data filtered by partition and optional time range parameters, including expanded tweet and user fields, using Bearer Token authentication.

        Args:
            partition (integer): The partition query parameter specifies the integer identifier of the data subset or bucket to stream from the firehose endpoint, enabling segmented retrieval of likes data.
            backfill_minutes (integer): The number of minutes (up to five) to backfill and recover missed data from the stream after a disconnection.
            start_time (string): Optional query parameter specifying the start time for filtering the firehose stream of likes. Example: '2021-02-14T18:40:40.000Z'.
            end_time (string): The end_time query parameter specifies the optional cutoff timestamp to limit the data streamed to only items created before this time. Example: '2021-02-14T18:40:40.000Z'.
            like_with_tweet_author_fields (array): A comma separated list of LikeWithTweetAuthor fields to display. Example: "['created_at', 'id', 'liked_tweet_author_id', 'liked_tweet_id', 'timestamp_ms']".
            expansions (array): A comma separated list of fields to expand. Example: "['liked_tweet_author_id', 'liked_tweet_id']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Likes
        """
        url = f"{self.main_app_client.base_url}/2/likes/firehose/stream"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
                ("start_time", start_time),
                ("end_time", end_time),
                ("like_with_tweet_author.fields", like_with_tweet_author_fields),
                ("expansions", expansions),
                ("user.fields", user_fields),
                ("tweet.fields", tweet_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def likes_sample_stream(
        self,
        partition,
        backfill_minutes=None,
        start_time=None,
        end_time=None,
        like_with_tweet_author_fields=None,
        expansions=None,
        user_fields=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Streams a sample of 10 likes using the GET method, optionally filtering by backfill minutes, partition, start and end times, and including specific tweet and user fields.

        Args:
            partition (integer): The partition query parameter specifies the integer identifier of the data partition to retrieve in the sample10 likes stream.
            backfill_minutes (integer): Optional integer parameter to specify the number of minutes of missed data to recover, used for reconnecting after a disconnection in the stream.
            start_time (string): Optional query parameter specifying the start time for filtering the stream of likes; defaults to no filtering if omitted. Example: '2021-02-14T18:40:40.000Z'.
            end_time (string): Optional query parameter specifying the end time for filtering the sample stream of likes. Example: '2021-02-14T18:40:40.000Z'.
            like_with_tweet_author_fields (array): A comma separated list of LikeWithTweetAuthor fields to display. Example: "['created_at', 'id', 'liked_tweet_author_id', 'liked_tweet_id', 'timestamp_ms']".
            expansions (array): A comma separated list of fields to expand. Example: "['liked_tweet_author_id', 'liked_tweet_id']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Likes
        """
        url = f"{self.main_app_client.base_url}/2/likes/sample10/stream"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
                ("start_time", start_time),
                ("end_time", end_time),
                ("like_with_tweet_author.fields", like_with_tweet_author_fields),
                ("expansions", expansions),
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
            self.get_likes_compliance_stream,
            self.likes_firehose_stream,
            self.likes_sample_stream,
        ]
