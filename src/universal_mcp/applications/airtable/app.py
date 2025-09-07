from collections.abc import Iterable
from typing import Any

# Import necessary components from pyairtable
from pyairtable import Api
from pyairtable.api.base import Base
from pyairtable.api.table import Table
from pyairtable.api.types import (
    RecordDeletedDict,
    RecordDict,
    RecordId,
    UpdateRecordDict,
    UpsertResultDict,
    WritableFields,
)
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

    def _get_client(self) -> Api:
        """Initializes and returns the pyairtable client after ensuring API key is set."""
        if not self.integration:
            raise ValueError("Integration is not set for AirtableApp.")
        credentials = self.integration.get_credentials()
        api_key = (
            credentials.get("api_key")
            or credentials.get("apiKey")
            or credentials.get("API_KEY")
        )
        if not api_key:
            raise ValueError("Airtable API key is not configured in the integration.")
        return Api(api_key)

    def _prepare_pyairtable_params(
        self, collected_options: dict[str, Any]
    ) -> dict[str, Any]:
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

    def list_bases(self) -> list[Base] | str:
        """
        Lists all bases accessible with the current API key.

        Returns:
            A list of pyairtable.api.base.Base objects on success,
            or a string containing an error message on failure.

        Tags:
            list, base, important
        """
        try:
            client = self._get_client()
            return client.bases()
        except Exception as e:
            return f"Error listing bases: {type(e).__name__} - {e}"

    def list_tables(self, base_id: str) -> list[Table] | str:
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
            client = self._get_client()
            base = client.base(base_id)
            return base.tables()
        except Exception as e:
            return (
                f"Error listing tables for base '{base_id}': {type(e).__name__} - {e}"
            )

    def get_record(
        self, base_id: str, table_id_or_name: str, record_id: RecordId, **options: Any
    ) -> RecordDict | str:
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            pyairtable_params = self._prepare_pyairtable_params(options)
            return table.get(record_id, **pyairtable_params)
        except Exception as e:
            return f"Error getting record '{record_id}' from '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    def list_records(
        self, base_id: str, table_id_or_name: str, **options: Any
    ) -> list[RecordDict] | str:
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            pyairtable_params = self._prepare_pyairtable_params(options)

            # Convert Formula object to string if provided, after preparing params
            if "formula" in pyairtable_params and isinstance(
                pyairtable_params["formula"], Formula
            ):
                pyairtable_params["formula"] = to_formula_str(
                    pyairtable_params["formula"]
                )

            return table.all(**pyairtable_params)
        except Exception as e:
            return f"Error listing records from '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    def create_record(
        self,
        base_id: str,
        table_id_or_name: str,
        fields: WritableFields,
        **options: Any,  # Captures typecast, use_field_ids etc.
    ) -> RecordDict | str:
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            # pyairtable's Table.create() takes typecast and use_field_ids as named args,
            # not as **kwargs. We need to extract them or use defaults.

            prepared_options = self._prepare_pyairtable_params(options)
            prepared_options.get("typecast", False)
            prepared_options.get(
                "use_field_ids"
            )  # Let pyairtable handle default if None

            # Ensure only valid kwargs for pyairtable's `create` are passed if it doesn't use **kwargs for these
            # For pyairtable.Table.create, it only takes `typecast` and `use_field_ids` as specific keyword args.
            # The `**options` in `AirtableApp` could collect other things if the tool call sends them.
            # The `pyairtable.Table.create` signature is:
            # create(self, fields: WritableFields, typecast: bool = False, use_field_ids: Optional[bool] = None)
            # It does NOT take a general **kwargs.

            # So, we must call it with the specific parameters.
            # `_prepare_pyairtable_params` helps if "options" is nested, but we still need to map.

            call_kwargs = {}
            if "typecast" in prepared_options:
                call_kwargs["typecast"] = prepared_options["typecast"]
            if (
                "use_field_ids" in prepared_options
            ):  # Pass it only if explicitly provided
                call_kwargs["use_field_ids"] = prepared_options["use_field_ids"]

            return table.create(fields=fields, **call_kwargs)
        except Exception as e:
            return f"Error creating record in '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    def update_record(
        self,
        base_id: str,
        table_id_or_name: str,
        record_id: RecordId,
        fields: WritableFields,
        **options: Any,  # Captures replace, typecast, use_field_ids etc.
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            # pyairtable.Table.update() signature:
            # update(self, record_id: RecordId, fields: WritableFields, replace: bool = False,
            #        typecast: bool = False, use_field_ids: Optional[bool] = None)
            # It does NOT take a general **kwargs.

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

    def delete_record(
        self, base_id: str, table_id_or_name: str, record_id: RecordId
    ) -> RecordDeletedDict | str:
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            return table.delete(record_id)
        except Exception as e:
            return f"Error deleting record '{record_id}' from '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    def batch_create_records(
        self,
        base_id: str,
        table_id_or_name: str,
        records: Iterable[WritableFields],
        **options: Any,  # Captures typecast, use_field_ids etc.
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            # pyairtable.Table.batch_create() signature:
            # batch_create(self, records: Iterable[WritableFields], typecast: bool = False, use_field_ids: Optional[bool] = None)
            # It does NOT take a general **kwargs.

            prepared_options = self._prepare_pyairtable_params(options)
            call_kwargs = {}
            if "typecast" in prepared_options:
                call_kwargs["typecast"] = prepared_options["typecast"]
            if "use_field_ids" in prepared_options:
                call_kwargs["use_field_ids"] = prepared_options["use_field_ids"]

            return table.batch_create(records, **call_kwargs)
        except Exception as e:
            return f"Error batch creating records in '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    def batch_update_records(
        self,
        base_id: str,
        table_id_or_name: str,
        records: Iterable[UpdateRecordDict],
        **options: Any,  # Captures replace, typecast, use_field_ids etc.
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            # pyairtable.Table.batch_update() signature:
            # batch_update(self, records: Iterable[UpdateRecordDict], replace: bool = False,
            #              typecast: bool = False, use_field_ids: Optional[bool] = None)
            # It does NOT take a general **kwargs.

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

    def batch_delete_records(
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            return table.batch_delete(record_ids)
        except Exception as e:
            return f"Error batch deleting records from '{table_id_or_name}' in '{base_id}': {type(e).__name__} - {e}"

    def batch_upsert_records(
        self,
        base_id: str,
        table_id_or_name: str,
        records: Iterable[
            dict[str, Any]
        ],  # pyairtable expects Dict, not UpdateRecordDict here
        key_fields: list[str],
        **options: Any,  # Captures replace, typecast, use_field_ids etc.
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
            client = self._get_client()
            table = client.table(base_id, table_id_or_name)
            # pyairtable.Table.batch_upsert() signature:
            # batch_upsert(self, records: Iterable[Dict[str, Any]], key_fields: List[FieldName],
            #              replace: bool = False, typecast: bool = False, use_field_ids: Optional[bool] = None)
            # It does NOT take a general **kwargs.

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
        ]
