
from typing import Any, List, Literal
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

NocoDBFieldType = Literal[
    "SingleLineText", "LongText", "Number", "Checkbox", "MultiSelect", "SingleSelect", 
    "Date", "DateTime", "Year", "Time", "PhoneNumber", "Email", "URL", "Decimal", 
    "Currency", "Percent", "Duration", "Rating", "Formula", "Rollup", "Lookup", 
    "Attachment", "JSON", "Geometry", "CreatedTime", "LastModifiedTime", "CreatedBy", "LastModifiedBy"
]

FIXED_BASE_ID = "prx1mkflfxn86fg" 
TOKEN = "9wEYlDWJc4W8bgAY28PnV_k5fPTsIovHCxlHQtd8" 

class NocodbV3App(APIApplication):
    """
    NocoDB Application using ONLY V3 API endpoints for all operations.
    Includes 6 Data operations and 4 Meta operations.
    """

    def __init__(self, integration: Integration = None, base_url: str = None, **kwargs) -> None:
        super().__init__(name="nocodb_v3", integration=integration, **kwargs)
        self.base_url = base_url or "https://nocodb.agentr.dev"

    async def _aget_headers(self) -> dict:
        return {
            "xc-token": TOKEN,
            "Content-Type": "application/json"
        }

    # ==================== Meta Operations (V3) ====================

    async def list_tables(
        self,
        limit: int = 50,
        offset: int = 0
    ) -> dict[str, Any]:
        """
        List all tables in the fixed base.

        Args:
            limit: Number of tables to return (default: 50).
            offset: Number of tables to skip (default: 0).

        Returns:
            dict: Dictionary with 'list' (array of tables) and 'pageInfo'.

        Tags:
            read, list, table, meta, important
        """
        url = f"{self.base_url}/api/v3/meta/bases/{FIXED_BASE_ID}/tables"
        params = {"limit": limit, "offset": offset}
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def create_table(
        self,
        title: str,
        table_name: str = None,
        columns: List[dict[str, Any]] = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a new table in the fixed base with optional initial columns.

        Args:
            title: The display title for the new table.
            table_name: The physical database table name (optional).
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

        Returns:
            dict: The created table object containing 'id', 'title', 'fields', etc.

        Raises:
            HTTPError: If the API request fails (e.g., 400 Bad Request if fields are invalid).

        Example:
            await app.create_table(
                title="Customers",
                columns=[
                    {'title': 'Name', 'uidt': 'SingleLineText'},
                    {'title': 'Status', 'uidt': 'SingleSelect', 'dtxp': 'Active,Inactive'}
                ]
            )

        Tags:
            create, table, meta, important
        """
        url = f"{self.base_url}/api/v3/meta/bases/{FIXED_BASE_ID}/tables"
        fields_payload = []
        for col in (columns or []):
            new_col = col.copy()
            if "type" not in new_col and "uidt" in new_col:
                new_col["type"] = new_col["uidt"]
            fields_payload.append(new_col)

        data = {
            "title": title,
            "table_name": table_name or title,
            "fields": fields_payload,
            **kwargs
        }
        response = await self._apost(url, data=data)
        response.raise_for_status()
        return response.json()

    async def delete_table(self, table_id: str) -> dict[str, Any]:
        """
        Delete a table by its ID from the fixed base.

        Args:
            table_id: The ID of the table to delete.

        Returns:
            dict: The deletion confirmation.

        Raises:
            HTTPError: If the table does not exist or deletion fails.

        Tags:
            delete, table, meta, destructive
        """
        url = f"{self.base_url}/api/v3/meta/bases/{FIXED_BASE_ID}/tables/{table_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    async def create_column(
        self,
        table_id: str,
        title: str,
        uidt: NocoDBFieldType = "SingleLineText",
        column_name: str = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a new column (field) in an existing table.

        Args:
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
                table_id="table456",
                title="Priority",
                uidt="SingleSelect",
                dtxp="High,Medium,Low"
            )

        Tags:
            create, column, field, meta
        """
        url = f"{self.base_url}/api/v3/meta/bases/{FIXED_BASE_ID}/tables/{table_id}/fields"
        data = {
            "title": title,
            "column_name": column_name or title,
            "uidt": uidt,
            "type": uidt, # Sending both just in case
            **kwargs
        }
        response = await self._apost(url, data=data)
        response.raise_for_status()
        return response.json()

    async def delete_column(self, table_id: str, column_id: str) -> dict[str, Any]:
        """
        Delete a column (field) by its ID.

        Args:
            table_id: The ID of the table.
            column_id: The ID of the column to delete.

        Returns:
            dict: The deletion confirmation.

        Raises:
            HTTPError: If the column does not exist or deletion fails.

        Tags:
            delete, column, field, meta, destructive
        """
        url = f"{self.base_url}/api/v3/meta/bases/{FIXED_BASE_ID}/tables/{table_id}/fields/{column_id}"
        response = await self._adelete(url)
        response.raise_for_status()
        return response.json()

    # ==================== Data Operations (V3) ====================

    async def list_records(
        self,
        table_id: str,
        limit: int = 25,
        offset: int = 0,
        view_id: str = None,
        where: str = None,
        fields: List[str] = None,
        sort: List[str] = None
    ) -> dict[str, Any]:
        """
        List records from a table with pagination and filtering.

        Args:
            table_id: The ID of the table.
            limit: Number of records to return (default: 25).
            offset: Number of records to skip (default: 0).
            view_id: The ID of the view to scope the request.
            where: Filter string (NocoDB filter syntax).
            fields: List of specific field names to retrieve.
            sort: List of fields to sort by (e.g., ["-CreatedAt"]).

        Returns:
            dict: A dictionary containing 'list' (array of records) and 'pageInfo'.
                  Note: In V3, the key for records is 'records'.

        Tags:
            read, list, data, records
        """
        url = f"{self.base_url}/api/v3/data/{FIXED_BASE_ID}/{table_id}/records"
        params = {"limit": limit, "offset": offset, "viewId": view_id, "where": where}
        if fields: params["fields"] = ",".join(fields)
        if sort: params["sort"] = ",".join(sort)
        params = {k: v for k, v in params.items() if v is not None}
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def create_records(
        self,
        table_id: str,
        data: List[dict[str, Any]] | dict[str, Any]
    ) -> dict[str, Any] | List[dict[str, Any]]:
        """
        Create one or more records in a table.

        Args:
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
        url = f"{self.base_url}/api/v3/data/{FIXED_BASE_ID}/{table_id}/records"
        is_bulk = isinstance(data, list)
        payload = data
        
        if is_bulk:
            payload = [{"fields": item} if 'fields' not in item else item for item in data]
        elif isinstance(data, dict):
            if 'fields' not in data: payload = {"fields": data}
            
        response = await self._apost(url, data=payload)
        response.raise_for_status()
        res_json = response.json()
        
        # Normalize response
        if isinstance(res_json, dict) and 'records' in res_json:
             records = res_json['records']
             if is_bulk:
                 return records
             elif records:
                 return records[0]
            
        return res_json

    async def get_record(
        self,
        table_id: str,
        record_id: str,
        fields: List[str] = None
    ) -> dict[str, Any]:
        """
        Retrieve a single record by ID.

        Args:
            table_id: The ID of the table.
            record_id: The ID of the record.
            fields: List of specific field names to retrieve.

        Returns:
            dict: The record object.

        Tags:
            read, get, data, records
        """
        url = f"{self.base_url}/api/v3/data/{FIXED_BASE_ID}/{table_id}/records/{record_id}"
        params = {}
        if fields: params["fields"] = ",".join(fields)
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def update_records(
        self,
        table_id: str,
        data: List[dict[str, Any]] | dict[str, Any]
    ) -> dict[str, Any] | List[dict[str, Any]]:
        """
        Update one or more records.

        Args:
            table_id: The ID of the table.
            data: A dictionary or list of dictionaries. NOT containing 'id' or 'Id' key.
                  The 'id' should be part of the object if possible, or handled by logic.

        Returns:
            dict | List: The updated record(s).

        Tags:
            update, data, records
        """
        url = f"{self.base_url}/api/v3/data/{FIXED_BASE_ID}/{table_id}/records"
        def wrap(item):
            rid = item.get("Id") or item.get("id")
            if not rid: raise ValueError("Missing Id/id")
            flds = {k: v for k, v in item.items() if k not in ["Id", "id"]}
            return {"id": rid, "fields": flds}
        
        is_bulk = isinstance(data, list)
        payload = [wrap(i) for i in data] if is_bulk else wrap(data)
        
        response = await self._apatch(url, data=payload)
        response.raise_for_status()
        res_json = response.json()
        
        if is_bulk and isinstance(res_json, dict) and 'records' in res_json:
            return res_json['records']
            
        return res_json

    async def delete_records(
        self,
        table_id: str,
        record_ids: List[dict[str, Any]] | dict[str, Any]
    ) -> dict[str, Any]:
        """
        Delete one or more records.

        Args:
            table_id: The ID of the table.
            record_ids: A list of dicts with 'id', or a single dict with 'id'.

        Returns:
            dict: The deletion result.

        Tags:
            delete, data, records, destructive
        """
        url = f"{self.base_url}/api/v3/data/{FIXED_BASE_ID}/{table_id}/records"
        def wrap(item):
            if isinstance(item, (int, str)): return {"id": item}
            rid = item.get("id") or item.get("Id")
            return {"id": rid}
        
        payload = [wrap(i) for i in record_ids] if isinstance(record_ids, list) else wrap(record_ids)
        if isinstance(record_ids, (int, str)): payload = [{"id": record_ids}]
        
        async with self.get_async_client() as client:
            response = await client.request("DELETE", url, json=payload)
        response.raise_for_status()
        return response.json()

    async def get_record_count(
        self,
        table_id: str,
        view_id: str = None,
        where: str = None
    ) -> dict[str, Any]:
        """
        Get the count of records in a table (or view).

        Args:
            table_id: The ID of the table.
            view_id: Optional View ID to count within.
            where: Optional filter.

        Returns:
            dict: Object containing 'count'.

        Tags:
            read, count, data, records
        """
        url = f"{self.base_url}/api/v3/data/{FIXED_BASE_ID}/{table_id}/count"
        params = {"viewId": view_id, "where": where}
        params = {k: v for k, v in params.items() if v is not None}
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.list_tables,
            self.create_table, 
            self.delete_table,
            self.create_column, 
            self.delete_column,
            self.list_records, 
            self.create_records, 
            self.get_record,
            self.update_records, 
            self.delete_records, 
            self.get_record_count
        ]
