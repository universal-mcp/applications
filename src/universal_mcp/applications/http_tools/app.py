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
        Perform a GET request to the specified URL with optional parameters.

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
        Perform a POST request to the specified URL with optional parameters.

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
        Perform a PUT request to the specified URL with optional parameters.

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
        Perform a DELETE request to the specified URL with optional parameters.

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
        response = httpx.delete(url, json=body, headers=headers)
        response.raise_for_status()
        return self._handle_response(response)

    def http_patch(
        self, url: str, headers: dict | None = None, body: dict | None = None
    ):
        """
        Perform a PATCH request to the specified URL with optional parameters.

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
