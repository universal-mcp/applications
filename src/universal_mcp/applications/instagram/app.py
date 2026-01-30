import os
from collections.abc import Callable
from typing import Any, Literal
import requests

from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class InstagramApp(APIApplication):
    """
    Instagram API integration via Unipile.
    """

    def __init__(self, integration: Integration) -> None:
        """
        Initialize the InstagramApp.

        Args:
            integration: The integration configuration containing credentials and other settings.
                         It is expected that the integration provides the 'x-api-key'
                         via headers in `integration.get_credentials_async()`, e.g.,
                         `{"headers": {"x-api-key": "YOUR_API_KEY"}}`.
        """
        super().__init__(name="instagram", integration=integration)
        self._base_url = None
        self._account_id = None

    async def _get_account_id(self) -> str | None:
        if self._account_id:
            return self._account_id
        if self.integration:
            credentials = await self.integration.get_credentials_async()
            self._account_id = credentials.get("account_id")
        else:
            logger.warning("Integration not found")
        return self._account_id

    @property
    def base_url(self) -> str:
        if not self._base_url:
            unipile_dsn = os.getenv("UNIPILE_DSN")
            if not unipile_dsn:
                logger.error("UnipileApp: UNIPILE_DSN environment variable is not set.")
                raise ValueError("UnipileApp: UNIPILE_DSN environment variable is required.")
            self._base_url = f"https://{unipile_dsn}"
        return self._base_url

    @base_url.setter
    def base_url(self, base_url: str) -> None:
        self._base_url = base_url
        logger.info(f"UnipileApp: Base URL set to {self._base_url}")

    def _get_headers(self) -> dict[str, str]:
        """
        Get the headers for Unipile API requests.
        Overrides the base class method to use X-Api-Key.
        """
        if not self.integration:
            logger.warning("UnipileApp: No integration configured, returning empty headers.")
            return {}
        api_key = os.getenv("UNIPILE_API_KEY")
        if not api_key:
            logger.error("UnipileApp: API key not found in integration credentials for Unipile.")
            return {"Content-Type": "application/json", "Cache-Control": "no-cache"}
        logger.debug("UnipileApp: Using X-Api-Key for authentication.")
        return {"x-api-key": api_key, "Content-Type": "application/json", "Cache-Control": "no-cache"}

    async def _aget_headers(self) -> dict[str, str]:
        """
        Get the headers for Unipile API requests asynchronously.
        Overrides the base class method to use X-Api-Key.
        """
        return self._get_headers()

    async def start_new_chat(self, provider_id: str, text: str) -> dict[str, Any]:
        """
        Starts a new chat conversation with a specified user by sending an initial message.
        This function constructs a multipart/form-data request using the `files` parameter
        to ensure correct formatting and headers, working around potential issues in the
        underlying request method.

        Args:
            provider_id: The Instagram provider ID of the user to start the chat with.
                        This is available in the response of the `retrieve_user_profile` tool.
            text: The initial message content.

        Returns:
            A dictionary containing the details of the newly created chat.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, chat, create, start, new, messaging, api, important
        """
        url = f"{self.base_url}/api/v1/chats"
        form_payload = {"account_id": (None, await self._get_account_id()), "text": (None, text), "attendees_ids": (None, provider_id)}
        api_key = os.getenv("UNIPILE_API_KEY")
        if not api_key:
            raise ValueError("UNIPILE_API_KEY environment variable is not set.")
        headers = {"x-api-key": api_key}
        response = requests.post(url, files=form_payload, headers=headers)
        return self._handle_response(response)

    async def list_all_chats(
        self,
        unread: bool | None = None,
        cursor: str | None = None,
        before: str | None = None,
        after: str | None = None,
        limit: int | None = None,
        account_type: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of all chat conversations across linked accounts. Supports filtering by unread status, date range, and account provider, distinguishing it from functions listing messages within a single chat.

        Args:
            unread: Filter for unread chats only or read chats only.
            cursor: Pagination cursor for the next page of entries.
            before: Filter for items created before this ISO 8601 UTC datetime (exclusive).
            after: Filter for items created after this ISO 8601 UTC datetime (exclusive).
            limit: Number of items to return (1-250).
            account_type: Filter by provider (e.g., "instagram").

        Returns:
            A dictionary containing a list of chat objects and a pagination cursor.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, chat, list, messaging, api
        """
        url = f"{self.base_url}/api/v1/chats"
        params: dict[str, Any] = {}
        params["account_id"] = await self._get_account_id()
        if unread is not None:
            params["unread"] = unread
        if cursor:
            params["cursor"] = cursor
        if before:
            params["before"] = before
        if after:
            params["after"] = after
        if limit:
            params["limit"] = limit
        if account_type:
            params["account_type"] = account_type
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def list_chat_messages(
        self,
        chat_id: str,
        cursor: str | None = None,
        before: str | None = None,
        after: str | None = None,
        limit: int | None = None,
        sender_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves messages from a specific chat identified by `chat_id`. Supports pagination and filtering by date or sender. Unlike `list_all_messages`, which fetches from all chats, this function targets the contents of a single conversation.

        Args:
            chat_id: The ID of the chat to retrieve messages from.
            cursor: Pagination cursor for the next page of entries.
            before: Filter for items created before this ISO 8601 UTC datetime (exclusive).
            after: Filter for items created after this ISO 8601 UTC datetime (exclusive).
            limit: Number of items to return (1-250).
            sender_id: Filter messages from a specific sender ID.

        Returns:
            A dictionary containing a list of message objects and a pagination cursor.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, chat, message, list, messaging, api
        """
        url = f"{self.base_url}/api/v1/chats/{chat_id}/messages"
        params: dict[str, Any] = {}
        if cursor:
            params["cursor"] = cursor
        if before:
            params["before"] = before
        if after:
            params["after"] = after
        if limit:
            params["limit"] = limit
        if sender_id:
            params["sender_id"] = sender_id
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def send_chat_message(self, chat_id: str, text: str) -> dict[str, Any]:
        """
        Sends a text message to a specific chat conversation using its `chat_id`. This function creates a new message via a POST request, distinguishing it from read-only functions like `list_chat_messages`. It returns the API's response, which typically confirms the successful creation of the message.

        Args:
            chat_id: The ID of the chat where the message will be sent.
            text: The text content of the message.
            attachments: Optional list of attachment objects to include with the message.

        Returns:
            A dictionary containing the ID of the sent message.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, chat, message, send, create, messaging, api
        """
        url = f"{self.base_url}/api/v1/chats/{chat_id}/messages"
        payload: dict[str, Any] = {"text": text}
        response = await self._apost(url, data=payload)
        return self._handle_response(response)

    async def retrieve_chat(self, chat_id: str) -> dict[str, Any]:
        """
        Retrieves a single chat's details using its Unipile or provider-specific ID. This function is distinct from `list_all_chats`, which returns a collection, by targeting one specific conversation.

        Args:
            chat_id: The Unipile or provider ID of the chat.

        Returns:
            A dictionary containing the chat object details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, chat, retrieve, get, messaging, api
        """
        url = f"{self.base_url}/api/v1/chats/{chat_id}"
        params: dict[str, Any] = {}
        if await self._get_account_id():
            params["account_id"] = await self._get_account_id()
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def list_all_messages(
        self,
        cursor: str | None = None,
        before: str | None = None,
        after: str | None = None,
        limit: int | None = None,
        sender_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of messages from all chats associated with the account. Unlike `list_chat_messages` which targets a specific conversation, this function provides a global message view, filterable by sender and date range.

        Args:
            cursor: Pagination cursor.
            before: Filter for items created before this ISO 8601 UTC datetime.
            after: Filter for items created after this ISO 8601 UTC datetime.
            limit: Number of items to return (1-250).
            sender_id: Filter messages from a specific sender.

        Returns:
            A dictionary containing a list of message objects and a pagination cursor.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, message, list, all_messages, messaging, api
        """
        url = f"{self.base_url}/api/v1/messages"
        params: dict[str, Any] = {}
        if cursor:
            params["cursor"] = cursor
        if before:
            params["before"] = before
        if after:
            params["after"] = after
        if limit:
            params["limit"] = limit
        if sender_id:
            params["sender_id"] = sender_id
        if await self._get_account_id():
            params["account_id"] = await self._get_account_id()
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def list_profile_posts(
        self, provider_id: str, cursor: str | None = None, limit: int | None = None, is_company: bool | None = None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of posts from a specific user or company profile using their provider ID. An authorizing `account_id` is required, and the `is_company` flag must specify the entity type, distinguishing this from `retrieve_post` which fetches a single post by its own ID.

        Args:
            provider_id: The entity's provider internal ID (Instagram ID).
            cursor: Pagination cursor.
            limit: Number of items to return (1-100).
            is_company: Boolean indicating if the provider_id is for a company.

        Returns:
            A dictionary containing a list of post objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, post, list, user_posts, company_posts, content, api, important
        """
        url = f"{self.base_url}/api/v1/users/{provider_id}/posts"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        if is_company is not None:
            params["is_company"] = is_company
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def list_profile_comments(self, provider_id: str, limit: int | None = None, cursor: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of comments made by a specific user using their provider ID.

        Args:
            provider_id: The entity's provider internal ID (Instagram ID).
            limit: Number of items to return (1-100).
            cursor: Pagination cursor.

        Returns:
            A dictionary containing the list of comments.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, user, comments, list, content, api
        """
        url = f"{self.base_url}/api/v1/users/{provider_id}/comments"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def retrieve_own_profile(self) -> dict[str, Any]:
        """
        Retrieves the profile details for the user associated with the Unipile account. This function targets the API's 'me' endpoint to fetch the authenticated user's profile, distinct from `retrieve_user_profile` which fetches profiles of other users by their public identifier.

        Returns:
            A dictionary containing the user's profile details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, user, profile, me, retrieve, get, api
        """
        url = f"{self.base_url}/api/v1/users/me"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def retrieve_post(self, post_id: str) -> dict[str, Any]:
        """
        Fetches a specific post's details by its unique ID. Unlike `list_profile_posts`, which retrieves a collection of posts from a user or company profile, this function targets one specific post and returns its full object.

        Args:
            post_id: The ID of the post to retrieve.

        Returns:
            A dictionary containing the post details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, post, retrieve, get, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/{post_id}"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def list_post_comments(
        self, post_id: str, comment_id: str | None = None, cursor: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        Fetches comments for a specific post. Providing an optional `comment_id` retrieves threaded replies instead of top-level comments. `retrieve_post` or `list_profile_posts` can be used to obtain the `post_id` which is the social_id in their response.

        Args:
            post_id: The social ID of the post which you get from using `retrieve_post` or `list_profile_posts` tools.
            comment_id: If provided, retrieves replies to this comment ID instead of top-level comments.
            cursor: Pagination cursor.
            limit: Number of comments to return.

        Returns:
            A dictionary containing a list of comment objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, post, comment, list, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/{post_id}/comments"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = str(limit)
        if comment_id:
            params["comment_id"] = comment_id
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def create_post(
        self, text: str, mentions: list[dict[str, Any]] | None = None, external_link: str | None = None
    ) -> dict[str, Any]:
        """
        Publishes a new top-level post from the account, including text, user mentions, and an external link. This function creates original content, distinguishing it from `create_post_comment` which adds replies to existing posts.

        Args:
            text: The main text content of the post.
            mentions: Optional list of dictionaries, each representing a mention.
            external_link: Optional string, an external URL that should be displayed.

        Returns:
            A dictionary containing the ID of the created post.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, post, create, share, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts"
        params: dict[str, str] = {"account_id": await self._get_account_id(), "text": text}
        if mentions:
            params["mentions"] = mentions
        if external_link:
            params["external_link"] = external_link
        response = await self._apost(url, data=params)
        return self._handle_response(response)

    async def list_content_reactions(
        self, post_id: str, comment_id: str | None = None, cursor: str | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of reactions for a given post or, optionally, a specific comment. This read-only operation uses the account for the request, distinguishing it from the `create_reaction` function which adds new reactions.

        Args:
            post_id: The social ID of the post.
            comment_id: If provided, retrieves reactions for this comment ID.
            cursor: Pagination cursor.
            limit: Number of reactions to return (1-100).

        Returns:
            A dictionary containing a list of reaction objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, post, reaction, list, like, content, api
        """
        url = f"{self.base_url}/api/v1/posts/{post_id}/reactions"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        if comment_id:
            params["comment_id"] = comment_id
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def create_post_comment(
        self, post_social_id: str, text: str, comment_id: str | None = None, mentions_body: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Publishes a comment on a specified post. By providing an optional `comment_id`, it creates a threaded reply to an existing comment instead of a new top-level one. This function's dual capability distinguishes it from `list_post_comments`, which only retrieves comments and their replies.

        Args:
            post_social_id: The social ID of the post to comment on.
            text: The text content of the comment.
            comment_id: Optional ID of a specific comment to reply to instead of commenting on the post.
            mentions_body: Optional list of mention objects for the request body if needed.

        Returns:
            A dictionary, likely confirming comment creation.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, post, comment, create, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/{post_social_id}/comments"
        params: dict[str, Any] = {"account_id": await self._get_account_id(), "text": text}
        if comment_id:
            params["comment_id"] = comment_id
        if mentions_body:
            params = {"mentions": mentions_body}
        response = await self._apost(url, data=params)
        return self._handle_response(response)

    async def create_reaction(
        self,
        post_social_id: str,
        reaction_type: Literal["like", "celebrate", "love", "insightful", "funny", "support"],
        comment_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Adds a specified reaction (e.g., 'like', 'love') to an Instagram post or, optionally, to a specific comment. This function performs a POST request to create the reaction, differentiating it from `list_content_reactions` which only retrieves existing ones.

        Args:
            post_social_id: The social ID of the post or comment to react to.
            reaction_type: The type of reaction.
            comment_id: Optional ID of a specific comment to react to instead of the post.

        Returns:
            A dictionary, likely confirming the reaction.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, post, reaction, create, like, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/reaction"
        params: dict[str, str] = {"account_id": await self._get_account_id(), "post_id": post_social_id, "reaction_type": reaction_type}
        if comment_id:
            params["comment_id"] = comment_id
        response = await self._apost(url, data=params)
        return self._handle_response(response)

    async def retrieve_user_profile(self, public_identifier: str) -> dict[str, Any]:
        """
        Retrieves a specific Instagram user's profile using their public or internal ID. Unlike `retrieve_own_profile`, which fetches the authenticated user's details, this function targets and returns data for any specified third-party user profile on the platform.

        Args:
            public_identifier: The user's public identifier or username.

        Returns:
            A dictionary containing the user's profile details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            instagram, user, profile, retrieve, get, api, important
        """
        url = f"{self.base_url}/api/v1/users/{public_identifier}"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    def list_tools(self) -> list[Callable]:
        return [
            self.start_new_chat,
            self.list_all_chats,
            self.list_chat_messages,
            self.send_chat_message,
            self.retrieve_chat,
            self.list_all_messages,
            self.list_profile_posts,
            self.list_profile_comments,
            self.retrieve_own_profile,
            self.retrieve_user_profile,
            self.retrieve_post,
            self.list_post_comments,
            self.create_post,
            self.list_content_reactions,
            self.create_post_comment,
            self.create_reaction,
        ]
