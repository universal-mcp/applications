# PostgreSQL MCP Server

An MCP Server for PostgreSQL databases with read-only safety features, schema introspection, and performance analysis tools.

## 🛠️ Tool List

Tools for interacting with PostgreSQL databases with built-in safety features and read-only mode by default.


| Tool | Description |
|------|-------------|
| `execute_sql` | Execute SQL queries with safety validation and configurable timeout. Supports read-only mode (default) to prevent destructive operations like DROP, DELETE, UPDATE, INSERT, etc. |
| `list_schemas` | List all database schemas with their types (system vs user schemas). Returns schema names, owners, and classification. |
| `list_tables` | List all tables in a specified schema. Simple wrapper around list_objects for convenience. |
| `list_objects` | List database objects (tables, views, sequences, or extensions) in a specified schema with detailed information. |
| `describe_table` | Get detailed table structure including column names, data types, nullability, defaults, and constraints. Returns complete schema information for a table. |
| `list_indexes` | List all indexes for a specific table including index definitions, uniqueness, primary key status, and validity. |
| `explain_query` | Get the PostgreSQL query execution plan in various formats (TEXT, JSON, XML, YAML). Useful for query optimization and performance analysis. |
| `check_health` | Check database connection health including version, connection count, database size, and overall status. |
| `get_database_size_info` | Get overall database size information and list the largest tables by size including their table and index sizes. |
