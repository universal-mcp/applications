from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class AsanaApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="asana", integration=integration, **kwargs)
        self.base_url = "https://app.asana.com/api/1.0"

    def get_an_allocation(
        self, allocation_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves details about an allocation by its GUID using the API endpoint "/allocations/{allocation_gid}" with optional fields and formatting controlled by query parameters "opt_fields" and "opt_pretty".

        Args:
            allocation_gid (string): allocation_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'assignee,assignee.name,created_by,created_by.name,effort,effort.type,effort.value,end_date,parent,parent.name,resource_subtype,start_date'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the record for a single allocation.

        Tags:
            Allocations, important
        """
        if allocation_gid is None:
            raise ValueError("Missing required parameter 'allocation_gid'")
        url = f"{self.base_url}/allocations/{allocation_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_allocation(
        self, allocation_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates or creates a resource identified by the allocation GID at the "/allocations/{allocation_gid}" path using the PUT method.

        Args:
            allocation_gid (string): allocation_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'assignee,assignee.name,created_by,created_by.name,effort,effort.type,effort.value,end_date,parent,parent.name,resource_subtype,start_date'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "assignee": "Duis sit et quis tempor",
                    "effort": {
                      "type": "percent",
                      "value": 50
                    },
                    "end_date": "2024-02-28",
                    "gid": "12345",
                    "parent": "proiden",
                    "resource_type": "task",
                    "start_date": "2024-02-28"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the allocation.

        Tags:
            Allocations, important
        """
        if allocation_gid is None:
            raise ValueError("Missing required parameter 'allocation_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/allocations/{allocation_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_allocation(self, allocation_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes the specified allocation by its global identifier and returns a status code indicating success or failure.

        Args:
            allocation_gid (string): allocation_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified allocation.

        Tags:
            Allocations, important
        """
        if allocation_gid is None:
            raise ValueError("Missing required parameter 'allocation_gid'")
        url = f"{self.base_url}/allocations/{allocation_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_allocations(
        self,
        parent=None,
        assignee=None,
        workspace=None,
        limit=None,
        offset=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of resource allocations filtered by parent, assignee, workspace, and pagination parameters.

        Args:
            parent (string): Globally unique identifier for the project to filter allocations by. Example: '77688'.
            assignee (string): Globally unique identifier for the user the allocation is assigned to. Example: '12345'.
            workspace (string): Globally unique identifier for the workspace. Example: '98765'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'assignee,assignee.name,created_by,created_by.name,effort,effort.type,effort.value,end_date,offset,parent,parent.name,path,resource_subtype,start_date,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested allocations.

        Tags:
            Allocations
        """
        url = f"{self.base_url}/allocations"
        query_params = {
            k: v
            for k, v in [
                ("parent", parent),
                ("assignee", assignee),
                ("workspace", workspace),
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_allocation(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new allocation using the API and returns a successful response upon completion, with optional fields and pretty printing available through query parameters.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'assignee,assignee.name,created_by,created_by.name,effort,effort.type,effort.value,end_date,parent,parent.name,resource_subtype,start_date'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "assignee": "consectetur enim est ea",
                    "effort": {
                      "type": "hours",
                      "value": 50
                    },
                    "end_date": "2024-02-28",
                    "gid": "12345",
                    "parent": "minim officia est esse",
                    "resource_type": "task",
                    "start_date": "2024-02-28"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new allocation.

        Tags:
            Allocations
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/allocations"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_an_attachment(
        self, attachment_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves details for a specific attachment using its identifier, with optional fields and pretty-printed responses.

        Args:
            attachment_gid (string): attachment_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'connected_to_app,created_at,download_url,host,name,parent,parent.created_by,parent.name,parent.resource_subtype,permanent_url,resource_subtype,size,view_url'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the record for a single attachment.

        Tags:
            Attachments
        """
        if attachment_gid is None:
            raise ValueError("Missing required parameter 'attachment_gid'")
        url = f"{self.base_url}/attachments/{attachment_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_attachment(self, attachment_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes an attachment identified by the attachment GID using the DELETE method.

        Args:
            attachment_gid (string): attachment_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified attachment.

        Tags:
            Attachments
        """
        if attachment_gid is None:
            raise ValueError("Missing required parameter 'attachment_gid'")
        url = f"{self.base_url}/attachments/{attachment_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachments_from_an_object(
        self, limit=None, offset=None, parent=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of attachments using the "GET" method at the "/attachments" endpoint, allowing optional filtering by limit, offset, parent, and additional fields for custom output.

        Args:
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            parent (string): (Required) Globally unique identifier for object to fetch statuses from. Must be a GID for a `project`, `project_brief`, or `task`. Example: '159874'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'connected_to_app,created_at,download_url,host,name,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permanent_url,resource_subtype,size,uri,view_url'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified object's attachments.

        Tags:
            Attachments
        """
        url = f"{self.base_url}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("parent", parent),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_audit_log_events(
        self,
        workspace_gid,
        start_at=None,
        end_at=None,
        event_type=None,
        actor_type=None,
        actor_gid=None,
        resource_gid=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of audit log events for a specified workspace, allowing filtering by time range, event type, actor type, and other parameters.

        Args:
            workspace_gid (string): workspace_gid
            start_at (string): Filter to events created after this time (inclusive). Example: '1983-07-10T20:31:48.443Z'.
            end_at (string): Filter to events created before this time (exclusive). Example: '1983-07-10T20:31:48.443Z'.
            event_type (string): Filter to events of this type.
        Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values. Example: 'eiusmod irure commodo'.
            actor_type (string): Filter to events with an actor of this type.
        This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded. Example: 'external_administrator'.
            actor_gid (string): Filter to events triggered by the actor with this ID. Example: 'eiusmod irure commodo'.
            resource_gid (string): Filter to events with this resource ID. Example: 'eiusmod irure commodo'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: AuditLogEvents were successfully retrieved.

        Tags:
            Audit log API
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/audit_log_events"
        query_params = {
            k: v
            for k, v in [
                ("start_at", start_at),
                ("end_at", end_at),
                ("event_type", event_type),
                ("actor_type", actor_type),
                ("actor_gid", actor_gid),
                ("resource_gid", resource_gid),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def submit_parallel_requests(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Processes a batch of API requests in a single call, allowing for efficient execution of multiple operations defined at the "/batch" path using the "POST" method.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'body,headers,status_code'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "actions": [
                      {
                        "data": {
                          "assignee": "me",
                          "workspace": "1337"
                        },
                        "method": "get",
                        "options": {
                          "fields": [
                            "name",
                            "notes",
                            "completed"
                          ],
                          "limit": 3
                        },
                        "relative_path": "/tasks/123"
                      },
                      {
                        "data": {
                          "assignee": "me",
                          "workspace": "1337"
                        },
                        "method": "get",
                        "options": {
                          "fields": [
                            "name",
                            "notes",
                            "completed"
                          ],
                          "limit": 3
                        },
                        "relative_path": "/tasks/123"
                      }
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully completed the requested batch API operations.

        Tags:
            Batch API
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/batch"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_acustom_field(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new custom field at the "/custom_fields" endpoint using the "POST" method, allowing for optional parameters to specify additional fields or formatting options.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'asana_created_field,created_by,created_by.name,currency_code,custom_label,custom_label_position,date_value,date_value.date,date_value.date_time,description,display_value,enabled,enum_options,enum_options.color,enum_options.enabled,enum_options.name,enum_value,enum_value.color,enum_value.enabled,enum_value.name,format,has_notifications_enabled,id_prefix,is_formula_field,is_global_to_workspace,is_value_read_only,multi_enum_values,multi_enum_values.color,multi_enum_values.enabled,multi_enum_values.name,name,number_value,people_value,people_value.name,precision,representation_type,resource_subtype,text_value,type'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "asana_created_field": "priority",
                    "currency_code": "EUR",
                    "custom_label": "gold pieces",
                    "custom_label_position": "suffix",
                    "date_value": {
                      "date": "2024-08-23",
                      "date_time": "2024-08-23T22:00:00.000Z"
                    },
                    "description": "Development team priority",
                    "display_value": "blue",
                    "enabled": true,
                    "enum_options": [
                      {
                        "color": "blue",
                        "enabled": true,
                        "gid": "12345",
                        "name": "Low",
                        "resource_type": "task"
                      },
                      {
                        "color": "blue",
                        "enabled": true,
                        "gid": "12345",
                        "name": "Low",
                        "resource_type": "task"
                      }
                    ],
                    "enum_value": {
                      "color": "blue",
                      "enabled": true,
                      "gid": "12345",
                      "name": "Low",
                      "resource_type": "task"
                    },
                    "format": "custom",
                    "gid": "12345",
                    "has_notifications_enabled": true,
                    "id_prefix": "ID",
                    "is_formula_field": false,
                    "is_global_to_workspace": true,
                    "multi_enum_values": [
                      {
                        "color": "blue",
                        "enabled": true,
                        "gid": "12345",
                        "name": "Low",
                        "resource_type": "task"
                      },
                      {
                        "color": "blue",
                        "enabled": true,
                        "gid": "12345",
                        "name": "Low",
                        "resource_type": "task"
                      }
                    ],
                    "name": "Status",
                    "number_value": 5.2,
                    "owned_by_app": false,
                    "people_value": [
                      "12345"
                    ],
                    "precision": 2,
                    "representation_type": "number",
                    "resource_subtype": "text",
                    "resource_type": "task",
                    "text_value": "Some Value",
                    "type": "date",
                    "workspace": "1331"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Custom field successfully created.

        Tags:
            Custom fields
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom_fields"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_acustom_field(
        self, custom_field_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves the details of a specific custom field using its unique identifier and supports optional query parameters for additional field data and formatted output.

        Args:
            custom_field_gid (string): custom_field_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'asana_created_field,created_by,created_by.name,currency_code,custom_label,custom_label_position,date_value,date_value.date,date_value.date_time,description,display_value,enabled,enum_options,enum_options.color,enum_options.enabled,enum_options.name,enum_value,enum_value.color,enum_value.enabled,enum_value.name,format,has_notifications_enabled,id_prefix,is_formula_field,is_global_to_workspace,is_value_read_only,multi_enum_values,multi_enum_values.color,multi_enum_values.enabled,multi_enum_values.name,name,number_value,people_value,people_value.name,precision,representation_type,resource_subtype,text_value,type'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the complete definition of a custom field’s metadata.

        Tags:
            Custom fields
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        url = f"{self.base_url}/custom_fields/{custom_field_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_acustom_field(
        self, custom_field_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates the specified custom field's configuration for the given object (e.g., project) and returns the modified resource.

        Args:
            custom_field_gid (string): custom_field_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'asana_created_field,created_by,created_by.name,currency_code,custom_label,custom_label_position,date_value,date_value.date,date_value.date_time,description,display_value,enabled,enum_options,enum_options.color,enum_options.enabled,enum_options.name,enum_value,enum_value.color,enum_value.enabled,enum_value.name,format,has_notifications_enabled,id_prefix,is_formula_field,is_global_to_workspace,is_value_read_only,multi_enum_values,multi_enum_values.color,multi_enum_values.enabled,multi_enum_values.name,name,number_value,people_value,people_value.name,precision,representation_type,resource_subtype,text_value,type'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "asana_created_field": "priority",
                    "currency_code": "EUR",
                    "custom_label": "gold pieces",
                    "custom_label_position": "suffix",
                    "date_value": {
                      "date": "2024-08-23",
                      "date_time": "2024-08-23T22:00:00.000Z"
                    },
                    "description": "Development team priority",
                    "display_value": "blue",
                    "enabled": true,
                    "enum_options": [
                      {
                        "color": "blue",
                        "enabled": true,
                        "gid": "12345",
                        "name": "Low",
                        "resource_type": "task"
                      },
                      {
                        "color": "blue",
                        "enabled": true,
                        "gid": "12345",
                        "name": "Low",
                        "resource_type": "task"
                      }
                    ],
                    "enum_value": {
                      "color": "blue",
                      "enabled": true,
                      "gid": "12345",
                      "name": "Low",
                      "resource_type": "task"
                    },
                    "format": "custom",
                    "gid": "12345",
                    "has_notifications_enabled": true,
                    "id_prefix": "ID",
                    "is_formula_field": false,
                    "is_global_to_workspace": true,
                    "multi_enum_values": [
                      {
                        "color": "blue",
                        "enabled": true,
                        "gid": "12345",
                        "name": "Low",
                        "resource_type": "task"
                      },
                      {
                        "color": "blue",
                        "enabled": true,
                        "gid": "12345",
                        "name": "Low",
                        "resource_type": "task"
                      }
                    ],
                    "name": "Status",
                    "number_value": 5.2,
                    "owned_by_app": false,
                    "people_value": [
                      "12345"
                    ],
                    "precision": 2,
                    "representation_type": "number",
                    "resource_subtype": "text",
                    "resource_type": "task",
                    "text_value": "Some Value",
                    "type": "date",
                    "workspace": "1331"
                  }
                }
                ```

        Returns:
            dict[str, Any]: The custom field was successfully updated.

        Tags:
            Custom fields
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom_fields/{custom_field_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_acustom_field(self, custom_field_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific custom field by its globally unique identifier (GID) and returns an empty response upon success.

        Args:
            custom_field_gid (string): custom_field_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: The custom field was successfully deleted.

        Tags:
            Custom fields
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        url = f"{self.base_url}/custom_fields/{custom_field_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace_scustom_fields(
        self, workspace_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of custom fields for a specified workspace using the Asana API, allowing for optional filtering and formatting of the response.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'asana_created_field,created_by,created_by.name,currency_code,custom_label,custom_label_position,date_value,date_value.date,date_value.date_time,description,display_value,enabled,enum_options,enum_options.color,enum_options.enabled,enum_options.name,enum_value,enum_value.color,enum_value.enabled,enum_value.name,format,has_notifications_enabled,id_prefix,is_formula_field,is_global_to_workspace,is_value_read_only,multi_enum_values,multi_enum_values.color,multi_enum_values.enabled,multi_enum_values.name,name,number_value,offset,path,people_value,people_value.name,precision,representation_type,resource_subtype,text_value,type,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved all custom fields for the given workspace.

        Tags:
            Custom fields
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/custom_fields"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_enum_option(
        self, custom_field_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new enum option for a custom field and allows specifying its position relative to existing options.

        Args:
            custom_field_gid (string): custom_field_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,enabled,name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "color": "blue",
                    "enabled": true,
                    "gid": "12345",
                    "insert_after": "12345",
                    "insert_before": "12345",
                    "name": "Low",
                    "resource_type": "task"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Custom field enum option successfully created.

        Tags:
            Custom fields
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom_fields/{custom_field_gid}/enum_options"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def reorder_acustom_field_senum(
        self, custom_field_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Reorders the enum options for a custom field using the Asana API by inserting an enum option at a specified position, allowing customization of the options' order.

        Args:
            custom_field_gid (string): custom_field_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,enabled,name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "after_enum_option": "12345",
                    "before_enum_option": "12345",
                    "enum_option": "97285"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Custom field enum option successfully reordered.

        Tags:
            Custom fields
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom_fields/{custom_field_gid}/enum_options/insert"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_enum_option(
        self, enum_option_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates an existing enum option's details in the custom field and returns the modified enum option.

        Args:
            enum_option_gid (string): enum_option_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,enabled,name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "color": "blue",
                    "enabled": true,
                    "gid": "12345",
                    "name": "Low",
                    "resource_type": "task"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the specified custom field enum.

        Tags:
            Custom fields
        """
        if enum_option_gid is None:
            raise ValueError("Missing required parameter 'enum_option_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/enum_options/{enum_option_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_scustom_fields(
        self, project_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves custom field settings for a project using a specified project GID, allowing for optional filtering by fields, formatting, and pagination.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'custom_field,custom_field.asana_created_field,custom_field.created_by,custom_field.created_by.name,custom_field.currency_code,custom_field.custom_label,custom_field.custom_label_position,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.description,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.format,custom_field.has_notifications_enabled,custom_field.id_prefix,custom_field.is_formula_field,custom_field.is_global_to_workspace,custom_field.is_value_read_only,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.people_value,custom_field.people_value.name,custom_field.precision,custom_field.representation_type,custom_field.resource_subtype,custom_field.text_value,custom_field.type,is_important,offset,parent,parent.name,path,project,project.name,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved custom field settings objects for a project.

        Tags:
            Custom field settings
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/custom_field_settings"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio_scustom_fields(
        self, portfolio_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves custom field settings for a portfolio using the "GET" method, allowing for optional parameters to customize the output.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'custom_field,custom_field.asana_created_field,custom_field.created_by,custom_field.created_by.name,custom_field.currency_code,custom_field.custom_label,custom_field.custom_label_position,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.description,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.format,custom_field.has_notifications_enabled,custom_field.id_prefix,custom_field.is_formula_field,custom_field.is_global_to_workspace,custom_field.is_value_read_only,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.people_value,custom_field.people_value.name,custom_field.precision,custom_field.representation_type,custom_field.resource_subtype,custom_field.text_value,custom_field.type,is_important,offset,parent,parent.name,path,project,project.name,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved custom field settings objects for a portfolio.

        Tags:
            Custom field settings
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}/custom_field_settings"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_events_on_aresource(
        self, opt_fields=None, resource=None, sync=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of events using the "GET" method at the "/events" endpoint, allowing optional filtering by fields, resource, synchronization status, and output format.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'action,change,change.action,change.added_value,change.field,change.new_value,change.removed_value,created_at,parent,parent.name,resource,resource.name,type,user,user.name'.
            resource (string): (Required) A resource ID to subscribe to. The resource can be a task, project, or goal. Example: '12345'.
            sync (string): A sync token received from the last request, or none on first sync. Events will be returned from the point in time that the sync token was generated.
        *Note: On your first request, omit the sync token. The response will be the same as for an expired sync token, and will include a new valid sync token.If the sync token is too old (which may happen from time to time) the API will return a `412 Precondition Failed` error, and include a fresh sync token in the response.* Example: 'de4774f6915eae04714ca93bb2f5ee81'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved events.

        Tags:
            Events
        """
        url = f"{self.base_url}/events"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("resource", resource),
                ("sync", sync),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_agoal(self, goal_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves information about a specific goal using the `GET` method at the path `/goals/{goal_gid}`, allowing optional parameters for customizing output fields and formatting.

        Args:
            goal_gid (string): goal_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,owner,owner.name,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the record for a single goal.

        Tags:
            Goals
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        url = f"{self.base_url}/goals/{goal_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal(
        self, goal_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates a specific goal identified by its GID using the PUT method at the path "/goals/{goal_gid}", optionally including query parameters for custom fields and formatting.

        Args:
            goal_gid (string): goal_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,owner,owner.name,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "due_on": "2019-09-15",
                    "gid": "12345",
                    "html_notes": "<body>Start building brand awareness.</body>",
                    "is_workspace_level": true,
                    "liked": false,
                    "name": "Grow web traffic by 30%",
                    "notes": "Start building brand awareness.",
                    "owner": "12345",
                    "resource_type": "task",
                    "start_on": "2019-09-14",
                    "status": "green",
                    "team": "12345",
                    "time_period": "12345",
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the goal.

        Tags:
            Goals
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_agoal(self, goal_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific goal resource identified by the `goal_gid` at the path "/goals/{goal_gid}" using the HTTP DELETE method.

        Args:
            goal_gid (string): goal_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified goal.

        Tags:
            Goals
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        url = f"{self.base_url}/goals/{goal_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_goals(
        self,
        portfolio=None,
        project=None,
        task=None,
        is_workspace_level=None,
        team=None,
        workspace=None,
        time_periods=None,
        limit=None,
        offset=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of goals using the GET method at the "/goals" endpoint, allowing filtering by parameters such as portfolio, project, task, team, workspace, and time periods.

        Args:
            portfolio (string): Globally unique identifier for supporting portfolio. Example: '159874'.
            project (string): Globally unique identifier for supporting project. Example: '512241'.
            task (string): Globally unique identifier for supporting task. Example: '78424'.
            is_workspace_level (string): Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter. Example: 'false'.
            team (string): Globally unique identifier for the team. Example: '31326'.
            workspace (string): Globally unique identifier for the workspace. Example: '31326'.
            time_periods (string): Globally unique identifiers for the time periods. Example: '221693,506165'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,offset,owner,owner.name,path,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested goals.

        Tags:
            Goals
        """
        url = f"{self.base_url}/goals"
        query_params = {
            k: v
            for k, v in [
                ("portfolio", portfolio),
                ("project", project),
                ("task", task),
                ("is_workspace_level", is_workspace_level),
                ("team", team),
                ("workspace", workspace),
                ("time_periods", time_periods),
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_agoal(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new goal in the system and returns the created resource.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,owner,owner.name,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "due_on": "2019-09-15",
                    "followers": [
                      "12345"
                    ],
                    "gid": "12345",
                    "html_notes": "<body>Start building brand awareness.</body>",
                    "is_workspace_level": true,
                    "liked": false,
                    "name": "Grow web traffic by 30%",
                    "notes": "Start building brand awareness.",
                    "owner": "12345",
                    "resource_type": "task",
                    "start_on": "2019-09-14",
                    "team": "12345",
                    "time_period": "12345",
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new goal.

        Tags:
            Goals
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_agoal_metric(
        self, goal_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Sets a metric for a specific goal identified by `{goal_gid}` and returns the updated goal data.

        Args:
            goal_gid (string): goal_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,owner,owner.name,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "currency_code": "EUR",
                    "current_display_value": "8.12",
                    "current_number_value": 8.12,
                    "gid": "12345",
                    "initial_number_value": 5.2,
                    "is_custom_weight": false,
                    "precision": 2,
                    "progress_source": "manual",
                    "resource_subtype": "number",
                    "resource_type": "task",
                    "target_number_value": 10.2,
                    "unit": "currency"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new goal metric.

        Tags:
            Goals
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/setMetric"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal_metric(
        self, goal_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Sets the current metric value for a specified goal using the "POST" method at the "/goals/{goal_gid}/setMetricCurrentValue" endpoint.

        Args:
            goal_gid (string): goal_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,owner,owner.name,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "current_number_value": 8.12,
                    "gid": "12345",
                    "resource_type": "task"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the goal metric.

        Tags:
            Goals
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/setMetricCurrentValue"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acollaborator_to_agoal(
        self, goal_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds followers to a specific goal using the "POST" method at the "/goals/{goal_gid}/addFollowers" endpoint and returns a status message based on the operation's success or failure.

        Args:
            goal_gid (string): goal_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,owner,owner.name,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "followers": [
                      "13579",
                      "321654"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added users as collaborators.

        Tags:
            Goals
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/addFollowers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acollaborator_from_agoal(
        self, goal_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes followers from a specified goal using the POST method at the "/goals/{goal_gid}/removeFollowers" path.

        Args:
            goal_gid (string): goal_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,owner,owner.name,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "followers": [
                      "13579",
                      "321654"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed users as collaborators.

        Tags:
            Goals
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/removeFollowers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_parent_goals_from_agoal(
        self, goal_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves parent goals associated with a specific goal identified by its goal_gid.

        Args:
            goal_gid (string): goal_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'current_status_update,current_status_update.resource_subtype,current_status_update.title,due_on,followers,followers.name,html_notes,is_workspace_level,liked,likes,likes.user,likes.user.name,metric,metric.can_manage,metric.currency_code,metric.current_display_value,metric.current_number_value,metric.initial_number_value,metric.is_custom_weight,metric.precision,metric.progress_source,metric.resource_subtype,metric.target_number_value,metric.unit,name,notes,num_likes,owner,owner.name,start_on,status,team,team.name,time_period,time_period.display_name,time_period.end_on,time_period.period,time_period.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified goal's parent goals.

        Tags:
            Goals
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        url = f"{self.base_url}/goals/{goal_gid}/parentGoals"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_agoal_relationship(
        self, goal_relationship_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a goal relationship object by its GID, optionally including additional fields in the response, using the Asana API.

        Args:
            goal_relationship_gid (string): goal_relationship_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'contribution_weight,resource_subtype,supported_goal,supported_goal.name,supported_goal.owner,supported_goal.owner.name,supporting_resource,supporting_resource.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the record for the goal relationship.

        Tags:
            Goal relationships
        """
        if goal_relationship_gid is None:
            raise ValueError("Missing required parameter 'goal_relationship_gid'")
        url = f"{self.base_url}/goal_relationships/{goal_relationship_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal_relationship(
        self, goal_relationship_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates a goal relationship using the Asana API and returns a response indicating the outcome of the operation.

        Args:
            goal_relationship_gid (string): goal_relationship_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'contribution_weight,resource_subtype,supported_goal,supported_goal.name,supported_goal.owner,supported_goal.owner.name,supporting_resource,supporting_resource.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "contribution_weight": 1,
                    "gid": "12345",
                    "resource_subtype": "subgoal",
                    "resource_type": "task",
                    "supported_goal": {
                      "gid": "12345",
                      "name": "Grow web traffic by 30%",
                      "owner": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "resource_type": "task"
                    },
                    "supporting_resource": {
                      "gid": "12345",
                      "name": "Stuff to buy",
                      "resource_type": "task"
                    }
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the goal relationship.

        Tags:
            Goal relationships
        """
        if goal_relationship_gid is None:
            raise ValueError("Missing required parameter 'goal_relationship_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goal_relationships/{goal_relationship_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_goal_relationships(
        self,
        opt_pretty=None,
        limit=None,
        offset=None,
        supported_goal=None,
        resource_subtype=None,
        opt_fields=None,
    ) -> dict[str, Any]:
        """
        Retrieves compact goal relationship objects between goals, projects, or portfolios with optional filtering and field selection.

        Args:
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            supported_goal (string): (Required) Globally unique identifier for the supported goal in the goal relationship. Example: '12345'.
            resource_subtype (string): If provided, filter to goal relationships with a given resource_subtype. Example: 'subgoal'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'contribution_weight,offset,path,resource_subtype,supported_goal,supported_goal.name,supported_goal.owner,supported_goal.owner.name,supporting_resource,supporting_resource.name,uri'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested goal relationships.

        Tags:
            Goal relationships
        """
        url = f"{self.base_url}/goal_relationships"
        query_params = {
            k: v
            for k, v in [
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
                ("supported_goal", supported_goal),
                ("resource_subtype", resource_subtype),
                ("opt_fields", opt_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_asupporting_goal_relationship(
        self, goal_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds a supporting relationship to a specified goal using the POST method at the "/goals/{goal_gid}/addSupportingRelationship" endpoint.

        Args:
            goal_gid (string): goal_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'contribution_weight,resource_subtype,supported_goal,supported_goal.name,supported_goal.owner,supported_goal.owner.name,supporting_resource,supporting_resource.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "contribution_weight": 1,
                    "insert_after": "1331",
                    "insert_before": "1331",
                    "supporting_resource": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the goal relationship.

        Tags:
            Goal relationships
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/addSupportingRelationship"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def removes_asupporting_goal_relationship(
        self, goal_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes the supporting relationship from a specified goal and returns a status message.

        Args:
            goal_gid (string): goal_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "supporting_resource": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the goal relationship.

        Tags:
            Goal relationships
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/removeSupportingRelationship"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ajob_by_id(
        self, job_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves job details using the specified job GID, with optional fields and formatting controls, via a GET request to the "/jobs/{job_gid}" endpoint.

        Args:
            job_gid (string): job_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,new_task_template,new_task_template.name,resource_subtype,status'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved Job.

        Tags:
            Jobs
        """
        if job_gid is None:
            raise ValueError("Missing required parameter 'job_gid'")
        url = f"{self.base_url}/jobs/{job_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_memberships(
        self,
        parent=None,
        member=None,
        limit=None,
        offset=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves paginated membership records with optional parent, member, and field selection parameters.

        Args:
            parent (string): Globally unique identifier for `goal`, `project`, or `portfolio`. Example: '159874'.
            member (string): Globally unique identifier for `team` or `user`. Example: '1061493'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'offset,path,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested membership.

        Tags:
            Memberships
        """
        url = f"{self.base_url}/memberships"
        query_params = {
            k: v
            for k, v in [
                ("parent", parent),
                ("member", member),
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_amembership(self, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new membership by sending a POST request to the "/memberships" endpoint, potentially returning a newly created membership resource with a status code indicating successful creation.

        Args:
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "access_level": "editor",
                    "member": "labore velit anim",
                    "parent": "987654",
                    "role": "editor"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the requested membership.

        Tags:
            Memberships
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/memberships"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_amembership(
        self, membership_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves membership details for a specified membership ID, supporting optional field selection and formatted responses.

        Args:
            membership_gid (string): membership_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'access_level,member,member.name,parent,parent.name,resource_subtype'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the record for a single membership.

        Tags:
            Memberships
        """
        if membership_gid is None:
            raise ValueError("Missing required parameter 'membership_gid'")
        url = f"{self.base_url}/memberships/{membership_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_amembership(
        self, membership_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates an existing membership identified by `{membership_gid}` using the PUT method.

        Args:
            membership_gid (string): membership_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "access_level": "editor"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the requested membership.

        Tags:
            Memberships
        """
        if membership_gid is None:
            raise ValueError("Missing required parameter 'membership_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/memberships/{membership_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_amembership(self, membership_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a membership by its GUID using the API, removing the associated relationship between entities.

        Args:
            membership_gid (string): membership_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the requested membership.

        Tags:
            Memberships
        """
        if membership_gid is None:
            raise ValueError("Missing required parameter 'membership_gid'")
        url = f"{self.base_url}/memberships/{membership_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_organization_export_request(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Initiates a request to export an organization's complete data in JSON format, returning a status response upon successful creation.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,download_url,organization,organization.name,state'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "organization": "1331"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created organization export request.

        Tags:
            Organization exports
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organization_exports"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_details_on_an_org_export_request(
        self, organization_export_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves information about an organization export using the provided GID, allowing optional specification of additional fields and pretty-print formatting.

        Args:
            organization_export_gid (string): organization_export_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,download_url,organization,organization.name,state'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved organization export object.

        Tags:
            Organization exports
        """
        if organization_export_gid is None:
            raise ValueError("Missing required parameter 'organization_export_gid'")
        url = f"{self.base_url}/organization_exports/{organization_export_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_portfolios(
        self,
        limit=None,
        offset=None,
        workspace=None,
        owner=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of portfolios with optional filtering and field selection parameters.

        Args:
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            workspace (string): (Required) The workspace or organization to filter portfolios on. Example: '1331'.
            owner (string): The user who owns the portfolio. Currently, API users can only get a list of portfolios that they themselves own, unless the request is made from a Service Account. In the case of a Service Account, if this parameter is specified, then all portfolios owned by this parameter are returned. Otherwise, all portfolios across the workspace are returned. Example: '14916'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,created_by,created_by.name,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,due_on,members,members.name,name,offset,owner,owner.name,path,permalink_url,privacy_setting,project_templates,project_templates.name,public,start_on,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved portfolios.

        Tags:
            Portfolios
        """
        url = f"{self.base_url}/portfolios"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("workspace", workspace),
                ("owner", owner),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aportfolio(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new portfolio and returns the result, optionally including specified fields and formatted output, using the Portfolio API.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,created_by,created_by.name,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,due_on,members,members.name,name,owner,owner.name,permalink_url,privacy_setting,project_templates,project_templates.name,public,start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "color": "light-green",
                    "gid": "12345",
                    "members": [
                      "52164",
                      "15363"
                    ],
                    "name": "Bug Portfolio",
                    "public": false,
                    "resource_type": "task",
                    "workspace": "167589"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created portfolio.

        Tags:
            Portfolios
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio(
        self, portfolio_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves details about a specific portfolio identified by `{portfolio_gid}` using the `GET` method, allowing optional fields (`opt_fields`) and pretty formatting (`opt_pretty`) in the query parameters.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,created_by,created_by.name,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,due_on,members,members.name,name,owner,owner.name,permalink_url,privacy_setting,project_templates,project_templates.name,public,start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aportfolio(
        self, portfolio_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Replaces the entire portfolio resource with the provided data and returns the updated portfolio.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,created_by,created_by.name,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,due_on,members,members.name,name,owner,owner.name,permalink_url,privacy_setting,project_templates,project_templates.name,public,start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "color": "light-green",
                    "gid": "12345",
                    "members": [
                      "52164",
                      "15363"
                    ],
                    "name": "Bug Portfolio",
                    "public": false,
                    "resource_type": "task",
                    "workspace": "167589"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aportfolio(self, portfolio_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes the specified portfolio and returns a success status or error code.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_portfolio_items(
        self, portfolio_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of items associated with a specified portfolio using a GET request, allowing for optional parameters to customize the response fields and pagination.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested portfolio's items.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}/items"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_aportfolio_item(
        self, portfolio_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds an item to a specified portfolio using a POST request, requiring item placement parameters.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "insert_after": "1331",
                    "insert_before": "1331",
                    "item": "1331"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added the item to the portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/addItem"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_aportfolio_item(
        self, portfolio_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes an item from a portfolio using the provided path "/portfolios/{portfolio_gid}/removeItem" via a POST request.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "item": "1331"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the item from the portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/removeItem"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acustom_field_to_aportfolio(
        self, portfolio_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds a custom field to a specified portfolio by creating a custom field setting using the Asana API.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "custom_field": "14916",
                    "insert_after": "1331",
                    "insert_before": "1331",
                    "is_important": true
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added the custom field to the portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/addCustomFieldSetting"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acustom_field_from_aportfolio(
        self, portfolio_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes a custom field setting from a portfolio and returns a success status.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "custom_field": "14916"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the custom field from the portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/removeCustomFieldSetting"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_users_to_aportfolio(
        self, portfolio_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds specified users as members to a portfolio and returns the updated portfolio record.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,created_by,created_by.name,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,due_on,members,members.name,name,owner,owner.name,permalink_url,privacy_setting,project_templates,project_templates.name,public,start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "members": "521621,621373"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added members to the portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/addMembers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_users_from_aportfolio(
        self, portfolio_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes members from a portfolio using the specified portfolio ID and returns a status message.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,created_by,created_by.name,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,due_on,members,members.name,name,owner,owner.name,permalink_url,privacy_setting,project_templates,project_templates.name,public,start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "members": "521621,621373"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the members from the portfolio.

        Tags:
            Portfolios
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/removeMembers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_portfolio_memberships(
        self,
        opt_fields=None,
        portfolio=None,
        workspace=None,
        user=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves portfolio membership details in Asana, including associated users and workspaces, with optional filtering and output field selection.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'access_level,offset,path,portfolio,portfolio.name,uri,user,user.name'.
            portfolio (string): The portfolio to filter results on. Example: '12345'.
            workspace (string): The workspace to filter results on. Example: '12345'.
            user (string): A string identifying a user. This can either be the string "me", an email, or the gid of a user. Example: 'me'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved portfolio memberships.

        Tags:
            Portfolio memberships
        """
        url = f"{self.base_url}/portfolio_memberships"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("portfolio", portfolio),
                ("workspace", workspace),
                ("user", user),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio_membership(
        self, portfolio_membership_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves details about a portfolio membership by its GID, optionally including additional fields and formatted output.

        Args:
            portfolio_membership_gid (string): portfolio_membership_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'access_level,portfolio,portfolio.name,user,user.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested portfolio membership.

        Tags:
            Portfolio memberships
        """
        if portfolio_membership_gid is None:
            raise ValueError("Missing required parameter 'portfolio_membership_gid'")
        url = f"{self.base_url}/portfolio_memberships/{portfolio_membership_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_aportfolio(
        self,
        portfolio_gid,
        opt_fields=None,
        user=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of portfolio memberships for a specific portfolio identified by its GID, allowing for optional filtering by user and customizing the response with additional fields.

        Args:
            portfolio_gid (string): portfolio_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'access_level,offset,path,portfolio,portfolio.name,uri,user,user.name'.
            user (string): A string identifying a user. This can either be the string "me", an email, or the gid of a user. Example: 'me'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested portfolio's memberships.

        Tags:
            Portfolio memberships
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}/portfolio_memberships"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("user", user),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_projects(
        self,
        limit=None,
        offset=None,
        workspace=None,
        team=None,
        archived=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of projects using the specified parameters such as limit, offset, workspace, team, archived status, optional fields, and formatting options.

        Args:
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            workspace (string): The workspace or organization to filter projects on. Example: '1331'.
            team (string): The team to filter projects on. Example: '14916'.
            archived (string): Only return projects whose `archived` field takes on the value of this parameter. Example: 'false'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved projects.

        Tags:
            Projects
        """
        url = f"{self.base_url}/projects"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("workspace", workspace),
                ("team", team),
                ("archived", archived),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new GitLab project with customizable fields and returns a success status upon completion.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "archived": false,
                    "color": "light-green",
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "current_status": {
                      "author": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "color": "complete",
                      "created_at": "2012-02-22T02:06:58.147Z",
                      "created_by": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "gid": "12345",
                      "html_text": "<body>The project <strong>is</strong> moving forward according to plan...</body>",
                      "modified_at": "2012-02-22T02:06:58.147Z",
                      "resource_type": "task",
                      "text": "The project is moving forward according to plan...",
                      "title": "Status Update - Jun 15"
                    },
                    "current_status_update": {
                      "gid": "12345",
                      "resource_subtype": "project_status_update",
                      "resource_type": "task",
                      "title": "Status Update - Jun 15"
                    },
                    "custom_field_settings": [
                      {
                        "custom_field": {
                          "asana_created_field": "priority",
                          "created_by": {
                            "gid": "12345",
                            "name": "Greg Sanchez",
                            "resource_type": "task"
                          },
                          "currency_code": "EUR",
                          "custom_label": "gold pieces",
                          "custom_label_position": "suffix",
                          "date_value": {
                            "date": "2024-08-23",
                            "date_time": "2024-08-23T22:00:00.000Z"
                          },
                          "description": "Development team priority",
                          "display_value": "blue",
                          "enabled": true,
                          "enum_options": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "enum_value": {
                            "color": "blue",
                            "enabled": true,
                            "gid": "12345",
                            "name": "Low",
                            "resource_type": "task"
                          },
                          "format": "custom",
                          "gid": "12345",
                          "has_notifications_enabled": true,
                          "id_prefix": "ID",
                          "is_formula_field": false,
                          "is_global_to_workspace": true,
                          "is_value_read_only": false,
                          "multi_enum_values": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "name": "Status",
                          "number_value": 5.2,
                          "people_value": [
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            },
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            }
                          ],
                          "precision": 2,
                          "representation_type": "number",
                          "resource_subtype": "text",
                          "resource_type": "task",
                          "text_value": "Some Value",
                          "type": "enum"
                        },
                        "gid": "12345",
                        "is_important": false,
                        "parent": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "resource_type": "task"
                      },
                      {
                        "custom_field": {
                          "asana_created_field": "priority",
                          "created_by": {
                            "gid": "12345",
                            "name": "Greg Sanchez",
                            "resource_type": "task"
                          },
                          "currency_code": "EUR",
                          "custom_label": "gold pieces",
                          "custom_label_position": "suffix",
                          "date_value": {
                            "date": "2024-08-23",
                            "date_time": "2024-08-23T22:00:00.000Z"
                          },
                          "description": "Development team priority",
                          "display_value": "blue",
                          "enabled": true,
                          "enum_options": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "enum_value": {
                            "color": "blue",
                            "enabled": true,
                            "gid": "12345",
                            "name": "Low",
                            "resource_type": "task"
                          },
                          "format": "custom",
                          "gid": "12345",
                          "has_notifications_enabled": true,
                          "id_prefix": "ID",
                          "is_formula_field": false,
                          "is_global_to_workspace": true,
                          "is_value_read_only": false,
                          "multi_enum_values": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "name": "Status",
                          "number_value": 5.2,
                          "people_value": [
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            },
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            }
                          ],
                          "precision": 2,
                          "representation_type": "number",
                          "resource_subtype": "text",
                          "resource_type": "task",
                          "text_value": "Some Value",
                          "type": "people"
                        },
                        "gid": "12345",
                        "is_important": false,
                        "parent": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "resource_type": "task"
                      }
                    ],
                    "custom_fields": {
                      "4578152156": "Not Started",
                      "5678904321": "On Hold"
                    },
                    "default_access_level": "admin",
                    "default_view": "calendar",
                    "due_date": "2019-09-15",
                    "due_on": "2019-09-15",
                    "followers": "12345,23456",
                    "gid": "12345",
                    "html_notes": "<body>These are things we need to purchase.</body>",
                    "members": [
                      {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      }
                    ],
                    "minimum_access_level_for_customization": "admin",
                    "minimum_access_level_for_sharing": "admin",
                    "modified_at": "2012-02-22T02:06:58.147Z",
                    "name": "Stuff to buy",
                    "notes": "These are things we need to purchase.",
                    "owner": "12345",
                    "privacy_setting": "public_to_workspace",
                    "public": false,
                    "resource_type": "task",
                    "start_on": "2019-09-14",
                    "team": "12345",
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully retrieved projects.

        Tags:
            Projects
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific project's details using its unique identifier (project_gid) with options to customize the response fields and formatting.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates an existing project at the specified path, replacing its entire resource with the provided request content, using the PUT method.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "archived": false,
                    "color": "light-green",
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "current_status": {
                      "author": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "color": "red",
                      "created_at": "2012-02-22T02:06:58.147Z",
                      "created_by": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "gid": "12345",
                      "html_text": "<body>The project <strong>is</strong> moving forward according to plan...</body>",
                      "modified_at": "2012-02-22T02:06:58.147Z",
                      "resource_type": "task",
                      "text": "The project is moving forward according to plan...",
                      "title": "Status Update - Jun 15"
                    },
                    "current_status_update": {
                      "gid": "12345",
                      "resource_subtype": "project_status_update",
                      "resource_type": "task",
                      "title": "Status Update - Jun 15"
                    },
                    "custom_field_settings": [
                      {
                        "custom_field": {
                          "asana_created_field": "priority",
                          "created_by": {
                            "gid": "12345",
                            "name": "Greg Sanchez",
                            "resource_type": "task"
                          },
                          "currency_code": "EUR",
                          "custom_label": "gold pieces",
                          "custom_label_position": "suffix",
                          "date_value": {
                            "date": "2024-08-23",
                            "date_time": "2024-08-23T22:00:00.000Z"
                          },
                          "description": "Development team priority",
                          "display_value": "blue",
                          "enabled": true,
                          "enum_options": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "enum_value": {
                            "color": "blue",
                            "enabled": true,
                            "gid": "12345",
                            "name": "Low",
                            "resource_type": "task"
                          },
                          "format": "custom",
                          "gid": "12345",
                          "has_notifications_enabled": true,
                          "id_prefix": "ID",
                          "is_formula_field": false,
                          "is_global_to_workspace": true,
                          "is_value_read_only": false,
                          "multi_enum_values": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "name": "Status",
                          "number_value": 5.2,
                          "people_value": [
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            },
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            }
                          ],
                          "precision": 2,
                          "representation_type": "number",
                          "resource_subtype": "text",
                          "resource_type": "task",
                          "text_value": "Some Value",
                          "type": "enum"
                        },
                        "gid": "12345",
                        "is_important": false,
                        "parent": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "resource_type": "task"
                      },
                      {
                        "custom_field": {
                          "asana_created_field": "priority",
                          "created_by": {
                            "gid": "12345",
                            "name": "Greg Sanchez",
                            "resource_type": "task"
                          },
                          "currency_code": "EUR",
                          "custom_label": "gold pieces",
                          "custom_label_position": "suffix",
                          "date_value": {
                            "date": "2024-08-23",
                            "date_time": "2024-08-23T22:00:00.000Z"
                          },
                          "description": "Development team priority",
                          "display_value": "blue",
                          "enabled": true,
                          "enum_options": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "enum_value": {
                            "color": "blue",
                            "enabled": true,
                            "gid": "12345",
                            "name": "Low",
                            "resource_type": "task"
                          },
                          "format": "custom",
                          "gid": "12345",
                          "has_notifications_enabled": true,
                          "id_prefix": "ID",
                          "is_formula_field": false,
                          "is_global_to_workspace": true,
                          "is_value_read_only": false,
                          "multi_enum_values": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "name": "Status",
                          "number_value": 5.2,
                          "people_value": [
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            },
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            }
                          ],
                          "precision": 2,
                          "representation_type": "number",
                          "resource_subtype": "text",
                          "resource_type": "task",
                          "text_value": "Some Value",
                          "type": "date"
                        },
                        "gid": "12345",
                        "is_important": false,
                        "parent": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "resource_type": "task"
                      }
                    ],
                    "custom_fields": {
                      "4578152156": "Not Started",
                      "5678904321": "On Hold"
                    },
                    "default_access_level": "admin",
                    "default_view": "calendar",
                    "due_date": "2019-09-15",
                    "due_on": "2019-09-15",
                    "followers": "12345,23456",
                    "gid": "12345",
                    "html_notes": "<body>These are things we need to purchase.</body>",
                    "members": [
                      {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      }
                    ],
                    "minimum_access_level_for_customization": "admin",
                    "minimum_access_level_for_sharing": "admin",
                    "modified_at": "2012-02-22T02:06:58.147Z",
                    "name": "Stuff to buy",
                    "notes": "These are things we need to purchase.",
                    "owner": "12345",
                    "privacy_setting": "public_to_workspace",
                    "public": false,
                    "resource_type": "task",
                    "start_on": "2019-09-14",
                    "team": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject(self, project_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a project identified by the project GID using the DELETE method at the path "/projects/{project_gid}", with optional support for pretty-printed output.

        Args:
            project_gid (string): project_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a duplicate of the specified project, including its structure and dependencies, while allowing optional field customization.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,new_task_template,new_task_template.name,resource_subtype,status'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "include": "g,g",
                    "name": "New Project Name",
                    "schedule_dates": {
                      "due_on": "2019-05-21",
                      "should_skip_weekends": true,
                      "start_on": "2019-05-21"
                    },
                    "team": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the job to handle duplication.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/duplicate"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_projects_atask_is_in(
        self, task_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves the projects associated with a specific task using the GET method, allowing for optional customization of output fields and pagination.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the projects for the given task.

        Tags:
            Projects
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/projects"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_sprojects(
        self,
        team_gid,
        limit=None,
        offset=None,
        archived=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of projects associated with a specific team, supporting optional filtering for archived status and custom field selection.

        Args:
            team_gid (string): team_gid
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            archived (string): Only return projects whose `archived` field takes on the value of this parameter. Example: 'false'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested team's projects.

        Tags:
            Projects
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}/projects"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("archived", archived),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_in_ateam(
        self, team_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds a project to a team using the GitHub API and returns a success status.

        Args:
            team_gid (string): team_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "archived": false,
                    "color": "light-green",
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "current_status": {
                      "author": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "color": "complete",
                      "created_at": "2012-02-22T02:06:58.147Z",
                      "created_by": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "gid": "12345",
                      "html_text": "<body>The project <strong>is</strong> moving forward according to plan...</body>",
                      "modified_at": "2012-02-22T02:06:58.147Z",
                      "resource_type": "task",
                      "text": "The project is moving forward according to plan...",
                      "title": "Status Update - Jun 15"
                    },
                    "current_status_update": {
                      "gid": "12345",
                      "resource_subtype": "project_status_update",
                      "resource_type": "task",
                      "title": "Status Update - Jun 15"
                    },
                    "custom_field_settings": [
                      {
                        "custom_field": {
                          "asana_created_field": "priority",
                          "created_by": {
                            "gid": "12345",
                            "name": "Greg Sanchez",
                            "resource_type": "task"
                          },
                          "currency_code": "EUR",
                          "custom_label": "gold pieces",
                          "custom_label_position": "suffix",
                          "date_value": {
                            "date": "2024-08-23",
                            "date_time": "2024-08-23T22:00:00.000Z"
                          },
                          "description": "Development team priority",
                          "display_value": "blue",
                          "enabled": true,
                          "enum_options": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "enum_value": {
                            "color": "blue",
                            "enabled": true,
                            "gid": "12345",
                            "name": "Low",
                            "resource_type": "task"
                          },
                          "format": "custom",
                          "gid": "12345",
                          "has_notifications_enabled": true,
                          "id_prefix": "ID",
                          "is_formula_field": false,
                          "is_global_to_workspace": true,
                          "is_value_read_only": false,
                          "multi_enum_values": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "name": "Status",
                          "number_value": 5.2,
                          "people_value": [
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            },
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            }
                          ],
                          "precision": 2,
                          "representation_type": "number",
                          "resource_subtype": "text",
                          "resource_type": "task",
                          "text_value": "Some Value",
                          "type": "enum"
                        },
                        "gid": "12345",
                        "is_important": false,
                        "parent": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "resource_type": "task"
                      },
                      {
                        "custom_field": {
                          "asana_created_field": "priority",
                          "created_by": {
                            "gid": "12345",
                            "name": "Greg Sanchez",
                            "resource_type": "task"
                          },
                          "currency_code": "EUR",
                          "custom_label": "gold pieces",
                          "custom_label_position": "suffix",
                          "date_value": {
                            "date": "2024-08-23",
                            "date_time": "2024-08-23T22:00:00.000Z"
                          },
                          "description": "Development team priority",
                          "display_value": "blue",
                          "enabled": true,
                          "enum_options": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "enum_value": {
                            "color": "blue",
                            "enabled": true,
                            "gid": "12345",
                            "name": "Low",
                            "resource_type": "task"
                          },
                          "format": "custom",
                          "gid": "12345",
                          "has_notifications_enabled": true,
                          "id_prefix": "ID",
                          "is_formula_field": false,
                          "is_global_to_workspace": true,
                          "is_value_read_only": false,
                          "multi_enum_values": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "name": "Status",
                          "number_value": 5.2,
                          "people_value": [
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            },
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            }
                          ],
                          "precision": 2,
                          "representation_type": "number",
                          "resource_subtype": "text",
                          "resource_type": "task",
                          "text_value": "Some Value",
                          "type": "people"
                        },
                        "gid": "12345",
                        "is_important": false,
                        "parent": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "resource_type": "task"
                      }
                    ],
                    "custom_fields": {
                      "4578152156": "Not Started",
                      "5678904321": "On Hold"
                    },
                    "default_access_level": "admin",
                    "default_view": "calendar",
                    "due_date": "2019-09-15",
                    "due_on": "2019-09-15",
                    "followers": "12345,23456",
                    "gid": "12345",
                    "html_notes": "<body>These are things we need to purchase.</body>",
                    "members": [
                      {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      }
                    ],
                    "minimum_access_level_for_customization": "admin",
                    "minimum_access_level_for_sharing": "admin",
                    "modified_at": "2012-02-22T02:06:58.147Z",
                    "name": "Stuff to buy",
                    "notes": "These are things we need to purchase.",
                    "owner": "12345",
                    "privacy_setting": "public_to_workspace",
                    "public": false,
                    "resource_type": "task",
                    "start_on": "2019-09-14",
                    "team": "12345",
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the specified project.

        Tags:
            Projects
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams/{team_gid}/projects"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_projects_in_aworkspace(
        self,
        workspace_gid,
        limit=None,
        offset=None,
        archived=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of projects for a specified workspace, allowing customization through parameters such as limit, offset, archived status, and optional fields, using the GET method.

        Args:
            workspace_gid (string): workspace_gid
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            archived (string): Only return projects whose `archived` field takes on the value of this parameter. Example: 'false'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested workspace's projects.

        Tags:
            Projects
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/projects"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("archived", archived),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_in_aworkspace(
        self, workspace_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new project within the specified workspace using optional query parameters to control response fields and formatting.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "archived": false,
                    "color": "light-green",
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "current_status": {
                      "author": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "color": "complete",
                      "created_at": "2012-02-22T02:06:58.147Z",
                      "created_by": {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      "gid": "12345",
                      "html_text": "<body>The project <strong>is</strong> moving forward according to plan...</body>",
                      "modified_at": "2012-02-22T02:06:58.147Z",
                      "resource_type": "task",
                      "text": "The project is moving forward according to plan...",
                      "title": "Status Update - Jun 15"
                    },
                    "current_status_update": {
                      "gid": "12345",
                      "resource_subtype": "project_status_update",
                      "resource_type": "task",
                      "title": "Status Update - Jun 15"
                    },
                    "custom_field_settings": [
                      {
                        "custom_field": {
                          "asana_created_field": "priority",
                          "created_by": {
                            "gid": "12345",
                            "name": "Greg Sanchez",
                            "resource_type": "task"
                          },
                          "currency_code": "EUR",
                          "custom_label": "gold pieces",
                          "custom_label_position": "suffix",
                          "date_value": {
                            "date": "2024-08-23",
                            "date_time": "2024-08-23T22:00:00.000Z"
                          },
                          "description": "Development team priority",
                          "display_value": "blue",
                          "enabled": true,
                          "enum_options": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "enum_value": {
                            "color": "blue",
                            "enabled": true,
                            "gid": "12345",
                            "name": "Low",
                            "resource_type": "task"
                          },
                          "format": "custom",
                          "gid": "12345",
                          "has_notifications_enabled": true,
                          "id_prefix": "ID",
                          "is_formula_field": false,
                          "is_global_to_workspace": true,
                          "is_value_read_only": false,
                          "multi_enum_values": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "name": "Status",
                          "number_value": 5.2,
                          "people_value": [
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            },
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            }
                          ],
                          "precision": 2,
                          "representation_type": "number",
                          "resource_subtype": "text",
                          "resource_type": "task",
                          "text_value": "Some Value",
                          "type": "enum"
                        },
                        "gid": "12345",
                        "is_important": false,
                        "parent": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "resource_type": "task"
                      },
                      {
                        "custom_field": {
                          "asana_created_field": "priority",
                          "created_by": {
                            "gid": "12345",
                            "name": "Greg Sanchez",
                            "resource_type": "task"
                          },
                          "currency_code": "EUR",
                          "custom_label": "gold pieces",
                          "custom_label_position": "suffix",
                          "date_value": {
                            "date": "2024-08-23",
                            "date_time": "2024-08-23T22:00:00.000Z"
                          },
                          "description": "Development team priority",
                          "display_value": "blue",
                          "enabled": true,
                          "enum_options": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "enum_value": {
                            "color": "blue",
                            "enabled": true,
                            "gid": "12345",
                            "name": "Low",
                            "resource_type": "task"
                          },
                          "format": "custom",
                          "gid": "12345",
                          "has_notifications_enabled": true,
                          "id_prefix": "ID",
                          "is_formula_field": false,
                          "is_global_to_workspace": true,
                          "is_value_read_only": false,
                          "multi_enum_values": [
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            },
                            {
                              "color": "blue",
                              "enabled": true,
                              "gid": "12345",
                              "name": "Low",
                              "resource_type": "task"
                            }
                          ],
                          "name": "Status",
                          "number_value": 5.2,
                          "people_value": [
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            },
                            {
                              "gid": "12345",
                              "name": "Greg Sanchez",
                              "resource_type": "task"
                            }
                          ],
                          "precision": 2,
                          "representation_type": "number",
                          "resource_subtype": "text",
                          "resource_type": "task",
                          "text_value": "Some Value",
                          "type": "people"
                        },
                        "gid": "12345",
                        "is_important": false,
                        "parent": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "resource_type": "task"
                      }
                    ],
                    "custom_fields": {
                      "4578152156": "Not Started",
                      "5678904321": "On Hold"
                    },
                    "default_access_level": "admin",
                    "default_view": "calendar",
                    "due_date": "2019-09-15",
                    "due_on": "2019-09-15",
                    "followers": "12345,23456",
                    "gid": "12345",
                    "html_notes": "<body>These are things we need to purchase.</body>",
                    "members": [
                      {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "name": "Greg Sanchez",
                        "resource_type": "task"
                      }
                    ],
                    "minimum_access_level_for_customization": "admin",
                    "minimum_access_level_for_sharing": "admin",
                    "modified_at": "2012-02-22T02:06:58.147Z",
                    "name": "Stuff to buy",
                    "notes": "These are things we need to purchase.",
                    "owner": "12345",
                    "privacy_setting": "public_to_workspace",
                    "public": false,
                    "resource_type": "task",
                    "start_on": "2019-09-14",
                    "team": "12345",
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new project in the specified workspace.

        Tags:
            Projects
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}/projects"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acustom_field_to_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds a custom field setting to a specified project using the POST method via the API endpoint "/projects/{project_gid}/addCustomFieldSetting", allowing optional query parameters for field selection and response formatting.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'custom_field,custom_field.asana_created_field,custom_field.created_by,custom_field.created_by.name,custom_field.currency_code,custom_field.custom_label,custom_field.custom_label_position,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.description,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.format,custom_field.has_notifications_enabled,custom_field.id_prefix,custom_field.is_formula_field,custom_field.is_global_to_workspace,custom_field.is_value_read_only,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.people_value,custom_field.people_value.name,custom_field.precision,custom_field.representation_type,custom_field.resource_subtype,custom_field.text_value,custom_field.type,is_important,parent,parent.name,project,project.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "custom_field": "14916",
                    "insert_after": "1331",
                    "insert_before": "1331",
                    "is_important": true
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added the custom field to the project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/addCustomFieldSetting"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acustom_field_from_aproject(
        self, project_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes a custom field setting from a specified project using the Asana API by sending a POST request to the "/projects/{project_gid}/removeCustomFieldSetting" endpoint.

        Args:
            project_gid (string): project_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "custom_field": "14916"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the custom field from the project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/removeCustomFieldSetting"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_task_count_of_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves task counts for a specified project using the Asana API, allowing users to obtain an object containing task count fields by opting in with the `opt_fields` parameter.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'num_completed_milestones,num_completed_tasks,num_incomplete_milestones,num_incomplete_tasks,num_milestones,num_tasks'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested project's task counts.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/task_counts"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_users_to_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds members to a project specified by its project GID using the POST method.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "members": "521621,621373"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added members to the project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/addMembers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_users_from_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes specified members from a project using their identifiers and returns an updated project object or error status.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "members": "521621,621373"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the members from the project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/removeMembers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_followers_to_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds specified users as followers to a project and returns a success or error status.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "followers": "521621,621373"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added followers to the project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/addFollowers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_followers_from_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes specified followers from a project identified by its GID, updating the project's record without affecting its membership status.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "followers": "521621,621373"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed followers from the project.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/removeFollowers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_template_from_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Saves a project as a template using the POST method at "/projects/{project_gid}/saveAsTemplate," allowing for the creation of new projects with predefined structures based on existing projects.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,new_task_template,new_task_template.name,resource_subtype,status'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "name": "New Project Template",
                    "public": true,
                    "team": "12345",
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the job to handle project template creation.

        Tags:
            Projects
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/saveAsTemplate"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_brief(
        self, project_brief_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific project brief identified by its unique identifier and returns its details, optionally including additional fields or formatted responses.

        Args:
            project_brief_gid (string): project_brief_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'html_text,permalink_url,project,project.name,text,title'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the record for a project brief.

        Tags:
            Project briefs
        """
        if project_brief_gid is None:
            raise ValueError("Missing required parameter 'project_brief_gid'")
        url = f"{self.base_url}/project_briefs/{project_brief_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aproject_brief(
        self, project_brief_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates or replaces a project brief with the specified ID and returns the modified resource.

        Args:
            project_brief_gid (string): project_brief_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'html_text,permalink_url,project,project.name,text,title'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "gid": "12345",
                    "html_text": "<body>This is a <strong>project brief</strong>.</body>",
                    "resource_type": "task",
                    "text": "This is a project brief.",
                    "title": "Stuff to buy \u2014 Project Brief"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the project brief.

        Tags:
            Project briefs
        """
        if project_brief_gid is None:
            raise ValueError("Missing required parameter 'project_brief_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/project_briefs/{project_brief_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_brief(
        self, project_brief_gid, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Deletes a specific project brief identified by its GID using the Asana API and returns an empty data record upon successful deletion.

        Args:
            project_brief_gid (string): project_brief_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified project brief.

        Tags:
            Project briefs
        """
        if project_brief_gid is None:
            raise ValueError("Missing required parameter 'project_brief_gid'")
        url = f"{self.base_url}/project_briefs/{project_brief_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_brief(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a project brief for the specified project using the provided data and returns the newly created brief.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'html_text,permalink_url,project,project.name,text,title'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "gid": "12345",
                    "html_text": "<body>This is a <strong>project brief</strong>.</body>",
                    "resource_type": "task",
                    "text": "This is a project brief.",
                    "title": "Stuff to buy \u2014 Project Brief"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new project brief.

        Tags:
            Project briefs
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/project_briefs"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_membership(
        self, project_membership_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves details of a specific project membership by its ID, including optional fields and formatted output.

        Args:
            project_membership_gid (string): project_membership_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'access_level,member,member.name,parent,parent.name,project,project.name,user,user.name,write_access'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested project membership.

        Tags:
            Project memberships
        """
        if project_membership_gid is None:
            raise ValueError("Missing required parameter 'project_membership_gid'")
        url = f"{self.base_url}/project_memberships/{project_membership_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_aproject(
        self,
        project_gid,
        opt_fields=None,
        user=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of project memberships with optional query parameters for filtering and pagination.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'access_level,member,member.name,offset,parent,parent.name,path,uri'.
            user (string): A string identifying a user. This can either be the string "me", an email, or the gid of a user. Example: 'me'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested project's memberships.

        Tags:
            Project memberships
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/project_memberships"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("user", user),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_status(
        self, project_status_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific project status by its GID using the "GET" method, allowing for optional fields and pretty-printing.

        Args:
            project_status_gid (string): project_status_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'author,author.name,color,created_at,created_by,created_by.name,html_text,modified_at,text,title'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified project's status updates.

        Tags:
            Project statuses
        """
        if project_status_gid is None:
            raise ValueError("Missing required parameter 'project_status_gid'")
        url = f"{self.base_url}/project_statuses/{project_status_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_status(
        self, project_status_gid, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Deletes a specific project status by its GID and returns an empty response upon success.

        Args:
            project_status_gid (string): project_status_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified project status.

        Tags:
            Project statuses
        """
        if project_status_gid is None:
            raise ValueError("Missing required parameter 'project_status_gid'")
        url = f"{self.base_url}/project_statuses/{project_status_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_statuses_from_aproject(
        self, project_gid, opt_pretty=None, limit=None, offset=None, opt_fields=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of project statuses for a specified project and returns paginated results with optional field filtering.

        Args:
            project_gid (string): project_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'author,author.name,color,created_at,created_by,created_by.name,html_text,modified_at,offset,path,text,title,uri'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified project's status updates.

        Tags:
            Project statuses
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/project_statuses"
        query_params = {
            k: v
            for k, v in [
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_status(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new project status for the specified project and returns the created status, supporting optional field selection and pretty-printed responses.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'author,author.name,color,created_at,created_by,created_by.name,html_text,modified_at,text,title'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "color": "complete",
                    "gid": "12345",
                    "html_text": "<body>The project <strong>is</strong> moving forward according to plan...</body>",
                    "resource_type": "task",
                    "text": "The project is moving forward according to plan...",
                    "title": "Status Update - Jun 15"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new story.

        Tags:
            Project statuses
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/project_statuses"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_template(
        self, project_template_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific project template by its unique identifier, providing configurable output fields and formatted responses.

        Args:
            project_template_gid (string): project_template_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,description,html_description,name,owner,public,requested_dates,requested_dates.description,requested_dates.name,requested_roles,requested_roles.name,team,team.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested project template.

        Tags:
            Project templates
        """
        if project_template_gid is None:
            raise ValueError("Missing required parameter 'project_template_gid'")
        url = f"{self.base_url}/project_templates/{project_template_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_template(
        self, project_template_gid, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Deletes an existing project template using the Asana API and returns an empty data record.

        Args:
            project_template_gid (string): project_template_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified project template.

        Tags:
            Project templates
        """
        if project_template_gid is None:
            raise ValueError("Missing required parameter 'project_template_gid'")
        url = f"{self.base_url}/project_templates/{project_template_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_project_templates(
        self,
        workspace=None,
        team=None,
        limit=None,
        offset=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of project templates, optionally filtered by workspace or team, with support for pagination and field selection.

        Args:
            workspace (string): The workspace to filter results on. Example: '12345'.
            team (string): The team to filter projects on. Example: '14916'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,description,html_description,name,offset,owner,path,public,requested_dates,requested_dates.description,requested_dates.name,requested_roles,requested_roles.name,team,team.name,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested team's or workspace's project templates.

        Tags:
            Project templates
        """
        url = f"{self.base_url}/project_templates"
        query_params = {
            k: v
            for k, v in [
                ("workspace", workspace),
                ("team", team),
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_sproject_templates(
        self, team_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of project templates associated with a specific team, supporting optional filtering and field customization.

        Args:
            team_gid (string): team_gid
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,description,html_description,name,offset,owner,path,public,requested_dates,requested_dates.description,requested_dates.name,requested_roles,requested_roles.name,team,team.name,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested team's project templates.

        Tags:
            Project templates
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}/project_templates"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def instantiate_aproject_from_aproject_template(
        self, project_template_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Instantiates a project template using the Asana API, creating a new project based on the specified template and optionally including additional fields and formatting options.

        Args:
            project_template_gid (string): project_template_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,new_task_template,new_task_template.name,resource_subtype,status'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "is_strict": true,
                    "name": "New Project Name",
                    "privacy_setting": "public_to_workspace",
                    "public": true,
                    "requested_dates": [
                      {
                        "gid": "1",
                        "value": "2010-03-22T06:29:02.176Z"
                      },
                      {
                        "gid": "1",
                        "value": "1998-03-28T04:45:29.888Z"
                      }
                    ],
                    "requested_roles": [
                      {
                        "gid": "1",
                        "value": "123"
                      },
                      {
                        "gid": "1",
                        "value": "123"
                      }
                    ],
                    "team": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the job to handle project instantiation.

        Tags:
            Project templates
        """
        if project_template_gid is None:
            raise ValueError("Missing required parameter 'project_template_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/project_templates/{project_template_gid}/instantiateProject"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def trigger_arule(self, rule_trigger_gid, data=None) -> dict[str, Any]:
        """
        Triggers the execution of a specific rule using the API defined at the path "/rule_triggers/{rule_trigger_gid}/run" via a POST request.

        Args:
            rule_trigger_gid (string): rule_trigger_gid
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "action_data": {
                      "jira_ticket_id": "123",
                      "jira_ticket_name": "Test"
                    },
                    "resource": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully triggered a rule.

        Tags:
            Rules
        """
        if rule_trigger_gid is None:
            raise ValueError("Missing required parameter 'rule_trigger_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/rule_triggers/{rule_trigger_gid}/run"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_asection(
        self, section_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves information about a specific section using the "GET" method at the "/sections/{section_gid}" endpoint, optionally allowing customization with additional fields and pretty-printing.

        Args:
            section_gid (string): section_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,name,project,project.name,projects,projects.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved section.

        Tags:
            Sections
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        url = f"{self.base_url}/sections/{section_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_asection(
        self, section_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates or replaces a specific section resource identified by its GID, returning relevant status messages based on success or failure, with optional parameters for customizing output fields and formatting.

        Args:
            section_gid (string): section_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,name,project,project.name,projects,projects.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "insert_after": "987654",
                    "insert_before": "86420",
                    "name": "Next Actions"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the specified section.

        Tags:
            Sections
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/sections/{section_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_asection(self, section_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes the specified section identified by its global ID and returns a success or error status.

        Args:
            section_gid (string): section_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified section.

        Tags:
            Sections
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        url = f"{self.base_url}/sections/{section_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sections_in_aproject(
        self, project_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of sections associated with a specific project, supporting optional query parameters for pagination and field customization.

        Args:
            project_gid (string): project_gid
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,name,offset,path,project,project.name,projects,projects.name,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved sections in project.

        Tags:
            Sections
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/sections"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_asection_in_aproject(
        self, project_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new section in a specified project using the Asana API and returns a status message.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,name,project,project.name,projects,projects.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "insert_after": "987654",
                    "insert_before": "86420",
                    "name": "Next Actions"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the specified section.

        Tags:
            Sections
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/sections"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_task_to_section(
        self, section_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds a task to the specified section using the POST method.

        Args:
            section_gid (string): section_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "insert_after": "987654",
                    "insert_before": "86420",
                    "task": "123456"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added the task.

        Tags:
            Sections
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/sections/{section_gid}/addTask"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def move_or_insert_sections(
        self, project_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Inserts a new section into a specific project and returns the operation's status.

        Args:
            project_gid (string): project_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "after_section": "987654",
                    "before_section": "86420",
                    "section": "321654"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully moved the specified section.

        Tags:
            Sections
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/sections/insert"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_astatus_update(
        self, status_update_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific status update's details and associated metadata based on the provided status update identifier.

        Args:
            status_update_gid (string): status_update_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'author,author.name,created_at,created_by,created_by.name,hearted,hearts,hearts.user,hearts.user.name,html_text,liked,likes,likes.user,likes.user.name,modified_at,num_hearts,num_likes,parent,parent.name,resource_subtype,status_type,text,title'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified object's status updates.

        Tags:
            Status updates
        """
        if status_update_gid is None:
            raise ValueError("Missing required parameter 'status_update_gid'")
        url = f"{self.base_url}/status_updates/{status_update_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_astatus_update(
        self, status_update_gid, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Deletes a specific status update identified by its GID and returns a response based on the operation's success or failure.

        Args:
            status_update_gid (string): status_update_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified status.

        Tags:
            Status updates
        """
        if status_update_gid is None:
            raise ValueError("Missing required parameter 'status_update_gid'")
        url = f"{self.base_url}/status_updates/{status_update_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_status_updates_from_an_object(
        self,
        parent=None,
        created_since=None,
        opt_fields=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves status updates with filtering options for parent, creation date, and other parameters, returning paginated results.

        Args:
            parent (string): (Required) Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal. Example: '159874'.
            created_since (string): Only return statuses that have been created since the given time. Example: '2012-02-22T02:06:58.158Z'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'author,author.name,created_at,created_by,created_by.name,hearted,hearts,hearts.user,hearts.user.name,html_text,liked,likes,likes.user,likes.user.name,modified_at,num_hearts,num_likes,offset,parent,parent.name,path,resource_subtype,status_type,text,title,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified object's status updates.

        Tags:
            Status updates
        """
        url = f"{self.base_url}/status_updates"
        query_params = {
            k: v
            for k, v in [
                ("parent", parent),
                ("created_since", created_since),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_astatus_update(
        self, opt_fields=None, opt_pretty=None, limit=None, offset=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a status update with optional fields, pagination controls, and returns success or error responses based on provided parameters.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'author,author.name,created_at,created_by,created_by.name,hearted,hearts,hearts.user,hearts.user.name,html_text,liked,likes,likes.user,likes.user.name,modified_at,num_hearts,num_likes,parent,parent.name,resource_subtype,status_type,text,title'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "gid": "12345",
                    "html_text": "<body>The project <strong>is</strong> moving forward according to plan...</body>",
                    "parent": "ut ut",
                    "resource_subtype": "project_status_update",
                    "resource_type": "task",
                    "status_type": "on_hold",
                    "text": "The project is moving forward according to plan...",
                    "title": "Status Update - Jun 15"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new status update.

        Tags:
            Status updates
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/status_updates"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_astory(self, story_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a specific story by its globally unique identifier (GID) with optional fields and formatting parameters.

        Args:
            story_gid (string): story_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'assignee,assignee.name,created_at,created_by,created_by.name,custom_field,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.id_prefix,custom_field.is_formula_field,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.representation_type,custom_field.resource_subtype,custom_field.text_value,custom_field.type,dependency,dependency.created_by,dependency.name,dependency.resource_subtype,duplicate_of,duplicate_of.created_by,duplicate_of.name,duplicate_of.resource_subtype,duplicated_from,duplicated_from.created_by,duplicated_from.name,duplicated_from.resource_subtype,follower,follower.name,hearted,hearts,hearts.user,hearts.user.name,html_text,is_editable,is_edited,is_pinned,liked,likes,likes.user,likes.user.name,new_approval_status,new_date_value,new_dates,new_dates.due_at,new_dates.due_on,new_dates.start_on,new_enum_value,new_enum_value.color,new_enum_value.enabled,new_enum_value.name,new_multi_enum_values,new_multi_enum_values.color,new_multi_enum_values.enabled,new_multi_enum_values.name,new_name,new_number_value,new_people_value,new_people_value.name,new_resource_subtype,new_section,new_section.name,new_text_value,num_hearts,num_likes,old_approval_status,old_date_value,old_dates,old_dates.due_at,old_dates.due_on,old_dates.start_on,old_enum_value,old_enum_value.color,old_enum_value.enabled,old_enum_value.name,old_multi_enum_values,old_multi_enum_values.color,old_multi_enum_values.enabled,old_multi_enum_values.name,old_name,old_number_value,old_people_value,old_people_value.name,old_resource_subtype,old_section,old_section.name,old_text_value,previews,previews.fallback,previews.footer,previews.header,previews.header_link,previews.html_text,previews.text,previews.title,previews.title_link,project,project.name,resource_subtype,source,sticker_name,story,story.created_at,story.created_by,story.created_by.name,story.resource_subtype,story.text,tag,tag.name,target,target.created_by,target.name,target.resource_subtype,task,task.created_by,task.name,task.resource_subtype,text,type'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified story.

        Tags:
            Stories
        """
        if story_gid is None:
            raise ValueError("Missing required parameter 'story_gid'")
        url = f"{self.base_url}/stories/{story_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_astory(
        self, story_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates or creates a story at the specified path "/stories/{story_gid}" using the provided data.

        Args:
            story_gid (string): story_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'assignee,assignee.name,created_at,created_by,created_by.name,custom_field,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.id_prefix,custom_field.is_formula_field,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.representation_type,custom_field.resource_subtype,custom_field.text_value,custom_field.type,dependency,dependency.created_by,dependency.name,dependency.resource_subtype,duplicate_of,duplicate_of.created_by,duplicate_of.name,duplicate_of.resource_subtype,duplicated_from,duplicated_from.created_by,duplicated_from.name,duplicated_from.resource_subtype,follower,follower.name,hearted,hearts,hearts.user,hearts.user.name,html_text,is_editable,is_edited,is_pinned,liked,likes,likes.user,likes.user.name,new_approval_status,new_date_value,new_dates,new_dates.due_at,new_dates.due_on,new_dates.start_on,new_enum_value,new_enum_value.color,new_enum_value.enabled,new_enum_value.name,new_multi_enum_values,new_multi_enum_values.color,new_multi_enum_values.enabled,new_multi_enum_values.name,new_name,new_number_value,new_people_value,new_people_value.name,new_resource_subtype,new_section,new_section.name,new_text_value,num_hearts,num_likes,old_approval_status,old_date_value,old_dates,old_dates.due_at,old_dates.due_on,old_dates.start_on,old_enum_value,old_enum_value.color,old_enum_value.enabled,old_enum_value.name,old_multi_enum_values,old_multi_enum_values.color,old_multi_enum_values.enabled,old_multi_enum_values.name,old_name,old_number_value,old_people_value,old_people_value.name,old_resource_subtype,old_section,old_section.name,old_text_value,previews,previews.fallback,previews.footer,previews.header,previews.header_link,previews.html_text,previews.text,previews.title,previews.title_link,project,project.name,resource_subtype,source,sticker_name,story,story.created_at,story.created_by,story.created_by.name,story.resource_subtype,story.text,tag,tag.name,target,target.created_by,target.name,target.resource_subtype,task,task.created_by,task.name,task.resource_subtype,text,type'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "gid": "12345",
                    "html_text": "<body>This is a comment.</body>",
                    "is_pinned": false,
                    "resource_subtype": "comment_added",
                    "resource_type": "task",
                    "sticker_name": "dancing_unicorn",
                    "text": "This is a comment."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully retrieved the specified story.

        Tags:
            Stories
        """
        if story_gid is None:
            raise ValueError("Missing required parameter 'story_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/stories/{story_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_astory(self, story_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific story identified by its story GID from the collection of stories.

        Args:
            story_gid (string): story_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified story.

        Tags:
            Stories
        """
        if story_gid is None:
            raise ValueError("Missing required parameter 'story_gid'")
        url = f"{self.base_url}/stories/{story_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_stories_from_atask(
        self, task_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves the stories associated with a specific task using the task's unique identifier and supports optional query parameters for pagination and field selection.

        Args:
            task_gid (string): task_gid
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'assignee,assignee.name,created_at,created_by,created_by.name,custom_field,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.id_prefix,custom_field.is_formula_field,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.representation_type,custom_field.resource_subtype,custom_field.text_value,custom_field.type,dependency,dependency.created_by,dependency.name,dependency.resource_subtype,duplicate_of,duplicate_of.created_by,duplicate_of.name,duplicate_of.resource_subtype,duplicated_from,duplicated_from.created_by,duplicated_from.name,duplicated_from.resource_subtype,follower,follower.name,hearted,hearts,hearts.user,hearts.user.name,html_text,is_editable,is_edited,is_pinned,liked,likes,likes.user,likes.user.name,new_approval_status,new_date_value,new_dates,new_dates.due_at,new_dates.due_on,new_dates.start_on,new_enum_value,new_enum_value.color,new_enum_value.enabled,new_enum_value.name,new_multi_enum_values,new_multi_enum_values.color,new_multi_enum_values.enabled,new_multi_enum_values.name,new_name,new_number_value,new_people_value,new_people_value.name,new_resource_subtype,new_section,new_section.name,new_text_value,num_hearts,num_likes,offset,old_approval_status,old_date_value,old_dates,old_dates.due_at,old_dates.due_on,old_dates.start_on,old_enum_value,old_enum_value.color,old_enum_value.enabled,old_enum_value.name,old_multi_enum_values,old_multi_enum_values.color,old_multi_enum_values.enabled,old_multi_enum_values.name,old_name,old_number_value,old_people_value,old_people_value.name,old_resource_subtype,old_section,old_section.name,old_text_value,path,previews,previews.fallback,previews.footer,previews.header,previews.header_link,previews.html_text,previews.text,previews.title,previews.title_link,project,project.name,resource_subtype,source,sticker_name,story,story.created_at,story.created_by,story.created_by.name,story.resource_subtype,story.text,tag,tag.name,target,target.created_by,target.name,target.resource_subtype,task,task.created_by,task.name,task.resource_subtype,text,type,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified task's stories.

        Tags:
            Stories
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/stories"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_astory_on_atask(
        self, task_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a story for a specific task using the "POST" method at the "/tasks/{task_gid}/stories" endpoint, allowing for optional fields and formatting through query parameters.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'assignee,assignee.name,created_at,created_by,created_by.name,custom_field,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.id_prefix,custom_field.is_formula_field,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.representation_type,custom_field.resource_subtype,custom_field.text_value,custom_field.type,dependency,dependency.created_by,dependency.name,dependency.resource_subtype,duplicate_of,duplicate_of.created_by,duplicate_of.name,duplicate_of.resource_subtype,duplicated_from,duplicated_from.created_by,duplicated_from.name,duplicated_from.resource_subtype,follower,follower.name,hearted,hearts,hearts.user,hearts.user.name,html_text,is_editable,is_edited,is_pinned,liked,likes,likes.user,likes.user.name,new_approval_status,new_date_value,new_dates,new_dates.due_at,new_dates.due_on,new_dates.start_on,new_enum_value,new_enum_value.color,new_enum_value.enabled,new_enum_value.name,new_multi_enum_values,new_multi_enum_values.color,new_multi_enum_values.enabled,new_multi_enum_values.name,new_name,new_number_value,new_people_value,new_people_value.name,new_resource_subtype,new_section,new_section.name,new_text_value,num_hearts,num_likes,old_approval_status,old_date_value,old_dates,old_dates.due_at,old_dates.due_on,old_dates.start_on,old_enum_value,old_enum_value.color,old_enum_value.enabled,old_enum_value.name,old_multi_enum_values,old_multi_enum_values.color,old_multi_enum_values.enabled,old_multi_enum_values.name,old_name,old_number_value,old_people_value,old_people_value.name,old_resource_subtype,old_section,old_section.name,old_text_value,previews,previews.fallback,previews.footer,previews.header,previews.header_link,previews.html_text,previews.text,previews.title,previews.title_link,project,project.name,resource_subtype,source,sticker_name,story,story.created_at,story.created_by,story.created_by.name,story.resource_subtype,story.text,tag,tag.name,target,target.created_by,target.name,target.resource_subtype,task,task.created_by,task.name,task.resource_subtype,text,type'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "gid": "12345",
                    "html_text": "<body>This is a comment.</body>",
                    "is_pinned": false,
                    "resource_subtype": "comment_added",
                    "resource_type": "task",
                    "sticker_name": "dancing_unicorn",
                    "text": "This is a comment."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new story.

        Tags:
            Stories
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/stories"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_tags(
        self, limit=None, offset=None, workspace=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of tags using the "GET" method at the "/tags" endpoint, allowing customization with parameters for limit, offset, workspace, optional fields, and pretty formatting.

        Args:
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            workspace (string): The workspace to filter tags on. Example: '1331'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,followers,followers.name,name,notes,offset,path,permalink_url,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified set of tags.

        Tags:
            Tags
        """
        url = f"{self.base_url}/tags"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("workspace", workspace),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atag(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new tag entry with optional fields and formatted response.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,followers,followers.name,name,notes,permalink_url,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "color": "light-green",
                    "followers": [
                      "12345",
                      "42563"
                    ],
                    "gid": "12345",
                    "name": "Stuff to buy",
                    "notes": "Mittens really likes the stuff from Humboldt.",
                    "resource_type": "task",
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the newly specified tag.

        Tags:
            Tags
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tags"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atag(self, tag_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves information about a specific tag, identified by its GID, using the "GET" method at the path "/tags/{tag_gid}" with optional formatting and field selection.

        Args:
            tag_gid (string): tag_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,followers,followers.name,name,notes,permalink_url,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified tag.

        Tags:
            Tags
        """
        if tag_gid is None:
            raise ValueError("Missing required parameter 'tag_gid'")
        url = f"{self.base_url}/tags/{tag_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atag(self, tag_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Updates or replaces a Git tag with the specified GID and returns the operation status.

        Args:
            tag_gid (string): tag_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,followers,followers.name,name,notes,permalink_url,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully updated the specified tag.

        Tags:
            Tags
        """
        if tag_gid is None:
            raise ValueError("Missing required parameter 'tag_gid'")
        url = f"{self.base_url}/tags/{tag_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atag(self, tag_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific tag from a repository using the API and returns relevant status messages, depending on the outcome of the deletion operation.

        Args:
            tag_gid (string): tag_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified tag.

        Tags:
            Tags
        """
        if tag_gid is None:
            raise ValueError("Missing required parameter 'tag_gid'")
        url = f"{self.base_url}/tags/{tag_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_stags(
        self, task_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves the tags associated with a specific task using the task's unique identifier and supports optional filtering/pagination through query parameters.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,followers,followers.name,name,notes,offset,path,permalink_url,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the tags for the given task.

        Tags:
            Tags
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/tags"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_in_aworkspace(
        self, workspace_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of tags associated with a specific workspace, with options to limit the response size and customize the output fields.

        Args:
            workspace_gid (string): workspace_gid
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,followers,followers.name,name,notes,offset,path,permalink_url,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified set of tags.

        Tags:
            Tags
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/tags"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atag_in_aworkspace(
        self, workspace_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds tags to a specified workspace using a POST request to the "/workspaces/{workspace_gid}/tags" endpoint.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'color,created_at,followers,followers.name,name,notes,permalink_url,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "color": "light-green",
                    "followers": [
                      "12345",
                      "42563"
                    ],
                    "gid": "12345",
                    "name": "Stuff to buy",
                    "notes": "Mittens really likes the stuff from Humboldt.",
                    "resource_type": "task"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the newly specified tag.

        Tags:
            Tags
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}/tags"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_tasks(
        self,
        limit=None,
        offset=None,
        assignee=None,
        project=None,
        section=None,
        workspace=None,
        completed_since=None,
        modified_since=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of tasks based on specified query parameters such as assignee, project, and completion status, using the GET method at the "/tasks" endpoint.

        Args:
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            assignee (string): The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified.
        *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.* Example: '14641'.
            project (string): The project to filter tasks on. Example: '321654'.
            section (string): The section to filter tasks on. Example: '321654'.
            workspace (string): The workspace to filter tasks on.
        *Note: If you specify `workspace`, you must also specify the `assignee` to filter on.* Example: '321654'.
            completed_since (string): Only return tasks that are either incomplete or that have been completed since this time. Example: '2012-02-22T02:06:58.158Z'.
            modified_since (string): Only return tasks that have been modified since the given time. *Note: A task is considered “modified” if any of its properties
        change, or associations between it and other objects are modified
        (e.g. a task being added to a project). A task is not considered
        modified just because another object it is associated with (e.g. a
        subtask) is modified. Actions that count as modifying the task
        include assigning, renaming, completing, and adding stories.* Example: '2012-02-22T02:06:58.158Z'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved requested tasks.

        Tags:
            Tasks
        """
        url = f"{self.base_url}/tasks"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("assignee", assignee),
                ("project", project),
                ("section", section),
                ("workspace", workspace),
                ("completed_since", completed_since),
                ("modified_since", modified_since),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atask(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new task using the API and returns a status message, allowing optional fields and pretty-printing configurations through query parameters.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "actual_time_minutes": 200,
                    "approval_status": "pending",
                    "assignee": "12345",
                    "assignee_section": "12345",
                    "assignee_status": "upcoming",
                    "completed": false,
                    "completed_at": "2012-02-22T02:06:58.147Z",
                    "completed_by": {
                      "gid": "12345",
                      "name": "Greg Sanchez",
                      "resource_type": "task"
                    },
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "created_by": {
                      "gid": "1111",
                      "resource_type": "user"
                    },
                    "custom_fields": {
                      "4578152156": "Not Started",
                      "5678904321": "On Hold"
                    },
                    "dependencies": [
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      }
                    ],
                    "dependents": [
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      }
                    ],
                    "due_at": "2019-09-15T02:06:58.147Z",
                    "due_on": "2019-09-15",
                    "external": {
                      "data": "A blob of information",
                      "gid": "my_gid"
                    },
                    "followers": [
                      "12345"
                    ],
                    "gid": "12345",
                    "hearted": true,
                    "hearts": [
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      },
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "html_notes": "<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>",
                    "is_rendered_as_separator": false,
                    "liked": true,
                    "likes": [
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      },
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "memberships": [
                      {
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "section": {
                          "gid": "12345",
                          "name": "Next Actions",
                          "resource_type": "task"
                        }
                      },
                      {
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "section": {
                          "gid": "12345",
                          "name": "Next Actions",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "modified_at": "2012-02-22T02:06:58.147Z",
                    "name": "Bug Task",
                    "notes": "Mittens really likes the stuff from Humboldt.",
                    "num_hearts": 5,
                    "num_likes": 5,
                    "num_subtasks": 3,
                    "parent": "12345",
                    "projects": [
                      "12345"
                    ],
                    "resource_subtype": "default_task",
                    "resource_type": "task",
                    "start_at": "2019-09-14T02:06:58.147Z",
                    "start_on": "2019-09-14",
                    "tags": [
                      "12345"
                    ],
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new task.

        Tags:
            Tasks
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask(self, task_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves task details using the Asana API and returns information about the specified task, with optional fields and formatting available through query parameters.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atask(
        self, task_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates an existing task specified by its ID using the PUT method, allowing for a complete replacement of the task resource.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "actual_time_minutes": 200,
                    "approval_status": "pending",
                    "assignee": "12345",
                    "assignee_section": "12345",
                    "assignee_status": "upcoming",
                    "completed": false,
                    "completed_at": "2012-02-22T02:06:58.147Z",
                    "completed_by": {
                      "gid": "12345",
                      "name": "Greg Sanchez",
                      "resource_type": "task"
                    },
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "created_by": {
                      "gid": "1111",
                      "resource_type": "user"
                    },
                    "custom_fields": {
                      "4578152156": "Not Started",
                      "5678904321": "On Hold"
                    },
                    "dependencies": [
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      }
                    ],
                    "dependents": [
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      }
                    ],
                    "due_at": "2019-09-15T02:06:58.147Z",
                    "due_on": "2019-09-15",
                    "external": {
                      "data": "A blob of information",
                      "gid": "my_gid"
                    },
                    "followers": [
                      "12345"
                    ],
                    "gid": "12345",
                    "hearted": true,
                    "hearts": [
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      },
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "html_notes": "<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>",
                    "is_rendered_as_separator": false,
                    "liked": true,
                    "likes": [
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      },
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "memberships": [
                      {
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "section": {
                          "gid": "12345",
                          "name": "Next Actions",
                          "resource_type": "task"
                        }
                      },
                      {
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "section": {
                          "gid": "12345",
                          "name": "Next Actions",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "modified_at": "2012-02-22T02:06:58.147Z",
                    "name": "Bug Task",
                    "notes": "Mittens really likes the stuff from Humboldt.",
                    "num_hearts": 5,
                    "num_likes": 5,
                    "num_subtasks": 3,
                    "parent": "12345",
                    "projects": [
                      "12345"
                    ],
                    "resource_subtype": "default_task",
                    "resource_type": "task",
                    "start_at": "2019-09-14T02:06:58.147Z",
                    "start_on": "2019-09-14",
                    "tags": [
                      "12345"
                    ],
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the specified task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atask(self, task_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes the specified task identified by the task_gid and returns an appropriate HTTP status code.

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_atask(
        self, task_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Duplicates a task using the Asana API and returns a job ID, requiring a subsequent update call to modify the new task's properties.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,new_task_template,new_task_template.name,resource_subtype,status'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "include": "n,n,n",
                    "name": "New Task Name"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the job to handle duplication.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/duplicate"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_aproject(
        self,
        project_gid,
        opt_fields=None,
        completed_since=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of tasks associated with a specific project, supporting optional filtering and pagination parameters.

        Args:
            project_gid (string): project_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name'.
            completed_since (string): Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. Example: '2012-02-22T02:06:58.158Z'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested project's tasks.

        Tags:
            Tasks
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/tasks"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("completed_since", completed_since),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_asection(
        self,
        section_gid,
        opt_fields=None,
        opt_pretty=None,
        limit=None,
        offset=None,
        completed_since=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of tasks within a specified section using the Asana API and returns the data based on optional query parameters such as fields, formatting, limit, offset, and completion status.

        Args:
            section_gid (string): section_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            completed_since (string): Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. Example: '2012-02-22T02:06:58.158Z'.

        Returns:
            dict[str, Any]: Successfully retrieved the section's tasks.

        Tags:
            Tasks
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        url = f"{self.base_url}/sections/{section_gid}/tasks"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
                ("completed_since", completed_since),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_atag(
        self, tag_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of tasks associated with a specific tag, allowing for optional filtering by fields, formatting, and pagination using query parameters.

        Args:
            tag_gid (string): tag_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the tasks associated with the specified tag.

        Tags:
            Tasks
        """
        if tag_gid is None:
            raise ValueError("Missing required parameter 'tag_gid'")
        url = f"{self.base_url}/tags/{tag_gid}/tasks"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_auser_task_list(
        self,
        user_task_list_gid,
        opt_fields=None,
        completed_since=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of tasks associated with a specific user task list, allowing optional filtering by completion status, custom fields, and pagination limits.

        Args:
            user_task_list_gid (string): user_task_list_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name'.
            completed_since (string): Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. Example: '2012-02-22T02:06:58.158Z'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the user task list's tasks.

        Tags:
            Tasks
        """
        if user_task_list_gid is None:
            raise ValueError("Missing required parameter 'user_task_list_gid'")
        url = f"{self.base_url}/user_task_lists/{user_task_list_gid}/tasks"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("completed_since", completed_since),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_subtasks_from_atask(
        self, task_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of subtasks for a specified task using the GET method, allowing optional parameters for customizing the response.

        Args:
            task_gid (string): task_gid
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified task's subtasks.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/subtasks"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_asubtask(
        self, task_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new subtask for the specified parent task and returns the created subtask details.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "actual_time_minutes": 200,
                    "approval_status": "pending",
                    "assignee": "12345",
                    "assignee_section": "12345",
                    "assignee_status": "upcoming",
                    "completed": false,
                    "completed_at": "2012-02-22T02:06:58.147Z",
                    "completed_by": {
                      "gid": "12345",
                      "name": "Greg Sanchez",
                      "resource_type": "task"
                    },
                    "created_at": "2012-02-22T02:06:58.147Z",
                    "created_by": {
                      "gid": "1111",
                      "resource_type": "user"
                    },
                    "custom_fields": {
                      "4578152156": "Not Started",
                      "5678904321": "On Hold"
                    },
                    "dependencies": [
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      }
                    ],
                    "dependents": [
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      },
                      {
                        "gid": "12345",
                        "resource_type": "task"
                      }
                    ],
                    "due_at": "2019-09-15T02:06:58.147Z",
                    "due_on": "2019-09-15",
                    "external": {
                      "data": "A blob of information",
                      "gid": "my_gid"
                    },
                    "followers": [
                      "12345"
                    ],
                    "gid": "12345",
                    "hearted": true,
                    "hearts": [
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      },
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "html_notes": "<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>",
                    "is_rendered_as_separator": false,
                    "liked": true,
                    "likes": [
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      },
                      {
                        "gid": "12345",
                        "user": {
                          "gid": "12345",
                          "name": "Greg Sanchez",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "memberships": [
                      {
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "section": {
                          "gid": "12345",
                          "name": "Next Actions",
                          "resource_type": "task"
                        }
                      },
                      {
                        "project": {
                          "gid": "12345",
                          "name": "Stuff to buy",
                          "resource_type": "task"
                        },
                        "section": {
                          "gid": "12345",
                          "name": "Next Actions",
                          "resource_type": "task"
                        }
                      }
                    ],
                    "modified_at": "2012-02-22T02:06:58.147Z",
                    "name": "Bug Task",
                    "notes": "Mittens really likes the stuff from Humboldt.",
                    "num_hearts": 5,
                    "num_likes": 5,
                    "num_subtasks": 3,
                    "parent": "12345",
                    "projects": [
                      "12345"
                    ],
                    "resource_subtype": "default_task",
                    "resource_type": "task",
                    "start_at": "2019-09-14T02:06:58.147Z",
                    "start_on": "2019-09-14",
                    "tags": [
                      "12345"
                    ],
                    "workspace": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the specified subtask.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/subtasks"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_the_parent_of_atask(
        self, task_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Changes the parent task of a specified task by submitting a POST request to the "/tasks/{task_gid}/setParent" endpoint.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "insert_after": "null",
                    "insert_before": "124816",
                    "parent": "987654"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully changed the parent of the specified subtask.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/setParent"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_dependencies_from_atask(
        self, task_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of dependencies for a task with the specified task GID, allowing customization with optional fields, pretty formatting, and pagination limits.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified task's dependencies.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/dependencies"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_dependencies_for_atask(
        self, task_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds dependencies to a task using the task's GID and returns a status message, with optional pretty formatting.

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "dependencies": [
                      "133713",
                      "184253"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully set the specified dependencies on the task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addDependencies"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unlink_dependencies_from_atask(
        self, task_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes dependencies from a task using the "POST" method at the "/tasks/{task_gid}/removeDependencies" path.

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "dependencies": [
                      "133713",
                      "184253"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully unlinked the dependencies from the specified task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeDependencies"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_dependents_from_atask(
        self, task_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of dependent tasks for a specified task using the GET method at "/tasks/{task_gid}/dependents," allowing for optional filtering with parameters such as `opt_fields`, `opt_pretty`, `limit`, and `offset`.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the specified dependents of the task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/dependents"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_dependents_for_atask(
        self, task_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds dependent tasks to a specified task using the POST method.

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "dependents": [
                      "133713",
                      "184253"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully set the specified dependents on the given task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addDependents"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unlink_dependents_from_atask(
        self, task_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes dependent tasks from the specified task using the POST method.

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "dependents": [
                      "133713",
                      "184253"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully unlinked the specified tasks as dependents.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeDependents"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_aproject_to_atask(
        self, task_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds a project to a specific task using the "POST" method at the path "/tasks/{task_gid}/addProject".

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "insert_after": "124816",
                    "insert_before": "432134",
                    "project": "13579",
                    "section": "987654"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added the specified project to the task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addProject"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_aproject_from_atask(
        self, task_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes the specified project from a task while retaining the task in the system.

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "project": "13579"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the specified project from the task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeProject"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_atag_to_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds a tag to a specified task in the system using the provided task identifier and returns a status message.

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "tag": "13579"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added the specified tag to the task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addTag"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_atag_from_atask(
        self, task_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes a tag from a task with the specified identifier using the "POST" method and returns a status message.

        Args:
            task_gid (string): task_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "tag": "13579"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the specified tag from the task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeTag"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_followers_to_atask(
        self, task_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds followers to a specific task identified by its GID using the POST method, allowing optional fields and formatting for the response.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "followers": [
                      "13579",
                      "321654"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added the specified followers to the task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addFollowers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_followers_from_atask(
        self, task_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes specified followers from a task using the POST method, returning the updated task record.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "followers": [
                      "13579",
                      "321654"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully removed the specified followers from the task.

        Tags:
            Tasks
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeFollowers"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_for_agiven_custom_id(
        self, workspace_gid, custom_id
    ) -> dict[str, Any]:
        """
        Retrieves a task by its custom ID from a specified workspace using the Asana API.

        Args:
            workspace_gid (string): workspace_gid
            custom_id (string): custom_id

        Returns:
            dict[str, Any]: Successfully retrieved task for given custom ID.

        Tags:
            Tasks
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        if custom_id is None:
            raise ValueError("Missing required parameter 'custom_id'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/tasks/custom_id/{custom_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_tasks_in_aworkspace(
        self,
        workspace_gid,
        opt_fields=None,
        opt_pretty=None,
        text=None,
        resource_subtype=None,
        assignee_any=None,
        assignee_not=None,
        portfolios_any=None,
        projects_any=None,
        projects_not=None,
        projects_all=None,
        sections_any=None,
        sections_not=None,
        sections_all=None,
        tags_any=None,
        tags_not=None,
        tags_all=None,
        teams_any=None,
        followers_not=None,
        created_by_any=None,
        created_by_not=None,
        assigned_by_any=None,
        assigned_by_not=None,
        liked_by_not=None,
        commented_on_by_not=None,
        due_on_before=None,
        due_on_after=None,
        due_on=None,
        due_at_before=None,
        due_at_after=None,
        start_on_before=None,
        start_on_after=None,
        start_on=None,
        created_on_before=None,
        created_on_after=None,
        created_on=None,
        created_at_before=None,
        created_at_after=None,
        completed_on_before=None,
        completed_on_after=None,
        completed_on=None,
        completed_at_before=None,
        completed_at_after=None,
        modified_on_before=None,
        modified_on_after=None,
        modified_on=None,
        modified_at_before=None,
        modified_at_after=None,
        is_blocking=None,
        is_blocked=None,
        has_attachment=None,
        completed=None,
        is_subtask=None,
        sort_by=None,
        sort_ascending=None,
    ) -> dict[str, Any]:
        """
        Searches for tasks within a specified workspace using various filters, such as text, assignees, projects, tags, and due dates, and returns a list of tasks matching these criteria.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.id_prefix,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            text (string): Performs full-text search on both task name and description Example: 'Bug'.
            resource_subtype (string): Filters results by the task's resource_subtype Example: 'milestone'.
            assignee_any (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            assignee_not (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            portfolios_any (string): Comma-separated list of portfolio IDs Example: '12345,23456,34567'.
            projects_any (string): Comma-separated list of project IDs Example: '12345,23456,34567'.
            projects_not (string): Comma-separated list of project IDs Example: '12345,23456,34567'.
            projects_all (string): Comma-separated list of project IDs Example: '12345,23456,34567'.
            sections_any (string): Comma-separated list of section or column IDs Example: '12345,23456,34567'.
            sections_not (string): Comma-separated list of section or column IDs Example: '12345,23456,34567'.
            sections_all (string): Comma-separated list of section or column IDs Example: '12345,23456,34567'.
            tags_any (string): Comma-separated list of tag IDs Example: '12345,23456,34567'.
            tags_not (string): Comma-separated list of tag IDs Example: '12345,23456,34567'.
            tags_all (string): Comma-separated list of tag IDs Example: '12345,23456,34567'.
            teams_any (string): Comma-separated list of team IDs Example: '12345,23456,34567'.
            followers_not (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            created_by_any (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            created_by_not (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            assigned_by_any (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            assigned_by_not (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            liked_by_not (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            commented_on_by_not (string): Comma-separated list of user identifiers Example: '12345,23456,34567'.
            due_on_before (string): ISO 8601 date string Example: '2019-09-15'.
            due_on_after (string): ISO 8601 date string Example: '2019-09-15'.
            due_on (string): ISO 8601 date string or `null` Example: '2019-09-15'.
            due_at_before (string): ISO 8601 datetime string Example: '2019-04-15T01:01:46.055Z'.
            due_at_after (string): ISO 8601 datetime string Example: '2019-04-15T01:01:46.055Z'.
            start_on_before (string): ISO 8601 date string Example: '2019-09-15'.
            start_on_after (string): ISO 8601 date string Example: '2019-09-15'.
            start_on (string): ISO 8601 date string or `null` Example: '2019-09-15'.
            created_on_before (string): ISO 8601 date string Example: '2019-09-15'.
            created_on_after (string): ISO 8601 date string Example: '2019-09-15'.
            created_on (string): ISO 8601 date string or `null` Example: '2019-09-15'.
            created_at_before (string): ISO 8601 datetime string Example: '2019-04-15T01:01:46.055Z'.
            created_at_after (string): ISO 8601 datetime string Example: '2019-04-15T01:01:46.055Z'.
            completed_on_before (string): ISO 8601 date string Example: '2019-09-15'.
            completed_on_after (string): ISO 8601 date string Example: '2019-09-15'.
            completed_on (string): ISO 8601 date string or `null` Example: '2019-09-15'.
            completed_at_before (string): ISO 8601 datetime string Example: '2019-04-15T01:01:46.055Z'.
            completed_at_after (string): ISO 8601 datetime string Example: '2019-04-15T01:01:46.055Z'.
            modified_on_before (string): ISO 8601 date string Example: '2019-09-15'.
            modified_on_after (string): ISO 8601 date string Example: '2019-09-15'.
            modified_on (string): ISO 8601 date string or `null` Example: '2019-09-15'.
            modified_at_before (string): ISO 8601 datetime string Example: '2019-04-15T01:01:46.055Z'.
            modified_at_after (string): ISO 8601 datetime string Example: '2019-04-15T01:01:46.055Z'.
            is_blocking (string): Filter to incomplete tasks with dependents Example: 'false'.
            is_blocked (string): Filter to tasks with incomplete dependencies Example: 'false'.
            has_attachment (string): Filter to tasks with attachments Example: 'false'.
            completed (string): Filter to completed tasks Example: 'false'.
            is_subtask (string): Filter to subtasks Example: 'false'.
            sort_by (string): One of `due_date`, `created_at`, `completed_at`, `likes`, or `modified_at`, defaults to `modified_at` Example: 'likes'.
            sort_ascending (string): Default `false` Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the section's tasks.

        Tags:
            Tasks
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/tasks/search"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("text", text),
                ("resource_subtype", resource_subtype),
                ("assignee.any", assignee_any),
                ("assignee.not", assignee_not),
                ("portfolios.any", portfolios_any),
                ("projects.any", projects_any),
                ("projects.not", projects_not),
                ("projects.all", projects_all),
                ("sections.any", sections_any),
                ("sections.not", sections_not),
                ("sections.all", sections_all),
                ("tags.any", tags_any),
                ("tags.not", tags_not),
                ("tags.all", tags_all),
                ("teams.any", teams_any),
                ("followers.not", followers_not),
                ("created_by.any", created_by_any),
                ("created_by.not", created_by_not),
                ("assigned_by.any", assigned_by_any),
                ("assigned_by.not", assigned_by_not),
                ("liked_by.not", liked_by_not),
                ("commented_on_by.not", commented_on_by_not),
                ("due_on.before", due_on_before),
                ("due_on.after", due_on_after),
                ("due_on", due_on),
                ("due_at.before", due_at_before),
                ("due_at.after", due_at_after),
                ("start_on.before", start_on_before),
                ("start_on.after", start_on_after),
                ("start_on", start_on),
                ("created_on.before", created_on_before),
                ("created_on.after", created_on_after),
                ("created_on", created_on),
                ("created_at.before", created_at_before),
                ("created_at.after", created_at_after),
                ("completed_on.before", completed_on_before),
                ("completed_on.after", completed_on_after),
                ("completed_on", completed_on),
                ("completed_at.before", completed_at_before),
                ("completed_at.after", completed_at_after),
                ("modified_on.before", modified_on_before),
                ("modified_on.after", modified_on_after),
                ("modified_on", modified_on),
                ("modified_at.before", modified_at_before),
                ("modified_at.after", modified_at_after),
                ("is_blocking", is_blocking),
                ("is_blocked", is_blocked),
                ("has_attachment", has_attachment),
                ("completed", completed),
                ("is_subtask", is_subtask),
                ("sort_by", sort_by),
                ("sort_ascending", sort_ascending),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_task_templates(
        self, limit=None, offset=None, project=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of available task templates for standardized task creation, supporting optional filters like project, pagination (limit/offset), and field customization (opt_fields).

        Args:
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            project (string): The project to filter task templates on. Example: '321654'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,created_by,name,project,template'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved requested task templates

        Tags:
            Task templates
        """
        url = f"{self.base_url}/task_templates"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("project", project),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_template(
        self, task_template_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific task template in Asana using the "GET" method at the "/task_templates/{task_template_gid}" path.

        Args:
            task_template_gid (string): task_template_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,created_by,name,project,template'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved requested task template

        Tags:
            Task templates
        """
        if task_template_gid is None:
            raise ValueError("Missing required parameter 'task_template_gid'")
        url = f"{self.base_url}/task_templates/{task_template_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atask_template(
        self, task_template_gid, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Deletes a specific task template by making a DELETE request to the API endpoint, returning an empty response upon success.

        Args:
            task_template_gid (string): task_template_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified task template.

        Tags:
            Task templates
        """
        if task_template_gid is None:
            raise ValueError("Missing required parameter 'task_template_gid'")
        url = f"{self.base_url}/task_templates/{task_template_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def instantiate_atask_from_atask_template(
        self, task_template_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Instantiates a task from a specified task template using the Asana API, allowing for the creation of standardized and repeatable workflows by leveraging pre-defined templates.

        Args:
            task_template_gid (string): task_template_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,new_task_template,new_task_template.name,resource_subtype,status'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "name": "New Task"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the job to handle task instantiation.

        Tags:
            Task templates
        """
        if task_template_gid is None:
            raise ValueError("Missing required parameter 'task_template_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/task_templates/{task_template_gid}/instantiateTask"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_ateam(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new team resource using the API at the "/teams" path with the "POST" method.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,organization,organization.name,permalink_url,team_content_management_access_level,team_member_removal_access_level,visibility'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "description": "All developers should be members of this team.",
                    "edit_team_name_or_description_access_level": "only_team_admins",
                    "edit_team_visibility_or_trash_team_access_level": "all_team_members",
                    "gid": "12345",
                    "guest_invite_management_access_level": "all_team_members",
                    "html_description": "<body><em>All</em> developers should be members of this team.</body>",
                    "join_request_management_access_level": "all_team_members",
                    "member_invite_management_access_level": "only_team_admins",
                    "name": "Marketing",
                    "organization": "123456789",
                    "resource_type": "task",
                    "team_content_management_access_level": "only_team_admins",
                    "team_member_removal_access_level": "only_team_admins",
                    "visibility": "request_to_join"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a new team.

        Tags:
            Teams
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam(self, team_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves details for a specific GitHub team by its global ID, supporting optional query parameters to customize the response format and included fields.

        Args:
            team_gid (string): team_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,organization,organization.name,permalink_url,team_content_management_access_level,team_member_removal_access_level,visibility'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the record for a single team.

        Tags:
            Teams
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_ateam(
        self, team_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates the details of a team with the specified GID using the provided parameters, returning a status response based on the operation's success or failure.

        Args:
            team_gid (string): team_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,organization,organization.name,permalink_url,team_content_management_access_level,team_member_removal_access_level,visibility'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "description": "All developers should be members of this team.",
                    "edit_team_name_or_description_access_level": "only_team_admins",
                    "edit_team_visibility_or_trash_team_access_level": "all_team_members",
                    "gid": "12345",
                    "guest_invite_management_access_level": "all_team_members",
                    "html_description": "<body><em>All</em> developers should be members of this team.</body>",
                    "join_request_management_access_level": "all_team_members",
                    "member_invite_management_access_level": "only_team_admins",
                    "name": "Marketing",
                    "organization": "123456789",
                    "resource_type": "task",
                    "team_content_management_access_level": "only_team_admins",
                    "team_member_removal_access_level": "only_team_admins",
                    "visibility": "request_to_join"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the team.

        Tags:
            Teams
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams/{team_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_teams_in_aworkspace(
        self, workspace_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of teams in a specified workspace using the GET method, allowing optional query parameters for customizing output fields, formatting, and pagination.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,offset,organization,organization.name,path,permalink_url,team_content_management_access_level,team_member_removal_access_level,uri,visibility'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Returns the team records for all teams in the organization or workspace accessible to the authenticated user.

        Tags:
            Teams
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/teams"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_teams_for_auser(
        self,
        user_gid,
        opt_fields=None,
        opt_pretty=None,
        limit=None,
        offset=None,
        organization=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of teams associated with a specific user, optionally filtered by organization, using query parameters for customization.

        Args:
            user_gid (string): user_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,offset,organization,organization.name,path,permalink_url,team_content_management_access_level,team_member_removal_access_level,uri,visibility'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            organization (string): (Required) The workspace or organization to filter teams on. Example: '1331'.

        Returns:
            dict[str, Any]: Returns the team records for all teams in the organization or workspace to which the given user is assigned.

        Tags:
            Teams
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/teams"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
                ("organization", organization),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_auser_to_ateam(
        self, team_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds a user to a team using the provided team ID, allowing for optional specification of additional fields and formatting preferences.

        Args:
            team_gid (string): team_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'is_admin,is_guest,is_limited_access,team,team.name,user,user.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "user": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully added user to the team.

        Tags:
            Teams
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams/{team_gid}/addUser"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_auser_from_ateam(
        self, team_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes a user from a specified team using a POST request and returns a success status upon completion.

        Args:
            team_gid (string): team_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "user": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Returns an empty data record

        Tags:
            Teams
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams/{team_gid}/removeUser"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_membership(
        self, team_membership_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific team membership using the "GET" method at "/team_memberships/{team_membership_gid}", allowing optional fields and formatting parameters to be specified.

        Args:
            team_membership_gid (string): team_membership_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'is_admin,is_guest,is_limited_access,team,team.name,user,user.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested team membership.

        Tags:
            Team memberships
        """
        if team_membership_gid is None:
            raise ValueError("Missing required parameter 'team_membership_gid'")
        url = f"{self.base_url}/team_memberships/{team_membership_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_memberships(
        self,
        team=None,
        user=None,
        workspace=None,
        opt_fields=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves team membership information for a specified user within a team and workspace, allowing optional fields and pagination.

        Args:
            team (string): Globally unique identifier for the team. Example: '159874'.
            user (string): A string identifying a user. This can either be the string "me", an email, or the gid of a user. This parameter must be used with the workspace parameter. Example: '512241'.
            workspace (string): Globally unique identifier for the workspace. This parameter must be used with the user parameter. Example: '31326'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'is_admin,is_guest,is_limited_access,offset,path,team,team.name,uri,user,user.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested team memberships.

        Tags:
            Team memberships
        """
        url = f"{self.base_url}/team_memberships"
        query_params = {
            k: v
            for k, v in [
                ("team", team),
                ("user", user),
                ("workspace", workspace),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_ateam(
        self, team_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves team memberships for a specified team using the GitHub API, returning details about members based on optional fields and pagination parameters.

        Args:
            team_gid (string): team_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'is_admin,is_guest,is_limited_access,offset,path,team,team.name,uri,user,user.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested team's memberships.

        Tags:
            Team memberships
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}/team_memberships"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_auser(
        self,
        user_gid,
        workspace=None,
        opt_fields=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of team memberships for a specified user, including optional filtering by workspace and customizable response fields.

        Args:
            user_gid (string): user_gid
            workspace (string): (Required) Globally unique identifier for the workspace. Example: '31326'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'is_admin,is_guest,is_limited_access,offset,path,team,team.name,uri,user,user.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested users's memberships.

        Tags:
            Team memberships
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/team_memberships"
        query_params = {
            k: v
            for k, v in [
                ("workspace", workspace),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atime_period(
        self, time_period_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves details about a specific time period, identified by its GID, using the "GET" method at the "/time_periods/{time_period_gid}" path.

        Args:
            time_period_gid (string): time_period_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'display_name,end_on,parent,parent.display_name,parent.end_on,parent.period,parent.start_on,period,start_on'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the record for a single time period.

        Tags:
            Time periods
        """
        if time_period_gid is None:
            raise ValueError("Missing required parameter 'time_period_gid'")
        url = f"{self.base_url}/time_periods/{time_period_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_time_periods(
        self,
        start_on=None,
        end_on=None,
        workspace=None,
        opt_fields=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of time periods filtered by start and end dates, workspace, and other optional parameters.

        Args:
            start_on (string): ISO 8601 date string Example: '2019-09-15'.
            end_on (string): ISO 8601 date string Example: '2019-09-15'.
            workspace (string): (Required) Globally unique identifier for the workspace. Example: '31326'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'display_name,end_on,offset,parent,parent.display_name,parent.end_on,parent.period,parent.start_on,path,period,start_on,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested time periods.

        Tags:
            Time periods
        """
        url = f"{self.base_url}/time_periods"
        query_params = {
            k: v
            for k, v in [
                ("start_on", start_on),
                ("end_on", end_on),
                ("workspace", workspace),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_time_tracking_entries_for_atask(
        self, task_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of time tracking entries for a specific task based on provided query parameters, such as limit, offset, and optional fields, returning the data in a formatted response.

        Args:
            task_gid (string): task_gid
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_by,created_by.name,duration_minutes,entered_on,offset,path,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested time tracking entries.

        Tags:
            Time tracking entries
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/time_tracking_entries"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atime_tracking_entry(
        self, task_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new time tracking entry for a specified task using the POST method, allowing for optional fields and formatting through query parameters.

        Args:
            task_gid (string): task_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,created_by,created_by.name,duration_minutes,entered_on,task,task.created_by,task.name,task.resource_subtype'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "duration_minutes": 12,
                    "entered_on": "2023-03-19"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created a time tracking entry for the task.

        Tags:
            Time tracking entries
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/time_tracking_entries"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atime_tracking_entry(
        self, time_tracking_entry_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific time tracking entry by its global ID, allowing optional field selection for the response.

        Args:
            time_tracking_entry_gid (string): time_tracking_entry_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,created_by,created_by.name,duration_minutes,entered_on,task,task.created_by,task.name,task.resource_subtype'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested time tracking entry.

        Tags:
            Time tracking entries
        """
        if time_tracking_entry_gid is None:
            raise ValueError("Missing required parameter 'time_tracking_entry_gid'")
        url = f"{self.base_url}/time_tracking_entries/{time_tracking_entry_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atime_tracking_entry(
        self, time_tracking_entry_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates an existing time tracking entry by its GID and returns the modified entry.

        Args:
            time_tracking_entry_gid (string): time_tracking_entry_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,created_by,created_by.name,duration_minutes,entered_on,task,task.created_by,task.name,task.resource_subtype'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "duration_minutes": 12,
                    "entered_on": "2023-03-19"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the time tracking entry.

        Tags:
            Time tracking entries
        """
        if time_tracking_entry_gid is None:
            raise ValueError("Missing required parameter 'time_tracking_entry_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/time_tracking_entries/{time_tracking_entry_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atime_tracking_entry(
        self, time_tracking_entry_gid, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Deletes a specific time tracking entry identified by the `time_tracking_entry_gid` using the DELETE method and returns relevant status messages based on the success or failure of the operation.

        Args:
            time_tracking_entry_gid (string): time_tracking_entry_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully deleted the specified time tracking entry.

        Tags:
            Time tracking entries
        """
        if time_tracking_entry_gid is None:
            raise ValueError("Missing required parameter 'time_tracking_entry_gid'")
        url = f"{self.base_url}/time_tracking_entries/{time_tracking_entry_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_objects_via_typeahead(
        self,
        workspace_gid,
        opt_fields=None,
        resource_type=None,
        type=None,
        query=None,
        count=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Queries a workspace for typeahead results using the specified parameters and returns relevant objects or suggestions.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'name'.
            resource_type (string): (Required) The type of values the typeahead should return. You can choose from one of the following: `custom_field`, `goal`, `project`, `project_template`, `portfolio`, `tag`, `task`, `team`, and `user`. Note that unlike in the names of endpoints, the types listed here are in singular form (e.g. `task`). Using multiple types is not yet supported. Example: 'user'.
            type (string): *Deprecated: new integrations should prefer the resource_type field.* Example: 'user'.
            query (string): The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results. Example: 'Greg'.
            count (string): The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned. Example: '20'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved objects via a typeahead search algorithm.

        Tags:
            Typeahead
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/typeahead"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("resource_type", resource_type),
                ("type", type),
                ("query", query),
                ("count", count),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_users(
        self,
        opt_fields=None,
        workspace=None,
        team=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of users with optional filtering parameters and pagination support.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'email,name,offset,path,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60,uri,workspaces,workspaces.name'.
            workspace (string): The workspace or organization ID to filter users on. Example: '1331'.
            team (string): The team ID to filter users on. Example: '15627'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested user records.

        Tags:
            Users
        """
        url = f"{self.base_url}/users"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("workspace", workspace),
                ("team", team),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser(self, user_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves details for a specific user using their unique identifier (user_gid) and offers optional query parameters for customizing the returned data fields (opt_fields) and response formatting (opt_pretty).

        Args:
            user_gid (string): user_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'email,name,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60,workspaces,workspaces.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Returns the user specified.

        Tags:
            Users
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_sfavorites(
        self,
        user_gid,
        opt_fields=None,
        opt_pretty=None,
        limit=None,
        offset=None,
        resource_type=None,
        workspace=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of favorites for a user with the specified `user_gid`, allowing optional filtering by resource type and workspace, and customizable output through additional query parameters.

        Args:
            user_gid (string): user_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'name,offset,path,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            resource_type (string): (Required) The resource type of favorites to be returned. Example: 'project'.
            workspace (string): (Required) The workspace in which to get favorites. Example: '1234'.

        Returns:
            dict[str, Any]: Returns the specified user's favorites.

        Tags:
            Users
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/favorites"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
                ("resource_type", resource_type),
                ("workspace", workspace),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_in_ateam(
        self, team_gid, opt_fields=None, opt_pretty=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of users associated with a specified team, supporting optional fields, pretty formatting, and offset parameters.

        Args:
            team_gid (string): team_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'email,name,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60,workspaces,workspaces.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Returns the user records for all the members of the team, including guests and limited access users

        Tags:
            Users
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}/users"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_in_aworkspace_or_organization(
        self, workspace_gid, opt_fields=None, opt_pretty=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of users associated with the specified workspace, supporting optional fields, pagination, and response formatting.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'email,name,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60,workspaces,workspaces.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Return the users in the specified workspace or org.

        Tags:
            Users
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/users"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_task_list(
        self, user_task_list_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves details of a user task list by its global ID, supporting optional query parameters for field selection and response formatting.

        Args:
            user_task_list_gid (string): user_task_list_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'name,owner,workspace'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the user task list.

        Tags:
            User task lists
        """
        if user_task_list_gid is None:
            raise ValueError("Missing required parameter 'user_task_list_gid'")
        url = f"{self.base_url}/user_task_lists/{user_task_list_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_stask_list(
        self, user_gid, opt_fields=None, opt_pretty=None, workspace=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of tasks for a user identified by the user_gid parameter, allowing optional filtering by additional fields or workspace.

        Args:
            user_gid (string): user_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'name,owner,workspace'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            workspace (string): (Required) The workspace in which to get the user task list. Example: '1234'.

        Returns:
            dict[str, Any]: Successfully retrieved the user's task list.

        Tags:
            User task lists
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/user_task_list"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("workspace", workspace),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_webhooks(
        self,
        limit=None,
        offset=None,
        workspace=None,
        resource=None,
        opt_fields=None,
        opt_pretty=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of webhooks, allowing for optional filtering by workspace, resource, and additional fields, with pagination options via limit and offset parameters.

        Args:
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.
            workspace (string): (Required) The workspace to query for webhooks in. Example: '1331'.
            resource (string): Only return webhooks for the given resource. Example: '51648'.
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'active,created_at,delivery_retry_count,failure_deletion_timestamp,filters,filters.action,filters.fields,filters.resource_subtype,last_failure_at,last_failure_content,last_success_at,next_attempt_after,offset,path,resource,resource.name,target,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested webhooks.

        Tags:
            Webhooks
        """
        url = f"{self.base_url}/webhooks"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("offset", offset),
                ("workspace", workspace),
                ("resource", resource),
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def establish_awebhook(
        self, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new webhook subscription to receive event notifications and returns the subscription details.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'active,created_at,delivery_retry_count,failure_deletion_timestamp,filters,filters.action,filters.fields,filters.resource_subtype,last_failure_at,last_failure_content,last_success_at,next_attempt_after,resource,resource.name,target'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "filters": [
                      {
                        "action": "changed",
                        "fields": [
                          "due_at",
                          "due_on",
                          "dependencies"
                        ],
                        "resource_subtype": "milestone",
                        "resource_type": "task"
                      },
                      {
                        "action": "changed",
                        "fields": [
                          "due_at",
                          "due_on",
                          "dependencies"
                        ],
                        "resource_subtype": "milestone",
                        "resource_type": "task"
                      }
                    ],
                    "resource": "12345",
                    "target": "https://example.com/receive-webhook/7654?app_specific_param=app_specific_value"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully created the requested webhook.

        Tags:
            Webhooks
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/webhooks"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_awebhook(
        self, webhook_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves information about a webhook with the specified ID using the "GET" method, allowing optional fields and pretty-print formatting.

        Args:
            webhook_gid (string): webhook_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'active,created_at,delivery_retry_count,failure_deletion_timestamp,filters,filters.action,filters.fields,filters.resource_subtype,last_failure_at,last_failure_content,last_success_at,next_attempt_after,resource,resource.name,target'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested webhook.

        Tags:
            Webhooks
        """
        if webhook_gid is None:
            raise ValueError("Missing required parameter 'webhook_gid'")
        url = f"{self.base_url}/webhooks/{webhook_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_awebhook(
        self, webhook_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates a webhook identified by its GID at the "/webhooks/{webhook_gid}" path, allowing modifications to existing webhook configurations.

        Args:
            webhook_gid (string): webhook_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'active,created_at,delivery_retry_count,failure_deletion_timestamp,filters,filters.action,filters.fields,filters.resource_subtype,last_failure_at,last_failure_content,last_success_at,next_attempt_after,resource,resource.name,target'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "filters": [
                      {
                        "action": "changed",
                        "fields": [
                          "due_at",
                          "due_on",
                          "dependencies"
                        ],
                        "resource_subtype": "milestone",
                        "resource_type": "task"
                      },
                      {
                        "action": "changed",
                        "fields": [
                          "due_at",
                          "due_on",
                          "dependencies"
                        ],
                        "resource_subtype": "milestone",
                        "resource_type": "task"
                      }
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Successfully updated the webhook.

        Tags:
            Webhooks
        """
        if webhook_gid is None:
            raise ValueError("Missing required parameter 'webhook_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/webhooks/{webhook_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_awebhook(self, webhook_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a webhook identified by the `{webhook_gid}` and returns a status message, allowing for the removal of existing webhook configurations.

        Args:
            webhook_gid (string): webhook_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested webhook.

        Tags:
            Webhooks
        """
        if webhook_gid is None:
            raise ValueError("Missing required parameter 'webhook_gid'")
        url = f"{self.base_url}/webhooks/{webhook_gid}"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_workspaces(
        self, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of workspaces with optional filtering and formatting parameters.

        Args:
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'email_domains,is_organization,name,offset,path,uri'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Return all workspaces visible to the authorized user.

        Tags:
            Workspaces
        """
        url = f"{self.base_url}/workspaces"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace(
        self, workspace_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific workspace by its GID using the Asana API, optionally including additional fields and formatting options.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'email_domains,is_organization,name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Return the full workspace record.

        Tags:
            Workspaces
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aworkspace(
        self, workspace_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Updates a specified workspace's properties and returns the modified workspace data.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'email_domains,is_organization,name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "gid": "12345",
                    "name": "My Company Workspace",
                    "resource_type": "task"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update for the workspace was successful.

        Tags:
            Workspaces
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_auser_to_aworkspace_or_organization(
        self, workspace_gid, opt_fields=None, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Adds a user to a specified workspace and returns the full user record upon successful completion.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'email,name,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "user": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: The user was added successfully to the workspace or organization.

        Tags:
            Workspaces
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}/addUser"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_auser_from_aworkspace_or_organization(
        self, workspace_gid, opt_pretty=None, data=None
    ) -> dict[str, Any]:
        """
        Removes a user from a workspace using the specified POST API operation at the "/workspaces/{workspace_gid}/removeUser" path.

        Args:
            workspace_gid (string): workspace_gid
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "user": "12345"
                  }
                }
                ```

        Returns:
            dict[str, Any]: The user was removed successfully to the workspace or organization.

        Tags:
            Workspaces
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}/removeUser"
        query_params = {k: v for k, v in [("opt_pretty", opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace_membership(
        self, workspace_membership_gid, opt_fields=None, opt_pretty=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific workspace membership entry by its global identifier (GID) with optional field filtering and formatted output.

        Args:
            workspace_membership_gid (string): workspace_membership_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,is_active,is_admin,is_guest,user,user.name,user_task_list,user_task_list.name,user_task_list.owner,user_task_list.workspace,vacation_dates,vacation_dates.end_on,vacation_dates.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested workspace membership.

        Tags:
            Workspace memberships
        """
        if workspace_membership_gid is None:
            raise ValueError("Missing required parameter 'workspace_membership_gid'")
        url = f"{self.base_url}/workspace_memberships/{workspace_membership_gid}"
        query_params = {
            k: v
            for k, v in [("opt_fields", opt_fields), ("opt_pretty", opt_pretty)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_workspace_memberships_for_auser(
        self, user_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of workspace memberships for a specified user based on the provided query parameters, including optional fields, formatting preferences, and pagination settings.

        Args:
            user_gid (string): user_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,is_active,is_admin,is_guest,offset,path,uri,user,user.name,user_task_list,user_task_list.name,user_task_list.owner,user_task_list.workspace,vacation_dates,vacation_dates.end_on,vacation_dates.start_on,workspace,workspace.name'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested user's workspace memberships.

        Tags:
            Workspace memberships
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/workspace_memberships"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_the_workspace_memberships_for_aworkspace(
        self,
        workspace_gid,
        opt_fields=None,
        user=None,
        opt_pretty=None,
        limit=None,
        offset=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of workspace memberships for a specified workspace, providing details about users and their roles within the workspace, allowing for optional filtering and customization of the response.

        Args:
            workspace_gid (string): workspace_gid
            opt_fields (string): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Example: 'created_at,is_active,is_admin,is_guest,offset,path,uri,user,user.name,user_task_list,user_task_list.name,user_task_list.owner,user_task_list.workspace,vacation_dates,vacation_dates.end_on,vacation_dates.start_on,workspace,workspace.name'.
            user (string): A string identifying a user. This can either be the string "me", an email, or the gid of a user. Example: 'me'.
            opt_pretty (string): Provides “pretty” output.
        Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. Example: 'true'.
            limit (string): Results per page.
        The number of objects to return per page. The value must be between 1 and 100. Example: '50'.
            offset (string): Offset token.
        An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
        *Note: You can only pass in an offset that was returned to you via a previously paginated request.* Example: 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'.

        Returns:
            dict[str, Any]: Successfully retrieved the requested workspace's memberships.

        Tags:
            Workspace memberships
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/workspace_memberships"
        query_params = {
            k: v
            for k, v in [
                ("opt_fields", opt_fields),
                ("user", user),
                ("opt_pretty", opt_pretty),
                ("limit", limit),
                ("offset", offset),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_an_allocation,
            self.update_an_allocation,
            self.delete_an_allocation,
            self.get_multiple_allocations,
            self.create_an_allocation,
            self.get_an_attachment,
            self.delete_an_attachment,
            self.get_attachments_from_an_object,
            self.get_audit_log_events,
            self.submit_parallel_requests,
            self.create_acustom_field,
            self.get_acustom_field,
            self.update_acustom_field,
            self.delete_acustom_field,
            self.get_aworkspace_scustom_fields,
            self.create_an_enum_option,
            self.reorder_acustom_field_senum,
            self.update_an_enum_option,
            self.get_aproject_scustom_fields,
            self.get_aportfolio_scustom_fields,
            self.get_events_on_aresource,
            self.get_agoal,
            self.update_agoal,
            self.delete_agoal,
            self.get_goals,
            self.create_agoal,
            self.create_agoal_metric,
            self.update_agoal_metric,
            self.add_acollaborator_to_agoal,
            self.remove_acollaborator_from_agoal,
            self.get_parent_goals_from_agoal,
            self.get_agoal_relationship,
            self.update_agoal_relationship,
            self.get_goal_relationships,
            self.add_asupporting_goal_relationship,
            self.removes_asupporting_goal_relationship,
            self.get_ajob_by_id,
            self.get_multiple_memberships,
            self.create_amembership,
            self.get_amembership,
            self.update_amembership,
            self.delete_amembership,
            self.create_an_organization_export_request,
            self.get_details_on_an_org_export_request,
            self.get_multiple_portfolios,
            self.create_aportfolio,
            self.get_aportfolio,
            self.update_aportfolio,
            self.delete_aportfolio,
            self.get_portfolio_items,
            self.add_aportfolio_item,
            self.remove_aportfolio_item,
            self.add_acustom_field_to_aportfolio,
            self.remove_acustom_field_from_aportfolio,
            self.add_users_to_aportfolio,
            self.remove_users_from_aportfolio,
            self.get_multiple_portfolio_memberships,
            self.get_aportfolio_membership,
            self.get_memberships_from_aportfolio,
            self.get_multiple_projects,
            self.create_aproject,
            self.get_aproject,
            self.update_aproject,
            self.delete_aproject,
            self.duplicate_aproject,
            self.get_projects_atask_is_in,
            self.get_ateam_sprojects,
            self.create_aproject_in_ateam,
            self.get_all_projects_in_aworkspace,
            self.create_aproject_in_aworkspace,
            self.add_acustom_field_to_aproject,
            self.remove_acustom_field_from_aproject,
            self.get_task_count_of_aproject,
            self.add_users_to_aproject,
            self.remove_users_from_aproject,
            self.add_followers_to_aproject,
            self.remove_followers_from_aproject,
            self.create_aproject_template_from_aproject,
            self.get_aproject_brief,
            self.update_aproject_brief,
            self.delete_aproject_brief,
            self.create_aproject_brief,
            self.get_aproject_membership,
            self.get_memberships_from_aproject,
            self.get_aproject_status,
            self.delete_aproject_status,
            self.get_statuses_from_aproject,
            self.create_aproject_status,
            self.get_aproject_template,
            self.delete_aproject_template,
            self.get_multiple_project_templates,
            self.get_ateam_sproject_templates,
            self.instantiate_aproject_from_aproject_template,
            self.trigger_arule,
            self.get_asection,
            self.update_asection,
            self.delete_asection,
            self.get_sections_in_aproject,
            self.create_asection_in_aproject,
            self.add_task_to_section,
            self.move_or_insert_sections,
            self.get_astatus_update,
            self.delete_astatus_update,
            self.get_status_updates_from_an_object,
            self.create_astatus_update,
            self.get_astory,
            self.update_astory,
            self.delete_astory,
            self.get_stories_from_atask,
            self.create_astory_on_atask,
            self.get_multiple_tags,
            self.create_atag,
            self.get_atag,
            self.update_atag,
            self.delete_atag,
            self.get_atask_stags,
            self.get_tags_in_aworkspace,
            self.create_atag_in_aworkspace,
            self.get_multiple_tasks,
            self.create_atask,
            self.get_atask,
            self.update_atask,
            self.delete_atask,
            self.duplicate_atask,
            self.get_tasks_from_aproject,
            self.get_tasks_from_asection,
            self.get_tasks_from_atag,
            self.get_tasks_from_auser_task_list,
            self.get_subtasks_from_atask,
            self.create_asubtask,
            self.set_the_parent_of_atask,
            self.get_dependencies_from_atask,
            self.set_dependencies_for_atask,
            self.unlink_dependencies_from_atask,
            self.get_dependents_from_atask,
            self.set_dependents_for_atask,
            self.unlink_dependents_from_atask,
            self.add_aproject_to_atask,
            self.remove_aproject_from_atask,
            self.add_atag_to_atask,
            self.remove_atag_from_atask,
            self.add_followers_to_atask,
            self.remove_followers_from_atask,
            self.get_atask_for_agiven_custom_id,
            self.search_tasks_in_aworkspace,
            self.get_multiple_task_templates,
            self.get_atask_template,
            self.delete_atask_template,
            self.instantiate_atask_from_atask_template,
            self.create_ateam,
            self.get_ateam,
            self.update_ateam,
            self.get_teams_in_aworkspace,
            self.get_teams_for_auser,
            self.add_auser_to_ateam,
            self.remove_auser_from_ateam,
            self.get_ateam_membership,
            self.get_team_memberships,
            self.get_memberships_from_ateam,
            self.get_memberships_from_auser,
            self.get_atime_period,
            self.get_time_periods,
            self.get_time_tracking_entries_for_atask,
            self.create_atime_tracking_entry,
            self.get_atime_tracking_entry,
            self.update_atime_tracking_entry,
            self.delete_atime_tracking_entry,
            self.get_objects_via_typeahead,
            self.get_multiple_users,
            self.get_auser,
            self.get_auser_sfavorites,
            self.get_users_in_ateam,
            self.get_users_in_aworkspace_or_organization,
            self.get_auser_task_list,
            self.get_auser_stask_list,
            self.get_multiple_webhooks,
            self.establish_awebhook,
            self.get_awebhook,
            self.update_awebhook,
            self.delete_awebhook,
            self.get_multiple_workspaces,
            self.get_aworkspace,
            self.update_aworkspace,
            self.add_auser_to_aworkspace_or_organization,
            self.remove_auser_from_aworkspace_or_organization,
            self.get_aworkspace_membership,
            self.get_workspace_memberships_for_auser,
            self.get_the_workspace_memberships_for_aworkspace,
        ]
