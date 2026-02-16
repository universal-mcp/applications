---
name: e2b
description: Application for interacting with the E2B (Code Interpreter Sandbox) platform. Provides tools to execute Python code in a sandboxed environment. Authentication is handled by the configured Integration, fetching the API key.
---

# E2b Integration

Application for interacting with the E2B (Code Interpreter Sandbox) platform. Provides tools to execute Python code in a sandboxed environment. Authentication is handled by the configured Integration, fetching the API key.

## Available Tools

| Tool | Description |
|------|-------------|
| `execute_python_code` | Executes a Python code string in a secure E2B sandbox. It authenticates using the configured API key, runs the code, and returns a formatted string containing the execution's output (stdout/stderr). It raises specific exceptions for authorization failures or general execution issues. |
