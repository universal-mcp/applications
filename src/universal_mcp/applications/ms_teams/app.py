from typing import Any, Literal
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class MsTeamsApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="ms_teams", integration=integration, **kwargs)
        self.base_url = "https://graph.microsoft.com/v1.0"

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

    # async def list_channels_for_team(
    #     self,
    #     team_id: str,
    #     top: int | None = None,
    #     skip: int | None = None,
    #     search: str | None = None,
    #     filter: str | None = None,
    #     count: bool | None = None,
    #     orderby: list[str] | None = None,
    #     select: list[str] | None = None,
    #     expand: list[str] | None = None,
    # ) -> dict[str, Any]:
    #     """
    #     Retrieves the collection of channels for a specified Microsoft Teams team by its ID. It supports advanced OData query parameters for filtering, sorting, and pagination, distinguishing it from functions that fetch single channels like `get_channel_details`.

    #     Args:
    #         team_id (string): team-id
    #         top (integer): Show only the first n items Example: '50'.
    #         skip (integer): Skip the first n items
    #         search (string): Search items by search phrases
    #         filter (string): Filter items by property values
    #         count (boolean): Include count of items
    #         orderby (array): Order items by property values
    #         select (array): Select properties to be returned
    #         expand (array): Expand related entities

    #     Returns:
    #         dict[str, Any]: Retrieved collection

    #     Raises:
    #         HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

    #     Tags:
    #         teams.channel, important
    #     """
    #     if team_id is None:
    #         raise ValueError("Missing required parameter 'team-id'.")
    #     url = f"{self.base_url}/teams/{team_id}/channels"
    #     # Helper to format list params
    #     def fmt(val):
    #         return ",".join(val) if isinstance(val, list) else val

    #     query_params = {
    #         k: fmt(v)
    #         for k, v in [
    #             ("$top", top),
    #             ("$skip", skip),
    #             ("$search", search),
    #             ("$filter", filter),
    #             ("$count", count),
    #             ("$orderby", orderby),
    #             ("$select", select),
    #             ("$expand", expand),
    #         ]
    #         if v is not None
    #     }
    #     response = await self._aget(url, params=query_params)
    #     return self._handle_response(response)

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

    async def create_chat(
        self,
        id: str | None = None,
        chatType: str | None = None,
        createdDateTime: str | None = None,
        isHiddenForAllMembers: bool | None = None,
        lastUpdatedDateTime: str | None = None,
        onlineMeetingInfo: dict[str, dict[str, Any]] | None = None,
        tenantId: str | None = None,
        topic: str | None = None,
        viewpoint: dict[str, dict[str, Any]] | None = None,
        webUrl: str | None = None,
        installedApps: list[Any] | None = None,
        lastMessagePreview: Any | None = None,
        members: list[Any] | None = None,
        messages: list[Any] | None = None,
        permissionGrants: list[Any] | None = None,
        pinnedMessages: list[Any] | None = None,
        tabs: list[Any] | None = None,
    ) -> Any:
        """
        Creates a new one-on-one or group chat in Microsoft Teams. This function provisions a new conversation using optional parameters like chatType and members, distinguishing it from functions that create teams (`create_team`) or send messages to existing chats (`send_chat_message`).

        Args:
            id (string): The unique identifier for an entity. Read-only.
            chatType (string): chatType
            createdDateTime (string): Date and time at which the chat was created. Read-only.
            isHiddenForAllMembers (boolean): Indicates whether the chat is hidden for all its members. Read-only.
            lastUpdatedDateTime (string): Date and time at which the chat was renamed or the list of members was last changed. Read-only.
            onlineMeetingInfo (object): onlineMeetingInfo
            tenantId (string): The identifier of the tenant in which the chat was created. Read-only.
            topic (string): (Optional) Subject or topic for the chat. Only available for group chats.
            viewpoint (object): viewpoint
            webUrl (string): The URL for the chat in Microsoft Teams. The URL should be treated as an opaque blob, and not parsed. Read-only.
            installedApps (array): A collection of all the apps in the chat. Nullable.
            lastMessagePreview (string): lastMessagePreview
            members (array): A collection of all the members in the chat. Nullable.
            messages (array): A collection of all the messages in the chat. Nullable.
            permissionGrants (array): A collection of permissions granted to apps for the chat.
            pinnedMessages (array): A collection of all the pinned messages in the chat. Nullable.
            tabs (array): A collection of all the tabs in the chat. Nullable.

        Returns:
            Any: Created entity

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chat
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "chatType": chatType,
            "createdDateTime": createdDateTime,
            "isHiddenForAllMembers": isHiddenForAllMembers,
            "lastUpdatedDateTime": lastUpdatedDateTime,
            "onlineMeetingInfo": onlineMeetingInfo,
            "tenantId": tenantId,
            "topic": topic,
            "viewpoint": viewpoint,
            "webUrl": webUrl,
            "installedApps": installedApps,
            "lastMessagePreview": lastMessagePreview,
            "members": members,
            "messages": messages,
            "permissionGrants": permissionGrants,
            "pinnedMessages": pinnedMessages,
            "tabs": tabs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/chats"
        query_params = {}
        response = await self._apost(url, data=request_body_data, params=query_params, content_type="application/json")
        return self._handle_response(response)

    async def get_chat_details(self, chat_id: str, select: list[str] | None = None, expand: list[str] | None = None) -> Any:
        """
        Retrieves the properties and relationships of a specific chat conversation by its unique ID. Unlike `get_user_chats` which lists all chats, this targets one chat. Optional parameters can select specific fields or expand related entities like members or apps to customize the returned data.

        Args:
            chat_id (string): chat-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved entity

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chat
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        url = f"{self.base_url}/chats/{chat_id}"
        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {k: fmt(v) for k, v in [("$select", select), ("$expand", expand)] if v is not None}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def update_chat_details(
        self,
        chat_id: str,
        id: str | None = None,
        chatType: str | None = None,
        createdDateTime: str | None = None,
        isHiddenForAllMembers: bool | None = None,
        lastUpdatedDateTime: str | None = None,
        onlineMeetingInfo: dict[str, dict[str, Any]] | None = None,
        tenantId: str | None = None,
        topic: str | None = None,
        viewpoint: dict[str, dict[str, Any]] | None = None,
        webUrl: str | None = None,
        installedApps: list[Any] | None = None,
        lastMessagePreview: Any | None = None,
        members: list[Any] | None = None,
        messages: list[Any] | None = None,
        permissionGrants: list[Any] | None = None,
        pinnedMessages: list[Any] | None = None,
        tabs: list[Any] | None = None,
    ) -> Any:
        """
        Updates properties of a specific chat, such as its topic, using its unique ID. This function performs a partial update (PATCH), distinguishing it from `get_chat_details` which only retrieves data, and `create_chat` which creates an entirely new chat conversation.

        Args:
            chat_id (string): chat-id
            id (string): The unique identifier for an entity. Read-only.
            chatType (string): chatType
            createdDateTime (string): Date and time at which the chat was created. Read-only.
            isHiddenForAllMembers (boolean): Indicates whether the chat is hidden for all its members. Read-only.
            lastUpdatedDateTime (string): Date and time at which the chat was renamed or the list of members was last changed. Read-only.
            onlineMeetingInfo (object): onlineMeetingInfo
            tenantId (string): The identifier of the tenant in which the chat was created. Read-only.
            topic (string): (Optional) Subject or topic for the chat. Only available for group chats.
            viewpoint (object): viewpoint
            webUrl (string): The URL for the chat in Microsoft Teams. The URL should be treated as an opaque blob, and not parsed. Read-only.
            installedApps (array): A collection of all the apps in the chat. Nullable.
            lastMessagePreview (string): lastMessagePreview
            members (array): A collection of all the members in the chat. Nullable.
            messages (array): A collection of all the messages in the chat. Nullable.
            permissionGrants (array): A collection of permissions granted to apps for the chat.
            pinnedMessages (array): A collection of all the pinned messages in the chat. Nullable.
            tabs (array): A collection of all the tabs in the chat. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chat
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "chatType": chatType,
            "createdDateTime": createdDateTime,
            "isHiddenForAllMembers": isHiddenForAllMembers,
            "lastUpdatedDateTime": lastUpdatedDateTime,
            "onlineMeetingInfo": onlineMeetingInfo,
            "tenantId": tenantId,
            "topic": topic,
            "viewpoint": viewpoint,
            "webUrl": webUrl,
            "installedApps": installedApps,
            "lastMessagePreview": lastMessagePreview,
            "members": members,
            "messages": messages,
            "permissionGrants": permissionGrants,
            "pinnedMessages": pinnedMessages,
            "tabs": tabs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/chats/{chat_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    async def list_chat_members(
        self,
        chat_id: str,
        top: int | None = None,
        skip: int | None = None,
        search: str | None = None,
        filter: str | None = None,
        count: bool | None = None,
        orderby: list[str] | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a collection of all members in a specific chat using its ID. It supports OData query parameters for pagination, filtering, and sorting. Unlike `get_chat_member`, which fetches a single individual, this function returns the entire collection of members for the specified chat.

        Args:
            chat_id (string): chat-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.conversationMember
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        url = f"{self.base_url}/chats/{chat_id}/members"
        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {
            k: fmt(v)
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_chat_member(
        self, chat_id: str, conversationMember_id: str, select: list[str] | None = None, expand: list[str] | None = None
    ) -> Any:
        """
        Retrieves detailed information for a specific member within a chat using their unique ID. This function targets a single individual, distinguishing it from `list_chat_members` which returns all members. The response can be customized by selecting specific properties or expanding related entities.

        Args:
            chat_id (string): chat-id
            conversationMember_id (string): conversationMember-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.conversationMember
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        if conversationMember_id is None:
            raise ValueError("Missing required parameter 'conversationMember-id'.")
        url = f"{self.base_url}/chats/{chat_id}/members/{conversationMember_id}"
        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {k: fmt(v) for k, v in [("$select", select), ("$expand", expand)] if v is not None}
        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def list_chat_messages(
        self,
        chat_id: str,
        top: int | None = None,
        skip: int | None = None,
        search: str | None = None,
        filter: str | None = None,
        count: bool | None = None,
        orderby: list[str] | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves messages from a specific chat using its ID. Unlike `get_chat_message`, which fetches a single message, this function returns a collection and supports advanced querying for filtering, sorting, and pagination to refine the results.

        Args:
            chat_id (string): chat-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chatMessage
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
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
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
