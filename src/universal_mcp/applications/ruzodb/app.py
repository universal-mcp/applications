from typing import Any, List, Literal
import json
from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

RuzodbFieldType = Literal[
    "SingleLineText",
    "LongText",
    "Number",
    "Checkbox",
    "MultiSelect",
    "SingleSelect",
    "Date",
    "DateTime",
    "Year",
    "Time",
    "PhoneNumber",
    "Email",
    "URL",
    "Decimal",
    "Currency",
    "Percent",
    "Duration",
    "Rating",
    "Formula",
    "Rollup",
    "Lookup",
    "Attachment",
    "JSON",
    "Geometry",
    "CreatedTime",
    "LastModifiedTime",
    "CreatedBy",
    "LastModifiedBy",
]


class RuzodbApp(APIApplication):
    """
    Ruzodb Application using ONLY V3 API endpoints for all operations.
    Includes 6 Data operations and 4 Meta operations.
    """

    def __init__(self, integration: Integration = None, base_url: str = None, **kwargs) -> None:
        super().__init__(name="ruzodb", integration=integration, **kwargs)
        self.base_url = base_url or "https://nocodb.agentr.dev"

        self._base_id = None


    async def _call_backend(self, method: str, path: str, json_data: dict = None) -> dict[str, Any]:
        """Helper to call AgentR backend endpoints."""
        async with self.integration.client.aclient() as client:
            response = await client.request(method, path, json=json_data)
            return self._handle_response(response)

    async def _resolve_external_id(self, human_readable_id: str) -> dict[str, str]:
        """
        Resolve internal human-readable ID to external NocoDB ID and Base ID.
        Returns a dict with 'table_id' (external) and 'base_id'.
        """
        if not human_readable_id:
            raise ValueError("Table ID is required.")
            
        if not self.integration or not hasattr(self.integration, "client"):
             raise ValueError("RuzodbApp requires an integration with an AgentrClient")
        
        try:
            # Call backend to get details. Backend returns internal ID as 'table_id' 
            # and external ID as 'external_table_id' (as per my backend update).
            response = await self._call_backend("GET", f"/ruzodb/tables/{human_readable_id}")
            
            if isinstance(response, dict):
                 # Backend returns:
                 # table_id: internal
                 # external_table_id: external (added in last backend step)
                 # base_id: external
                 return {
                     "table_id": response.get("external_table_id"),
                     "base_id": response.get("base_id")
                 }
            
            raise ValueError(f"Unexpected response format for table {human_readable_id}")

        except Exception as e:
            raise ValueError(f"Failed to resolve ID for table {human_readable_id}: {str(e)}")

    async def _get_base_id(self, table_id: str) -> str:
        """Resolve base_id for a given table_id (internal)."""
        # We can reuse _resolve_external_id but we just want base_id
        resolved = await self._resolve_external_id(table_id)
        return resolved["base_id"]

    def _get_column_id(self, schema: dict, field_name: str) -> str:
        """Helper to find column ID by name from schema."""
        fields = schema.get("fields", [])
        for f in fields:
            if f.get("title") == field_name or f.get("column_name") == field_name:
                return f.get("id")
        return field_name # Return as is if not found (might already be ID)

    async def _aget_headers(self) -> dict:
        credentials = await self.integration.get_credentials_async()
        token = credentials.get("token") or credentials.get("xc-token")
        return {"xc-token": token, "Content-Type": "application/json"}

    async def getTablesList(self, limit: int = 7, offset: int = 0) -> dict[str, Any]:
        """
        List all tables accessible by the user with pagination support.

        Args:
            limit: Maximum number of tables to return (default: 7).
            offset: Number of tables to skip (default: 0).

        Returns:
            dict: The list of tables and pagination metadata.
            - total (int): Total number of tables available.
            - items (List[dict]): List of table objects.
                - table_id (str): The unique identifier for the table.
                - title (str): The display name of the table.
                - base_id (str): The ID of the base this table belongs to.
                - is_shared (bool): Whether the table is shared.
                - is_owner (bool): Whether the user owns this table.
                - share_url (str, optional): The URL to share the table, if applicable.

        Tags:
            read, meta, tables, structure, list
        """
        return await self._call_backend("GET", f"/ruzodb/tables?limit={limit}&offset={offset}")

    async def getTableSchema(self, tableId: str) -> dict[str, Any]:
        """
        Retrieve the detailed schema of a specific table including fields and views.

        Args:
            tableId: Table ID (Internal Human-Readable).

        Returns:
            dict: The complete schema definition of the table.
            - id (str): The unique identifier of the table.
            - title (str): The name of the table.
            - base_id (str): The ID of the base this table belongs to.
            - workspace_id (str): The ID of the workspace.
            - fields (List[dict]): List of field (column) definitions.
                - id (str): Field ID.
                - title (str): Field name.
                - type (str): Field type definition.
                - system (bool): Whether it is a system field.
            - views (List[dict]): List of views defined for this table.
                - id (str): View ID.
                - title (str): View name.

        Tags:
            read, meta, table, schema, structure
        """
        # Resolve internal ID to external ID and Base ID
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{external_table_id}"
        response = await self._aget(url)
        return self._handle_response(response)

    async def createTable(
        self,
        title: str,
        columns: List[dict[str, Any]] = None,
        description: str = None,
        meta: dict[str, Any] = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a new table within the user's base with optional columns and metadata.

        Args:
            title: The display title for the new table.
            columns: A list of column definitions to create immediately with the table.
                     Each column dict should specify 'title' and 'uidt' (or 'type').

                     Supported 'uidt' / 'type' values:
                     - Text: 'SingleLineText', 'LongText', 'Email', 'URL', 'PhoneNumber'
                     - Numeric: 'Number', 'Decimal', 'Currency', 'Percent'
                     - Date/Time: 'Date', 'DateTime', 'Time', 'Year', 'Duration'
                     - Choice: 'Checkbox', 'Rating'
                     - Selects: 'SingleSelect', 'MultiSelect' (Requires 'dtxp' options string, e.g., 'Option1,Option2')
                     - Specialized: 'Formula', 'Rollup', 'Lookup', 'Attachment', 'JSON', 'Geometry'
                     - System: 'CreatedTime', 'LastModifiedTime', 'CreatedBy', 'LastModifiedBy'
            description: Optional description for the table.
            meta: Optional metadata for the table (e.g. icon, color).
            **kwargs: Additional fields for table creation.

        Returns:
            dict: The created table metadata.
            - table_id (str): The unique identifier for the new table.
            - title (str): The table name.
            - base_id (str): The ID of the base.
            - is_shared (bool): Sharing status.
            - is_owner (bool): Ownership status.
            - share_url (str, optional): URL for sharing.

        Raises:
            HTTPError: If the API request fails (e.g., 400 Bad Request if fields are invalid).

        Example:
            await app.create_table(
                title="Customers",
                description="Customer data",
                columns=[
                    {'title': 'Name', 'uidt': 'SingleLineText'},
                    {'title': 'Status', 'uidt': 'SingleSelect', 'dtxp': 'Active,Inactive'}
                ]
            )

        Tags:
            create, meta, table, structure, important
        """
        payload = {"title": title, "columns": columns or []}
        return await self._call_backend("POST", "/ruzodb/tables", json_data=payload)

    async def deleteTable(self, tableId: str) -> dict[str, Any]:
        """
        Permanently delete a table by its ID.

        Args:
            tableId: The ID of the table to delete

        Returns:
            dict: Response containing deletion details.
            - detail (str): message confirming deletion or status.

        Raises:
            HTTPError: If the table does not exist or deletion fails.

        Tags:
            delete, meta, table, structure, destructive
        """
        return await self._call_backend("DELETE", f"/ruzodb/tables/{tableId}")

    async def updateTable(self, tableId: str, title: str) -> dict[str, Any]:
        """
        Update a table's metadata such as its title.

        Args:
            tableId: The ID of the table to update
            title: The new title for the table.

        Returns:
            dict: The updated table metadata.
            - table_id (str): The unique identifier.
            - title (str): The updated name.
            - base_id (str): The base ID.
            - is_shared (bool): Sharing status.

        Tags:
            update, meta, table, structure
        """
        payload = {"title": title}
        return await self._call_backend("PATCH", f"/ruzodb/tables/{tableId}", json_data=payload)

    async def createColumn(
        self, tableId: str, title: str, uidt: RuzodbFieldType = "SingleLineText", **kwargs
    ) -> dict[str, Any]:
        """
        Add a new column (field) to an existing table.

        Args:
            tableId: The ID of the table (Internal).
            title: Name of the new column.
            uidt: Type of the column (e.g., 'SingleLineText', 'Number').
            **kwargs: Type-specific options.

        Returns:
            dict: The created field definition.
            - id (str): Unique identifier for the new column.
            - table_id (str): The ID of the table containing this column.
            - title (str): The name of the column.
            - type (str): The data type code.
            - system (bool): Whether it is a system column.

        Tags:
            create, meta, column, structure
        """
        # Resolve
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{external_table_id}/fields"

        data = {
            "title": title,
            "type": uidt,
            **kwargs,
        }
        response = await self._apost(url, data=data)
        return self._handle_response(response)

    async def deleteColumn(self, tableId: str, columnId: str) -> dict[str, Any]:
        """
        Permanently remove a column from a table.

        Args:
            tableId: The ID of the table (Internal).
            columnId: The ID of the column to delete.

        Returns:
            dict: An empty dictionary upon successful deletion, or dict with keys for details.

        Tags:
            delete, meta, column, structure, destructive
        """
        # Resolve
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{external_table_id}/fields/{columnId}"
        response = await self._adelete(url)
        return self._handle_response(response)

    # ==================== Data Operations (V3) ====================

    async def queryRecords(
        self,
        tableId: str,
        limit: int = 25,
        offset: int = 0,
        viewId: str = None,
        where: str = None,
        fields: List[str] = None,
        sort: List[str] = None,
    ) -> dict[str, Any]:
        """
        Retrieve records from a table with advanced filtering, sorting, and pagination. Use `~and` and `~or` for combining conditions.

        Args:
            tableId: Table ID (Internal).
            limit: Maximum number of records to return (default: 25).
            offset: Number of records to skip (default: 0).
            viewId: Optional View ID to scope the query.
            where: Filter string using `(Col,Operator,Value)` syntax (e.g., `(Name,eq,John)`).
            fields: List of specific field names to retrieve.
            sort: List of field names to sort by. Use `-Field` for descending.

        Returns:
            dict: The query results and pagination info.
            - records (List[dict]): List of record objects containing field data and metadata (like 'id').
            - nestedNext (dict or None): Pagination cursor or metadata for next page.

        Tags:
            read, data, records, list, search
        """
        # Resolve
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/data/{base_id}/{external_table_id}/records"
        params = {"limit": limit, "offset": offset, "viewId": viewId, "where": where}
        if fields:
            params["fields"] = ",".join(fields)
        if sort:
            # NocoDB V3 expects sort as JSON string: [{"field": "column_name", "direction": "asc|desc"}]
            sort_list = []
            for s in sort:
                direction = "asc"
                field = s
                if s.startswith("-"):
                    direction = "desc"
                    field = s[1:]
                sort_list.append({"field": field, "direction": direction})
            import json
            params["sort"] = json.dumps(sort_list)
            
        params = {k: v for k, v in params.items() if v is not None}
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def createRecords(
        self, tableId: str, records: List[dict[str, Any]] | dict[str, Any]
    ) -> dict[str, Any] | List[dict[str, Any]]:
        """
        Create one or multiple new records in a table.

        Args:
            tableId: Table ID (Internal).
            records: A single dictionary of fields or a list of dictionaries for bulk creation.

        Returns:
            List[dict]: A list containing the created record objects, even if only one was created.
            - id (int|str): The ID of the created record.
            - fields (dict, optional): The field values of the record.

        Tags:
            create, data, records, batch
        """
        # Resolve
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/data/{base_id}/{external_table_id}/records"
        data = records
        is_bulk = isinstance(data, list)

        if is_bulk:
            payload = [{"fields": item} if "fields" not in item else item for item in data]
        elif isinstance(data, dict):
            if "fields" not in data:
                payload = {"fields": data}
            else:
                payload = data

        chunk_size = 10
        all_records = []
        
        # If not bulk, payload is a dict, just make one call
        if not is_bulk:
            response = await self._apost(url, data=payload)
            res_json = self._handle_response(response)
            if isinstance(res_json, dict) and "records" in res_json:
                 # It's a single record creation but wrapped in records list sometimes? 
                 # Actually single creation usually returns the record directly or a list of 1.
                 # Let's keep existing logic for single record but use new flow.
                 pass
            return res_json

        # Bulk creation
        for i in range(0, len(payload), chunk_size):
            chunk = payload[i : i + chunk_size]
            response = await self._apost(url, data=chunk)
            res_json = self._handle_response(response)
            
            if isinstance(res_json, dict) and "records" in res_json:
                all_records.extend(res_json["records"])
            elif isinstance(res_json, list):
                all_records.extend(res_json)
            else:
                # Unexpected format, maybe just append the whole thing?
                # Or if it's a single object, append it.
                all_records.append(res_json)

        return all_records

    async def getRecord(self, tableId: str, recordId: str, fields: List[str] = None) -> dict[str, Any]:
        """
        Retrieve a single unique record by its ID.

        Args:
            tableId: Table ID (Internal).
            recordId: The unique ID of the record.
            fields: Optional list of fields to include in the response.

        Returns:
            dict: The record object.
            - id (int|str): The unique ID of the record.
            - fields (dict, optional): Dictionary of field names and values.

        Tags:
            read, data, records, detail
        """
        # Resolve
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/data/{base_id}/{external_table_id}/records/{recordId}"
        params = {}
        if fields:
            params["fields"] = ",".join(fields)
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def updateRecords(
        self, tableId: str, records: List[dict[str, Any]] | dict[str, Any]
    ) -> dict[str, Any] | List[dict[str, Any]]:
        """
        Update existing records in a table with new value.

        Args:
            tableId: Table ID (Internal).
            records: A single dictionary or list of dictionaries. Each must contain an 'id' or 'Id' key.

        Returns:
            List[dict]: A list of updated record objects.
            - id (int|str): The ID of the updated record.
            - fields (dict, optional): The updated field values.

        Tags:
            update, data, records, batch
        """
        # Resolve
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/data/{base_id}/{external_table_id}/records"
        data = records

        is_bulk = isinstance(data, list)

        def wrap(item):
            rid = item.get("Id") or item.get("id")
            fields = item.get("fields")
            if not fields:
                # If fields not explicit, assume other keys are fields
                fields = {k: v for k, v in item.items() if k.lower() != "id"}
            
            return {"id": rid, "fields": fields}

        payload = [wrap(i) for i in data] if is_bulk else wrap(data)

        if not is_bulk:
            response = await self._apatch(url, data=payload)
            return self._handle_response(response)

        chunk_size = 10
        all_records = []

        for i in range(0, len(payload), chunk_size):
            chunk = payload[i : i + chunk_size]
            response = await self._apatch(url, data=chunk)
            res_json = self._handle_response(response)

            if isinstance(res_json, dict) and "records" in res_json:
                all_records.extend(res_json["records"])
            elif isinstance(res_json, list):
                all_records.extend(res_json)
            else:
                all_records.append(res_json)

        return all_records

    async def deleteRecords(self, tableId: str, records: List[dict[str, Any]] | dict[str, Any]) -> dict[str, Any]:
        """
        Permanently delete one or more records from a table.

        Args:
            tableId: Table ID (Internal).
            records: A single record dictionary/ID, or a list of them. Each item must identify the record to delete.

        Returns:
            dict: Result of the deletion operation.
            - records (List[dict]): List of deleted record stubs.
                - id (int|str): ID of the deleted record.
                - deleted (bool): Status of deletion.

        Tags:
            delete, data, records, destructive, batch
        """
        # Resolve
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/data/{base_id}/{external_table_id}/records"
        record_ids = records

        def wrap(item):
            if isinstance(item, (int, str)):
                return {"id": item}
            rid = item.get("id") or item.get("Id")
            return {"id": rid}

        payload = [wrap(i) for i in record_ids] if isinstance(record_ids, list) else wrap(record_ids)
        if isinstance(record_ids, (int, str)):
            payload = [{"id": record_ids}]

        chunk_size = 10
        results = []
        
        async with self.get_async_client() as client:
            for i in range(0, len(payload), chunk_size):
                chunk = payload[i : i + chunk_size]
                response = await client.request("DELETE", url, json=chunk)
                
                results.append(self._handle_response(response))
                
        # Return the last result or a consolidated one. 
        # For simplicity returning the last one or the first if available.
        return results[-1] if results else {}

    async def countRecords(self, tableId: str, viewId: str = None, where: str = None) -> dict[str, Any]:
        """
        Count the total number of records matching optional filters.

        Args:
            tableId: Table ID (Internal).
            viewId: Optional View ID to restrict scope.
            where: Optional filter string in `(Col,Operator,Value)` format.

        Returns:
            dict: The count result.
            - count (int): The total count of matching records.

        Tags:
            read, data, records, count
        """
        # Resolve
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        base_id = resolved["base_id"]

        url = f"{self.base_url}/api/v3/data/{base_id}/{external_table_id}/count"

        params = {"viewId": viewId, "where": where}
        params = {k: v for k, v in params.items() if v is not None}
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def findDuplicates(
        self, tableId: str, fieldName: str, values: List[str | int | float | bool], viewId: str = None
    ) -> List[dict[str, Any]]:
        """
        Identify existing records that match a specific list of values for a given column.

        Args:
            tableId: The ID of the table (Internal).
            fieldName: The name of the column to check against.
            values: List of values to check for existence.
            viewId: Optional View ID to restrict scope.

        Returns:
            List[dict]: A list of found duplicates.
            - value (Any): The value that was found in the table.
            - record_id (int|str): The ID of the existing record containing this value.

        Tags:
            read, data, records, convenience, search
        """
        if not values:
            return []

        existing_values = []
        chunk_size = 40
        
        for i in range(0, len(values), chunk_size):
            chunk = values[i : i + chunk_size]
            # Construct where clause for (col,eq,val) OR ...
            conditions = [f"({fieldName},eq,{v})" for v in chunk]
            where_clause = "~or".join(conditions)

            # queryRecords handles ID resolution internally
            results = await self.queryRecords(
                tableId=tableId,
                viewId=viewId,
                where=where_clause,
                fields=[fieldName, "Id", "id"],
                limit=1000,
            )
            
            records = results.get("list", []) or results.get("records", [])
            for record in records:
                data = record.get("fields", record)
                rid = record.get("Id") or record.get("id") or data.get("Id") or data.get("id")
                
                # Check if value matches (formatting might differ, e.g. string vs int)
                # But we queried for it, so it should be there.
                val_in_record = data.get(fieldName)
                if val_in_record is not None:
                     existing_values.append({"value": val_in_record, "record_id": rid})

        return existing_values

    async def aggregateRecords(
        self,
        tableId: str,
        aggregations: List[dict[str, Any]],
        viewId: str = None,
        where: str = None,
    ) -> dict[str, Any]:
        """
        Perform aggregation calculations (e.g., avg, sum) on table data.

        Args:
            tableId: The ID of the table (Internal).
            aggregations: List of aggregation requests. Each dict must have:
                          - field: Name of the column.
                          - type: Function (avg, sum, min, max, count).
                          - alias: Optional custom key for the result.
            viewId: Optional View ID.
            where: Optional filter string.

        Returns:
            dict: Dictionary where keys are aliases (or generated names) and values are the computed results.
            Example: {'Age_avg': 25.5, 'Total_Revenue': 5000}

        Tags:
            read, data, analytics, aggregation
        """
        schema = await self.getTableSchema(tableId)
        
        resolved = await self._resolve_external_id(tableId)
        external_table_id = resolved["table_id"]
        if not external_table_id: 
             raise ValueError("Failed to resolve external table ID")

        # 1. Fetch Schema (using Internal ID as getTableSchema expects)
        # Note: getTableSchema already resolves ID internally, but we need it here for column IDs
        
        # 2. Resolve View ID
        target_view_id = viewId
        if not target_view_id:
            views = schema.get("views", [])
            if views:
                target_view_id = views[0]["id"]
            else:
                # If schema doesn't have views, fetch them manually using external ID
                base_id = resolved["base_id"]
                url_views = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{external_table_id}/views"
                resp_views = await self._aget(url_views)
                if resp_views.status_code == 200:
                    views = resp_views.json().get("list", [])
                    if views:
                        target_view_id = views[0]["id"]
        
        if not target_view_id:
             raise ValueError("Could not determine a View ID for aggregation.")

        final_results = {}
        
        for agg in aggregations:
            field_name = agg.get("field")
            col_id = self._get_column_id(schema, field_name)
            agg_type = agg.get("type")
            key = agg.get("alias") or f"{field_name or 'count'}_{agg_type}"
            
            single_agg = [{"field": col_id, "type": agg_type}]
            
            # Use EXTERNAL Table ID here for V2 aggregation endpoint
            url = f"{self.base_url}/api/v2/tables/{external_table_id}/aggregate"
            params = {"aggregation": json.dumps(single_agg), "viewId": target_view_id}
            
            if where: params["where"] = where
                
            try:
                response = await self._aget(url, params=params)
                data = self._handle_response(response)
                
                if isinstance(data, dict) and data.get("status") == "error":
                    final_results[key] = data
                    continue

                val = None
                if data: val = next(iter(data.values()))
                
                if val is None and agg_type == "count" and field_name in ["Id", "id"]:
                    non_id_fields = [f for f in schema.get("fields", []) if f.get("title") not in ["Id", "id"]]
                    if non_id_fields:
                        fallback_agg = [{"field": non_id_fields[0].get("id"), "type": "count"}]
                        params["aggregation"] = json.dumps(fallback_agg)
                        data_retry = self._handle_response(await self._aget(url, params=params))
                        if data_retry: val = next(iter(data_retry.values()))

                final_results[key] = val

            except Exception as e:
                final_results[key] = {"status": "error", "text": str(e)}
                
        return final_results

    def list_tools(self):
        return [
            self.getTablesList,
            self.getTableSchema,
            self.createTable,
            self.deleteTable,
            self.updateTable,
            self.createColumn,
            self.deleteColumn,
            self.queryRecords,
            self.createRecords,
            self.getRecord,
            self.updateRecords,
            self.deleteRecords,
            self.countRecords,
            self.aggregateRecords,
            self.findDuplicates,
        ]
