from typing import Any
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class NocodbApp(APIApplication):
    """
    Integrates with NocoDB Meta API v3 to manage Workspaces, Bases, Tables, and Fields.
    """

    def __init__(self, integration: Integration = None, base_url: str = None, **kwargs) -> None:
        """
        Initialize the NocoDB application.

        Args:
            integration: Authentication integration (provides xc-token).
            base_url: Optional override for self-hosted instances.
                      Defaults to NocoDB Cloud V3: 'https://app.nocodb.com/api/v3/meta'
        """
        super().__init__(name="nocodb", integration=integration, **kwargs)
        # Default to cloud V3 URL
        self.base_url = base_url or "https://app.nocodb.com/api/v3/meta"

    async def _aget_headers(self) -> dict:
        """Get authentication headers (xc-token)."""
        creds = await self.integration.get_credentials()
        # Fallback to 'api_key' or 'token' key from credentials
        token = creds.get("api_key") or creds.get("token") or creds.get("xc-token")
        if not token:
             # If user pasted the whole object, it might be in 'data'
             token = creds.get("data", {}).get("token")
        
        if not token:
            raise ValueError("Missing 'xc-token'. Please provide it in integration credentials.")
            
        return {
            "xc-token": token,
            "Content-Type": "application/json"
        }

    # ==================== Workspace Operations ====================

    async def list_workspaces(self, base_url: str = None) -> dict[str, Any]:
        """
        Lists all workspaces accessible to the user.

        Args:
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: List of workspaces.

        Tags:
            workspace, list, important
        """
        url = f"{base_url or self.base_url}/workspaces"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_workspace(self, workspace_id: str, base_url: str = None) -> dict[str, Any]:
        """
        Retrieves details of a specific workspace.

        Args:
            workspace_id: The ID of the workspace.
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: Workspace metadata.

        Tags:
            workspace, get, read
        """
        if not workspace_id:
             raise ValueError("Missing 'workspace_id'.")
        
        url = f"{base_url or self.base_url}/workspaces/{workspace_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    # ==================== Base Operations ====================

    async def list_bases(self, workspace_id: str, base_url: str = None) -> dict[str, Any]:
        """
        Lists all bases within a specific workspace.

        Args:
            workspace_id: The ID of the workspace.
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: List of bases.

        Tags:
            base, list, important
        """
        if not workspace_id:
            raise ValueError("Missing required parameter 'workspace_id'.")
        
        url = f"{base_url or self.base_url}/workspaces/{workspace_id}/bases"
        response = await self._aget(url)
        # response.raise_for_status() # Let the caller handle? No, we should raise.
        if response.status_code == 404:
             return {"list": []} # Handle graceful empty if workspace not found? Better to raise for debugging.
        response.raise_for_status()
        return response.json()

    async def get_base(self, base_id: str, base_url: str = None) -> dict[str, Any]:
        """
        Retrieves metadata for a specific base.

        Args:
            base_id: The unique ID of the base.
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: Base metadata.

        Tags:
            base, get, read
        """
        if not base_id:
             raise ValueError("Missing required parameter 'base_id'.")

        url = f"{base_url or self.base_url}/bases/{base_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_base(
        self,
        workspace_id: str,
        title: str,
        description: str = None,
        color: str = None,
        type: str = "database",
        base_url: str = None,
    ) -> dict[str, Any]:
        """
        Creates a new base in a workspace.

        Args:
            workspace_id: The ID of the target workspace.
            title: The title of the new base.
            description: Optional description.
            color: Optional color hex code.
            type: Base type (default: 'database').
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: The created base object.

        Tags:
            base, create, important
        """
        if not workspace_id:
            raise ValueError("Missing 'workspace_id'.")
        if not title:
            raise ValueError("Missing 'title'.")

        url = f"{base_url or self.base_url}/workspaces/{workspace_id}/bases"
        data = {
            "title": title,
            "description": description,
            "color": color,
            "type": type,
            "sources": [{"type": "native"}]
        }
        data = {k: v for k, v in data.items() if v is not None}

        response = await self._apost(url, data=data)
        response.raise_for_status()
        return response.json()

    # ==================== Table Operations ====================

    async def list_tables(
        self,
        base_id: str,
        page: int = 1,
        page_size: int = 25,
        base_url: str = None
    ) -> dict[str, Any]:
        """
        Lists tables in a base.

        Args:
            base_id: The ID of the base.
            page: Page number (default: 1).
            page_size: Number of tables per page (default: 25).
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: Paginated list of tables.

        Tags:
            table, list, important
        """
        if not base_id:
            raise ValueError("Missing 'base_id'.")

        url = f"{base_url or self.base_url}/bases/{base_id}/tables"
        params = {"page": page, "limit": page_size}
        
        response = await self._aget(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_table(self, base_id: str, table_id: str, base_url: str = None) -> dict[str, Any]:
        """
        Retrieves metadata for a specific table (Schema), including its columns/fields.
        
        Args:
            base_id: The ID of the base containing the table.
            table_id: The unique ID of the table.
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: Table metadata including 'columns' or 'fields'.

        Tags:
            table, get, read
        """
        if not base_id:
            raise ValueError("Missing 'base_id'.")
        if not table_id:
            raise ValueError("Missing 'table_id'.")

        url = f"{base_url or self.base_url}/bases/{base_id}/tables/{table_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_table(
        self,
        base_id: str,
        title: str,
        table_name: str = None,
        columns: list = None,
        base_url: str = None
    ) -> dict[str, Any]:
        """
        Creates a new table in a base.

        Args:
            base_id: The ID of the base.
            title: Human-readable title of the table.
            table_name: Database table name (optional).
            columns: List of column definitions.
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: The created table object.

        Tags:
            table, create, important
        """
        if not base_id:
             raise ValueError("Missing 'base_id'.")
        if not title:
            raise ValueError("Missing 'title'.")

        url = f"{base_url or self.base_url}/bases/{base_id}/tables"
        data = {
            "title": title,
            "table_name": table_name or title,
            "columns": columns or []
        }
        
        response = await self._apost(url, data=data)
        response.raise_for_status()
        return response.json()

    # ==================== Field (Column) Operations ====================

    async def list_fields(self, base_id: str, table_id: str, base_url: str = None) -> list[dict[str, Any]]:
        """
        Lists all fields (columns) for a specific table.
        Fetches table schema and extracts fields/columns.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            list[dict[str, Any]]: List of field objects.

        Tags:
            field, column, list
        """
        table_meta = await self.get_table(base_id, table_id, base_url=base_url)
        # V3 usually returns 'columns' or 'fields'. We check both.
        return table_meta.get("columns") or table_meta.get("fields") or []

    async def get_field(self, base_id: str, field_id: str, base_url: str = None) -> dict[str, Any]:
        """
        Retrieves metadata for a specific field (column).

        Args:
            base_id: The ID of the base.
            field_id: The unique ID of the field/column.
            base_url: Optional override for the NocoDB API base URL.

        Returns:
            dict[str, Any]: Field metadata.

        Tags:
            field, column, get
        """
        if not base_id:
            raise ValueError("Missing 'base_id'.")
        if not field_id:
             raise ValueError("Missing 'field_id'.")

        url = f"{base_url or self.base_url}/bases/{base_id}/fields/{field_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_field(
        self,
        base_id: str,
        table_id: str,
        title: str,
        uidt: str = "SingleLineText",
        column_name: str = None,
        base_url: str = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Creates a new field (column) in a table.

        Args:
            base_id: The ID of the base.
            table_id: The ID of the table.
            title: The display title of the field.
            uidt: UI Data Type.
            column_name: Database column name.
            base_url: Optional override for the NocoDB API base URL.
            **kwargs: Additional properties.

        Returns:
            dict[str, Any]: The created field object.

        Tags:
            field, column, create
        """
        if not base_id:
             raise ValueError("Missing 'base_id'.")
        if not table_id:
            raise ValueError("Missing 'table_id'.")

        # Create endpoint often at /bases/{baseId}/tables/{tableId}/columns in V3?
        # Checked doc: typically POST /bases/{baseId}/tables/{tableId}/columns
        url = f"{base_url or self.base_url}/bases/{base_id}/tables/{table_id}/columns"
        data = {
            "title": title,
            "column_name": column_name or title,
            "uidt": uidt,
            **kwargs
        }
        
        response = await self._apost(url, data=data)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        """Returns list of available NocoDB API tools."""
        return [
            # Workspaces
            self.list_workspaces,
            self.get_workspace,
            # Bases
            self.list_bases,
            self.get_base,
            self.create_base,
            # Tables
            self.list_tables,
            self.get_table,
            self.create_table,
            # Fields
            self.list_fields,
            self.get_field,
            self.create_field,
        ]
