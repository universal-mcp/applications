from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class SlackApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="slack", integration=integration, **kwargs)
        self.base_url = "https://slack.com/api"

    def chat_delete(
        self,
        as_user: bool | None = None,
        channel: str | None = None,
        ts: float | None = None,
    ) -> dict[str, Any]:
        """
        Deletes a specific message from a Slack channel. It identifies the message using its channel ID and timestamp (`ts`). This function is distinct from `chat_update` which modifies a message, and `chat_post_message` which sends a new one.

        Args:
            as_user (boolean): Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](https://slack.dev) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope.
            channel (string): Channel containing the message to be deleted.
            ts (number): Timestamp of the message to be deleted.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chat
        """
        request_body_data = None
        request_body_data = {
            "as_user": as_user,
            "channel": channel,
            "ts": ts,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/chat.delete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/x-www-form-urlencoded",
        )
        return self._handle_response(response)

    def chat_post_message(
        self,
        as_user: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        channel: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        mrkdwn: bool | None = None,
        parse: str | None = None,
        reply_broadcast: bool | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        username: str | None = None,
    ) -> dict[str, Any]:
        """
        Posts a new message to a specified Slack channel. It supports rich content formats like text, attachments, and blocks, along with options for threading and authorship. This function creates new messages, unlike `chat_update` which modifies existing ones or `chat_delete` which removes them.

        Args:
            as_user (boolean): Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](https://slack.dev) below.
            attachments (string): A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks (string): A JSON-based array of structured blocks, presented as a URL-encoded string.
            channel (string): Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See [below](https://slack.dev) for more details.
            icon_emoji (string): Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](https://slack.dev) below.
            icon_url (string): URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](https://slack.dev) below.
            link_names (boolean): Find and link channel names and usernames.
            mrkdwn (boolean): Disable Slack markup parsing by setting to `false`. Enabled by default.
            parse (string): Change how messages are treated. Defaults to `none`. See [below](https://slack.dev).
            reply_broadcast (boolean): Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.
            text (string): How this field works and whether it is required depends on other fields you use in your API call. [See below](https://slack.dev) for more detail.
            thread_ts (string): Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.
            unfurl_links (boolean): Pass true to enable unfurling of primarily text-based content.
            unfurl_media (boolean): Pass false to disable unfurling of media content.
            username (string): Set your bot's user name. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](https://slack.dev) below.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chat
        """
        request_body_data = None
        request_body_data = {
            "as_user": as_user,
            "attachments": attachments,
            "blocks": blocks,
            "channel": channel,
            "icon_emoji": icon_emoji,
            "icon_url": icon_url,
            "link_names": link_names,
            "mrkdwn": mrkdwn,
            "parse": parse,
            "reply_broadcast": reply_broadcast,
            "text": text,
            "thread_ts": thread_ts,
            "unfurl_links": unfurl_links,
            "unfurl_media": unfurl_media,
            "username": username,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/chat.postMessage"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/x-www-form-urlencoded",
        )
        return self._handle_response(response)

    def chat_update(
        self,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        channel: str | None = None,
        link_names: str | None = None,
        parse: str | None = None,
        text: str | None = None,
        ts: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates a specific, existing message in a Slack channel, identified by its timestamp. It modifies content such as text, blocks, or attachments by calling the `chat.update` API endpoint, distinguishing it from functions that create (`chat_post_message`) or delete (`chat_delete`) messages.

        Args:
            as_user (string): Pass true to update the message as the authed user. [Bot users](https://slack.dev) in this context are considered authed users.
            attachments (string): A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting `text`. If you don't include this field, the message's previous `attachments` will be retained. To remove previous `attachments`, include an empty array for this field.
            blocks (string): A JSON-based array of [structured blocks](https://slack.dev), presented as a URL-encoded string. If you don't include this field, the message's previous `blocks` will be retained. To remove previous `blocks`, include an empty array for this field.
            channel (string): Channel containing the message to be updated.
            link_names (string): Find and link channel names and usernames. Defaults to `none`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `none`.
            parse (string): Change how messages are treated. Defaults to `client`, unlike `chat.postMessage`. Accepts either `none` or `full`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `client`.
            text (string): New text for the message, using the [default formatting rules](https://slack.dev). It's not required when presenting `blocks` or `attachments`.
            ts (string): Timestamp of the message to be updated.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chat, important
        """
        request_body_data = None
        request_body_data = {
            "as_user": as_user,
            "attachments": attachments,
            "blocks": blocks,
            "channel": channel,
            "link_names": link_names,
            "parse": parse,
            "text": text,
            "ts": ts,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/chat.update"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/x-www-form-urlencoded",
        )
        return self._handle_response(response)

    def conversations_history(
        self,
        token: str | None = None,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
    ) -> dict[str, Any]:
        """
        Fetches the message history for a specific Slack conversation or channel. Supports filtering messages by timestamp and pagination using a cursor. This method retrieves messages *within* a conversation, unlike `conversations_list` which retrieves a list of available conversations.

        Args:
            token (string): Authentication token used to access conversation history.
            channel (string): The ID of the channel to retrieve the conversation history from.
            latest (number): Specifies the number of the latest conversation messages to retrieve from the history.
            oldest (number): Timestamp (in seconds) of the oldest message to include in the conversation history results.
            inclusive (boolean): Determines whether to include the messages at the end of the history range in the response.
            limit (integer): Specifies the maximum number of conversation history entries to retrieve in a single API call.
            cursor (string): A string token used for cursor-based pagination to fetch the next set of conversation history results starting from a specific point.

        Returns:
            dict[str, Any]: Typical success response containing a channel's messages

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            conversations
        """
        url = f"{self.base_url}/conversations.history"
        query_params = {
            k: v
            for k, v in [
                ("token", token),
                ("channel", channel),
                ("latest", latest),
                ("oldest", oldest),
                ("inclusive", inclusive),
                ("limit", limit),
                ("cursor", cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def conversations_list(
        self,
        token: str | None = None,
        exclude_archived: bool | None = None,
        types: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of channel-like conversations in a workspace. Allows filtering by type and excluding archived channels. This function lists available conversations, unlike `conversations_history` which retrieves the message history from within a specific conversation.

        Args:
            token (string): The token parameter in the query string is a string used for authentication to authorize and identify the client making the GET request to the /conversations.list endpoint.
            exclude_archived (boolean): Exclude archived conversations from the list of results.
            types (string): Specifies the types of conversations to include in the list, as a string query parameter.
            limit (integer): Specifies the maximum number of conversations to return in the response, with a default value of 1.
            cursor (string): A cursor string used for pagination to specify the position from which to continue retrieving the next set of conversation results.

        Returns:
            dict[str, Any]: Typical success response with only public channels

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            conversations
        """
        url = f"{self.base_url}/conversations.list"
        query_params = {
            k: v
            for k, v in [
                ("token", token),
                ("exclude_archived", exclude_archived),
                ("types", types),
                ("limit", limit),
                ("cursor", cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def reactions_add(self, channel: str, name: str, timestamp: str) -> dict[str, Any]:
        """
        Adds a specific emoji reaction to a message in a Slack channel, identifying the message by its channel ID and timestamp. This method creates a new reaction, unlike `reactions_get` or `reactions_list` which retrieve existing reaction data for items or users.

        Args:
            channel (string): Channel where the message to add reaction to was posted.
            name (string): Reaction (emoji) name.
            timestamp (string): Timestamp of the message to add reaction to.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reactions
        """
        request_body_data = None
        request_body_data = {
            "channel": channel,
            "name": name,
            "timestamp": timestamp,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/reactions.add"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/x-www-form-urlencoded",
        )
        return self._handle_response(response)

    def get_reactions_for_item(
        self,
        token: str,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        full: bool | None = None,
        timestamp: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves all reactions for a single item, such as a message, file, or file comment. This function targets reactions *on* a specific item, unlike `reactions_list` which gets reactions created *by* a user.

        Args:
            token (string): The "token" parameter is a required string that must be provided in the query string for authentication purposes when using the GET operation at "/reactions.get" to authorize access to reaction data.
            channel (string): The channel identifier to filter reactions by, specified as a string.
            file (string): The file parameter specifies the identifier of the file for which to retrieve reactions.
            file_comment (string): A query parameter to filter reactions by a specific file comment.
            full (boolean): Whether to return full reaction details or only basic reaction information.
            timestamp (string): The timestamp parameter filters results based on a specific date and time value, expected in an ISO 8601 format string.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reactions
        """
        url = f"{self.base_url}/reactions.get"
        query_params = {
            k: v
            for k, v in [
                ("token", token),
                ("channel", channel),
                ("file", file),
                ("file_comment", file_comment),
                ("full", full),
                ("timestamp", timestamp),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_user_reactions(
        self,
        token: str,
        user: str | None = None,
        full: bool | None = None,
        count: int | None = None,
        page: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of items (e.g., messages, files) that a specific user has reacted to. Unlike `reactions_get`, which fetches all reactions for a single item, this function lists all items a given user has reacted to across Slack.

        Args:
            token (string): Required authentication token passed as a query parameter to authenticate the request for listing reactions.
            user (string): Filter reactions by specifying the user, which can be a username or identifier.
            full (boolean): Indicates whether to retrieve a full list of reactions, with `true` returning all reactions and `false` returning a partial list.
            count (integer): The "count" query parameter specifies the maximum number of reaction items to return in the response.
            page (integer): The "page" parameter is an integer query parameter used to specify the page number for pagination in the list of reactions.
            cursor (string): A string used to specify the position in the list of reactions for pagination, allowing retrieval of additional items after or before the specified cursor.
            limit (integer): The `limit` parameter specifies the maximum number of reactions to return in the response.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reactions
        """
        url = f"{self.base_url}/reactions.list"
        query_params = {
            k: v
            for k, v in [
                ("token", token),
                ("user", user),
                ("full", full),
                ("count", count),
                ("page", page),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def search_messages(
        self,
        token: str,
        query: str,
        count: int | None = None,
        highlight: bool | None = None,
        page: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
    ) -> dict[str, Any]:
        """
        Searches a Slack workspace for messages matching a specific query. It supports advanced control over results through pagination, sorting by relevance or timestamp, and an option to highlight search terms within the returned message content.

        Args:
            token (string): A required string parameter named "token" passed as a query parameter to authenticate the request for retrieving search messages.
            query (string): The search query string to specify the text or keywords to search for in messages.
            count (integer): Optional integer parameter "count" specifying the number of search messages to return, defaulting to 1 if not provided.
            highlight (boolean): Indicates whether to highlight specific parts of the search results in the messages.
            page (integer): The page query parameter specifies the page number of search results to retrieve in the GET /search.messages operation.
            sort (string): Sorts the search results by a specified field, allowing clients to customize the order of returned messages.
            sort_dir (string): The "sort_dir" query parameter specifies the direction of sorting for the search results, typically accepting values like "asc" for ascending or "desc" for descending order.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            search, important
        """
        url = f"{self.base_url}/search.messages"
        query_params = {
            k: v
            for k, v in [
                ("token", token),
                ("count", count),
                ("highlight", highlight),
                ("page", page),
                ("query", query),
                ("sort", sort),
                ("sort_dir", sort_dir),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def team_info(self, token: str, team: str | None = None) -> dict[str, Any]:
        """
        Fetches details for a Slack team, such as name and domain, by calling the `team.info` API endpoint. This function requires an authentication token and can optionally target a specific team by its ID, distinguishing it from user or channel-specific functions.

        Args:
            token (string): Mandatory authentication token passed as a query parameter to authenticate the request for retrieving team information.
            team (string): The "team" parameter is a query string parameter of type string, used to specify the team for which information is requested in the GET operation at the "/team.info" path.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            team
        """
        url = f"{self.base_url}/team.info"
        query_params = {
            k: v for k, v in [("token", token), ("team", team)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_user_info(
        self,
        token: str,
        include_locale: bool | None = None,
        user: str | None = None,
    ) -> dict[str, Any]:
        """
        Fetches detailed profile information for a single Slack user, identified by their user ID. Unlike `users_list`, which retrieves all workspace members, this function targets an individual and can optionally include their locale information. It directly calls the `users.info` Slack API endpoint.

        Args:
            token (string): The token query parameter is a required string used to authenticate and authorize the API request to access user information in the GET /users.info operation.
            include_locale (boolean): Indicates whether to include locale information in the response, with a value of true or false.
            user (string): A string parameter used to identify or specify a user in the request.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users, important
        """
        url = f"{self.base_url}/users.info"
        query_params = {
            k: v
            for k, v in [
                ("token", token),
                ("include_locale", include_locale),
                ("user", user),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def users_list(
        self,
        token: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        include_locale: bool | None = None,
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of all users in a Slack workspace, including deactivated members. Unlike `users_info` which retrieves a single user's details, this function returns a collection and supports limiting results or including locale data through optional parameters.

        Args:
            token (string): Required authentication token for accessing the list of users.
            limit (integer): Specifies the maximum number of users to return in the response, defaults to 1.
            cursor (string): A unique string identifier used for cursor-based pagination, indicating the starting point for retrieving the next set of users in the list.
            include_locale (boolean): A boolean query parameter to optionally include locale information in the response.

        Returns:
            dict[str, Any]: Typical success response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users
        """
        url = f"{self.base_url}/users.list"
        query_params = {
            k: v
            for k, v in [
                ("token", token),
                ("limit", limit),
                ("cursor", cursor),
                ("include_locale", include_locale),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.chat_delete,
            self.chat_post_message,
            self.chat_update,
            self.conversations_history,
            self.conversations_list,
            self.reactions_add,
            self.get_reactions_for_item,
            self.get_user_reactions,
            self.search_messages,
            self.team_info,
            self.get_user_info,
            self.users_list,
        ]
