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
        Fetches all Microsoft Teams the authenticated user is a member of. This function queries the `/me/joinedTeams` API endpoint, returning a list of dictionaries where each dictionary contains the details of a specific team.
        
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
        Retrieves channels for a specified Microsoft Teams team using its unique ID. Optional parameters allow for advanced querying, including filtering, searching, sorting, and pagination of the results, to customize the returned collection of channels.
        
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
        Posts a new message to a specific Microsoft Teams chat using its unique ID. It sends a POST request to the Graph API endpoint with the provided content (text/HTML). This function targets direct/group chats, differentiating it from `send_channel_message`, which posts to team channels.
        
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
        Posts a new message to a specified channel within a Microsoft Teams team using the team and channel IDs. This function initiates a new conversation thread, unlike `reply_to_channel_message`. The content can be plain text or HTML. It differs from `send_chat_message` which targets private/group chats.
        
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
        Posts a reply to a specific message within a Microsoft Teams channel. It uses the team, channel, and original message IDs to target the correct conversation thread, distinguishing it from `send_channel_message` which starts a new thread.
        
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
        Creates a new Microsoft Teams chat conversation. It takes optional parameters like chat type, topic, and members to configure the chat. This function sends a POST request to the `/chats` API endpoint, initiating a new one-on-one or group chat based on the provided details.
        
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
        Retrieves the properties and relationships of a specific chat conversation by its unique ID. Optional parameters can select specific fields or expand related entities in the response, such as chat members or installed apps.
        
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
        Updates properties of a specific chat, such as its topic, using its unique ID. This function performs a partial update (PATCH) on an existing chat, distinguishing it from `get_chat` which only retrieves data, and `create_chat_operation` which creates an entirely new chat conversation.
        
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
        Retrieves the collection of applications installed within a specific Microsoft Teams chat, identified by its ID. It supports advanced querying through optional parameters for pagination, filtering, searching, and sorting to customize the results.
        
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
        Retrieves a list of members for a specific chat, identified by `chat_id`. Supports advanced querying, including pagination, filtering, searching, and sorting. This function lists all members, unlike `get_chat_member_details` which fetches information for a single member.
        
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
        Adds a member to a specified Microsoft Teams chat using its `chat_id`. Details such as the member's roles and the extent of their visible chat history can be provided. This operation sends a POST request to the `/chats/{chat_id}/members` API endpoint.
        
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
        Retrieves detailed information for a specific member within a chat using their unique ID. Unlike `list_chat_members` which fetches all members, this function targets a single individual. The response can be customized by selecting specific properties or expanding related entities.
        
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
        Removes a specific member from a chat using their unique ID and the chat's ID. This function sends a DELETE request to the Microsoft Graph API to permanently remove the user from the specified conversation, acting as the counterpart to `add_member_to_chat`.
        
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
        Retrieves a collection of messages from a specific chat, identified by its unique ID. Supports advanced querying with options for pagination (top, skip), filtering, sorting, and searching to refine the results, distinguishing it from functions that get single messages or replies.
        
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
        Retrieves the full details of a single message from a specific chat, identified by both the chat and message IDs. Supports optional query parameters to select specific properties or expand related entities, enabling customized API responses for a particular message.
        
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
        Retrieves a collection of replies for a specific message within a given chat. It identifies the parent message using `chat_id` and `chatMessage_id` and supports optional OData query parameters for advanced filtering, sorting, and pagination of the results.
        
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
        Posts a reply to a specific message within a chat. This comprehensive function allows for detailed configuration of the reply message's properties, such as its body and attachments. It is distinct from `reply_to_channel_message`, which sends simple replies to messages within team channels.
        
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
        Retrieves a single, specific reply from a chat message thread using its unique ID, requiring the parent message and chat IDs. It targets one reply for detailed information, unlike `read_chat_replies` which lists all replies to a parent message.
        
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
        Enables a Microsoft Teams instance for a pre-existing Microsoft 365 group, identified by its ID. This 'team-ifies' the group, allowing optional team properties to be configured. It differs from `create_team`, which provisions a new team and group simultaneously.
        
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
        Retrieves detailed information for a specific channel within a Microsoft Teams team, identified by both team and channel IDs. Optional parameters allow for selecting specific properties or expanding related entities in the response to get more targeted data.
        
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
        Updates properties of a specific message within a Microsoft Teams channel, identified by its team, channel, and message IDs. It applies modifications like changing the message body or attachments by sending a PATCH request to the Microsoft Graph API.
        
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
        Retrieves a list of all tabs within a specific channel of a Microsoft Teams team. Supports advanced OData query parameters for filtering, sorting, and pagination, allowing for customized retrieval of the tab collection.
        
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
        Adds a new tab to a specified channel within a Microsoft Teams team. It requires team and channel IDs to target the location, and accepts optional configuration details like the tab's display name and associated application to create the new tab.
        
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
        Retrieves detailed information for a specific tab within a channel using its unique ID. Requires team and channel identifiers to locate the resource. This function fetches a single tab, unlike `get_channel_tabs` which lists all tabs for the channel.
        
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
        Updates an existing tab within a specific channel of a Microsoft Teams team. It identifies the tab using team, channel, and tab IDs to modify properties like its display name or configuration. This function performs a partial update on the tab's resource.
        
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
        Deletes a specific tab from a Microsoft Teams channel. The function requires the team ID, channel ID, and the tab's unique ID to target and permanently remove the specified tab from the channel's interface.
        
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
        Retrieves details for the primary channel (typically 'General') of a specified Microsoft Teams team. Optional parameters allow for selecting specific properties or expanding related entities in the API response. This differs from `get_team_channel_info`, which requires a specific channel ID.
        
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
        Retrieves the collection of applications installed in a specific user's personal Microsoft Teams scope. This function accepts optional parameters for filtering, sorting, and pagination, enabling customized queries to refine the list of apps returned from the Microsoft Graph API.
        
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
