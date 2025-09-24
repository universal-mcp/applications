from typing import Any

from .api_segment_base import APISegmentBase


class UsageApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def get_usage_tweets(self, days=None, usage_fields=None) -> dict[str, Any]:
        """
        Fetches Tweet usage data from the `/2/usage/tweets` API endpoint. It allows users to specify the number of days for the report and select specific usage fields to return, providing customized metrics on project consumption.

        Args:
            days (integer): Number of days to include in the tweet usage data, defaulting to 7 if not specified.
            usage_fields (array): A comma separated list of Usage fields to display. Example: "['cap_reset_day', 'daily_client_app_usage', 'daily_project_usage', 'project_cap', 'project_id', 'project_usage']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Usage
        """
        url = f"{self.main_app_client.base_url}/2/usage/tweets"
        query_params = {
            k: v
            for k, v in [("days", days), ("usage.fields", usage_fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [self.get_usage_tweets]
