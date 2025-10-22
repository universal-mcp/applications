import json
from collections.abc import Callable
from typing import Any, Literal

from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class UnipileApp(APIApplication):
    """
    Application for interacting with the LinkedIn API via Unipile.
    Handles operations related to chats, messages, accounts, posts, and user profiles.
    """

    def __init__(self, integration: Integration) -> None:
        """
        Initialize the LinkedinApp.

        Args:
            integration: The integration configuration containing credentials and other settings.
                         It is expected that the integration provides the 'x-api-key'
                         via headers in `integration.get_credentials()`, e.g.,
                         `{"headers": {"x-api-key": "YOUR_API_KEY"}}`.
        """
        super().__init__(name="unipile", integration=integration)

        self._base_url = None

    @property
    def base_url(self) -> str:
        """
        A property that lazily constructs and caches the Unipile API base URL from 'subdomain' and 'port' credentials. Built on first access and used by all API methods, it raises a ValueError if credentials are missing. This is the default construction, unlike the setter which allows manual override.
        """
        if not self._base_url:
            credentials = self.integration.get_credentials()
            subdomain = credentials.get("subdomain")
            port = credentials.get("port")
            if not subdomain or not port:
                logger.error(
                    "UnipileApp: Missing 'subdomain' or 'port' in integration credentials."
                )
                raise ValueError(
                    "Integration credentials must include 'subdomain' and 'port'."
                )
            self._base_url = f"https://{subdomain}.unipile.com:{port}"
        return self._base_url

    @base_url.setter
    def base_url(self, base_url: str) -> None:
        """
        Sets or overrides the Unipile API's base URL. This setter allows manually changing the endpoint, bypassing the default URL that is dynamically constructed from integration credentials. It is primarily intended for testing against different environments or for custom deployments.

        Args:
            base_url: The new base URL to set.
        """
        self._base_url = base_url
        logger.info(f"UnipileApp: Base URL set to {self._base_url}")

    def _get_headers(self) -> dict[str, str]:
        """
        Get the headers for Unipile API requests.
        Overrides the base class method to use X-Api-Key.
        """
        if not self.integration:
            logger.warning(
                "UnipileApp: No integration configured, returning empty headers."
            )
            return {}

        credentials = self.integration.get_credentials()

        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )

        if not api_key:
            logger.error(
                "UnipileApp: API key not found in integration credentials for Unipile."
            )
            return {  # Or return minimal headers if some calls might not need auth (unlikely for Unipile)
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
            }

        logger.debug("UnipileApp: Using X-Api-Key for authentication.")
        return {
            "x-api-key": api_key,
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",  # Often good practice for APIs
        }

    def list_all_chats(
        self,
        unread: bool | None = None,
        cursor: str | None = None,
        before: str | None = None,  # ISO 8601 UTC datetime
        after: str | None = None,  # ISO 8601 UTC datetime
        limit: int | None = None,  # 1-250
        account_type: str | None = None,
        account_id: str | None = None,  # Comma-separated list of ids
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of all chat conversations across linked accounts. Supports filtering by unread status, date range, account provider, and specific account IDs, distinguishing it from functions listing messages within a single chat.

        Args:
            unread: Filter for unread chats only or read chats only.
            cursor: Pagination cursor for the next page of entries.
            before: Filter for items created before this ISO 8601 UTC datetime (exclusive).
            after: Filter for items created after this ISO 8601 UTC datetime (exclusive).
            limit: Number of items to return (1-250).
            account_type: Filter by provider (e.g., "linkedin").
            account_id: Filter by specific account IDs (comma-separated).

        Returns:
            A dictionary containing a list of chat objects and a pagination cursor.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, chat, list, messaging, api
        """
        url = f"{self.base_url}/api/v1/chats"
        params: dict[str, Any] = {}
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
        if account_id:
            params["account_id"] = account_id

        response = self._get(url, params=params)
        return response.json()

    def list_chat_messages(
        self,
        chat_id: str,
        cursor: str | None = None,
        before: str | None = None,  # ISO 8601 UTC datetime
        after: str | None = None,  # ISO 8601 UTC datetime
        limit: int | None = None,  # 1-250
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
            linkedin, chat, message, list, messaging, api
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

        response = self._get(url, params=params)
        return response.json()

    def send_chat_message(
        self,
        chat_id: str,
        text: str,
    ) -> dict[str, Any]:
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
            linkedin, chat, message, send, create, messaging, api
        """
        url = f"{self.base_url}/api/v1/chats/{chat_id}/messages"
        payload: dict[str, Any] = {"text": text}

        response = self._post(url, data=payload)
        return response.json()

    def retrieve_chat(
        self, chat_id: str, account_id: str | None = None
    ) -> dict[str, Any]:
        """
        Retrieves a single chat's details using its Unipile or provider-specific ID. Requires an `account_id` when using a provider ID for context. This function is distinct from `list_all_chats`, which returns a collection, by targeting one specific conversation.

        Args:
            chat_id: The Unipile or provider ID of the chat.
            account_id: Mandatory if the chat_id is a provider ID. Specifies the account context.

        Returns:
            A dictionary containing the chat object details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, chat, retrieve, get, messaging, api
        """
        url = f"{self.base_url}/api/v1/chats/{chat_id}"
        params: dict[str, Any] = {}
        if account_id:
            params["account_id"] = account_id

        response = self._get(url, params=params)
        return response.json()

    def list_all_messages(
        self,
        cursor: str | None = None,
        before: str | None = None,  # ISO 8601 UTC datetime
        after: str | None = None,  # ISO 8601 UTC datetime
        limit: int | None = None,  # 1-250
        sender_id: str | None = None,
        account_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of messages from all chats associated with the account(s). Unlike `list_chat_messages` which targets a specific conversation, this function provides a global message view, filterable by sender, account, and date range.

        Args:
            cursor: Pagination cursor.
            before: Filter for items created before this ISO 8601 UTC datetime.
            after: Filter for items created after this ISO 8601 UTC datetime.
            limit: Number of items to return (1-250).
            sender_id: Filter messages from a specific sender.
            account_id: Filter messages from a specific linked account.

        Returns:
            A dictionary containing a list of message objects and a pagination cursor.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, message, list, all_messages, messaging, api
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
        if account_id:
            params["account_id"] = account_id

        response = self._get(url, params=params)
        return response.json()

    def list_all_accounts(
        self,
        cursor: str | None = None,
        limit: int | None = None,  # 1-259 according to spec
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of all social media accounts linked to the Unipile service. This is crucial for obtaining the `account_id` required by other methods to specify which user account should perform an action, like sending a message or retrieving user-specific posts.

        Args:
            cursor: Pagination cursor.
            limit: Number of items to return (1-259).

        Returns:
            A dictionary containing a list of account objects and a pagination cursor.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, account, list, unipile, api, important
        """
        url = f"{self.base_url}/api/v1/accounts"
        params: dict[str, Any] = {}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit

        response = self._get(url, params=params)
        return response.json()

    def retrieve_linked_account(
        self,
        account_id: str,
    ) -> dict[str, Any]:
        """
        Retrieves details for a specific account linked to Unipile using its ID. It fetches metadata about the connection itself (e.g., a linked LinkedIn account), differentiating it from `retrieve_user_profile` which fetches a user's profile from the external platform.

        Args:
            account_id: The ID of the account to retrieve.

        Returns:
            A dictionary containing the account object details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, account, retrieve, get, unipile, api, important
        """
        url = f"{self.base_url}/api/v1/accounts/{account_id}"
        response = self._get(url)
        return response.json()

    def list_profile_posts(
        self,
        identifier: str,  # User or Company provider internal ID
        account_id: str,  # Account to perform the request from (REQUIRED)
        cursor: str | None = None,
        limit: int | None = None,  # 1-100 (spec says max 250)
        is_company: bool | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of posts from a specific user or company profile using their provider ID. An authorizing `account_id` is required, and the `is_company` flag must specify the entity type, distinguishing this from `retrieve_post` which fetches a single post by its own ID.

        Args:
            identifier: The entity's provider internal ID (LinkedIn ID).
            account_id: The ID of the Unipile account to perform the request from (REQUIRED).
            cursor: Pagination cursor.
            limit: Number of items to return (1-100, as per Unipile example, though spec allows up to 250).
            is_company: Boolean indicating if the identifier is for a company.

        Returns:
            A dictionary containing a list of post objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, list, user_posts, company_posts, content, api, important
        """
        url = f"{self.base_url}/api/v1/users/{identifier}/posts"
        params: dict[str, Any] = {"account_id": account_id}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        if is_company is not None:
            params["is_company"] = is_company

        response = self._get(url, params=params)
        return response.json()

    def retrieve_own_profile(
        self,
        account_id: str,
    ) -> dict[str, Any]:
        """
        Retrieves the profile details for the user associated with the specified Unipile account ID. This function targets the API's 'me' endpoint to fetch the authenticated user's profile, distinct from `retrieve_user_profile` which fetches profiles of other users by their public identifier.

        Args:
            account_id: The ID of the Unipile account to use for retrieving the profile (REQUIRED).

        Returns:
            A dictionary containing the user's profile details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, profile, me, retrieve, get, api
        """
        url = f"{self.base_url}/api/v1/users/me"
        params: dict[str, Any] = {"account_id": account_id}
        response = self._get(url, params=params)
        return response.json()

    def retrieve_post(
        self,
        post_id: str,
        account_id: str,
    ) -> dict[str, Any]:
        """
        Fetches a specific post's details by its unique ID, requiring an `account_id` for authorization. Unlike `list_profile_posts`, which retrieves a collection of posts from a user or company profile, this function targets one specific post and returns its full object.

        Args:
            post_id: The ID of the post to retrieve.
            account_id: The ID of the Unipile account to perform the request from (REQUIRED).

        Returns:
            A dictionary containing the post details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, retrieve, get, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/{post_id}"
        params: dict[str, Any] = {"account_id": account_id}
        response = self._get(url, params=params)
        return response.json()

    def list_post_comments(
        self,
        post_id: str,
        account_id: str,
        comment_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Fetches comments for a specific post using an `account_id` for authorization. Providing an optional `comment_id` retrieves threaded replies instead of top-level comments. This read-only operation contrasts with `create_post_comment`, which publishes new comments, and `list_content_reactions`, which retrieves 'likes'.

        Args:
            post_id: The social ID of the post.
            account_id: The ID of the Unipile account to perform the request from (REQUIRED).
            comment_id: If provided, retrieves replies to this comment ID instead of top-level comments.
            cursor: Pagination cursor.
            limit: Number of comments to return. (OpenAPI spec shows type string, passed as string if provided).

        Returns:
            A dictionary containing a list of comment objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, comment, list, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/{post_id}/comments"
        params: dict[str, Any] = {"account_id": account_id}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = str(limit)
        if comment_id:
            params["comment_id"] = comment_id

        response = self._get(url, params=params)
        return response.json()

    def create_post(
        self,
        account_id: str,
        text: str,
        mentions: list[dict[str, Any]] | None = None,
        external_link: str | None = None,
    ) -> dict[str, Any]:
        """
        Publishes a new top-level post from a specified account, including text, user mentions, and an external link. This function creates original content, distinguishing it from `create_post_comment` which adds replies to existing posts.

        Args:
            account_id: The ID of the Unipile account that will author the post (added as query parameter).
            text: The main text content of the post.
            mentions: Optional list of dictionaries, each representing a mention.
                      Example: `[{"entity_urn": "urn:li:person:...", "start_index": 0, "end_index": 5}]`
            external_link: Optional string, an external URL that should be displayed within a card.

        Returns:
            A dictionary containing the ID of the created post.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, create, share, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts"

        params: dict[str, str] = {
            "account_id": account_id,
            "text": text,
        }

        if mentions:
            params["mentions"] = mentions
        if external_link:
            params["external_link"] = external_link

        response = self._post(url, data=params)
        return response.json()

    def list_content_reactions(
        self,
        post_id: str,
        account_id: str,
        comment_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of reactions for a given post or, optionally, a specific comment. This read-only operation uses the provided `account_id` for the request, distinguishing it from the `create_reaction` function which adds new reactions.

        Args:
            post_id: The social ID of the post.
            account_id: The ID of the Unipile account to perform the request from .
            comment_id: If provided, retrieves reactions for this comment ID.
            cursor: Pagination cursor.
            limit: Number of reactions to return (1-100, spec max 250).

        Returns:
            A dictionary containing a list of reaction objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, reaction, list, like, content, api
        """
        url = f"{self.base_url}/api/v1/posts/{post_id}/reactions"
        params: dict[str, Any] = {"account_id": account_id}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        if comment_id:
            params["comment_id"] = comment_id

        response = self._get(url, params=params)
        return response.json()

    def create_post_comment(
        self,
        post_social_id: str,
        account_id: str,
        text: str,
        comment_id: str | None = None,  # If provided, replies to a specific comment
        mentions_body: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Publishes a comment on a specified post. By providing an optional `comment_id`, it creates a threaded reply to an existing comment instead of a new top-level one. This function's dual capability distinguishes it from `list_post_comments`, which only retrieves comments and their replies.

        Args:
            post_social_id: The social ID of the post to comment on.
            account_id: The ID of the Unipile account performing the comment.
            text: The text content of the comment (passed as a query parameter).
                  Supports Unipile's mention syntax like "Hey {{0}}".
            comment_id: Optional ID of a specific comment to reply to instead of commenting on the post.
            mentions_body: Optional list of mention objects for the request body if needed.

        Returns:
            A dictionary, likely confirming comment creation. (Structure depends on actual API response)

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, comment, create, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/{post_social_id}/comments"
        params: dict[str, Any] = {
            "account_id": account_id,
            "text": text,
        }

        if comment_id:
            params["comment_id"] = comment_id

        if mentions_body:
            params = {"mentions": mentions_body}

        response = self._post(url, data=params)

        try:
            return response.json()
        except json.JSONDecodeError:
            return {
                "status": response.status_code,
                "message": "Comment action processed.",
            }

    def create_reaction(
        self,
        post_social_id: str,
        reaction_type: Literal[
            "like", "celebrate", "love", "insightful", "funny", "support"
        ],
        account_id: str,
        comment_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Adds a specified reaction (e.g., 'like', 'love') to a LinkedIn post or, optionally, to a specific comment. This function performs a POST request to create the reaction, differentiating it from `list_content_reactions` which only retrieves existing ones.

        Args:
            post_social_id: The social ID of the post or comment to react to.
            reaction_type: The type of reaction .
            account_id: Account ID of the Unipile account performing the reaction.
            comment_id: Optional ID of a specific comment to react to instead of the post.

        Returns:
            A dictionary, likely confirming the reaction. (Structure depends on actual API response)

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, reaction, create, like, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/reaction"

        params: dict[str, str] = {
            "account_id": account_id,
            "post_id": post_social_id,
            "reaction_type": reaction_type,
        }

        if comment_id:
            params["comment_id"] = comment_id

        response = self._post(url, data=params)

        try:
            return response.json()
        except json.JSONDecodeError:
            return {
                "status": response.status_code,
                "message": "Reaction action processed.",
            }

    def search(
        self,
        account_id: str,
        category: Literal["people", "companies", "posts", "jobs"],
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        date_posted: Literal["past_day", "past_week", "past_month"] | None = None,
        sort_by: Literal["relevance", "date"] = "relevance",
        minimum_salary_value: int = 40,
    ) -> dict[str, Any]:
        """
        Performs a comprehensive LinkedIn search for people, companies, posts, or jobs using keywords.
        Supports pagination and targets either the classic or Sales Navigator API for posts.
        For people, companies, and jobs, it uses the classic API.

        Args:
            account_id: The ID of the Unipile account to perform the search from (REQUIRED).
            category: Type of search to perform - "people", "companies", "posts", or "jobs".
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            date_posted: Filter by when the post was posted (posts only).
            sort_by: How to sort the results (for posts and jobs).
            minimum_salary_value: The minimum salary to filter for (jobs only).

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
            ValueError: If the category is empty.

        Tags:
            linkedin, search, people, companies, posts, jobs, api, important
        """
        if not category:
            raise ValueError("Category cannot be empty.")

        url = f"{self.base_url}/api/v1/linkedin/search"

        params: dict[str, Any] = {"account_id": account_id}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit

        payload: dict[str, Any] = {"api": "classic", "category": category}

        if keywords:
            payload["keywords"] = keywords

        if category == "posts":
            if date_posted:
                payload["date_posted"] = date_posted
            if sort_by:
                payload["sort_by"] = sort_by

        elif category == "jobs":
            payload["minimum_salary"] = {
                "currency": "USD",
                "value": minimum_salary_value,
            }
            if sort_by:
                payload["sort_by"] = sort_by

        response = self._post(url, params=params, data=payload)
        return self._handle_response(response)

    def retrieve_user_profile(
        self,
        identifier: str,
        account_id: str,
    ) -> dict[str, Any]:
        """
        Retrieves a specific LinkedIn user's profile using their public or internal ID, authorized via the provided `account_id`. Unlike `retrieve_own_profile`, which fetches the authenticated user's details, this function targets and returns data for any specified third-party user profile on the platform.

        Args:
            identifier: Can be the provider's internal id OR the provider's public id of the requested user.For example, for https://www.linkedin.com/in/manojbajaj95/, the identifier is "manojbajaj95".

            account_id: The ID of the Unipile account to perform the request from (REQUIRED).

        Returns:
            A dictionary containing the user's profile details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, profile, retrieve, get, api, important
        """
        url = f"{self.base_url}/api/v1/users/{identifier}"
        params: dict[str, Any] = {"account_id": account_id}
        response = self._get(url, params=params)
        return self._handle_response(response)

    def list_tools(self) -> list[Callable]:
        return [
            self.list_all_chats,
            self.list_chat_messages,
            self.send_chat_message,
            self.retrieve_chat,
            self.list_all_messages,
            self.list_all_accounts,
            self.retrieve_linked_account,
            self.list_profile_posts,
            self.retrieve_own_profile,
            self.retrieve_user_profile,
            self.retrieve_post,
            self.list_post_comments,
            self.create_post,
            self.list_content_reactions,
            self.create_post_comment,
            self.create_reaction,
            self.search,
        ]
