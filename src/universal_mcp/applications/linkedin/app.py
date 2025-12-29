import os
from collections.abc import Callable
from typing import Any, Literal
import requests

from loguru import logger
from universal_mcp.applications.application import APIApplication, BaseApplication
from universal_mcp.integrations import Integration


class LinkedinApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """

    def __init__(self, integration: Integration) -> None:
        """
        Initialize the LinkedinApp.

        Args:
            integration: The integration configuration containing credentials and other settings.
                         It is expected that the integration provides the 'x-api-key'
                         via headers in `integration.get_credentials_async()`, e.g.,
                         `{"headers": {"x-api-key": "YOUR_API_KEY"}}`.
        """
        super().__init__(name="linkedin", integration=integration)
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

    async def _aget_search_parameter_id(self, param_type: str, keywords: str) -> str:
        """
        Retrieves the ID for a given LinkedIn search parameter by its name asynchronously.

        Args:
            param_type: The type of parameter to search for (e.g., "LOCATION", "COMPANY").
            keywords: The name of the parameter to find (e.g., "United States").

        Returns:
            The corresponding ID for the search parameter.

        Raises:
            ValueError: If no exact match for the keywords is found.
            httpx.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/api/v1/linkedin/search/parameters"
        params = {"account_id": await self._get_account_id(), "keywords": keywords, "type": param_type}
        response = await self._aget(url, params=params)
        results = self._handle_response(response)
        items = results.get("items", [])
        if items:
            return items[0]["id"]
        raise ValueError(f'Could not find a matching ID for {param_type}: "{keywords}"')

    async def start_new_chat(self, provider_id: str, text: str) -> dict[str, Any]:
        """
        Starts a new chat conversation with a specified user by sending an initial message.
        This function constructs a multipart/form-data request using the `files` parameter
        to ensure correct formatting and headers, working around potential issues in the
        underlying request method.

        Args:
            provider_id: The LinkedIn provider ID of the user to start the chat with.
                        This is available in the response of the `retrieve_user_profile` tool.
            text: The initial message content. For LinkedIn Recruiter accounts, this can include
                HTML tags like <strong>, <em>, <a>, <ul>, <ol>, and <li>.

        Returns:
            A dictionary containing the details of the newly created chat.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, chat, create, start, new, messaging, api, important
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
            account_type: Filter by provider (e.g., "linkedin").

        Returns:
            A dictionary containing a list of chat objects and a pagination cursor.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, chat, list, messaging, api
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
            linkedin, chat, message, send, create, messaging, api
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
            linkedin, chat, retrieve, get, messaging, api
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
        if await self._get_account_id():
            params["account_id"] = await self._get_account_id()
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def list_profile_posts(
        self, identifier: str, cursor: str | None = None, limit: int | None = None, is_company: bool | None = None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of posts from a specific user or company profile using their provider ID. An authorizing `account_id` is required, and the `is_company` flag must specify the entity type, distinguishing this from `retrieve_post` which fetches a single post by its own ID.

        Args:
            identifier: The entity's provider internal ID (LinkedIn ID).
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
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        if is_company is not None:
            params["is_company"] = is_company
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
            linkedin, user, profile, me, retrieve, get, api
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
            linkedin, post, retrieve, get, content, api, important
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
            limit: Number of comments to return. (OpenAPI spec shows type string, passed as string if provided).

        Returns:
            A dictionary containing a list of comment objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, comment, list, content, api, important
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
            limit: Number of reactions to return (1-100, spec max 250).

        Returns:
            A dictionary containing a list of reaction objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, reaction, list, like, content, api
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
        Adds a specified reaction (e.g., 'like', 'love') to a LinkedIn post or, optionally, to a specific comment. This function performs a POST request to create the reaction, differentiating it from `list_content_reactions` which only retrieves existing ones.

        Args:
            post_social_id: The social ID of the post or comment to react to.
            reaction_type: The type of reaction. Valid values are "like", "celebrate", "love", "insightful", "funny", or "support".
            comment_id: Optional ID of a specific comment to react to instead of the post.

        Returns:
            A dictionary, likely confirming the reaction. (Structure depends on actual API response)

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, reaction, create, like, content, api, important
        """
        url = f"{self.base_url}/api/v1/posts/reaction"
        params: dict[str, str] = {"account_id": await self._get_account_id(), "post_id": post_social_id, "reaction_type": reaction_type}
        if comment_id:
            params["comment_id"] = comment_id
        response = await self._apost(url, data=params)
        return self._handle_response(response)

    async def retrieve_user_profile(self, public_identifier: str) -> dict[str, Any]:
        """
        Retrieves a specific LinkedIn user's profile using their public or internal ID. Unlike `retrieve_own_profile`, which fetches the authenticated user's details, this function targets and returns data for any specified third-party user profile on the platform.

        Args:
            public_identifier: Extract this value from the response of `search_people` tool. The response contains a public_identifier field.For example, for https://www.linkedin.com/in/manojbajaj95/, the identifier is "manojbajaj95".

        Returns:
            A dictionary containing the user's profile details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, profile, retrieve, get, api, important
        """
        url = f"{self.base_url}/api/v1/users/{public_identifier}"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def search_people(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        location: str | None = None,
        industry: str | None = None,
        company: str | None = None,
    ) -> dict[str, Any]:
        """
        Searches for LinkedIn user profiles using keywords, with optional filters for location, industry, and company. This function specifically targets the 'people' category, distinguishing it from other search methods like `search_companies` or `search_jobs` that query different entity types through the same API endpoint.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            location: The geographical location to filter people by (e.g., "United States").
            industry: The industry to filter people by.(eg., "Information Technology and Services").
            company: The company to filter people by.(e.g., "Google").

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/api/v1/linkedin/search"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        payload: dict[str, Any] = {"api": "classic", "category": "people"}
        if keywords:
            payload["keywords"] = keywords
        if location:
            location_id = await self._aget_search_parameter_id("LOCATION", location)
            payload["location"] = [location_id]
        if industry:
            industry_id = await self._aget_search_parameter_id("INDUSTRY", industry)
            payload["industry"] = [industry_id]
        if company:
            company_id = await self._aget_search_parameter_id("COMPANY", company)
            payload["company"] = [company_id]
        response = await self._apost(url, params=params, data=payload)
        return self._handle_response(response)

    async def search_companies(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        location: str | None = None,
        industry: str | None = None,
    ) -> dict[str, Any]:
        """
        Performs a paginated search for companies on LinkedIn using keywords, with optional location and industry filters. Its specific 'companies' search category distinguishes it from other methods like `search_people` or `search_posts`, ensuring that only company profiles are returned.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            location: The geographical location to filter companies by (e.g., "United States").
            industry: The industry to filter companies by.(e.g., "Information Technology and Services").

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/api/v1/linkedin/search"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        payload: dict[str, Any] = {"api": "classic", "category": "companies"}
        if keywords:
            payload["keywords"] = keywords
        if location:
            location_id = await self._aget_search_parameter_id("LOCATION", location)
            payload["location"] = [location_id]
        if industry:
            industry_id = await self._aget_search_parameter_id("INDUSTRY", industry)
            payload["industry"] = [industry_id]
        response = await self._apost(url, params=params, data=payload)
        return self._handle_response(response)

    async def search_posts(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        date_posted: Literal["past_day", "past_week", "past_month"] | None = None,
        sort_by: Literal["relevance", "date"] = "relevance",
    ) -> dict[str, Any]:
        """
        Performs a keyword-based search for LinkedIn posts, allowing filters for date and sorting by relevance. This function executes a general, platform-wide content search, distinguishing it from other search functions that target people, companies, or jobs, and from `list_profile_posts` which retrieves from a specific profile.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            date_posted: Filter by when the post was posted.
            sort_by: How to sort the results.

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/api/v1/linkedin/search"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        payload: dict[str, Any] = {"api": "classic", "category": "posts"}
        if keywords:
            payload["keywords"] = keywords
        if date_posted:
            payload["date_posted"] = date_posted
        if sort_by:
            payload["sort_by"] = sort_by
        response = await self._apost(url, params=params, data=payload)
        return self._handle_response(response)

    async def search_jobs(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        region: str | None = None,
        sort_by: Literal["relevance", "date"] = "relevance",
        minimum_salary_value: Literal[40, 60, 80, 100, 120, 140, 160, 180, 200] = 40,
        industry: str | None = None,
    ) -> dict[str, Any]:
        """
        Performs a LinkedIn search for jobs, filtering results by keywords, region, industry, and minimum salary. Unlike other search functions (`search_people`, `search_companies`), this method is specifically configured to query the 'jobs' category, providing a paginated list of relevant employment opportunities.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            region: The geographical region to filter jobs by (e.g., "United States").
            sort_by: How to sort the results.(e.g., "relevance" or "date".)
            minimum_salary_value: The minimum salary to filter for. Allowed values are 40, 60, 80, 100, 120, 140, 160, 180, 200.
            industry: The industry to filter jobs by.(e.g., "Software Development").

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.
            ValueError: If the specified location is not found.
        """
        url = f"{self.base_url}/api/v1/linkedin/search"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        payload: dict[str, Any] = {
            "api": "classic",
            "category": "jobs",
            "minimum_salary": {"currency": "USD", "value": minimum_salary_value},
        }
        if keywords:
            payload["keywords"] = keywords
        if sort_by:
            payload["sort_by"] = sort_by
        if region:
            location_id = await self._aget_search_parameter_id("LOCATION", region)
            payload["region"] = location_id
        if industry:
            industry_id = await self._aget_search_parameter_id("INDUSTRY", industry)
            payload["industry"] = [industry_id]
        response = await self._apost(url, params=params, data=payload)
        return self._handle_response(response)

    async def send_invitation(self, provider_id: str, user_email: str | None = None, message: str | None = None) -> dict[str, Any]:
        """
        Sends a connection invitation to a LinkedIn user specified by their provider ID. An optional message and the user's email can be included.

        Args:
            provider_id: The LinkedIn provider ID of the user to invite. This is available in response of `retrieve_user_profile` tool.
            user_email: Optional. The email address of the user, which may be required by LinkedIn.
            message: Optional. A personalized message to include with the invitation (max 300 characters).

        Returns:
            A dictionary confirming the invitation was sent.

        Raises:
            httpx.HTTPError: If the API request fails.
            ValueError: If the message exceeds 300 characters.

        Tags:
            linkedin, user, invite, connect, contact, api, important
        """
        url = f"{self.base_url}/api/v1/users/invite"
        payload: dict[str, Any] = {"account_id": await self._get_account_id(), "provider_id": provider_id}
        if user_email:
            payload["user_email"] = user_email
        if message:
            if len(message) > 300:
                raise ValueError("Message cannot exceed 300 characters.")
            payload["message"] = message
        response = await self._apost(url, data=payload)
        return self._handle_response(response)

    async def list_sent_invitations(self, cursor: str | None = None, limit: int | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of all sent connection invitations that are currently pending. This function allows for iterating through the history of outstanding connection requests made from the specified account.

        Args:
            cursor: A pagination cursor for retrieving the next page of entries.
            limit: The number of items to return, ranging from 1 to 100. Defaults to 10 if not specified.

        Returns:
            A dictionary containing a list of sent invitation objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, invite, sent, list, contacts, api
        """
        url = f"{self.base_url}/api/v1/users/invite/sent"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def list_received_invitations(self, cursor: str | None = None, limit: int | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of all received connection invitations. This function allows for reviewing and processing incoming connection requests to the specified account.

        Args:
            cursor: A pagination cursor for retrieving the next page of entries.
            limit: The number of items to return, ranging from 1 to 100. Defaults to 10 if not specified.

        Returns:
            A dictionary containing a list of received invitation objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, invite, received, list, contacts, api
        """
        url = f"{self.base_url}/api/v1/users/invite/received"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def handle_received_invitation(
        self, invitation_id: str, action: Literal["accept", "decline"], shared_secret: str
    ) -> dict[str, Any]:
        """
        Accepts or declines a received LinkedIn connection invitation using its ID and a required shared secret. This function performs a POST request to update the invitation's status, distinguishing it from read-only functions like `list_received_invitations`.

        Args:
            invitation_id: The ID of the invitation to handle.Get this ID from the 'list_received_invitations' tool.
            action: The action to perform, either "accept" or "decline".
            shared_secret: The token provided by LinkedIn, retrieved from the 'list_received_invitations' tool, which is mandatory for this action.

        Returns:
            A dictionary confirming the action was processed.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, invite, received, handle, accept, decline, api
        """
        url = f"{self.base_url}/api/v1/users/invite/received/{invitation_id}"
        payload: dict[str, Any] = {"provider": "LINKEDIN", "action": action, "shared_secret": shared_secret, "account_id": await self._get_account_id()}
        response = await self._apost(url, data=payload)
        return self._handle_response(response)

    async def cancel_sent_invitation(self, invitation_id: str) -> dict[str, Any]:
        """
        Cancels a sent LinkedIn connection invitation that is currently pending. This function performs a DELETE request to remove the invitation, withdrawing the connection request.

        Args:
            invitation_id: The unique ID of the invitation to cancel. This ID can be obtained from the 'list_sent_invitations' tool.

        Returns:
            A dictionary confirming the invitation was cancelled.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, invite, sent, cancel, delete, api
        """
        url = f"{self.base_url}/api/v1/users/invite/sent/{invitation_id}"
        params = {"account_id": await self._get_account_id()}
        response = await self._adelete(url, params=params)
        return self._handle_response(response)

    async def list_followers(self, cursor: str | None = None, limit: int | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of all followers for the current user's account. This function is distinct from `list_following` as it shows who follows the user, not who the user follows.

        Args:
            cursor: A pagination cursor for retrieving the next page of entries.
            limit: The number of items to return, ranging from 1 to 1000.

        Returns:
            A dictionary containing a list of follower objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, followers, list, contacts, api
        """
        url = f"{self.base_url}/api/v1/users/followers"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def list_following(self, cursor: str | None = None, limit: int | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of all accounts that the current user is following. This function is the counterpart to `list_followers`, focusing on the user's outgoing connections rather than incoming ones.

        Args:
            cursor: A pagination cursor for retrieving the next page of entries.
            limit: The number of items to return, ranging from 1 to 1000.

        Returns:
            A dictionary containing a list of followed account objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, following, list, contacts, api
        """
        url = f"{self.base_url}/api/v1/users/following"
        params: dict[str, Any] = {"account_id": await self._get_account_id()}
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        response = self._get(url, params=params)
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
            self.retrieve_own_profile,
            self.retrieve_user_profile,
            self.retrieve_post,
            self.list_post_comments,
            self.create_post,
            self.list_content_reactions,
            self.create_post_comment,
            self.create_reaction,
            self.search_companies,
            self.search_jobs,
            self.search_people,
            self.search_posts,
            self.send_invitation,
            self.list_sent_invitations,
            self.cancel_sent_invitation,
            self.list_received_invitations,
            self.handle_received_invitation,
            self.list_followers,
            # self.list_following       this endpoint is not yet implemented by unipile
        ]
