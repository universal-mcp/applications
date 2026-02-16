---
name: airtable
description: A comprehensive interface for interacting with the Airtable API. This application allows for the management of bases, tables, records, and fields, enabling automation of data entry, retrieval, and schema modifications. It requires a configured Airtable integration with a valid API key.
---

# Airtable Integration

A comprehensive interface for interacting with the Airtable API. This application allows for the management of bases, tables, records, and fields, enabling automation of data entry, retrieval, and schema modifications. It requires a configured Airtable integration with a valid API key.

## Available Tools

| Tool | Description |
|------|-------------|
| `list_bases` | Retrieves a list of all Airtable bases accessible to the authenticated user. |
| `list_tables` | Retrieves the schema and metadata for all tables in a specific base. |
| `get_record` | Fetches a specific record's data from a given table and base. |
| `list_records` | Retrieves a list of records from a table, optionally filtered or sorted. |
| `create_record` | Adds a new record to a table with the specified field values. |
| `update_record` | Modifies specific fields of an existing record. |
| `delete_record` | Permanently removes a record from a table. |
| `batch_create_records` | Creates multiple records efficiently in a single batch operation. |
| `batch_update_records` | Updates multiple records efficiently in a single batch operation. |
| `batch_delete_records` | Permanently removes multiple records in a single batch operation. |
| `batch_upsert_records` | Performs a batch upsert (update or insert) operation. |
| `create_table` | Adds a new table to an existing base with a defined schema. |
| `update_table` | Modifies metadata (name or description) of an existing table. |
| `create_field` | Adds a new field (column) to a table. |
| `update_field` | Modifies the properties of an existing field. |
