import ast
import os

# List of applications to be converted to async
APPS = [
    "ahrefs",
    "airtable",
    "apollo",
    "asana",
    "aws_s3",
    "bill",  # not seeded
    "box",
    "braze",
    # "cal_com_v2",   # not seeded
    "calendly",
    "canva",
    "clickup",
    "coda",
    "confluence",  # not seeded
    "contentful",  # not seeded
    "crustdata",
    "dialpad",  # not seeded
    "digitalocean",
    "domain_checker",
    "e2b",
    "elevenlabs",
    "exa",
    "falai",
    "figma",
    "file_system",
    "firecrawl",
    "fireflies",
    "fpl",
    "ghost_content",
    "github",
    "gong",
    "google_calendar",
    "google_docs",
    "google_drive",
    "google_gemini",
    "google_mail",
    "google_searchconsole",
    "google_sheet",
    "hashnode",
    "heygen",
    "http_tools",
    # "hubspot",
    "jira",
    "klaviyo",
    "linkedin",
    "mailchimp",
    "markitdown",
    "miro",
    "ms_teams",
    "neon",
    "notion",
    "onedrive",
    "openai",
    "outlook",
    "perplexity",
    "pipedrive",  # not seeded
    "posthog",
    "reddit",
    "resend",
    "retell",
    "rocketlane",
    "scraper",
    "semanticscholar",
    "semrush",  # not seeded
    "sendgrid",
    "sentry",
    "serpapi",
    "sharepoint",
    "shopify",
    "shortcut",
    "slack",
    "spotify",  # not seeded
    "supabase",
    "tavily",
    "trello",
    "twilio",
    # "twitter",
    "whatsapp",
    "whatsapp_business",
    "wrike",  # not seeded
    "yahoo_finance",
    "youtube",
    "zenquotes",
]


class AsyncMethodCallConverter(ast.NodeTransformer):
    """
    An AST transformer that converts synchronous method calls to asynchronous ones
    within specified async tool functions.
    """

    def __init__(self, tool_functions):
        self.tool_functions = tool_functions
        self.current_function_is_tool = False

    def visit_AsyncFunctionDef(self, node):
        """
        Checks if the async function is a tool function and processes its body.
        """
        original_state = self.current_function_is_tool
        if node.name in self.tool_functions:
            self.current_function_is_tool = True

        self.generic_visit(node)

        self.current_function_is_tool = original_state
        return node

    def visit_Call(self, node):
        """
        Transforms method calls like `_get` to `await _async_get` inside tool functions.
        """
        if self.current_function_is_tool:
            if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
                if node.func.attr in ["_get", "_post", "_put", "_delete", "_patch"]:
                    node.func.attr = f"_async{node.func.attr}"
                    return ast.Await(value=node)

        return self.generic_visit(node)

    def visit_Return(self, node):
        """
        Transforms `return self._handle_response(response)` to
        `return await self._async_handle_response(response)`.
        """
        if self.current_function_is_tool and node.value:
            if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute):
                if (
                    node.value.func.attr == "_handle_response"
                    and isinstance(node.value.func.value, ast.Name)
                    and node.value.func.value.id == "self"
                ):
                    node.value.func.attr = "_async_handle_response"
                    return ast.Return(value=ast.Await(value=node.value))

        return self.generic_visit(node)


def get_tool_function_names(tree):
    """
    Extracts the names of the tool functions from the 'list_tools' method in the AST.
    """
    tool_functions = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "list_tools":
                    for statement in item.body:
                        if isinstance(statement, ast.Return) and isinstance(statement.value, (ast.List, ast.Tuple)):
                            for elt in statement.value.elts:
                                if isinstance(elt, ast.Attribute):
                                    tool_functions.add(elt.attr)
    return list(tool_functions)


def process_file(file_path):
    """
    Reads, transforms, and writes back the Python source file to make functions async.
    """
    with open(file_path, "r") as f:
        source = f.read()

    tree = ast.parse(source)
    tool_functions = get_tool_function_names(tree)

    if not tool_functions:
        print(f"No tool functions found in {file_path}")
        return

    converter = AsyncMethodCallConverter(tool_functions)
    new_tree = converter.visit(tree)
    ast.fix_missing_locations(new_tree)

    new_source = ast.unparse(new_tree)

    with open(file_path, "w") as f:
        f.write(new_source)
    print(f"Successfully converted method calls in {file_path} to async.")


def main():
    """
    Main function to process the applications listed in APPS.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "universal_mcp", "applications"))

    for app in APPS:
        app_path = os.path.join(base_path, app, "app.py")
        if os.path.exists(app_path):
            process_file(app_path)
        else:
            print(f"Could not find {app_path}")


if __name__ == "__main__":
    main()
