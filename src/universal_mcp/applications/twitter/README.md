# TwitterApp MCP Server

An MCP Server for the TwitterApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the TwitterApp API.


| Tool | Description |
|------|-------------|
| `list_batch_compliance_jobs` | Retrieves a list of compliance jobs based on the specified job type, with optional filtering by status. |
| `create_batch_compliance_job` | Creates a new compliance job using JSON data in the request body and authenticates the request using a Bearer token. |
| `get_batch_compliance_job` | Retrieves information about a compliance job by its ID using the BearerToken for authentication. |
| `dm_conversation_id_create` | Creates a new group Direct Message conversation and sends an initial message to the specified participants. |
| `get_dm_convo_with_patcpnts_id_dm_evnts` | Retrieves a list of direct message events for a conversation with a specific participant, allowing for optional filtering by event types and pagination. |
| `get_dm_conversations_id_dm_events` | Retrieves a list of direct message events for a specified conversation ID, allowing for optional filtering by event types and pagination. |
| `get_dm_events` | Retrieves a list of direct message events with optional filtering by event types, pagination, and field expansions for media, users, tweets, and DM event details. |
| `dm_event_delete` | Deletes a DM event by its ID using the DELETE method, requiring authentication via OAuth2UserToken with "dm.read" and "dm.write" scopes or UserToken. |
| `get_dm_events_by_id` | Retrieves detailed information about a specific direct message event by its event ID with optional expansions and field selections. |
| `get_likes_compliance_stream` | Streams compliance-related likes data using the GET method, allowing optional filtering by backfill minutes and time range. |
| `likes_firehose_stream` | Streams a real-time firehose of likes data filtered by partition and optional time range parameters, including expanded tweet and user fields, using Bearer Token authentication. |
| `likes_sample10_stream` | Streams a sample of 10 likes using the GET method, optionally filtering by backfill minutes, partition, start and end times, and including specific tweet and user fields. |
| `list_id_create` | Creates a new Twitter list using the X API v2 and returns the newly created list's details. |
| `list_id_delete` | Deletes a list specified by its ID using the DELETE method. |
| `list_id_get` | Retrieves detailed information about a specific Twitter List by its unique identifier, including optional expansions and fields for lists and users. |
| `list_id_update` | Updates a list specified by the ID using the provided JSON payload, authenticating with OAuth2 or user tokens. |
| `list_get_followers` | Retrieves a list of users who follow a specified Twitter list using the list ID, with optional parameters for pagination and user data customization. |
| `list_get_members` | Retrieves a list of User objects that are members of a specified Twitter List by the provided List ID. |
| `list_add_member` | Adds one or more members to a specified list by list ID using the POST method. |
| `list_remove_member` | Removes a member from a list using the provided list ID and user ID, requiring appropriate permissions for the operation. |
| `lists_id_tweets` | Retrieves a list of tweets for a specified list by ID using the "GET" method, allowing optional parameters for pagination and field customization. |
| `get_open_api_spec` | Retrieves the OpenAPI JSON file at the specified path "/2/openapi.json" using the GET method. |
| `find_spaces_by_ids` | Retrieves detailed information about specified spaces using the "GET" method, allowing customization through parameters such as space IDs, space fields, space expansions, user fields, and topic fields, while requiring authentication via Bearer or OAuth2 tokens for authorized access. |
| `find_spaces_by_creator_ids` | Retrieves a list of spaces by their creator IDs using the specified user IDs, with optional filtering by space fields, space expansions, user fields, and topic fields. |
| `search_spaces` | Searches for spaces using the specified query and optional filters like state, and returns the results with customizable fields and expansions. |
| `find_space_by_id` | Retrieves details about a specific space by its ID, allowing optional customization through space fields, space expansions, user fields, and topic fields, using a Bearer or OAuth2 token for authentication. |
| `space_buyers` | Retrieves a list of buyers for a specific space using the "GET" method, allowing optional pagination and customization of returned user and tweet fields. |
| `space_tweets` | Retrieves a list of tweets from a specified Twitter Space by its ID, with optional parameters to customize the fields and expansions included in the response. |
| `get_trends` | Retrieves trending information by WOEID (Where On Earth ID) using the specified trend fields and returns a response with a valid Bearer token. |
| `find_tweets_by_id` | Retrieves one or more Tweets by their IDs and returns associated details, supporting optional parameters for specifying additional fields and expansions. |
| `create_tweet` | Creates a new tweet using the Twitter API v2, requiring an application/json payload and OAuth2 user token for authentication, and returns a 201 status upon successful creation. |
| `get_tweets_compliance_stream` | Streams compliance events for tweets in real-time, allowing for the retrieval of events such as post deletions, edits, and withholdings, as well as user account changes, using parameters like partition, backfill_minutes, start_time, and end_time. |
| `tweet_counts_full_archive_search` | Retrieves the full-archive count of tweets for a specified query using the "/2/tweets/counts/all" endpoint, allowing optional filtering by start and end times, granularity, and pagination. |
| `tweet_counts_recent_search` | Retrieves the count of recent Tweets that match a search query over the last seven days, using the "GET" method with optional parameters for specifying start and end times, granularity, and pagination. |
| `get_tweets_firehose_stream` | Streams all tweets in real-time using the Firehose API, allowing parameters such as partition, backfill minutes, start and end time, and various field expansions to customize the data retrieved, which requires authentication via a Bearer Token. |
| `get_tweets_firehose_stream_lang_en` | Connects to the Twitter Firehose streaming API to receive a real-time stream of English-language tweets with optional filtering and data field expansions. |
| `get_tweets_firehose_stream_lang_ja` | Retrieves a stream of Tweets in Japanese using the Firehose API, allowing for real-time access to a high-volume stream of Tweets based on specified parameters such as partitions and optional backfill minutes, start and end times, and customizable fields for Tweets, users, and media. |
| `get_tweets_firehose_stream_lang_ko` | Streams real-time tweets in Korean from the Twitter firehose, allowing for optional backfill, specific partitions, and customizable start and end times, with support for various tweet, media, poll, user, and place fields. |
| `get_tweets_firehose_stream_lang_pt` | Streams real-time Tweets in Portuguese using the Firehose API, allowing for filtering by specific parameters such as tweet fields, expansions, media, polls, users, and places, and requires a partition number for the stream. |
| `get_tweets_label_stream` | Streams tweets labeled with a specific identifier in real-time using the Twitter API, allowing for optional parameters to specify backfill minutes, start time, and end time, and requires authentication via a Bearer Token. |
| `sample_stream` | Retrieves a real-time sampled stream of public Tweets with optional parameters to specify Tweet, user, media, poll, and place fields, supporting backfill for missed data. |
| `get_tweets_sample10_stream` | Streams a random sample of 10% of all Tweets in real-time, allowing optional filtering by specifying additional parameters such as backfill minutes, partition, start and end times, and various field expansions for tweets, media, polls, users, and places. |
| `tweets_fullarchive_search` | Retrieves and returns a list of historical Tweets matching a specified query, allowing for filtering by time range, tweet ID, and other parameters. |
| `tweets_recent_search` | Retrieves recent tweets based on a specified search query, allowing for optional filtering by time range and additional parameters such as tweet fields, expansions, and user details. |
| `search_stream` | Streams tweets based on predefined rules using the Twitter API v2, allowing for real-time filtering and retrieval of tweets with optional parameters for backfill minutes, start and end times, and various tweet, media, poll, user, and place fields. |
| `get_rules` | Retrieves the active stream filtering rules for a user's Twitter API v2 filtered stream, optionally filtered by rule IDs, with support for pagination and maximum results. |
| `get_rule_count` | Retrieves the counts of Tweets matching specific search rules using the "GET" method, providing a way to analyze the volume of Tweets based on predefined criteria. |
| `delete_tweet_by_id` | Deletes a specified Tweet by its ID on behalf of an authenticated user. |
| `find_tweet_by_id` | Retrieves detailed information about a single Tweet specified by its unique ID, with optional expansions for fields related to the Tweet, user, media, polls, and places. |
| `tweets_id_liking_users` | Retrieves a list of users who have liked a specified tweet using the provided tweet ID. |
| `find_tweets_that_quote_atweet` | Retrieves a list of quote Tweets for a specified Tweet ID, allowing for optional parameters to customize the results with fields like tweet fields, media fields, and user expansions, and supports pagination for handling large responses. |
| `tweets_id_retweeting_users` | Retrieves a list of User objects representing users who have retweeted the Tweet specified by the given Tweet ID. |
| `find_tweets_that_retweet_atweet` | Retrieves a list of retweets for a specified Tweet ID, optionally allowing for pagination and customization of returned fields via query parameters. |
| `hide_reply_by_id` | Hides or unhides a reply to a specified Tweet by its tweet_id. |
| `get_usage_tweets` | Retrieves and returns Twitter usage data using the specified fields and optionally filters by a number of days. |
| `find_users_by_id` | Retrieves information about one or more users specified by their IDs, allowing for customization with user fields and expansions. |
| `find_users_by_username` | Retrieves information about one or more users specified by their usernames using the Twitter API, allowing optional specification of additional user fields and expansions. |
| `find_user_by_username` | Retrieves information about a user specified by their username, optionally including additional fields and expansions, using the "GET" method with authentication. |
| `get_users_compliance_stream` | Streams compliance data for users using the "GET" method, supporting optional backfill minutes, start and end times, and requiring a partition parameter. |
| `find_my_user` | Retrieves detailed information about the authenticated user, including optional expansions and fields for user and tweet data. |
| `search_user_by_query` | Searches for users using a query string, returning a list of matching users with optional fields for user details, expansions, and related tweet fields. |
| `find_user_by_id` | Retrieves information about a user specified by their ID, with optional parameters for specifying additional user fields, expansions, and tweet fields. |
| `users_id_blocking` | Retrieves a list of user objects that are blocked by the specified user ID, allowing for additional fields and expansions to be specified. |
| `get_users_id_bookmarks` | Retrieves a list of bookmarks for a user with the specified ID, allowing optional pagination and customization of returned fields. |
| `post_users_id_bookmarks` | Adds bookmarks for a specified user using the provided JSON data and returns a successful response upon completion. |
| `users_id_bookmarks_delete` | Deletes a bookmarked tweet for a specified user using the "DELETE" method. |
| `user_followed_lists` | Retrieves a list of Twitter lists followed by a specified user, with optional parameters for pagination, list fields, and user fields. |
| `list_user_follow` | Adds a Twitter user to a list of followed lists using the Twitter API and returns a status message. |
| `list_user_unfollow` | Deletes the specified list followed by the user identified by the given user ID and list ID. |
| `users_id_followers` | Retrieves a list of users who follow a specified user using the Twitter API, with optional parameters for result pagination and additional user or tweet fields. |
| `users_id_following` | Retrieves a list of users followed by the specified user ID, allowing optional parameters to customize the response with additional user fields, expansions, and tweet fields. |
| `users_id_follow` | Follows another user on behalf of the current user using the Twitter API, returning a status message indicating whether the action was successful. |
| `users_id_liked_tweets` | Retrieves a list of tweets liked by the specified user, supporting pagination and optional expansions and fields for tweets, users, media, polls, and places. |
| `users_id_like` | Creates a new like for a user's content using the provided user ID and returns a status message. |
| `users_id_unlike` | Deletes a user's like on a specific tweet using the provided user ID and tweet ID, requiring OAuth2UserToken with "like.write," "tweet.read," and "users.read" permissions. |
| `get_user_list_memberships` | Retrieves a list of memberships for a specified user using their ID, allowing for optional filtering by maximum results and pagination, and returns the membership details. |
| `users_id_mentions` | Retrieves the timeline of tweets that mention the user associated with the provided ID, allowing for customization with parameters such as since and until IDs, pagination tokens, and various field expansions. |
| `users_id_muting` | Retrieves a list of users muted by the specified user using the Twitter API with optional filtering by max results, pagination token, user fields, user expansions, tweet fields, and returns the response upon authorization with the required "mute.read," "tweet.read," and "users.read" scopes. |
| `users_id_mute` | Mutes a user identified by their ID using the API, requiring a POST request with appropriate OAuth2 credentials. |
| `list_user_owned_lists` | Retrieves a list of Twitter Lists owned by the specified user, supporting optional pagination and field expansions. |
| `list_user_pinned_lists` | Retrieves the pinned Lists of a specified user by their user ID, returning detailed information about each pinned List. |
| `list_user_pin` | Creates a pinned list for a user identified by {id} using JSON data and OAuth2UserToken or UserToken authentication. |
| `list_user_unpin` | Deletes a specified pinned list from a user's account by user ID and list ID. |
| `users_id_retweets` | Retweets a post using the X API on behalf of a specified user, requiring authentication with OAuth2UserToken and appropriate permissions. |
| `users_id_unretweets` | Undoes a retweet of a specified tweet by a user using the Twitter API v2, requiring OAuth authentication and user permissions. |
| `users_id_timeline` | Retrieves a user's reverse chronological timeline, returning tweets in the order they were posted, with optional filtering by time range, tweet IDs, and additional metadata fields. |
| `users_id_tweets` | Retrieves a list of tweets for a user with the specified ID, allowing optional filtering by tweet ID range, result count, pagination token, excluded fields, and time range, using the "GET" method. |
| `users_id_unfollow` | Unfollows a target user by deleting the follow relationship between the source user and the target user using the "DELETE" method. |
| `users_id_unmute` | Unmutes a target user using the "DELETE" method on the "/2/users/{source_user_id}/muting/{target_user_id}" path, reversing the mute action applied by the source user to the target user. |
