from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class MsTeamsApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="ms_teams", integration=integration, **kwargs)
        self.base_url = "https://graph.microsoft.com/v1.0"

    def get_user_chats(
        self,
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
        Retrieves a collection of chats the authenticated user is participating in. Supports optional OData query parameters for advanced filtering, sorting, pagination, and field selection, enabling customized data retrieval from the Microsoft Graph API.

        Args:
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
            chats.chat, important
        """
        url = f"{self.base_url}/chats"
        query_params = {
            k: v
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
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_joined_teams(self) -> list[dict[str, Any]]:
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
        response = self._get(url)
        data = self._handle_response(response)
        # The API returns the list of teams under the "value" key.
        return data.get("value", [])

    def list_channels_for_team(
        self,
        team_id: str,
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
        Retrieves the collection of channels for a specified Microsoft Teams team by its ID. It supports advanced OData query parameters for filtering, sorting, and pagination, distinguishing it from functions that fetch single channels like `get_channel_details`.

        Args:
            team_id (string): team-id
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
            teams.channel, important
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        url = f"{self.base_url}/teams/{team_id}/channels"
        query_params = {
            k: v
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
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def send_chat_message(self, chat_id: str, content: str) -> dict[str, Any]:
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
        response = self._post(url, data=payload)
        return self._handle_response(response)

    def send_channel_message(
        self, team_id: str, channel_id: str, content: str
    ) -> dict[str, Any]:
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
        response = self._post(url, data=payload)
        return self._handle_response(response)

    def reply_to_channel_message(
        self, team_id: str, channel_id: str, message_id: str, content: str
    ) -> dict[str, Any]:
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
        response = self._post(url, data=payload)
        return self._handle_response(response)

    def create_chat(
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
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/chats"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_chat_details(
        self,
        chat_id: str,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> Any:
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
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_chat_details(
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
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/chats/{chat_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def list_installed_chat_apps(
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
        Retrieves applications installed in a specific chat, identified by `chat_id`. Differentiating from `list_user_installed_apps`, which targets a user's personal scope, this function queries a single conversation. It supports optional parameters for advanced filtering, sorting, and pagination to customize the returned collection.

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
            chats.teamsAppInstallation
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        url = f"{self.base_url}/chats/{chat_id}/installedApps"
        query_params = {
            k: v
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
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_chat_members(
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
        query_params = {
            k: v
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
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def add_member_to_chat(
        self,
        chat_id: str,
        id: str | None = None,
        displayName: str | None = None,
        roles: list[str] | None = None,
        visibleHistoryStartDateTime: str | None = None,
    ) -> Any:
        """
        Adds a new member to a specific Microsoft Teams chat using its `chat_id`. This function allows for configuring member roles and chat history visibility. It is the direct counterpart to `delete_chat_member`, performing the 'create' action for a chat's membership.

        Args:
            chat_id (string): chat-id
            id (string): The unique identifier for an entity. Read-only.
            displayName (string): The display name of the user.
            roles (array): The roles for that user. This property contains more qualifiers only when relevant - for example, if the member has owner privileges, the roles property contains owner as one of the values. Similarly, if the member is an in-tenant guest, the roles property contains guest as one of the values. A basic member shouldn't have any values specified in the roles property. An Out-of-tenant external member is assigned the owner role.
            visibleHistoryStartDateTime (string): The timestamp denoting how far back a conversation's history is shared with the conversation member. This property is settable only for members of a chat.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.conversationMember
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "displayName": displayName,
            "roles": roles,
            "visibleHistoryStartDateTime": visibleHistoryStartDateTime,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/chats/{chat_id}/members"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_chat_member(
        self,
        chat_id: str,
        conversationMember_id: str,
        select: list[str] | None = None,
        expand: list[str] | None = None,
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
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_chat_member(self, chat_id: str, conversationMember_id: str) -> Any:
        """
        Removes a specific member from a chat using their unique ID and the chat's ID. This function sends a DELETE request to the Microsoft Graph API to permanently remove the user from the conversation, acting as the counterpart to `add_member_to_chat`.

        Args:
            chat_id (string): chat-id
            conversationMember_id (string): conversationMember-id

        Returns:
            Any: Success

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
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def list_chat_messages(
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
        query_params = {
            k: v
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
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_chat_message(
        self,
        chat_id: str,
        chatMessage_id: str,
        select: list[str] | None = None,
        expand: list[str] | None = None,
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
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_chat_message_replies(
        self,
        chat_id: str,
        chatMessage_id: str,
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
        Retrieves all replies for a specific message within a chat, using the parent message's ID. This function, unlike `get_chat_reply_details`, returns a collection and supports OData query parameters for advanced filtering, sorting, and pagination of the results.

        Args:
            chat_id (string): chat-id
            chatMessage_id (string): chatMessage-id
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
        if chatMessage_id is None:
            raise ValueError("Missing required parameter 'chatMessage-id'.")
        url = f"{self.base_url}/chats/{chat_id}/messages/{chatMessage_id}/replies"
        query_params = {
            k: v
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
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def reply_to_chat_message(
        self,
        chat_id: str,
        chatMessage_id: str,
        id: str | None = None,
        attachments: list[dict[str, dict[str, Any]]] | None = None,
        body: dict[str, dict[str, Any]] | None = None,
        channelIdentity: dict[str, dict[str, Any]] | None = None,
        chatId: str | None = None,
        createdDateTime: str | None = None,
        deletedDateTime: str | None = None,
        etag: str | None = None,
        eventDetail: dict[str, dict[str, Any]] | None = None,
        from_: Any | None = None,
        importance: str | None = None,
        lastEditedDateTime: str | None = None,
        lastModifiedDateTime: str | None = None,
        locale: str | None = None,
        mentions: list[dict[str, dict[str, Any]]] | None = None,
        messageHistory: list[dict[str, dict[str, Any]]] | None = None,
        messageType: str | None = None,
        policyViolation: dict[str, dict[str, Any]] | None = None,
        reactions: list[dict[str, dict[str, Any]]] | None = None,
        replyToId: str | None = None,
        subject: str | None = None,
        summary: str | None = None,
        webUrl: str | None = None,
        hostedContents: list[Any] | None = None,
        replies: list[Any] | None = None,
    ) -> Any:
        """
        Posts a reply to a specific message within a chat. This comprehensive function allows for detailed configuration of the reply's properties, like its body and attachments. It differs from `reply_to_channel_message`, which sends simpler replies to messages within team channels.

        Args:
            chat_id (string): chat-id
            chatMessage_id (string): chatMessage-id
            id (string): The unique identifier for an entity. Read-only.
            attachments (array): References to attached objects like files, tabs, meetings etc.
            body (object): body
            channelIdentity (object): channelIdentity
            chatId (string): If the message was sent in a chat, represents the identity of the chat.
            createdDateTime (string): Timestamp of when the chat message was created.
            deletedDateTime (string): Read only. Timestamp at which the chat message was deleted, or null if not deleted.
            etag (string): Read-only. Version number of the chat message.
            eventDetail (object): eventDetail
            from_ (string): from
            importance (string): importance
            lastEditedDateTime (string): Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Teams UI. If no edits are made the value is null.
            lastModifiedDateTime (string): Read only. Timestamp when the chat message is created (initial setting) or modified, including when a reaction is added or removed.
            locale (string): Locale of the chat message set by the client. Always set to en-us.
            mentions (array): List of entities mentioned in the chat message. Supported entities are: user, bot, team, channel, chat, and tag.
            messageHistory (array): List of activity history of a message item, including modification time and actions, such as reactionAdded, reactionRemoved, or reaction changes, on the message.
            messageType (string): messageType
            policyViolation (object): policyViolation
            reactions (array): Reactions for this chat message (for example, Like).
            replyToId (string): Read-only. ID of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels, not chats.)
            subject (string): The subject of the chat message, in plaintext.
            summary (string): Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.
            webUrl (string): Read-only. Link to the message in Microsoft Teams.
            hostedContents (array): Content in a message hosted by Microsoft Teams - for example, images or code snippets.
            replies (array): Replies for a specified message. Supports $expand for channel messages.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chatMessage
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        if chatMessage_id is None:
            raise ValueError("Missing required parameter 'chatMessage-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "attachments": attachments,
            "body": body,
            "channelIdentity": channelIdentity,
            "chatId": chatId,
            "createdDateTime": createdDateTime,
            "deletedDateTime": deletedDateTime,
            "etag": etag,
            "eventDetail": eventDetail,
            "from": from_,
            "importance": importance,
            "lastEditedDateTime": lastEditedDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "locale": locale,
            "mentions": mentions,
            "messageHistory": messageHistory,
            "messageType": messageType,
            "policyViolation": policyViolation,
            "reactions": reactions,
            "replyToId": replyToId,
            "subject": subject,
            "summary": summary,
            "webUrl": webUrl,
            "hostedContents": hostedContents,
            "replies": replies,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/chats/{chat_id}/messages/{chatMessage_id}/replies"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_chat_reply_details(
        self,
        chat_id: str,
        chatMessage_id: str,
        chatMessage_id1: str,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> Any:
        """
        Retrieves a specific reply from a chat message thread using the chat, parent message, and reply IDs. Unlike `list_chat_message_replies`, which fetches all replies, this function targets a single reply for detailed information, allowing for customized field selection.

        Args:
            chat_id (string): chat-id
            chatMessage_id (string): chatMessage-id
            chatMessage_id1 (string): chatMessage-id1
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
        if chatMessage_id1 is None:
            raise ValueError("Missing required parameter 'chatMessage-id1'.")
        url = f"{self.base_url}/chats/{chat_id}/messages/{chatMessage_id}/replies/{chatMessage_id1}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_team_from_group(
        self,
        group_id: str,
        id: str | None = None,
        classification: str | None = None,
        createdDateTime: str | None = None,
        description: str | None = None,
        displayName: str | None = None,
        firstChannelName: str | None = None,
        funSettings: dict[str, dict[str, Any]] | None = None,
        guestSettings: dict[str, dict[str, Any]] | None = None,
        internalId: str | None = None,
        isArchived: bool | None = None,
        memberSettings: dict[str, dict[str, Any]] | None = None,
        messagingSettings: dict[str, dict[str, Any]] | None = None,
        specialization: str | None = None,
        summary: dict[str, dict[str, Any]] | None = None,
        tenantId: str | None = None,
        visibility: str | None = None,
        webUrl: str | None = None,
        allChannels: list[Any] | None = None,
        channels: list[Any] | None = None,
        group: Any | None = None,
        incomingChannels: list[Any] | None = None,
        installedApps: list[Any] | None = None,
        members: list[Any] | None = None,
        operations: list[Any] | None = None,
        permissionGrants: list[Any] | None = None,
        photo: Any | None = None,
        primaryChannel: Any | None = None,
        schedule: Any | None = None,
        tags: list[Any] | None = None,
        template: Any | None = None,
    ) -> Any:
        """
        Enables Microsoft Teams functionality for a pre-existing Microsoft 365 group using its ID. This 'team-ifies' the group, allowing optional configuration of team properties. It differs from `create_team`, which provisions both a new team and its associated group simultaneously.

        Args:
            group_id (string): group-id
            id (string): The unique identifier for an entity. Read-only.
            classification (string): An optional label. Typically describes the data or business sensitivity of the team. Must match one of a preconfigured set in the tenant's directory.
            createdDateTime (string): Timestamp at which the team was created.
            description (string): An optional description for the team. Maximum length: 1,024 characters.
            displayName (string): The name of the team.
            firstChannelName (string): The name of the first channel in the team. This is an optional property, only used during team creation and isn't returned in methods to get and list teams.
            funSettings (object): funSettings
            guestSettings (object): guestSettings
            internalId (string): A unique ID for the team that was used in a few places such as the audit log/Office 365 Management Activity API.
            isArchived (boolean): Whether this team is in read-only mode.
            memberSettings (object): memberSettings
            messagingSettings (object): messagingSettings
            specialization (string): specialization
            summary (object): summary
            tenantId (string): The ID of the Microsoft Entra tenant.
            visibility (string): visibility
            webUrl (string): A hyperlink that goes to the team in the Microsoft Teams client. You get this URL when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.
            allChannels (array): List of channels either hosted in or shared with the team (incoming channels).
            channels (array): The collection of channels and messages associated with the team.
            group (string): group
            incomingChannels (array): List of channels shared with the team.
            installedApps (array): The apps installed in this team.
            members (array): Members and owners of the team.
            operations (array): The async operations that ran or are running on this team.
            permissionGrants (array): A collection of permissions granted to apps to access the team.
            photo (string): photo
            primaryChannel (string): primaryChannel
            schedule (string): schedule
            tags (array): The tags associated with the team.
            template (string): template

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            groups.team
        """
        if group_id is None:
            raise ValueError("Missing required parameter 'group-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "classification": classification,
            "createdDateTime": createdDateTime,
            "description": description,
            "displayName": displayName,
            "firstChannelName": firstChannelName,
            "funSettings": funSettings,
            "guestSettings": guestSettings,
            "internalId": internalId,
            "isArchived": isArchived,
            "memberSettings": memberSettings,
            "messagingSettings": messagingSettings,
            "specialization": specialization,
            "summary": summary,
            "tenantId": tenantId,
            "visibility": visibility,
            "webUrl": webUrl,
            "allChannels": allChannels,
            "channels": channels,
            "group": group,
            "incomingChannels": incomingChannels,
            "installedApps": installedApps,
            "members": members,
            "operations": operations,
            "permissionGrants": permissionGrants,
            "photo": photo,
            "primaryChannel": primaryChannel,
            "schedule": schedule,
            "tags": tags,
            "template": template,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/groups/{group_id}/team"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_team(
        self,
        id: str | None = None,
        classification: str | None = None,
        createdDateTime: str | None = None,
        description: str | None = None,
        displayName: str | None = None,
        firstChannelName: str | None = None,
        funSettings: dict[str, dict[str, Any]] | None = None,
        guestSettings: dict[str, dict[str, Any]] | None = None,
        internalId: str | None = None,
        isArchived: bool | None = None,
        memberSettings: dict[str, dict[str, Any]] | None = None,
        messagingSettings: dict[str, dict[str, Any]] | None = None,
        specialization: str | None = None,
        summary: dict[str, dict[str, Any]] | None = None,
        tenantId: str | None = None,
        visibility: str | None = None,
        webUrl: str | None = None,
        allChannels: list[Any] | None = None,
        channels: list[Any] | None = None,
        group: Any | None = None,
        incomingChannels: list[Any] | None = None,
        installedApps: list[Any] | None = None,
        members: list[Any] | None = None,
        operations: list[Any] | None = None,
        permissionGrants: list[Any] | None = None,
        photo: Any | None = None,
        primaryChannel: Any | None = None,
        schedule: Any | None = None,
        tags: list[Any] | None = None,
        template: Any | None = None,
    ) -> Any:
        """
        Creates a new Microsoft Team and its associated Microsoft 365 group. This method builds a team from scratch, allowing specification of initial properties like display name, description, and members. It differs from `create_team_from_group`, which enables team functionality for an existing group.

        Args:
            id (string): The unique identifier for an entity. Read-only.
            classification (string): An optional label. Typically describes the data or business sensitivity of the team. Must match one of a preconfigured set in the tenant's directory.
            createdDateTime (string): Timestamp at which the team was created.
            description (string): An optional description for the team. Maximum length: 1,024 characters.
            displayName (string): The name of the team.
            firstChannelName (string): The name of the first channel in the team. This is an optional property, only used during team creation and isn't returned in methods to get and list teams.
            funSettings (object): funSettings
            guestSettings (object): guestSettings
            internalId (string): A unique ID for the team that was used in a few places such as the audit log/Office 365 Management Activity API.
            isArchived (boolean): Whether this team is in read-only mode.
            memberSettings (object): memberSettings
            messagingSettings (object): messagingSettings
            specialization (string): specialization
            summary (object): summary
            tenantId (string): The ID of the Microsoft Entra tenant.
            visibility (string): visibility
            webUrl (string): A hyperlink that goes to the team in the Microsoft Teams client. You get this URL when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.
            allChannels (array): List of channels either hosted in or shared with the team (incoming channels).
            channels (array): The collection of channels and messages associated with the team.
            group (string): group
            incomingChannels (array): List of channels shared with the team.
            installedApps (array): The apps installed in this team.
            members (array): Members and owners of the team.
            operations (array): The async operations that ran or are running on this team.
            permissionGrants (array): A collection of permissions granted to apps to access the team.
            photo (string): photo
            primaryChannel (string): primaryChannel
            schedule (string): schedule
            tags (array): The tags associated with the team.
            template (string): template

        Returns:
            Any: Created entity

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            teams.team
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "classification": classification,
            "createdDateTime": createdDateTime,
            "description": description,
            "displayName": displayName,
            "firstChannelName": firstChannelName,
            "funSettings": funSettings,
            "guestSettings": guestSettings,
            "internalId": internalId,
            "isArchived": isArchived,
            "memberSettings": memberSettings,
            "messagingSettings": messagingSettings,
            "specialization": specialization,
            "summary": summary,
            "tenantId": tenantId,
            "visibility": visibility,
            "webUrl": webUrl,
            "allChannels": allChannels,
            "channels": channels,
            "group": group,
            "incomingChannels": incomingChannels,
            "installedApps": installedApps,
            "members": members,
            "operations": operations,
            "permissionGrants": permissionGrants,
            "photo": photo,
            "primaryChannel": primaryChannel,
            "schedule": schedule,
            "tags": tags,
            "template": template,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/teams"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_channel_details(
        self,
        team_id: str,
        channel_id: str,
        select: list[str] | None = None,
        expand: list[str] | None = None,
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
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chatMessage_id: str,
        id: str | None = None,
        attachments: list[dict[str, dict[str, Any]]] | None = None,
        body: dict[str, dict[str, Any]] | None = None,
        channelIdentity: dict[str, dict[str, Any]] | None = None,
        chatId: str | None = None,
        createdDateTime: str | None = None,
        deletedDateTime: str | None = None,
        etag: str | None = None,
        eventDetail: dict[str, dict[str, Any]] | None = None,
        from_: Any | None = None,
        importance: str | None = None,
        lastEditedDateTime: str | None = None,
        lastModifiedDateTime: str | None = None,
        locale: str | None = None,
        mentions: list[dict[str, dict[str, Any]]] | None = None,
        messageHistory: list[dict[str, dict[str, Any]]] | None = None,
        messageType: str | None = None,
        policyViolation: dict[str, dict[str, Any]] | None = None,
        reactions: list[dict[str, dict[str, Any]]] | None = None,
        replyToId: str | None = None,
        subject: str | None = None,
        summary: str | None = None,
        webUrl: str | None = None,
        hostedContents: list[Any] | None = None,
        replies: list[Any] | None = None,
    ) -> Any:
        """
        Updates an existing message within a Microsoft Teams channel, identified by team, channel, and message IDs. This function modifies the original message's properties, like its body, via a PATCH request, distinguishing it from functions that create new messages or update replies.

        Args:
            team_id (string): team-id
            channel_id (string): channel-id
            chatMessage_id (string): chatMessage-id
            id (string): The unique identifier for an entity. Read-only.
            attachments (array): References to attached objects like files, tabs, meetings etc.
            body (object): body
            channelIdentity (object): channelIdentity
            chatId (string): If the message was sent in a chat, represents the identity of the chat.
            createdDateTime (string): Timestamp of when the chat message was created.
            deletedDateTime (string): Read only. Timestamp at which the chat message was deleted, or null if not deleted.
            etag (string): Read-only. Version number of the chat message.
            eventDetail (object): eventDetail
            from_ (string): from
            importance (string): importance
            lastEditedDateTime (string): Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Teams UI. If no edits are made the value is null.
            lastModifiedDateTime (string): Read only. Timestamp when the chat message is created (initial setting) or modified, including when a reaction is added or removed.
            locale (string): Locale of the chat message set by the client. Always set to en-us.
            mentions (array): List of entities mentioned in the chat message. Supported entities are: user, bot, team, channel, chat, and tag.
            messageHistory (array): List of activity history of a message item, including modification time and actions, such as reactionAdded, reactionRemoved, or reaction changes, on the message.
            messageType (string): messageType
            policyViolation (object): policyViolation
            reactions (array): Reactions for this chat message (for example, Like).
            replyToId (string): Read-only. ID of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels, not chats.)
            subject (string): The subject of the chat message, in plaintext.
            summary (string): Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.
            webUrl (string): Read-only. Link to the message in Microsoft Teams.
            hostedContents (array): Content in a message hosted by Microsoft Teams - for example, images or code snippets.
            replies (array): Replies for a specified message. Supports $expand for channel messages.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            teams.channel
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'.")
        if chatMessage_id is None:
            raise ValueError("Missing required parameter 'chatMessage-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "attachments": attachments,
            "body": body,
            "channelIdentity": channelIdentity,
            "chatId": chatId,
            "createdDateTime": createdDateTime,
            "deletedDateTime": deletedDateTime,
            "etag": etag,
            "eventDetail": eventDetail,
            "from": from_,
            "importance": importance,
            "lastEditedDateTime": lastEditedDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "locale": locale,
            "mentions": mentions,
            "messageHistory": messageHistory,
            "messageType": messageType,
            "policyViolation": policyViolation,
            "reactions": reactions,
            "replyToId": replyToId,
            "subject": subject,
            "summary": summary,
            "webUrl": webUrl,
            "hostedContents": hostedContents,
            "replies": replies,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}/messages/{chatMessage_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def update_channel_message_reply(
        self,
        team_id: str,
        channel_id: str,
        chatMessage_id: str,
        chatMessage_id1: str,
        id: str | None = None,
        attachments: list[dict[str, dict[str, Any]]] | None = None,
        body: dict[str, dict[str, Any]] | None = None,
        channelIdentity: dict[str, dict[str, Any]] | None = None,
        chatId: str | None = None,
        createdDateTime: str | None = None,
        deletedDateTime: str | None = None,
        etag: str | None = None,
        eventDetail: dict[str, dict[str, Any]] | None = None,
        from_: Any | None = None,
        importance: str | None = None,
        lastEditedDateTime: str | None = None,
        lastModifiedDateTime: str | None = None,
        locale: str | None = None,
        mentions: list[dict[str, dict[str, Any]]] | None = None,
        messageHistory: list[dict[str, dict[str, Any]]] | None = None,
        messageType: str | None = None,
        policyViolation: dict[str, dict[str, Any]] | None = None,
        reactions: list[dict[str, dict[str, Any]]] | None = None,
        replyToId: str | None = None,
        subject: str | None = None,
        summary: str | None = None,
        webUrl: str | None = None,
        hostedContents: list[Any] | None = None,
        replies: list[Any] | None = None,
    ) -> Any:
        """
        Updates an existing reply to a specific message within a Microsoft Teams channel. It identifies the target reply using team, channel, parent message, and reply IDs, modifying its properties (e.g., body content, attachments) via a PATCH request.

        Args:
            team_id (string): team-id
            channel_id (string): channel-id
            chatMessage_id (string): chatMessage-id
            chatMessage_id1 (string): chatMessage-id1
            id (string): The unique identifier for an entity. Read-only.
            attachments (array): References to attached objects like files, tabs, meetings etc.
            body (object): body
            channelIdentity (object): channelIdentity
            chatId (string): If the message was sent in a chat, represents the identity of the chat.
            createdDateTime (string): Timestamp of when the chat message was created.
            deletedDateTime (string): Read only. Timestamp at which the chat message was deleted, or null if not deleted.
            etag (string): Read-only. Version number of the chat message.
            eventDetail (object): eventDetail
            from_ (string): from
            importance (string): importance
            lastEditedDateTime (string): Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Teams UI. If no edits are made the value is null.
            lastModifiedDateTime (string): Read only. Timestamp when the chat message is created (initial setting) or modified, including when a reaction is added or removed.
            locale (string): Locale of the chat message set by the client. Always set to en-us.
            mentions (array): List of entities mentioned in the chat message. Supported entities are: user, bot, team, channel, chat, and tag.
            messageHistory (array): List of activity history of a message item, including modification time and actions, such as reactionAdded, reactionRemoved, or reaction changes, on the message.
            messageType (string): messageType
            policyViolation (object): policyViolation
            reactions (array): Reactions for this chat message (for example, Like).
            replyToId (string): Read-only. ID of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels, not chats.)
            subject (string): The subject of the chat message, in plaintext.
            summary (string): Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.
            webUrl (string): Read-only. Link to the message in Microsoft Teams.
            hostedContents (array): Content in a message hosted by Microsoft Teams - for example, images or code snippets.
            replies (array): Replies for a specified message. Supports $expand for channel messages.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            teams.channel
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'.")
        if chatMessage_id is None:
            raise ValueError("Missing required parameter 'chatMessage-id'.")
        if chatMessage_id1 is None:
            raise ValueError("Missing required parameter 'chatMessage-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "attachments": attachments,
            "body": body,
            "channelIdentity": channelIdentity,
            "chatId": chatId,
            "createdDateTime": createdDateTime,
            "deletedDateTime": deletedDateTime,
            "etag": etag,
            "eventDetail": eventDetail,
            "from": from_,
            "importance": importance,
            "lastEditedDateTime": lastEditedDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "locale": locale,
            "mentions": mentions,
            "messageHistory": messageHistory,
            "messageType": messageType,
            "policyViolation": policyViolation,
            "reactions": reactions,
            "replyToId": replyToId,
            "subject": subject,
            "summary": summary,
            "webUrl": webUrl,
            "hostedContents": hostedContents,
            "replies": replies,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}/messages/{chatMessage_id}/replies/{chatMessage_id1}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def list_channel_tabs(
        self,
        team_id: str,
        channel_id: str,
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
        Retrieves a collection of tabs from a specified channel within a Microsoft Teams team. Unlike `get_channel_tab_details`, which fetches a single tab, this function lists all tabs and supports advanced OData query parameters for filtering, sorting, and pagination of the entire collection.

        Args:
            team_id (string): team-id
            channel_id (string): channel-id
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
            teams.channel
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'.")
        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}/tabs"
        query_params = {
            k: v
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
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_channel_tab(
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
        request_body_data = {
            "id": id,
            "configuration": configuration,
            "displayName": displayName,
            "webUrl": webUrl,
            "teamsApp": teamsApp,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}/tabs"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_channel_tab_details(
        self,
        team_id: str,
        channel_id: str,
        teamsTab_id: str,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> Any:
        """
        Fetches properties for a single tab within a specific Microsoft Teams channel, identified by its team, channel, and tab IDs. Unlike `list_channel_tabs` which gets all tabs, this targets a specific one, with options to select fields or expand related entities in the response.

        Args:
            team_id (string): team-id
            channel_id (string): channel-id
            teamsTab_id (string): teamsTab-id
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
        if teamsTab_id is None:
            raise ValueError("Missing required parameter 'teamsTab-id'.")
        url = (
            f"{self.base_url}/teams/{team_id}/channels/{channel_id}/tabs/{teamsTab_id}"
        )
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_channel_tab(
        self,
        team_id: str,
        channel_id: str,
        teamsTab_id: str,
        id: str | None = None,
        configuration: dict[str, dict[str, Any]] | None = None,
        displayName: str | None = None,
        webUrl: str | None = None,
        teamsApp: Any | None = None,
    ) -> Any:
        """
        Modifies properties of an existing tab within a specific Microsoft Teams channel. It uses the team, channel, and tab IDs to target the tab, allowing for partial updates to its configuration or display name via a PATCH request, differentiating it from tab creation or deletion functions.

        Args:
            team_id (string): team-id
            channel_id (string): channel-id
            teamsTab_id (string): teamsTab-id
            id (string): The unique identifier for an entity. Read-only.
            configuration (object): configuration
            displayName (string): Name of the tab.
            webUrl (string): Deep link URL of the tab instance. Read only.
            teamsApp (string): teamsApp

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            teams.channel
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'.")
        if teamsTab_id is None:
            raise ValueError("Missing required parameter 'teamsTab-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "configuration": configuration,
            "displayName": displayName,
            "webUrl": webUrl,
            "teamsApp": teamsApp,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.base_url}/teams/{team_id}/channels/{channel_id}/tabs/{teamsTab_id}"
        )
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def delete_channel_tab(
        self, team_id: str, channel_id: str, teamsTab_id: str
    ) -> Any:
        """
        Permanently removes a specific tab from a Microsoft Teams channel using its unique ID, along with the parent team and channel IDs. This function is the destructive counterpart to `create_channel_tab`, designed to delete a tab rather than create, list, or update one.

        Args:
            team_id (string): team-id
            channel_id (string): channel-id
            teamsTab_id (string): teamsTab-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            teams.channel
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'.")
        if teamsTab_id is None:
            raise ValueError("Missing required parameter 'teamsTab-id'.")
        url = (
            f"{self.base_url}/teams/{team_id}/channels/{channel_id}/tabs/{teamsTab_id}"
        )
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def get_primary_team_channel(
        self,
        team_id: str,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> Any:
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
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_user_installed_apps(
        self,
        user_id: str,
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
        Retrieves applications installed in a user's personal Microsoft Teams scope, identified by their ID. Unlike `list_installed_chat_apps` which targets chat installations, this focuses on the user's scope. It supports optional OData parameters for filtering, sorting, and pagination to customize the returned app collection.

        Args:
            user_id (string): user-id
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
            users.userTeamwork
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.base_url}/users/{user_id}/teamwork/installedApps"
        query_params = {
            k: v
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
        response = self._get(url, params=query_params)
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
            self.list_installed_chat_apps,
            self.list_chat_members,
            self.add_member_to_chat,
            self.get_chat_member,
            self.delete_chat_member,
            self.list_chat_messages,
            self.get_chat_message,
            self.list_chat_message_replies,
            self.reply_to_chat_message,
            self.get_chat_reply_details,
            self.create_team_from_group,
            self.create_team,
            self.get_channel_details,
            self.update_channel_message,
            self.update_channel_message_reply,
            self.list_channel_tabs,
            self.create_channel_tab,
            self.get_channel_tab_details,
            self.update_channel_tab,
            self.delete_channel_tab,
            self.get_primary_team_channel,
            self.list_user_installed_apps,
        ]
