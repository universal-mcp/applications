from typing import Any, Optional, List
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration
from .schemas import *


class AttioApp(APIApplication):
    def __init__(self, integration: Integration, **kwargs) -> None:
        super().__init__(name="attio", integration=integration, **kwargs)
        self.base_url = "https://api.attio.com"

    def get_v2_objects(self) -> Getobjectsresponse:
        """
        List objects

        Returns:
            Getobjectsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Objects
        """
        url = f"{self.base_url}/v2/objects"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getobjectsresponse.model_validate(self._handle_response(response))

    def post_v2_objects(self, data: dict[str, Any]) -> Postobjectsresponse:
        """
        Create an object

        Args:
            data (object): data

        Returns:
            Postobjectsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Objects
        """
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/objects"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postobjectsresponse.model_validate(self._handle_response(response))

    def get_v2_objects_by_object(self, object: str) -> Postobjectsresponse:
        """
        Get an object

        Args:
            object (string): object

        Returns:
            Postobjectsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Objects
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        url = f"{self.base_url}/v2/objects/{object}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Postobjectsresponse.model_validate(self._handle_response(response))

    def patch_v2_objects_by_object(
        self, object: str, data: dict[str, Any]
    ) -> Postobjectsresponse:
        """
        Update an object

        Args:
            object (string): object
            data (object): data

        Returns:
            Postobjectsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Objects
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/objects/{object}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Postobjectsresponse.model_validate(self._handle_response(response))

    def get_v2_by_target_by_identifier_attributes(
        self,
        target: str,
        identifier: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        show_archived: Optional[bool] = None,
    ) -> Getattributesresponse:
        """
        List attributes

        Args:
            target (string): target
            identifier (string): identifier
            limit (integer): No description provided. Example: '10'.
            offset (integer): No description provided. Example: '5'.
            show_archived (boolean): No description provided. Example: 'True'.

        Returns:
            Getattributesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        url = f"{self.base_url}/v2/{target}/{identifier}/attributes"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("show_archived", show_archived),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Getattributesresponse.model_validate(self._handle_response(response))

    def post_v2_by_target_by_identifier_attributes(
        self, target: str, identifier: str, data: dict[str, Any]
    ) -> Postattributesresponse:
        """
        Create an attribute

        Args:
            target (string): target
            identifier (string): identifier
            data (object): data

        Returns:
            Postattributesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/{target}/{identifier}/attributes"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postattributesresponse.model_validate(self._handle_response(response))

    def get_v2_by_target_by_identifier_attributes_by_attribute(
        self, target: str, identifier: str, attribute: str
    ) -> Postattributesresponse:
        """
        Get an attribute

        Args:
            target (string): target
            identifier (string): identifier
            attribute (string): attribute

        Returns:
            Postattributesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        url = f"{self.base_url}/v2/{target}/{identifier}/attributes/{attribute}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Postattributesresponse.model_validate(self._handle_response(response))

    def patch_v2_by_target_by_identifier_attributes_by_attribute(
        self, target: str, identifier: str, attribute: str, data: dict[str, Any]
    ) -> Postattributesresponse:
        """
        Update an attribute

        Args:
            target (string): target
            identifier (string): identifier
            attribute (string): attribute
            data (object): data

        Returns:
            Postattributesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/{target}/{identifier}/attributes/{attribute}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Postattributesresponse.model_validate(self._handle_response(response))

    def get_v2_by_target_by_identifier_attributes_by_attribute_options(
        self,
        target: str,
        identifier: str,
        attribute: str,
        show_archived: Optional[bool] = None,
    ) -> Getoptionsresponse:
        """
        List select options

        Args:
            target (string): target
            identifier (string): identifier
            attribute (string): attribute
            show_archived (boolean): No description provided. Example: 'True'.

        Returns:
            Getoptionsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        url = f"{self.base_url}/v2/{target}/{identifier}/attributes/{attribute}/options"
        query_params = {
            k: v for k, v in [("show_archived", show_archived)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Getoptionsresponse.model_validate(self._handle_response(response))

    def post_v2_by_target_by_identifier_attributes_by_attribute_options(
        self, target: str, identifier: str, attribute: str, data: dict[str, Any]
    ) -> Postoptionsresponse:
        """
        Create a select option

        Args:
            target (string): target
            identifier (string): identifier
            attribute (string): attribute
            data (object): data

        Returns:
            Postoptionsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/{target}/{identifier}/attributes/{attribute}/options"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postoptionsresponse.model_validate(self._handle_response(response))

    def patch_v2_by_target_by_identifier_attributes_by_attribute_options_by_option(
        self,
        target: str,
        identifier: str,
        attribute: str,
        option: str,
        data: dict[str, Any],
    ) -> Postoptionsresponse:
        """
        Update a select option

        Args:
            target (string): target
            identifier (string): identifier
            attribute (string): attribute
            option (string): option
            data (object): data

        Returns:
            Postoptionsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        if option is None:
            raise ValueError("Missing required parameter 'option'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/{target}/{identifier}/attributes/{attribute}/options/{option}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Postoptionsresponse.model_validate(self._handle_response(response))

    def get_v2_by_target_by_identifier_attributes_by_attribute_statuses(
        self,
        target: str,
        identifier: str,
        attribute: str,
        show_archived: Optional[bool] = None,
    ) -> Getstatusesresponse:
        """
        List statuses

        Args:
            target (string): target
            identifier (string): identifier
            attribute (string): attribute
            show_archived (boolean): No description provided. Example: 'True'.

        Returns:
            Getstatusesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        url = (
            f"{self.base_url}/v2/{target}/{identifier}/attributes/{attribute}/statuses"
        )
        query_params = {
            k: v for k, v in [("show_archived", show_archived)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Getstatusesresponse.model_validate(self._handle_response(response))

    def post_v2_by_target_by_identifier_attributes_by_attribute_statuses(
        self, target: str, identifier: str, attribute: str, data: dict[str, Any]
    ) -> Poststatusesresponse:
        """
        Create a status

        Args:
            target (string): target
            identifier (string): identifier
            attribute (string): attribute
            data (object): data

        Returns:
            Poststatusesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.base_url}/v2/{target}/{identifier}/attributes/{attribute}/statuses"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Poststatusesresponse.model_validate(self._handle_response(response))

    def patch_v2_by_target_by_identifier_attributes_by_attribute_statuses_by_status(
        self,
        target: str,
        identifier: str,
        attribute: str,
        status: str,
        data: dict[str, Any],
    ) -> Poststatusesresponse:
        """
        Update a status

        Args:
            target (string): target
            identifier (string): identifier
            attribute (string): attribute
            status (string): status
            data (object): data

        Returns:
            Poststatusesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Attributes
        """
        if target is None:
            raise ValueError("Missing required parameter 'target'.")
        if identifier is None:
            raise ValueError("Missing required parameter 'identifier'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        if status is None:
            raise ValueError("Missing required parameter 'status'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/{target}/{identifier}/attributes/{attribute}/statuses/{status}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Poststatusesresponse.model_validate(self._handle_response(response))

    def post_v2_objects_by_object_records_query(
        self,
        object: str,
        filter: Optional[dict[str, Any]] = None,
        sorts: Optional[List[Any]] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
    ) -> Postqueryresponse:
        """
        List records

        Args:
            object (string): object
            filter (object): An object used to filter results to a subset of results. See the [full guide to filtering and sorting here](/rest-api/how-to/filtering-and-sorting). Example: "{'name': 'Ada Lovelace'}".
            sorts (array): An object used to sort results. See the [full guide to filtering and sorting here](/rest-api/how-to/filtering-and-sorting). Example: "[{'direction': 'asc', 'attribute': 'name', 'field': 'last_name'}]".
            limit (number): The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/rest-api/how-to/pagination). Example: '500'.
            offset (number): The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/rest-api/how-to/pagination). Example: '0'.

        Returns:
            Postqueryresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        request_body_data = None
        request_body_data = {
            "filter": filter,
            "sorts": sorts,
            "limit": limit,
            "offset": offset,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/objects/{object}/records/query"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postqueryresponse.model_validate(self._handle_response(response))

    def post_v2_objects_by_object_records(
        self, object: str, data: dict[str, Any]
    ) -> Postrecordsresponse:
        """
        Create a record

        Args:
            object (string): object
            data (object): data

        Returns:
            Postrecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/objects/{object}/records"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postrecordsresponse.model_validate(self._handle_response(response))

    def put_v2_objects_by_object_records(
        self, object: str, matching_attribute: str, data: dict[str, Any]
    ) -> Postrecordsresponse:
        """
        Assert a record

        Args:
            object (string): object
            matching_attribute (string): No description provided. Example: '41252299-f8c7-4b5e-99c9-4ff8321d2f96'.
            data (object): data

        Returns:
            Postrecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/objects/{object}/records"
        query_params = {
            k: v
            for k, v in [("matching_attribute", matching_attribute)]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postrecordsresponse.model_validate(self._handle_response(response))

    def get_v2_objects_by_object_records_by_record_id(
        self, object: str, record_id: str
    ) -> Postrecordsresponse:
        """
        Get a record

        Args:
            object (string): object
            record_id (string): record_id

        Returns:
            Postrecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        if record_id is None:
            raise ValueError("Missing required parameter 'record_id'.")
        url = f"{self.base_url}/v2/objects/{object}/records/{record_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Postrecordsresponse.model_validate(self._handle_response(response))

    def patch_v2_objects_by_object_records_by_record_id(
        self, object: str, record_id: str, data: dict[str, Any]
    ) -> Postrecordsresponse:
        """
        Update a record (append multiselect values)

        Args:
            object (string): object
            record_id (string): record_id
            data (object): data

        Returns:
            Postrecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        if record_id is None:
            raise ValueError("Missing required parameter 'record_id'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/objects/{object}/records/{record_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Postrecordsresponse.model_validate(self._handle_response(response))

    def put_v2_objects_by_object_records_by_record_id(
        self, object: str, record_id: str, data: dict[str, Any]
    ) -> Postrecordsresponse:
        """
        Update a record (overwrite multiselect values)

        Args:
            object (string): object
            record_id (string): record_id
            data (object): data

        Returns:
            Postrecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        if record_id is None:
            raise ValueError("Missing required parameter 'record_id'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/objects/{object}/records/{record_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postrecordsresponse.model_validate(self._handle_response(response))

    def delete_v2_objects_by_object_records_by_record_id(
        self, object: str, record_id: str
    ) -> Deleterecordsresponse:
        """
        Delete a record

        Args:
            object (string): object
            record_id (string): record_id

        Returns:
            Deleterecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        if record_id is None:
            raise ValueError("Missing required parameter 'record_id'.")
        url = f"{self.base_url}/v2/objects/{object}/records/{record_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleterecordsresponse.model_validate(self._handle_response(response))

    def get_v2_objects_by_object_records_by_record_id_attributes_by_attribute_values(
        self,
        object: str,
        record_id: str,
        attribute: str,
        show_historic: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Getvaluesresponse:
        """
        List record attribute values

        Args:
            object (string): object
            record_id (string): record_id
            attribute (string): attribute
            show_historic (boolean): No description provided. Example: 'True'.
            limit (integer): No description provided. Example: '10'.
            offset (integer): No description provided. Example: '5'.

        Returns:
            Getvaluesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        if record_id is None:
            raise ValueError("Missing required parameter 'record_id'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        url = f"{self.base_url}/v2/objects/{object}/records/{record_id}/attributes/{attribute}/values"
        query_params = {
            k: v
            for k, v in [
                ("show_historic", show_historic),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Getvaluesresponse.model_validate(self._handle_response(response))

    def get_v2_objects_by_object_records_by_record_id_entries(
        self,
        object: str,
        record_id: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Getentriesresponse:
        """
        List record entries

        Args:
            object (string): object
            record_id (string): record_id
            limit (integer): No description provided. Example: '10'.
            offset (integer): No description provided. Example: '5'.

        Returns:
            Getentriesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        if object is None:
            raise ValueError("Missing required parameter 'object'.")
        if record_id is None:
            raise ValueError("Missing required parameter 'record_id'.")
        url = f"{self.base_url}/v2/objects/{object}/records/{record_id}/entries"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Getentriesresponse.model_validate(self._handle_response(response))

    def post_v2_objects_records_search(
        self,
        query: str,
        objects: List[str],
        request_as: Any,
        limit: Optional[float] = None,
    ) -> Postsearchresponse:
        """
        Search records

        Args:
            query (string): Query string to search for. An empty string returns a default set of results. Example: 'alan mathis'.
            objects (array): Specifies which objects to filter results by. At least one object must be specified. Accepts object slugs or IDs. Example: "['people', 'deals', '1b31b79a-ddf9-4d57-a320-884061b2bcff']".
            request_as (string): Specifies the context in which to perform the search. Use 'workspace' to return all search results or specify a workspace member to limit results to what one specific person in your workspace can see.
            limit (number): The maximum number of results to return. Defaults to 25. Example: '25'.

        Returns:
            Postsearchresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Records
        """
        request_body_data = None
        request_body_data = {
            "query": query,
            "limit": limit,
            "objects": objects,
            "request_as": request_as,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/objects/records/search"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postsearchresponse.model_validate(self._handle_response(response))

    def get_v2_lists(self) -> Getlistsresponse:
        """
        List all lists

        Returns:
            Getlistsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists
        """
        url = f"{self.base_url}/v2/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getlistsresponse.model_validate(self._handle_response(response))

    def post_v2_lists(self, data: dict[str, Any]) -> Postlistsresponse:
        """
        Create a list

        Args:
            data (object): data

        Returns:
            Postlistsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists
        """
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/lists"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postlistsresponse.model_validate(self._handle_response(response))

    def get_v2_lists_by_list(self, list: str) -> Postlistsresponse:
        """
        Get a list

        Args:
            list (string): list

        Returns:
            Postlistsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        url = f"{self.base_url}/v2/lists/{list}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Postlistsresponse.model_validate(self._handle_response(response))

    def patch_v2_lists_by_list(
        self, list: str, data: dict[str, Any]
    ) -> Postlistsresponse:
        """
        Update a list

        Args:
            list (string): list
            data (object): data

        Returns:
            Postlistsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Lists
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/lists/{list}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Postlistsresponse.model_validate(self._handle_response(response))

    def post_v2_lists_by_list_entries_query(
        self,
        list: str,
        filter: Optional[dict[str, Any]] = None,
        sorts: Optional[List[Any]] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
    ) -> Postqueryresponse1:
        """
        List entries

        Args:
            list (string): list
            filter (object): An object used to filter results to a subset of results. See the [full guide to filtering and sorting here](/rest-api/how-to/filtering-and-sorting). Example: "{'name': 'Ada Lovelace'}".
            sorts (array): An object used to sort results. See the [full guide to filtering and sorting here](/rest-api/how-to/filtering-and-sorting). Example: "[{'direction': 'asc', 'attribute': 'name', 'field': 'last_name'}]".
            limit (number): The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/rest-api/how-to/pagination). Example: '500'.
            offset (number): The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/rest-api/how-to/pagination). Example: '0'.

        Returns:
            Postqueryresponse1: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Entries
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        request_body_data = None
        request_body_data = {
            "filter": filter,
            "sorts": sorts,
            "limit": limit,
            "offset": offset,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/lists/{list}/entries/query"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postqueryresponse1.model_validate(self._handle_response(response))

    def post_v2_lists_by_list_entries(
        self, list: str, data: dict[str, Any]
    ) -> Postentriesresponse:
        """
        Create an entry (add record to list)

        Args:
            list (string): list
            data (object): data

        Returns:
            Postentriesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Entries
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/lists/{list}/entries"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postentriesresponse.model_validate(self._handle_response(response))

    def put_v2_lists_by_list_entries(
        self, list: str, data: dict[str, Any]
    ) -> Postentriesresponse:
        """
        Assert a list entry by parent

        Args:
            list (string): list
            data (object): data

        Returns:
            Postentriesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Entries
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/lists/{list}/entries"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postentriesresponse.model_validate(self._handle_response(response))

    def get_v2_lists_by_list_entries_by_entry_id(
        self, list: str, entry_id: str
    ) -> Postentriesresponse:
        """
        Get a list entry

        Args:
            list (string): list
            entry_id (string): entry_id

        Returns:
            Postentriesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Entries
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        if entry_id is None:
            raise ValueError("Missing required parameter 'entry_id'.")
        url = f"{self.base_url}/v2/lists/{list}/entries/{entry_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Postentriesresponse.model_validate(self._handle_response(response))

    def patch_v2_lists_by_list_entries_by_entry_id(
        self, list: str, entry_id: str, data: dict[str, Any]
    ) -> Postentriesresponse:
        """
        Update a list entry (append multiselect values)

        Args:
            list (string): list
            entry_id (string): entry_id
            data (object): data

        Returns:
            Postentriesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Entries
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        if entry_id is None:
            raise ValueError("Missing required parameter 'entry_id'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/lists/{list}/entries/{entry_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Postentriesresponse.model_validate(self._handle_response(response))

    def put_v2_lists_by_list_entries_by_entry_id(
        self, list: str, entry_id: str, data: dict[str, Any]
    ) -> Postentriesresponse:
        """
        Update a list entry (overwrite multiselect values)

        Args:
            list (string): list
            entry_id (string): entry_id
            data (object): data

        Returns:
            Postentriesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Entries
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        if entry_id is None:
            raise ValueError("Missing required parameter 'entry_id'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/lists/{list}/entries/{entry_id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postentriesresponse.model_validate(self._handle_response(response))

    def delete_v2_lists_by_list_entries_by_entry_id(
        self, list: str, entry_id: str
    ) -> Deleterecordsresponse:
        """
        Delete a list entry

        Args:
            list (string): list
            entry_id (string): entry_id

        Returns:
            Deleterecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Entries
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        if entry_id is None:
            raise ValueError("Missing required parameter 'entry_id'.")
        url = f"{self.base_url}/v2/lists/{list}/entries/{entry_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleterecordsresponse.model_validate(self._handle_response(response))

    def get_v2_lists_by_list_entries_by_entry_id_attributes_by_attribute_values(
        self,
        list: str,
        entry_id: str,
        attribute: str,
        show_historic: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Getvaluesresponse:
        """
        List attribute values for a list entry

        Args:
            list (string): list
            entry_id (string): entry_id
            attribute (string): attribute
            show_historic (boolean): No description provided. Example: 'True'.
            limit (integer): No description provided. Example: '10'.
            offset (integer): No description provided. Example: '5'.

        Returns:
            Getvaluesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Entries
        """
        if list is None:
            raise ValueError("Missing required parameter 'list'.")
        if entry_id is None:
            raise ValueError("Missing required parameter 'entry_id'.")
        if attribute is None:
            raise ValueError("Missing required parameter 'attribute'.")
        url = f"{self.base_url}/v2/lists/{list}/entries/{entry_id}/attributes/{attribute}/values"
        query_params = {
            k: v
            for k, v in [
                ("show_historic", show_historic),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Getvaluesresponse.model_validate(self._handle_response(response))

    def get_v2_workspace_members(self) -> GetworkspaceMembersresponse:
        """
        List workspace members

        Returns:
            GetworkspaceMembersresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Workspace members
        """
        url = f"{self.base_url}/v2/workspace_members"
        query_params = {}
        response = self._get(url, params=query_params)
        return GetworkspaceMembersresponse.model_validate(
            self._handle_response(response)
        )

    def get_v2_workspace_members_by_workspace_member_id(
        self, workspace_member_id: str
    ) -> GetworkspaceMembersresponse1:
        """
        Get a workspace member

        Args:
            workspace_member_id (string): workspace_member_id

        Returns:
            GetworkspaceMembersresponse1: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Workspace members
        """
        if workspace_member_id is None:
            raise ValueError("Missing required parameter 'workspace_member_id'.")
        url = f"{self.base_url}/v2/workspace_members/{workspace_member_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return GetworkspaceMembersresponse1.model_validate(
            self._handle_response(response)
        )

    def get_v2_notes(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parent_object: Optional[str] = None,
        parent_record_id: Optional[str] = None,
    ) -> Getnotesresponse:
        """
        List notes

        Args:
            limit (integer): No description provided. Example: '10'.
            offset (integer): No description provided. Example: '5'.
            parent_object (string): No description provided. Example: 'people'.
            parent_record_id (string): No description provided. Example: '891dcbfc-9141-415d-9b2a-2238a6cc012d'.

        Returns:
            Getnotesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Notes
        """
        url = f"{self.base_url}/v2/notes"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("parent_object", parent_object),
                ("parent_record_id", parent_record_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Getnotesresponse.model_validate(self._handle_response(response))

    def post_v2_notes(self, data: dict[str, Any]) -> Postnotesresponse:
        """
        Create a note

        Args:
            data (object): data

        Returns:
            Postnotesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Notes
        """
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/notes"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postnotesresponse.model_validate(self._handle_response(response))

    def get_v2_notes_by_note_id(self, note_id: str) -> Postnotesresponse:
        """
        Get a note

        Args:
            note_id (string): note_id

        Returns:
            Postnotesresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Notes
        """
        if note_id is None:
            raise ValueError("Missing required parameter 'note_id'.")
        url = f"{self.base_url}/v2/notes/{note_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Postnotesresponse.model_validate(self._handle_response(response))

    def delete_v2_notes_by_note_id(self, note_id: str) -> Deleterecordsresponse:
        """
        Delete a note

        Args:
            note_id (string): note_id

        Returns:
            Deleterecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Notes
        """
        if note_id is None:
            raise ValueError("Missing required parameter 'note_id'.")
        url = f"{self.base_url}/v2/notes/{note_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleterecordsresponse.model_validate(self._handle_response(response))

    def get_v2_tasks(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        linked_object: Optional[str] = None,
        linked_record_id: Optional[str] = None,
        assignee: Optional[str] = None,
        is_completed: Optional[bool] = None,
    ) -> Gettasksresponse:
        """
        List tasks

        Args:
            limit (integer): The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/rest-api/how-to/pagination). Example: 10.
            offset (integer): The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/rest-api/how-to/pagination). Example: 5.
            sort (string): Optionally sort the results. "created_at:asc" returns oldest results first, "created_at:desc" returns the newest results first. If unspecified, defaults to "created_at:asc" (oldest results first). Example: "created_at:desc".
            linked_object (string): Pass a value to this parameter to filter results to only those tasks that contain the specified record in the `linked_records` property of the task. This parameter should identify the object that the linked record belongs to. For example, if filtering to tasks that link to a specific person record, this parameter should be `people`. If provided, `linked_record_id` must also be provided. Example: "people".
            linked_record_id (string): Pass a value to this parameter to filter results to only those tasks that contain the specified record in the `linked_records` property of the task. This parameter should contain the record ID of the linked record. If provided, `linked_object` must also be provided. Example: "891dcbfc-9141-415d-9b2a-2238a6cc012d".
            assignee (string): Filter tasks by workspace member assignees. Workspace members can be referenced by either their email address or ID. Pass an empty value or the string `null` to find tasks with no assignee. Example: "50cf242c-7fa3-4cad-87d0-75b1af71c57b".
            is_completed (boolean): Filter tasks by whether they have been completed. By default, both completed and non-completed tasks are returned. Specify `true` to only return completed tasks, or `false` to only return non-completed tasks. Example: True.

        Returns:
            Gettasksresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Tasks
        """
        url = f"{self.base_url}/v2/tasks"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("sort", sort),
                ("linked_object", linked_object),
                ("linked_record_id", linked_record_id),
                ("assignee", assignee),
                ("is_completed", is_completed),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Gettasksresponse.model_validate(self._handle_response(response))

    def post_v2_tasks(self, data: dict[str, Any]) -> Gettasksresponse:
        """
        Create a task

        Args:
            data (object): data

        Returns:
            Gettasksresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Tasks
        """
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/tasks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Gettasksresponse.model_validate(self._handle_response(response))

    def get_v2_tasks_by_task_id(self, task_id: str) -> Gettasksresponse:
        """
        Get a task

        Args:
            task_id (string): task_id

        Returns:
            Gettasksresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Tasks
        """
        if task_id is None:
            raise ValueError("Missing required parameter 'task_id'.")
        url = f"{self.base_url}/v2/tasks/{task_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Gettasksresponse.model_validate(self._handle_response(response))

    def patch_v2_tasks_by_task_id(
        self, task_id: str, data: dict[str, Any]
    ) -> Gettasksresponse:
        """
        Update a task

        Args:
            task_id (string): task_id
            data (object): data

        Returns:
            Gettasksresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Tasks
        """
        if task_id is None:
            raise ValueError("Missing required parameter 'task_id'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/tasks/{task_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Gettasksresponse.model_validate(self._handle_response(response))

    def delete_v2_tasks_by_task_id(self, task_id: str) -> Deleterecordsresponse:
        """
        Delete a task

        Args:
            task_id (string): task_id

        Returns:
            Deleterecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Tasks
        """
        if task_id is None:
            raise ValueError("Missing required parameter 'task_id'.")
        url = f"{self.base_url}/v2/tasks/{task_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleterecordsresponse.model_validate(self._handle_response(response))

    def get_v2_threads(
        self,
        record_id: Optional[str] = None,
        object: Optional[str] = None,
        entry_id: Optional[str] = None,
        list: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Getthreadsresponse:
        """
        List threads

        Args:
            record_id (string): No description provided. Example: '891dcbfc-9141-415d-9b2a-2238a6cc012d'.
            object (string): No description provided. Example: 'people'.
            entry_id (string): No description provided. Example: '2e6e29ea-c4e0-4f44-842d-78a891f8c156'.
            list (string): No description provided. Example: '33ebdbe9-e529-47c9-b894-0ba25e9c15c0'.
            limit (integer): No description provided. Example: '10'.
            offset (integer): No description provided. Example: '5'.

        Returns:
            Getthreadsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Threads
        """
        url = f"{self.base_url}/v2/threads"
        query_params = {
            k: v
            for k, v in [
                ("record_id", record_id),
                ("object", object),
                ("entry_id", entry_id),
                ("list", list),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Getthreadsresponse.model_validate(self._handle_response(response))

    def get_v2_threads_by_thread_id(self, thread_id: str) -> Getthreadsresponse1:
        """
        Get a thread

        Args:
            thread_id (string): thread_id

        Returns:
            Getthreadsresponse1: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Threads
        """
        if thread_id is None:
            raise ValueError("Missing required parameter 'thread_id'.")
        url = f"{self.base_url}/v2/threads/{thread_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getthreadsresponse1.model_validate(self._handle_response(response))

    def post_v2_comments(self, data: Any) -> Postcommentsresponse:
        """
        Create a comment

        Args:
            data (string): data

        Returns:
            Postcommentsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Comments
        """
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/comments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postcommentsresponse.model_validate(self._handle_response(response))

    def get_v2_comments_by_comment_id(self, comment_id: str) -> Postcommentsresponse:
        """
        Get a comment

        Args:
            comment_id (string): comment_id

        Returns:
            Postcommentsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Comments
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'.")
        url = f"{self.base_url}/v2/comments/{comment_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Postcommentsresponse.model_validate(self._handle_response(response))

    def delete_v2_comments_by_comment_id(
        self, comment_id: str
    ) -> Deleterecordsresponse:
        """
        Delete a comment

        Args:
            comment_id (string): comment_id

        Returns:
            Deleterecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Comments
        """
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'.")
        url = f"{self.base_url}/v2/comments/{comment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleterecordsresponse.model_validate(self._handle_response(response))

    def get_v2_meetings(
        self,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        linked_object: Optional[str] = None,
        linked_record_id: Optional[str] = None,
        participants: Optional[str] = None,
        sort: Optional[str] = None,
        ends_from: Optional[str] = None,
        starts_before: Optional[str] = None,
        timezone: Optional[str] = None,
    ) -> Getmeetingsresponse:
        """
        List meetings

        Args:
            limit (integer): The maximum number of meetings to return. Must be between 1 and 200. Defaults to 50. Example: 50.
            cursor (string): A pagination cursor used to fetch the next page of meetings. Responses with more meetings will include a cursor for you to use here. If not provided, the first page will be returned.
            linked_object (string): The object to filter meetings by. Must be a valid object slug or ID. If provided, linked_record_id must also be provided.
            linked_record_id (string): Used to filter meetings to only those values that include a specific linked record. Must be a valid record ID. If provided, linked_object must also be provided.
            participants (string): A comma-separated list of emails to filter meetings by. If provided, meetings will be filtered to only include meetings that include at least one of the provided emails as participants.
            sort (string): The order in which to sort the meetings. Defaults to start_asc.
            ends_from (string): Use `ends_from` to filter meetings to only those that end after the specified timestamp. `ends_from` is inclusive, meaning that meetings that end at the exact timestamp will be included in results. When evaluating all-day meetings, we filter results from the perspective of a specific timezone (see `timezone` for more information).
            starts_before (string): Use `starts_before` to filter meetings to only those that start before the specified timestamp. `starts_before` is exclusive, meaning that meetings that start at the exact timestamp will not be included in results. When evaluating all-day meetings, we filter results from the perspective of a specific timezone (see `timezone` for more information).
            timezone (string): The timezone to use when filtering meetings using `ends_from` and `starts_before`. Defaults to UTC. This property has no effect for non-all-day meetings.

        Returns:
            Getmeetingsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Meetings
        """
        url = f"{self.base_url}/v2/meetings"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("cursor", cursor),
                ("linked_object", linked_object),
                ("linked_record_id", linked_record_id),
                ("participants", participants),
                ("sort", sort),
                ("ends_from", ends_from),
                ("starts_before", starts_before),
                ("timezone", timezone),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Getmeetingsresponse.model_validate(self._handle_response(response))

    def get_v2_meetings_by_meeting_id(self, meeting_id: str) -> Getmeetingsresponse:
        """
        Get a meeting

        Args:
            meeting_id (string): meeting_id

        Returns:
            Getmeetingsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Meetings
        """
        if meeting_id is None:
            raise ValueError("Missing required parameter 'meeting_id'.")
        url = f"{self.base_url}/v2/meetings/{meeting_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getmeetingsresponse.model_validate(self._handle_response(response))

    def get_v2_meetings_by_meeting_id_call_recordings(
        self, meeting_id: str, limit: Optional[int] = None, cursor: Optional[str] = None
    ) -> GetcallRecordingsresponse:
        """
        List call recordings

        Args:
            meeting_id (string): meeting_id
            limit (integer): No description provided. Example: '50'.
            cursor (string): No description provided. Example: 'eyJkZXNjcmlwdGlvbiI6ICJ0aGlzIGlzIGEgY3Vyc29yIn0=.eM56CGbqZ6G1NHiJchTIkH4vKDr'.

        Returns:
            GetcallRecordingsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Call recordings
        """
        if meeting_id is None:
            raise ValueError("Missing required parameter 'meeting_id'.")
        url = f"{self.base_url}/v2/meetings/{meeting_id}/call_recordings"
        query_params = {
            k: v for k, v in [("limit", limit), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetcallRecordingsresponse.model_validate(self._handle_response(response))

    def get_v2_meetings_by_meeting_id_call_recordings_by_call_recording_id(
        self, meeting_id: str, call_recording_id: str
    ) -> GetcallRecordingsresponse1:
        """
        Get call recording

        Args:
            meeting_id (string): meeting_id
            call_recording_id (string): call_recording_id

        Returns:
            GetcallRecordingsresponse1: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Call recordings
        """
        if meeting_id is None:
            raise ValueError("Missing required parameter 'meeting_id'.")
        if call_recording_id is None:
            raise ValueError("Missing required parameter 'call_recording_id'.")
        url = f"{self.base_url}/v2/meetings/{meeting_id}/call_recordings/{call_recording_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return GetcallRecordingsresponse1.model_validate(
            self._handle_response(response)
        )

    def get_v2_meetings_by_meeting_id_call_recordings_by_call_recording_id_transcript(
        self, meeting_id: str, call_recording_id: str, cursor: Optional[str] = None
    ) -> Gettranscriptresponse:
        """
        Get call transcript

        Args:
            meeting_id (string): meeting_id
            call_recording_id (string): call_recording_id
            cursor (string): No description provided. Example: 'eyJkZXNjcmlwdGlvbiI6ICJ0aGlzIGlzIGEgY3Vyc29yIn0=.eM56CGbqZ6G1NHiJchTIkH4vKDr'.

        Returns:
            Gettranscriptresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Transcripts
        """
        if meeting_id is None:
            raise ValueError("Missing required parameter 'meeting_id'.")
        if call_recording_id is None:
            raise ValueError("Missing required parameter 'call_recording_id'.")
        url = f"{self.base_url}/v2/meetings/{meeting_id}/call_recordings/{call_recording_id}/transcript"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        return Gettranscriptresponse.model_validate(self._handle_response(response))

    def get_v2_webhooks(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Getwebhooksresponse:
        """
        List webhooks

        Args:
            limit (integer): No description provided. Example: '10'.
            offset (integer): No description provided. Example: '5'.

        Returns:
            Getwebhooksresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        url = f"{self.base_url}/v2/webhooks"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Getwebhooksresponse.model_validate(self._handle_response(response))

    def post_v2_webhooks(self, data: dict[str, Any]) -> Postwebhooksresponse:
        """
        Create a webhook

        Args:
            data (object): data

        Returns:
            Postwebhooksresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/webhooks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Postwebhooksresponse.model_validate(self._handle_response(response))

    def get_v2_webhooks_by_webhook_id(self, webhook_id: str) -> Getwebhooksresponse1:
        """
        Get a webhook

        Args:
            webhook_id (string): webhook_id

        Returns:
            Getwebhooksresponse1: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'.")
        url = f"{self.base_url}/v2/webhooks/{webhook_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getwebhooksresponse1.model_validate(self._handle_response(response))

    def patch_v2_webhooks_by_webhook_id(
        self, webhook_id: str, data: dict[str, Any]
    ) -> Getwebhooksresponse1:
        """
        Update a webhook

        Args:
            webhook_id (string): webhook_id
            data (object): data

        Returns:
            Getwebhooksresponse1: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'.")
        request_body_data = None
        request_body_data = {
            "data": data,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/webhooks/{webhook_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Getwebhooksresponse1.model_validate(self._handle_response(response))

    def delete_v2_webhooks_by_webhook_id(
        self, webhook_id: str
    ) -> Deleterecordsresponse:
        """
        Delete a webhook

        Args:
            webhook_id (string): webhook_id

        Returns:
            Deleterecordsresponse: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'.")
        url = f"{self.base_url}/v2/webhooks/{webhook_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleterecordsresponse.model_validate(self._handle_response(response))

    def get_v2_self(self) -> Any:
        """
        Identify

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Meta
        """
        url = f"{self.base_url}/v2/self"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.get_v2_objects,
            self.post_v2_objects,
            self.get_v2_objects_by_object,
            self.patch_v2_objects_by_object,
            self.get_v2_by_target_by_identifier_attributes,
            self.post_v2_by_target_by_identifier_attributes,
            self.get_v2_by_target_by_identifier_attributes_by_attribute,
            self.patch_v2_by_target_by_identifier_attributes_by_attribute,
            self.get_v2_by_target_by_identifier_attributes_by_attribute_options,
            self.post_v2_by_target_by_identifier_attributes_by_attribute_options,
            self.patch_v2_by_target_by_identifier_attributes_by_attribute_options_by_option,
            self.get_v2_by_target_by_identifier_attributes_by_attribute_statuses,
            self.post_v2_by_target_by_identifier_attributes_by_attribute_statuses,
            self.patch_v2_by_target_by_identifier_attributes_by_attribute_statuses_by_status,
            self.post_v2_objects_by_object_records_query,
            self.post_v2_objects_by_object_records,
            self.put_v2_objects_by_object_records,
            self.get_v2_objects_by_object_records_by_record_id,
            self.patch_v2_objects_by_object_records_by_record_id,
            self.put_v2_objects_by_object_records_by_record_id,
            self.delete_v2_objects_by_object_records_by_record_id,
            self.get_v2_objects_by_object_records_by_record_id_attributes_by_attribute_values,
            self.get_v2_objects_by_object_records_by_record_id_entries,
            self.post_v2_objects_records_search,
            self.get_v2_lists,
            self.post_v2_lists,
            self.get_v2_lists_by_list,
            self.patch_v2_lists_by_list,
            self.post_v2_lists_by_list_entries_query,
            self.post_v2_lists_by_list_entries,
            self.put_v2_lists_by_list_entries,
            self.get_v2_lists_by_list_entries_by_entry_id,
            self.patch_v2_lists_by_list_entries_by_entry_id,
            self.put_v2_lists_by_list_entries_by_entry_id,
            self.delete_v2_lists_by_list_entries_by_entry_id,
            self.get_v2_lists_by_list_entries_by_entry_id_attributes_by_attribute_values,
            self.get_v2_workspace_members,
            self.get_v2_workspace_members_by_workspace_member_id,
            self.get_v2_notes,
            self.post_v2_notes,
            self.get_v2_notes_by_note_id,
            self.delete_v2_notes_by_note_id,
            self.get_v2_tasks,
            self.post_v2_tasks,
            self.get_v2_tasks_by_task_id,
            self.patch_v2_tasks_by_task_id,
            self.delete_v2_tasks_by_task_id,
            self.get_v2_threads,
            self.get_v2_threads_by_thread_id,
            self.post_v2_comments,
            self.get_v2_comments_by_comment_id,
            self.delete_v2_comments_by_comment_id,
            self.get_v2_meetings,
            self.get_v2_meetings_by_meeting_id,
            self.get_v2_meetings_by_meeting_id_call_recordings,
            self.get_v2_meetings_by_meeting_id_call_recordings_by_call_recording_id,
            self.get_v2_meetings_by_meeting_id_call_recordings_by_call_recording_id_transcript,
            self.get_v2_webhooks,
            self.post_v2_webhooks,
            self.get_v2_webhooks_by_webhook_id,
            self.patch_v2_webhooks_by_webhook_id,
            self.delete_v2_webhooks_by_webhook_id,
            self.get_v2_self,
        ]
