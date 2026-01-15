# GoogleDocsApp MCP Server

An MCP Server for the GoogleDocsApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the GoogleDocsApp API.


| Tool | Description |
|------|-------------|
| `create_document` | Creates a blank Google Document with a specified title by sending a POST request to the Google Docs API. The function returns a dictionary containing the new document's metadata, including the unique document ID required by other functions for subsequent modifications or retrieval. Note that you need to call other google_docs functions (e.g. `google_docs__insert_text`) to actually add content after creating the document. |
| `get_document` | Retrieves the complete, raw JSON object for a Google Document by its ID. This function returns the full, unprocessed API response with all metadata and structural elements, distinguishing it from `get_document_content`, which parses this data to extract only the title and plain text. |
| `get_document_content` | Retrieves and converts a Google Docs document into Markdown-formatted content. |
| `insert_text` | Inserts a text string at a specified index within a Google Document using the batchUpdate API. Unlike functions that format existing text or delete content ranges, this method specifically adds new textual content to the document body. |
| `apply_text_style` | Applies character-level formatting (e.g., bold, italic, color, links) to a specified text range. This function modifies text attributes directly, distinguishing it from `update_paragraph_style` which handles block-level properties like alignment. |
| `update_paragraph_style` | Applies paragraph-level formatting like alignment, named styles (e.g., 'HEADING_1'), and text direction to a text range in a Google Doc. Distinct from `apply_text_style`, which handles character formatting, this method modifies properties for entire paragraphs using the batchUpdate API. |
| `delete_content_range` | Removes content from a specified index range in a Google Document via the batchUpdate API. Unlike functions that delete entire elements (e.g., `delete_header`), this provides granular control by targeting content based on its precise start and end location, optionally within a specific segment or tab. |
| `insert_table` | Inserts a table with specified rows and columns at a given index in a Google Document using the batchUpdate API. It can optionally place the table within specific document segments, such as headers or footers, handling structural additions rather than text or style modifications. |
| `create_footer` | Creates a footer of a specified type in a Google Document using the batch update API. This function, distinct from `create_header`, can optionally associate the new footer with a specific section break, enabling section-specific footers within the document. |
| `create_footnote` | Inserts a numbered footnote reference into a Google Document using the batchUpdate API. The footnote can be placed at a precise index or at the end of a document segment, distinct from the `create_footer` function which adds standard page footers. |
| `delete_footer` | Deletes a specific footer from a Google Document using its unique ID via a batchUpdate API request. This operation removes the entire footer object, optionally within a specific tab, distinguishing it from functions that delete headers (`delete_header`) or general content (`delete_content_range`). |
| `create_header` | Creates a header of a specified type in a Google Document using the batchUpdate API. This function can optionally associate the new header with a specific section break, distinguishing it from the `create_footer` method, which performs the equivalent action for footers. |
| `delete_header` | Deletes a specific header from a Google Document using its unique ID via a batchUpdate API request. This function, the counterpart to `create_header`, removes headers and can optionally target a header within a specific tab. It requires both the document and header IDs for the operation. |
| `apply_list_style` | Applies a predefined list style (bulleted or numbered) to paragraphs within a specified range using a chosen preset. Unlike `delete_paragraph_bullets`, which removes list formatting, this function creates it, distinguishing it from other text and paragraph styling methods in the class. |
| `delete_paragraph_bullets` | Removes bullet points or numbering from paragraphs within a specified index range in a Google Document. This reverts list formatting to normal text while preserving content, acting as the inverse operation to the `apply_list_style` function. |
