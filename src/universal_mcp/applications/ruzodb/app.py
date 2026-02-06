from typing import Any, List, Literal
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

        self._workspace_id = None

    async def _get_workspace_id(self) -> str:
        if self._workspace_id:
            return self._workspace_id

        credentials = await self.integration.get_credentials_async()
        self._workspace_id = credentials.get("workspace_id")
        return self._workspace_id

    async def _aget_headers(self) -> dict:
        credentials = await self.integration.get_credentials_async()
        token = credentials.get("token") or credentials.get("xc-token")
        return {"xc-token": token, "Content-Type": "application/json"}

    # ==================== Meta Operations (V3) ====================

    async def list_bases(self) -> dict[str, Any]:
        """
        List all bases in a specific workspace.

        Returns:
            dict: Dictionary with 'list' (array of bases).

        Tags:
            read, list, base, meta
        """
        workspace_id = await self._get_workspace_id()
        url = f"{self.base_url}/api/v3/meta/workspaces/{workspace_id}/bases"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_base(self, base_id: str) -> dict[str, Any]:
        """
        Get details of a specific base.

        Args:
            base_id: The ID of the base.

        Returns:
            dict: The base object.

        Tags:
            read, get, base, meta
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_base(self, title: str, type: str = "documentation", **kwargs) -> dict[str, Any]:
        """
        Create a new base in a specific workspace.

        Args:
            title: The title of the new base.
            type: Type of the base (default: 'documentation').

        Returns:
            dict: The created base object.

        Raises:
            HTTPError: If creation fails.

        Tags:
            create, base, meta
        """
        workspace_id = await self._get_workspace_id()
        url = f"{self.base_url}/api/v3/meta/workspaces/{workspace_id}/bases"
        data = {"title": title, "type": type, **kwargs}
        response = await self._apost(url, data=data)
        response.raise_for_status()
        return response.json()

    async def update_base(self, base_id: str, **kwargs) -> dict[str, Any]:
        """
        Update a base's metadata.

        Args:
            base_id: The ID of the base to update.
            **kwargs: Fields to update (e.g., title, color, etc.).

        Returns:
            dict: The updated base object.

        Tags:
            update, base, meta
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}"
        response = await self._apatch(url, data=kwargs)
        response.raise_for_status()
        return response.json()

    async def delete_base(self, base_id: str) -> dict[str, Any]:
        """
        Delete a base.

        Args:
            base_id: The ID of the base to delete.

        Returns:
            dict: The deletion confirmation.

        Tags:
            delete, base, meta, destructive
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def list_tables(self, base_id: str, limit: int = 50, offset: int = 0) -> dict[str, Any]:
        """
        List all tables in a specific base.

        Args:
            base_id: The ID of the base.
            limit: Number of tables to return (default: 50).
            offset: Number of tables to skip (default: 0).

        Returns:
            dict: Dictionary with 'list' (array of tables) and 'pageInfo'.

        Tags:
            read, list, table, meta, important
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables"
        params = {"limit": limit, "offset": offset}
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_table(self, base_id: str, table_id: str) -> dict[str, Any]:
        """
        Get the schema and metadata of a specific table.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.

        Returns:
            dict: The table object containing schema details.

        Tags:
            read, get, table, meta
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{table_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def list_views(self, base_id: str, table_id: str) -> dict[str, Any]:
        """
        List all views for a specific table.

        Args:
            base_id: The ID of the base (not used in V2 API, kept for compatibility).
            table_id: The ID of the table.

        Returns:
            dict: Dictionary with 'list' (array of views).

        Tags:
            read, list, view, meta
        """
        # Views API uses V2, not V3
        url = f"{self.base_url}/api/v2/meta/tables/{table_id}/views"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_shared_view(
        self,
        base_id: str,
        table_id: str,
        view_id: str,
        password: str = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a shared (public) view for a table view and get a shareable link.

        Args:
            base_id: The ID of the base (not used in V2 API, kept for compatibility).
            table_id: The ID of the table (not used in V2 API, kept for compatibility).
            view_id: The ID of the view to share.
            password: Optional password to protect the shared view.
            **kwargs: Additional sharing options (e.g., meta, survey_mode, etc.).

        Returns:
            dict: The shared view object containing 'uuid' and shareable URL.
                  The shareable URL format: {base_url}/nc/view/{uuid}

        Raises:
            HTTPError: If shared view creation fails.

        Tags:
            create, share, view, meta
        """
        # Shared views API uses V2, not V3
        url = f"{self.base_url}/api/v2/meta/views/{view_id}/share"
        data = {**kwargs}
        if password:
            data["password"] = password

        response = await self._apost(url, data=data)
        response.raise_for_status()
        result = response.json()

        # Add the shareable URL to the result for convenience
        if "uuid" in result:
            result["shareable_url"] = f"{self.base_url}/dashboard/#/nc/view/{result['uuid']}"

        return result

    async def delete_shared_view(
        self,
        base_id: str,
        table_id: str,
        view_id: str
    ) -> dict[str, Any]:
        """
        Delete (unshare) a shared view.

        Args:
            base_id: The ID of the base (not used in V2 API, kept for compatibility).
            table_id: The ID of the table (not used in V2 API, kept for compatibility).
            view_id: The ID of the view to unshare.

        Returns:
            dict: The deletion confirmation.

        Tags:
            delete, share, view, meta
        """
        # Shared views API uses V2, not V3
        url = f"{self.base_url}/api/v2/meta/views/{view_id}/share"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def create_table(
        self,
        base_id: str,
        title: str,
        columns: List[dict[str, Any]] = None,
        description: str = None,
        meta: dict[str, Any] = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a new table in a specific base with optional initial columns, description and metadata.

        Args:
            base_id: The ID of the base.
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
            dict: The created table object containing 'id', 'title', 'fields', 'public_view_url' which is the shareable url of the table.

        Raises:
            HTTPError: If the API request fails (e.g., 400 Bad Request if fields are invalid).

        Example:
            await app.create_table(
                base_id="base123",
                title="Customers",
                description="Customer data",
                columns=[
                    {'title': 'Name', 'uidt': 'SingleLineText'},
                    {'title': 'Status', 'uidt': 'SingleSelect', 'dtxp': 'Active,Inactive'}
                ]
            )

        Tags:
            create, table, meta, important
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables"
        fields_payload = []
        for col in columns or []:
            new_col = col.copy()
            if "type" not in new_col and "uidt" in new_col:
                new_col["type"] = new_col["uidt"]
            fields_payload.append(new_col)

        data = {"title": title, "fields": fields_payload, **kwargs}
        if description:
            data["description"] = description
        if meta:
            data["meta"] = meta

        response = await self._apost(url, data=data)
        response.raise_for_status()
        result = response.json()
        
        # Only create shared view if views exist in response (usually they do)
        if "views" in result and result["views"]:
            url = await self.create_shared_view(base_id=base_id, table_id=result["id"], view_id=result["views"][0]["id"])
            result["public_view_url"] = url["shareable_url"]
            
        return result

    async def update_table(
        self,
        base_id: str,
        table_id: str,
        title: str = None,
        description: str = None,
        meta: dict[str, Any] = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update a table's metadata (title, description, etc.).

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table to update.
            title: New title for the table (optional).
            description: New description for the table (optional).
            meta: New metadata (e.g., icon) for the table (optional).
            **kwargs: Additional fields to update.

        Returns:
            dict: The updated table object or confirmation.

        Tags:
            update, table, meta
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{table_id}"
        
        data = {**kwargs}
        if title:
            data["title"] = title
        if description:
            data["description"] = description
        if meta:
            data["meta"] = meta
            
        response = await self._apatch(url, data=data)
        response.raise_for_status()
        return response.json()

    async def delete_table(self, base_id: str, table_id: str) -> dict[str, Any]:
        """
        Delete a table by its ID from a specific base.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table to delete.

        Returns:
            dict: The deletion confirmation.

        Raises:
            HTTPError: If the table does not exist or deletion fails.

        Tags:
            delete, table, meta, destructive
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{table_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def create_column(
        self, base_id: str, table_id: str, title: str, uidt: RuzodbFieldType = "SingleLineText", column_name: str = None, **kwargs
    ) -> dict[str, Any]:
        """
        Create a new column (field) in an existing table.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            title: Display title for the column.
            uidt: UI Data Type. See `create_table` for full list of supported types.
                  Common types: 'SingleLineText', 'Number', 'Checkbox', 'Date', 'SingleSelect'.
            column_name: Database column name (optional).

        Returns:
            dict: The created column object containing 'id', 'title', 'uidt', etc.

        Raises:
            HTTPError: If column creation fails.

        Example:
            await app.create_column(
                base_id="base123",
                table_id="table456",
                title="Priority",
                uidt="SingleSelect",
                dtxp="High,Medium,Low"
            )

        Tags:
            create, column, field, meta
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{table_id}/fields"

        data = {
            "title": title,
            "column_name": column_name or title,
            "uidt": uidt,
            "type": uidt,  # Sending both just in case
            **kwargs,
        }
        response = await self._apost(url, data=data)
        response.raise_for_status()
        return response.json()

    async def delete_column(self, base_id: str, table_id: str, column_id: str) -> dict[str, Any]:
        """
        Delete a column (field) by its ID.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            column_id: The ID of the column to delete.

        Returns:
            dict: The deletion confirmation.

        Raises:
            HTTPError: If the column does not exist or deletion fails.

        Tags:
            delete, column, field, meta, destructive
        """
        url = f"{self.base_url}/api/v3/meta/bases/{base_id}/tables/{table_id}/fields/{column_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    # ==================== Data Operations (V3) ====================

    async def list_records(
        self,
        base_id: str,
        table_id: str,
        limit: int = 25,
        offset: int = 0,
        view_id: str = None,
        where: str = None,
        fields: List[str] = None,
        sort: List[str] = None,
    ) -> dict[str, Any]:
        """
        List records from a table with pagination and filtering.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            limit: Number of records to return (default: 25).
            offset: Number of records to skip (default: 0).
            view_id: The ID of the view to scope the request.
            where: Filter string (Ruzodb filter syntax).
            fields: List of specific field names to retrieve.
            sort: List of fields to sort by (e.g., ["-CreatedAt"]).

        Returns:
            dict: A dictionary containing 'list' (array of records) and 'pageInfo'.
                  Note: In V3, the key for records is 'records'.

        Tags:
            read, list, data, records
        """
        url = f"{self.base_url}/api/v3/data/{base_id}/{table_id}/records"
        params = {"limit": limit, "offset": offset, "viewId": view_id, "where": where}
        if fields:
            params["fields"] = ",".join(fields)
        if sort:
            params["sort"] = ",".join(sort)
        params = {k: v for k, v in params.items() if v is not None}
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def create_records(
        self, base_id: str, table_id: str, data: List[dict[str, Any]] | dict[str, Any]
    ) -> dict[str, Any] | List[dict[str, Any]]:
        """
        Create one or more records in a table.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            data: A dictionary (single record) or list of dictionaries (multiple records).
                  Keys should match column titles or names.

        Returns:
            dict | List: The created record(s).
                         If input is a list, returns a list of created records.
                         If input is a dict, returns the single created record dict.

        Tags:
            create, data, records
        """
        url = f"{self.base_url}/api/v3/data/{base_id}/{table_id}/records"
        is_bulk = isinstance(data, list)
        payload = data

        if is_bulk:
            payload = [{"fields": item} if "fields" not in item else item for item in data]
        elif isinstance(data, dict):
            if "fields" not in data:
                payload = {"fields": data}

        response = await self._apost(url, data=payload)
        response.raise_for_status()
        res_json = response.json()

        # Normalize response
        if isinstance(res_json, dict) and "records" in res_json:
            records = res_json["records"]
            if is_bulk:
                return records
            elif records:
                return records[0]

        return res_json

    async def get_record(self, base_id: str, table_id: str, record_id: str, fields: List[str] = None) -> dict[str, Any]:
        """
        Retrieve a single record by ID.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            record_id: The ID of the record.
            fields: List of specific field names to retrieve.

        Returns:
            dict: The record object.

        Tags:
            read, get, data, records
        """
        url = f"{self.base_url}/api/v3/data/{base_id}/{table_id}/records/{record_id}"
        params = {}
        if fields:
            params["fields"] = ",".join(fields)
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def update_records(
        self, base_id: str, table_id: str, data: List[dict[str, Any]] | dict[str, Any]
    ) -> dict[str, Any] | List[dict[str, Any]]:
        """
        Update one or more records.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            data: A dictionary or list of dictionaries. NOT containing 'id' or 'Id' key.
                  The 'id' should be part of the object if possible, or handled by logic.

        Returns:
            dict | List: The updated record(s).

        Tags:
            update, data, records
        """
        url = f"{self.base_url}/api/v3/data/{base_id}/{table_id}/records"

        def wrap(item):
            rid = item.get("Id") or item.get("id")
            if not rid:
                raise ValueError("Missing Id/id")
            flds = {k: v for k, v in item.items() if k not in ["Id", "id"]}
            return {"id": rid, "fields": flds}

        is_bulk = isinstance(data, list)
        payload = [wrap(i) for i in data] if is_bulk else wrap(data)

        response = await self._apatch(url, data=payload)
        response.raise_for_status()
        res_json = response.json()

        if is_bulk and isinstance(res_json, dict) and "records" in res_json:
            return res_json["records"]

        return res_json

    async def delete_records(self, base_id: str, table_id: str, record_ids: List[dict[str, Any]] | dict[str, Any]) -> dict[str, Any]:
        """
        Delete one or more records.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            record_ids: A list of dicts with 'id', or a single dict with 'id'.

        Returns:
            dict: The deletion result.

        Tags:
            delete, data, records, destructive
        """
        url = f"{self.base_url}/api/v3/data/{base_id}/{table_id}/records"

        def wrap(item):
            if isinstance(item, (int, str)):
                return {"id": item}
            rid = item.get("id") or item.get("Id")
            return {"id": rid}

        payload = [wrap(i) for i in record_ids] if isinstance(record_ids, list) else wrap(record_ids)
        if isinstance(record_ids, (int, str)):
            payload = [{"id": record_ids}]

        async with self.get_async_client() as client:
            response = await client.request("DELETE", url, json=payload)
        response.raise_for_status()
        return response.json()

    async def get_record_count(self, base_id: str, table_id: str, view_id: str = None, where: str = None) -> dict[str, Any]:
        """
        Get the count of records in a table (or view).

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            view_id: Optional View ID to count within.
            where: Optional filter.

        Returns:
            dict: Object containing 'count'.

        Tags:
            read, count, data, records
        """
        url = f"{self.base_url}/api/v3/data/{base_id}/{table_id}/count"

        params = {"viewId": view_id, "where": where}
        params = {k: v for k, v in params.items() if v is not None}
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def find_existing_values(
        self, base_id: str, table_id: str, field_name: str, values: List[str | int | float | bool], view_id: str = None
    ) -> List[dict[str, Any]]:
        """
        Check a list of values against a specific column and return those that already exist,
        along with their Record ID.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            field_name: The name of the column to check.
            values: A list of values to check for existence.
            view_id: Optional View ID.

        Returns:
            List[dict]: A list of dicts found: `[{"value": <val>, "record_id": <id>}, ...]`

        Tags:
            read, list, data, records, convenience, batch
        """
        if not values:
            return []

        existing_values = []
        chunk_size = 40  # Conservative limit to avoid URL length issues

        # Helper to chunk the list
        for i in range(0, len(values), chunk_size):
            chunk = values[i : i + chunk_size]

            # Construct where clause: (field,eq,val1)~or(field,eq,val2)...
            # We sanitize by ensuring basic string conversion
            conditions = [f"({field_name},eq,{v})" for v in chunk]
            where_clause = "~or".join(conditions)

            # We need the specific field AND the ID
            results = await self.list_records(
                base_id=base_id,
                table_id=table_id,
                view_id=view_id,
                where=where_clause,
                fields=[field_name, "Id", "id"],  # Request ID explicitly to be safe
                limit=100,
            )

            records = results.get("list", []) or results.get("records", [])
            for record in records:
                # NocoDB V3 wraps data in 'fields'
                data = record.get("fields", record)

                # Try to get ID from top-level record or nested data
                rid = record.get("Id") or record.get("id") or data.get("Id") or data.get("id")

                if field_name in data:
                    existing_values.append({"value": data[field_name], "record_id": rid})

        return existing_values

    def list_tools(self):
        return [
            self.list_bases,
            self.get_base,
            self.create_base,
            self.update_base,
            self.delete_base,
            self.list_tables,
            self.list_views,
            self.create_shared_view,
            self.delete_shared_view,
            self.create_table,
            self.update_table,
            self.get_table,
            self.delete_table,
            self.create_column,
            self.delete_column,
            self.list_records,
            self.create_records,
            self.get_record,
            self.update_records,
            self.delete_records,
            self.get_record_count,
            self.find_existing_values,
        ]
