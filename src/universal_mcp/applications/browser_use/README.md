# BrowserUseApp MCP Server

An MCP Server for the BrowserUseApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the BrowserUseApp API.


| Tool | Description |
|------|-------------|
| `browser_task` | Creates and starts a browser automation task in the background. Unlike synchronous tools, this returns immediately with a Task ID so the agent does not block while the browser works. You must use `get_browser_task_status` to check progress and retrieve the final result. |
| `get_browser_task_status` | Checks the status of a browser automation task. Use this to poll for completion and retrieve the final output of a background task. |
| `list_tasks` | Lists recent browser automation tasks. Useful for finding lost task IDs or auditing recent activity. |
| `stop_task` | Stops a running browser automation task. Use this to cancel a stuck or long-running task. |
