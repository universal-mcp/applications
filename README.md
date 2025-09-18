# Universal MCP Applications

**A collection of 80+ installable application wrappers for the Universal MCP framework.**

This package provides a unified collection of all individual Universal MCP applications. It allows you to install every available tool at once and use them either as Python libraries in your own code.

## Installation

It is recommended to use `uv` for faster installation.

```bash
# Recommended using uv
uv pip install universal-mcp-applications

# Or using standard pip
pip install universal-mcp-applications
```

## Usage

The primary way to use the tools in this package is give below :-

### 1. As a Library

Each application can be imported and used directly in your Python projects. This is useful for integrating with other scripts or building more complex workflows.

**Example:**

```python
from universal_mcp_applications.falai import FalaiApp
from universal_mcp.utils import process_output

# Instantiate the application
# You may need to provide credentials via an integration
app = FalaiApp() 

# Call a method
result = app.some_method(param1="value1")

# Process and print the output
process_output(result)
```