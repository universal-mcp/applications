from typing import Any, Literal
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class MsTeamsApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="ms_teams", integration=integration, **kwargs)
        self.base_url = "https://graph.microsoft.com/v1.0"

# Chat Management

    async def get_user_chats(
        self,
        top: int | None = None,
        expand: list[Literal["members", "lastMessagePreview"]] | None = None,
        filter: str | None = None,
        orderby: Literal["lastMessagePreview/createdDateTime desc"] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a collection of chats the authenticated user is participating in. Supports optional OData query parameters for advanced filtering, sorting, pagination, and field selection, enabling customized data retrieval from the Microsoft Graph API.

        Args:
            top (integer): Controls the number of items per response. Maximum allowed $top value is 50.
            expand (array): Currently supports 'members' and 'lastMessagePreview' properties.
            filter (string): Filters results.
            orderby (string): Currently supports 'lastMessagePreview/createdDateTime desc'. Ascending order is currently not supported.

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chat, important
        """
        url = f"{self.base_url}/chats"
        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {
            k: fmt(v)
            for k, v in [
                ("$top", top),
                ("$expand", expand),
                ("$filter", filter),
                ("$orderby", orderby),
            ]
            if v is not None
        }
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def create_chat(
        self,
        chatType: Literal["oneOnOne", "group"] | str,
        members: list[dict[str, Any]],
        topic: str | None = None,
    ) -> dict[str, Any]:
        """
        Creates a new one-on-one or group chat in Microsoft Teams. This function provisions a new conversation using required parameters like chatType and members.

        Args:
            chatType (string): The type of chat. Possible values are: oneOnOne, group.
            members (array): A collection of member dictionaries. For oneOnOne chats, typically 2 users. For group chats, multiple users. Each member should specify roles and user binding (e.g. `{'@odata.type': '#microsoft.graph.aadUserConversationMember', 'roles': ['owner'], 'user@odata.bind': 'https://graph.microsoft.com/v1.0/users(\\'<user-id>\\')'}`).
            topic (string): (Optional) Subject or topic for the chat. Only available for group chats.

        Returns:
            dict[str, Any]: The newly created chat entity.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chat, create
        """
        request_body_data = {
            "chatType": chatType,
            "members": members,
            "topic": topic,
        }
        # Filter explicitly None values, though for required ones they should be validated by type hints/caller
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        
        url = f"{self.base_url}/chats"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        return self._handle_response(response)

    async def get_chat_details(
        self,
        chat_id: str,
    ) -> Any:
        """
        Retrieves the properties and relationships of a specific chat conversation by its unique ID.

        Args:
            chat_id (string): The unique identifier of the chat.

        Returns:
            Any: Retrieved entity

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chat, read
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        url = f"{self.base_url}/chats/{chat_id}"
        response = await self._aget(url)
        return self._handle_response(response)

    async def update_chat_details(
        self,
        chat_id: str,
        topic: str | None = None,
    ) -> Any:
        """
        Updates properties of a specific chat, such as its topic, using its unique ID. This function performs a partial update (PATCH). Currently, only the 'topic' property can be updated for group chats.

        Args:
            chat_id (string): The unique identifier of the chat.
            topic (string): (Optional) The new subject or topic for the chat. Only applicable for group chats.

        Returns:
            Any: Variable response depending on the API, typically the updated entity or status.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chat, update
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        
        request_body_data = {"topic": topic}
        # Filter explicitly None values
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        
        if not request_body_data:
             raise ValueError("No updateable parameters provided.")

        url = f"{self.base_url}/chats/{chat_id}"
        response = await self._apatch(url, data=request_body_data, content_type="application/json")
        return self._handle_response(response)

    async def list_chat_members(
        self,
        chat_id: str,
    ) -> list[dict[str, Any]]:
        """
        Retrieves a collection of all members in a specific chat using its ID.
        Note: The Microsoft Graph API for getting chat members does NOT support OData query parameters like $top, $filter, etc.

        Args:
            chat_id (string): The unique identifier of the chat.

        Returns:
            list[dict[str, Any]]: A list of conversationMember objects.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.conversationMember, list, read
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        url = f"{self.base_url}/chats/{chat_id}/members"
        
        # This endpoint generally does not support OData params, so we send none.
        response = await self._aget(url)
        data = self._handle_response(response)
        return data.get("value", [])

    async def get_chat_member(
        self, chat_id: str, conversationMember_id: str
    ) -> Any:
        """
        Retrieves detailed information for a specific member within a chat using their unique ID.
        Note: The Microsoft Graph API for this endpoint does NOT support OData query parameters.

        Args:
            chat_id (string): The unique identifier of the chat.
            conversationMember_id (string): The unique identifier of the member.

        Returns:
            Any: Retrieved conversationMember entity.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.conversationMember, read
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        if conversationMember_id is None:
            raise ValueError("Missing required parameter 'conversationMember-id'.")
        url = f"{self.base_url}/chats/{chat_id}/members/{conversationMember_id}"
        
        # This endpoint generally does not support OData params
        response = await self._aget(url)
        return self._handle_response(response)


    async def get_joined_teams(self) -> list[dict[str, Any]]:
        """
        Fetches all Microsoft Teams the authenticated user belongs to by querying the `/me/joinedTeams` Graph API endpoint. It returns a list of dictionaries, where each dictionary represents a single team's details, unlike functions that list channels or chats for a specific team.

        Returns:
            A list of dictionaries, where each dictionary represents a team.

        Raises:
            httpx.HTTPStatusError: If the API request fails due to authentication or other issues.

        Tags:
            read, list, teams, microsoft-teams, api, important
        """
        url = f"{self.base_url}/me/joinedTeams"
        response = await self._aget(url)
        data = self._handle_response(response)
        return data.get("value", [])

    async def send_chat_message(self, chat_id: str, content: str) -> dict[str, Any]:
        """
        Posts a new message to a specific Microsoft Teams chat using its unique ID. This function targets direct or group chats, distinguishing it from `send_channel_message`, which posts to public team channels, and `reply_to_chat_message`, which responds to existing messages.

        Args:
            chat_id: The unique identifier of the chat.
            content: The message content to send (can be plain text or HTML).

        Returns:
            A dictionary containing the API response for the sent message, including its ID.

        Raises:
            httpx.HTTPStatusError: If the API request fails due to invalid ID, permissions, etc.

        Tags:
            create, send, message, chat, microsoft-teams, api, important
        """
        url = f"{self.base_url}/chats/{chat_id}/messages"
        payload = {"body": {"content": content}}
        response = await self._apost(url, data=payload)
        return self._handle_response(response)

    async def send_channel_message(self, team_id: str, channel_id: str, content: str) -> dict[str, Any]:
        """
        Posts a new message to a specified team channel, initiating a new conversation thread. Unlike `reply_to_channel_message`, which replies to a message, this function starts a new topic. It's distinct from `send_chat_message`, which is for private or group chats, not team channels.

        Args:
            team_id: The unique identifier of the team.
            channel_id: The unique identifier of the channel within the team.
            content: The message content to send (can be plain text or HTML).

        Returns:
            A dictionary containing the API response for the sent message, including its ID.

        Raises:
            httpx.HTTPStatusError: If the API request fails due to invalid IDs, permissions, etc.

        Tags:
            create, send, message, channel, microsoft-teams, api, important
        """
        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}/messages"
        payload = {"body": {"content": content}}
        response = await self._apost(url, data=payload)
        return self._handle_response(response)

    async def reply_to_channel_message(self, team_id: str, channel_id: str, message_id: str, content: str) -> dict[str, Any]:
        """
        Posts a reply to a specific message within a Microsoft Teams channel. It uses the team, channel, and original message IDs to target an existing conversation thread, distinguishing it from `send_channel_message` which starts a new one.

        Args:
            team_id: The unique identifier of the team.
            channel_id: The unique identifier of the channel.
            message_id: The unique identifier of the message to reply to.
            content: The reply message content (can be plain text or HTML).

        Returns:
            A dictionary containing the API response for the sent reply, including its ID.

        Raises:
            httpx.HTTPStatusError: If the API request fails due to invalid IDs, permissions, etc.

        Tags:
            create, send, reply, message, channel, microsoft-teams, api, important
        """
        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}/messages/{message_id}/replies"
        payload = {"body": {"content": content}}
        response = await self._apost(url, data=payload)
        return self._handle_response(response)

    async def list_chat_messages(
        self,
        chat_id: str,
        top: int | None = None,
        orderby: list[Literal["lastModifiedDateTime desc", "createdDateTime desc"]] | None = None,
        filter: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves messages from a specific chat using its ID.
        
        Supported OData parameters with strict limitations:
        - $top: Controls the number of items per response. Maximum allowed value is 50.
        - $orderby: Currently supports 'lastModifiedDateTime desc' (default) and 'createdDateTime desc'. Ascending order is NOT supported.
        - $filter: Sets the date range filter for 'lastModifiedDateTime' (supports gt/lt) and 'createdDateTime' (supports lt). 
          Note: You can only filter results if 'orderby' is configured for the same property!

        Args:
            chat_id (string): The unique identifier of the chat.
            top (integer): Show only the first n items. Max 50.
            orderby (array): Order items by property values. Restrict to supported descending sorts.
            filter (string): Filter items by property values. Must match orderby property.

        Returns:
            dict[str, Any]: Retrieved collection of messages.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chatMessage, list, read
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        url = f"{self.base_url}/chats/{chat_id}/messages"
        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {
            k: fmt(v)
            for k, v in [
                ("$top", top),
                ("$orderby", orderby),
                ("$filter", filter),
            ]
            if v is not None
        }
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_chat_message(
        self, chat_id: str, chatMessage_id: str, select: list[str] | None = None, expand: list[str] | None = None
    ) -> Any:
        """
        Retrieves the full details of a single message from a specific chat using both chat and message IDs. This function targets an individual message, differentiating it from `list_chat_messages`, which retrieves a collection. Optional parameters can customize the response by selecting specific properties or expanding entities.

        Args:
            chat_id (string): chat-id
            chatMessage_id (string): chatMessage-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chatMessage
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        if chatMessage_id is None:
            raise ValueError("Missing required parameter 'chatMessage-id'.")
        url = f"{self.base_url}/chats/{chat_id}/messages/{chatMessage_id}"
        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {k: fmt(v) for k, v in [("$select", select), ("$expand", expand)] if v is not None}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_channel_details(
        self, team_id: str, channel_id: str, select: list[str] | None = None, expand: list[str] | None = None
    ) -> Any:
        """
        Retrieves detailed information for a specific channel within a Microsoft Teams team, identified by both team and channel IDs. Optional parameters can select specific properties or expand related entities in the response, distinguishing it from list_channels_for_team, which retrieves a collection of channels.

        Args:
            team_id (string): team-id
            channel_id (string): channel-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            teams.channel
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'.")
        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}"
        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {k: fmt(v) for k, v in [("$select", select), ("$expand", expand)] if v is not None}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def create_channel_tab(
        self,
        team_id: str,
        channel_id: str,
        id: str | None = None,
        configuration: dict[str, dict[str, Any]] | None = None,
        displayName: str | None = None,
        webUrl: str | None = None,
        teamsApp: Any | None = None,
    ) -> Any:
        """
        Creates a new tab in a specified Microsoft Teams channel using team and channel IDs. This function configures the tab's initial properties, such as display name and application, distinguishing it from functions that list (`list_channel_tabs`) or modify (`update_channel_tab`) existing tabs.

        Args:
            team_id (string): team-id
            channel_id (string): channel-id
            id (string): The unique identifier for an entity. Read-only.
            configuration (object): configuration
            displayName (string): Name of the tab.
            webUrl (string): Deep link URL of the tab instance. Read only.
            teamsApp (string): teamsApp

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            teams.channel
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'.")
        request_body_data = None
        request_body_data = {"id": id, "configuration": configuration, "displayName": displayName, "webUrl": webUrl, "teamsApp": teamsApp}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}/tabs"
        query_params = {}
        response = await self._apost(url, data=request_body_data, params=query_params, content_type="application/json")
        return self._handle_response(response)

    async def get_primary_team_channel(self, team_id: str, select: list[str] | None = None, expand: list[str] | None = None) -> Any:
        """
        Retrieves the primary channel (usually 'General') for a specified team using its ID. Unlike `get_channel_details`, this function directly accesses the team's default channel without requiring a specific channel ID. Optional parameters can select or expand properties in the returned data.

        Args:
            team_id (string): team-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            teams.channel
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        url = f"{self.base_url}/teams/{team_id}/primaryChannel"
        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {k: fmt(v) for k, v in [("$select", select), ("$expand", expand)] if v is not None}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.get_user_chats,
            self.get_joined_teams,
            self.list_channels_for_team,
            self.send_chat_message,
            self.send_channel_message,
            self.reply_to_channel_message,
            self.create_chat,
            self.get_chat_details,
            self.update_chat_details,
            self.list_chat_members,
            self.get_chat_member,
            self.list_chat_messages,
            self.get_chat_message,
            self.get_channel_details,
            self.get_primary_team_channel,
        ]
