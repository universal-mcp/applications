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

    async def _resolve_internal_id(self, tableId: str) -> str:
        """Resolve external NocoDB Table ID to backend's RuzodbTable ID."""
        if not tableId:
            return tableId
        if tableId.startswith("ruzodb-table"):
            return tableId

        try:
            async with self.integration.client.aclient() as client:
                response = await client.request("GET", "/ruzodb/tables")
                if response.status_code == 200:
                    tables = response.json()
                    for t in tables:
                        if t.get("table_id") == tableId:
                            return t.get("id")
        except Exception as e:
            logger.warning(f"Failed to resolve internal ID for {tableId}: {e}")
        
        return tableId

    async def _call_backend(self, method: str, path: str, json_data: dict = None) -> dict[str, Any]:
        """Helper to call AgentR backend endpoints."""
        async with self.integration.client.aclient() as client:
            response = await client.request(method, path, json=json_data)
            return self._handle_response(response)

    async def _get_base_id(self, table_id: str) -> str:
        """Resolve base_id for a given table_id."""
        if not table_id:
            raise ValueError("Table ID is required to perform this operation.")
            
        if not self.integration or not hasattr(self.integration, "client"):
             raise ValueError("RuzodbApp requires an integration with an AgentrClient to auto-fetch base_id")
        
        try:
            async with self.integration.client.aclient() as client:
                # Resolve base_id for specific table (potentially shared)
                # The backend endpoint /ruzodb/tables/{table_id} handles resolution and auth
                response = await client.request("GET", f"/ruzodb/tables/{table_id}")
                if response.status_code == 200:
                    data = response.json()
                    return data.get("base_id")
                
                # If backend resolution fails, we can't proceed because we don't know which base to use.
                # Falling back to user's default base is dangerous for shared tables.
                raise ValueError(f"Could not resolve base_id for table {table_id} (Status {response.status_code})")

        except Exception as e:
            raise ValueError(f"Failed to resolve RuzoDB base_id: {str(e)}")

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

    async def getTablesList(self) -> dict[str, Any]:
        """
        List tables accessible by user.

        Returns:
            dict: A dictionary containing a 'list' key, which holds a list of table objects.
                  Each table object is a dictionary with keys: 'id', 'title', 'base_id', 'workspace_id'.
                  Example: {'list': [{'id': '...', 'title': '...', 'base_id': '...', 'workspace_id': '...'}, ...]}

        Tags:
            read, list, meta, tables, structure
        """
        return {"list": await self._call_backend("GET", "/ruzodb/tables")}

    async def getTableSchema(self, tableId: str) -> dict[str, Any]:
        """
        Get the table schema including fields and views information.

        Args:
            tableId: Table Id.

        Returns:
            dict: The table object.
                  Keys include: 'id', 'title', 'base_id', 'workspace_id', 'views' (list), 'fields' (list), 'display_field_id', 'source_id'.
                  Example: {'id': '...', 'title': 'mytable', 'fields': [...], 'views': [...]}

        Tags:
            read, get, meta, table, structure
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{tableId}"
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
        Create a new table in a specific base with optional initial columns, description and metadata.

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
            dict: The created table object.
                  Keys include: 'id', 'title', 'base_id', 'workspace_id', 'fields' (list of columns), 'views' (list of views).
                  Example: {'id': '...', 'title': '...', 'fields': [...], 'views': [...]}

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
            create, meta, table, structure
        """
        payload = {"title": title, "columns": columns or []}
        return await self._call_backend("POST", "/ruzodb/tables", json_data=payload)

    async def deleteTable(self, tableId: str) -> dict[str, Any]:
        """
        Delete a table by its ID from a specific base.


        Args:
            tableId: The ID of the table to delete


        Returns:
            dict: An empty dictionary {} on successful deletion.

        Raises:
            HTTPError: If the table does not exist or deletion fails.

        Tags:
            delete, meta, table, structure, destructive
        """
        internal_id = await self._resolve_internal_id(tableId)
        return await self._call_backend("DELETE", f"/ruzodb/tables/{internal_id}")

    async def updateTable(self, tableId: str, title: str) -> dict[str, Any]:
        """
        Update a table (e.g. rename) via backend endpoint to maintain sync.

        Args:
            tableId: The ID of the table to update
            title: The new title for the table.

        Returns:
            dict: The updated table object.

        Tags:
            update, meta, table, structure
        """
        internal_id = await self._resolve_internal_id(tableId)
        payload = {"title": title}
        return await self._call_backend("PATCH", f"/ruzodb/tables/{internal_id}", json_data=payload)

    async def createColumn(
        self, tableId: str, title: str, uidt: RuzodbFieldType = "SingleLineText", **kwargs
    ) -> dict[str, Any]:
        """
        Create a new column (field) in an existing table.

        Args:
            tableId: The ID of the table.
            title: Display title for the column.
            uidt: UI Data Type. See `createTable` for full list of supported types.
                  Common types: 'SingleLineText', 'Number', 'Checkbox', 'Date', 'SingleSelect'.

        Returns:
            dict: The created column object.
                  Keys include: 'id', 'table_id', 'title', 'type', 'system'.
                  Example: {'id': '...', 'title': '...', 'type': '...', ...}

        Raises:
            HTTPError: If column creation fails.

        Example:
            await app.create_column(
                table_id="table456",
                title="Priority",
                uidt="SingleSelect",
                dtxp="High,Medium,Low"
            )

        Tags:
            create, meta, column, field, structure
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{tableId}/fields"

        data = {
            "title": title,
            "type": uidt,
            **kwargs,
        }
        response = await self._apost(url, data=data)
        return self._handle_response(response)

    async def deleteColumn(self, tableId: str, columnId: str) -> dict[str, Any]:
        """
        Delete a column (field) by its ID.


        Args:
            tableId: The ID of the table.
            columnId: The ID of the column to delete.


        Returns:
            dict: An empty dictionary {} on successful deletion.

        Raises:
            HTTPError: If the column does not exist or deletion fails.

        Tags:
            delete, meta, column, field, structure, destructive
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{tableId}/fields/{columnId}"
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
        List records from a table with pagination and specific filtering using `(Col,Operator,Value)` syntax.

        Args:
            tableId: Table ID.
            limit: Number of records to return (default: 25).
            offset: Number of records to skip (default: 0).
            viewId: The ID of the view to scope the request.
            where: Filter string (Ruzodb/NocoDB filter syntax).
                   Syntax: `(ColumnName,Operator,Value)`
                   Child clauses can be combined with `~or` or `~and`.
                   
                   Common Operators:
                   - eq, neq, like, ge (>=), le (<=), gt (>), lt (<)
                   - isnull, isnotnull
                   - in, notin (Values separated by comma)

                   Examples:
                   - `(Status,eq,Active)`
                   - `(Age,gt,18)~and(City,like,New York)`
                   - `(Category,in,Tech,Science)`
            fields: List of specific field names to retrieve.
            sort: List of fields to sort by (e.g., ["-CreatedAt"]).

        Returns:
            dict: The query result.
                  Keys include: 'records' (list), 'next' (pagination URL), 'nestedNext'.
                  Example: {'records': [{'id': 1, 'fields': {...}}], 'next': '...', 'nestedNext': ...}

        Tags:
            read, list, data, records, filter, sort
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/data/{base_id}/{tableId}/records"
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
        Create records in a table.

        Args:
            tableId: Table ID.
            records: Array of records, each with a `fields` object containing key-value pairs.
                     (Note: Single record dict is also supported for convenience)

        Returns:
            dict | list: The created record(s).
                  - Single input (dict): Returns {'records': [{'id': ..., 'fields': {...}}]}
                  - Bulk input (list): Returns a list of record objects [{'id': ..., 'fields': {...}}, ...]

        Tags:
            create, data, records, batch, important
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/data/{base_id}/{tableId}/records"
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
        Fetch a record by ID.

        Args:
            tableId: Table ID.
            recordId: Record ID or primary key value.
            fields: List of specific field names to retrieve.

        Returns:
            dict: The record object.
                  Keys include: 'id', 'fields' (dictionary of column values).
                  Example: {'id': 1, 'fields': {'Title': '...', 'Status': '...'}}

        Tags:
            read, get, data, records
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/data/{base_id}/{tableId}/records/{recordId}"
        params = {}
        if fields:
            params["fields"] = ",".join(fields)
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def updateRecords(
        self, tableId: str, records: List[dict[str, Any]] | dict[str, Any]
    ) -> dict[str, Any] | List[dict[str, Any]]:
        """
        Update records in a table.

        Args:
            tableId: Table ID.
            records: Array of records, each with `id` and `fields` to update.
                     (Note: Single record dict is also supported)

        Returns:
            dict | list: The updated record(s).
                  - Single input (dict): Returns {'records': [{'id': ..., 'fields': {...}}]}
                  - Bulk input (list): Returns a list of record objects [{'id': ..., 'fields': {...}}, ...]

        Tags:
            update, data, records, batch
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/data/{base_id}/{tableId}/records"
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
        Delete records in a table.

        Args:
            tableId: Table ID.
            records: Array of records with `id` property to delete.
                     (Note: Single record dict or ID list is also supported)

        Returns:
            dict: The result of the deletion operation.
                  Format: {'records': [{'id': ..., 'deleted': True}, ...]}
                  Note: If deleting > 10 records, returns the result of the last batch.

        Tags:
            delete, data, records, destructive, batch
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/data/{base_id}/{tableId}/records"
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
        Count Records in a Table.

        Args:
            tableId: Table ID.
            viewId: Optional View ID to count within.
            where: Optional filter.

        Returns:
            dict: The count object.
                  Keys include: 'count'.
                  Example: {'count': 42}

        Tags:
            read, count, data, records
        """
        base_id = await self._get_base_id(tableId)

        url = f"{self.base_url}/api/v3/data/{base_id}/{tableId}/count"

        params = {"viewId": viewId, "where": where}
        params = {k: v for k, v in params.items() if v is not None}
        response = await self._aget(url, params=params)
        return self._handle_response(response)

    async def findDuplicates(
        self, tableId: str, fieldName: str, values: List[str | int | float | bool], viewId: str = None
    ) -> List[dict[str, Any]]:
        """
        Check a list of values against a specific column and return those that already exist along with their Record ID.

        Args:
            tableId: The ID of the table.
            fieldName: The name of the column to check.
            values: A list of values to check for existence.
            viewId: Optional View ID.

        Returns:
            List[dict]: A list of dictionaries representing found duplicates.
                        Keys include: 'value', 'record_id'.
                        Example: [{'value': 'Dup1', 'record_id': 123}, ...]

        Tags:
            read, list, data, records, convenience, batch, search
        """
        if not values:
            return []

        base_id = await self._get_base_id(tableId)

        existing_values = []
        chunk_size = 40  # Conservative limit to avoid URL length issues

        # Helper to chunk the list
        for i in range(0, len(values), chunk_size):
            chunk = values[i : i + chunk_size]

            # Construct where clause: (field,eq,val1)~or(field,eq,val2)...
            # We sanitize by ensuring basic string conversion
            conditions = [f"({fieldName},eq,{v})" for v in chunk]
            where_clause = "~or".join(conditions)

            # We need the specific field AND the ID
            results = await self.queryRecords(
                tableId=tableId,
                viewId=viewId,
                where=where_clause,
                fields=[fieldName, "Id", "id"],  # Request ID explicitly to be safe
                limit=1000,
            )

            records = results.get("list", []) or results.get("records", [])
            for record in records:
                # NocoDB V3 wraps data in 'fields'
                data = record.get("fields", record)

                # Try to get ID from top-level record or nested data
                rid = record.get("Id") or record.get("id") or data.get("Id") or data.get("id")

                if fieldName in data:
                    existing_values.append({"value": data[fieldName], "record_id": rid})

        return existing_values

    async def aggregateRecords(
        self,
        tableId: str,
        aggregations: List[dict[str, Any]],
        viewId: str = None,
        where: str = None,
    ) -> dict[str, Any]:
        """
        Perform aggregations on a table with a filter condition. This allows you to compute summary statistics across your data.

        Args:
            tableId: The ID of the table to aggregate data from.
            aggregations: Array of aggregation operations to perform. Each object must have:
                          - `field`: The field/column ID (or Title) to aggregate.
                          - `type`: The aggregation type to perform.
                          - `alias`: Optional alias for the result key.
                          
                          Supported Types:
                          - Numerical: `sum`, `min`, `max`, `avg`, `median`, `std_dev`, `range`
                          - All Types: `count`, `count_empty`, `count_filled`, `count_unique`, `percent_empty`, `percent_filled`, `percent_unique`
                          - Boolean: `checked`, `unchecked`, `percent_checked`, `percent_unchecked`
                          - Date: `earliest_date`, `latest_date`, `date_range`, `month_range`
            viewId: Optional View ID. (Required for V2 API, auto-fetched if None)
            where: Filter condition using NocoDB syntax (e.g., `(status,eq,completed)`).

        Returns:
            dict: The aggregation results.
                  Keys are Field Names (or provided aliases).
                  Example: {'revenue': 5000, 'customer_id': 150}

        Tags:
            read, data, records, aggregate, batch, statistics
        """
        # 1. Fetch Schema to map Field Names to IDs and get default View ID
        schema = await self.getTableSchema(tableId)
        
        # 2. Resolve View ID
        target_view_id = viewId
        if not target_view_id:
            views = schema.get("views", [])
            if views:
                target_view_id = views[0]["id"]
            else:
                # Try fetching views explicitly if schema didn't have them
                base_id = await self._get_base_id(tableId)
                url_views = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{tableId}/views"
                resp_views = await self._aget(url_views)
                if resp_views.status_code == 200:
                     views = resp_views.json().get("list", [])
                     if views:
                         target_view_id = views[0]["id"]
        
        if not target_view_id:
             raise ValueError("Could not determine a View ID for aggregation. Please provide 'viewId'.")

        # 3. Map Aggregations (Field Name -> Column ID) and Prepare Sequential Execution
        # NocoDB V2 has a limitation where multiple aggregations on the same field clobber each other in the response 
        # (e.g. {"Score": 25} overwrites {"Score": 100}). Also, aliases are ignored in the response keys.
        # To robustly support multiple aggregations and aliases, we must execute them sequentially or grouped by field.
        # For simplicity and reliability, we will execute them sequentially.
        
        final_results = {}
        
        for agg in aggregations:
            field_name = agg.get("field")
            col_id = self._get_column_id(schema, field_name)
            agg_type = agg.get("type")
            alias = agg.get("alias")
            
            # Construct single-item aggregation payload
            single_agg = [{
                "field": col_id,
                "type": agg_type
            }]
            
            # Call V2 API
            url = f"{self.base_url}/api/v2/tables/{tableId}/aggregate"
            params = {"aggregation": json.dumps(single_agg), "viewId": target_view_id}
            
            if where:
                params["where"] = where
                
            try:
                response = await self._aget(url, params=params)
                data = self._handle_response(response)
                
                if isinstance(data, dict) and data.get("status") == "error":
                    final_results[key] = data
                    continue

                # data is like {"Score": 25} or {"Id": null}
                val = None
                if data:
                    val = next(iter(data.values()))
                
                # Special handling for COUNT on ID returning null (NocoDB bug/quirk?)
                if val is None and agg_type == "count" and field_name in ["Id", "id"]:
                    # Find a fallback field (e.g. Title field)
                    non_id_fields = [f for f in schema.get("fields", []) if f.get("title") not in ["Id", "id"]]
                    if non_id_fields:
                        fallback_field = non_id_fields[0]
                        fallback_id = fallback_field.get("id")
                        fallback_agg = [{"field": fallback_id, "type": "count"}]
                        
                        params["aggregation"] = json.dumps(fallback_agg)
                        resp_retry = await self._aget(url, params=params)
                        data_retry = self._handle_response(resp_retry)
                        
                        if isinstance(data_retry, dict) and data_retry.get("status") == "error":
                            val = data_retry
                        elif data_retry:
                            val = next(iter(data_retry.values()))

                # Store result
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
