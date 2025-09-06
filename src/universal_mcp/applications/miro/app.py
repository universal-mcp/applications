from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class MiroApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="miro", integration=integration, **kwargs)
        self.base_url = "https://api.miro.com"

    def revoke_token_v1(self, access_token=None) -> Any:
        """
        Revokes an OAuth access token using the POST method at "/v1/oauth/revoke", allowing clients to invalidate tokens as needed.

        Args:
            access_token (string): (Required) Access token that you want to revoke Example: '<Add your access token here>'.

        Returns:
            Any: API response data.

        Tags:
            Tokens
        """
        url = f"{self.base_url}/v1/oauth/revoke"
        query_params = {
            k: v for k, v in [("access_token", access_token)] if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_access_token_information(self) -> Any:
        """
        Retrieves an OAuth 2.0 token using the GET method for client authorization purposes.

        Returns:
            Any: API response data.

        Tags:
            Tokens
        """
        url = f"{self.base_url}/v1/oauth-token"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_audit_logs(
        self,
        createdAfter=None,
        createdBefore=None,
        cursor=None,
        limit=None,
        sorting=None,
    ) -> Any:
        """
        Retrieves audit logs with optional filtering by time range, pagination, and sorting parameters.

        Args:
            createdAfter (string): (Required) Retrieve audit logs created after the date and time provided. This is the start date of the duration for which you want to retrieve audit logs. For example, if you want to retrieve audit logs between `2023-03-30T17:26:50.000Z` and `2023-04-30T17:26:50.000Z`, provide `2023-03-30T17:26:50.000Z` as the value for the `createdAfter` parameter.<br>Format: UTC, adheres to [ISO 8601]( including milliseconds and a [trailing Z offset]( Example: '2023-03-30T17:26:50.000Z'.
            createdBefore (string): (Required) Retrieve audit logs created before the date and time provided. This is the end date of the duration for which you want to retrieve audit logs. For example, if you want to retrieve audit logs between `2023-03-30T17:26:50.000Z` and `2023-04-30T17:26:50.000Z`, provide `2023-04-30T17:26:50.000Z` as the value for the `createdBefore` parameter.<br>Format: UTC, adheres to [ISO 8601]( including milliseconds and a [trailing Z offset]( Example: '2023-04-30T17:26:50.000Z'.
            cursor (string): A cursor-paginated method returns a portion of the total set of results based on the `limit` specified and a `cursor` that points to the next portion of the results. To retrieve the next set of results of the collection, set the `cursor` parameter in your next request to the appropriate cursor value returned in the response.
            limit (string): Maximum number of results returned based on the `limit` specified in the request. For example, if there are `30` results, the request has no `cursor` value, and the `limit` is set to `20`,the `size` of the results will be `20`. The rest of the results will not be returned. To retrieve the rest of the results, you must make another request and set the appropriate value for the `cursor` parameter value that you obtained from the response.<br>Default: `100` Example: '100'.
            sorting (string): Sort order in which you want to view the result set. Based on the value you provide, the results are sorted in an ascending or descending order of the audit log creation date (audit log `createdAt` parameter).<br>Default: `ASC` Example: 'ASC'.

        Returns:
            Any: API response data.

        Tags:
            Audit Logs
        """
        url = f"{self.base_url}/v2/audit/logs"
        query_params = {
            k: v
            for k, v in [
                ("createdAfter", createdAfter),
                ("createdBefore", createdBefore),
                ("cursor", cursor),
                ("limit", limit),
                ("sorting", sorting),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_settings(self, org_id) -> Any:
        """
        Retrieves data classification settings for an organization, providing information on how data is categorized and handled within the specified organization.

        Args:
            org_id (string): org_id

        Returns:
            Any: API response data.

        Tags:
            Board classification: Organization level
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/data-classification-settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_update_boards_classification(
        self, org_id, team_id, labelId=None, notClassifiedOnly=None
    ) -> Any:
        """
        Updates the data classification settings for a specific team in an organization using the "PATCH" method.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            labelId (number): labelId Example: '3000457366756291000'.
            notClassifiedOnly (boolean): notClassifiedOnly
                Example:
                ```json
                {
                  "labelId": 3000457366756291000,
                  "notClassifiedOnly": true
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Board classification: Team level
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        request_body = {
            "labelId": labelId,
            "notClassifiedOnly": notClassifiedOnly,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/data-classification"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_settings(self, org_id, team_id) -> Any:
        """
        Retrieves the data classification settings for a specific team within an organization.

        Args:
            org_id (string): org_id
            team_id (string): team_id

        Returns:
            Any: API response data.

        Tags:
            Board classification: Team level
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/data-classification-settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_team_settings(
        self, org_id, team_id, defaultLabelId=None, enabled=None
    ) -> Any:
        """
        Updates data classification settings for a specific team within an organization using the PATCH method.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            defaultLabelId (number): defaultLabelId Example: '3000457366756291000'.
            enabled (boolean): enabled
                Example:
                ```json
                {
                  "defaultLabelId": 3000457366756291000,
                  "enabled": true
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Board classification: Team level
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        request_body = {
            "defaultLabelId": defaultLabelId,
            "enabled": enabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/data-classification-settings"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_board_classification(self, org_id, team_id, board_id) -> Any:
        """
        Retrieves data classification details for a specified organization, team, and board using the provided identifiers.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            board_id (string): board_id

        Returns:
            Any: API response data.

        Tags:
            Board classification: Board level
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/boards/{board_id}/data-classification"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_board_classification(
        self, org_id, team_id, board_id, labelId=None
    ) -> Any:
        """
        Assigns data classifications to a board within a specified organization and team using the provided criteria and returns a success status upon completion.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            board_id (string): board_id
            labelId (string): labelId
                Example:
                ```json
                {
                  "labelId": "3000457366756290996"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Board classification: Board level
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "labelId": labelId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/boards/{board_id}/data-classification"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_cases(self, org_id, limit=None, cursor=None) -> Any:
        """
        Retrieves a list of cases for a specified organization using the "GET" method, allowing optional query parameters for pagination via "limit" and "cursor".

        Args:
            org_id (string): org_id
            limit (string): (Required) The maximum number of items in the result list. Example: '10'.
            cursor (string): An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request. Example: 'MTY2OTg4NTIwMDAwMHwxMjM='.

        Returns:
            Any: API response data.

        Tags:
            Legal holds
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/cases"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_case(self, org_id, case_id) -> Any:
        """
        Retrieves a specific case for an organization with the provided org_id and case_id.

        Args:
            org_id (string): org_id
            case_id (string): case_id

        Returns:
            Any: API response data.

        Tags:
            Legal holds
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if case_id is None:
            raise ValueError("Missing required parameter 'case_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/cases/{case_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_legal_holds_within_acase(
        self, org_id, case_id, limit=None, cursor=None
    ) -> Any:
        """
        Retrieves a paginated list of legal holds for a specific case and organization using cursor-based pagination.

        Args:
            org_id (string): org_id
            case_id (string): case_id
            limit (string): (Required) The maximum number of items in the result list. Example: '10'.
            cursor (string): An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request. Example: 'MTY2OTg4NTIwMDAwMHwxMjM='.

        Returns:
            Any: API response data.

        Tags:
            Legal holds
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if case_id is None:
            raise ValueError("Missing required parameter 'case_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/cases/{case_id}/legal-holds"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_legal_hold_information(self, org_id, case_id, legal_hold_id) -> Any:
        """
        Retrieves a specific legal hold for a case within an organization using the provided identifiers.

        Args:
            org_id (string): org_id
            case_id (string): case_id
            legal_hold_id (string): legal_hold_id

        Returns:
            Any: API response data.

        Tags:
            Legal holds
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if case_id is None:
            raise ValueError("Missing required parameter 'case_id'")
        if legal_hold_id is None:
            raise ValueError("Missing required parameter 'legal_hold_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/cases/{case_id}/legal-holds/{legal_hold_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_content_items_under_legal_hold(
        self, org_id, case_id, legal_hold_id, limit=None, cursor=None
    ) -> Any:
        """
        Retrieves a list of content items under a specific legal hold in a case for an organization, allowing for pagination using limit and cursor parameters.

        Args:
            org_id (string): org_id
            case_id (string): case_id
            legal_hold_id (string): legal_hold_id
            limit (string): (Required) The maximum number of items in the result list. Example: '10'.
            cursor (string): An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request. Example: 'MTY2OTg4NTIwMDAwMHwxMjM='.

        Returns:
            Any: API response data.

        Tags:
            Legal holds
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if case_id is None:
            raise ValueError("Missing required parameter 'case_id'")
        if legal_hold_id is None:
            raise ValueError("Missing required parameter 'legal_hold_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/cases/{case_id}/legal-holds/{legal_hold_id}/content-items"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_board_export_job(
        self, org_id, request_id=None, boardFormat=None, boardIds=None
    ) -> Any:
        """
        Exports board data for a specified organization using the "POST" method and returns a job status.

        Args:
            org_id (string): org_id
            request_id (string): (Required) Unique identifier of the board export job. Example: '92343229-c532-446d-b8cb-2f155bedb807'.
            boardFormat (string): boardFormat Example: 'SVG'.
            boardIds (array): boardIds
                Example:
                ```json
                {
                  "boardFormat": "SVG",
                  "boardIds": [
                    "o9J_kzlUDmo="
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Board Export
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        request_body = {
            "boardFormat": boardFormat,
            "boardIds": boardIds,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/boards/export/jobs"
        query_params = {k: v for k, v in [("request_id", request_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_board_export_job_status(self, org_id, job_id) -> Any:
        """
        Retrieves the status and details of a specified board export job for an organization using the API.

        Args:
            org_id (string): org_id
            job_id (string): job_id

        Returns:
            Any: API response data.

        Tags:
            Board Export
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/boards/export/jobs/{job_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_results_for_board_export_job(self, org_id, job_id) -> Any:
        """
        Retrieves the export results for a specific organization's board export job using the API.

        Args:
            org_id (string): org_id
            job_id (string): job_id

        Returns:
            Any: API response data.

        Tags:
            Board Export
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/boards/export/jobs/{job_id}/results"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_content_change_logs_of_board_items(
        self,
        org_id,
        board_ids=None,
        emails=None,
        from_=None,
        to=None,
        cursor=None,
        limit=None,
        sorting=None,
    ) -> Any:
        """
        Retrieves organization content logs with filtering options such as board IDs, email addresses, date ranges, and pagination parameters.

        Args:
            org_id (string): org_id
            board_ids (string): List of board IDs for which you want to retrieve the content logs. Example: 'o9J_kzlUDmo='.
            emails (string): Filter content logs based on the list of emails of users who created, modified, or deleted the board item. Example: 'someone@domain.com'.
            from_ (string): (Required) Filter content logs based on the date and time when the board item was last modified. This is the start date and time for the modified date duration.
        Format: UTC, adheres to [ISO 8601]( includes a [trailing Z offset]( Example: '2022-03-30T17:26:50Z'.
            to (string): (Required) Filter content logs based on the date and time when the board item was last modified. This is the end date and time for the modified date duration. Format: UTC, adheres to
        [ISO 8601]( includes a [trailing Z offset]( Example: '2023-03-30T17:26:50Z'.
            cursor (string): A cursor-paginated method returns a portion of the total set of results based on the limit specified and a cursor that points to the next portion of the results. To retrieve the next portion of the collection, set the cursor parameter equal to the cursor value you received in the response of the previous request. Example: 'MTY2OTg4NTIwMDAwMHwxMjM='.
            limit (string): The maximum number of results to return per call. If the number of logs in the response is greater than the limit specified, the response returns the cursor parameter with a value. Example: '1000'.
            sorting (string): Sort order in which you want to view the result set based on the modified date. To sort by an ascending modified date, specify `asc`. To sort by a descending modified date, specify `desc`. Example: 'asc'.

        Returns:
            Any: API response data.

        Tags:
            Board Content Logs
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/content-logs/items"
        query_params = {
            k: v
            for k, v in [
                ("board_ids", board_ids),
                ("emails", emails),
                ("from", from_),
                ("to", to),
                ("cursor", cursor),
                ("limit", limit),
                ("sorting", sorting),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def reset_all_sessions_of_auser(self, email=None) -> Any:
        """
        Resets all active sessions for a specified user (identified by email), requiring reauthentication.

        Args:
            email (string): (Required) Email ID of the user whose sessions you want to reset. Note that this user will be signed out from all devices. Example: 'john.smith@example.com'.

        Returns:
            Any: API response data.

        Tags:
            Reset all sessions of a user
        """
        url = f"{self.base_url}/v2/sessions/reset_all"
        query_params = {k: v for k, v in [("email", email)] if v is not None}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_info(self, org_id) -> Any:
        """
        Retrieves information about an organization specified by its ID using the API endpoint "/v2/orgs/{org_id}" with the GET method.

        Args:
            org_id (string): org_id

        Returns:
            Any: API response data.

        Tags:
            Organizations
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_members(
        self,
        org_id,
        emails=None,
        role=None,
        license=None,
        active=None,
        cursor=None,
        limit=None,
    ) -> Any:
        """
        Retrieves a list of members from an organization specified by `{org_id}` using query parameters for filtering by email, role, license status, and member activity, with pagination options.

        Args:
            org_id (string): org_id
            emails (string): Comma-separated list of member email addresses to filter the organization membership list. Example: 'someEmail1@miro.com'.
            role (string): Filters members by their assigned role within the organization. Example: 'organization_internal_admin'.
            license (string): Filter results by a specific license when retrieving members of an organization. Example: 'full'.
            active (string): A boolean query parameter indicating whether to include only active members in the response. Example: 'false'.
            cursor (string): Used for cursor-based pagination, this parameter specifies a unique identifier or token that marks the position in the dataset, allowing the retrieval of the next or previous page of results. Example: '3055557345821141000'.
            limit (string): The **limit** parameter specifies the maximum number of member records to return in a single response for the organization identified by `{org_id}`. Example: '100'.

        Returns:
            Any: API response data.

        Tags:
            Organization Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/members"
        query_params = {
            k: v
            for k, v in [
                ("emails", emails),
                ("role", role),
                ("license", license),
                ("active", active),
                ("cursor", cursor),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_member(self, org_id, member_id) -> Any:
        """
        Retrieves a specific member's details within an organization using their unique identifiers.

        Args:
            org_id (string): org_id
            member_id (string): member_id

        Returns:
            Any: API response data.

        Tags:
            Organization Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/members/{member_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_boards(
        self,
        team_id=None,
        project_id=None,
        query=None,
        owner=None,
        limit=None,
        offset=None,
        sort=None,
    ) -> Any:
        """
        Retrieves a list of boards filtered by team, project, search query, owner, and pagination parameters.

        Args:
            team_id (string): The `team_id` parameter specifies the identifier of the team to be queried in conjunction with the `GET /v2/boards` operation. Example: '{{team_id}}'.
            project_id (string): The `project_id` query parameter specifies the unique identifier of the project associated with the API request.
            query (string): A search parameter to filter or specify which boards to retrieve.
            owner (string): Filters results to include only boards owned by the specified user.
            limit (string): Specifies the maximum number of results to return in response to a GET operation on the "/v2/boards" endpoint.
            offset (string): Specifies the starting position in the dataset to exclude the first N items from the response.
            sort (string): Specifies the field(s) to sort results by, using comma-separated values with optional +/- prefixes for ascending/descending order (e.g., "+date,-title"). Example: 'default'.

        Returns:
            Any: API response data.

        Tags:
            Boards
        """
        url = f"{self.base_url}/v2/boards"
        query_params = {
            k: v
            for k, v in [
                ("team_id", team_id),
                ("project_id", project_id),
                ("query", query),
                ("owner", owner),
                ("limit", limit),
                ("offset", offset),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def copy_board(
        self, copy_from=None, description=None, name=None, policy=None, teamId=None
    ) -> Any:
        """
        Updates a board's configuration (with optional source copying) and returns the updated board details.

        Args:
            copy_from (string): (Required) Unique identifier (ID) of the board that you want to copy. Example: 'o9J_kzlUDmo='.
            description (string): description Example: 'Description'.
            name (string): name Example: 'Untitled'.
            policy (object): policy
            teamId (string): teamId
                Example:
                ```json
                {
                  "description": "Description",
                  "name": "Untitled",
                  "policy": {
                    "permissionsPolicy": {
                      "collaborationToolsStartAccess": "all_editors",
                      "copyAccess": "anyone",
                      "sharingAccess": "team_members_with_editing_rights"
                    },
                    "sharingPolicy": {
                      "access": "private",
                      "inviteToAccountAndBoardLinkAccess": "no_access",
                      "organizationAccess": "private",
                      "teamAccess": "private"
                    }
                  },
                  "teamId": "{{team_id}}"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Boards
        """
        request_body = {
            "description": description,
            "name": name,
            "policy": policy,
            "teamId": teamId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards"
        query_params = {k: v for k, v in [("copy_from", copy_from)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_board(
        self, description=None, name=None, policy=None, projectId=None, teamId=None
    ) -> Any:
        """
        Creates a new board resource and returns a success status upon completion.

        Args:
            description (string): description Example: 'Description'.
            name (string): name Example: 'Untitled'.
            policy (object): policy
            projectId (string): projectId Example: '<value>'.
            teamId (string): teamId
                Example:
                ```json
                {
                  "description": "Description",
                  "name": "Untitled",
                  "policy": {
                    "permissionsPolicy": {
                      "collaborationToolsStartAccess": "all_editors",
                      "copyAccess": "anyone",
                      "sharingAccess": "team_members_with_editing_rights"
                    },
                    "sharingPolicy": {
                      "access": "private",
                      "inviteToAccountAndBoardLinkAccess": "no_access",
                      "organizationAccess": "private",
                      "teamAccess": "private"
                    }
                  },
                  "projectId": "<value>",
                  "teamId": "{{team_id}}"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Boards
        """
        request_body = {
            "description": description,
            "name": name,
            "policy": policy,
            "projectId": projectId,
            "teamId": teamId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_board(self, board_id) -> Any:
        """
        Retrieves information about a specific board identified by its ID using the API endpoint "/v2/boards/{board_id}" with the GET method.

        Args:
            board_id (string): board_id

        Returns:
            Any: API response data.

        Tags:
            Boards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_board(self, board_id) -> Any:
        """
        Deletes a specific board identified by its ID using the "DELETE" method, effectively removing it from the system and returning a success status when completed.

        Args:
            board_id (string): board_id

        Returns:
            Any: API response data.

        Tags:
            Boards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_board(
        self,
        board_id,
        description=None,
        name=None,
        policy=None,
        projectId=None,
        teamId=None,
    ) -> Any:
        """
        Updates a Trello board identified by `{board_id}` using the Trello API and returns a status message.

        Args:
            board_id (string): board_id
            description (string): description Example: 'Description'.
            name (string): name Example: 'Untitled'.
            policy (object): policy
            projectId (string): projectId Example: '<value>'.
            teamId (string): teamId
                Example:
                ```json
                {
                  "description": "Description",
                  "name": "Untitled",
                  "policy": {
                    "permissionsPolicy": {
                      "collaborationToolsStartAccess": "all_editors",
                      "copyAccess": "anyone",
                      "sharingAccess": "team_members_with_editing_rights"
                    },
                    "sharingPolicy": {
                      "access": "private",
                      "inviteToAccountAndBoardLinkAccess": "no_access",
                      "organizationAccess": "private",
                      "teamAccess": "private"
                    }
                  },
                  "projectId": "<value>",
                  "teamId": "{{team_id}}"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Boards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "description": description,
            "name": name,
            "policy": policy,
            "projectId": projectId,
            "teamId": teamId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_app_card_item(
        self, board_id, data=None, geometry=None, parent=None, position=None, style=None
    ) -> Any:
        """
        Creates a new app card on a specified board using the "POST" method, identified by the path "/v2/boards/{board_id}/app_cards".

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "description": "Sample app card description",
                    "fields": [
                      {
                        "fillColor": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "iconShape": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "iconUrl": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "textColor": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "tooltip": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "value": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        }
                      },
                      {
                        "fillColor": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "iconShape": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "iconUrl": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "textColor": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "tooltip": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "value": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        }
                      }
                    ],
                    "status": "disconnected",
                    "title": "sample app card item"
                  },
                  "geometry": {
                    "height": 60,
                    "rotation": 0,
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "fillColor": "#2d9bf0"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            App Cards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/app_cards"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_app_card_item(self, board_id, item_id) -> Any:
        """
        Retrieves the details of an app card with the specified item ID from a board using the GET method.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            App Cards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/app_cards/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_app_card_item(self, board_id, item_id) -> Any:
        """
        Deletes an app card item from the specified board using the DELETE method and returns a success status upon completion.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            App Cards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/app_cards/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_app_card_item(
        self,
        board_id,
        item_id,
        data=None,
        geometry=None,
        parent=None,
        position=None,
        style=None,
    ) -> Any:
        """
        Updates a specific app card on the specified board using partial modifications via the PATCH method.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "description": "Sample app card description",
                    "fields": [
                      {
                        "fillColor": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "iconShape": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "iconUrl": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "textColor": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "tooltip": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "value": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        }
                      },
                      {
                        "fillColor": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "iconShape": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "iconUrl": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "textColor": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "tooltip": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "value": {
                          "value": "<Error: Too many levels of nesting to fake this schema>"
                        }
                      }
                    ],
                    "status": "disconnected",
                    "title": "sample app card item"
                  },
                  "geometry": {
                    "height": 60,
                    "rotation": 0,
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "fillColor": "#2d9bf0"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            App Cards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/app_cards/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_card_item(
        self, board_id, data=None, geometry=None, parent=None, position=None, style=None
    ) -> Any:
        """
        Creates a new card on the specified board using the provided data and returns the operation status upon success.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "assigneeId": "3074457362577955300",
                    "description": "sample card description",
                    "dueDate": "2023-10-12T22:00:55.000Z",
                    "title": "sample card item"
                  },
                  "geometry": {
                    "height": 60,
                    "rotation": 0,
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "cardTheme": "#2d9bf0"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Cards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/cards"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_card_item(self, board_id, item_id) -> Any:
        """
        Retrieves a specific card from a board using its board ID and item ID, returning relevant details in the response.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Cards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/cards/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_card_item(self, board_id, item_id) -> Any:
        """
        Deletes a specific card item from a board by ID and returns a success status upon removal.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Cards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/cards/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_card_item(
        self,
        board_id,
        item_id,
        data=None,
        geometry=None,
        parent=None,
        position=None,
        style=None,
    ) -> Any:
        """
        Updates specified fields of a card item on a board using partial modifications.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "assigneeId": "3074457362577955300",
                    "description": "sample card description",
                    "dueDate": "2023-10-12T22:00:55.000Z",
                    "title": "sample card item"
                  },
                  "geometry": {
                    "height": 60,
                    "rotation": 0,
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "cardTheme": "#2d9bf0"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Cards
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/cards/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_connectors(self, board_id, limit=None, cursor=None) -> Any:
        """
        Retrieves a list of connectors associated with a specific board, allowing optional filtering by limit and cursor parameters.

        Args:
            board_id (string): board_id
            limit (string): Specifies the maximum number of connectors to return in a single response page. Example: '10'.
            cursor (string): A unique identifier used for cursor pagination, allowing incremental retrieval of data in a specific order, typically included in subsequent GET requests to fetch the next or previous page of results.

        Returns:
            Any: API response data.

        Tags:
            Connectors
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/connectors"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_connector(
        self,
        board_id,
        captions=None,
        endItem=None,
        shape=None,
        startItem=None,
        style=None,
    ) -> Any:
        """
        Establishes a connection to a specific board by creating a new connector using the API at the path "/v2/boards/{board_id}/connectors" with the POST method.

        Args:
            board_id (string): board_id
            captions (array): captions Example: "[{'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}]".
            endItem (object): endItem
            shape (string): shape Example: 'straight'.
            startItem (object): startItem
            style (object): style
                Example:
                ```json
                {
                  "captions": [
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    }
                  ],
                  "endItem": {
                    "id": "3458764517517818867",
                    "position": {
                      "x": "50%",
                      "y": "0%"
                    },
                    "snapTo": "auto"
                  },
                  "shape": "straight",
                  "startItem": {
                    "id": "3458764517517818867",
                    "position": {
                      "x": "50%",
                      "y": "0%"
                    },
                    "snapTo": "auto"
                  },
                  "style": {
                    "color": "#9510ac",
                    "endStrokeCap": "none",
                    "fontSize": "15",
                    "startStrokeCap": "none",
                    "strokeColor": "#2d9bf0",
                    "strokeStyle": "normal",
                    "strokeWidth": "2.0",
                    "textOrientation": "horizontal"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Connectors
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "captions": captions,
            "endItem": endItem,
            "shape": shape,
            "startItem": startItem,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/connectors"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_connector(self, board_id, connector_id) -> Any:
        """
        Retrieves a specific connector from a board using the provided board and connector identifiers.

        Args:
            board_id (string): board_id
            connector_id (string): connector_id

        Returns:
            Any: API response data.

        Tags:
            Connectors
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if connector_id is None:
            raise ValueError("Missing required parameter 'connector_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/connectors/{connector_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_connector(self, board_id, connector_id) -> Any:
        """
        Deletes a specific connector associated with a board, identified by the provided `board_id` and `connector_id`, removing it along with any related configurations.

        Args:
            board_id (string): board_id
            connector_id (string): connector_id

        Returns:
            Any: API response data.

        Tags:
            Connectors
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if connector_id is None:
            raise ValueError("Missing required parameter 'connector_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/connectors/{connector_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_connector(
        self,
        board_id,
        connector_id,
        captions=None,
        endItem=None,
        shape=None,
        startItem=None,
        style=None,
    ) -> Any:
        """
        Updates a connector on a specific board using the PATCH method, returning a status message upon successful modification.

        Args:
            board_id (string): board_id
            connector_id (string): connector_id
            captions (array): captions Example: "[{'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}, {'content': '<p>Caption text</p>', 'position': '50%', 'textAlignVertical': 'top'}]".
            endItem (object): endItem
            shape (string): shape Example: 'straight'.
            startItem (object): startItem
            style (object): style
                Example:
                ```json
                {
                  "captions": [
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    },
                    {
                      "content": "<p>Caption text</p>",
                      "position": "50%",
                      "textAlignVertical": "top"
                    }
                  ],
                  "endItem": {
                    "id": "3458764517517818867",
                    "position": {
                      "x": "50%",
                      "y": "0%"
                    },
                    "snapTo": "auto"
                  },
                  "shape": "straight",
                  "startItem": {
                    "id": "3458764517517818867",
                    "position": {
                      "x": "50%",
                      "y": "0%"
                    },
                    "snapTo": "auto"
                  },
                  "style": {
                    "color": "#9510ac",
                    "endStrokeCap": "none",
                    "fontSize": "15",
                    "startStrokeCap": "none",
                    "strokeColor": "#2d9bf0",
                    "strokeStyle": "normal",
                    "strokeWidth": "2.0",
                    "textOrientation": "horizontal"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Connectors
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if connector_id is None:
            raise ValueError("Missing required parameter 'connector_id'")
        request_body = {
            "captions": captions,
            "endItem": endItem,
            "shape": shape,
            "startItem": startItem,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/connectors/{connector_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_document_item_using_url(
        self, board_id, data=None, geometry=None, parent=None, position=None
    ) -> Any:
        """
        Adds a document to a specified board using the POST method and returns a status message.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
                Example:
                ```json
                {
                  "data": {
                    "title": "Sample document title",
                    "url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
                  },
                  "geometry": {
                    "height": 100,
                    "rotation": 0,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Documents
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/documents"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_document_item(self, board_id, item_id) -> Any:
        """
        Retrieves a specific document from a board using the provided board ID and item ID.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Documents
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/documents/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_document_item(self, board_id, item_id) -> Any:
        """
        Deletes a specified document from a board using its unique identifier and returns a success status upon completion.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Documents
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/documents/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_document_item_using_url(
        self, board_id, item_id, data=None, geometry=None, parent=None, position=None
    ) -> Any:
        """
        Updates a specific document within a board using partial modifications and returns a success status.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
                Example:
                ```json
                {
                  "data": {
                    "title": "<value>",
                    "url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
                  },
                  "geometry": {
                    "height": 100,
                    "rotation": 0,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Documents
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/documents/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_embed_item(
        self, board_id, data=None, geometry=None, parent=None, position=None
    ) -> Any:
        """
        Creates an embed associated with a specific board, returning the result upon successful creation.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
                Example:
                ```json
                {
                  "data": {
                    "mode": "inline",
                    "previewUrl": "https://miro.com/static/images/page/mr-index/localization/en/slider/ideation_brainstorming.png",
                    "url": "https://www.youtube.com/watch?v=HlVSNEiFCBk"
                  },
                  "geometry": {
                    "height": 100,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Embeds
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/embeds"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_embed_item(self, board_id, item_id) -> Any:
        """
        Retrieves an embedded item from a specified board using the provided board and item identifiers.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Embeds
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/embeds/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_embed_item(self, board_id, item_id) -> Any:
        """
        Deletes the specified embed item from the board by its ID and returns a success status upon removal.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Embeds
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/embeds/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_embed_item(
        self, board_id, item_id, data=None, geometry=None, parent=None, position=None
    ) -> Any:
        """
        Updates an embedded item within a specified board and returns the updated result.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
                Example:
                ```json
                {
                  "data": {
                    "mode": "inline",
                    "previewUrl": "https://miro.com/static/images/page/mr-index/localization/en/slider/ideation_brainstorming.png",
                    "url": "https://www.youtube.com/watch?v=HlVSNEiFCBk"
                  },
                  "geometry": {
                    "height": 100,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Embeds
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/embeds/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_image_item_using_url(
        self, board_id, data=None, geometry=None, parent=None, position=None
    ) -> Any:
        """
        Uploads an image to a specified board and returns success status upon completion.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
                Example:
                ```json
                {
                  "data": {
                    "title": "Sample image title",
                    "url": "https://miro.com/static/images/page/mr-index/localization/en/slider/ideation_brainstorming.png"
                  },
                  "geometry": {
                    "height": 100,
                    "rotation": 0,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Images
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/images"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image_item(self, board_id, item_id) -> Any:
        """
        Retrieves a specific image item from a designated board using the provided identifiers.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Images
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/images/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_image_item(self, board_id, item_id) -> Any:
        """
        Deletes a specific image from a specified board.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Images
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/images/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_image_item_using_url(
        self, board_id, item_id, data=None, geometry=None, parent=None, position=None
    ) -> Any:
        """
        Updates a specific image in a board using the PATCH method, applying partial modifications to the image's properties.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
                Example:
                ```json
                {
                  "data": {
                    "title": "Test image title",
                    "url": "https://miro.com/static/images/page/mr-index/localization/en/slider/ideation_brainstorming.png"
                  },
                  "geometry": {
                    "height": 100,
                    "rotation": 0,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Images
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/images/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_on_board(self, board_id, limit=None, type=None, cursor=None) -> Any:
        """
        Retrieves a paginated list of items from a specified board using query parameters for limit, type, and cursor-based pagination.

        Args:
            board_id (string): board_id
            limit (string): Limits the number of items returned in the response when retrieving items from a board. Example: '10'.
            type (string): Specifies the category or classification of items to retrieve from the board. Example: 'text'.
            cursor (string): A token used to fetch the next page of items, typically a unique identifier from the last retrieved record.

        Returns:
            Any: API response data.

        Tags:
            Items
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/items"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("type", type), ("cursor", cursor)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_item_on_board(self, board_id, item_id) -> Any:
        """
        Retrieves details of a specific item from a board using the GET method and returns the data in response.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Items
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/items/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_item(self, board_id, item_id) -> Any:
        """
        Deletes a specific item from a board by its ID and returns a success status.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Items
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/items/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_item_position_or_parent(
        self, board_id, item_id, parent=None, position=None
    ) -> Any:
        """
        Partially updates an existing item on a board using the PATCH method, allowing for specific modifications to resource properties.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            parent (object): parent
            position (object): position
                Example:
                ```json
                {
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Items
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/items/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_within_frame(
        self,
        board_id_PlatformContainers,
        parent_item_id=None,
        limit=None,
        type=None,
        cursor=None,
    ) -> Any:
        """
        Retrieves a paginated list of items from a specified board, filtered by parent item ID and type, using cursor-based pagination.

        Args:
            board_id_PlatformContainers (string): board_id_PlatformContainers
            parent_item_id (string): (Required) ID of the frame for which you want to retrieve the list of available items.
            limit (string): The "limit" parameter specifies the maximum number of items to return in a single response for the specified board. Example: '10'.
            type (string): Specifies the type of items to retrieve within the board.
            cursor (string): A token representing the position in the dataset for paginated results, used to fetch subsequent pages of items.

        Returns:
            Any: API response data.

        Tags:
            Items
        """
        if board_id_PlatformContainers is None:
            raise ValueError("Missing required parameter 'board_id_PlatformContainers'")
        url = f"{self.base_url}/v2/boards/{board_id_PlatformContainers}/items"
        query_params = {
            k: v
            for k, v in [
                ("parent_item_id", parent_item_id),
                ("limit", limit),
                ("type", type),
                ("cursor", cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_item_on_board1(self, board_id, item_id) -> Any:
        """
        Retrieves a specific item from a board using the specified identifiers.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Flowchart shapes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/items/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_item1(self, board_id, item_id) -> Any:
        """
        Deletes a specific item from a Miro board using the "DELETE" method.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Items
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/items/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_board_members(self, board_id, limit=None, offset=None) -> Any:
        """
        Retrieves a paginated list of board members using query parameters for limit and offset, returning a 200 status on success.

        Args:
            board_id (string): board_id
            limit (string): Specifies the maximum number of member results to return in the response for the specified board.
            offset (string): The "offset" parameter specifies the starting point in the dataset, excluding the first N items from the response, allowing users to fetch subsequent pages of data.

        Returns:
            Any: API response data.

        Tags:
            Board Members
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/members"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def share_board(self, board_id, emails=None, message=None, role=None) -> Any:
        """
        Adds a new member to a board using the API at path "/v2/boards/{board_id}/members" and returns a successful status message upon completion.

        Args:
            board_id (string): board_id
            emails (array): emails Example: "['member@email.com']".
            message (string): message Example: "Hey there! Join my board and let's collaborate on this project!".
            role (string): role
                Example:
                ```json
                {
                  "emails": [
                    "member@email.com"
                  ],
                  "message": "Hey there! Join my board and let's collaborate on this project!",
                  "role": "commenter"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Board Members
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "emails": emails,
            "message": message,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/members"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_board_member(self, board_id, board_member_id) -> Any:
        """
        Retrieves information about a specific board member using the "GET" method, providing details associated with the member identified by `{board_member_id}` within the board identified by `{board_id}`.

        Args:
            board_id (string): board_id
            board_member_id (string): board_member_id

        Returns:
            Any: API response data.

        Tags:
            Board Members
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if board_member_id is None:
            raise ValueError("Missing required parameter 'board_member_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/members/{board_member_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_board_member(self, board_id, board_member_id) -> Any:
        """
        Removes a user from a board using the Miro API and returns a successful response upon completion.

        Args:
            board_id (string): board_id
            board_member_id (string): board_member_id

        Returns:
            Any: API response data.

        Tags:
            Board Members
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if board_member_id is None:
            raise ValueError("Missing required parameter 'board_member_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/members/{board_member_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_board_member(self, board_id, board_member_id, role=None) -> Any:
        """
        Updates a board member's details for the specified board using the PATCH method.

        Args:
            board_id (string): board_id
            board_member_id (string): board_member_id
            role (string): role
                Example:
                ```json
                {
                  "role": "commenter"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Board Members
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if board_member_id is None:
            raise ValueError("Missing required parameter 'board_member_id'")
        request_body = {
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/members/{board_member_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_shape_item(
        self, board_id, data=None, geometry=None, parent=None, position=None, style=None
    ) -> Any:
        """
        Creates a new shape on a specified board using the provided data.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "content": "Hello",
                    "shape": "rectangle"
                  },
                  "geometry": {
                    "height": 60,
                    "rotation": 0,
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "borderColor": "#1a1a1a",
                    "borderOpacity": "0.0",
                    "borderStyle": "normal",
                    "borderWidth": "1.0",
                    "color": "#1a1a1a",
                    "fillColor": "#8fd14f",
                    "fillOpacity": "1.0",
                    "fontFamily": "arial",
                    "fontSize": "12",
                    "textAlign": "left",
                    "textAlignVertical": "top"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Shapes
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/shapes"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_shape_item(self, board_id, item_id) -> Any:
        """
        Retrieves a specific shape from the specified board.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Shapes
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/shapes/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_shape_item(self, board_id, item_id) -> Any:
        """
        Deletes a specified shape from a board using the provided board and item identifiers.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Shapes
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/shapes/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_shape_item(
        self,
        board_id,
        item_id,
        data=None,
        geometry=None,
        parent=None,
        position=None,
        style=None,
    ) -> Any:
        """
        Updates a specific shape on a board by its ID and returns a success status.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "content": "Hello",
                    "shape": "rectangle"
                  },
                  "geometry": {
                    "height": 60,
                    "rotation": 0,
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "borderColor": "#1a1a1a",
                    "borderOpacity": "0.0",
                    "borderStyle": "normal",
                    "borderWidth": "1.0",
                    "color": "#1a1a1a",
                    "fillColor": "#8fd14f",
                    "fillOpacity": "1.0",
                    "fontFamily": "arial",
                    "fontSize": "12",
                    "textAlign": "left",
                    "textAlignVertical": "top"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Shapes
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/shapes/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_sticky_note_item(
        self, board_id, data=None, geometry=None, parent=None, position=None, style=None
    ) -> Any:
        """
        Creates a new sticky note on a specific board using the "POST" method and returns a successful status message when the operation is completed.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "content": "Hello",
                    "shape": "square"
                  },
                  "geometry": {
                    "height": 100,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "fillColor": "gray",
                    "textAlign": "left",
                    "textAlignVertical": "top"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Sticky Notes
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/sticky_notes"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sticky_note_item(self, board_id, item_id) -> Any:
        """
        Retrieves a specific sticky note from a board using the provided board and item IDs.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Sticky Notes
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/sticky_notes/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_sticky_note_item(self, board_id, item_id) -> Any:
        """
        Deletes a specific sticky note from a board using the DELETE method, returning a successful status message.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Sticky Notes
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/sticky_notes/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_sticky_note_item(
        self,
        board_id,
        item_id,
        data=None,
        geometry=None,
        parent=None,
        position=None,
        style=None,
    ) -> Any:
        """
        Updates a sticky note on the specified board using partial modifications and returns a success status.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "content": "Hello",
                    "shape": "square"
                  },
                  "geometry": {
                    "height": 100,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "fillColor": "gray",
                    "textAlign": "left",
                    "textAlignVertical": "top"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Sticky Notes
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/sticky_notes/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_text_item(
        self, board_id, data=None, geometry=None, parent=None, position=None, style=None
    ) -> Any:
        """
        Creates a new text entry on a specified board and returns a success status.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "content": "Hello"
                  },
                  "geometry": {
                    "rotation": 0,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "color": "#1a1a1a",
                    "fillColor": "#e6e6e6",
                    "fillOpacity": "1.0",
                    "fontFamily": "arial",
                    "fontSize": "12",
                    "textAlign": "left"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Texts
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/texts"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_text_item(self, board_id, item_id) -> Any:
        """
        Retrieves a specific text item from a board using the provided board and item identifiers.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Texts
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/texts/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_text_item(self, board_id, item_id) -> Any:
        """
        Deletes a specific text item from a board using the provided board and item identifiers.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Texts
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/texts/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_text_item(
        self,
        board_id,
        item_id,
        data=None,
        geometry=None,
        parent=None,
        position=None,
        style=None,
    ) -> Any:
        """
        Updates a specific text item on a board using the PATCH method, allowing partial modifications of the item's properties.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "content": "Hello"
                  },
                  "geometry": {
                    "rotation": 0,
                    "width": 100
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "color": "#1a1a1a",
                    "fillColor": "#e6e6e6",
                    "fillOpacity": "1.0",
                    "fontFamily": "arial",
                    "fontSize": "12",
                    "textAlign": "left"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Texts
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/texts/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_items_in_bulk(self, board_id, items=None) -> Any:
        """
        Bulk updates or creates items on a specified board using the API endpoint "/v2/boards/{board_id}/items/bulk" via the POST method.

        Args:
            board_id (string): board_id

        Returns:
            Any: API response data.

        Tags:
            Bulk operations
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        # Use items array directly as request body
        request_body = items
        url = f"{self.base_url}/v2/boards/{board_id}/items/bulk"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_frame(
        self, board_id, data=None, geometry=None, position=None, style=None
    ) -> Any:
        """
        Creates a new frame in the specified board using the API and returns a successful response.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "format": "custom",
                    "showContent": true,
                    "title": "Sample frame title",
                    "type": "freeform"
                  },
                  "geometry": {
                    "height": 100,
                    "width": 100
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "fillColor": "#ffffffff"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Frames
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/frames"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_frame(self, board_id, item_id) -> Any:
        """
        Retrieves the details of a specific frame within a board using the "GET" method.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Frames
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/frames/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_frame(self, board_id, item_id) -> Any:
        """
        Deletes a frame with the specified item ID from a board with the given board ID.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Frames
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/frames/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_frame(
        self, board_id, item_id, data=None, geometry=None, position=None, style=None
    ) -> Any:
        """
        Updates specific frame properties for a board using partial modifications and returns a success status.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "format": "custom",
                    "showContent": true,
                    "title": "Sample frame title",
                    "type": "freeform"
                  },
                  "geometry": {
                    "height": 100,
                    "width": 100
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "fillColor": "#ffffffff"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Frames
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/frames/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_app_metrics(self, app_id, startDate=None, endDate=None, period=None) -> Any:
        """
        Retrieves application metrics for a specified time period using the `startDate`, `endDate`, and `period` query parameters.

        Args:
            app_id (string): app_id
            startDate (string): (Required) Start date of the period in UTC format. For example, 2024-12-31. Example: '1978-06-11'.
            endDate (string): (Required) End date of the period in UTC format. For example, 2024-12-31. Example: '1978-06-11'.
            period (string): Group data by this time period. Example: 'WEEK'.

        Returns:
            Any: API response data.

        Tags:
            App metrics (experimental)
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'")
        url = f"{self.base_url}/v2-experimental/apps/{app_id}/metrics"
        query_params = {
            k: v
            for k, v in [
                ("startDate", startDate),
                ("endDate", endDate),
                ("period", period),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_total_app_metrics(self, app_id) -> Any:
        """
        Retrieves total metrics for a specified application by its ID.

        Args:
            app_id (string): app_id

        Returns:
            Any: API response data.

        Tags:
            App metrics (experimental)
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'")
        url = f"{self.base_url}/v2-experimental/apps/{app_id}/metrics-total"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_webhook_subscription(
        self, boardId=None, callbackUrl=None, status=None
    ) -> Any:
        """
        Creates a board subscription webhook and returns a success status upon configuration.

        Args:
            boardId (string): boardId Example: 'o9J_kzlUDmo='.
            callbackUrl (string): callbackUrl Example: 'https://yourwebhooklistener.com/v2/webhooks_endpoint'.
            status (string): status
                Example:
                ```json
                {
                  "boardId": "o9J_kzlUDmo=",
                  "callbackUrl": "https://yourwebhooklistener.com/v2/webhooks_endpoint",
                  "status": "enabled"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Webhooks (experimental)
        """
        request_body = {
            "boardId": boardId,
            "callbackUrl": callbackUrl,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2-experimental/webhooks/board_subscriptions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_webhook_subscription(
        self, subscription_id, callbackUrl=None, status=None
    ) -> Any:
        """
        Updates a webhook subscription for a board using the GitHub API and returns a success status.

        Args:
            subscription_id (string): subscription_id
            callbackUrl (string): callbackUrl Example: 'https://yourwebhooklistener.com/v2/webhooks_endpoint'.
            status (string): status
                Example:
                ```json
                {
                  "callbackUrl": "https://yourwebhooklistener.com/v2/webhooks_endpoint",
                  "status": "enabled"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Webhooks (experimental)
        """
        if subscription_id is None:
            raise ValueError("Missing required parameter 'subscription_id'")
        request_body = {
            "callbackUrl": callbackUrl,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2-experimental/webhooks/board_subscriptions/{subscription_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_subscriptions(self, limit=None, cursor=None) -> Any:
        """
        Retrieves a paginated list of webhook subscriptions using cursor-based pagination.

        Args:
            limit (string): The number of webhook subscriptions to return in the response. Example: '10'.
            cursor (string): A unique identifier used in cursor-based pagination to specify the starting point for retrieving the next set of webhook subscription records.

        Returns:
            Any: API response data.

        Tags:
            Webhooks (experimental)
        """
        url = f"{self.base_url}/v2-experimental/webhooks/subscriptions"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_webhook_subscription(self, subscription_id) -> Any:
        """
        Retrieves details about a specific webhook subscription identified by the provided subscription ID using the GET method.

        Args:
            subscription_id (string): subscription_id

        Returns:
            Any: API response data.

        Tags:
            Webhooks (experimental)
        """
        if subscription_id is None:
            raise ValueError("Missing required parameter 'subscription_id'")
        url = (
            f"{self.base_url}/v2-experimental/webhooks/subscriptions/{subscription_id}"
        )
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_webhook_subscription(self, subscription_id) -> Any:
        """
        Deletes a webhook subscription by a specified `subscription_id`, stopping the delivery of notifications associated with that subscription.

        Args:
            subscription_id (string): subscription_id

        Returns:
            Any: API response data.

        Tags:
            Webhooks (experimental)
        """
        if subscription_id is None:
            raise ValueError("Missing required parameter 'subscription_id'")
        url = (
            f"{self.base_url}/v2-experimental/webhooks/subscriptions/{subscription_id}"
        )
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_mind_map_node(self, board_id, item_id) -> Any:
        """
        Retrieves a specific mind map node by ID from a specified board using the GET method.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Mind map nodes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = (
            f"{self.base_url}/v2-experimental/boards/{board_id}/mindmap_nodes/{item_id}"
        )
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_mind_map_node(self, board_id, item_id) -> Any:
        """
        Deletes a specified mindmap node from a board using the experimental v2 API.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Mind map nodes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = (
            f"{self.base_url}/v2-experimental/boards/{board_id}/mindmap_nodes/{item_id}"
        )
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_mind_map_nodes(self, board_id, limit=None, cursor=None) -> Any:
        """
        Retrieves a paginated list of mindmap nodes from a specified Miro board, supporting limit and cursor parameters for result pagination.

        Args:
            board_id (string): board_id
            limit (string): Maximum number of results returned
            cursor (string): Points to the next portion of the results set

        Returns:
            Any: API response data.

        Tags:
            Mind map nodes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/mindmap_nodes"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_mind_map_node(
        self, board_id, data=None, geometry=None, parent=None, position=None
    ) -> Any:
        """
        Creates a new mind map node in a specified Miro board using the POST method and returns a response upon successful creation.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
                Example:
                ```json
                {
                  "data": {
                    "nodeView": {
                      "data": {
                        "value": "<Error: Too many levels of nesting to fake this schema>"
                      }
                    }
                  },
                  "geometry": {
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Mind map nodes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/mindmap_nodes"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_on_board1(self, board_id, limit=None, type=None, cursor=None) -> Any:
        """
        Retrieves a paginated list of items from a specified board, filtered by type and limited by cursor-based pagination.

        Args:
            board_id (string): board_id
            limit (string): Specifies the maximum number of items to return in a single response for the list of items on the specified board. Example: '10'.
            type (string): Specifies the type of items to retrieve from the board, such as "card", "task", or other supported item types. Example: 'shape'.
            cursor (string): Specifies a unique identifier or token used for cursor-based pagination to retrieve the next or previous page of items from the specified board.

        Returns:
            Any: API response data.

        Tags:
            Flowchart shapes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/items"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("type", type), ("cursor", cursor)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_shape_item1(
        self, board_id, data=None, geometry=None, parent=None, position=None, style=None
    ) -> Any:
        """
        Creates a new shape on a board with the specified `board_id` using the API.

        Args:
            board_id (string): board_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "content": "Hello",
                    "shape": "rectangle"
                  },
                  "geometry": {
                    "height": 60,
                    "rotation": 0,
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "borderColor": "#1a1a1a",
                    "borderOpacity": "0.0",
                    "borderStyle": "normal",
                    "borderWidth": "1.0",
                    "color": "#1a1a1a",
                    "fillColor": "#8fd14f",
                    "fillOpacity": "1.0",
                    "fontFamily": "arial",
                    "fontSize": "12",
                    "textAlign": "left",
                    "textAlignVertical": "top"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Flowchart shapes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/shapes"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_shape_item1(self, board_id, item_id) -> Any:
        """
        Retrieves shape details from a specific item within a board, identified by the board ID and item ID.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Flowchart shapes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/shapes/{item_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_shape_item1(self, board_id, item_id) -> Any:
        """
        Deletes a specific shape from the specified board.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Flowchart shapes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/shapes/{item_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_shape_item1(
        self,
        board_id,
        item_id,
        data=None,
        geometry=None,
        parent=None,
        position=None,
        style=None,
    ) -> Any:
        """
        Updates a specific shape on a board and returns a status message.

        Args:
            board_id (string): board_id
            item_id (string): item_id
            data (object): data
            geometry (object): geometry
            parent (object): parent
            position (object): position
            style (object): style
                Example:
                ```json
                {
                  "data": {
                    "content": "Hello",
                    "shape": "rectangle"
                  },
                  "geometry": {
                    "height": 60,
                    "rotation": 0,
                    "width": 320
                  },
                  "parent": {
                    "id": "null"
                  },
                  "position": {
                    "x": 100,
                    "y": 100
                  },
                  "style": {
                    "borderColor": "#1a1a1a",
                    "borderOpacity": "0.0",
                    "borderStyle": "normal",
                    "borderWidth": "1.0",
                    "color": "#1a1a1a",
                    "fillColor": "#8fd14f",
                    "fillOpacity": "1.0",
                    "fontFamily": "arial",
                    "fontSize": "12",
                    "textAlign": "left",
                    "textAlignVertical": "top"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Flowchart shapes (experimental)
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2-experimental/boards/{board_id}/shapes/{item_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_groups_on_aboard(self, board_id, limit=None, cursor=None) -> Any:
        """
        Retrieves a list of groups associated with a specified board, allowing for pagination with optional limit and cursor parameters.

        Args:
            board_id (string): board_id
            limit (string): The maximum number of items to return at one time, default is 10, maximum is 50. Example: '10'.
            cursor (string): A string token that determines the starting position for paginated results, allowing sequential retrieval of data chunks in subsequent requests.

        Returns:
            Any: API response data.

        Tags:
            Groups
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/groups"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_group(self, board_id, data=None) -> Any:
        """
        Creates a new group in the specified board using the provided board ID and returns a success status.

        Args:
            board_id (string): board_id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "items": [
                      "3458764517517852417",
                      "3458764517517852418"
                    ]
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Groups
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/groups"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_of_agroup_by_id(
        self, board_id, limit=None, cursor=None, group_item_id=None
    ) -> Any:
        """
        Retrieves a paginated list of group items for a specific board, optionally filtered by group item ID, with cursor-based pagination support.

        Args:
            board_id (string): board_id
            limit (string): The maximum number of items to return at one time, default is 10, maximum is 50. Example: '10'.
            cursor (string): A token used to paginate through results, where each request returns the next set of items after the specified cursor position.
            group_item_id (string): (Required) The ID of the group item to retrieve.

        Returns:
            Any: API response data.

        Tags:
            Groups
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/groups/items"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("cursor", cursor),
                ("group_item_id", group_item_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_agroup_by_its_id(self, board_id, group_id) -> Any:
        """
        Retrieves a group associated with a specific board from the API.

        Args:
            board_id (string): board_id
            group_id (string): group_id

        Returns:
            Any: API response data.

        Tags:
            Groups
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/groups/{group_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_agroup_with_new_items(self, board_id, group_id, data=None) -> Any:
        """
        Updates a group on a specific board using the provided group ID and board ID.

        Args:
            board_id (string): board_id
            group_id (string): group_id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "items": [
                      "3458764517517852417",
                      "3458764517517852418"
                    ]
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Groups
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/groups/{group_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def ungroup_items(self, board_id, group_id, delete_items=None) -> Any:
        """
        Deletes a group from a specified board using the DELETE method, optionally allowing for the deletion of associated items.

        Args:
            board_id (string): board_id
            group_id (string): group_id
            delete_items (string): Indicates whether the items should be removed. By default, false. Example: 'true'.

        Returns:
            Any: API response data.

        Tags:
            Groups
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if group_id is None:
            raise ValueError("Missing required parameter 'group_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/groups/{group_id}"
        query_params = {
            k: v for k, v in [("delete_items", delete_items)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_the_group(self, board_id, delete_items=None) -> Any:
        """
        Deletes a group from a specified board, with an option to delete associated items, and returns a success status.

        Args:
            board_id (string): board_id
             (string): No description provided. Example: 'null'.
            delete_items (string): (Required) Indicates whether the items should be removed. Set to `true` to delete items in the group. Example: 'true'.

        Returns:
            Any: API response data.

        Tags:
            Groups
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/groups/<string>"
        query_params = {
            k: v for k, v in [("delete_items", delete_items)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def revoke_token_v2(
        self, accessToken=None, clientId=None, clientSecret=None
    ) -> Any:
        """
        Revokes an OAuth 2.0 access or refresh token at the authorization server's revocation endpoint and returns a successful status upon invalidation.

        Args:
            accessToken (string): accessToken Example: '<Add your access token here>'.
            clientId (string): clientId Example: '<value>'.
            clientSecret (string): clientSecret
                Example:
                ```json
                {
                  "accessToken": "<Add your access token here>",
                  "clientId": "<value>",
                  "clientSecret": "<value>"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            OAuth
        """
        request_body = {
            "accessToken": accessToken,
            "clientId": clientId,
            "clientSecret": clientSecret,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/oauth/revoke"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_from_item(self, board_id, item_id) -> Any:
        """
        Retrieves tags associated with a specific item on a board using the API.

        Args:
            board_id (string): board_id
            item_id (string): item_id

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/items/{item_id}/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_from_board(self, board_id, limit=None, offset=None) -> Any:
        """
        Retrieves a list of tags associated with a specific board, allowing for pagination control via limit and offset parameters.

        Args:
            board_id (string): board_id
            limit (string): Specifies the maximum number of tags to return in the response for the given board.
            offset (string): Specifies the starting position in the collection of tags, indicating the number of items to skip before returning results.

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/tags"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag(self, board_id, fillColor=None, title=None) -> Any:
        """
        Creates and adds new tags to a specific board using the provided board ID.

        Args:
            board_id (string): board_id
            fillColor (string): fillColor Example: 'red'.
            title (string): title
                Example:
                ```json
                {
                  "fillColor": "red",
                  "title": "to do"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        request_body = {
            "fillColor": fillColor,
            "title": title,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/tags"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag(self, board_id, tag_id) -> Any:
        """
        Retrieves information about a specific tag associated with a board, identified by the board ID and tag ID, using the GET method.

        Args:
            board_id (string): board_id
            tag_id (string): tag_id

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if tag_id is None:
            raise ValueError("Missing required parameter 'tag_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/tags/{tag_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag(self, board_id, tag_id) -> Any:
        """
        Deletes a tag from a specific board using the API and returns a successful status message.

        Args:
            board_id (string): board_id
            tag_id (string): tag_id

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if tag_id is None:
            raise ValueError("Missing required parameter 'tag_id'")
        url = f"{self.base_url}/v2/boards/{board_id}/tags/{tag_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tag(self, board_id, tag_id, fillColor=None, title=None) -> Any:
        """
        Updates a tag associated with a specific board by modifying its details using the specified `board_id` and `tag_id`.

        Args:
            board_id (string): board_id
            tag_id (string): tag_id
            fillColor (string): fillColor Example: 'red'.
            title (string): title
                Example:
                ```json
                {
                  "fillColor": "red",
                  "title": "done"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id is None:
            raise ValueError("Missing required parameter 'board_id'")
        if tag_id is None:
            raise ValueError("Missing required parameter 'tag_id'")
        request_body = {
            "fillColor": fillColor,
            "title": title,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/boards/{board_id}/tags/{tag_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_by_tag(
        self, board_id_PlatformTags, limit=None, offset=None, tag_id=None
    ) -> Any:
        """
        Retrieves paginated items from a specific board's platform tags, optionally filtered by tag ID.

        Args:
            board_id_PlatformTags (string): board_id_PlatformTags
            limit (string): The `limit` query parameter specifies the maximum number of items to return in a single response page.
            offset (string): Specifies the starting position in the results to retrieve, excluding the first N items.
            tag_id (string): (Required) Unique identifier (ID) of the tag that you want to retrieve. Example: '{{tag_id}}'.

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id_PlatformTags is None:
            raise ValueError("Missing required parameter 'board_id_PlatformTags'")
        url = f"{self.base_url}/v2/boards/{board_id_PlatformTags}/items"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("offset", offset), ("tag_id", tag_id)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def attach_tag_to_item(self, board_id_PlatformTags, item_id, tag_id=None) -> Any:
        """
        Adds an item to a board with specific platform tags using the POST method, optionally specifying a tag ID in the query parameters.

        Args:
            board_id_PlatformTags (string): board_id_PlatformTags
            item_id (string): item_id
            tag_id (string): (Required) Unique identifier (ID) of the tag you want to add to the item. Example: '{{tag_id}}'.

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id_PlatformTags is None:
            raise ValueError("Missing required parameter 'board_id_PlatformTags'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id_PlatformTags}/items/{item_id}"
        query_params = {k: v for k, v in [("tag_id", tag_id)] if v is not None}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_item(self, board_id_PlatformTags, item_id, tag_id=None) -> Any:
        """
        Deletes a specific item from a board's PlatformTags collection, requiring a tag_id parameter for identification.

        Args:
            board_id_PlatformTags (string): board_id_PlatformTags
            item_id (string): item_id
            tag_id (string): (Required) Unique identifier (ID) of the tag that you want to remove from the item. Example: '{{tag_id}}'.

        Returns:
            Any: API response data.

        Tags:
            Tags
        """
        if board_id_PlatformTags is None:
            raise ValueError("Missing required parameter 'board_id_PlatformTags'")
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'")
        url = f"{self.base_url}/v2/boards/{board_id_PlatformTags}/items/{item_id}"
        query_params = {k: v for k, v in [("tag_id", tag_id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_of_projects(self, org_id, team_id, limit=None, cursor=None) -> Any:
        """
        Retrieves a list of projects for a specified team within an organization, allowing pagination via limit and cursor parameters.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            limit (string): The maximum number of results to return per call. If the number of projects in the response is greater than the limit specified, the response returns the cursor parameter with a value. Example: '100'.
            cursor (string): An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request. Example: '3074457345618265000'.

        Returns:
            Any: API response data.

        Tags:
            Projects
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_project(self, org_id, team_id, name=None) -> Any:
        """
        Assigns a project to a team within an organization using a POST request and returns a success status upon completion.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            name (string): name
                Example:
                ```json
                {
                  "name": "My project"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Projects
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_project(self, org_id, team_id, project_id) -> Any:
        """
        Retrieves project details for a specific team within an organization.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id

        Returns:
            Any: API response data.

        Tags:
            Projects
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_project(self, org_id, team_id, project_id) -> Any:
        """
        Deletes a specific organization's team project and returns a success message upon removal.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id

        Returns:
            Any: API response data.

        Tags:
            Projects
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_project(self, org_id, team_id, project_id, name=None) -> Any:
        """
        Updates project details within the specified team and organization using the PATCH method and returns a successful response upon completion.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id
            name (string): name
                Example:
                ```json
                {
                  "name": "My project"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Projects
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_project_settings(self, org_id, team_id, project_id) -> Any:
        """
        Retrieves the settings for a specified organization's team project.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id

        Returns:
            Any: API response data.

        Tags:
            Project Settings
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}/settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_project_settings(
        self, org_id, team_id, project_id, sharingPolicySettings=None
    ) -> Any:
        """
        Updates organization, team, and project settings for the specified project.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id
            sharingPolicySettings (object): sharingPolicySettings
                Example:
                ```json
                {
                  "sharingPolicySettings": {
                    "teamAccess": "private"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Project Settings
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "sharingPolicySettings": sharingPolicySettings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}/settings"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_of_project_members(
        self, org_id, team_id, project_id, limit=None, cursor=None
    ) -> Any:
        """
        Retrieves a list of members in a specific project within a team for an organization using the provided limit and cursor query parameters.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id
            limit (string): The maximum number of results to return per call. If the number of project members in the response is greater than the limit specified, the response returns the cursor parameter with a value. Example: '100'.
            cursor (string): An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request. Example: '3074457345618265000'.

        Returns:
            Any: API response data.

        Tags:
            Project Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}/members"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_member_in_aproject(
        self, org_id, team_id, project_id, email=None, role=None
    ) -> Any:
        """
        Adds a member to a specified project within a team and organization.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id
            email (string): email Example: 'someone@domain.com'.
            role (string): role
                Example:
                ```json
                {
                  "email": "someone@domain.com",
                  "role": "viewer"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Project Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "email": email,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}/members"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_project_member(self, org_id, team_id, project_id, member_id) -> Any:
        """
        Retrieves a specific member's details from a project team within an organization.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id
            member_id (string): member_id

        Returns:
            Any: API response data.

        Tags:
            Project Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}/members/{member_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_project_member(self, org_id, team_id, project_id, member_id) -> Any:
        """
        Deletes a member from a specific project within a team in an organization using the provided member ID.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id
            member_id (string): member_id

        Returns:
            Any: API response data.

        Tags:
            Project Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}/members/{member_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_project_member(
        self, org_id, team_id, project_id, member_id, role=None
    ) -> Any:
        """
        Updates team member information in an organization project using the "PATCH" method and returns a successful status response.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            project_id (string): project_id
            member_id (string): member_id
            role (string): role
                Example:
                ```json
                {
                  "role": "viewer"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Project Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        request_body = {
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/projects/{project_id}/members/{member_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_teams(self, org_id, limit=None, cursor=None, name=None) -> Any:
        """
        Retrieves a paginated list of teams for a specified organization with optional filtering by name.

        Args:
            org_id (string): org_id
            limit (string): Specifies the maximum number of teams to return in a single response. Example: '100'.
            cursor (string): An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request. Example: '3055557345821140500'.
            name (string): Name query. Filters teams by name using case insensitive partial match. A value "dev" will return both "Developer's team" and "Team for developers". Example: 'My team'.

        Returns:
            Any: API response data.

        Tags:
            Teams
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("cursor", cursor), ("name", name)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_team(self, org_id, name=None) -> Any:
        """
        Creates a new team within the specified organization using the POST method.

        Args:
            org_id (string): org_id
            name (string): name
                Example:
                ```json
                {
                  "name": "My Team"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Teams, important
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team(self, org_id, team_id) -> Any:
        """
        Retrieves team details for the specified organization and team ID.

        Args:
            org_id (string): org_id
            team_id (string): team_id

        Returns:
            Any: API response data.

        Tags:
            Teams, important
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_team(self, org_id, team_id) -> Any:
        """
        Deletes a team within an organization using the specified organization and team IDs.

        Args:
            org_id (string): org_id
            team_id (string): team_id

        Returns:
            Any: API response data.

        Tags:
            Teams, important
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_team(self, org_id, team_id, name=None) -> Any:
        """
        Updates specific properties of a team within an organization using partial modifications.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            name (string): name
                Example:
                ```json
                {
                  "name": "My Team"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Teams, important
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_team_members(
        self, org_id, team_id, limit=None, cursor=None, role=None
    ) -> Any:
        """
        Retrieves a paginated list of members for a specified team within an organization, optionally filtered by role.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            limit (string): The "limit" parameter specifies the maximum number of team members to return in a single response for the specified organization and team. Example: '100'.
            cursor (string): An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request. Example: '3055557345821140500'.
            role (string): Role query. Filters members by role using full word match. Accepted values are:
        * "member": Team member with full member permissions.
        * "admin": Admin of a team. Team member with permission to manage team.
        * "non_team": External user, non-team user.
        * "team_guest": Team-guest user, user with access only to a team without access to organization.

        Returns:
            Any: API response data.

        Tags:
            Team Members, important
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/members"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("cursor", cursor), ("role", role)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def invite_team_members(self, org_id, team_id, email=None, role=None) -> Any:
        """
        Adds a member to a specific team within an organization using the API endpoint at "/v2/orgs/{org_id}/teams/{team_id}/members".

        Args:
            org_id (string): org_id
            team_id (string): team_id
            email (string): email Example: 'user@miro.com'.
            role (string): role
                Example:
                ```json
                {
                  "email": "user@miro.com",
                  "role": "member"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Team Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        request_body = {
            "email": email,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/members"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_member(self, org_id, team_id, member_id) -> Any:
        """
        Retrieves information about a specific team member using the provided organization, team, and member identifiers.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            member_id (string): member_id

        Returns:
            Any: API response data.

        Tags:
            Team Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/members/{member_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_team_member_from_team(self, org_id, team_id, member_id) -> Any:
        """
        Removes a member from a specified team in an organization using the GitHub API.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            member_id (string): member_id

        Returns:
            Any: API response data.

        Tags:
            Team Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/members/{member_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_team_member(self, org_id, team_id, member_id, role=None) -> Any:
        """
        Updates the membership details of a team member in an organization using the GitHub API.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            member_id (string): member_id
            role (string): role
                Example:
                ```json
                {
                  "role": "member"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Team Members
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        request_body = {
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/members/{member_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_default_team_settings(self, org_id) -> Any:
        """
        Retrieves the default team settings for an organization via the GitHub API.

        Args:
            org_id (string): org_id

        Returns:
            Any: API response data.

        Tags:
            Team Settings
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/default_teams_settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_settings1(self, org_id, team_id) -> Any:
        """
        Retrieves team settings for a specified team within an organization using the "GET" method.

        Args:
            org_id (string): org_id
            team_id (string): team_id

        Returns:
            Any: API response data.

        Tags:
            Team Settings
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_team_settings1(
        self,
        org_id,
        team_id,
        teamAccountDiscoverySettings=None,
        teamCollaborationSettings=None,
        teamCopyAccessLevelSettings=None,
        teamInvitationSettings=None,
        teamSharingPolicySettings=None,
    ) -> Any:
        """
        Updates settings for a team within an organization using the GitHub API and returns a status message.

        Args:
            org_id (string): org_id
            team_id (string): team_id
            teamAccountDiscoverySettings (object): teamAccountDiscoverySettings
            teamCollaborationSettings (object): teamCollaborationSettings
            teamCopyAccessLevelSettings (object): teamCopyAccessLevelSettings
            teamInvitationSettings (object): teamInvitationSettings
            teamSharingPolicySettings (object): teamSharingPolicySettings
                Example:
                ```json
                {
                  "teamAccountDiscoverySettings": {
                    "accountDiscovery": "hidden"
                  },
                  "teamCollaborationSettings": {
                    "coOwnerRole": "enabled"
                  },
                  "teamCopyAccessLevelSettings": {
                    "copyAccessLevel": "anyone",
                    "copyAccessLevelLimitation": "anyone"
                  },
                  "teamInvitationSettings": {
                    "inviteExternalUsers": "allowed",
                    "whoCanInvite": "only_org_admins"
                  },
                  "teamSharingPolicySettings": {
                    "allowListedDomains": [
                      "mollit id",
                      "irure id pariatur reprehenderit"
                    ],
                    "createAssetAccessLevel": "company_admins",
                    "defaultBoardAccess": "private",
                    "defaultBoardSharingAccess": "team_members_with_editing_rights",
                    "defaultOrganizationAccess": "private",
                    "defaultProjectAccess": "private",
                    "moveBoardToAccount": "allowed",
                    "restrictAllowedDomains": "enabled",
                    "sharingOnAccount": "allowed",
                    "sharingOnOrganization": "allowed",
                    "sharingViaPublicLink": "allowed"
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Team Settings
        """
        if org_id is None:
            raise ValueError("Missing required parameter 'org_id'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        request_body = {
            "teamAccountDiscoverySettings": teamAccountDiscoverySettings,
            "teamCollaborationSettings": teamCollaborationSettings,
            "teamCopyAccessLevelSettings": teamCopyAccessLevelSettings,
            "teamInvitationSettings": teamInvitationSettings,
            "teamSharingPolicySettings": teamSharingPolicySettings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/orgs/{org_id}/teams/{team_id}/settings"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.revoke_token_v1,
            self.get_access_token_information,
            self.get_audit_logs,
            self.get_organization_settings,
            self.bulk_update_boards_classification,
            self.get_team_settings,
            self.update_team_settings,
            self.get_board_classification,
            self.update_board_classification,
            self.get_all_cases,
            self.get_case,
            self.get_all_legal_holds_within_acase,
            self.get_legal_hold_information,
            self.get_content_items_under_legal_hold,
            self.create_board_export_job,
            self.get_board_export_job_status,
            self.get_results_for_board_export_job,
            self.retrieve_content_change_logs_of_board_items,
            self.reset_all_sessions_of_auser,
            self.get_organization_info,
            self.get_organization_members,
            self.get_organization_member,
            self.get_boards,
            self.copy_board,
            self.create_board,
            self.get_specific_board,
            self.delete_board,
            self.update_board,
            self.create_app_card_item,
            self.get_app_card_item,
            self.delete_app_card_item,
            self.update_app_card_item,
            self.create_card_item,
            self.get_card_item,
            self.delete_card_item,
            self.update_card_item,
            self.get_connectors,
            self.create_connector,
            self.get_specific_connector,
            self.delete_connector,
            self.update_connector,
            self.create_document_item_using_url,
            self.get_document_item,
            self.delete_document_item,
            self.update_document_item_using_url,
            self.create_embed_item,
            self.get_embed_item,
            self.delete_embed_item,
            self.update_embed_item,
            self.create_image_item_using_url,
            self.get_image_item,
            self.delete_image_item,
            self.update_image_item_using_url,
            self.get_items_on_board,
            self.get_specific_item_on_board,
            self.delete_item,
            self.update_item_position_or_parent,
            self.get_items_within_frame,
            self.get_specific_item_on_board1,
            self.delete_item1,
            self.get_all_board_members,
            self.share_board,
            self.get_specific_board_member,
            self.remove_board_member,
            self.update_board_member,
            self.create_shape_item,
            self.get_shape_item,
            self.delete_shape_item,
            self.update_shape_item,
            self.create_sticky_note_item,
            self.get_sticky_note_item,
            self.delete_sticky_note_item,
            self.update_sticky_note_item,
            self.create_text_item,
            self.get_text_item,
            self.delete_text_item,
            self.update_text_item,
            self.create_items_in_bulk,
            self.create_frame,
            self.get_frame,
            self.delete_frame,
            self.update_frame,
            self.get_app_metrics,
            self.get_total_app_metrics,
            self.create_webhook_subscription,
            self.update_webhook_subscription,
            self.get_webhook_subscriptions,
            self.get_specific_webhook_subscription,
            self.delete_webhook_subscription,
            self.get_specific_mind_map_node,
            self.delete_mind_map_node,
            self.get_mind_map_nodes,
            self.create_mind_map_node,
            self.get_items_on_board1,
            self.create_shape_item1,
            self.get_shape_item1,
            self.delete_shape_item1,
            self.update_shape_item1,
            self.get_all_groups_on_aboard,
            self.create_group,
            self.get_items_of_agroup_by_id,
            self.get_agroup_by_its_id,
            self.updates_agroup_with_new_items,
            self.ungroup_items,
            self.deletes_the_group,
            self.revoke_token_v2,
            self.get_tags_from_item,
            self.get_tags_from_board,
            self.create_tag,
            self.get_tag,
            self.delete_tag,
            self.update_tag,
            self.get_items_by_tag,
            self.attach_tag_to_item,
            self.remove_tag_from_item,
            self.list_of_projects,
            self.create_project,
            self.get_project,
            self.delete_project,
            self.update_project,
            self.get_project_settings,
            self.update_project_settings,
            self.list_of_project_members,
            self.add_member_in_aproject,
            self.get_project_member,
            self.remove_project_member,
            self.update_project_member,
            self.list_teams,
            self.create_team,
            self.get_team,
            self.delete_team,
            self.update_team,
            self.list_team_members,
            self.invite_team_members,
            self.get_team_member,
            self.delete_team_member_from_team,
            self.update_team_member,
            self.get_default_team_settings,
            self.get_team_settings1,
            self.update_team_settings1,
        ]
