"""Docstring generator using litellm with structured output.

This module provides a simple way to generate docstrings and suggest improved
names for Python functions using LLMs with structured output.
"""

import ast
import json
import os
import re
import sys
import time
import traceback
from pathlib import Path

import typer
from rich.console import Console

console = Console()

import litellm
from pydantic import BaseModel, Field

# --- CHANGE 1: Import prompts from the new prompts.py file ---
from src.scripts.prompts import SYSTEM_PROMPT_TEMPLATE, USER_PROMPT_TEMPLATE


class DescriptionOutput(BaseModel):
    """Structure for the generated description output."""

    description: str = Field(
        description="A clear, detailed description of what the function does"
    )
    # suggested_name: Optional[str] = Field(None, description="A better name for the function, if applicable")


class FunctionExtractor(ast.NodeVisitor):
    """
    An AST node visitor that collects the source code of all function
    and method definitions within a Python script.
    """

    def __init__(self, source_code: str):
        self.source_lines = source_code.splitlines(keepends=True)
        self.functions: list[
            tuple[str, str]
        ] = []  # Store tuples of (function_name, function_source)

    def _get_source_segment(self, node: ast.AST) -> str | None:
        """Safely extracts the source segment for a node using ast.get_source_segment."""
        try:
            source_segment = ast.get_source_segment("".join(self.source_lines), node)
            return source_segment
        except Exception:
            return None

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Visits a regular function definition and collects it if not excluded."""
        if not node.name.startswith("_") and node.name != "list_tools":
            source_code = self._get_source_segment(node)
            if source_code:
                self.functions.append((node.name, source_code))
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        """Visits an asynchronous function definition and collects it if not excluded."""
        if not node.name.startswith("_") and node.name != "list_tools":
            source_code = self._get_source_segment(node)
            if source_code:
                self.functions.append((node.name, source_code))
        self.generic_visit(node)


def extract_functions_from_script(file_path: str) -> list[tuple[str, str]]:
    """
    Reads a Python script and extracts the source code of all functions.

    Args:
        file_path: The path to the Python (.py) script.

    Returns:
        A list of tuples, where each tuple contains the function name (str)
        and its full source code (str), including decorators.
        Returns an empty list if the file cannot be read, parsed, or contains no functions.

    Raises:
        FileNotFoundError: If the file_path does not exist.
        SyntaxError: If the file contains invalid Python syntax.
        Exception: For other potential I/O or AST processing errors.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            source_code = f.read()
    except FileNotFoundError:
        raise
    except Exception:
        raise

    try:
        tree = ast.parse(source_code, filename=file_path)
    except SyntaxError:
        raise
    except Exception:
        raise

    try:
        extractor = FunctionExtractor(source_code)
        extractor.visit(tree)

        if not extractor.functions:
            pass

        return extractor.functions
    except Exception:
        import traceback

        traceback.print_exc()
        return []


def extract_json_from_text(text):
    """Extract valid JSON from text that might contain additional content.

    Args:
        text: Raw text response from the model

    Returns:
        Dict containing the extracted JSON data

    Raises:
        ValueError: If no valid JSON could be extracted
    """
    json_match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if json_match:
        try:
            return json.loads(json_match.group(1))
        except json.JSONDecodeError:
            pass

    try:
        start = text.find("{")
        if start >= 0:
            brace_count = 0
            for i in range(start, len(text)):
                if text[i] == "{":
                    brace_count += 1
                elif text[i] == "}":
                    brace_count -= 1
                    if brace_count == 0:
                        return json.loads(text[start : i + 1])
    except json.JSONDecodeError:
        pass

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError("Could not extract valid JSON from the response") from e


def parse_existing_docstring(docstring: str | None) -> tuple[str, str]:
    """
    Parses an existing docstring to separate the summary from the rest.

    Args:
        docstring: The existing docstring string.

    Returns:
        A tuple containing (summary, rest_of_docstring).
        'rest_of_docstring' will include Args, Returns, etc.
    """
    if not docstring:
        return "", ""

    lines = docstring.strip().split("\n")
    summary_lines = []
    rest_lines = []
    summary_done = False

    # Sections that mark the end of the summary
    section_markers = ("Args:", "Returns:", "Raises:", "Tags:", "Example:", "Examples:")

    for i, line in enumerate(lines):
        stripped_line = line.strip()
        if (
            not summary_done
            and stripped_line
            and not stripped_line.startswith(section_markers)
        ):
            summary_lines.append(line.strip())
        elif not summary_done and not stripped_line and summary_lines:
            # This blank line marks the end of the summary
            summary_done = True
            rest_lines = lines[i + 1 :]
            break
        elif stripped_line.startswith(section_markers):
            # A section starts immediately after the summary
            summary_done = True
            rest_lines = lines[i:]
            break
        else:
            # We are already in the rest of the docstring
            rest_lines.append(line)

    summary = " ".join(summary_lines)
    # Reconstruct the rest of the docstring, preserving original indentation
    rest_of_docstring = "\n".join(rest_lines)

    return summary, rest_of_docstring


def generate_description(
    function_code: str, file_content: str, model: str = "perplexity/sonar"
) -> DescriptionOutput:
    """
    Generate a high-quality description and suggest a name for a Python function.

    Args:
        function_code: The source code of the function to document.
        file_content: The entire content of the Python file for context.
        model: The model to use for generating the description.

    Returns:
        A DescriptionOutput object containing the description and optional name.
    """
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(file_content=file_content)
    user_prompt = USER_PROMPT_TEMPLATE.format(function_code=function_code)

    # --- NEW: Retry logic with exponential backoff ---
    max_retries = 3
    base_delay = 2  # in seconds

    for attempt in range(max_retries):
        try:
            response = litellm.completion(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            )
            response_text = response.choices[0].message.content
            try:
                parsed_data = extract_json_from_text(response_text)
                return DescriptionOutput(
                    description=parsed_data.get(
                        "description", "No description available."
                    ),
                    # suggested_name=parsed_data.get("suggested_name"),
                )
            except ValueError:
                return DescriptionOutput(description="Failed to extract description.")

        except litellm.InternalServerError as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt)
                time.sleep(delay)
            else:
                return DescriptionOutput(
                    description=f"Error generating description after {max_retries} retries: {e}"
                )

        except Exception as e:
            return DescriptionOutput(description=f"An unexpected error occurred: {e}")

    return DescriptionOutput(
        description="Failed to generate description after all retries."
    )


def insert_docstring_into_function(function_code: str, docstring: str) -> str:
    """
    Insert a docstring into a function's code, replacing an existing one if present.

    Args:
        function_code: The source code of the function snippet.
        docstring: The formatted docstring string content.

    Returns:
        The updated function code with the docstring inserted.
    """
    try:
        lines = function_code.splitlines(keepends=True)
        tree = ast.parse(function_code)
        if not tree.body or not isinstance(
            tree.body[0], (ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            return function_code

        func_node = tree.body[0]

        # --- REVISED INDENTATION LOGIC ---
        # Determine the correct indentation from the function's existing body.
        if func_node.body:
            # Use the indentation of the first statement in the body (e.g., the old docstring).
            first_body_line_str = lines[func_node.body[0].lineno - 1]
            body_indent = first_body_line_str[
                : len(first_body_line_str) - len(first_body_line_str.lstrip())
            ]
        else:
            # Fallback for empty functions: calculate from the 'def' line.
            def_line = lines[func_node.lineno - 1]
            def_indent = def_line[: len(def_line) - len(def_line.lstrip())]
            body_indent = def_indent + "    "
        # --- END OF REVISED LOGIC ---

        # Format the new docstring with the determined indentation
        new_docstring_lines_formatted = [f'{body_indent}"""\n']
        new_docstring_lines_formatted.extend(
            [f"{body_indent}{line}\n" for line in docstring.splitlines()]
        )
        new_docstring_lines_formatted.append(f'{body_indent}"""\n')

        # Check if the first statement is an existing docstring
        existing_docstring_node = None
        if (
            func_node.body
            and isinstance(func_node.body[0], ast.Expr)
            and isinstance(func_node.body[0].value, ast.Constant)
            and isinstance(func_node.body[0].value.value, str)
        ):
            existing_docstring_node = func_node.body[0]

        # Splice the code
        insert_idx = (
            func_node.body[0].lineno - 1 if func_node.body else func_node.lineno
        )
        pre_insertion_lines = lines[:insert_idx]

        if existing_docstring_node:
            post_insertion_lines = lines[existing_docstring_node.end_lineno :]
        else:
            post_insertion_lines = lines[insert_idx:]

        output_lines = (
            pre_insertion_lines + new_docstring_lines_formatted + post_insertion_lines
        )

        final_code = "".join(output_lines)
        ast.parse(final_code)  # Validate syntax
        return final_code

    except Exception:
        traceback.print_exc(file=sys.stderr)
        return function_code


def rename_function_in_code(function_code: str, old_name: str, new_name: str) -> str:
    """
    Safely renames a function within its source code snippet.

    Args:
        function_code: The source code of the function.
        old_name: The original name of the function.
        new_name: The new name for the function.

    Returns:
        The function code with the updated name.
    """
    # This regex looks for 'def' or 'async def' followed by the old name
    pattern = r"(async\s+def|def)\s+" + re.escape(old_name) + r"(\s*\()"
    replacement = r"\1 " + new_name + r"\2"

    new_function_code, num_replacements = re.subn(
        pattern, replacement, function_code, 1
    )

    if num_replacements == 0:
        return function_code

    return new_function_code


def update_list_tools_method(content: str, old_name: str, new_name: str) -> str:
    """
    Updates the list_tools method by renaming a function reference.

    This function uses regex to find the `list_tools` method and replace
    `self.old_name` with `self.new_name` within its return list, preserving
    surrounding code and formatting.

    Args:
        content: The full source code of the file as a string.
        old_name: The original name of the function to replace.
        new_name: The new name for the function.

    Returns:
        The updated file content with the function renamed in list_tools.
    """
    # Regex to find `self.old_name` followed by a comma, newline, or closing bracket
    # This ensures we only replace the specific tool reference in the list.
    pattern = r"(self\.)" + re.escape(old_name) + r"(?=\s*[,\]])"
    replacement = r"\1" + new_name

    # First, find the list_tools method definition to narrow the search area
    list_tools_match = re.search(
        r"def\s+list_tools\s*\([^)]*\):\s*return\s*\[[^\]]*\]", content, re.DOTALL
    )

    if not list_tools_match:
        return content

    list_tools_code = list_tools_match.group(0)

    # Perform the replacement only within the found method block
    updated_list_tools_code, num_replacements = re.subn(
        pattern, replacement, list_tools_code
    )

    if num_replacements > 0:
        return content.replace(list_tools_code, updated_list_tools_code)
    else:
        return content


def process_file(file_path: str, model: str = "perplexity/sonar") -> int:
    """
    Process a Python file to update docstrings and optionally rename functions.

    Args:
        file_path: Path to the Python file to process.
        model: The model to use for generating descriptions.

    Returns:
        Number of functions processed.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, encoding="utf-8") as f:
        original_content = f.read()

    functions = extract_functions_from_script(file_path)
    if not functions:
        return 0

    updated_content = original_content
    count = 0

    for function_name, function_code in functions:

        try:
            func_tree = ast.parse(function_code)
            func_node = func_tree.body[0]
            existing_docstring = ast.get_docstring(func_node, clean=True)
            _, rest_of_docstring = parse_existing_docstring(existing_docstring)
        except (SyntaxError, IndexError):
            continue

        # 1. Generate new description and check for suggested name
        output = generate_description(function_code, original_content, model)
        new_description = output.description.strip()
        # suggested_name = output.suggested_name

        if not new_description or "Error generating description" in new_description:
            continue

        # 2. Reconstruct the full docstring content
        reconstructed_docstring = new_description
        if rest_of_docstring:
            reconstructed_docstring += "\n\n" + rest_of_docstring

        # 3. Handle function renaming if suggested
        code_to_update = function_code
        # if suggested_name and suggested_name != function_name:
        #     print(f"  - Renaming function '{function_name}' to '{suggested_name}'")
        #     code_to_update = rename_function_in_code(code_to_update, function_name, suggested_name)
        #     is_renamed = True

        # 4. Insert the new docstring back into the (potentially renamed) function code
        updated_function_block = insert_docstring_into_function(
            code_to_update, reconstructed_docstring
        )

        # 5. If any changes were made, update the main content
        if updated_function_block != function_code:
            updated_content = updated_content.replace(
                function_code, updated_function_block
            )
            count += 1

            # 6. If the function was renamed, also update the list_tools method
            # if is_renamed:
            #     updated_content = update_list_tools_method(updated_content, function_name, suggested_name)

    if updated_content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
    else:
        pass

    return count


app = typer.Typer()


@app.command()
def docgen(
    file_path: Path = typer.Argument(..., help="Path to the Python file to process"),
    model: str = typer.Option(
        "gemini/gemini-2.5-pro",
        "--model",
        "-m",
        help="Model to use for generating docstrings",
    ),
):
    """
    Generate/update docstrings and function names in Python files using LLMs.

    This command uses litellm to generate high-quality docstring descriptions
    and suggest better function names, updating the file accordingly.
    """
    if not file_path.exists():
        console.print(f"[red]Error: File not found: {file_path}[/red]")
        raise typer.Exit(1)

    try:
        processed = process_file(str(file_path), model)
        console.print(f"[green]Successfully processed {processed} functions[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e


if __name__ == "__main__":
    app()
