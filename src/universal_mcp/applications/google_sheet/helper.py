"""
Helper functions for Google Sheets table detection and analysis.
"""

from typing import Any


def analyze_sheet_for_tables(
    get_values_func,
    spreadsheet_id: str,
    sheet_id: int,
    sheet_title: str,
    min_rows: int,
    min_columns: int,
    min_confidence: float,
) -> list[dict]:
    """Analyze a sheet to find potential tables."""
    tables = []

    try:
        # Get sample data from the sheet (first 100 rows)
        sample_range = f"{sheet_title}!A1:Z100"
        sample_data = get_values_func(spreadsheetId=spreadsheet_id, range=sample_range)

        values = sample_data.get("values", [])
        if not values or len(values) < min_rows:
            return tables

        # Find potential table regions
        table_regions = find_table_regions(values, min_rows, min_columns)

        for i, region in enumerate(table_regions):
            confidence = calculate_table_confidence(values, region)

            if confidence >= min_confidence:
                table_info = {
                    "table_id": f"{sheet_title}_table_{i + 1}",
                    "table_name": f"{sheet_title}_Table_{i + 1}",
                    "sheet_id": sheet_id,
                    "sheet_name": sheet_title,
                    "start_row": region["start_row"],
                    "end_row": region["end_row"],
                    "start_column": region["start_column"],
                    "end_column": region["end_column"],
                    "rows": region["end_row"] - region["start_row"] + 1,
                    "columns": region["end_column"] - region["start_column"] + 1,
                    "confidence": confidence,
                    "range": f"{sheet_title}!{get_column_letter(region['start_column'])}{region['start_row'] + 1}:{get_column_letter(region['end_column'])}{region['end_row'] + 1}",
                }
                tables.append(table_info)

    except Exception:
        # If analysis fails for a sheet, continue with other sheets
        pass

    return tables


def analyze_table_schema(
    get_values_func, spreadsheet_id: str, table_info: dict, sample_size: int = 50
) -> dict[str, Any]:
    """
    Analyze table structure and infer column names, types, and constraints.

    Args:
        get_values_func: Function to get values from spreadsheet
        spreadsheet_id: The spreadsheet ID
        table_info: Dictionary containing table information from list_tables
        sample_size: Number of rows to sample for type inference

    Returns:
        Dictionary containing the table schema with column analysis
    """
    try:
        # Get sample data from the table
        sample_range = table_info["range"]
        sample_data = get_values_func(spreadsheetId=spreadsheet_id, range=sample_range)

        values = sample_data.get("values", [])
        if not values:
            raise ValueError("No data found in the specified table")

        # Limit sample size to available data
        actual_sample_size = min(sample_size, len(values))
        sample_values = values[:actual_sample_size]

        # Analyze column structure
        columns = analyze_columns(sample_values)

        return {
            "spreadsheet_id": spreadsheet_id,
            "table_name": table_info["table_name"],
            "sheet_name": table_info["sheet_name"],
            "table_range": table_info["range"],
            "total_rows": table_info["rows"],
            "total_columns": table_info["columns"],
            "sample_size": actual_sample_size,
            "columns": columns,
            "schema_version": "1.0",
        }

    except Exception as e:
        raise ValueError(f"Failed to analyze table schema: {str(e)}")


def analyze_columns(sample_values: list[list[Any]]) -> list[dict]:
    """Analyze column structure and infer types."""
    if not sample_values:
        return []

    # Get headers (first row)
    headers = sample_values[0] if sample_values else []
    data_rows = sample_values[1:] if len(sample_values) > 1 else []

    columns = []

    for col_idx in range(len(headers)):
        column_name = (
            str(headers[col_idx]) if col_idx < len(headers) else f"Column_{col_idx + 1}"
        )

        # Extract column values
        column_values = []
        for row in data_rows:
            if col_idx < len(row):
                column_values.append(row[col_idx])

        # Analyze column type
        column_type, constraints = infer_column_type(column_values)

        column_info = {
            "name": column_name,
            "index": col_idx,
            "type": column_type,
            "constraints": constraints,
            "sample_values": column_values[:5],  # First 5 sample values
            "null_count": sum(
                1 for val in column_values if not val or str(val).strip() == ""
            ),
            "unique_count": len(
                set(str(val) for val in column_values if val and str(val).strip())
            ),
        }

        columns.append(column_info)

    return columns


def infer_column_type(values: list[Any]) -> tuple[str, dict]:
    """Infer the most likely data type for a column."""
    if not values:
        return "TEXT", {}

    # Remove empty values
    non_empty_values = [val for val in values if val and str(val).strip()]

    if not non_empty_values:
        return "TEXT", {}

    # Check for boolean values
    boolean_count = sum(
        1
        for val in non_empty_values
        if str(val).lower() in ["true", "false", "yes", "no", "1", "0"]
    )
    if boolean_count / len(non_empty_values) >= 0.8:
        return "BOOLEAN", {}

    # Check for numeric values
    numeric_count = 0
    decimal_count = 0
    date_count = 0

    for val in non_empty_values:
        val_str = str(val)

        # Check for dates (basic patterns)
        if any(
            pattern in val_str.lower()
            for pattern in [
                "/",
                "-",
                "jan",
                "feb",
                "mar",
                "apr",
                "may",
                "jun",
                "jul",
                "aug",
                "sep",
                "oct",
                "nov",
                "dec",
            ]
        ):
            date_count += 1

        # Check for numbers
        if val_str.replace(".", "").replace("-", "").replace(",", "").isdigit():
            numeric_count += 1
            if "." in val_str:
                decimal_count += 1

    # Determine type based on analysis
    if date_count / len(non_empty_values) >= 0.6:
        return "DATE", {}
    elif numeric_count / len(non_empty_values) >= 0.8:
        if decimal_count / numeric_count >= 0.3:
            return "DECIMAL", {"precision": 2}
        else:
            return "INTEGER", {}
    else:
        return "TEXT", {}


def find_table_regions(
    values: list[list], min_rows: int, min_columns: int
) -> list[dict]:
    """Find potential table regions in the data."""
    regions = []

    if not values or len(values) < min_rows:
        return regions

    rows = len(values)
    cols = max(len(row) for row in values) if values else 0

    if cols < min_columns:
        return regions

    # Simple heuristic: look for regions with consistent data
    current_start = -1

    for i in range(rows):
        # Check if this row has enough data
        row_data_count = sum(1 for cell in values[i] if cell and str(cell).strip())

        if row_data_count >= min_columns:
            # Continue current region
            if current_start == -1:
                current_start = i
        else:
            # End current region if it's valid
            if current_start != -1 and i - current_start >= min_rows:
                regions.append(
                    {
                        "start_row": current_start,
                        "end_row": i - 1,
                        "start_column": 0,
                        "end_column": cols - 1,
                    }
                )
            current_start = -1

    # Handle region that extends to end
    if current_start != -1 and rows - current_start >= min_rows:
        regions.append(
            {
                "start_row": current_start,
                "end_row": rows - 1,
                "start_column": 0,
                "end_column": cols - 1,
            }
        )

    return regions


def calculate_table_confidence(values: list[list], region: dict) -> float:
    """Calculate confidence score for a potential table region."""
    if not values:
        return 0.0

    start_row = region["start_row"]
    end_row = region["end_row"]
    start_col = region["start_column"]
    end_col = region["end_column"]

    # Extract region data
    region_data = []
    for i in range(start_row, min(end_row + 1, len(values))):
        row = values[i]
        if len(row) > start_col:
            region_data.append(row[start_col : min(end_col + 1, len(row))])

    if not region_data:
        return 0.0

    # Calculate confidence based on data consistency
    total_cells = sum(len(row) for row in region_data)
    non_empty_cells = sum(
        sum(1 for cell in row if cell and str(cell).strip()) for row in region_data
    )

    if total_cells == 0:
        return 0.0

    # Base confidence on data density
    data_density = non_empty_cells / total_cells

    # Additional factors
    has_headers = has_header_row(region_data)
    consistent_columns = has_consistent_columns(region_data)

    confidence = data_density * 0.6  # 60% weight to data density

    if has_headers:
        confidence += 0.2  # 20% bonus for headers

    if consistent_columns:
        confidence += 0.2  # 20% bonus for consistent structure

    return min(confidence, 1.0)


def has_header_row(data: list[list]) -> bool:
    """Check if the first row looks like a header."""
    if not data or len(data) < 2:
        return False

    header_row = data[0]
    data_rows = data[1:]

    if not header_row or not data_rows:
        return False

    # Check if header row has mostly text values
    header_text_count = sum(
        1
        for cell in header_row
        if cell
        and isinstance(cell, str)
        and not cell.replace(".", "").replace("-", "").isdigit()
    )

    # Check if data rows have different data types than header
    data_numeric_count = 0
    for row in data_rows[:3]:  # Check first 3 data rows
        for cell in row:
            if cell and str(cell).replace(".", "").replace("-", "").isdigit():
                data_numeric_count += 1

    return header_text_count > len(header_row) * 0.5 and data_numeric_count > 0


def has_consistent_columns(data: list[list]) -> bool:
    """Check if columns have consistent data types."""
    if not data or len(data) < 2:
        return False

    # Check if most columns have consistent data types
    consistent_columns = 0
    total_columns = max(len(row) for row in data)

    for col in range(total_columns):
        column_values = [row[col] for row in data if col < len(row) and row[col]]
        if len(column_values) >= 2:
            # Check if column has consistent type
            numeric_count = sum(
                1
                for val in column_values
                if str(val).replace(".", "").replace("-", "").isdigit()
            )
            text_count = len(column_values) - numeric_count

            # If 80% of values are same type, consider consistent
            if (
                numeric_count / len(column_values) >= 0.8
                or text_count / len(column_values) >= 0.8
            ):
                consistent_columns += 1

    return consistent_columns / total_columns >= 0.6 if total_columns > 0 else False


def get_column_letter(column_index: int) -> str:
    """Convert column index to A1 notation letter."""
    result = ""
    while column_index >= 0:
        column_index, remainder = divmod(column_index, 26)
        result = chr(65 + remainder) + result
        column_index -= 1
    return result
