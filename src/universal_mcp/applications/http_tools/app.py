import httpx
from loguru import logger
from universal_mcp.applications.application import APIApplication


class HttpToolsApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize the HttpToolsApp.

        Args:
            **kwargs: Additional keyword arguments for the parent APIApplication.
        """
        super().__init__(name="http_tools", **kwargs)

    def _handle_response(self, response: httpx.Response):
        """
        Handle the HTTP response, returning JSON if possible, otherwise text.
        """
        try:
            return response.json()
        except Exception:
            logger.warning(
                f"Response is not JSON, returning text. Content-Type: {response.headers.get('content-type')}"
            )
            return {
                "text": response.text,
                "status_code": response.status_code,
                "headers": dict(response.headers),
            }

    def http_get(
        self, url: str, headers: dict | None = None, query_params: dict | None = None
    ):
        """
        Executes an HTTP GET request to a given URL with optional headers and query parameters. It handles HTTP errors by raising an exception and processes the response, returning parsed JSON or a dictionary with the raw text and status details if JSON is unavailable.

        Args:
            url (str): The URL to send the GET request to. Example: "https://api.example.com/data"
            headers (dict, optional): Optional HTTP headers to include in the request. Example: {"Authorization": "Bearer token"}
            query_params (dict, optional): Optional dictionary of query parameters to include in the request. Example: {"page": 1}

        Returns:
            dict: The JSON response from the GET request, or text if not JSON.
        Tags:
            get, important
        """
        logger.debug(
            f"GET request to {url} with headers {headers} and query params {query_params}"
        )
        response = httpx.get(url, params=query_params, headers=headers)
        response.raise_for_status()
        return self._handle_response(response)

    def http_post(
        self, url: str, headers: dict | None = None, body: dict | None = None
    ):
        """
        Sends an HTTP POST request to a URL with an optional JSON body and headers. It returns the parsed JSON response or raw text if parsing fails and raises an exception for HTTP errors. It is used for creating new resources, unlike http_get which retrieves data.

        Args:
            url (str): The URL to send the POST request to. Example: "https://api.example.com/data"
            headers (dict, optional): Optional HTTP headers to include in the request. Example: {"Content-Type": "application/json"}
            body (dict, optional): Optional JSON body to include in the request. Example: {"name": "John"}

        Returns:
            dict: The JSON response from the POST request, or text if not JSON.
        Tags:
            post, important
        """
        logger.debug(f"POST request to {url} with headers {headers} and body {body}")
        response = httpx.post(url, json=body, headers=headers)
        response.raise_for_status()
        return self._handle_response(response)

    def http_put(self, url: str, headers: dict | None = None, body: dict | None = None):
        """
        Performs an HTTP PUT request to update or replace a resource at a specified URL. It accepts an optional JSON body and headers, raises an exception for error responses, and returns the parsed JSON response or a dictionary with the raw text and status details.

        Args:
            url (str): The URL to send the PUT request to. Example: "https://api.example.com/data/1"
            headers (dict, optional): Optional HTTP headers to include in the request. Example: {"Authorization": "Bearer token"}
            body (dict, optional): Optional JSON body to include in the request. Example: {"name": "Jane"}

        Returns:
            dict: The JSON response from the PUT request, or text if not JSON.
        Tags:
            put, important
        """
        logger.debug(f"PUT request to {url} with headers {headers} and body {body}")
        response = httpx.put(url, json=body, headers=headers)
        response.raise_for_status()
        return self._handle_response(response)

    def http_delete(
        self, url: str, headers: dict | None = None, body: dict | None = None
    ):
        """
        Sends an HTTP DELETE request to a URL with optional headers and a JSON body. Raises an exception for HTTP error statuses and returns the parsed JSON response. If the response isn't JSON, it returns the text content, status code, and headers.

        Args:
            url (str): The URL to send the DELETE request to. Example: "https://api.example.com/data/1"
            headers (dict, optional): Optional HTTP headers to include in the request. Example: {"Authorization": "Bearer token"}
            body (dict, optional): Optional JSON body to include in the request. Example: {"reason": "obsolete"}

        Returns:
            dict: The JSON response from the DELETE request, or text if not JSON.
        Tags:
            delete, important
        """
        logger.debug(f"DELETE request to {url} with headers {headers} and body {body}")
        response = httpx.delete(url, headers=headers)
        response.raise_for_status()
        return self._handle_response(response)

    def http_patch(
        self, url: str, headers: dict | None = None, body: dict | None = None
    ):
        """
        Sends an HTTP PATCH request to apply partial modifications to a resource at a given URL. It accepts optional headers and a JSON body. It returns the parsed JSON response, or the raw text with status details if the response is not valid JSON.

        Args:
            url (str): The URL to send the PATCH request to. Example: "https://api.example.com/data/1"
            headers (dict, optional): Optional HTTP headers to include in the request. Example: {"Authorization": "Bearer token"}
            body (dict, optional): Optional JSON body to include in the request. Example: {"status": "active"}

        Returns:
            dict: The JSON response from the PATCH request, or text if not JSON.
        Tags:
            patch, important
        """
        logger.debug(f"PATCH request to {url} with headers {headers} and body {body}")
        response = httpx.patch(url, json=body, headers=headers)
        response.raise_for_status()
        return self._handle_response(response)

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        Tags:
            list, important
        """
        return [
            self.http_get,
            self.http_post,
            self.http_put,
            self.http_delete,
            self.http_patch,
        ]
