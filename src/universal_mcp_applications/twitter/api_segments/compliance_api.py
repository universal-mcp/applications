from typing import Any

from .api_segment_base import APISegmentBase


class ComplianceApi(APISegmentBase):
    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def list_batch_compliance_jobs(
        self, type, status=None, compliance_job_fields=None
    ) -> dict[str, Any]:
        """

        Retrieves a list of compliance jobs based on the specified job type, with optional filtering by status.

        Args:
            type (string): The type parameter specifies the compliance job type and must be either "tweets" or "users".
            status (string): Filters compliance jobs by their current status, which can be one of: created, in_progress, failed, or complete.
            compliance_job_fields (array): A comma separated list of ComplianceJob fields to display. Example: "['created_at', 'download_expires_at', 'download_url', 'id', 'name', 'resumable', 'status', 'type', 'upload_expires_at', 'upload_url']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Compliance
        """
        url = f"{self.main_app_client.base_url}/2/compliance/jobs"
        query_params = {
            k: v
            for k, v in [
                ("type", type),
                ("status", status),
                ("compliance_job.fields", compliance_job_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_batch_compliance_job(
        self, type, name=None, resumable=None
    ) -> dict[str, Any]:
        """

        Creates a new compliance job using JSON data in the request body and authenticates the request using a Bearer token.

        Args:
            type (string): Type of compliance job to list.
            name (string): User-provided name for a compliance job. Example: 'my-job'.
            resumable (boolean): If true, this endpoint will return a pre-signed URL with resumable uploads enabled.

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Compliance
        """
        request_body_data = None
        request_body_data = {"name": name, "resumable": resumable, "type": type}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/2/compliance/jobs"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        return response.json()

    def get_batch_compliance_job(
        self, id, compliance_job_fields=None
    ) -> dict[str, Any]:
        """

        Retrieves information about a compliance job by its ID using the BearerToken for authentication.

        Args:
            id (string): id
            compliance_job_fields (array): A comma separated list of ComplianceJob fields to display. Example: "['created_at', 'download_expires_at', 'download_url', 'id', 'name', 'resumable', 'status', 'type', 'upload_expires_at', 'upload_url']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Compliance
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.main_app_client.base_url}/2/compliance/jobs/{id}"
        query_params = {
            k: v
            for k, v in [("compliance_job.fields", compliance_job_fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.list_batch_compliance_jobs,
            self.create_batch_compliance_job,
            self.get_batch_compliance_job,
        ]
