# Application Docstring Protocol

This protocol defines the strict process for writing and updating docstrings for all applications in this repository.

## 1. Test and Verification
Before writing any docstring, you MUST verify the tool's behavior:
1.  **Functional Test**: Run the tool to ensure it works.
2.  **Limit Check**: Explicitly test boundaries (e.g., pagination limits, default return sizes) to determine validity of arguments like `limit` or `offset`.
3.  **Structure Inspection**: Inspect the raw JSON response to identify **every** key returned by the API.

## 2. Docstring Format Rules
- **Summary**: All key information describing the tool's behavior (including any unusual behavior like lack of pagination) must be in the **first line**.
- **No External References**: Do NOT mention specific internal API names (e.g., "NocoDB", "Airtable") in the description unless necessary for context. Keep it generic to the tool's purpose (e.g., "List all tables...").
- **No 'Note' Blocks**: Do not use separate "Note:" sections. Integrate warnings or important info into the summary line.

## 3. 'Returns' Section
The `Returns` section must be exhaustive and explicit:
- **Type**: Specify the return type (e.g., `dict`, `List[dict]`).
- **Structure**: Describe the exact keys present in the response.
- **Example**: Provide a concise example of the returned structure if it is complex.

## 4. 'Tags' Section
Tags are critical for the agent to quickly identify the tool's capabilities and intended use cases.
- **Functional Tags**: Describe *what* the tool does (e.g., `create`, `read`, `update`, `delete`, `list`, `search`).
- **Domain Tags**: Describe the *entity* it operates on (e.g., `table`, `column`, `record`, `file`, `user`).
- **Behavioral Tags**: Describe *how* it behaves (e.g., `batch` for bulk operations, `idempotent` if safe to retry, `destructive` for deletions).
- **Convenience Tags**: Use `convenience` if the tool wraps complex logic into a single step (e.g., `find_duplicates`).

### Tagging Strategy
Think: "If I were an agent looking for a tool to [action] [entity] in [mode], what keywords would I search for?"
- **Example**: `delete_records` -> `delete`, `data`, `records`, `destructive`, `batch`
- **Example**: `list_tables` -> `read`, `list`, `meta`, `tables`, `structure`
