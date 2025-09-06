from typing import Any

from .api_segment_base import APISegmentBase


class TweetsApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def find_tweets_by_id(
        self,
        ids,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves one or more Tweets by their IDs and returns associated details, supporting optional parameters for specifying additional fields and expansions.

        Args:
            ids (array): An array of IDs for the tweets to retrieve, required for the operation.
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
        url = f"{self.main_app_client.base_url}/2/tweets"
        query_params = {
            k: v
            for k, v in [
                ("ids", ids),
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

    def create_tweet(
        self,
        card_uri=None,
        direct_message_deep_link=None,
        for_super_followers_only=None,
        geo=None,
        media=None,
        nullcast=None,
        poll=None,
        quote_tweet_id=None,
        reply=None,
        reply_settings=None,
        text=None,
    ) -> dict[str, Any]:
        """

        Creates a new tweet using the Twitter API v2, requiring an application/json payload and OAuth2 user token for authentication, and returns a 201 status upon successful creation.

        Args:
            card_uri (string): Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link.
            direct_message_deep_link (string): Link to take the conversation from the public timeline to a private Direct Message.
            for_super_followers_only (boolean): Exclusive Tweet for super followers.
            geo (object): Place ID being attached to the Tweet for geo location.
            media (object): Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.
            nullcast (boolean): Nullcasted (promoted-only) Posts do not appear in the public timeline and are not served to followers.
            poll (object): Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.
            quote_tweet_id (string): Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. Example: '1346889436626259968'.
            reply (object): Tweet information of the Tweet being replied to.
            reply_settings (string): Settings to indicate who can reply to the Tweet.
            text (string): The content of the Tweet. Example: 'Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i'.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        request_body_data = None
        request_body_data = {
            "card_uri": card_uri,
            "direct_message_deep_link": direct_message_deep_link,
            "for_super_followers_only": for_super_followers_only,
            "geo": geo,
            "media": media,
            "nullcast": nullcast,
            "poll": poll,
            "quote_tweet_id": quote_tweet_id,
            "reply": reply,
            "reply_settings": reply_settings,
            "text": text,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/tweets"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def get_tweets_compliance_stream(
        self, partition, backfill_minutes=None, start_time=None, end_time=None
    ) -> Any:
        """

        Streams compliance events for tweets in real-time, allowing for the retrieval of events such as post deletions, edits, and withholdings, as well as user account changes, using parameters like partition, backfill_minutes, start_time, and end_time.

        Args:
            partition (integer): Specifies the partition number from which to retrieve compliance stream events, with a required integer value between 1 and 4.
            backfill_minutes (integer): Optional integer parameter to specify the number of minutes of data to recover from a stream disconnection, allowing retrieval of missed tweets.
            start_time (string): Optional string parameter specifying the earliest UTC timestamp from which compliance events will be provided, formatted as YYYY-MM-DDTHH:mm:ssZ. Example: '2021-02-01T18:40:40.000Z'.
            end_time (string): The `end_time` parameter specifies the latest UTC timestamp (in ISO 8601 format) until which compliance events will be streamed. Example: '2021-02-14T18:40:40.000Z'.

        Returns:
            Any: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Compliance
        """
        url = f"{self.main_app_client.base_url}/2/tweets/compliance/stream"
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

    def tweet_counts_full_archive_search(
        self,
        query,
        start_time=None,
        end_time=None,
        since_id=None,
        until_id=None,
        next_token=None,
        pagination_token=None,
        granularity=None,
        search_count_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves the full-archive count of tweets for a specified query using the "/2/tweets/counts/all" endpoint, allowing optional filtering by start and end times, granularity, and pagination.

        Args:
            query (string): The "query" parameter is a required string used to filter tweets by specifying keywords or phrases, allowing users to retrieve counts for specific topics or hashtags. Example: '(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet'.
            start_time (string): The start_time parameter sets the earliest timestamp from which to begin counting Tweets in the full-archive matching the query, formatted as an ISO 8601 string.
            end_time (string): The end_time parameter specifies the exclusive end timestamp to limit the search query for tweet counts in ISO 8601 format.
            since_id (string): Optional parameter to return results with a Tweet ID greater than the specified ID, effectively retrieving more recent Tweets. Example: '1346889436626259968'.
            until_id (string): Returns tweet counts with Tweet IDs less than (older than) the specified Tweet ID, limiting results to those before this ID. Example: '1346889436626259968'.
            next_token (string): Optional parameter to fetch the next page of results in a paginated response, obtained from the `meta.next_token` field of the previous response.
            pagination_token (string): Used to request the next page of results, providing the value of `next_token` from the previous response to paginate through data.
            granularity (string): The **granularity** parameter specifies the time unit for retrieving tweet counts, allowing options of "minute", "hour", or "day", with "hour" as the default.
            search_count_fields (array): A comma separated list of SearchCount fields to display. Example: "['end', 'start', 'tweet_count']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        url = f"{self.main_app_client.base_url}/2/tweets/counts/all"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("start_time", start_time),
                ("end_time", end_time),
                ("since_id", since_id),
                ("until_id", until_id),
                ("next_token", next_token),
                ("pagination_token", pagination_token),
                ("granularity", granularity),
                ("search_count.fields", search_count_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tweet_counts_recent_search(
        self,
        query,
        start_time=None,
        end_time=None,
        since_id=None,
        until_id=None,
        next_token=None,
        pagination_token=None,
        granularity=None,
        search_count_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves the count of recent Tweets that match a search query over the last seven days, using the "GET" method with optional parameters for specifying start and end times, granularity, and pagination.

        Args:
            query (string): The search query to filter recent tweets for counting matching tweets. Example: '(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet'.
            start_time (string): Optional start time for the recent Tweet counts query, specified in ISO 8601 format, which determines the beginning of the time window for which Tweet counts are returned.
            end_time (string): Optional string parameter specifying the end time for the range of Tweets to be included in the count results, formatted in ISO 8601/RFC 3339.
            since_id (string): Optional parameter to retrieve recent tweet counts with IDs greater than the specified ID, returning data for tweets posted after that ID. Example: '1346889436626259968'.
            until_id (string): Optional parameter to specify the latest Tweet ID up to which the count of Tweets will be provided. Example: '1346889436626259968'.
            next_token (string): Optional parameter to paginate through results, used to retrieve the next page of tweet count data by including the token from the previous response's `meta.next_token` field.
            pagination_token (string): Optional parameter to paginate through the results, used by passing the `next_token` value from the previous response to retrieve the next page of tweet count data.
            granularity (string): The granularity parameter specifies the time interval for aggregating Tweet counts in the response, with possible values of "minute," "hour" (default), or "day".
            search_count_fields (array): A comma separated list of SearchCount fields to display. Example: "['end', 'start', 'tweet_count']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        url = f"{self.main_app_client.base_url}/2/tweets/counts/recent"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("start_time", start_time),
                ("end_time", end_time),
                ("since_id", since_id),
                ("until_id", until_id),
                ("next_token", next_token),
                ("pagination_token", pagination_token),
                ("granularity", granularity),
                ("search_count.fields", search_count_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tweets_firehose_stream(
        self,
        partition,
        backfill_minutes=None,
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

        Streams all tweets in real-time using the Firehose API, allowing parameters such as partition, backfill minutes, start and end time, and various field expansions to customize the data retrieved, which requires authentication via a Bearer Token.

        Args:
            partition (integer): A required integer parameter that specifies the partition from which to retrieve the firehose stream data.
            backfill_minutes (integer): The backfill_minutes parameter allows requesting up to five minutes of missed streaming data to be delivered upon reconnection, helping recover Tweets lost during short disconnections; it accepts an integer value from 1 to 5 and is available only with Academic Research access.
            start_time (string): Optional ISO 8601-formatted timestamp indicating the earliest time from which to retrieve tweets, allowing filtering by time period. Example: '2021-02-14T18:40:40.000Z'.
            end_time (string): The end_time parameter specifies the exclusive upper bound timestamp to filter tweets created before this time in the stream. Example: '2021-02-14T18:40:40.000Z'.
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
        url = f"{self.main_app_client.base_url}/2/tweets/firehose/stream"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
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

    def get_tweets_firehose_stream_lang_en(
        self,
        partition,
        backfill_minutes=None,
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

        Connects to the Twitter Firehose streaming API to receive a real-time stream of English-language tweets with optional filtering and data field expansions.

        Args:
            partition (integer): The `partition` parameter is an integer value required in the query for the GET operation at path "/2/tweets/firehose/stream/lang/en", specifying the partition number for the stream.
            backfill_minutes (integer): Requests up to five minutes of missed streaming data to be delivered upon reconnection, useful for recovering data lost during brief disconnections.
            start_time (string): Optional string parameter specifying the start time in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ) to filter the oldest Tweets included in the response. Example: '2021-02-14T18:40:40.000Z'.
            end_time (string): Optional parameter to specify the end time for filtering tweets in the firehose stream, allowing retrieval of tweets created before this time. Example: '2021-02-14T18:40:40.000Z'.
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
        url = f"{self.main_app_client.base_url}/2/tweets/firehose/stream/lang/en"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
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

    def get_tweets_firehose_stream_lang_ja(
        self,
        partition,
        backfill_minutes=None,
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

        Retrieves a stream of Tweets in Japanese using the Firehose API, allowing for real-time access to a high-volume stream of Tweets based on specified parameters such as partitions and optional backfill minutes, start and end times, and customizable fields for Tweets, users, and media.

        Args:
            partition (integer): The partition number used to identify and organize the data stream, which is required for this operation.
            backfill_minutes (integer): The number of minutes (1 to 5) of missed streaming data to backfill and recover upon reconnection, available only with Academic Research access.
            start_time (string): The start_time parameter specifies the oldest UTC timestamp in ISO 8601 format from which Tweets will be provided, inclusive and in second granularity. Example: '2021-02-14T18:40:40.000Z'.
            end_time (string): Optional query parameter to specify the end time for retrieving Tweets in the format compatible with the API's date and time requirements, limiting the results to those created before this time. Example: '2021-02-14T18:40:40.000Z'.
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
        url = f"{self.main_app_client.base_url}/2/tweets/firehose/stream/lang/ja"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
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

    def get_tweets_firehose_stream_lang_ko(
        self,
        partition,
        backfill_minutes=None,
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

        Streams real-time tweets in Korean from the Twitter firehose, allowing for optional backfill, specific partitions, and customizable start and end times, with support for various tweet, media, poll, user, and place fields.

        Args:
            partition (integer): The partition parameter specifies the integer partition number to use for streaming tweets.
            backfill_minutes (integer): The number of minutes (1 to 5) of previously missed Tweets to backfill and deliver upon reconnection, allowing recovery of up to five minutes of data missed during a disconnection; duplicates may occur and this feature requires Academic Research access.
            start_time (string): The "start_time" parameter specifies the earliest UTC timestamp from which Tweets should be retrieved, formatted as YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). Example: '2021-02-14T18:40:40.000Z'.
            end_time (string): end_time: Optional query parameter to specify the exclusive upper bound timestamp for filtering Tweets in the stream, returning only those created before this time. Example: '2021-02-14T18:40:40.000Z'.
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
        url = f"{self.main_app_client.base_url}/2/tweets/firehose/stream/lang/ko"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
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

    def get_tweets_firehose_stream_lang_pt(
        self,
        partition,
        backfill_minutes=None,
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

        Streams real-time Tweets in Portuguese using the Firehose API, allowing for filtering by specific parameters such as tweet fields, expansions, media, polls, users, and places, and requires a partition number for the stream.

        Args:
            partition (integer): The **partition** parameter is a required integer that specifies the partition number for the GET operation at the "/2/tweets/firehose/stream/lang/pt" path, used to distribute the stream of tweets across multiple partitions for efficient processing.
            backfill_minutes (integer): The number of minutes (1-5) of missed streaming data to recover and deliver upon reconnection, available only for Academic Research access.
            start_time (string): The "start_time" parameter specifies the starting point for retrieving Tweets, expressed in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ), indicating the earliest UTC timestamp for which to include Tweets. Example: '2021-02-14T18:40:40.000Z'.
            end_time (string): The `end_time` parameter specifies the timestamp, in ISO 8601 format, after which tweets are not included in the response, allowing filtering of the firehose stream by a specific end time. Example: '2021-02-14T18:40:40.000Z'.
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
        url = f"{self.main_app_client.base_url}/2/tweets/firehose/stream/lang/pt"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
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

    def get_tweets_label_stream(
        self, backfill_minutes=None, start_time=None, end_time=None
    ) -> Any:
        """

        Streams tweets labeled with a specific identifier in real-time using the Twitter API, allowing for optional parameters to specify backfill minutes, start time, and end time, and requires authentication via a Bearer Token.

        Args:
            backfill_minutes (integer): The number of minutes (up to five) of missed tweet data to recover and backfill after a disconnection, available for Academic Research access.
            start_time (string): Optional parameter specifying the earliest UTC timestamp (in ISO 8601/RFC 3339 format) from which to retrieve tweets, allowing filtering by creation time. Example: '2021-02-01T18:40:40.000Z'.
            end_time (string): Optional parameter specifying the end time in ISO 8601 format for retrieving tweets from a label stream, used to filter tweets created before this time. Example: '2021-02-01T18:40:40.000Z'.

        Returns:
            Any: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Compliance
        """
        url = f"{self.main_app_client.base_url}/2/tweets/label/stream"
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

    def sample_stream(
        self,
        backfill_minutes=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a real-time sampled stream of public Tweets with optional parameters to specify Tweet, user, media, poll, and place fields, supporting backfill for missed data.

        Args:
            backfill_minutes (integer): The number of minutes (1 to 5) of missed streaming Tweets to backfill and receive upon reconnection, available for Academic Research access.
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
        url = f"{self.main_app_client.base_url}/2/tweets/sample/stream"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
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

    def get_tweets_sample_stream(
        self,
        partition,
        backfill_minutes=None,
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

        Streams a random sample of 10% of all Tweets in real-time, allowing optional filtering by specifying additional parameters such as backfill minutes, partition, start and end times, and various field expansions for tweets, media, polls, users, and places.

        Args:
            partition (integer): The "partition" parameter specifies the partition number for the stream, which is required for the GET operation at path "/2/tweets/sample10/stream".
            backfill_minutes (integer): The `backfill_minutes` parameter allows you to request up to five minutes of missed streaming data to be delivered upon reconnection, helping recover data lost during disconnections; it is only available for Academic Research access.
            start_time (string): The `start_time` parameter specifies the earliest UTC timestamp from which tweets are returned, formatted as YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339), and is inclusive. Example: '2021-02-14T18:40:40.000Z'.
            end_time (string): An optional string parameter specifying the end time in seconds since the Unix epoch for which to stop streaming Tweets. Example: '2021-02-14T18:40:40.000Z'.
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
        url = f"{self.main_app_client.base_url}/2/tweets/sample10/stream"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
                ("partition", partition),
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

    def tweets_fullarchive_search(
        self,
        query,
        start_time=None,
        end_time=None,
        since_id=None,
        until_id=None,
        max_results=None,
        next_token=None,
        pagination_token=None,
        sort_order=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves and returns a list of historical Tweets matching a specified query, allowing for filtering by time range, tweet ID, and other parameters.

        Args:
            query (string): The "query" parameter is a required string input used to specify the search criteria for retrieving tweets. Example: '(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet'.
            start_time (string): Optional timestamp specifying the earliest date and time from which to retrieve Tweets, formatted as YYYY-MM-DDTHH:mm:ssZ in ISO 8601/RFC 3339 format; if not specified and end_time is provided, it defaults to 30 days before end_time.
            end_time (string): The **end_time** parameter specifies the most recent UTC timestamp (in ISO 8601/RFC 3339 format) up to which tweets are returned, exclusive of the specified time.
            since_id (string): Optional parameter to return results with IDs greater than (more recent than) the specified ID, useful for fetching new tweets since the last query. Example: '1346889436626259968'.
            until_id (string): Optional parameter specifying the Tweet ID to return results with IDs less than (i.e., older than) the given ID. Example: '1346889436626259968'.
            max_results (integer): Specifies the maximum number of Tweets to return per response page, with a default value of 10.
            next_token (string): Optional parameter used for pagination; it specifies a token to retrieve the next page of results in the search query response.
            pagination_token (string): The pagination_token query parameter is used to retrieve the next page of results by passing the next_token value returned in the previous response, enabling pagination through large result sets.
            sort_order (string): Optional query parameter to specify the order in which tweets are returned, either by most recent first ("recency") or by most relevant first ("relevancy").
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
        url = f"{self.main_app_client.base_url}/2/tweets/search/all"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("start_time", start_time),
                ("end_time", end_time),
                ("since_id", since_id),
                ("until_id", until_id),
                ("max_results", max_results),
                ("next_token", next_token),
                ("pagination_token", pagination_token),
                ("sort_order", sort_order),
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

    def tweets_recent_search(
        self,
        query,
        start_time=None,
        end_time=None,
        since_id=None,
        until_id=None,
        max_results=None,
        next_token=None,
        pagination_token=None,
        sort_order=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves recent tweets based on a specified search query, allowing for optional filtering by time range and additional parameters such as tweet fields, expansions, and user details.

        Args:
            query (string): A string parameter used to specify the search query for retrieving recent tweets. Example: '(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet'.
            start_time (string): Optional parameter to specify the earliest time to search for tweets, formatted as ISO8601/RFC3339 (e.g., 2023-05-12T00:00:00Z).
            end_time (string): Optional parameter to specify the UTC timestamp (in YYYY-MM-DDTHH:mm:ssZ format) up to which the returned Tweets are retrieved, exclusive of the specified time.
            since_id (string): Optional parameter to return results with an ID greater than the specified ID, retrieving more recent tweets. Example: '1346889436626259968'.
            until_id (string): Returns results with an ID less than (older than) the specified ID, limiting the search to tweets older than that ID. Example: '1346889436626259968'.
            max_results (integer): The "max_results" parameter specifies the maximum number of recent tweets to return per response page, with a default of 10 and a maximum of 100.
            next_token (string): Optional query parameter used to paginate results, specifying the token from a previous response to fetch the next page of tweets.
            pagination_token (string): Used to request the next page of results by passing the `next_token` value from the previous response.
            sort_order (string): Optional parameter to specify the order of search results, either by "recency" (most recent first) or "relevancy" (most relevant first).
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
        url = f"{self.main_app_client.base_url}/2/tweets/search/recent"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("start_time", start_time),
                ("end_time", end_time),
                ("since_id", since_id),
                ("until_id", until_id),
                ("max_results", max_results),
                ("next_token", next_token),
                ("pagination_token", pagination_token),
                ("sort_order", sort_order),
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

    def search_stream(
        self,
        backfill_minutes=None,
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

        Streams tweets based on predefined rules using the Twitter API v2, allowing for real-time filtering and retrieval of tweets with optional parameters for backfill minutes, start and end times, and various tweet, media, poll, user, and place fields.

        Args:
            backfill_minutes (integer): The "backfill_minutes" parameter allows clients to request up to five minutes of missed data upon reconnection, helping to recover Tweets that were missed due to a disconnection.
            start_time (string): The "start_time" parameter specifies the earliest UTC timestamp (in ISO 8601 format) from which to include Tweets in the search results. Example: '2021-02-01T18:40:40.000Z'.
            end_time (string): The timestamp (in ISO 8601/RFC 3339 format) specifying the exclusive upper bound of the time range for which Tweets will be returned. Example: '2021-02-14T18:40:40.000Z'.
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
        url = f"{self.main_app_client.base_url}/2/tweets/search/stream"
        query_params = {
            k: v
            for k, v in [
                ("backfill_minutes", backfill_minutes),
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

    def get_rules(
        self, ids=None, max_results=None, pagination_token=None
    ) -> dict[str, Any]:
        """

        Retrieves the active stream filtering rules for a user's Twitter API v2 filtered stream, optionally filtered by rule IDs, with support for pagination and maximum results.

        Args:
            ids (array): Optional array of rule IDs to fetch a subset of rules from the user's active rule set.
            max_results (integer): The maximum number of stream filtering rules to return per response, up to 1000; defaults to 1000 if not specified.
            pagination_token (string): The `pagination_token` parameter is a string used to request the next page of results in a paginated response, typically obtained from the `next_token` value in the previous response.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        url = f"{self.main_app_client.base_url}/2/tweets/search/stream/rules"
        query_params = {
            k: v
            for k, v in [
                ("ids", ids),
                ("max_results", max_results),
                ("pagination_token", pagination_token),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_or_delete_rules(
        self, dry_run=None, delete_all=None, add=None, delete=None
    ) -> dict[str, Any]:
        """

        Adds or removes rules from a Twitter API v2 filtered stream using a POST request, allowing for optional dry-run or delete-all parameters.

        Args:
            dry_run (boolean): Indicates whether to test the syntax of the rule without applying it to the stream, allowing validation of rule changes without taking effect.
            delete_all (boolean): Indicates whether to delete all existing rules for the user before applying new rules; if true, all existing rules will be deleted.
            add (array): add
            delete (object): IDs and values of all deleted user-specified stream filtering rules.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        request_body_data = None
        request_body_data = {"add": add, "delete": delete}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/tweets/search/stream/rules"
        query_params = {
            k: v
            for k, v in [("dry_run", dry_run), ("delete_all", delete_all)]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def get_rule_count(self, rules_count_fields=None) -> dict[str, Any]:
        """

        Retrieves the counts of Tweets matching specific search rules using the "GET" method, providing a way to analyze the volume of Tweets based on predefined criteria.

        Args:
            rules_count_fields (array): A comma separated list of RulesCount fields to display. Example: "['all_project_client_apps', 'cap_per_client_app', 'cap_per_project', 'client_app_rules_count', 'project_rules_count']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            General
        """
        url = f"{self.main_app_client.base_url}/2/tweets/search/stream/rules/counts"
        query_params = {
            k: v
            for k, v in [("rules_count.fields", rules_count_fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tweet_by_id(self, id) -> dict[str, Any]:
        """

        Deletes a specified Tweet by its ID on behalf of an authenticated user.

        Args:
            id (string): id

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
        url = f"{self.main_app_client.base_url}/2/tweets/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_tweet_by_id(
        self,
        id,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves detailed information about a single Tweet specified by its unique ID, with optional expansions for fields related to the Tweet, user, media, polls, and places.

        Args:
            id (string): id
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
        url = f"{self.main_app_client.base_url}/2/tweets/{id}"
        query_params = {
            k: v
            for k, v in [
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

    def tweets_id_liking_users(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of users who have liked a specified tweet using the provided tweet ID.

        Args:
            id (string): id
            max_results (integer): Specifies the maximum number of liking users to return in a response, with a default value of 100 and a maximum allowed value of 100.
            pagination_token (string): The pagination_token query parameter is an optional token used to retrieve the next page of results in a paginated response for the list of users who liked the tweet.
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
        url = f"{self.main_app_client.base_url}/2/tweets/{id}/liking_users"
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

    def find_tweets_that_quote_atweet(
        self,
        id,
        max_results=None,
        pagination_token=None,
        exclude=None,
        tweet_fields=None,
        expansions=None,
        media_fields=None,
        poll_fields=None,
        user_fields=None,
        place_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of quote Tweets for a specified Tweet ID, allowing for optional parameters to customize the results with fields like tweet fields, media fields, and user expansions, and supports pagination for handling large responses.

        Args:
            id (string): id
            max_results (integer): Specifies the maximum number of quote Tweets to return in the response, ranging from 1 to 100, with a default of 10.
            pagination_token (string): pagination_token is an optional query parameter used to retrieve the next page of results by setting it to the next_token value returned in the previous response.
            exclude (array): Optional array parameter to exclude specific types of Tweet results from the response, such as retweets. Example: "['replies', 'retweets']".
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
        url = f"{self.main_app_client.base_url}/2/tweets/{id}/quote_tweets"
        query_params = {
            k: v
            for k, v in [
                ("max_results", max_results),
                ("pagination_token", pagination_token),
                ("exclude", exclude),
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

    def tweets_id_retweeting_users(
        self,
        id,
        max_results=None,
        pagination_token=None,
        user_fields=None,
        expansions=None,
        tweet_fields=None,
    ) -> dict[str, Any]:
        """

        Retrieves a list of User objects representing users who have retweeted the Tweet specified by the given Tweet ID.

        Args:
            id (string): id
            max_results (integer): The `max_results` parameter specifies the maximum number of users to return who have retweeted the specified Tweet, with a default value of 100 and a required range of 1 to 100.
            pagination_token (string): Optional parameter used to retrieve the next page of results by passing the value of the `next_token` returned in the previous response.
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
        url = f"{self.main_app_client.base_url}/2/tweets/{id}/retweeted_by"
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

    def find_tweets_that_retweet_atweet(
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

        Retrieves a list of retweets for a specified Tweet ID, optionally allowing for pagination and customization of returned fields via query parameters.

        Args:
            id (string): id
            max_results (integer): Specifies the maximum number of retweets to return per request, with a default of 100 and a maximum value of 100.
            pagination_token (string): Used to request the next page of results, set this parameter to the `next_token` value returned in the previous response.
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
        url = f"{self.main_app_client.base_url}/2/tweets/{id}/retweets"
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

    def hide_reply_by_id(self, tweet_id, hidden=None) -> dict[str, Any]:
        """

        Hides or unhides a reply to a specified Tweet by its tweet_id.

        Args:
            tweet_id (string): tweet_id
            hidden (boolean): hidden

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tweets
        """
        if tweet_id is None:
            raise ValueError("Missing required parameter 'tweet_id'.")
        request_body_data = None
        request_body_data = {"hidden": hidden}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/tweets/{tweet_id}/hidden"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.find_tweets_by_id,
            self.create_tweet,
            self.get_tweets_compliance_stream,
            self.tweet_counts_full_archive_search,
            self.tweet_counts_recent_search,
            self.get_tweets_firehose_stream,
            self.get_tweets_firehose_stream_lang_en,
            self.get_tweets_firehose_stream_lang_ja,
            self.get_tweets_firehose_stream_lang_ko,
            self.get_tweets_firehose_stream_lang_pt,
            self.get_tweets_label_stream,
            self.sample_stream,
            self.get_tweets_sample_stream,
            self.tweets_fullarchive_search,
            self.tweets_recent_search,
            self.search_stream,
            self.get_rules,
            self.add_or_delete_rules,
            self.get_rule_count,
            self.delete_tweet_by_id,
            self.find_tweet_by_id,
            self.tweets_id_liking_users,
            self.find_tweets_that_quote_atweet,
            self.tweets_id_retweeting_users,
            self.find_tweets_that_retweet_atweet,
            self.hide_reply_by_id,
        ]
