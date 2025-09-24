from typing import Any  # For type hinting

import httpx
from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError  # For auth errors
from universal_mcp.integrations import Integration  # For integration type hint

from serpapi import SerpApiClient as SerpApiSearch  # Added SerpApiError


class SerpapiApp(APIApplication):
    def __init__(self, integration: Integration | None = None, **kwargs: Any) -> None:
        super().__init__(name="serpapi", integration=integration, **kwargs)
        self._serpapi_api_key: str | None = None  # Cache for the API key
        self.base_url = "https://serpapi.com/search"

    @property
    def serpapi_api_key(self) -> str:
        """
        A property that lazily retrieves the SerpApi API key from the integration and caches it for future use. It fetches credentials on first access, raising a `NotAuthorizedError` if the key is missing. Subsequent calls efficiently return the cached key.
        """
        if self._serpapi_api_key is None:
            if not self.integration:
                logger.error("SerpApi App: Integration not configured.")
                raise NotAuthorizedError(
                    "Integration not configured for SerpApi App. Cannot retrieve API key."
                )

            try:
                credentials = self.integration.get_credentials()
            except NotAuthorizedError as e:
                logger.error(
                    f"SerpApi App: Authorization error when fetching credentials: {e.message}"
                )
                raise  # Re-raise the original NotAuthorizedError
            except Exception as e:
                logger.error(
                    f"SerpApi App: Unexpected error when fetching credentials: {e}",
                    exc_info=True,
                )
                raise NotAuthorizedError(f"Failed to get SerpApi credentials: {e}")

            api_key = (
                credentials.get("api_key")
                or credentials.get("API_KEY")  # Check common variations
                or credentials.get("apiKey")
            )

            if not api_key:
                logger.error("SerpApi App: API key not found in credentials.")
                action_message = "API key for SerpApi is missing. Please ensure it's set in the store (e.g., SERPAPI_API_KEY in credentials)."
                if hasattr(self.integration, "authorize") and callable(
                    self.integration.authorize
                ):
                    try:
                        auth_details = self.integration.authorize()
                        if isinstance(auth_details, str):
                            action_message = auth_details
                        elif isinstance(auth_details, dict) and "url" in auth_details:
                            action_message = (
                                f"Please authorize via: {auth_details['url']}"
                            )
                        elif (
                            isinstance(auth_details, dict) and "message" in auth_details
                        ):
                            action_message = auth_details["message"]
                    except Exception as auth_e:
                        logger.warning(
                            f"Could not retrieve specific authorization action for SerpApi: {auth_e}"
                        )
                raise NotAuthorizedError(action_message)

            self._serpapi_api_key = api_key
            logger.info("SerpApi API Key successfully retrieved and cached.")
        return self._serpapi_api_key

    async def web_search(self, params: dict[str, Any] | None = None) -> str:
        """
        Performs a general web search via SerpApi, defaulting to the 'google_light' engine. It accepts custom parameters, retrieves organic results, and formats them into a string with titles, links, and snippets. It also handles API authentication and raises `NotAuthorizedError` for credential-related issues.

        Args:
            params: Dictionary of engine-specific parameters (e.g., {'q': 'Coffee', 'engine': 'google_light', 'location': 'Austin, TX'}). Defaults to None.

        Returns:
            A formatted string containing search results with titles, links, and snippets, or an error message if the search fails.

        Raises:
            NotAuthorizedError: If the API key cannot be retrieved or is invalid/rejected by SerpApi.
            Exception: For other unexpected errors during the search process. (Specific HTTP errors or SerpApiErrors are caught and returned as strings or raise NotAuthorizedError).

        Tags:
            search, async, web-scraping, api, serpapi, important
        """
        request_params = params or {}

        try:
            current_api_key = self.serpapi_api_key  # This can raise NotAuthorizedError
            logger.info("Attempting SerpApi search.")

            serpapi_call_params = {
                "api_key": current_api_key,
                "engine": "google_light",  # Fastest engine by default
                **request_params,  # Include any additional parameters from the user
            }

            # SerpApiSearch (SerpApiClient) uses the 'requests' library and its get_dict() is synchronous.
            # If true async behavior is needed, this call should be wrapped with asyncio.to_thread.
            search_client = SerpApiSearch(serpapi_call_params)
            data = search_client.get_dict()

            # Check for errors returned in the API response body
            if "error" in data:
                error_message = data["error"]
                logger.error(f"SerpApi API returned an error: {error_message}")
                # Keywords indicating authorization/authentication issues
                auth_error_keywords = [
                    "invalid api key",
                    "authorization failed",
                    "api key needed",
                    "forbidden",
                    "account disabled",
                    "private api key is missing",
                ]
                if any(
                    keyword in error_message.lower() for keyword in auth_error_keywords
                ):
                    raise NotAuthorizedError(f"SerpApi Error: {error_message}")
                return f"SerpApi API Error: {error_message}"  # Other API errors (e.g., missing parameters)

            # Process organic search results if available
            if "organic_results" in data:
                formatted_results = []
                for result in data.get("organic_results", []):
                    title = result.get("title", "No title")
                    link = result.get("link", "No link")
                    snippet = result.get("snippet", "No snippet")
                    formatted_results.append(
                        f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n"
                    )
                return (
                    "\n".join(formatted_results)
                    if formatted_results
                    else "No organic results found."
                )
            else:
                return "No organic results found."

        except (
            NotAuthorizedError
        ):  # Catches from self.serpapi_api_key or explicit raise above
            logger.error("SerpApi search failed due to an authorization error.")
            raise  # Re-raise to be handled by the MCP framework

        except httpx.HTTPStatusError as e:  # Kept from original for robustness, though SerpApiClient uses 'requests'
            logger.warning(
                f"SerpApi search encountered httpx.HTTPStatusError (unexpected with default SerpApiClient): {e.response.status_code}",
                exc_info=True,
            )
            if e.response.status_code == 429:
                return "Error: Rate limit exceeded (HTTP 429). Please try again later."
            elif (
                e.response.status_code == 401
            ):  # Key was fetched but rejected by API with HTTP 401
                raise NotAuthorizedError(
                    "Error: Invalid API key (HTTP 401). Please check your SERPAPI_API_KEY."
                )
            else:
                return f"HTTP Error: {e.response.status_code} - {e.response.text}"

        except Exception as e:  # General catch-all, similar to E2B's final catch
            error_message_lower = str(e).lower()
            logger.error(f"Unexpected error during SerpApi search: {e}", exc_info=True)
            # Infer auth error from generic exception message
            auth_error_keywords = [
                "authentication",
                "api key",
                "unauthorized",
                "401",
                "forbidden",
                "invalid key",
            ]
            if any(keyword in error_message_lower for keyword in auth_error_keywords):
                raise NotAuthorizedError(
                    f"SerpApi authentication/authorization failed: {str(e)}"
                )
            return f"An unexpected error occurred during search: {str(e)}"

    async def google_maps_search(
        self,
        q: str | None = None,
        ll: str | None = None,
        place_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Executes a Google Maps search via SerpApi using a query, coordinates, or place ID. It enhances the results by adding a `google_maps_url` to each location, distinguishing it from `get_google_maps_reviews` which retrieves reviews for a known place.

        Args:
            q (string, optional): The search query for Google Maps (e.g., "Coffee", "Restaurants", "Gas stations").
            ll (string, optional): Latitude and longitude with zoom level in format "@lat,lng,zoom" (e.g., "@40.7455096,-74.0083012,14z"). The zoom attribute ranges from 3z (map completely zoomed out) to 21z (map completely zoomed in). Results are not guaranteed to be within the requested geographic location.
            place_id (string, optional): The unique reference to a place in Google Maps. Place IDs are available for most locations, including businesses, landmarks, parks, and intersections. You can find the place_id using our Google Maps API. place_id can be used without any other optional parameter. place_id and data_cid can't be used together.

        Returns:
            dict[str, Any]: Formatted Google Maps search results with place names, addresses, ratings, and other details.

        Raises:
            ValueError: Raised when required parameters are missing.
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            google-maps, search, location, places, important
        """

        query_params = {}
        query_params = {
            "engine": "google_maps",
            "api_key": self.serpapi_api_key,
        }

        if q is not None:
            query_params["q"] = q

        if ll is not None:
            query_params["ll"] = ll

        if place_id is not None:
            query_params["place_id"] = place_id

        response = self._get(
            self.base_url,
            params=query_params,
        )
        data = self._handle_response(response)

        # Add Google Maps URLs for each place in the results
        if "local_results" in data:
            for place in data["local_results"]:
                if "place_id" in place:
                    place["google_maps_url"] = (
                        f"https://www.google.com/maps/place/?q=place_id:{place['place_id']}"
                    )

        return data

    async def get_google_maps_reviews(
        self,
        data_id: str,
        hl: str | None = None,
    ) -> dict[str, Any]:
        """
        Fetches Google Maps reviews for a specific location via SerpApi using its unique `data_id`. This function uses the `google_maps_reviews` engine, unlike `google_maps_search` which finds locations. Results can be returned in a specified language, defaulting to English.

        Args:
            data_id (string): The data ID of the place to get reviews for (e.g., "0x89c259af336b3341:0xa4969e07ce3108de").
            hl (string, optional): Language parameter for the search results. Defaults to "en".

        Returns:
            dict[str, Any]: Google Maps reviews data with ratings, comments, and other review details.

        Raises:
            ValueError: Raised when required parameters are missing.
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            google-maps, reviews, ratings, places, important
        """

        query_params = {}
        query_params = {
            "engine": "google_maps_reviews",
            "data_id": data_id,
            "api_key": self.serpapi_api_key,
        }

        if hl is not None:
            query_params["hl"] = hl
        else:
            query_params["hl"] = "en"

        response = self._get(
            self.base_url,
            params=query_params,
        )
        return self._handle_response(response)

    def list_tools(self) -> list[callable]:
        return [
            self.web_search,
            self.google_maps_search,
            self.get_google_maps_reviews,
        ]
