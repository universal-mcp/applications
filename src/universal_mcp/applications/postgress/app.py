import re
from typing import Annotated, Any, Dict

import psycopg
from psycopg.rows import dict_row

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class PostgresApp(APIApplication):
    """
    Application for interacting with PostgreSQL databases.
    Provides tools for SQL execution, schema introspection, and database management.
    Supports both read-only and read-write operations with safety features.
    """

    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="postgres", integration=integration, **kwargs)
        self._connection = None
        self._read_only_mode = True
        self._connection_string = None
        
        

    @property
    def connection_string(self) -> str:
        """Get the PostgreSQL connection string from integration credentials."""
        if self._connection_string:
            return self._connection_string
            
        if not self.integration:
            raise ValueError("Integration is required but not provided")
            
        credentials = self.integration.get_credentials()
        conn_str = credentials.get("connection_string")
        
        if not conn_str:
            raise ValueError(
                "PostgreSQL connection URL is required."
            )
            
        self._connection_string = conn_str
        return conn_str

    @property
    def connection(self) -> Any:
        """Get or create a PostgreSQL connection using lazy initialization."""
        if self._connection is not None and not self._connection.closed:
            return self._connection
            
        
            
        try:
            self._connection = psycopg.connect(
                self.connection_string,
                row_factory=dict_row  # type: ignore
            )
            return self._connection
        except Exception as e:
            raise

    def _validate_sql_safety(self, sql_query: str) -> bool:
        """Validate SQL query for safety in read-only mode."""
        if not self._read_only_mode:
            return True
            
        query_upper = sql_query.upper().strip()
        query_clean = re.sub(r'--.*$', '', query_upper, flags=re.MULTILINE)
        query_clean = re.sub(r'/\*.*?\*/', '', query_clean, flags=re.DOTALL)
        query_clean = ' '.join(query_clean.split())
        
        dangerous_operations = [
            'DROP', 'DELETE', 'UPDATE', 'INSERT', 'CREATE', 'ALTER',
            'TRUNCATE', 'GRANT', 'REVOKE', 'COMMIT', 'ROLLBACK',
            'BEGIN', 'START TRANSACTION', 'SAVEPOINT', 'RELEASE'
        ]
        
        for operation in dangerous_operations:
            if query_clean.startswith(operation):
                raise ValueError(f"Operation '{operation}' is not allowed in read-only mode")
                
        return True

    async def execute_sql(
        self,
        query: Annotated[str, "SQL query to execute"],
        read_only: Annotated[bool, "Force read-only mode for this query"] = True,
        timeout: Annotated[int, "Query timeout in seconds"] = 30
    ) -> Dict[str, Any]:
        """
        Execute a SQL query with safety checks and error handling.
        
        Args:
            query: The SQL query to execute
            read_only: Whether to enforce read-only mode (default: True)
            timeout: Query timeout in seconds
            
        Returns:
            Dictionary containing query results and metadata
        """
        if psycopg is None:
            raise RuntimeError("PostgreSQL support is not available")
            
        original_read_only = self._read_only_mode
        if read_only:
            self._read_only_mode = True
            
        try:
            self._validate_sql_safety(query)
            
            conn = self.connection
            with conn.cursor() as cur:
                timeout_ms = timeout * 1000
                cur.execute(f"SET statement_timeout = {timeout_ms}")  # type: ignore
                cur.execute(query)  # type: ignore
                
                if cur.description:
                    rows = cur.fetchall()
                    columns = [desc[0] for desc in cur.description]
                    
                    return {
                        "success": True,
                        "query": query,
                        "columns": columns,
                        "rows": rows,
                        "row_count": len(rows),
                    }
                else:
                    return {
                        "success": True,
                        "query": query,
                        "affected_rows": cur.rowcount,
                        "message": f"Query executed successfully. {cur.rowcount} rows affected."
                    }
                    
        except Exception as e:
            return {
                "success": False,
                "query": query,
                "error": str(e),
                "error_type": type(e).__name__
            }
        finally:
            self._read_only_mode = original_read_only

    async def list_schemas(self) -> Dict[str, Any]:
        """
        List all schemas in the database with their types.
        
        Returns:
            Dictionary containing schema information with types
        """
        query = """
        SELECT
            schema_name,
            schema_owner,
            CASE
                WHEN schema_name LIKE 'pg_%' THEN 'System Schema'
                WHEN schema_name = 'information_schema' THEN 'System Information Schema'
                ELSE 'User Schema'
            END as schema_type
        FROM information_schema.schemata
        ORDER BY schema_type, schema_name
        """
        
        result = await self.execute_sql(query, read_only=True)
        if result["success"]:
            return {
                "success": True,
                "schemas": result["rows"],
                "schema_count": result["row_count"]
            }
        else:
            return result

    async def list_tables(
        self,
        schema: Annotated[str, "Schema name to list tables from"] = "public"
    ) -> Dict[str, Any]:
        """
        List all tables in the specified schema.
        
        Args:
            schema: The schema name (default: 'public')
            
        Returns:
            Dictionary containing table information
        """
        return await self.list_objects(schema, "table")

    async def list_objects(
        self,
        schema_name: Annotated[str, "Schema name to list objects from"] = "public",
        object_type: Annotated[str, "Object type: 'table', 'view', 'sequence', or 'extension'"] = "table"
    ) -> Dict[str, Any]:
        """
        List objects of a specific type in a schema.
        
        Args:
            schema_name: The schema name (default: 'public')
            object_type: Type of objects to list (default: 'table')
            
        Returns:
            Dictionary containing object information
        """
        if object_type in ("table", "view"):
            table_type = "BASE TABLE" if object_type == "table" else "VIEW"
            query = f"""
            SELECT table_schema, table_name, table_type
            FROM information_schema.tables
            WHERE table_schema = '{schema_name}' AND table_type = '{table_type}'
            ORDER BY table_name
            """
            result = await self.execute_sql(query, read_only=True)
            
        elif object_type == "sequence":
            query = f"""
            SELECT sequence_schema, sequence_name, data_type
            FROM information_schema.sequences
            WHERE sequence_schema = '{schema_name}'
            ORDER BY sequence_name
            """
            result = await self.execute_sql(query, read_only=True)
            
        elif object_type == "extension":
            query = """
            SELECT extname, extversion, extowner
            FROM pg_extension
            ORDER BY extname
            """
            result = await self.execute_sql(query, read_only=True)
            
        else:
            return {
                "success": False,
                "error": f"Unsupported object type: {object_type}. Use 'table', 'view', 'sequence', or 'extension'"
            }
        
        if result["success"]:
            return {
                "success": True,
                "schema": schema_name,
                "object_type": object_type,
                "objects": result["rows"],
                "object_count": result["row_count"]
            }
        else:
            return result

    async def describe_table(
        self,
        table_name: Annotated[str, "Name of the table to describe"],
        schema: Annotated[str, "Schema name"] = "public"
    ) -> Dict[str, Any]:
        """
        Get detailed information about a table including columns, types, and constraints.
        
        Args:
            table_name: The name of the table
            schema: The schema name (default: 'public')
            
        Returns:
            Dictionary containing table schema information
        """
        query = f"""
        SELECT 
            column_name,
            data_type,
            is_nullable,
            column_default,
            character_maximum_length,
            numeric_precision,
            numeric_scale,
            ordinal_position
        FROM information_schema.columns 
        WHERE table_name = '{table_name}' AND table_schema = '{schema}'
        ORDER BY ordinal_position
        """
        
        result = await self.execute_sql(query, read_only=True)
        if result["success"]:
            return {
                "success": True,
                "table": f"{schema}.{table_name}",
                "columns": result["rows"],
                "column_count": result["row_count"]
            }
        else:
            return result

    async def list_indexes(
        self,
        table_name: Annotated[str, "Name of the table to list indexes for"],
        schema: Annotated[str, "Schema name"] = "public"
    ) -> Dict[str, Any]:
        """
        List all indexes for a specific table.
        
        Args:
            table_name: The name of the table
            schema: The schema name (default: 'public')
            
        Returns:
            Dictionary containing index information
        """
        query = f"""
        SELECT 
            i.indexname,
            i.indexdef,
            idx.indisunique,
            idx.indisprimary,
            idx.indisvalid
        FROM pg_indexes i
        JOIN pg_class c ON c.relname = i.tablename
        JOIN pg_index idx ON idx.indexrelid = (i.schemaname || '.' || i.indexname)::regclass
        WHERE i.tablename = '{table_name}' AND i.schemaname = '{schema}'
        ORDER BY i.indexname
        """
        
        result = await self.execute_sql(query, read_only=True)
        if result["success"]:
            return {
                "success": True,
                "table": f"{schema}.{table_name}",
                "indexes": result["rows"],
                "index_count": result["row_count"]
            }
        else:
            return result

    async def explain_query(
        self,
        query: Annotated[str, "SQL query to explain"],
        format_type: Annotated[str, "Explain format (TEXT, JSON, XML, YAML)"] = "TEXT"
    ) -> Dict[str, Any]:
        """
        Get the execution plan for a SQL query.
        
        Args:
            query: The SQL query to explain
            format_type: The format for the explain output
            
        Returns:
            Dictionary containing the execution plan
        """
        if format_type.upper() not in ["TEXT", "JSON", "XML", "YAML"]:
            raise ValueError("Format type must be one of: TEXT, JSON, XML, YAML")
            
        explain_query = f"EXPLAIN (FORMAT {format_type.upper()}) {query}"
        
        result = await self.execute_sql(explain_query, read_only=True)
        if result["success"]:
            return {
                "success": True,
                "original_query": query,
                "format": format_type.upper(),
                "execution_plan": result["rows"] if result["rows"] else result.get("message", "")
            }
        else:
            return result

    async def check_health(self) -> Dict[str, Any]:
        """
        Check the health and status of the PostgreSQL database connection.
        
        Returns:
            Dictionary containing health information
        """
        try:
            conn = self.connection
            with conn.cursor() as cur:
                cur.execute("SELECT version()")  # type: ignore
                row = cur.fetchone()
                version = row["version"] if row else "Unknown"
                
                cur.execute("SELECT current_database()")  # type: ignore
                row = cur.fetchone()
                db_name = row["current_database"] if row else "Unknown"
                
                cur.execute("SELECT count(*) as connection_count FROM pg_stat_activity")  # type: ignore
                row = cur.fetchone()
                conn_count = row["connection_count"] if row else 0
                
                cur.execute("SELECT pg_size_pretty(pg_database_size(current_database())) as db_size")  # type: ignore
                row = cur.fetchone()
                db_size = row["db_size"] if row else "Unknown"
                
                return {
                    "success": True,
                    "status": "healthy",
                    "database": db_name,
                    "version": version,
                    "connection_count": conn_count,
                    "database_size": db_size,
                    "read_only_mode": self._read_only_mode
                }
                
        except Exception as e:
            return {
                "success": False,
                "status": "unhealthy",
                "error": str(e)
            }


    async def get_database_size_info(self) -> Dict[str, Any]:
        """
        Get overall database size information and top tables by size.
        
        Returns:
            Dictionary containing database size information
        """
        db_size_query = """
        SELECT 
            pg_size_pretty(pg_database_size(current_database())) as database_size,
            current_database() as database_name
        """
        
        tables_size_query = """
        SELECT 
            schemaname,
            tablename,
            pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size,
            pg_size_pretty(pg_relation_size(schemaname||'.'||tablename)) as table_size,
            pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename) - pg_relation_size(schemaname||'.'||tablename)) as index_size
        FROM pg_tables 
        WHERE schemaname NOT IN ('information_schema', 'pg_catalog')
        ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
        LIMIT 10
        """
        
        db_result = await self.execute_sql(db_size_query, read_only=True)
        tables_result = await self.execute_sql(tables_size_query, read_only=True)
        
        if db_result["success"] and tables_result["success"]:
            return {
                "success": True,
                "database_info": db_result["rows"][0] if db_result["rows"] else {},
                "largest_tables": tables_result["rows"],
                "table_count": tables_result["row_count"]
            }
        else:
            return {
                "success": False,
                "error": "Failed to get database size information"
            }

    def close_connection(self) -> None:
        """Close the database connection."""
        if self._connection and not self._connection.closed:
            self._connection.close()
            self._connection = None

    def __del__(self):
        """Ensure connection is closed when object is destroyed."""
        self.close_connection()

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [
            self.execute_sql,
            self.list_schemas,
            self.list_tables,
            self.list_objects,
            self.describe_table,
            self.list_indexes,
            self.explain_query,
            self.check_health,
            self.get_database_size_info,
        ]