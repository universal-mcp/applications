from collections.abc import Iterable
from typing import Any, Literal
from pyairtable import Api
from pyairtable.api.base import Base
from pyairtable.api.table import Table
from pyairtable.api.types import RecordDeletedDict, RecordDict, RecordId, UpdateRecordDict, UpsertResultDict, WritableFields
from pyairtable.models.schema import FieldSchema, TableSchema
from pyairtable.formulas import Formula, to_formula_str
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class AirtableApp(APIApplication):
    """
    Application for interacting with the Airtable API to manage bases, tables,
    and records. Requires an Airtable API key configured via integration.
    """

    def __init__(self, integration: Integration | None = None) -> None:
        super().__init__(name="airtable", integration=integration)

    async def get_client(self) -> Api:
        """Initializes and returns the pyairtable client after ensuring API key is set."""
        if not self.integration:
            raise ValueError("Integration is not set for AirtableApp.")
        credentials = await self.integration.get_credentials_async()
        api_key = credentials.get("api_key") or credentials.get("apiKey") or credentials.get("API_KEY")
        if not api_key:
            raise ValueError("Airtable API key is not configured in the integration.")
        return Api(api_key)

    def _prepare_pyairtable_params(self, collected_options: dict[str, Any]) -> dict[str, Any]:
        """
        Extracts the actual parameters for pyairtable from the collected options.
        If `collected_options` contains a key "options" whose value is a dictionary
        (as might come from a JSON tool call), that nested dictionary is used.
        Otherwise, `collected_options` itself is assumed to contain the direct parameters.
        """
        nested_options = collected_options.get("options")
        if isinstance(nested_options, dict):
            return nested_options
        return collected_options

    async def list_bases(self) -> list[Base] | str:
        """
        Lists all bases accessible with the current API key.

        Returns:
            A list of pyairtable.api.base.Base objects on success,
            or a string containing an error message on failure.

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
        Lists all tables within a specified base.

        Args:
            base_id: The ID of the base.

        Returns:
            A list of pyairtable.api.table.Table objects on success,
            or a string containing an error message on failure.

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
        Retrieves a single record by its ID from a specified table within a base.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            record_id: The ID of the record to retrieve.
            **options: Additional options for retrieving the record (e.g., cell_format, user_locale).
                       If these are passed within a nested "options" dict from a tool call,
                       they will be extracted.

        Returns:
            A dictionary representing the record on success,
            or a string containing an error message on failure.

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
        Lists records from a specified table within a base.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            **options: Additional options for listing records (e.g., view, max_records, formula, sort).
                       Formula can be a string or a pyairtable.formulas.Formula object.
                       If these are passed within a nested "options" dict from a tool call,
                       they will be extracted.

        Returns:
            A list of dictionaries, where each dictionary represents a record, on success,
            or a string containing an error message on failure.

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
        Creates a new record in a specified table within a base.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            fields: A dictionary where keys are field names/IDs and values are the field data.
            **options: Additional options for creating the record (e.g., typecast, use_field_ids).
                       If these are passed within a nested "options" dict from a tool call,
                       they will be extracted.

        Returns:
            A dictionary representing the newly created record on success,
            or a string containing an error message on failure.

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
        Updates an existing record in a specified table within a base.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            record_id: The ID of the record to update.
            fields: A dictionary where keys are field names/IDs and values are the field data to update.
            **options: Additional options for updating the record (e.g., replace, typecast, use_field_ids).
                       If these are passed within a nested "options" dict from a tool call,
                       they will be extracted.

        Returns:
            A dictionary representing the updated record on success,
            or a string containing an error message on failure.

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
        Deletes a record from a specified table within a base.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            record_id: The ID of the record to delete.

        Returns:
            A dictionary confirming the deletion on success,
            or a string containing an error message on failure.

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
        Creates multiple records in batches in a specified table.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            records: An iterable of dictionaries, where each dictionary contains the fields for a new record.
            **options: Additional options for creating records (e.g., typecast, use_field_ids).
                       If these are passed within a nested "options" dict from a tool call,
                       they will be extracted.

        Returns:
            A list of dictionaries representing the newly created records on success,
            or a string containing an error message on failure.

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
        Updates multiple records in batches in a specified table.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            records: An iterable of dictionaries, where each dictionary must contain 'id' and 'fields' for the record to update.
            **options: Additional options for updating records (e.g., replace, typecast, use_field_ids).
                       If these are passed within a nested "options" dict from a tool call,
                       they will be extracted.

        Returns:
            A list of dictionaries representing the updated records on success,
            or a string containing an error message on failure.

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
        Deletes multiple records in batches from a specified table.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            record_ids: An iterable of record IDs to delete.

        Returns:
            A list of dictionaries confirming the deletion status for each record on success,
            or a string containing an error message on failure.

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
        Updates or creates records in batches in a specified table.

        Records are matched by 'id' if provided, or by 'key_fields'.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            records: An iterable of dictionaries, where each dictionary contains either
                     'id' and 'fields' for existing records, or just 'fields' for new records.
            key_fields: A list of field names/IDs used to match records if 'id' is not provided.
            **options: Additional options for upserting records (e.g., replace, typecast, use_field_ids).
                       If these are passed within a nested "options" dict from a tool call,
                       they will be extracted.

        Returns:
            A dictionary containing lists of created/updated record IDs and the affected records on success,
            or a string containing an error message on failure.

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
        Creates a new table in the specified base.

        Args:
            base_id: The ID of the base.
            name: The name of the new table.
            fields: A list of field definitions (dictionaries). Each dict must have a 'name' and 'type'.
            description: An optional description for the table.

        Returns:
            A TableSchema object representing the created table on success,
            or a string containing an error message on failure.

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
        Updates an existing table's name and/or description.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table to update.
            name: The new name for the table (optional).
            description: The new description for the table (optional).

        Returns:
            A TableSchema object representing the updated table on success,
            or a string containing an error message on failure.

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
        Creates a new field in the specified table.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            name: The name of the new field.
            field_type: The type of the field. allowed values: "singleLineText", "number", "date", "dateTime", "singleSelect", "multipleSelects", "currency", "url", "checkbox".
            options: Specific options for the field type (optional).
            description: A description for the field (optional).

        Returns:
            A FieldSchema object representing the created field on success,
            or a string containing an error message on failure.

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
        Updates an existing field's name, description, and/or options.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            field_id: The ID of the field to update.
            name: The new name for the field (optional).
            field_type: The new type for the field. allowed values: "singleLineText", "number", "date", "dateTime", "singleSelect", "multipleSelects", "currency", "url", "checkbox".
            description: The new description for the field (optional).
            options: The new options for the field (optional).

        Returns:
            A FieldSchema object representing the updated field on success,
            or a string containing an error message on failure.

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
            from pyairtable.models.schema import FieldSchema

            return FieldSchema.parse_obj(response)

        except Exception as e:
            return f"Error updating field '{field_id}' in table '{table_id_or_name}': {type(e).__name__} - {e}"

    async def delete_table(self, base_id: str, table_id_or_name: str) -> str:
        """
        Deletes a table from the specified base.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table to delete.

        Returns:
            A string confirming the deletion on success,
            or a string containing an error message on failure.

        Tags:
            delete, table
        """
        try:
            client = await self.get_client()
            base = client.base(base_id)
            table_obj = base.table(table_id_or_name)
            table_id = table_obj.id

            # URL: /meta/bases/{baseId}/tables/{tableId}
            url = base.urls.tables / table_id
            
            client.request("DELETE", url)
            return f"Table '{table_id_or_name}' (ID: {table_id}) deleted successfully."
        except Exception as e:
            return f"Error deleting table '{table_id_or_name}' in base '{base_id}': {type(e).__name__} - {e}"

    async def delete_field(
        self, base_id: str, table_id_or_name: str, field_id: str
    ) -> str:
        """
        Deletes a field from the specified table.

        Args:
            base_id: The ID of the base.
            table_id_or_name: The ID or name of the table.
            field_id: The ID of the field to delete.

        Returns:
            A string confirming the deletion on success,
            or a string containing an error message on failure.

        Tags:
            delete, field
        """
        try:
            client = await self.get_client()
            base = client.base(base_id)
            table_obj = base.table(table_id_or_name)
            table_id = table_obj.id

            # URL: /meta/bases/{baseId}/tables/{tableId}/fields/{fieldId}
            url = base.urls.tables / table_id / "fields" / field_id
            
            client.request("DELETE", url)
            return f"Field '{field_id}' deleted successfully from table '{table_id_or_name}'."
        except Exception as e:
            return f"Error deleting field '{field_id}' in table '{table_id_or_name}': {type(e).__name__} - {e}"

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
            self.delete_table,
            self.delete_field,
        ]
