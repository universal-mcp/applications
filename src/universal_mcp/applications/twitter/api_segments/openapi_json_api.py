from typing import Any

from .api_segment_base import APISegmentBase


class OpenapiJsonApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def get_open_api_spec(self) -> dict[str, Any]:
        """
        Args:
            None

        Retrieves the OpenAPI JSON file at the specified path "/2/openapi.json" using the GET method.

        Returns:
            dict[str, Any]: The request was successful

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            General
        """
        url = f"{self.main_app_client.base_url}/2/openapi.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [self.get_open_api_spec]
