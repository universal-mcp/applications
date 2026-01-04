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

# Chat Messages

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
        self, chat_id: str, chatMessage_id: str
    ) -> Any:
        """
        Retrieves the full details of a single message from a specific chat using both chat and message IDs.
        Note: The Microsoft Graph API for this endpoint does NOT support OData query parameters like $select or $expand.

        Args:
            chat_id (string): The unique identifier of the chat.
            chatMessage_id (string): The unique identifier of the message.

        Returns:
            Any: Retrieved chatMessage entity.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            chats.chatMessage, read
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        if chatMessage_id is None:
            raise ValueError("Missing required parameter 'chatMessage-id'.")
        url = f"{self.base_url}/chats/{chat_id}/messages/{chatMessage_id}"
        
        # This endpoint explicitly does not support OData params
        response = await self._aget(url)
        return self._handle_response(response)

    async def send_chat_message(self, chat_id: str, content: str) -> dict[str, Any]:
        """
        Posts a new message to a specific Microsoft Teams chat using its unique ID.
        
        Args:
            chat_id (string): The unique identifier of the chat.
            content (string): The message content to send (plain text or HTML).

        Returns:
            dict[str, Any]: A dictionary containing the API response for the sent message, including its ID.

        Raises:
            HTTPStatusError: If the API request fails due to invalid ID, permissions, etc.

        Tags:
            chats.chatMessage, create, send
        """
        if chat_id is None:
            raise ValueError("Missing required parameter 'chat-id'.")
        
        url = f"{self.base_url}/chats/{chat_id}/messages"
        payload = {"body": {"content": content}}
        
        response = await self._apost(url, data=payload)
        return self._handle_response(response)

    async def list_all_channels(
        self,
        team_id: str,
        filter: str | None = None,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves the list of channels either in this team or shared with this team (incoming channels).
        Supported OData parameters:
        - $filter: Filter by property values.
        - $select: Select specific properties to return (recommended for performance).
        - $expand: Expand related entities.

        Args:
            team_id (string): The unique identifier of the team.
            filter (string): Filter items by property values.
            select (array): Select properties to be returned.
            expand (array): Expand related entities.

        Returns:
            dict[str, Any]: Retrieved collection of channels.

        Raises:
            HTTPStatusError: If the API request fails.

        Tags:
            teams.channel, list, read
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")

        url = f"{self.base_url}/teams/{team_id}/allChannels"

        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {
            k: fmt(v)
            for k, v in [
                ("$filter", filter),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }

        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    async def get_channel(
        self,
        team_id: str,
        channel_id: str,
        select: list[str] | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve the properties and relationships of a channel.
        Supported OData parameters:
        - $select: Select specific properties to return (recommended for performance).
        - $expand: Expand related entities.

        Args:
            team_id (string): The unique identifier of the team.
            channel_id (string): The unique identifier of the channel.
            select (array): Select properties to be returned.
            expand (array): Expand related entities.

        Returns:
            dict[str, Any]: Retrieved channel entity.

        Raises:
            HTTPStatusError: If the API request fails.

        Tags:
            teams.channel, read
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team-id'.")
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'.")

        url = f"{self.base_url}/teams/{team_id}/channels/{channel_id}"

        # Helper to format list params
        def fmt(val):
            return ",".join(val) if isinstance(val, list) else val

        query_params = {
            k: fmt(v)
            for k, v in [
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }

        response = await self._aget(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.get_user_chats,
            self.create_chat,
            self.get_chat_details,
            self.update_chat_details,
            self.list_chat_members,
            self.get_chat_member,
            self.list_chat_messages,
            self.get_chat_message,
            self.send_chat_message,
            self.list_all_channels,
            self.get_channel,
        ]
