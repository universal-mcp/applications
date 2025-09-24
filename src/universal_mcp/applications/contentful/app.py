from collections.abc import Callable
from typing import Any

from loguru import logger
from universal_mcp.applications.application import GraphQLApplication
from universal_mcp.exceptions import NotAuthorizedError
from universal_mcp.integrations import Integration


class ContentfulApp(GraphQLApplication):
    def __init__(
        self,
        integration: Integration | None = None,
        **kwargs: Any,
    ) -> None:
        self.space_id: str | None = None
        self.environment_id: str = "master"
        self._access_token: str | None = None
        self._is_eu_customer: bool = False
        self._credentials_loaded: bool = False
        default_base_url = "https://graphql.contentful.com"

        super().__init__(
            name="contentful",
            base_url=default_base_url,
            integration=integration,
            **kwargs,
        )

    def _load_credentials_and_construct_url(self) -> bool:
        """
        Loads credentials from the integration, constructs the precise API URL,
        and prepares the instance for API calls. Runs only once.

        Returns:
            bool: True if setup was successful, False otherwise.
        """
        if self._credentials_loaded:
            return True

        logger.debug("Attempting to load Contentful credentials and construct URL...")

        if not self.integration:
            logger.error(
                "Contentful integration not configured. Cannot load credentials or construct URL."
            )
            # Mark as 'loaded' to prevent retries, even though it failed.
            self._credentials_loaded = True
            return False

        try:
            credentials = self.integration.get_credentials()
        except NotAuthorizedError as e:
            logger.error(
                f"Authorization required or credentials unavailable for Contentful: {e.message}"
            )
            self._credentials_loaded = True  # Prevent retries
            return False
        except Exception as e:
            logger.error(
                f"Failed to get credentials from integration: {e}", exc_info=True
            )
            self._credentials_loaded = True  # Prevent retries
            return False

        self.space_id = credentials.get("space_id")
        self._access_token = credentials.get("access_token") or credentials.get(
            "api_key"
        )
        self.environment_id = credentials.get(
            "environment_id", "master"
        )  # Use default if not specified
        self._is_eu_customer = credentials.get(
            "is_eu_customer", False
        )  # Use default if not specified

        missing_creds = []
        if not self.space_id:
            missing_creds.append("'space_id'")
        if not self._access_token:
            missing_creds.append("'access_token' or 'api_key'")

        if missing_creds:
            logger.error(
                f"Missing required Contentful credentials in integration: {', '.join(missing_creds)}. "
                "API calls will fail."
            )
            self._credentials_loaded = True  # Prevent retries
            return False

        contentful_api_domain = (
            "graphql.eu.contentful.com"
            if self._is_eu_customer
            else "graphql.contentful.com"
        )
        self.base_url = f"https://{contentful_api_domain}/content/v1/spaces/{self.space_id}/environments/{self.environment_id}"

        self._client = None

        logger.info(
            f"Contentful credentials loaded and URL constructed successfully. "
            f"Space: '{self.space_id}', Environment: '{self.environment_id}'. "
            f"Base URL: {self.base_url}"
        )
        self._credentials_loaded = True
        return True

    @staticmethod
    def _to_camel_case(s: str) -> str:
        """Converts a string to camelCase based on Contentful's typical ID to GraphQL name conversion."""
        s = s.replace("-", " ").replace("_", " ")
        parts = s.split()
        if not parts:
            return ""
        if len(parts) == 1 and parts[0] == s and s:
            return s[0].lower() + s[1:] if len(s) > 1 else s.lower()
        return parts[0].lower() + "".join(word.capitalize() for word in parts[1:])

    @staticmethod
    def _to_pascal_case(s: str) -> str:
        """Converts a string to PascalCase based on Contentful's typical ID to GraphQL name conversion."""
        s = s.replace("-", " ").replace("_", " ")
        parts = s.split()
        if not parts:
            return ""
        if len(parts) == 1 and parts[0] == s and s:
            return s[0].upper() + s[1:] if len(s) > 1 else s.upper()
        return "".join(word.capitalize() for word in parts)

    def _ensure_loaded(self) -> bool:
        """Internal helper to trigger lazy loading and check status."""
        if not self._credentials_loaded:
            return self._load_credentials_and_construct_url()
        # If already marked as loaded, check if essential parts are actually set (robustness check)
        return bool(self.base_url and self.space_id and self._access_token)

    # --- Tool Methods ---

    def get_entry(
        self,
        content_type_id: str,
        entry_id: str,
        fields_to_select: str,
        locale: str | None = None,
        preview: bool = False,
    ) -> dict[str, Any]:
        """
        Fetches a single entry of a specified content type by its ID.
        (See original docstring for details)
        """
        if not self._ensure_loaded():
            return {
                "error": "Failed to initialize ContentfulApp. Check credentials and configuration."
            }

        query_field = self._to_camel_case(content_type_id)
        logger.debug(
            f"Fetching entry for content_type_id='{content_type_id}' (query field='{query_field}'), entry_id='{entry_id}'"
        )
        query_gql = f"""
            query GetEntryById($id: String!, $locale: String, $preview: Boolean) {{
                {query_field}(id: $id, locale: $locale, preview: $preview) {{
                    {fields_to_select}
                }}
            }}
        """
        variables: dict[str, Any] = {"id": entry_id, "preview": preview}
        if locale:
            variables["locale"] = locale

        # Call the base class query method which uses the configured client
        try:
            return self.query(query_gql, variables=variables)
        except Exception as e:
            logger.error(f"Error executing get_entry query: {e}", exc_info=True)
            return {"error": f"Failed to get entry: {e}"}

    def get_entries_collection(
        self,
        content_type_id: str,
        fields_to_select_for_item: str,
        limit: int | None = None,
        skip: int | None = None,
        where: dict[str, Any] | None = None,
        order: list[str] | None = None,
        locale: str | None = None,
        preview: bool = False,
    ) -> dict[str, Any]:
        """
        Fetches a collection of entries of a specified content type.
        (See original docstring for details)
        """
        if not self._ensure_loaded():
            return {
                "error": "Failed to initialize ContentfulApp. Check credentials and configuration."
            }

        collection_field = self._to_camel_case(content_type_id) + "Collection"
        filter_type = self._to_pascal_case(content_type_id) + "Filter"
        order_enum_type = self._to_pascal_case(content_type_id) + "Order"
        logger.debug(
            f"Fetching collection for content_type_id='{content_type_id}' "
            f"(collection field='{collection_field}', filter type='{filter_type}', order enum='{order_enum_type}')"
        )
        query_gql = f"""
            query GetEntries(
                $limit: Int, $skip: Int, $where: {filter_type}, $order: [{order_enum_type}!], $locale: String, $preview: Boolean
            ) {{
                {collection_field}(
                    limit: $limit, skip: $skip, where: $where, order: $order, locale: $locale, preview: $preview
                ) {{
                    total skip limit items {{ {fields_to_select_for_item} }}
                }}
            }}
        """
        variables: dict[str, Any] = {"preview": preview}
        if limit is not None:
            variables["limit"] = limit
        if skip is not None:
            variables["skip"] = skip
        if where:
            variables["where"] = where
        if order:
            variables["order"] = order
        if locale:
            variables["locale"] = locale

        try:
            return self.query(query_gql, variables=variables)
        except Exception as e:
            logger.error(
                f"Error executing get_entries_collection query: {e}", exc_info=True
            )
            return {"error": f"Failed to get entries collection: {e}"}

    def get_asset(
        self,
        asset_id: str,
        fields_to_select: str = "sys { id } url title description fileName contentType size width height",
        preview: bool = False,
    ) -> dict[str, Any]:
        """
        Fetches a single asset by its ID.
        (See original docstring for details)
        """
        if not self._ensure_loaded():
            return {
                "error": "Failed to initialize ContentfulApp. Check credentials and configuration."
            }

        logger.debug(f"Fetching asset_id='{asset_id}'")
        query_gql = f"""
            query GetAssetById($id: String!, $preview: Boolean) {{
                asset(id: $id, preview: $preview) {{ {fields_to_select} }}
            }}
        """
        variables: dict[str, Any] = {"id": asset_id, "preview": preview}

        try:
            return self.query(query_gql, variables=variables)
        except Exception as e:
            logger.error(f"Error executing get_asset query: {e}", exc_info=True)
            return {"error": f"Failed to get asset: {e}"}

    def get_assets_collection(
        self,
        fields_to_select_for_item: str = "sys { id } url title description fileName contentType size width height",
        limit: int | None = None,
        skip: int | None = None,
        where: dict[str, Any] | None = None,
        order: list[str] | None = None,
        locale: str | None = None,
        preview: bool = False,
    ) -> dict[str, Any]:
        """
        Fetches a collection of assets.
        (See original docstring for details)
        """
        if not self._ensure_loaded():
            return {
                "error": "Failed to initialize ContentfulApp. Check credentials and configuration."
            }

        logger.debug("Fetching assets collection")
        query_gql = f"""
            query GetAssets(
                $limit: Int, $skip: Int, $where: AssetFilter, $order: [AssetOrder!], $locale: String, $preview: Boolean
            ) {{
                assetCollection(
                    limit: $limit, skip: $skip, where: $where, order: $order, locale: $locale, preview: $preview
                ) {{
                    total skip limit items {{ {fields_to_select_for_item} }}
                }}
            }}
        """
        variables: dict[str, Any] = {"preview": preview}
        if limit is not None:
            variables["limit"] = limit
        if skip is not None:
            variables["skip"] = skip
        if where:
            variables["where"] = where
        if order:
            variables["order"] = order
        if locale:
            variables["locale"] = locale

        try:
            return self.query(query_gql, variables=variables)
        except Exception as e:
            logger.error(
                f"Error executing get_assets_collection query: {e}", exc_info=True
            )
            return {"error": f"Failed to get assets collection: {e}"}

    def execute_graphql_query(
        self, query_string: str, variables: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Executes an arbitrary GraphQL query against the configured Contentful space/environment.

        Args:
            query_string: The GraphQL query string.
            variables: Optional dictionary of variables for the query.

        Returns:
            The result of the query, or an error dictionary.

        Tags:
            important
        """
        if not self._ensure_loaded():
            return {
                "error": "Failed to initialize ContentfulApp. Check credentials and configuration."
            }

        logger.debug(f"Executing custom GraphQL query with variables: {variables}")
        try:
            return self.query(query_string, variables=variables)
        except Exception as e:
            logger.error(f"Error executing custom GraphQL query: {e}", exc_info=True)
            return {"error": f"Failed to execute custom query: {e}"}

    def list_tools(self) -> list[Callable]:
        """Returns a list of methods exposed as tools."""
        return [
            self.get_entry,
            self.get_entries_collection,
            self.get_asset,
            self.get_assets_collection,
            self.execute_graphql_query,
        ]
