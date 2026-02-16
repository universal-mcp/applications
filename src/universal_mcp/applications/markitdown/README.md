---
name: markitdown
description: Defines the foundational structure for applications in Universal MCP. This abstract base class (ABC) outlines the common interface and core functionality that all concrete application classes must implement. It handles basic initialization, such as setting the application name, and mandates the implementation of a method to list available tools. Analytics for application loading are also tracked here. Attributes: name (str): The unique name identifying the application.
---

# Markitdown Integration

Defines the foundational structure for applications in Universal MCP. This abstract base class (ABC) outlines the common interface and core functionality that all concrete application classes must implement. It handles basic initialization, such as setting the application name, and mandates the implementation of a method to list available tools. Analytics for application loading are also tracked here. Attributes: name (str): The unique name identifying the application.

## Available Tools

| Tool | Description |
|------|-------------|
| `convert_to_markdown` | Asynchronously converts a URI or local file path to markdown format using the markitdown converter. |
