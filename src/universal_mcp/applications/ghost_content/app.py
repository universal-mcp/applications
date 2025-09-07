from collections.abc import Callable
from typing import Any

from loguru import logger

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class GhostContentApp(APIApplication):
    """
    Application for interacting with the Ghost Content API.
    Handles operations related to posts, pages, tags, authors, tiers, newsletters,
    offers, products, collections, and general site information.
    """

    def __init__(self, integration: Integration) -> None:
        """
        Initialize the GhostContentApp.

        Args:
            integration: The integration configuration containing the Ghost site URL
                         and Content API key.
                         It is expected that the integration provides 'url' (e.g.,
                         "https://your-ghost-site.com") and 'key' (the Content API key)
                         via `integration.get_credentials()`.
        """
        super().__init__(name="ghost_content", integration=integration)
        self._base_url = None
        self._api_key = None  # Cache the API key
        self._version = None  # Cache the version

    @property
    def base_url(self) -> str:
        """
        Get the base URL for the Ghost Content API.
        This is constructed from the integration's credentials.
        """
        if not self._base_url:
            credentials = self.integration.get_credentials()
            ghost_url = credentials.get("url") or credentials.get("admin_domain")
            if not ghost_url:
                logger.error(
                    "GhostContentApp: Missing 'url' or 'admin_domain' in integration credentials."
                )
                raise ValueError(
                    "Integration credentials must include 'url' or 'admin_domain' for the Ghost site."
                )

            self._base_url = f"{ghost_url.rstrip('/')}/api/content/"
            logger.info(f"GhostContentApp: Constructed base URL as {self._base_url}")
        return self._base_url

    @base_url.setter
    def base_url(self, base_url: str) -> None:
        """
        Set the base URL for the Ghost Content API.
        This is useful for testing or if the base URL changes.

        Args:
            base_url: The new base URL to set.
        """
        self._base_url = base_url
        logger.info(f"GhostContentApp: Base URL set to {self._base_url}")

    @property
    def _get_api_key(self) -> str:
        """
        Retrieves the Ghost Content API key from integration credentials.
        Caches the key after the first retrieval.
        """
        if not self._api_key:
            credentials = self.integration.get_credentials()
            api_key = (
                credentials.get("key")
                or credentials.get("api_key")
                or credentials.get("API_KEY")
            )
            if not api_key:
                logger.error(
                    "GhostContentApp: Content API key ('key') not found in integration credentials."
                )
                raise ValueError(
                    "Integration credentials must include the Ghost Content API 'key'."
                )
            self._api_key = api_key
        return self._api_key

    @property
    def _get_version(self) -> str:
        """
        Retrieves the Ghost Content API version from integration credentials.
        Caches the version after the first retrieval.
        """
        if not self._version:
            credentials = self.integration.get_credentials()
            version = credentials.get("api_version")
            if not version:
                logger.warning(
                    "GhostContentApp: 'version' not found in integration credentials. Defaulting to 'v5.0'."
                )
                version = "v5.0"  # Default to a common version if not specified
            self._version = version
        return self._version

    def _get_headers(self) -> dict[str, str]:
        """
        Get the headers for Ghost Content API requests.
        Overrides the base class method to include the `Accept-Version` header.
        """
        headers = super()._get_headers()  # Get base headers (e.g., Content-Type)

        # Add the Accept-Version header as per Ghost Content API documentation
        headers["Accept-Version"] = self._get_version
        logger.debug(
            f"GhostContentApp: Using Accept-Version: {self._get_version} in headers."
        )
        return headers

    def _build_common_params(
        self,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,  # Changed from filter_str to filter
        limit: int | None = None,
        order: str | None = None,
        page: int | None = None,
        formats: list[str] | None = None,  # Specific to posts/pages for content format
        visibility: str | None = None,  # Specific to posts/pages/tiers for visibility
    ) -> dict[str, Any]:
        """
        Helper to build common query parameters for Ghost Content API requests,
        including the mandatory API key.
        """
        params: dict[str, Any] = {"key": self._get_api_key}

        if include:
            params["include"] = ",".join(include)
        if fields:
            params["fields"] = ",".join(fields)
        if filter:  # Use 'filter' here
            params["filter"] = filter
        if limit is not None:
            params["limit"] = limit
        if order:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if formats:
            params["formats"] = ",".join(formats)
        if visibility:
            params["visibility"] = visibility
        return params

    # --- Posts Tools ---
    def browse_posts(
        self,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        order: str | None = None,
        formats: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type to Dict[str, Any]
        """
        Retrieves and browses posts from a data source based on provided parameters.

        Args:
            include: A list of fields to include in the response.
            fields: A list of specific fields to retrieve.
            filter: A string to filter the posts by.
            limit: The maximum number of posts to return.
            page: The page number to start retrieving posts from.
            order: The order in which to retrieve posts.
            formats: A list of formats in which to retrieve posts.

        Returns:
            The result of the posts retrieval, which may be in various formats depending on the request parameters.

        Raises:
            httpx.HTTPError: An exception might be raised if there is an issue with the request execution, such as network errors or invalid parameters.

        Tags:
            browse, fetch, posts, management, important
        """
        url = f"{self.base_url}posts/"
        # Removed 'visibility' from params as it's not in the method signature
        params = self._build_common_params(
            include=include,
            fields=fields,
            filter=filter,
            limit=limit,
            page=page,
            order=order,
            formats=formats,
        )
        response = self._get(url, params=params)
        return response.json()

    def read_post_by_id(
        self,
        id: str,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        formats: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Retrieves a post by its ID, optionally including additional data or specific fields.

        Args:
            id: The unique identifier of the post to retrieve.
            include: Optional list of additional data to include in the response.
            fields: Optional list of specific fields to retrieve for the post.
            formats: Optional list of formats for the post data.

        Returns:
            The retrieved post data in the specified format.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            read, post, management
        """
        url = f"{self.base_url}posts/{id}/"
        params = self._build_common_params(
            include=include, fields=fields, formats=formats
        )
        response = self._get(url, params=params)
        return response.json()

    def read_post_by_slug(
        self,
        slug: str,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        formats: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Retrieves a post by its slug, with optional parameters to specify included data, select specific fields, or request particular data formats.

        Args:
            slug: Unique slug identifier of the post to retrieve.
            include: Optional list of related objects to include with the post.
            fields: Optional list of fields to include in the returned post data.
            formats: Optional list of data formats in which to return the post.

        Returns:
            The retrieved post data or response payload, as returned by the underlying GET request executor.

        Raises:
            httpx.HTTPError: May be raised if the underlying GET request fails, e.g., due to network issues, invalid parameters, or unauthorized access.

        Tags:
            read, post, fetch, management
        """
        url = f"{self.base_url}posts/slug/{slug}/"
        params = self._build_common_params(
            include=include, fields=fields, formats=formats
        )
        response = self._get(url, params=params)
        return response.json()

    # --- Authors Tools ---
    def browse_authors(
        self,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Browse authors using various filtering and pagination options.

        Args:
            include: Optional list of fields to include in the response.
            fields: Optional list of specific fields to retrieve.
            filter: Optional string filter to apply to the results.
            limit: Optional integer specifying the maximum number of results to return.
            page: Optional integer indicating the page number.
            order: Optional string defining the order of results.

        Returns:
            Any data returned from the GET request to the authors endpoint.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            list, management, important
        """
        url = f"{self.base_url}authors/"
        params = self._build_common_params(
            include=include,
            fields=fields,
            filter=filter,
            limit=limit,
            page=page,
            order=order,
        )
        response = self._get(url, params=params)
        return response.json()

    def read_author_by_id(
        self,
        id: str,
        include: list[str] | None = None,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Read an author from the database by their unique ID.

        Args:
            id: The unique identifier of the author.
            include: Optional list of related resources to include in the response.
            fields: Optional list of fields to retrieve from the author record.

        Returns:
            The author data as a JSON response or other arbitrary data type.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            read, author, data-access
        """
        url = f"{self.base_url}authors/{id}/"
        params = self._build_common_params(include=include, fields=fields)
        response = self._get(url, params=params)
        return response.json()

    def read_author_by_slug(
        self,
        slug: str,
        include: list[str] | None = None,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Retrieve an author's information by their slug.

        Args:
            slug: The unique slug of the author to retrieve.
            include: Optional list of fields to include in the response.
            fields: Optional list of fields to request in the response.

        Returns:
            The result of the GET request to retrieve the author's information.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            fetch, author, management
        """
        url = f"{self.base_url}authors/slug/{slug}/"
        params = self._build_common_params(include=include, fields=fields)
        response = self._get(url, params=params)
        return response.json()

    # --- Tags Tools ---
    def browse_tags(
        self,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Browse and retrieve tags based on specified parameters.

        Args:
            include: Optional list of tags or fields to include.
            fields: Optional list of specific fields to retrieve.
            filter: Optional filter expression to apply.
            limit: Optional limit on the number of tags to return.
            page: Optional page number for pagination.
            order: Optional ordering criteria for the returned tags.

        Returns:
            Response from the GET request to retrieve tags.

        Raises:
            httpx.HTTPError: Raised if the connection to the server fails, or request times out.

        Tags:
            browse, tags, management, important
        """
        url = f"{self.base_url}tags/"
        params = self._build_common_params(
            include=include,
            fields=fields,
            filter=filter,
            limit=limit,
            page=page,
            order=order,
        )
        response = self._get(url, params=params)
        return response.json()

    def read_tag_by_id(
        self,
        id: str,
        include: list[str] | None = None,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Retrieves a tag's details by its unique identifier, optionally filtering by included and field sets.

        Args:
            id: str: The unique identifier of the tag to retrieve.
            include: Optional[List[str]]: Additional related resources or attributes to include in the response.
            fields: Optional[List[str]]: Specific fields to return in the response.

        Returns:
            Any: The retrieved tag object, with details as specified by the included and field parameters. The exact type depends on the server response.

        Raises:
            httpx.HTTPError: Depending on the backend, may raise connection, authentication, or data retrieval exceptions.

        Tags:
            read, tag, search, fetch, api, management
        """
        url = f"{self.base_url}tags/{id}/"
        params = self._build_common_params(include=include, fields=fields)
        response = self._get(url, params=params)
        return response.json()

    def read_tag_by_slug(
        self,
        slug: str,
        include: list[str] | None = None,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Retrieve tag information identified by a unique slug, with optional inclusion of related data and selective fields.

        Args:
            slug: str: The unique slug identifier of the tag to retrieve.
            include: Optional[List[str]]: A list of related resource names to include in the response, or None to include none.
            fields: Optional[List[str]]: A list of specific fields to return for the tag, or None to return all fields.

        Returns:
            Any: The data corresponding to the requested tag, potentially including related resources and filtered fields, as returned by the GET request.

        Raises:
            httpx.HTTPError: If the underlying GET request fails due to network issues, invalid slug, or server errors.

        Tags:
            read, retrieve, get
        """
        url = f"{self.base_url}tags/slug/{slug}/"
        params = self._build_common_params(include=include, fields=fields)
        response = self._get(url, params=params)
        return response.json()

    # --- Pages Tools ---
    def browse_pages(
        self,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        order: str | None = None,
        formats: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Retrieves a list of pages using optional filtering, pagination, and formatting parameters.

        Args:
            include: Optional list of related resources or entities to include in the response.
            fields: Optional list of specific fields to include for each page in the response.
            filter: Optional string to filter the pages based on certain criteria.
            limit: Optional integer specifying the maximum number of pages to return.
            page: Optional integer specifying the page number for pagination.
            order: Optional string defining the sorting order of the returned pages.
            formats: Optional list of formats that the pages should be returned in.

        Returns:
            The result of the GET request to the 'pages/' endpoint, typically a collection of pages matching the query parameters.

        Raises:
            httpx.HTTPError: If the underlying GET request fails due to network issues, invalid parameters, or server errors.

        Tags:
            browse, list, management, important
        """
        url = f"{self.base_url}pages/"
        # Removed 'visibility' from params as it's not in the method signature
        params = self._build_common_params(
            include=include,
            fields=fields,
            filter=filter,
            limit=limit,
            page=page,
            order=order,
            formats=formats,
        )
        response = self._get(url, params=params)
        return response.json()

    def read_page_by_id(
        self,
        id: str,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        formats: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Read a page by ID, allowing for optional inclusion of additional data, specific fields, and formats.

        Args:
            id: The unique identifier of the page to be read.
            include: Optional list of related data to include in the response.
            fields: Optional list of fields to filter the response by.
            formats: Optional list of formats for the response data.

        Returns:
            The result of the GET request to read the page.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            read, page, data-retrieval
        """
        url = f"{self.base_url}pages/{id}/"
        params = self._build_common_params(
            include=include, fields=fields, formats=formats
        )
        response = self._get(url, params=params)
        return response.json()

    def read_page_by_slug(
        self,
        slug: str,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        formats: list[str] | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Retrieve a page's content and metadata by its slug identifier, optionally including related data, specific fields, and content formats.

        Args:
            slug: The unique slug string identifying the page to be retrieved.
            include: Optional list of related resource names to include in the response.
            fields: Optional list of specific fields of the page to return.
            formats: Optional list of content formats to retrieve for the page.

        Returns:
            The response from the GET request containing the page data, typically as a parsed JSON object or equivalent.

        Raises:
            httpx.HTTPError: If the underlying GET request fails due to network issues, invalid slug, or server errors.

        Tags:
            read, get, page, slug, http-request
        """
        url = f"{self.base_url}pages/slug/{slug}/"
        params = self._build_common_params(
            include=include, fields=fields, formats=formats
        )
        response = self._get(url, params=params)
        return response.json()

    # --- Tiers Tool ---
    def browse_tiers(
        self,
        include: list[str] | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:  # Changed return type
        """
        Browse tiers based on optional filters and pagination.

        Args:
            include: List of items to include in the response, if applicable.
            fields: List of fields to retrieve from the tiers.
            filter: String filter to apply to the tiers.
            limit: Maximum number of tiers to return in the response.
            page: Page number for pagination.
            order: Ordering parameter for the tiers.

        Returns:
            Response from the tiers browsing request.

        Raises:
            httpx.HTTPError: Raised on any issue during the execution of the GET request.

        Tags:
            browse, pagination, filter, management, important
        """
        url = f"{self.base_url}tiers/"
        # Removed 'visibility' from params as it's not in the method signature
        params = self._build_common_params(
            include=include,
            fields=fields,
            filter=filter,
            limit=limit,
            page=page,
            order=order,
        )
        response = self._get(url, params=params)
        return response.json()

    # --- Settings Tool ---
    def browse_settings(self) -> dict[str, Any]:  # Changed return type
        """
        Fetches site settings by making a GET request to the settings endpoint.

        Args:
            None: This function does not accept any parameters.

        Returns:
            The result of the GET request to retrieve site settings.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            fetch, settings, management, important
        """
        url = f"{self.base_url}settings/"
        params = (
            self._build_common_params()
        )  # Only the API key is needed for this endpoint via _build_common_params
        response = self._get(url, params=params)
        return response.json()

    def list_tools(self) -> list[Callable]:
        """Returns a list of methods exposed as tools for the Ghost Content API."""
        return [
            self.browse_posts,
            self.read_post_by_id,
            self.read_post_by_slug,
            self.browse_authors,
            self.read_author_by_id,
            self.read_author_by_slug,
            self.browse_tags,
            self.read_tag_by_id,
            self.read_tag_by_slug,
            self.browse_pages,
            self.read_page_by_id,
            self.read_page_by_slug,
            self.browse_tiers,
            self.browse_settings,
        ]
