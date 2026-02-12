# RuzodbApp MCP Server

An MCP Server for the RuzodbApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the RuzodbApp API.


| Tool | Description |
|------|-------------|
| `getTablesList` | List tables accessible by user. |
| `getTableSchema` | Get the table schema including fields and views information. |
| `createTable` | Create a new table in a specific base with optional initial columns, description and metadata. |
| `deleteTable` | Delete a table by its ID from a specific base. |
| `createColumn` | Create a new column (field) in an existing table. |
| `deleteColumn` | Delete a column (field) by its ID. |
| `queryRecords` | List records from a table with pagination and specific filtering using `(Col,Operator,Value)` syntax. |
| `createRecords` | Create records in a table. |
| `getRecord` | Fetch a record by ID. |
| `updateRecords` | Update records in a table. |
| `deleteRecords` | Delete records in a table. |
| `countRecords` | Count Records in a Table. |
| `aggregateRecords` | Perform aggregations on a table with a filter condition. This allows you to compute summary statistics across your data. |
| `findDuplicates` | Check a list of values against a specific column and return those that already exist along with their Record ID. |
