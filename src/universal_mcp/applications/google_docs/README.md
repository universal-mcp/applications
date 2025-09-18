# GoogleDocsApp MCP Server

An MCP Server for the GoogleDocsApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the GoogleDocsApp API.


| Tool | Description |
|------|-------------|
| `create_document` | Creates a blank Google Document with a specified title using a POST request to the Google Docs API. This is the primary creation method, returning the document's metadata, including the ID required by functions like `get_document` or `insert_text` to perform subsequent operations on the new file. |
| `get_document` | Retrieves the complete content and metadata for a specific Google Document using its unique ID. This function performs a GET request to the API, returning the full JSON response. It's the primary read operation, contrasting with `create_document` which creates new documents. |
| `insert_text` | Inserts a text string at a specified index within an existing Google Document using the `batchUpdate` API. This function adds new textual content, distinguishing it from functions that insert non-text elements like tables or apply formatting (`apply_text_style`) to existing content. |
| `apply_text_style` | Applies character-level formatting such as bold, italic, font size, color, and hyperlinks to a specified text range in a document. This function modifies text appearance, distinguishing it from `update_paragraph_style`, which handles block-level formatting like alignment and headings. |
| `delete_content_range` | Deletes content within a specified index range in a Google Document via the batchUpdate API. It removes any content based on location, distinguishing it from functions like `delete_header` or `delete_paragraph_bullets`, which remove specific structures or styles instead. |
| `insert_table` | Inserts a table with specified row and column dimensions at a given index in a Google Document. This function uses the `batchUpdate` API for precise placement, allowing the table to be added to the document's body, a header, or a footer, returning the API's response. |
| `create_footer` | Creates a footer of a specified type in a Google Document via the batch update API. The footer can optionally be associated with a specific section break, enabling distinct footers for different document sections, distinguishing it from the `create_header` and `create_footnote` functions. |
| `create_footnote` | Creates a footnote via the batch update API, inserting a numbered reference at a specified index or a segment's end. This function adds an in-body citation, distinguishing it from `create_footer` which creates a content block at the bottom of the page. |
| `delete_footer` | Deletes a specific footer from a Google Document using its unique ID via a `batchUpdate` request. This operation, the counterpart to `create_footer`, removes an entire footer section, unlike `delete_content_range` which targets text within a specified index range. |
| `create_header` | Creates a header in a specified Google Document via the batchUpdate API endpoint. This function allows defining the header type and can optionally associate it with a specific section break location. It complements the `delete_header` and `create_footer` functions for managing document structure. |
| `delete_header` | Removes a specific header from a Google Document using its unique ID. This function sends a `deleteHeader` request to the batch update API, acting as the direct counterpart to `create_header` and distinguishing it from `delete_footer` which removes footers. |
| `apply_list_style` | Applies a predefined bulleted or numbered list format to paragraphs within a specified range using a `bullet_preset`. This function adds list formatting, distinguishing it from its counterpart, `delete_paragraph_bullets`, and other styling functions like `update_paragraph_style`, which handles alignment and headings. |
| `delete_paragraph_bullets` | Removes bullet points or numbering from paragraphs within a specified range in a Google Document. This function reverts list formatting via the batch update API, acting as the direct counterpart to `apply_list_style` and preserving the underlying text content, unlike `delete_content_range`. |
| `update_paragraph_style` | Applies paragraph-level formatting, such as named styles (e.g., 'HEADING_1'), alignment, or text direction, to a specified text range. This function handles block-level styles, distinguishing it from `apply_text_style`, which formats individual characters with attributes like bold or italic. |
