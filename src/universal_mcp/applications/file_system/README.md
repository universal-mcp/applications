---
name: file-system
description: Defines the foundational structure for applications in Universal MCP. This abstract base class (ABC) outlines the common interface and core functionality that all concrete application classes must implement. It handles basic initialization, such as setting the application name, and mandates the implementation of a method to list available tools. Analytics for application loading are also tracked here. Attributes: name (str): The unique name identifying the application.
---

# FileSystem Integration

Defines the foundational structure for applications in Universal MCP. This abstract base class (ABC) outlines the common interface and core functionality that all concrete application classes must implement. It handles basic initialization, such as setting the application name, and mandates the implementation of a method to list available tools. Analytics for application loading are also tracked here. Attributes: name (str): The unique name identifying the application.

## Available Tools

| Tool | Description |
|------|-------------|
| `read_file` | Asynchronously reads the entire content of a specified file in binary mode. This static method takes a file path and returns its data as a bytes object, serving as a fundamental file retrieval operation within the FileSystem application. |
| `write_file` | Writes binary data to a specified file path. If no path is provided, it creates a unique temporary file in `/tmp`. The function returns a dictionary confirming success and providing metadata about the new file, including its path and size. |
