from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from universal_mcp.applications.google_sheet.helper import (
    analyze_sheet_for_tables,
    analyze_table_schema,
)


class GoogleSheetApp(APIApplication):
    """
    Application for interacting with Google Sheets API.
    Provides tools to create and manage Google Spreadsheets.
    """

    def __init__(self, integration: Integration | None = None) -> None:
        super().__init__(name="google_sheet", integration=integration)
        self.base_url = "https://sheets.googleapis.com/v4/spreadsheets"

    def create_spreadsheet(self, title: str) -> dict[str, Any]:
        """
        Creates a new, blank Google Spreadsheet file with a specified title. This function generates a completely new document, unlike `add_sheet` which adds a worksheet (tab) to an existing spreadsheet. It returns the API response containing the new spreadsheet's metadata.

        Args:
            title: String representing the desired title for the new spreadsheet

        Returns:
            Dictionary containing the full response from the Google Sheets API, including the spreadsheet's metadata and properties

        Raises:
            HTTPError: When the API request fails due to invalid authentication, network issues, or API limitations
            ValueError: When the title parameter is empty or contains invalid characters

        Tags:
            create, spreadsheet, google-sheets, api, important
        """
        url = self.base_url
        spreadsheet_data = {"properties": {"title": title}}
        response = self._post(url, data=spreadsheet_data)
        return self._handle_response(response)

    def get_spreadsheet_metadata(self, spreadsheetId: str) -> dict[str, Any]:
        """
        Retrieves a spreadsheet's metadata and structural properties, such as sheet names, IDs, and named ranges, using its unique ID. This function intentionally excludes cell data, distinguishing it from `get_values` which fetches the actual content within cells.

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to retrieve (found in the spreadsheet's URL)

        Returns:
            A dictionary containing the full spreadsheet metadata and contents, including properties, sheets, named ranges, and other spreadsheet-specific information from the Google Sheets API

        Raises:
            HTTPError: When the API request fails due to invalid spreadsheetId or insufficient permissions
            ConnectionError: When there's a network connectivity issue
            ValueError: When the response cannot be parsed as JSON

        Tags:
            get, retrieve, spreadsheet, api, metadata, read, important
        """
        url = f"{self.base_url}/{spreadsheetId}"
        response = self._get(url)
        return self._handle_response(response)

    def get_values(
        self,
        spreadsheetId: str,
        range: str,
        majorDimension: str | None = None,
        valueRenderOption: str | None = None,
        dateTimeRenderOption: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves cell values from a single, specified A1 notation range. Unlike `batch_get_values_by_range` which fetches multiple ranges, this function is for a singular query and provides options to control the data's output format (e.g., rows vs. columns, formatted vs. raw values).

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to retrieve values from
            range: A1 notation range string (e.g., 'Sheet1!A1:B2')
            majorDimension: The major dimension that results should use. "ROWS" or "COLUMNS". Example: "ROWS"
            valueRenderOption: How values should be represented in the output. "FORMATTED_VALUE", "UNFORMATTED_VALUE", or "FORMULA". Example: "FORMATTED_VALUE"
            dateTimeRenderOption: How dates, times, and durations should be represented. "SERIAL_NUMBER" or "FORMATTED_STRING". Example: "FORMATTED_STRING"

        Returns:
            A dictionary containing the API response with the requested spreadsheet values and metadata

        Raises:
            HTTPError: If the API request fails due to invalid spreadsheetId, insufficient permissions, or invalid range format
            ValueError: If the spreadsheetId is empty or invalid

        Tags:
            get, read, spreadsheet, values, important
        """
        url = f"{self.base_url}/{spreadsheetId}/values/{range}"
        params = {}

        if majorDimension:
            params["majorDimension"] = majorDimension
        if valueRenderOption:
            params["valueRenderOption"] = valueRenderOption
        if dateTimeRenderOption:
            params["dateTimeRenderOption"] = dateTimeRenderOption

        response = self._get(url, params=params)
        return self._handle_response(response)

    def batch_get_values_by_range(
        self, spreadsheetId: str, ranges: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Efficiently retrieves values from multiple predefined A1 notation ranges in a single API request. Unlike `get_values`, which fetches a single range, or `batch_get_values_by_data_filter`, which uses dynamic filtering criteria, this function operates on a simple list of range strings for bulk data retrieval.

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to retrieve values from
            ranges: Optional list of A1 notation or R1C1 notation range strings (e.g., ['Sheet1!A1:B2', 'Sheet2!C3:D4']). If None, returns values from the entire spreadsheet

        Returns:
            A dictionary containing the API response with the requested spreadsheet values and metadata

        Raises:
            HTTPError: If the API request fails due to invalid spreadsheetId, insufficient permissions, or invalid range format
            ValueError: If the spreadsheetId is empty or invalid

        Tags:
            get, batch, read, spreadsheet, values
        """
        url = f"{self.base_url}/{spreadsheetId}/values:batchGet"
        params = {}
        if ranges:
            params["ranges"] = ranges
        response = self._get(url, params=params)
        return self._handle_response(response)

    def insert_dimensions(
        self,
        spreadsheetId: str,
        sheet_id: int,
        dimension: str,
        start_index: int,
        end_index: int,
        inherit_from_before: bool = True,
        include_spreadsheet_in_response: bool | None = None,
        response_include_grid_data: bool | None = None,
        response_ranges: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Inserts a specified number of empty rows or columns at a given index, shifting existing content. Distinct from `append_dimensions`, which only adds to the end, this function creates space within the sheet's data grid, preserving surrounding data and formatting.

        This function inserts empty rows or columns at a specified location, shifting existing content.
        Use this when you need to add rows/columns in the middle of your data.

        Args:
            spreadsheetId: The ID of the spreadsheet to update. Example: "abc123spreadsheetId"
            sheet_id: The ID of the sheet where the dimensions will be inserted. Example: 0
            dimension: The dimension to insert. Valid values are "ROWS" or "COLUMNS". Example: "ROWS"
            start_index: The start index (0-based) of the dimension range to insert. The inserted dimensions will be placed before this index. Example: 1
            end_index: The end index (0-based, exclusive) of the dimension range to insert. The number of rows/columns to insert is `endIndex - startIndex`. Example: 3
            inherit_from_before: If true, the new dimensions will inherit properties from the dimension before the startIndex. If false (default), they will inherit from the dimension at the startIndex. startIndex must be greater than 0 if inheritFromBefore is true. Example: True
            include_spreadsheet_in_response: True if the updated spreadsheet should be included in the response. Example: True
            response_include_grid_data: True if grid data should be included in the response (if includeSpreadsheetInResponse is true). Example: True
            response_ranges: Limits the ranges of the spreadsheet to include in the response. Example: ["Sheet1!A1:B10"]

        Returns:
            A dictionary containing the Google Sheets API response with update details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or dimension is not "ROWS" or "COLUMNS"

        Tags:
            insert, modify, spreadsheet, rows, columns, dimensions, important
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if dimension not in ["ROWS", "COLUMNS"]:
            raise ValueError('dimension must be either "ROWS" or "COLUMNS"')

        if start_index < 0 or end_index < 0:
            raise ValueError("start_index and end_index must be non-negative")

        if start_index >= end_index:
            raise ValueError("end_index must be greater than start_index")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        request_body: dict[str, Any] = {
            "requests": [
                {
                    "insertDimension": {
                        "inheritFromBefore": inherit_from_before,
                        "range": {
                            "dimension": dimension,
                            "sheetId": sheet_id,
                            "startIndex": start_index,
                            "endIndex": end_index,
                        },
                    }
                }
            ]
        }

        # Add optional parameters if provided
        if include_spreadsheet_in_response is not None:
            request_body["includeSpreadsheetInResponse"] = (
                include_spreadsheet_in_response
            )

        if response_include_grid_data is not None:
            request_body["responseIncludeGridData"] = response_include_grid_data

        if response_ranges is not None:
            request_body["responseRanges"] = response_ranges

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def append_dimensions(
        self,
        spreadsheetId: str,
        sheet_id: int,
        dimension: str,
        length: int,
    ) -> dict[str, Any]:
        """
        Adds a specified number of empty rows or columns to the end of a designated sheet. Unlike `insert_dimensions`, which adds space at a specific index, this function exclusively extends the sheet's boundaries at the bottom or to the right without affecting existing content.

        This function adds empty rows or columns to the end of the sheet without affecting existing content.
        Use this when you need to extend the sheet with additional space at the bottom or right.

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to modify
            sheet_id: The ID of the sheet within the spreadsheet (0 for first sheet)
            dimension: The type of dimension to append - "ROWS" or "COLUMNS"
            length: The number of rows or columns to append to the end

        Returns:
            A dictionary containing the Google Sheets API response with update details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty, dimension is not "ROWS" or "COLUMNS", or length is not positive

        Tags:
            append, modify, spreadsheet, rows, columns, dimensions, important
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if dimension not in ["ROWS", "COLUMNS"]:
            raise ValueError('dimension must be either "ROWS" or "COLUMNS"')

        if length <= 0:
            raise ValueError("length must be a positive integer")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        request_body = {
            "requests": [
                {
                    "appendDimension": {
                        "sheetId": sheet_id,
                        "dimension": dimension,
                        "length": length,
                    }
                }
            ]
        }

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def delete_dimensions(
        self,
        spreadsheetId: str,
        sheet_id: int,
        dimension: str,
        start_index: int,
        end_index: int,
        include_spreadsheet_in_response: bool | None = None,
        response_include_grid_data: bool | None = None,
        response_ranges: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Deletes a specified range of rows or columns, permanently removing them and shifting subsequent cells. This alters the sheet's structure, unlike `clear_values` which only removes cell content. It is the direct counterpart to `insert_dimensions`, which adds space within the data grid.

        Args:
            spreadsheetId: The ID of the spreadsheet. Example: "abc123xyz789"
            sheet_id: The ID of the sheet from which to delete the dimension. Example: 0 for first sheet
            dimension: The dimension to delete. Example: "ROWS"
            start_index: The zero-based start index of the range to delete, inclusive. The start index must be less than the end index. Example: 0
            end_index: The zero-based end index of the range to delete, exclusive. The end index must be greater than the start index. Example: 1
            include_spreadsheet_in_response: Determines if the update response should include the spreadsheet resource. Example: True
            response_include_grid_data: True if grid data should be returned. This parameter is ignored if a field mask was set in the request. Example: True
            response_ranges: Limits the ranges of cells included in the response spreadsheet. Example: ["Sheet1!A1:B2", "Sheet2!C:C"]

        Returns:
            A dictionary containing the Google Sheets API response with update details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty, dimension is not "ROWS" or "COLUMNS", or indices are invalid

        Tags:
            delete, modify, spreadsheet, rows, columns, dimensions, important
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if dimension not in ["ROWS", "COLUMNS"]:
            raise ValueError('dimension must be either "ROWS" or "COLUMNS"')

        if start_index < 0 or end_index < 0:
            raise ValueError("start_index and end_index must be non-negative")

        if start_index >= end_index:
            raise ValueError("end_index must be greater than start_index")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        request_body: dict[str, Any] = {
            "requests": [
                {
                    "deleteDimension": {
                        "range": {
                            "sheetId": sheet_id,
                            "dimension": dimension,
                            "startIndex": start_index,
                            "endIndex": end_index,
                        }
                    }
                }
            ]
        }

        # Add optional response parameters if provided
        if include_spreadsheet_in_response is not None:
            request_body["includeSpreadsheetInResponse"] = (
                include_spreadsheet_in_response
            )

        if response_include_grid_data is not None:
            request_body["responseIncludeGridData"] = response_include_grid_data

        if response_ranges is not None:
            request_body["responseRanges"] = response_ranges

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def add_sheet(
        self,
        spreadsheetId: str,
        title: str | None = None,
        sheetId: int | None = None,
        index: int | None = None,
        sheetType: str = "GRID",
        hidden: bool | None = None,
        rightToLeft: bool | None = None,
        tabColorStyle: dict | None = None,
        # Grid properties
        rowCount: int | None = None,
        columnCount: int | None = None,
        frozenRowCount: int | None = None,
        frozenColumnCount: int | None = None,
        hideGridlines: bool | None = None,
        rowGroupControlAfter: bool | None = None,
        columnGroupControlAfter: bool | None = None,
        # Response options
        includeSpreadsheetInResponse: bool = False,
        responseIncludeGridData: bool = False,
    ) -> dict[str, Any]:
        """
        Adds a new worksheet (tab) to an existing Google Spreadsheet. It allows extensive customization of the new sheet's properties, such as its title, position, and dimensions. This is distinct from `create_spreadsheet`, which generates a completely new spreadsheet file instead of modifying an existing one.

        Args:
            spreadsheetId: The ID of the spreadsheet to add the sheet to. This is the long string of characters in the URL of your Google Sheet. Example: "abc123xyz789"
            title: The name of the sheet. Example: "Q3 Report"
            sheetId: The ID of the sheet. If not set, an ID will be randomly generated. Must be non-negative if set.
            index: The zero-based index of the sheet in the spreadsheet. Example: 0 for the first sheet.
            sheetType: The type of sheet. Options: "GRID", "OBJECT", "DATA_SOURCE". Defaults to "GRID"
            hidden: True if the sheet is hidden in the UI, false if it's visible.
            rightToLeft: True if the sheet is an RTL sheet, false if it's LTR.
            tabColorStyle: The color of the sheet tab. Can contain either 'rgbColor' (with red, green, blue, alpha values 0-1) or 'themeColor' (TEXT, BACKGROUND, ACCENT1-6, LINK).
            rowCount: The number of rows in the sheet.
            columnCount: The number of columns in the sheet.
            frozenRowCount: The number of rows that are frozen in the sheet.
            frozenColumnCount: The number of columns that are frozen in the sheet.
            hideGridlines: True if the gridlines are hidden, false if they are shown.
            rowGroupControlAfter: True if the row group control toggle is shown after the group, false if before.
            columnGroupControlAfter: True if the column group control toggle is shown after the group, false if before.
            includeSpreadsheetInResponse: Whether the response should include the entire spreadsheet resource. Defaults to false.
            responseIncludeGridData: True if grid data should be returned. This parameter is ignored if includeSpreadsheetInResponse is false. Defaults to false.

        Returns:
            A dictionary containing the Google Sheets API response with the new sheet details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or invalid parameters are provided

        Tags:
            add, sheet, spreadsheet, create
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        # Build the addSheet request with properties
        add_sheet_request = {"properties": {}}

        if title is not None:
            add_sheet_request["properties"]["title"] = title

        if sheetId is not None:
            add_sheet_request["properties"]["sheetId"] = sheetId

        if index is not None:
            add_sheet_request["properties"]["index"] = index

        if sheetType is not None:
            add_sheet_request["properties"]["sheetType"] = sheetType

        if hidden is not None:
            add_sheet_request["properties"]["hidden"] = hidden

        if rightToLeft is not None:
            add_sheet_request["properties"]["rightToLeft"] = rightToLeft

        if tabColorStyle is not None:
            add_sheet_request["properties"]["tabColorStyle"] = tabColorStyle

        # Build grid properties if any grid-related parameters are provided
        grid_properties = {}
        if any(
            param is not None
            for param in [
                rowCount,
                columnCount,
                frozenRowCount,
                frozenColumnCount,
                hideGridlines,
                rowGroupControlAfter,
                columnGroupControlAfter,
            ]
        ):
            if rowCount is not None:
                grid_properties["rowCount"] = rowCount

            if columnCount is not None:
                grid_properties["columnCount"] = columnCount

            if frozenRowCount is not None:
                grid_properties["frozenRowCount"] = frozenRowCount

            if frozenColumnCount is not None:
                grid_properties["frozenColumnCount"] = frozenColumnCount

            if hideGridlines is not None:
                grid_properties["hideGridlines"] = hideGridlines

            if rowGroupControlAfter is not None:
                grid_properties["rowGroupControlAfter"] = rowGroupControlAfter

            if columnGroupControlAfter is not None:
                grid_properties["columnGroupControlAfter"] = columnGroupControlAfter

            add_sheet_request["properties"]["gridProperties"] = grid_properties

        request_body = {
            "requests": [{"addSheet": add_sheet_request}],
            "includeSpreadsheetInResponse": includeSpreadsheetInResponse,
            "responseIncludeGridData": responseIncludeGridData,
        }

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def add_basic_chart(
        self,
        spreadsheetId: str,
        source_sheet_id: int,
        chart_title: str,
        chart_type: str,
        domain_range: dict,
        series_ranges: list[dict],
        new_sheet: bool = False,
        chart_position: dict | None = None,
        x_axis_title: str | None = None,
        y_axis_title: str | None = None,
    ) -> dict[str, Any]:
        """
        Adds various axis-based charts (e.g., column, bar, line, area) to a spreadsheet from specified data ranges. The chart can be placed on a new sheet or positioned on an existing one. This is distinct from `add_pie_chart`, which creates proportional visualizations instead of axis-based charts.

        This function creates various types of charts from the specified data ranges and places it in a new sheet or existing sheet.
        Use this when you need to visualize data in different chart formats.

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to modify
            source_sheet_id: The ID of the sheet containing the source data
            chart_title: The title for the chart
            chart_type: The type of chart to create. Supported types: "COLUMN", "BAR", "LINE", "AREA", "STEPPED_AREA", "SCATTER", "COMBO"
            domain_range: Dictionary containing domain range info (e.g., {"startRowIndex": 0, "endRowIndex": 7, "startColumnIndex": 0, "endColumnIndex": 1})
            series_ranges: List of dictionaries containing series range info for each data series
            new_sheet: Whether to create the chart in a new sheet (True) or existing sheet (False)
            chart_position: Optional positioning for chart when new_sheet=False. Example: {"overlayPosition": {"anchorCell": {"sheetId": 0, "rowIndex": 10, "columnIndex": 5}, "offsetXPixels": 0, "offsetYPixels": 0, "widthPixels": 600, "heightPixels": 400}}
            x_axis_title: Optional title for the X-axis (bottom axis). If not provided, defaults to "Categories"
            y_axis_title: Optional title for the Y-axis (left axis). If not provided, defaults to "Values"

        Returns:
            A dictionary containing the Google Sheets API response with the chart details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or invalid parameters are provided

        Tags:
            add, chart, basic-chart, visualization
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not chart_title:
            raise ValueError("chart_title cannot be empty")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        # Build the chart specification
        chart_spec = {
            "title": chart_title,
            "basicChart": {
                "chartType": chart_type,
                "legendPosition": "BOTTOM_LEGEND",
                "axis": [
                    {
                        "position": "BOTTOM_AXIS",
                        "title": x_axis_title if x_axis_title else "Categories",
                    },
                    {
                        "position": "LEFT_AXIS",
                        "title": y_axis_title if y_axis_title else "Values",
                    },
                ],
                "domains": [
                    {
                        "domain": {
                            "sourceRange": {
                                "sources": [
                                    {
                                        "sheetId": source_sheet_id,
                                        "startRowIndex": domain_range.get(
                                            "startRowIndex", 0
                                        ),
                                        "endRowIndex": domain_range.get(
                                            "endRowIndex", 1
                                        ),
                                        "startColumnIndex": domain_range.get(
                                            "startColumnIndex", 0
                                        ),
                                        "endColumnIndex": domain_range.get(
                                            "endColumnIndex", 1
                                        ),
                                    }
                                ]
                            }
                        }
                    }
                ],
                "series": [],
                "headerCount": 1,
            },
        }

        # Add series data
        for series_range in series_ranges:
            series = {
                "series": {
                    "sourceRange": {
                        "sources": [
                            {
                                "sheetId": source_sheet_id,
                                "startRowIndex": series_range.get("startRowIndex", 0),
                                "endRowIndex": series_range.get("endRowIndex", 1),
                                "startColumnIndex": series_range.get(
                                    "startColumnIndex", 0
                                ),
                                "endColumnIndex": series_range.get("endColumnIndex", 1),
                            }
                        ]
                    }
                },
                "targetAxis": "LEFT_AXIS",
            }
            chart_spec["basicChart"]["series"].append(series)

        # Build the position specification
        if new_sheet:
            position_spec = {"newSheet": True}
        # For existing sheet, use overlayPosition structure
        elif chart_position:
            position_spec = chart_position
        else:
            # Default positioning when placing in existing sheet
            position_spec = {
                "overlayPosition": {
                    "anchorCell": {
                        "sheetId": source_sheet_id,
                        "rowIndex": 0,
                        "columnIndex": 0,
                    },
                    "offsetXPixels": 0,
                    "offsetYPixels": 0,
                    "widthPixels": 600,
                    "heightPixels": 400,
                }
            }

        # Build the request body
        request_body = {
            "requests": [
                {"addChart": {"chart": {"spec": chart_spec, "position": position_spec}}}
            ]
        }

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def add_pie_chart(
        self,
        spreadsheetId: str,
        source_sheet_id: int,
        chart_title: str,
        data_range: dict,
        new_sheet: bool = False,
        chart_position: dict | None = None,
        legend_position: str = "BOTTOM_LEGEND",
        pie_hole: float | None = None,
    ) -> dict[str, Any]:
        """
        Adds a pie or donut chart to a Google Spreadsheet from a specified data range. Unlike the more general `add_basic_chart`, this is specialized for visualizing data as proportions of a whole and supports pie-specific options like creating a donut chart via the `pie_hole` parameter.

        This function creates a pie chart from the specified data range and places it in a new sheet or existing sheet.
        Use this when you need to visualize data as proportions of a whole.

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to modify
            source_sheet_id: The ID of the sheet containing the source data
            chart_title: The title for the chart
            data_range: Dictionary containing data range info (e.g., {"startRowIndex": 0, "endRowIndex": 7, "startColumnIndex": 0, "endColumnIndex": 2})
            new_sheet: Whether to create the chart in a new sheet (True) or existing sheet (False)
            chart_position: Optional positioning for chart when new_sheet=False. Example: {"overlayPosition": {"anchorCell": {"sheetId": 0, "rowIndex": 10, "columnIndex": 5}, "offsetXPixels": 0, "offsetYPixels": 0, "widthPixels": 600, "heightPixels": 400}}
            legend_position: Position of the legend. Options: "BOTTOM_LEGEND", "LEFT_LEGEND", "RIGHT_LEGEND", "TOP_LEGEND", "NO_LEGEND"
            pie_hole: Optional hole size for creating a donut chart (0.0 to 1.0). 0.0 = solid pie, 0.5 = 50% hole

        Returns:
            A dictionary containing the Google Sheets API response with the chart details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or invalid parameters are provided

        Tags:
            add, chart, pie, visualization
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not chart_title:
            raise ValueError("chart_title cannot be empty")

        if pie_hole is not None and not 0 <= pie_hole <= 1:
            raise ValueError("pie_hole must be between 0.0 and 1.0")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        # Build the pie chart specification
        pie_chart_spec = {
            "legendPosition": legend_position,
            "domain": {
                "sourceRange": {
                    "sources": [
                        {
                            "sheetId": source_sheet_id,
                            "startRowIndex": data_range.get("startRowIndex", 0),
                            "endRowIndex": data_range.get("endRowIndex", 1),
                            "startColumnIndex": data_range.get("startColumnIndex", 0),
                            "endColumnIndex": data_range.get("startColumnIndex", 0) + 1,
                        }
                    ]
                }
            },
            "series": {
                "sourceRange": {
                    "sources": [
                        {
                            "sheetId": source_sheet_id,
                            "startRowIndex": data_range.get("startRowIndex", 0),
                            "endRowIndex": data_range.get("endRowIndex", 1),
                            "startColumnIndex": data_range.get("startColumnIndex", 0)
                            + 1,
                            "endColumnIndex": data_range.get("endColumnIndex", 2),
                        }
                    ]
                }
            },
        }

        # Add pie hole for donut chart if specified
        if pie_hole is not None:
            pie_chart_spec["pieHole"] = pie_hole

        # Build the chart specification
        chart_spec = {"title": chart_title, "pieChart": pie_chart_spec}

        # Build the position specification
        if new_sheet:
            position_spec = {"newSheet": True}
        # For existing sheet, use overlayPosition structure
        elif chart_position:
            position_spec = chart_position
        else:
            # Default positioning when placing in existing sheet
            position_spec = {
                "overlayPosition": {
                    "anchorCell": {
                        "sheetId": source_sheet_id,
                        "rowIndex": 0,
                        "columnIndex": 0,
                    },
                    "offsetXPixels": 0,
                    "offsetYPixels": 0,
                    "widthPixels": 600,
                    "heightPixels": 400,
                }
            }

        # Build the request body
        request_body = {
            "requests": [
                {"addChart": {"chart": {"spec": chart_spec, "position": position_spec}}}
            ]
        }

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def add_table(
        self,
        spreadsheetId: str,
        sheet_id: int,
        table_name: str,
        table_id: str,
        start_row_index: int,
        end_row_index: int,
        start_column_index: int,
        end_column_index: int,
        column_properties: list[dict] | None = None,
    ) -> dict[str, Any]:
        """
        Creates a structured table within a specified range on a Google Sheet. Defines the table's name, ID, and dimensions, and can optionally configure column properties like data types and validation rules. This action creates a formal table object, distinct from functions that only write cell values.

        This function creates a table with specified properties and column types.
        Use this when you need to create structured data with headers, footers, and column types.

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to modify
            sheet_id: The ID of the sheet where the table will be created
            table_name: The name of the table
            table_id: The unique identifier for the table
            start_row_index: The starting row index (0-based)
            end_row_index: The ending row index (exclusive)
            start_column_index: The starting column index (0-based)
            end_column_index: The ending column index (exclusive)
            column_properties: Optional list of column properties with types and validation rules. Valid column types: "TEXT", "PERCENT", "DROPDOWN", "DOUBLE", "CURRENCY", "DATE", "TIME", "DATE_TIME". Example: [{"columnIndex": 0, "columnName": "Model Number", "columnType": "TEXT"}, {"columnIndex": 1, "columnName": "Sales - Jan", "columnType": "DOUBLE"}, {"columnIndex": 2, "columnName": "Price", "columnType": "CURRENCY"}, {"columnIndex": 3, "columnName": "Progress", "columnType": "PERCENT"}, {"columnIndex": 4, "columnName": "Created Date", "columnType": "DATE"}, {"columnIndex": 5, "columnName": "Status", "columnType": "DROPDOWN", "dataValidationRule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": "Active"}, {"userEnteredValue": "Inactive"}]}}}]
        Returns:
            A dictionary containing the Google Sheets API response with the table details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or invalid parameters are provided

        Tags:
            add, table, structured-data
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not table_name:
            raise ValueError("table_name cannot be empty")

        if not table_id:
            raise ValueError("table_id cannot be empty")

        if (
            start_row_index < 0
            or end_row_index < 0
            or start_column_index < 0
            or end_column_index < 0
        ):
            raise ValueError("All indices must be non-negative")

        if start_row_index >= end_row_index:
            raise ValueError("end_row_index must be greater than start_row_index")

        if start_column_index >= end_column_index:
            raise ValueError("end_column_index must be greater than start_column_index")

        # Validate column properties if provided
        if column_properties:
            valid_column_types = [
                "TEXT",
                "PERCENT",
                "DROPDOWN",
                "DOUBLE",
                "CURRENCY",
                "DATE",
                "TIME",
                "DATE_TIME",
            ]
            for i, prop in enumerate(column_properties):
                if (
                    "columnType" in prop
                    and prop["columnType"] not in valid_column_types
                ):
                    raise ValueError(
                        f"Invalid column type '{prop['columnType']}' at index {i}. Valid types are: {', '.join(valid_column_types)}"
                    )

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        # Build the table specification
        table_spec = {
            "name": table_name,
            "tableId": table_id,
            "range": {
                "sheetId": sheet_id,
                "startColumnIndex": start_column_index,
                "endColumnIndex": end_column_index,
                "startRowIndex": start_row_index,
                "endRowIndex": end_row_index,
            },
        }

        # Add column properties if provided
        if column_properties:
            table_spec["columnProperties"] = column_properties

        # Build the request body
        request_body = {"requests": [{"addTable": {"table": table_spec}}]}

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def update_table(
        self,
        spreadsheetId: str,
        table_id: str,
        table_name: str | None = None,
        start_row_index: int | None = None,
        end_row_index: int | None = None,
        start_column_index: int | None = None,
        end_column_index: int | None = None,
        column_properties: list[dict] | None = None,
    ) -> dict[str, Any]:
        """
        Modifies properties of an existing table within a Google Sheet, such as its name, data range, or column specifications. This function updates the table's structural metadata, distinguishing it from `update_values` which alters the cell data within the table's range.

        This function modifies table properties such as name, range, and column properties.
        Use this when you need to modify an existing table's structure or properties.

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to modify
            table_id: The unique identifier of the table to update
            table_name: Optional new name for the table
            start_row_index: Optional new starting row index (0-based)
            end_row_index: Optional new ending row index (exclusive)
            start_column_index: Optional new starting column index (0-based)
            end_column_index: Optional new ending column index (exclusive)
            column_properties: Optional list of column properties with types and validation rules. Valid column types: "TEXT", "PERCENT", "DROPDOWN", "DOUBLE", "CURRENCY", "DATE", "TIME", "DATE_TIME". Example: [{"columnIndex": 0, "columnName": "Model Number", "columnType": "TEXT"}, {"columnIndex": 1, "columnName": "Sales - Jan", "columnType": "DOUBLE"}, {"columnIndex": 2, "columnName": "Price", "columnType": "CURRENCY"}, {"columnIndex": 3, "columnName": "Progress", "columnType": "PERCENT"}, {"columnIndex": 4, "columnName": "Created Date", "columnType": "DATE"}, {"columnIndex": 5, "columnName": "Status", "columnType": "DROPDOWN", "dataValidationRule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": "Active"}, {"userEnteredValue": "Inactive"}]}}}]

        Returns:
            A dictionary containing the Google Sheets API response with the updated table details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId or table_id is empty or invalid parameters are provided

        Tags:
            update, table, modify, structured-data
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not table_id:
            raise ValueError("table_id cannot be empty")

        # Validate indices if provided
        if start_row_index is not None and start_row_index < 0:
            raise ValueError("start_row_index must be non-negative")

        if end_row_index is not None and end_row_index < 0:
            raise ValueError("end_row_index must be non-negative")

        if start_column_index is not None and start_column_index < 0:
            raise ValueError("start_column_index must be non-negative")

        if end_column_index is not None and end_column_index < 0:
            raise ValueError("end_column_index must be non-negative")

        if (
            start_row_index is not None
            and end_row_index is not None
            and start_row_index >= end_row_index
        ):
            raise ValueError("end_row_index must be greater than start_row_index")

        if (
            start_column_index is not None
            and end_column_index is not None
            and start_column_index >= end_column_index
        ):
            raise ValueError("end_column_index must be greater than start_column_index")

        # Validate column properties if provided
        if column_properties:
            valid_column_types = [
                "TEXT",
                "PERCENT",
                "DROPDOWN",
                "DOUBLE",
                "CURRENCY",
                "DATE",
                "TIME",
                "DATE_TIME",
            ]
            for i, prop in enumerate(column_properties):
                if (
                    "columnType" in prop
                    and prop["columnType"] not in valid_column_types
                ):
                    raise ValueError(
                        f"Invalid column type '{prop['columnType']}' at index {i}. Valid types are: {', '.join(valid_column_types)}"
                    )

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        # Build the table specification and track fields to update
        table_spec: dict[str, Any] = {"tableId": table_id}
        fields_to_update = []

        # Add optional properties if provided
        if table_name is not None:
            table_spec["name"] = table_name
            fields_to_update.append("name")

        # Build range if any range parameters are provided
        range_params: dict[str, Any] = {}
        if start_row_index is not None:
            range_params["startRowIndex"] = start_row_index
        if end_row_index is not None:
            range_params["endRowIndex"] = end_row_index
        if start_column_index is not None:
            range_params["startColumnIndex"] = start_column_index
        if end_column_index is not None:
            range_params["endColumnIndex"] = end_column_index

        if range_params:
            table_spec["range"] = range_params
            fields_to_update.append("range")

        # Add column properties if provided
        if column_properties:
            table_spec["columnProperties"] = column_properties
            fields_to_update.append("columnProperties")

        # Validate that at least one field is being updated
        if not fields_to_update:
            raise ValueError(
                "At least one field must be provided for update (table_name, range indices, or column_properties)"
            )

        # Build the request body
        request_body = {
            "requests": [
                {
                    "updateTable": {
                        "table": table_spec,
                        "fields": ",".join(fields_to_update),
                    }
                }
            ]
        }

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def clear_values(self, spreadsheetId: str, range: str) -> dict[str, Any]:
        """
        Clears data from a single, specified cell range while preserving all formatting. Unlike `delete_dimensions`, it only removes content, not the cells themselves. For clearing multiple ranges simultaneously, use the `batch_clear_values` function.

        Args:
            spreadsheetId: The unique identifier of the Google Spreadsheet to modify
            range: The A1 or R1C1 notation range of cells to clear (e.g., 'Sheet1!A1:B2')

        Returns:
            A dictionary containing the Google Sheets API response

        Raises:
            HttpError: When the API request fails due to invalid spreadsheetId, invalid range format, or insufficient permissions
            ValueError: When spreadsheetId is empty or range is in invalid format

        Tags:
            clear, modify, spreadsheet, api, sheets, data-management, important
        """
        url = f"{self.base_url}/{spreadsheetId}/values/{range}:clear"
        response = self._post(url, data={})
        return self._handle_response(response)

    def update_values(
        self,
        spreadsheetId: str,
        range: str,
        values: list[list[Any]],
        value_input_option: str = "RAW",
    ) -> dict[str, Any]:
        """
        Overwrites cell values within a specific A1 notation range using a provided 2D list. This function replaces existing data in a predefined area, distinguishing it from `append_values`, which adds new rows after a table instead of overwriting a specific block of cells.

        Args:
            spreadsheetId: The unique identifier of the target Google Spreadsheet
            range: The A1 notation range where values will be updated (e.g., 'Sheet1!A1:B2')
            values: A list of lists containing the data to write, where each inner list represents a row of values
            value_input_option: Determines how input data should be interpreted: 'RAW' (as-is) or 'USER_ENTERED' (parsed as UI input). Defaults to 'RAW'

        Returns:
            A dictionary containing the Google Sheets API response with update details

        Raises:
            RequestError: When the API request fails due to invalid parameters or network issues
            AuthenticationError: When authentication with the Google Sheets API fails

        Tags:
            update, write, sheets, api, important, data-modification, google-sheets
        """
        url = f"{self.base_url}/{spreadsheetId}/values/{range}"
        params = {"valueInputOption": value_input_option}
        data = {"range": range, "values": values}
        response = self._put(url, data=data, params=params)
        return self._handle_response(response)

    def batch_clear_values(
        self,
        spreadsheetId: str,
        ranges: list[str],
    ) -> dict[str, Any]:
        """
        Clears cell values from multiple specified ranges in a single batch operation, preserving existing formatting. Unlike `clear_values`, which handles a single range, this method efficiently processes a list of ranges at once, removing only the content and not the cells themselves.

        Args:
            spreadsheetId: The ID of the spreadsheet to update. Example: "1q2w3e4r5t6y7u8i9o0p"
            ranges: The ranges to clear, in A1 notation or R1C1 notation. Example: ["Sheet1!A1:B2", "Sheet1!C3:D4"]

        Returns:
            A dictionary containing the Google Sheets API response with clear details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or ranges is empty

        Tags:
            clear, batch, values, spreadsheet
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not ranges or not isinstance(ranges, list) or len(ranges) == 0:
            raise ValueError("ranges must be a non-empty list")

        url = f"{self.base_url}/{spreadsheetId}/values:batchClear"

        request_body = {"ranges": ranges}

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def batch_get_values_by_data_filter(
        self,
        spreadsheetId: str,
        data_filters: list[dict],
        major_dimension: str | None = None,
        value_render_option: str | None = None,
        date_time_render_option: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves values from spreadsheet ranges matching a list of data filters. This method provides dynamic, criteria-based selection using A1 notation or grid coordinates, unlike `batch_get_values_by_range` which uses a simple list of range strings. It is ideal for fetching multiple, specific datasets in one request.

        Args:
            spreadsheetId: The ID of the spreadsheet to retrieve data from. Example: "1q2w3e4r5t6y7u8i9o0p"
            data_filters: The data filters used to match the ranges of values to retrieve. Ranges that match any of the specified data filters are included in the response. Each filter can contain:
                - a1Range: Selects data that matches the specified A1 range. Example: "Sheet1!A1:B5"
                - gridRange: Selects data that matches the specified grid range. Example: {"sheetId": 0, "startRowIndex": 0, "endRowIndex": 5, "startColumnIndex": 0, "endColumnIndex": 2}
            major_dimension: The major dimension that results should use. For example, if the spreadsheet data is: A1=1,B1=2,A2=3,B2=4, then a request that selects that range and sets majorDimension=ROWS returns [[1,2],[3,4]], whereas a request that sets majorDimension=COLUMNS returns [[1,3],[2,4]]. Options: "ROWS" or "COLUMNS". Example: "ROWS"
            value_render_option: How values should be represented in the output. The default render option is FORMATTED_VALUE. Options: "FORMATTED_VALUE", "UNFORMATTED_VALUE", or "FORMULA". Example: "FORMATTED_VALUE"
            date_time_render_option: How dates, times, and durations should be represented in the output. This is ignored if valueRenderOption is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER. Options: "SERIAL_NUMBER" or "FORMATTED_STRING". Example: "SERIAL_NUMBER"

        Returns:
            A dictionary containing the filtered values that match the specified data filters

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or data_filters is empty

        Tags:
            get, batch, data-filter, values, spreadsheet
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if (
            not data_filters
            or not isinstance(data_filters, list)
            or len(data_filters) == 0
        ):
            raise ValueError("data_filters must be a non-empty list")

        if major_dimension and major_dimension not in ["ROWS", "COLUMNS"]:
            raise ValueError('major_dimension must be either "ROWS" or "COLUMNS"')

        if value_render_option and value_render_option not in [
            "FORMATTED_VALUE",
            "UNFORMATTED_VALUE",
            "FORMULA",
        ]:
            raise ValueError(
                'value_render_option must be either "FORMATTED_VALUE", "UNFORMATTED_VALUE", or "FORMULA"'
            )

        if date_time_render_option and date_time_render_option not in [
            "SERIAL_NUMBER",
            "FORMATTED_STRING",
        ]:
            raise ValueError(
                'date_time_render_option must be either "SERIAL_NUMBER" or "FORMATTED_STRING"'
            )

        url = f"{self.base_url}/{spreadsheetId}/values:batchGetByDataFilter"

        request_body: dict[str, Any] = {"dataFilters": data_filters}

        # Add optional parameters if provided
        if major_dimension:
            request_body["majorDimension"] = major_dimension

        if value_render_option:
            request_body["valueRenderOption"] = value_render_option

        if date_time_render_option:
            request_body["dateTimeRenderOption"] = date_time_render_option

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def copy_sheet_to_spreadsheet(
        self,
        spreadsheetId: str,
        sheet_id: int,
        destination_spreadsheetId: str,
    ) -> dict[str, Any]:
        """
        Copies a specific sheet, including all its data and formatting, from a source spreadsheet to a different destination spreadsheet. This action duplicates an entire worksheet into another workbook, returning properties of the newly created sheet.


        Args:
            spreadsheetId: The ID of the spreadsheet containing the sheet to copy. Example: "1qZ_..."
            sheet_id: The ID of the sheet to copy. Example: 0
            destination_spreadsheetId: The ID of the spreadsheet to copy the sheet to. Example: "2rY_..."

        Returns:
            A dictionary containing the Google Sheets API response with copy details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When any required parameter is empty or invalid

        Tags:
            copy, sheet, spreadsheet, duplicate
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if sheet_id is None:
            raise ValueError("sheet_id cannot be empty")

        if not destination_spreadsheetId:
            raise ValueError("destination_spreadsheetId cannot be empty")

        url = f"{self.base_url}/{spreadsheetId}/sheets/{sheet_id}:copyTo"

        request_body = {"destinationSpreadsheetId": destination_spreadsheetId}

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def write_values_to_sheet(
        self,
        spreadsheetId: str,
        sheet_name: str,
        values: list[list[Any]],
        first_cell_location: str | None = None,
        value_input_option: str = "USER_ENTERED",
        include_values_in_response: bool = False,
    ) -> dict[str, Any]:
        """
        Writes a 2D list of values to a sheet, overwriting existing data. Data is written starting from a specified cell, or defaults to cell A1 if no location is provided. This differs from `append_values`, which adds new rows after existing data without replacing content.

        Args:
            spreadsheetId: The unique identifier of the Google Sheets spreadsheet to be updated. Example: "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
            sheet_name: The name of the specific sheet within the spreadsheet to update. Example: "Sheet1"
            values: A 2D list of cell values. Each inner list represents a row. Values can be strings, numbers, or booleans. Ensure columns are properly aligned across rows. Example: [['Item', 'Cost', 'Stocked', 'Ship Date'], ['Wheel', 20.5, True, '2020-06-01'], ['Screw', 0.5, True, '2020-06-03'], ['Nut', 0.25, False, '2020-06-02']]
            first_cell_location: The starting cell for the update range, specified in A1 notation (e.g., 'A1', 'B2'). The update will extend from this cell to the right and down, based on the provided values. If omitted, values are appended to the end of the sheet. Example: "A1"
            value_input_option: How input data is interpreted. 'USER_ENTERED': Values parsed as if typed by a user (e.g., strings may become numbers/dates, formulas are calculated); recommended for formulas. 'RAW': Values stored as-is without parsing (e.g., '123' stays string, '=SUM(A1:B1)' stays string). Defaults to 'USER_ENTERED'. Example: "USER_ENTERED"
            include_values_in_response: If set to True, the response will include the updated values from the spreadsheet. Defaults to False. Example: True

        Returns:
            A dictionary containing the Google Sheets API response with update details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty, sheet_name is empty, or values is empty

        Tags:
            batch, update, write, sheets, api, important, data-modification, google-sheets
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not sheet_name:
            raise ValueError("sheet_name cannot be empty")

        if not values or not isinstance(values, list) or len(values) == 0:
            raise ValueError("values must be a non-empty 2D list")

        if value_input_option not in ["RAW", "USER_ENTERED"]:
            raise ValueError(
                'value_input_option must be either "RAW" or "USER_ENTERED"'
            )

        # Determine the range based on first_cell_location
        if first_cell_location:
            # Update specific range starting from first_cell_location
            range_str = f"{sheet_name}!{first_cell_location}"
        else:
            # Append to the sheet (no specific range)
            range_str = f"{sheet_name}"

        url = f"{self.base_url}/{spreadsheetId}/values/{range_str}"

        params = {
            "valueInputOption": value_input_option,
            "includeValuesInResponse": include_values_in_response,
        }

        data = {"values": values}

        response = self._put(url, data=data, params=params)
        return self._handle_response(response)

    def append_values(
        self,
        spreadsheetId: str,
        range: str,
        value_input_option: str,
        values: list[list[Any]],
        insert_data_option: str | None = None,
        include_values_in_response: bool | None = None,
        response_value_render_option: str | None = None,
        response_date_time_render_option: str | None = None,
    ) -> dict[str, Any]:
        """
        Appends rows of data after a specified table in a Google Sheet. Distinct from `update_values` which overwrites data, this function adds new rows at the end of the table. It can also insert rows, shifting existing cells down, offering finer control over data addition.

        Args:
            spreadsheetId: The ID of the spreadsheet to update. Example: "1q0gLhLdGXYZblahblahblah"
            range: The A1 notation of a range to search for a logical table of data. Values are appended after the last row of the table. Example: "Sheet1!A1:B2"
            value_input_option: How the input data should be interpreted. Required. Options: "RAW" or "USER_ENTERED". Example: "USER_ENTERED"
            values: The data to be written. This is an array of arrays, the outer array representing all the data and each inner array representing a major dimension. Each item in the inner array corresponds with one cell. Example: [["A1_val1", "A1_val2"], ["A2_val1", "A2_val2"]]
            insert_data_option: How the input data should be inserted. Options: "OVERWRITE" or "INSERT_ROWS". Use "INSERT_ROWS" to add new rows instead of overwriting existing data. Example: "INSERT_ROWS"
            include_values_in_response: Determines if the update response should include the values of the cells that were appended. By default, responses do not include the updated values. Example: True
            response_value_render_option: Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE. Options: "FORMATTED_VALUE", "UNFORMATTED_VALUE", or "FORMULA". Example: "FORMATTED_VALUE"
            response_date_time_render_option: Determines how dates, times, and durations in the response should be rendered. This is ignored if responseValueRenderOption is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER. Options: "SERIAL_NUMBER" or "FORMATTED_STRING". Example: "SERIAL_NUMBER"

        Returns:
            A dictionary containing the Google Sheets API response with append details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When required parameters are empty or invalid

        Tags:
            append, values, spreadsheet, data, important
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not range:
            raise ValueError("range cannot be empty")

        if not value_input_option:
            raise ValueError("value_input_option cannot be empty")

        if value_input_option not in ["RAW", "USER_ENTERED"]:
            raise ValueError(
                'value_input_option must be either "RAW" or "USER_ENTERED"'
            )

        if not values or not isinstance(values, list) or len(values) == 0:
            raise ValueError("values must be a non-empty 2D list")

        if insert_data_option and insert_data_option not in [
            "OVERWRITE",
            "INSERT_ROWS",
        ]:
            raise ValueError(
                'insert_data_option must be either "OVERWRITE" or "INSERT_ROWS"'
            )

        if response_value_render_option and response_value_render_option not in [
            "FORMATTED_VALUE",
            "UNFORMATTED_VALUE",
            "FORMULA",
        ]:
            raise ValueError(
                'response_value_render_option must be either "FORMATTED_VALUE", "UNFORMATTED_VALUE", or "FORMULA"'
            )

        if (
            response_date_time_render_option
            and response_date_time_render_option
            not in ["SERIAL_NUMBER", "FORMATTED_STRING"]
        ):
            raise ValueError(
                'response_date_time_render_option must be either "SERIAL_NUMBER" or "FORMATTED_STRING"'
            )

        url = f"{self.base_url}/{spreadsheetId}/values/{range}:append"

        params: dict[str, Any] = {"valueInputOption": value_input_option}

        # Add optional parameters if provided
        if insert_data_option:
            params["insertDataOption"] = insert_data_option

        if include_values_in_response is not None:
            params["includeValuesInResponse"] = include_values_in_response

        if response_value_render_option:
            params["responseValueRenderOption"] = response_value_render_option

        if response_date_time_render_option:
            params["responseDateTimeRenderOption"] = response_date_time_render_option

        data = {"values": values}

        response = self._post(url, data=data, params=params)
        return self._handle_response(response)

    def clear_basic_filter(
        self,
        spreadsheetId: str,
        sheet_id: int,
    ) -> dict[str, Any]:
        """
        Removes the basic filter from a specified sheet, clearing active sorting and filtering criteria to restore the default data view. As the direct counterpart to `set_basic_filter`, this function removes the entire filter object, not just the cell content.

        Args:
            spreadsheetId: The ID of the spreadsheet. Example: "abc123xyz789"
            sheet_id: The ID of the sheet on which the basic filter should be cleared. Example: 0

        Returns:
            A dictionary containing the Google Sheets API response with update details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or sheet_id is negative

        Tags:
            clear, filter, basic-filter, spreadsheet
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if sheet_id < 0:
            raise ValueError("sheet_id must be non-negative")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        request_body = {"requests": [{"clearBasicFilter": {"sheetId": sheet_id}}]}

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def delete_sheet(
        self,
        spreadsheetId: str,
        sheet_id: int,
    ) -> dict[str, Any]:
        """
        Permanently deletes a specific sheet (worksheet) from a Google Spreadsheet using its sheet ID. This operation removes the target sheet and all its contents, acting as the direct counterpart to the `add_sheet` function which creates new sheets within a spreadsheet.

        Args:
            spreadsheetId: The ID of the spreadsheet from which to delete the sheet. Example: "abc123xyz789"
            sheet_id: The ID of the sheet to delete. If the sheet is of DATA_SOURCE type, the associated DataSource is also deleted. Example: 123456789

        Returns:
            A dictionary containing the Google Sheets API response with update details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or sheet_id is negative

        Tags:
            delete, sheet, spreadsheet, worksheet
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if sheet_id < 0:
            raise ValueError("sheet_id must be non-negative")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        request_body = {"requests": [{"deleteSheet": {"sheetId": sheet_id}}]}

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def discover_tables(
        self,
        spreadsheetId: str,
        min_rows: int = 2,
        min_columns: int = 1,
        min_confidence: float = 0.5,
    ) -> dict[str, Any]:
        """
        Heuristically analyzes a spreadsheet to discover and list all table-like data structures, identifying headers and data boundaries. It returns informal data blocks meeting specified size criteria, distinguishing it from functions like `add_table` that manage formally defined tables.

        Args:
            spreadsheetId: Google Sheets ID from the URL (e.g., '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'). Example: "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
            min_rows: Minimum number of data rows to consider a valid table. Example: 2
            min_columns: Minimum number of columns to consider a valid table. Example: 1
            min_confidence: Minimum confidence score (0.0-1.0) to consider a valid table. Example: 0.5

        Returns:
            A dictionary containing the list of discovered tables with their properties

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or parameters are invalid

        Tags:
            list, tables, discover, analyze, spreadsheet, important
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if min_rows < 1:
            raise ValueError("min_rows must be at least 1")

        if min_columns < 1:
            raise ValueError("min_columns must be at least 1")

        if not 0 <= min_confidence <= 1:
            raise ValueError("min_confidence must be between 0.0 and 1.0")

        # Get spreadsheet structure
        spreadsheet = self.get_spreadsheet_metadata(spreadsheetId)

        tables = []

        for sheet in spreadsheet.get("sheets", []):
            sheet_properties = sheet.get("properties", {})
            sheet_id = sheet_properties.get("sheetId")
            sheet_title = sheet_properties.get("title", "Sheet1")

            # Analyze sheet for tables using helper function
            sheet_tables = analyze_sheet_for_tables(
                self.get_values,  # Pass the get_values method as a function
                spreadsheetId,
                sheet_id,
                sheet_title,
                min_rows,
                min_columns,
                min_confidence,
            )

            tables.extend(sheet_tables)

        return {
            "spreadsheetId": spreadsheetId,
            "total_tables": len(tables),
            "tables": tables,
            "analysis_parameters": {
                "min_rows": min_rows,
                "min_columns": min_columns,
            },
        }

    def analyze_table_schema(
        self,
        spreadsheetId: str,
        table_name: str,
        sheet_name: str | None = None,
        sample_size: int = 50,
    ) -> dict[str, Any]:
        """
        Infers a specified table's schema by analyzing a data sample. After locating the table by name (a value discovered via `discover_tables`), this function determines the most likely data type and properties for each column, providing a detailed structural breakdown of its content.

        Args:
            spreadsheetId: Google Sheets ID from the URL (e.g., '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms')
            table_name: Specific table name from LIST_TABLES response (e.g., 'Sales_Data', 'Employee_List'). Use 'auto' to analyze the largest/most prominent table
            sheet_name: Sheet/tab name if table_name is ambiguous across multiple sheets
            sample_size: Number of rows to sample for type inference (1-1000, default 50)

        Returns:
            A dictionary containing the table schema with column names, types, and constraints

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty, table_name is empty, or sample_size is invalid

        Tags:
            schema, analyze, table, structure, types, columns
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not table_name:
            raise ValueError("table_name cannot be empty")

        if not 1 <= sample_size <= 1000:
            raise ValueError("sample_size must be between 1 and 1000")

        # Get spreadsheet structure
        spreadsheet = self.get_spreadsheet_metadata(spreadsheetId)

        # Find the target table
        target_table = None

        for sheet in spreadsheet.get("sheets", []):
            sheet_properties = sheet.get("properties", {})
            sheet_title = sheet_properties.get("title", "Sheet1")

            # If sheet_name is specified, only look in that sheet
            if sheet_name and sheet_title != sheet_name:
                continue

            # Get tables in this sheet
            sheet_tables = analyze_sheet_for_tables(
                self.get_values,
                spreadsheetId,
                sheet_properties.get("sheetId", 0),
                sheet_title,
                min_rows=2,
                min_columns=1,
                min_confidence=0.3,
            )

            for table in sheet_tables:
                if table_name == "auto":
                    # For auto mode, select the largest table
                    if target_table is None or (
                        table["rows"] * table["columns"]
                        > target_table["rows"] * target_table["columns"]
                    ):
                        target_table = table
                elif table["table_name"] == table_name:
                    target_table = table
                    break

            if target_table and table_name != "auto":
                break

        if not target_table:
            raise ValueError(f"Table '{table_name}' not found in spreadsheet")

        # Use the helper function to analyze the table schema
        return analyze_table_schema(
            self.get_values, spreadsheetId, target_table, sample_size
        )

    def set_basic_filter(
        self,
        spreadsheetId: str,
        filter: dict,
    ) -> dict[str, Any]:
        """
        Sets or updates a basic filter on a specified range within a sheet, enabling data sorting and filtering. The filter's target range and optional sort specifications are defined in a dictionary argument. It is the counterpart to `clear_basic_filter`, which removes an existing filter.

        Args:
            spreadsheetId: The ID of the spreadsheet. Example: "abc123xyz789"
            filter: The filter to set. This parameter is required. Contains:
                - range: The range the filter covers (required)
                    - sheetId: The sheet this range is on (required)
                    - startRowIndex: The start row (inclusive) of the range (optional)
                    - endRowIndex: The end row (exclusive) of the range (optional)
                    - startColumnIndex: The start column (inclusive) of the range (optional)
                    - endColumnIndex: The end column (exclusive) of the range (optional)
                - sortSpecs: The sort specifications for the filter (optional)
                    - dimensionIndex: The dimension the sort should be applied to
                    - sortOrder: The order data should be sorted ("ASCENDING", "DESCENDING", "SORT_ORDER_UNSPECIFIED")

        Returns:
            A dictionary containing the Google Sheets API response with filter details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty or filter is missing required fields

        Tags:
            filter, basic-filter, spreadsheet, sort, important
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if not filter:
            raise ValueError("filter cannot be empty")

        # Validate required filter fields
        if "range" not in filter:
            raise ValueError("filter must contain 'range' field")

        # Validate required filter fields using Google API naming convention
        range_data = filter["range"]
        if "sheetId" not in range_data:
            raise ValueError("filter range must contain 'sheetId' field")

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        request_body = {"requests": [{"setBasicFilter": {"filter": filter}}]}

        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def format_cells(
        self,
        spreadsheetId: str,
        worksheetId: int,
        startRowIndex: int,
        startColumnIndex: int,
        endRowIndex: int,
        endColumnIndex: int,
        # Text formatting
        bold: bool | None = None,
        italic: bool | None = None,
        underline: bool | None = None,
        strikethrough: bool | None = None,
        fontSize: int | None = None,
        fontFamily: str | None = None,
        # Colors
        backgroundRed: float | None = None,
        backgroundGreen: float | None = None,
        backgroundBlue: float | None = None,
        textRed: float | None = None,
        textGreen: float | None = None,
        textBlue: float | None = None,
        # Alignment
        horizontalAlignment: str | None = None,  # "LEFT", "CENTER", "RIGHT"
        verticalAlignment: str | None = None,  # "TOP", "MIDDLE", "BOTTOM"
        # Text wrapping
        wrapStrategy: str
        | None = None,  # "OVERFLOW_CELL", "LEGACY_WRAP", "CLIP", "WRAP"
        # Number format
        numberFormat: str | None = None,
        # Borders
        borderTop: dict | None = None,
        borderBottom: dict | None = None,
        borderLeft: dict | None = None,
        borderRight: dict | None = None,
        # Merge cells
        mergeCells: bool = False,
    ) -> dict[str, Any]:
        """
        Applies comprehensive formatting to a specified cell range in a worksheet. It modifies visual properties like text style, color, alignment, borders, and can merge cells, without altering the underlying cell values, distinguishing it from data-modification functions like `update_values`.

        Args:
            spreadsheetId: Identifier of the Google Sheets spreadsheet. Example: "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
            worksheetId: ID (sheetId) of the worksheet. Use `get_spreadsheet_metadata` to find this ID. Example: 123456789
            startRowIndex: 0-based index of the first row in the range. Example: 0
            startColumnIndex: 0-based index of the first column in the range. Example: 0
            endRowIndex: 0-based index of the row *after* the last row in the range (exclusive). Example: 1
            endColumnIndex: 0-based index of the column *after* the last column in the range (exclusive). Example: 2


            bold: Apply bold formatting. Example: True
            italic: Apply italic formatting. Example: False
            underline: Apply underline formatting. Example: False
            strikethrough: Apply strikethrough formatting. Example: False
            fontSize: Font size in points. Example: 12
            fontFamily: Font family name. Example: "Arial", "Times New Roman"

            backgroundRed: Red component of background color. Example: 0.9
            backgroundGreen: Green component of background color. Example: 0.9
            backgroundBlue: Blue component of background color. Example: 0.9

            textRed: Red component of text color. Example: 0.0
            textGreen: Green component of text color. Example: 0.0
            textBlue: Blue component of text color. Example: 0.0

            horizontalAlignment: "LEFT", "CENTER", or "RIGHT". Example: "CENTER"
            verticalAlignment: "TOP", "MIDDLE", or "BOTTOM". Example: "MIDDLE"

            wrapStrategy: "OVERFLOW_CELL", "LEGACY_WRAP", "CLIP", or "WRAP". Example: "WRAP"

            numberFormat: Number format string. Example: "#,##0.00", "0.00%", "$#,##0.00"

            borderTop: Top border settings. Example: {"style": "SOLID", "color": {"red": 0, "green": 0, "blue": 0}}
            borderBottom: Bottom border settings. Example: {"style": "SOLID", "color": {"red": 0, "green": 0, "blue": 0}}
            borderLeft: Left border settings. Example: {"style": "SOLID", "color": {"red": 0, "green": 0, "blue": 0}}
            borderRight: Right border settings. Example: {"style": "SOLID", "color": {"red": 0, "green": 0, "blue": 0}}

            mergeCells: Whether to merge the specified range into a single cell. Example: True

        Returns:
            A dictionary containing the Google Sheets API response with formatting details

        Raises:
            HTTPError: When the API request fails due to invalid parameters or insufficient permissions
            ValueError: When spreadsheetId is empty, indices are invalid, or color values are out of range

        Tags:
            format, cells, styling, text-formatting, background-color, borders, alignment, merge
        """
        if not spreadsheetId:
            raise ValueError("spreadsheetId cannot be empty")

        if worksheetId < 0:
            raise ValueError("worksheetId must be non-negative")

        if (
            startRowIndex < 0
            or startColumnIndex < 0
            or endRowIndex < 0
            or endColumnIndex < 0
        ):
            raise ValueError("All indices must be non-negative")

        if startRowIndex >= endRowIndex:
            raise ValueError("endRowIndex must be greater than startRowIndex")

        if startColumnIndex >= endColumnIndex:
            raise ValueError("endColumnIndex must be greater than startColumnIndex")

        # Validate color values if provided
        for color_name, color_value in [
            ("backgroundRed", backgroundRed),
            ("backgroundGreen", backgroundGreen),
            ("backgroundBlue", backgroundBlue),
            ("textRed", textRed),
            ("textGreen", textGreen),
            ("textBlue", textBlue),
        ]:
            if color_value is not None and not 0 <= color_value <= 1:
                raise ValueError(f"{color_name} must be between 0.0 and 1.0")

        if fontSize is not None and fontSize <= 0:
            raise ValueError("fontSize must be positive")

        if horizontalAlignment and horizontalAlignment not in [
            "LEFT",
            "CENTER",
            "RIGHT",
        ]:
            raise ValueError('horizontalAlignment must be "LEFT", "CENTER", or "RIGHT"')

        if verticalAlignment and verticalAlignment not in ["TOP", "MIDDLE", "BOTTOM"]:
            raise ValueError('verticalAlignment must be "TOP", "MIDDLE", or "BOTTOM"')

        if wrapStrategy and wrapStrategy not in [
            "OVERFLOW_CELL",
            "LEGACY_WRAP",
            "CLIP",
            "WRAP",
        ]:
            raise ValueError(
                'wrapStrategy must be "OVERFLOW_CELL", "LEGACY_WRAP", "CLIP", or "WRAP"'
            )

        url = f"{self.base_url}/{spreadsheetId}:batchUpdate"

        requests = []

        # Handle cell merging first if requested
        if mergeCells:
            requests.append(
                {
                    "mergeCells": {
                        "range": {
                            "sheetId": worksheetId,
                            "startRowIndex": startRowIndex,
                            "endRowIndex": endRowIndex,
                            "startColumnIndex": startColumnIndex,
                            "endColumnIndex": endColumnIndex,
                        },
                        "mergeType": "MERGE_ALL",
                    }
                }
            )

        # Build the cell format request
        cell_format = {}

        # Text format
        text_format = {}
        if bold is not None:
            text_format["bold"] = bold
        if italic is not None:
            text_format["italic"] = italic
        if underline is not None:
            text_format["underline"] = underline
        if strikethrough is not None:
            text_format["strikethrough"] = strikethrough
        if fontSize is not None:
            text_format["fontSize"] = fontSize
        if fontFamily is not None:
            text_format["fontFamily"] = fontFamily

        # Text color
        if any(color is not None for color in [textRed, textGreen, textBlue]):
            text_color = {}
            if textRed is not None:
                text_color["red"] = textRed
            if textGreen is not None:
                text_color["green"] = textGreen
            if textBlue is not None:
                text_color["blue"] = textBlue
            if text_color:
                text_format["foregroundColor"] = {"rgbColor": text_color}

        if text_format:
            cell_format["textFormat"] = text_format

        # Background color
        if any(
            color is not None
            for color in [backgroundRed, backgroundGreen, backgroundBlue]
        ):
            background_color = {}
            if backgroundRed is not None:
                background_color["red"] = backgroundRed
            if backgroundGreen is not None:
                background_color["green"] = backgroundGreen
            if backgroundBlue is not None:
                background_color["blue"] = backgroundBlue
            if background_color:
                cell_format["backgroundColorStyle"] = {"rgbColor": background_color}

        # Alignment
        if horizontalAlignment or verticalAlignment:
            cell_format["horizontalAlignment"] = horizontalAlignment
            cell_format["verticalAlignment"] = verticalAlignment

        # Text wrapping
        if wrapStrategy:
            cell_format["wrapStrategy"] = wrapStrategy

        # Number format
        if numberFormat:
            cell_format["numberFormat"] = {"type": "TEXT", "pattern": numberFormat}

        # Borders
        borders = {}
        for border_side, border_config in [
            ("top", borderTop),
            ("bottom", borderBottom),
            ("left", borderLeft),
            ("right", borderRight),
        ]:
            if border_config:
                borders[border_side] = border_config

        if borders:
            cell_format["borders"] = borders

        # Add cell formatting request if any formatting is specified
        if cell_format:
            requests.append(
                {
                    "repeatCell": {
                        "range": {
                            "sheetId": worksheetId,
                            "startRowIndex": startRowIndex,
                            "endRowIndex": endRowIndex,
                            "startColumnIndex": startColumnIndex,
                            "endColumnIndex": endColumnIndex,
                        },
                        "cell": {"userEnteredFormat": cell_format},
                        "fields": "userEnteredFormat",
                    }
                }
            )

        request_body = {"requests": requests}
        response = self._post(url, data=request_body)
        return self._handle_response(response)

    def list_tools(self):
        """Returns a list of methods exposed as tools."""
        return [
            self.create_spreadsheet,
            self.get_spreadsheet_metadata,
            self.get_values,
            self.batch_get_values_by_range,
            self.insert_dimensions,
            self.append_dimensions,
            self.delete_dimensions,
            self.add_sheet,
            self.add_basic_chart,
            self.add_pie_chart,
            self.add_table,
            self.update_table,
            self.clear_values,
            self.update_values,
            self.batch_clear_values,
            self.batch_get_values_by_data_filter,
            self.copy_sheet_to_spreadsheet,
            self.write_values_to_sheet,
            self.append_values,
            self.clear_basic_filter,
            self.delete_sheet,
            self.discover_tables,
            self.analyze_table_schema,
            self.set_basic_filter,
            self.format_cells,
        ]
