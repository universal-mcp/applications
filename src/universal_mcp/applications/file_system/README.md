# FileSystemApp MCP Server

An MCP Server for the FileSystemApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the FileSystemApp API.


| Tool | Description |
|------|-------------|
| `read_file` | Asynchronously reads the entire content of a specified file in binary mode. This static method takes a file path and returns its data as a bytes object, serving as a fundamental file retrieval operation within the FileSystem application. |
| `write_file` | Writes binary data to a specified file path. If no path is provided, it creates a unique temporary file in `/tmp`. The function returns a dictionary confirming success and providing metadata about the new file, including its path and size. |
