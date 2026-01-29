from collections.abc import Iterable
from typing import Any, Literal
from pyairtable import Api
from pyairtable.api.base import Base
from pyairtable.api.table import Table
from pyairtable.api.types import RecordDeletedDict, RecordDict, RecordId, UpdateRecordDict, UpsertResultDict, WritableFields
from pyairtable.models.schema import FieldSchema, TableSchema, parse_field_schema
from pyairtable.formulas import Formula, to_formula_str
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class AirtableApp(APIApplication):
    """
    A comprehensive interface for interacting with the Airtable API.
    This application allows for the management of bases, tables, records, and fields,
    enabling automation of data entry, retrieval, and schema modifications.
    It requires a configured Airtable integration with a valid API key.
    """

    def __init__(self, integration: Integration | None = None) -> None:
        super().__init__(name="airtable", integration=integration)

    async def get_client(self) -> Api:
        """
        Retrieves an authenticated pyairtable client instance.

        This method validates the integration configuration and extracts the API key
        to initialize the connection to Airtable.

        Returns:
            Api: An initialized pyairtable API client ready for API requests.

        Raises:
            ValueError: If the integration is missing or the API key is not configured.
        """
        if not self.integration:
            raise ValueError("Integration is not set for AirtableApp.")
        credentials = await self.integration.get_credentials_async()
        api_key = credentials.get("api_key") or credentials.get("apiKey") or credentials.get("API_KEY")
        if not api_key:
            raise ValueError("Airtable API key is not configured in the integration.")
        return Api(api_key)

    def _prepare_pyairtable_params(self, collected_options: dict[str, Any]) -> dict[str, Any]:
        """
        Parses and extracts parameters for pyairtable method calls.

        Handles nested 'options' dictionaries commonly received from tool calls,
        flattening the structure to be compatible with pyairtable arguments.

        Args:
            collected_options: The raw dictionary of options passed to the method.

        Returns:
            dict[str, Any]: A dictionary of cleaned arguments ready for pyairtable.
        """
        nested_options = collected_options.get("options")
        if isinstance(nested_options, dict):
            return nested_options
        return collected_options

    async def list_bases(self) -> list[Base] | str:
        """
        Retrieves a list of all Airtable bases accessible to the authenticated user.

        This is useful for discovering available workspaces and bases to interact with.

        Returns:
            list[Base] | str: A list of Base objects containing metadata about each base,
            or an error message string if the request fails.

        Tags:
            list, base, important
        """
        try:
            client = await self.get_client()
            return client.bases()
        except Exception as e:
            return f"Error listing bases: {type(e).__name__} - {e}"

    async def list_tables(self, base_id: str) -> list[Table] | str:
        """
        Retrieves the schema and metadata for all tables in a specific base.

        Args:
            base_id: The unique identifier of the Airtable base (e.g., 'appAbc123').

        Returns:
            list[Table] | str: A list of Table objects representing the tables in the base,
            or an error message string if the request fails.

        Tags:
            list, table, important
        """
        try:
            client = await self.get_client()
            base = client.base(base_id)
            return base.tables()
        except Exception as e:
            return f"Error listing tables for base '{base_id}': {type(e).__name__} - {e}"

    async def get_record(self, base_id: str, table_id_or_name: str, record_id: RecordId, **options: Any) -> RecordDict | str:
        """
        Fetches a specific record's data from a given table and base.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table containing the record.
            record_id: The unique identifier of the record to retrieve (e.g., 'recAbc123').
            **options: Optional parameters to customize the response, such as 'cell_format' or 'user_locale'.
                       Can be passed directly or within a nested 'options' dictionary.

        Returns:
            RecordDict | str: A dictionary containing the record's fields and metadata,
            or an error message string if the retrieval fails.

        Tags:
            get, record, important
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            pyairtable_params = self._prepare_pyairtable_params(options)
            return table.get(record_id, **pyairtable_params)
        except Exception as e:
            return f"Error getting record '{record_id}' from '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def list_records(self, base_id: str, table_id_or_name: str, **options: Any) -> list[RecordDict] | str:
        """
        Retrieves a list of records from a table, optionally filtered or sorted.

        Supports advanced querying features like filtering by formula, sorting, and limiting results.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table to query.
            **options: Query parameters including:
                - view (str): The name or ID of a specific view to fetch records from.
                - max_records (int): The maximum number of records to return.
                - formula (str): An Airtable formula string to filter records.
                - sort (list): A list of fields to sort by.
                - fields (list): A list of specific field names to retrieve.

        Returns:
            list[RecordDict] | str: A list of dictionaries representing the records found,
            or an error message string if the request fails.

        Tags:
            list, record, important
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            pyairtable_params = self._prepare_pyairtable_params(options)
            if "formula" in pyairtable_params and isinstance(pyairtable_params["formula"], Formula):
                pyairtable_params["formula"] = to_formula_str(pyairtable_params["formula"])
            return table.all(**pyairtable_params)
        except Exception as e:
            return f"Error listing records from '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def create_record(self, base_id: str, table_id_or_name: str, fields: WritableFields, **options: Any) -> RecordDict | str:
        """
        Adds a new record to a table with the specified field values.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            fields: A dictionary mapping field names (or IDs) to their values.
            **options: Optional creation parameters:
                - typecast (bool): If True, attempts to convert string values to the appropriate cell type (default: False).
                - use_field_ids (bool): If True, expects 'fields' keys to be field IDs instead of names (default: False).

        Returns:
            RecordDict | str: A dictionary representing the newly created record, including its ID,
            or an error message string if the creation fails.

        Tags:
            create, record, important
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            prepared_options = self._prepare_pyairtable_params(options)
            prepared_options.get("typecast", False)
            prepared_options.get("use_field_ids")
            call_kwargs = {}
            if "typecast" in prepared_options:
                call_kwargs["typecast"] = prepared_options["typecast"]
            if "use_field_ids" in prepared_options:
                call_kwargs["use_field_ids"] = prepared_options["use_field_ids"]
            return table.create(fields=fields, **call_kwargs)
        except Exception as e:
            return f"Error creating record in '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def update_record(
        self, base_id: str, table_id_or_name: str, record_id: RecordId, fields: WritableFields, **options: Any
    ) -> RecordDict | str:
        """
        Modifies specific fields of an existing record.

        This method performs a partial update (PATCH) by default, only changing the fields provided.
        To perform a destructive update (clearing unspecified fields), use the 'replace' option.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            record_id: The unique identifier of the record to update.
            fields: A dictionary of field names (or IDs) and their new values.
            **options: Optional update parameters:
                - replace (bool): If True, performs a destructive update (PUT), clearing fields not included in 'fields'.
                - typecast (bool): If True, performs automatic data conversion.
                - use_field_ids (bool): If True, expects field IDs as keys.

        Returns:
            RecordDict | str: A dictionary representing the updated record,
            or an error message string if the update fails.

        Tags:
            update, record
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            prepared_options = self._prepare_pyairtable_params(options)
            call_kwargs = {}
            if "replace" in prepared_options:
                call_kwargs["replace"] = prepared_options["replace"]
            if "typecast" in prepared_options:
                call_kwargs["typecast"] = prepared_options["typecast"]
            if "use_field_ids" in prepared_options:
                call_kwargs["use_field_ids"] = prepared_options["use_field_ids"]
            return table.update(record_id, fields=fields, **call_kwargs)
        except Exception as e:
            return f"Error updating record '{record_id}' in '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def delete_record(self, base_id: str, table_id_or_name: str, record_id: RecordId) -> RecordDeletedDict | str:
        """
        Permanently removes a record from a table.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            record_id: The unique identifier of the record to delete.

        Returns:
            RecordDeletedDict | str: A dictionary confirming the deletion (e.g., {"deleted": True, "id": "rec..."}),
            or an error message string if the deletion fails.

        Tags:
            delete, record
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            return table.delete(record_id)
        except Exception as e:
            return f"Error deleting record '{record_id}' from '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def batch_create_records(
        self, base_id: str, table_id_or_name: str, records: Iterable[WritableFields], **options: Any
    ) -> list[RecordDict] | str:
        """
        Creates multiple records efficiently in a single batch operation.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            records: An iterable of dictionaries, where each dictionary represents the fields for a new record.
            **options: Optional parameters:
                - typecast (bool): Enable automatic data conversion.
                - use_field_ids (bool): Use field IDs instead of names for keys.

        Returns:
            list[RecordDict] | str: A list of the created record objects,
            or an error message string if the operation fails.

        Tags:
            create, record, batch
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            prepared_options = self._prepare_pyairtable_params(options)
            call_kwargs = {}
            if "typecast" in prepared_options:
                call_kwargs["typecast"] = prepared_options["typecast"]
            if "use_field_ids" in prepared_options:
                call_kwargs["use_field_ids"] = prepared_options["use_field_ids"]
            return table.batch_create(records, **call_kwargs)
        except Exception as e:
            return f"Error batch creating records in '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def batch_update_records(
        self, base_id: str, table_id_or_name: str, records: Iterable[UpdateRecordDict], **options: Any
    ) -> list[RecordDict] | str:
        """
        Updates multiple records efficiently in a single batch operation.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            records: A list of dictionaries. Each must contain an 'id' key (record ID) and a 'fields' key (dict of updates).
            **options: Optional parameters:
                - replace (bool): If True, performs destructive updates for each record.
                - typecast (bool): Enable automatic data conversion.
                - use_field_ids (bool): Use field IDs as keys.

        Returns:
            list[RecordDict] | str: A list of the updated record objects,
            or an error message string if the operation fails.

        Tags:
            update, record, batch
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            prepared_options = self._prepare_pyairtable_params(options)
            call_kwargs = {}
            if "replace" in prepared_options:
                call_kwargs["replace"] = prepared_options["replace"]
            if "typecast" in prepared_options:
                call_kwargs["typecast"] = prepared_options["typecast"]
            if "use_field_ids" in prepared_options:
                call_kwargs["use_field_ids"] = prepared_options["use_field_ids"]
            return table.batch_update(records, **call_kwargs)
        except Exception as e:
            return f"Error batch updating records in '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def batch_delete_records(
        self, base_id: str, table_id_or_name: str, record_ids: Iterable[RecordId]
    ) -> list[RecordDeletedDict] | str:
        """
        Permanently removes multiple records in a single batch operation.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            record_ids: A list of record IDs to be deleted.

        Returns:
            list[RecordDeletedDict] | str: A list of dictionaries confirming the deletion of each record,
            or an error message string if the operation fails.

        Tags:
            delete, record, batch
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            return table.batch_delete(record_ids)
        except Exception as e:
            return f"Error batch deleting records from '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def batch_upsert_records(
        self, base_id: str, table_id_or_name: str, records: Iterable[dict[str, Any]], key_fields: list[str], **options: Any
    ) -> UpsertResultDict | str:
        """
        Performs a batch upsert (update or insert) operation.

        This method attempts to update existing records or create new ones based on matching criteria.
        Records are matched by their 'id' (if provided) or by a set of specified 'key_fields'.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            records: A list of dictionaries representing records.
            key_fields: A list of field names (or IDs) used to identify unique records for matching.
            **options: Optional parameters:
                - replace (bool): If True, performs destructive updates.
                - typecast (bool): Enable automatic data conversion.
                - use_field_ids (bool): Use field IDs as keys.

        Returns:
            UpsertResultDict | str: A result object containing lists of created and updated record IDs and the modified records,
            or an error message string if the operation fails.

        Tags:
            create, update, record, batch, upsert
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            prepared_options = self._prepare_pyairtable_params(options)
            call_kwargs = {}
            if "replace" in prepared_options:
                call_kwargs["replace"] = prepared_options["replace"]
            if "typecast" in prepared_options:
                call_kwargs["typecast"] = prepared_options["typecast"]
            if "use_field_ids" in prepared_options:
                call_kwargs["use_field_ids"] = prepared_options["use_field_ids"]
            return table.batch_upsert(records, key_fields=key_fields, **call_kwargs)
        except Exception as e:
            return f"Error batch upserting records in '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    async def create_table(
        self, base_id: str, name: str, fields: list[dict[str, Any]], description: str | None = None
    ) -> TableSchema | str:
        """
        Adds a new table to an existing base with a defined schema.

        Args:
            base_id: The unique identifier of the Airtable base.
            name: The display name for the new table.
            fields: A list of field definitions. Each field is a dictionary with 'name' and 'type' keys,
                    and optionally 'options' or 'description'.
            description: An optional text description for the table.

        Returns:
            TableSchema | str: Such as schema object for the newly created table,
            or an error message string if the creation fails.

        Tags:
            create, table
        """
        try:
            client = await self.get_client()
            base = client.base(base_id)
            return base.create_table(name, fields, description)
        except Exception as e:
            return f"Error creating table '{name}' in base '{base_id}': {type(e).__name__} - {e}"

    async def update_table(
        self, base_id: str, table_id_or_name: str, name: str | None = None, description: str | None = None
    ) -> TableSchema | str:
        """
        Modifies metadata (name or description) of an existing table.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table to update.
            name: The new name for the table (optional).
            description: The new description for the table (optional).

        Returns:
            TableSchema | str: The updated table schema object,
            or an error message string if the update fails.

        Tags:
            update, table
        """
        try:
            client = await self.get_client()
            # We need the table ID for the meta API call
            base = client.base(base_id)
            table_obj = base.table(table_id_or_name)
            table_id = table_obj.id

            url = base.urls.tables / table_id
            payload = {}
            if name:
                payload["name"] = name
            if description:
                payload["description"] = description
            
            if not payload:
                 return "Error: No update parameters (name or description) provided."

            response = client.request("PATCH", url, json=payload)
            # Fetch the updated schema to return a TableSchema object
            # Ideally we'd parse the response directly if it matches, but getting a fresh schema is safer
            # The response from PATCH /meta/bases/{baseId}/tables/{tableId} returns the table schema
            # We can try to parse it using TableSchema.from_api but we need the context.
            # Simpler approach for now is to just re-fetch or construct it if we had a helper.
            # Let's inspect what create_table returns - it returns a Table object which has .schema().
            # Let's try to return the schema from the response.
            from pyairtable.models.schema import TableSchema
            return TableSchema.parse_obj(response)
        except Exception as e:
            return f"Error updating table '{table_id_or_name}' in base '{base_id}': {type(e).__name__} - {e}"

    async def create_field(
        self,
        base_id: str,
        table_id_or_name: str,
        name: str,
        field_type: Literal[
            "singleLineText",
            "number",
            "date",
            "dateTime",
            "singleSelect",
            "multipleSelects",
            "currency",
            "url",
            "checkbox",
        ],
        options: dict[str, Any] | None = None,
        description: str | None = None,
    ) -> FieldSchema | str:
        """
        Adds a new field (column) to a table.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            name: The name of the new field.
            field_type: The data type of the field (e.g., 'singleLineText', 'number', 'singleSelect').
            options: A dictionary of configuration options specific to the chosen field_type (e.g., choices for valid selects).
            description: An optional text description for the field.

        Returns:
            FieldSchema | str: The schema definition of the created field,
            or an error message string if the creation fails.

        Tags:
            create, field
        """
        try:
            client = await self.get_client()
            table = client.table(base_id, table_id_or_name)
            return table.create_field(name, field_type, description, options)
        except Exception as e:
            return f"Error creating field '{name}' in table '{table_id_or_name}': {type(e).__name__} - {e}"

    async def update_field(
        self,
        base_id: str,
        table_id_or_name: str,
        field_id: str,
        name: str | None = None,
        field_type: Literal[
            "singleLineText",
            "number",
            "date",
            "dateTime",
            "singleSelect",
            "multipleSelects",
            "currency",
            "url",
            "checkbox",
        ]
        | None = None,
        description: str | None = None,
        options: dict[str, Any] | None = None,
    ) -> FieldSchema | str:
        """
        Modifies the properties of an existing field.

        Allows changing the field's name, description, type, or specific options.

        Args:
            base_id: The unique identifier of the Airtable base.
            table_id_or_name: The name or ID of the table.
            field_id: The unique identifier of the field to update.
            name: The new name for the field.
            field_type: The new data type for the field.
            description: The new description for the field.
            options: The new configuration options for the field.

        Returns:
            FieldSchema | str: The updated field schema object,
            or an error message string if the update fails.

        Tags:
            update, field
        """
        try:
            client = await self.get_client()
            base = client.base(base_id)
            # We need the table ID for the URL construction if table_id_or_name is a name
            table_obj = base.table(table_id_or_name)
            table_id = table_obj.id

            # Construct URL: https://api.airtable.com/v0/meta/bases/{baseId}/tables/{tableId}/fields/{fieldId}
            # We can use base.urls.tables which gives .../tables
            url = base.urls.tables / table_id / "fields" / field_id

            payload = {}
            if name:
                payload["name"] = name
            if field_type:
                payload["type"] = field_type
            if description:
                payload["description"] = description
            if options:
                payload["options"] = options

            if not payload:
                return "Error: No update parameters (name, field_type, description, or options) provided."

            response = client.request("PATCH", url, json=payload)
            return parse_field_schema(response)

        except Exception as e:
            return f"Error updating field '{field_id}' in table '{table_id_or_name}': {type(e).__name__} - {e}"



    def list_tools(self):
        """Returns a list of methods exposed as tools."""
        return [
            self.list_bases,
            self.list_tables,
            self.get_record,
            self.list_records,
            self.create_record,
            self.update_record,
            self.delete_record,
            self.batch_create_records,
            self.batch_update_records,
            self.batch_delete_records,
            self.batch_upsert_records,
            self.create_table,
            self.update_table,
            self.create_field,
            self.update_field,
        ]
