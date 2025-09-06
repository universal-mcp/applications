# GoogleSheetApp MCP Server

An MCP Server for the GoogleSheetApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the GoogleSheetApp API.


| Tool | Description |
|------|-------------|
| `create_spreadsheet` | Creates a new blank Google Spreadsheet with the specified title and returns the API response. |
| `get_spreadsheet` | Retrieves detailed information about a specific Google Spreadsheet using its ID  excluding cell data. |
| `batch_get_values` | Retrieves multiple ranges of values from a Google Spreadsheet in a single batch request. |
| `insert_dimensions` | Inserts new rows or columns into a Google Sheet at a specific position within the sheet. |
| `append_dimensions` | Appends empty rows or columns to the end of a Google Sheet. |
| `delete_dimensions` | Tool to delete specified rows or columns from a sheet in a google spreadsheet. use when you need to remove a range of rows or columns. |
| `add_sheet` | Adds a new sheet (worksheet) to a spreadsheet. use this tool to create a new tab within an existing google sheet, optionally specifying its title, index, size, and other properties. |
| `delete_sheet` | Tool to delete a sheet (worksheet) from a spreadsheet. use when you need to remove a specific sheet from a google sheet document. |
| `add_basic_chart` | Adds a basic chart to a Google Spreadsheet like a column chart, bar chart, line chart and  area chart. |
| `add_pie_chart` | Adds a pie chart to a Google Spreadsheet. |
| `add_table` | Adds a table to a Google Spreadsheet. |
| `update_table` | Updates an existing table in a Google Spreadsheet. |
| `clear_values` | Clears all values from a specified range in a Google Spreadsheet while preserving cell formatting and other properties |
| `update_values` | Updates cell values in a specified range of a Google Spreadsheet using the Sheets API |
| `batch_update` | Updates a specified range in a google sheet with given values, or appends them as new rows if `first cell location` is omitted; ensure the target sheet exists and the spreadsheet contains at least one worksheet. |
| `clear_basic_filter` | Tool to clear the basic filter from a sheet. use when you need to remove an existing basic filter from a specific sheet within a google spreadsheet. |
| `list_tables` | This action is used to list all tables in a google spreadsheet, call this action to get the list of tables in a spreadsheet. discover all tables in a google spreadsheet by analyzing sheet structure and detecting data patterns. uses heuristic analysis to find header rows, data boundaries, and table structures. |
| `get_values` | Retrieves values from a specific range in a Google Spreadsheet. |
| `get_table_schema` | Analyzes table structure and infers column names, types, and constraints. |
| `set_basic_filter` | Tool to set a basic filter on a sheet in a google spreadsheet. use when you need to filter or sort data within a specific range on a sheet. |
| `copy_to_sheet` | Tool to copy a single sheet from a spreadsheet to another spreadsheet. Use when you need to duplicate a sheet into a different spreadsheet. |
| `append_values` | Tool to append values to a spreadsheet. use when you need to add new data to the end of an existing table in a google sheet. |
| `batch_clear_values` | Tool to clear one or more ranges of values from a spreadsheet. use when you need to remove data from specific cells or ranges while keeping formatting and other properties intact. |
| `batch_get_values_by_data_filter` | Tool to return one or more ranges of values from a spreadsheet that match the specified data filters. use when you need to retrieve specific data sets based on filtering criteria rather than entire sheets or fixed ranges. |
| `format_cells` | Applies comprehensive cell formatting to a specified range in a Google Sheets worksheet. |
