from typing import Any
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class GoogleDocsApp(APIApplication):
    def __init__(self, integration: Integration) -> None:
        super().__init__(name="google_docs", integration=integration)
        self.base_api_url = "https://docs.googleapis.com/v1/documents"

    async def create_document(self, title: str) -> dict[str, Any]:
        """
        Creates a blank Google Document with a specified title by sending a POST request to the Google Docs API. The function returns a dictionary containing the new document's metadata, including the unique document ID required by other functions for subsequent modifications or retrieval. Note that you need to call other google_docs functions (e.g. `google_docs__insert_text`) to actually add content after creating the document.

        Args:
            title: The title for the new Google Document to be created.

        Returns:
            A dictionary containing the response from the Google Docs API with document details and metadata.

        Raises:
            HTTPError: If the API request fails due to network issues, authentication errors, or invalid parameters.
            RequestException: If there are connection errors or timeout issues during the API request.

        Tags:
            create, document, api, important, google-docs, http
        """
        url = self.base_api_url
        document_data = {"title": title}
        response = await self._apost(url, data=document_data)
        response.raise_for_status()
        payload = response.json()
        payload["Note"] = "You must load and call other google docs content functions (like google_docs__insert_text)"
        return payload

    def get_document(self, document_id: str) -> dict[str, Any]:
        """
        Retrieves the complete, raw JSON object for a Google Document by its ID. This function returns the full, unprocessed API response with all metadata and structural elements, distinguishing it from `get_document_content`, which parses this data to extract only the title and plain text.

        Args:
            document_id: The unique identifier of the Google Document to retrieve.

        Returns:
            A dictionary containing the complete document data as returned by the Google Docs API.

        Raises:
            HTTPError: If the API request fails or the specified document cannot be found.
            JSONDecodeError: If the API response is not valid JSON and cannot be parsed.

        Tags:
            retrieve, read, api, document, google-docs, important
        """
        url = f"{self.base_api_url}/{document_id}"
        response = self._get(url)
        return response.json()

    async def get_document_content(self, document_id: str) -> dict[str, Any]:
        """
        Retrieves and converts a Google Docs document into Markdown-formatted content.

        This method calls the Google Docs API via `get_document`, then parses the document structure
        to extract paragraphs, headings, lists, tables, images, equations, footnotes, and horizontal rules.
        The final result is a clean Markdown string that closely mirrors the layout and content of
        the original document, including support for nested lists and multi-row tables.

        Args:
            document_id (str): The unique ID of the Google Document to retrieve.

        Returns:
            dict[str, Any]: A dictionary with the following keys:
                - 'title' (str): The document's title.
                - 'content' (str): The document content converted to Markdown.
        Markdown Output Supports:
            - Paragraphs and line breaks
            - Headings (Heading 1-6)
            - Bulleted and numbered lists (with nesting)
            - Tables (converted to Markdown tables)
            - Inline images (`![](URL)` format)
            - Equations (LaTeX-style `$...$`)
            - Footnotes (`[^1]` references and notes at the end)
            - Horizontal rules (`---`)

        Tags:
            google-docs, markdown, document-parsing, text-extraction, conversion, structured-data
        """
        import re

        response = self.get_document(document_id)
        title = response.get("title", "")
        body_content = response.get("body", {}).get("content", [])
        inline_objects = response.get("inlineObjects", {})
        lists = response.get("lists", {})
        footnotes_data = response.get("footnotes", {})
        text_chunks: list[str] = []
        footnotes: dict[str, str] = {}
        footnote_index: dict[str, int] = {}
        current_list_counters: dict[str, int] = {}

        def extract_text_from_paragraph(paragraph: dict) -> str:
            """Extracts paragraph text with inline formatting."""
            text = ""
            for elem in paragraph.get("elements", []):
                if "textRun" in elem:
                    content = elem["textRun"].get("content", "")
                    text += content
                elif "inlineObjectElement" in elem:
                    obj_id = elem["inlineObjectElement"]["inlineObjectId"]
                    obj = inline_objects.get(obj_id, {})
                    embed = obj.get("inlineObjectProperties", {}).get("embeddedObject", {})
                    image_source = embed.get("imageProperties", {}).get("contentUri", "")
                    if image_source:
                        text += f"\n\n![]({image_source})\n\n"
            return text

        def extract_table(table: dict) -> str:
            rows = []
            for i, row in enumerate(table.get("tableRows", [])):
                cells = []
                for cell in row.get("tableCells", []):
                    cell_text = ""
                    for content in cell.get("content", []):
                        if "paragraph" in content:
                            cell_text += extract_text_from_paragraph(content["paragraph"]).strip()
                    cells.append(cell_text)
                row_line = "| " + " | ".join(cells) + " |"
                rows.append(row_line)
                if i == 0:
                    rows.insert(1, "| " + " | ".join(["---"] * len(cells)) + " |")
            return "\n".join(rows)

        def extract_heading_style(paragraph: dict) -> str:
            """Returns appropriate Markdown heading level."""
            style = paragraph.get("paragraphStyle", {})
            heading = style.get("namedStyleType", "")
            match = re.match("HEADING_(\\d)", heading)
            if match:
                level = int(match.group(1))
                return "#" * level
            return ""

        def extract_list_prefix(paragraph: dict) -> str:
            """Generates proper list prefix (numbered or bullet)."""
            list_id = paragraph.get("bullet", {}).get("listId")
            if not list_id:
                return ""
            glyph = paragraph["bullet"].get("glyph", None)
            nesting = paragraph["bullet"].get("nestingLevel", 0)
            list_info = lists.get(list_id, {})
            list_type = list_info.get("listProperties", {}).get("nestingLevels", [{}])[nesting].get("glyphType")
            indent = "  " * nesting
            if list_type and "DECIMAL" in list_type:
                current_list_counters[list_id] = current_list_counters.get(list_id, 1)
                prefix = f"{current_list_counters[list_id]}. "
                current_list_counters[list_id] += 1
            else:
                prefix = "- "
            return indent + prefix

        def extract_equation(paragraph: dict) -> str:
            return "\n\n$" + paragraph.get("equation", {}).get("equation", "") + "$\n\n"

        def extract_footnote_ref(footnote_id: str) -> str:
            if footnote_id not in footnote_index:
                footnote_index[footnote_id] = len(footnotes) + 1
                fn_content = footnotes_data.get(footnote_id, {}).get("content", [])
                fn_text = ""
                for item in fn_content:
                    if "paragraph" in item:
                        fn_text += extract_text_from_paragraph(item["paragraph"]).strip()
                footnotes[footnote_id] = fn_text
            return f"[^{footnote_index[footnote_id]}]"

        for element in body_content:
            if "paragraph" in element:
                para = element["paragraph"]
                if "equation" in para:
                    text_chunks.append(extract_equation(para))
                    continue
                heading_md = extract_heading_style(para)
                list_prefix = extract_list_prefix(para)
                para_text = extract_text_from_paragraph(para).strip()
                if para_text:
                    if heading_md:
                        text_chunks.append(f"{heading_md} {para_text}")
                    elif list_prefix:
                        text_chunks.append(f"{list_prefix}{para_text}")
                    else:
                        text_chunks.append(para_text)
            elif "table" in element:
                table_md = extract_table(element["table"])
                text_chunks.append(table_md)
            elif "horizontalRule" in element:
                text_chunks.append("\n---\n")
            elif "tableOfContents" in element:
                text_chunks.append("<!-- Table of Contents -->")
            elif "footnoteReference" in element:
                footnote_id = element["footnoteReference"]["footnoteId"]
                ref = extract_footnote_ref(footnote_id)
                text_chunks.append(ref)
        if footnotes:
            text_chunks.append("\n## Footnotes\n")
            for fid, index in sorted(footnote_index.items(), key=lambda x: x[1]):
                text_chunks.append(f"[^{index}]: {footnotes[fid]}")
        content = "\n\n".join((chunk.strip() for chunk in text_chunks if chunk.strip()))
        return {"title": title, "content": content}

    async def insert_text(self, document_id: str, content: str, index: int = 1) -> dict[str, Any]:
        """
        Inserts a text string at a specified index within a Google Document using the batchUpdate API. Unlike functions that format existing text or delete content ranges, this method specifically adds new textual content to the document body.

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            content: The text content to be inserted into the document.
            index: The zero-based position in the document where the text should be inserted (default is 1).

        Returns:
            A dictionary containing the Google Docs API response after performing the batch update operation.

        Raises:
            HTTPError: If the API request fails, for example due to invalid document_id or insufficient permissions.
            RequestException: If there are network connectivity issues or problems contacting the API endpoint.

        Tags:
            update, insert, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        batch_update_data = {"requests": [{"insertText": {"location": {"index": index}, "text": content}}]}
        response = await self._apost(url, data=batch_update_data)
        response.raise_for_status()
        return response.json()

    async def apply_text_style(
        self,
        document_id: str,
        start_index: int,
        end_index: int,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        font_size: float | None = None,
        link_url: str | None = None,
        foreground_color: dict[str, float] | None = None,
        background_color: dict[str, float] | None = None,
    ) -> dict[str, Any]:
        """
        Applies character-level formatting (e.g., bold, italic, color, links) to a specified text range. This function modifies text attributes directly, distinguishing it from `update_paragraph_style` which handles block-level properties like alignment.

        Args:
            document_id: The unique identifier of the Google Document to update.
            start_index: The zero-based start index of the text range to apply the style.
            end_index: The zero-based end index (exclusive) of the text range to apply the style.
            bold: Whether to apply bold formatting to the text.
            italic: Whether to apply italic formatting to the text.
            underline: Whether to apply underline formatting to the text.
            font_size: Font size in points (e.g., 12.0 for 12pt) to apply to the text.
            link_url: URL to apply as a hyperlink to the text.
            foreground_color: RGB color dictionary with 'red', 'green', and 'blue' floats (0.0 to 1.0) for the text color.
            background_color: RGB color dictionary with 'red', 'green', and 'blue' floats (0.0 to 1.0) for the text background color.

        Returns:
            A dictionary containing the Google Docs API response, or a message if no styling was applied.

        Raises:
            HTTPError: If the Google Docs API request fails.
            RequestException: If there are network connectivity issues during the API request.

        Tags:
            style, format, text, document, api, google-docs, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        text_style = {}
        fields_to_update = []
        if bold:
            text_style["bold"] = True
            fields_to_update.append("bold")
        if italic:
            text_style["italic"] = True
            fields_to_update.append("italic")
        if underline:
            text_style["underline"] = True
            fields_to_update.append("underline")
        if font_size is not None:
            text_style["fontSize"] = {"magnitude": font_size, "unit": "PT"}
            fields_to_update.append("fontSize")
        if link_url is not None:
            text_style["link"] = {"url": link_url}
            fields_to_update.append("link")
        if foreground_color is not None:
            text_style["foregroundColor"] = {
                "color": {
                    "rgbColor": {
                        "red": foreground_color.get("red", 0.0),
                        "green": foreground_color.get("green", 0.0),
                        "blue": foreground_color.get("blue", 0.0),
                    }
                }
            }
            fields_to_update.append("foregroundColor")
        if background_color is not None:
            text_style["backgroundColor"] = {
                "color": {
                    "rgbColor": {
                        "red": background_color.get("red", 0.0),
                        "green": background_color.get("green", 0.0),
                        "blue": background_color.get("blue", 0.0),
                    }
                }
            }
            fields_to_update.append("backgroundColor")
        if not text_style:
            return {"message": "No styling applied"}
        batch_update_data = {
            "requests": [
                {
                    "updateTextStyle": {
                        "range": {"startIndex": start_index, "endIndex": end_index},
                        "textStyle": text_style,
                        "fields": ",".join(fields_to_update),
                    }
                }
            ]
        }
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def update_paragraph_style(
        self,
        document_id: str,
        start_index: int,
        end_index: int,
        named_style_type: str | None = None,
        alignment: str | None = None,
        direction: str | None = None,
        spacing_mode: str | None = None,
        segment_id: str | None = None,
        tab_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Applies paragraph-level formatting like alignment, named styles (e.g., 'HEADING_1'), and text direction to a text range in a Google Doc. Distinct from `apply_text_style`, which handles character formatting, this method modifies properties for entire paragraphs using the batchUpdate API.

        Args:
            document_id: The unique identifier of the Google Document to update.
            start_index: The zero-based start index of the paragraph range to style.
            end_index: The zero-based end index of the paragraph range to style (exclusive).
            named_style_type: The named style type to apply (e.g., 'NORMAL_TEXT', 'TITLE', 'HEADING_1').
            alignment: Paragraph alignment option ('START', 'CENTER', 'END', 'JUSTIFIED').
            direction: Content direction of the paragraph ('LEFT_TO_RIGHT', 'RIGHT_TO_LEFT').
            spacing_mode: Spacing mode for the paragraph ('NEVER_COLLAPSE', 'COLLAPSE_LISTS').
            segment_id: Optional segment ID for the text range.
            tab_id: Optional tab ID for the text range.

        Returns:
            A dictionary containing the API response from the Google Docs batchUpdate request.

        Raises:
            HTTPError: If the API request to update the document fails due to an HTTP error.
            RequestException: If there are network connectivity issues during the API request.

        Tags:
            style, format, paragraph, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        paragraph_style = {}
        fields_to_update = []
        if named_style_type is not None:
            paragraph_style["namedStyleType"] = named_style_type
            fields_to_update.append("namedStyleType")
        if alignment is not None:
            paragraph_style["alignment"] = alignment
            fields_to_update.append("alignment")
        if direction is not None:
            paragraph_style["direction"] = direction
            fields_to_update.append("direction")
        if spacing_mode is not None:
            paragraph_style["spacingMode"] = spacing_mode
            fields_to_update.append("spacingMode")
        if not paragraph_style:
            return {"message": "No paragraph styling applied"}
        range_obj: dict[str, Any] = {"startIndex": start_index, "endIndex": end_index}
        if segment_id is not None:
            range_obj["segmentId"] = segment_id
        if tab_id is not None:
            range_obj["tabId"] = tab_id
        batch_update_data = {
            "requests": [
                {"updateParagraphStyle": {"range": range_obj, "paragraphStyle": paragraph_style, "fields": ",".join(fields_to_update)}}
            ]
        }
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def delete_content_range(
        self, document_id: str, start_index: int, end_index: int, segment_id: str | None = None, tab_id: str | None = None
    ) -> dict[str, Any]:
        """
        Removes content from a specified index range in a Google Document via the batchUpdate API. Unlike functions that delete entire elements (e.g., `delete_header`), this provides granular control by targeting content based on its precise start and end location, optionally within a specific segment or tab.

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            start_index: The zero-based start index of the content range to delete.
            end_index: The zero-based end index of the content range to delete (exclusive).
            segment_id: Optional; the ID of the header, footer, or footnote segment containing the content.
            tab_id: Optional; the ID of the tab containing the content to delete.

        Returns:
            A dictionary representing the Google Docs API response after performing the delete operation.

        Raises:
            HTTPError: Raised when the API request fails due to issues such as invalid document ID or insufficient permissions.
            RequestException: Raised when there are network connectivity issues or problems with the API endpoint.

        Tags:
            delete, remove, content, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        delete_request: dict[str, Any] = {"range": {"startIndex": start_index, "endIndex": end_index}}
        if segment_id is not None:
            delete_request["range"]["segmentId"] = segment_id
        if tab_id is not None:
            delete_request["tabId"] = tab_id
        batch_update_data = {"requests": [{"deleteContentRange": delete_request}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def insert_table(
        self, document_id: str, location_index: int, rows: int, columns: int, segment_id: str = None, tab_id: str = None
    ) -> dict[str, Any]:
        """
        Inserts a table with specified rows and columns at a given index in a Google Document using the batchUpdate API. It can optionally place the table within specific document segments, such as headers or footers, handling structural additions rather than text or style modifications.

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            location_index: The zero-based index within the document body or segment where the table should be inserted.
            rows: The number of rows the inserted table should have.
            columns: The number of columns the inserted table should have.
            segment_id: Optional ID of the header, footer, or footnote segment where the table will be inserted (if applicable).
            tab_id: Optional ID of the tab containing the insertion location.

        Returns:
            A dictionary containing the response from the Google Docs API after performing the table insertion.

        Raises:
            HTTPError: Raised when the API request fails due to reasons such as invalid document ID or insufficient permissions.
            RequestException: Raised when there are network connectivity issues or problems reaching the API endpoint.

        Tags:
            table, insert, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        location = {"index": location_index}
        if segment_id is not None:
            location["segmentId"] = segment_id
        if tab_id is not None:
            location["tabId"] = tab_id
        batch_update_data = {"requests": [{"insertTable": {"location": location, "rows": rows, "columns": columns}}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def create_footer(
        self,
        document_id: str,
        footer_type: str = "DEFAULT",
        section_break_location_index: int = None,
        section_break_segment_id: str = None,
        section_break_tab_id: str = None,
    ) -> dict[str, Any]:
        """
        Creates a footer of a specified type in a Google Document using the batch update API. This function, distinct from `create_header`, can optionally associate the new footer with a specific section break, enabling section-specific footers within the document.

        Args:
            document_id: The unique identifier of the Google Document to update.
            footer_type: The type of footer to create, such as 'DEFAULT' or 'HEADER_FOOTER_TYPE_UNSPECIFIED'.
            section_break_location_index: Optional index of the SectionBreak location to associate with the footer.
            section_break_segment_id: Optional segment ID of the SectionBreak location.
            section_break_tab_id: Optional tab ID of the SectionBreak location.

        Returns:
            A dictionary containing the Google Docs API response from the create footer operation.

        Raises:
            HTTPError: Raised when the API request fails due to reasons like invalid document_id or insufficient permissions.
            RequestException: Raised when there are network connectivity issues or problems with the API endpoint.

        Tags:
            footer, create, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        create_footer_request = {"type": footer_type}
        if section_break_location_index is not None:
            section_break_location = {"index": section_break_location_index}
            if section_break_segment_id is not None:
                section_break_location["segmentId"] = section_break_segment_id
            if section_break_tab_id is not None:
                section_break_location["tabId"] = section_break_tab_id
            create_footer_request["sectionBreakLocation"] = section_break_location
        batch_update_data = {"requests": [{"createFooter": create_footer_request}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def create_footnote(
        self,
        document_id: str,
        location_index: int = None,
        location_segment_id: str = None,
        location_tab_id: str = None,
        end_of_segment_location: bool = False,
        end_of_segment_segment_id: str = None,
        end_of_segment_tab_id: str = None,
    ) -> dict[str, Any]:
        """
        Inserts a numbered footnote reference into a Google Document using the batchUpdate API. The footnote can be placed at a precise index or at the end of a document segment, distinct from the `create_footer` function which adds standard page footers.

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            location_index: The zero-based index within the document where the footnote reference will be inserted (optional if inserting at end of segment).
            location_segment_id: The segment ID where the footnote reference should be inserted (optional, usually empty for the document body).
            location_tab_id: The tab ID for the location within the segment (optional).
            end_of_segment_location: If True, inserts the footnote reference at the end of a segment instead of a specific index (default is False).
            end_of_segment_segment_id: The segment ID indicating where to insert the footnote at the end of a segment (optional).
            end_of_segment_tab_id: The tab ID for the end-of-segment location (optional).

        Returns:
            A dictionary containing the response from the Google Docs API after performing the footnote creation operation.

        Raises:
            HTTPError: Raised when the API request fails, such as due to an invalid document ID or insufficient permissions.
            RequestException: Raised when there are network connectivity issues or problems reaching the API endpoint.

        Tags:
            footnote, create, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        create_footnote_request = {}
        if end_of_segment_location:
            end_of_segment_location_obj = {}
            if end_of_segment_segment_id is not None:
                end_of_segment_location_obj["segmentId"] = end_of_segment_segment_id
            if end_of_segment_tab_id is not None:
                end_of_segment_location_obj["tabId"] = end_of_segment_tab_id
            create_footnote_request["endOfSegmentLocation"] = end_of_segment_location_obj
        else:
            location = {"index": location_index}
            if location_segment_id is not None:
                location["segmentId"] = location_segment_id
            if location_tab_id is not None:
                location["tabId"] = location_tab_id
            create_footnote_request["location"] = location
        batch_update_data = {"requests": [{"createFootnote": create_footnote_request}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def delete_footer(self, document_id: str, footer_id: str, tab_id: str = None) -> dict[str, Any]:
        """
        Deletes a specific footer from a Google Document using its unique ID via a batchUpdate API request. This operation removes the entire footer object, optionally within a specific tab, distinguishing it from functions that delete headers (`delete_header`) or general content (`delete_content_range`).

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            footer_id: The identifier of the footer to delete.
            tab_id: Optional identifier of the tab containing the footer to delete.

        Returns:
            A dictionary containing the response from the Google Docs API after performing the delete footer operation.

        Raises:
            HTTPError: Raised when the API request fails due to reasons such as an invalid document ID or insufficient permissions.
            RequestException: Raised for network-related issues or problems reaching the API endpoint.

        Tags:
            footer, delete, remove, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        delete_footer_request = {"footerId": footer_id}
        if tab_id is not None:
            delete_footer_request["tabId"] = tab_id
        batch_update_data = {"requests": [{"deleteFooter": delete_footer_request}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def create_header(
        self,
        document_id: str,
        header_type: str = "DEFAULT",
        section_break_location_index: int = None,
        section_break_segment_id: str = None,
        section_break_tab_id: str = None,
    ) -> dict[str, Any]:
        """
        Creates a header of a specified type in a Google Document using the batchUpdate API. This function can optionally associate the new header with a specific section break, distinguishing it from the `create_footer` method, which performs the equivalent action for footers.

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            header_type: The type of header to create, e.g., 'DEFAULT' or 'HEADER_FOOTER_TYPE_UNSPECIFIED'.
            section_break_location_index: The index position of the section break location within the document, if applicable.
            section_break_segment_id: The segment ID associated with the section break location, if applicable.
            section_break_tab_id: The tab ID associated with the section break location, if applicable.

        Returns:
            A dictionary containing the response from the Google Docs API after the header creation request.

        Raises:
            HTTPError: If the API request fails due to issues such as an invalid document ID or insufficient permissions.
            RequestException: If there are network problems or issues reaching the API endpoint.

        Tags:
            header, create, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        create_header_request = {"type": header_type}
        if section_break_location_index is not None:
            section_break_location = {"index": section_break_location_index}
            if section_break_segment_id is not None:
                section_break_location["segmentId"] = section_break_segment_id
            if section_break_tab_id is not None:
                section_break_location["tabId"] = section_break_tab_id
            create_header_request["sectionBreakLocation"] = section_break_location
        batch_update_data = {"requests": [{"createHeader": create_header_request}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def delete_header(self, document_id: str, header_id: str, tab_id: str = None) -> dict[str, Any]:
        """
        Deletes a specific header from a Google Document using its unique ID via a batchUpdate API request. This function, the counterpart to `create_header`, removes headers and can optionally target a header within a specific tab. It requires both the document and header IDs for the operation.

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            header_id: The ID of the header to delete.
            tab_id: Optional ID of the tab containing the header to delete.

        Returns:
            A dictionary containing the response from the Google Docs API after performing the delete header operation.

        Raises:
            HTTPError: Raised when the API request fails due to invalid document_id, insufficient permissions, or other HTTP errors.
            RequestException: Raised when network connectivity issues or API endpoint problems occur during the request.

        Tags:
            header, delete, remove, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        delete_header_request = {"headerId": header_id}
        if tab_id is not None:
            delete_header_request["tabId"] = tab_id
        batch_update_data = {"requests": [{"deleteHeader": delete_header_request}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def apply_list_style(
        self, document_id: str, start_index: int, end_index: int, bullet_preset: str, segment_id: str = None, tab_id: str = None
    ) -> dict[str, Any]:
        """
        Applies a predefined list style (bulleted or numbered) to paragraphs within a specified range using a chosen preset. Unlike `delete_paragraph_bullets`, which removes list formatting, this function creates it, distinguishing it from other text and paragraph styling methods in the class.

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            start_index: The zero-based start index of the text range to which the list style should be applied.
            end_index: The zero-based end index (exclusive) of the text range to apply the list style.
            bullet_preset: Specifies the bullet or numbering style preset to use (e.g., bulleted or numbered formats with specific glyphs).
            segment_id: Optional segment ID within the document where the updates apply.
            tab_id: Optional tab ID within the segment to narrow the update scope.

        Returns:
            A dictionary representing the Google Docs API response confirming the application of the bullet list style.

        Raises:
            HTTPError: Raised when the API request to update the document fails (e.g., invalid document ID or insufficient permissions).
            RequestException: Raised on network issues or problems reaching the API endpoint.

        Tags:
            bullets, list, paragraph, document, api, google-docs, batch, content-management, important
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        range_obj = {"startIndex": start_index, "endIndex": end_index}
        if segment_id is not None:
            range_obj["segmentId"] = segment_id
        if tab_id is not None:
            range_obj["tabId"] = tab_id
        batch_update_data = {"requests": [{"createParagraphBullets": {"range": range_obj, "bulletPreset": bullet_preset}}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    async def delete_paragraph_bullets(
        self, document_id: str, start_index: int, end_index: int, segment_id: str = None, tab_id: str = None
    ) -> dict[str, Any]:
        """
        Removes bullet points or numbering from paragraphs within a specified index range in a Google Document. This reverts list formatting to normal text while preserving content, acting as the inverse operation to the `apply_list_style` function.

        Args:
            document_id: The unique identifier of the Google Document to be updated.
            start_index: The zero-based start index of the range to remove bullets from.
            end_index: The zero-based end index of the range to remove bullets from (exclusive).
            segment_id: Optional segment ID specifying a subset of the document where the range applies.
            tab_id: Optional tab ID specifying a particular tab within the document where the range applies.

        Returns:
            A dictionary containing the Google Docs API response after performing the delete bullets operation.

        Raises:
            HTTPError: Raised when the API request fails due to invalid document ID, insufficient permissions, or other server-side errors.
            RequestException: Raised when there are network connectivity issues or problems accessing the API endpoint.

        Tags:
            bullets, delete, remove, list, paragraph, document, api, google-docs, batch, content-management
        """
        url = f"{self.base_api_url}/{document_id}:batchUpdate"
        range_obj = {"startIndex": start_index, "endIndex": end_index}
        if segment_id is not None:
            range_obj["segmentId"] = segment_id
        if tab_id is not None:
            range_obj["tabId"] = tab_id
        batch_update_data = {"requests": [{"deleteParagraphBullets": {"range": range_obj}}]}
        response = await self._apost(url, data=batch_update_data)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.create_document,
            self.get_document_content,
            self.insert_text,
            self.apply_text_style,
            self.delete_content_range,
            self.insert_table,
            self.create_footer,
            self.create_footnote,
            self.delete_footer,
            self.create_header,
            self.delete_header,
            self.apply_list_style,
            self.delete_paragraph_bullets,
            self.update_paragraph_style,
        ]
