from datetime import UTC, datetime
from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class CrmApi:
    def __init__(self, api_client):
        pass

    def list_tools(self):
        return []


class MarketingApi:
    def __init__(self, api_client):
        pass

    def list_tools(self):
        return []


class HubspotApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="hubspot", integration=integration, **kwargs)
        self.base_url = "https://api.hubapi.com"
        self.crm = CrmApi(self)
        self.marketing = MarketingApi(self)

    def add_a_note(
        self,
        hs_note_body: str,
        hs_timestamp: str | None = None,
        associations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Create a note in HubSpot with the given properties and associations.

        Args:
            hs_note_body (str): The body/content of the note
            hs_timestamp (Optional[str]): Timestamp for the note (ISO format). If not provided, current time will be used.
            associations (Optional[List[dict[str, Any]]]): List of associations to other objects. Exmaple: To add notes to contact [{"to": {"id": "101"}, "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 202}]}], to add notes to company [{"to": {"id": "101"}, "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 190}]}]

        Returns:
            dict[str, Any]: The created note object with ID

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Notes, CRM, important
        """
        if hs_note_body is None:
            raise ValueError("Missing required parameter 'hs_note_body'.")

        url = f"{self.base_url}/crm/v3/objects/notes"

        # Build the properties object
        properties = {
            "hs_note_body": hs_note_body,
            "hs_timestamp": hs_timestamp
            if hs_timestamp
            else datetime.now(UTC).isoformat(),
        }

        # Build the request body
        request_body_data: dict[str, Any] = {"properties": properties}

        # Add associations if provided
        if associations:
            request_body_data["associations"] = associations

        response = self._post(url, data=request_body_data)
        return self._handle_response(response)

    def fetch_multiple_lists(
        self, listIds: list[str] | None = None, includeFilters: bool | None = None
    ) -> dict[str, Any]:
        """
        Fetch multiple lists in a single request by ILS list ID. The response will include the definitions of all lists that exist for the listIds provided.

        Args:
            listIds (array): The **ILS IDs** of the lists to fetch.
            includeFilters (boolean): A flag indicating whether or not the response object list definitions should include a filter branch definition. By default, object list definitions will not have their filter branch definitions included in the response.

        Returns:
            dict[str, Any]: Successful response, for a request with `includeFilters` set to `true`.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists
        """
        url = f"{self.base_url}/crm/v3/lists/"
        query_params = {
            k: v
            for k, v in [("listIds", listIds), ("includeFilters", includeFilters)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def fetch_list_memberships(
        self,
        listId: str,
        after: str | None = None,
        before: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Fetch the memberships of a list in order sorted by the recordId of the records in the list.

        Args:
            listId (str): The ILS ID of the list
            after (Optional[str]): The paging offset token for the page that comes after the previously requested records
            before (Optional[str]): The paging offset token for the page that comes before the previously requested records
            limit (Optional[int]): The number of records to return in the response (max 250)

        Returns:
            dict[str, Any]: List memberships ordered by recordId

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists, CRM
        """
        if listId is None:
            raise ValueError("Missing required parameter 'listId'.")

        url = f"{self.base_url}/crm/v3/lists/{listId}/memberships"
        query_params = {}

        if after is not None:
            query_params["after"] = after
        if before is not None:
            query_params["before"] = before
        if limit is not None:
            query_params["limit"] = limit

        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_list(
        self,
        objectTypeId: str,
        processingType: str,
        name: str,
        membershipSettings: dict[str, Any] | None = None,
        customProperties: dict[str, str] | None = None,
        listFolderId: int | None = None,
        listPermissions: dict[str, Any] | None = None,
        filterBranch: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create a new list in HubSpot with the specified object type, processing type, and name.
        Optionally use this to provide membership settings, custom properties, a folder ID, list permissions,
        and a filter branch to further configure the list.

        Args:
            objectTypeId (string): The object type ID of the type of objects that the list will store. Example: '0-1'.
            processingType (string): The processing type of the list. One of: `SNAPSHOT`, `MANUAL`, or `DYNAMIC`. Example: 'DYNAMIC'.
            name (string): The name of the list, which must be globally unique across all public lists in the portal. Example: 'Dynamic Association List Example'.
            membershipSettings (object): membershipSettings
            customProperties (object): The list of custom properties to tie to the list. Custom property name is the key, the value is the value.
            listFolderId (integer): The ID of the folder that the list should be created in. If left blank, then the list will be created in the root of the list folder structure.
            listPermissions (object): listPermissions
            filterBranch (string): filterBranch Example: {'filterBranchType': 'OR', 'filterBranches': [{'filterBranchType': 'AND', 'filterBranches': [{'associationCategory': 'HUBSPOT_DEFINED', 'associationTypeId': 4, 'filterBranchType': 'ASSOCIATION', 'filters': [{'filterType': 'PROPERTY', 'operation': {'operationType': 'BOOL', 'operator': 'IS_EQUAL_TO', 'value': True}, 'property': 'hs_is_closed_won'}], 'objectTypeId': '0-3', 'operator': 'IN_LIST'}], 'filters': [{'filterType': 'PROPERTY', 'operation': {'operationType': 'MULTISTRING', 'operator': 'IS_EQUAL_TO', 'values': ['test', 'name']}, 'property': 'firstname'}]}]}.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists, CRM
        """
        request_body_data = None
        request_body_data = {
            "membershipSettings": membershipSettings,
            "objectTypeId": objectTypeId,
            "processingType": processingType,
            "customProperties": customProperties,
            "listFolderId": listFolderId,
            "name": name,
            "listPermissions": listPermissions,
            "filterBranch": filterBranch,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/crm/v3/lists/"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_list_by_id(
        self, listId: str, includeFilters: bool | None = None
    ) -> dict[str, Any]:
        """
        Fetch a single list by ILS list ID.

        Args:
            listId (string): listId
            includeFilters (boolean): A flag indicating whether or not the response object list definition should include a filter branch definition. By default, object list definitions will not have their filter branch definitions included in the response.

        Returns:
            dict[str, Any]: Successful response, for a request with `includeFilters` set to `true`.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists, CRM
        """
        if listId is None:
            raise ValueError("Missing required parameter 'listId'.")
        url = f"{self.base_url}/crm/v3/lists/{listId}"
        query_params = {
            k: v for k, v in [("includeFilters", includeFilters)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_list_by_id(self, listId: str) -> Any:
        """
        Delete a list by ILS list ID. Lists deleted through this endpoint can be restored for up to 90 days. After 90 days, the list is permanently purged and cannot be restored

        Args:
            listId (string): listId

        Returns:
            Any: No content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists, CRM
        """
        if listId is None:
            raise ValueError("Missing required parameter 'listId'.")
        url = f"{self.base_url}/crm/v3/lists/{listId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def add_records_to_list(self, listId: str, items: list[str]) -> dict[str, Any]:
        """
        Add the records provided to the list. Records that do not exist or that are already members of the list are ignored.
        This only works for lists that have a processingType of MANUAL or SNAPSHOT.

        Args:
            listId (string): listId
            items (array): The **ILS IDs** of the records to add to the list.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Memberships, Lists
        """
        if listId is None:
            raise ValueError("Missing required parameter 'listId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/crm/v3/lists/{listId}/memberships/add"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def remove_records_from_list(self, listId: str, items: list[str]) -> dict[str, Any]:
        """
        Remove the records provided from the list. Records that are not members of the list are ignored.
        This only works for lists that have a processingType of MANUAL or SNAPSHOT.

        Args:
            listId (string): listId
            items (array): The **ILS IDs** of the records to remove from the list.

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Memberships, Lists
        """
        if listId is None:
            raise ValueError("Missing required parameter 'listId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/crm/v3/lists/{listId}/memberships/remove"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search_lists(
        self,
        listIds: list[str] | None = None,
        offset: int | None = None,
        query: str | None = None,
        count: int | None = None,
        processingTypes: list[str] | None = None,
        additionalProperties: list[str] | None = None,
        sort: str | None = None,
    ) -> dict[str, Any]:
        """
        Search lists by list name or page through all lists by providing an empty query value.

        Args:
            listIds (array): The `listIds` that will be used to filter results by `listId`. If values are provided, then the response will only include results that have a `listId` in this array.

        If no value is provided, or if an empty list is provided, then the results will not be filtered by `listId`.
            offset (integer): Value used to paginate through lists. The `offset` provided in the response can be used in the next request to fetch the next page of results. Defaults to `0` if no offset is provided. Example: 0.
            query (string): The `query` that will be used to search for lists by list name. If no `query` is provided, then the results will include all lists. Example: 'Test'.
            count (integer): The number of lists to include in the response. Defaults to `20` if no value is provided. The max `count` is `500`. Example: 100.
            processingTypes (array): The `processingTypes` that will be used to filter results by `processingType`. If values are provided, then the response will only include results that have a `processingType` in this array.

        If no value is provided, or if an empty list is provided, then results will not be filtered by `processingType`.

        Valid `processingTypes` are: `MANUAL`, `SNAPSHOT`, or `DYNAMIC`.
            additionalProperties (array): The property names of any additional list properties to include in the response. Properties that do not exist or that are empty for a particular list are not included in the response.

        By default, all requests will fetch the following properties for each list: `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`, `hs_folder_name`, and `hs_list_reference_count`. Example: ['hs_list_size_week_delta'].
            sort (string): sort

        Returns:
            dict[str, Any]: Successful response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists, CRM
        """
        request_body_data = None
        request_body_data = {
            "listIds": listIds,
            "offset": offset,
            "query": query,
            "count": count,
            "processingTypes": processingTypes,
            "additionalProperties": additionalProperties,
            "sort": sort,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/crm/v3/lists/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def fetch_list_by_name(
        self, objectTypeId: str, listName: str, includeFilters: bool | None = None
    ) -> dict[str, Any]:
        """
        Fetch a list by its name and object type ID.

        Args:
            objectTypeId (string): objectTypeId
            listName (string): listName
            includeFilters (boolean): A flag indicating whether or not the response object list definition should include a filter branch definition. By default, object list definitions will not have their filter branch definitions included in the response.

        Returns:
            dict[str, Any]: Successful response, for a request with `includeFilters` set to `false`.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists, CRM
        """
        if objectTypeId is None:
            raise ValueError("Missing required parameter 'objectTypeId'.")
        if listName is None:
            raise ValueError("Missing required parameter 'listName'.")
        url = f"{self.base_url}/crm/v3/lists/object-type-id/{objectTypeId}/name/{listName}"
        query_params = {
            k: v for k, v in [("includeFilters", includeFilters)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        all_tools = [
            self.add_a_note,
            self.fetch_multiple_lists,
            self.fetch_list_memberships,
            self.create_list,
            self.get_list_by_id,
            self.delete_list_by_id,
            self.add_records_to_list,
            self.remove_records_from_list,
            self.search_lists,
            self.fetch_list_by_name,
        ]
        all_tools.extend(self.crm.list_tools())
        all_tools.extend(self.marketing.list_tools())
        return all_tools
