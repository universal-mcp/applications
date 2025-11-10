import ast
import os

# List of applications to be checked for internal calls
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
    "hubspot",
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
    "twitter",
    "whatsapp",
    "whatsapp_business",
    "wrike",  # not seeded
    "yahoo_finance",
    "youtube",
    "zenquotes",
]


class InternalCallFinder(ast.NodeVisitor):
    """
    An AST visitor that finds calls to tool functions from within other tool functions.
    """

    def __init__(self, tool_functions):
        self.tool_functions = set(tool_functions)
        self.current_function = None
        self.internal_calls = []

    def visit_FunctionDef(self, node):
        if node.name in self.tool_functions:
            self.current_function = node.name
            self.generic_visit(node)
            self.current_function = None
        else:
            self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        if node.name in self.tool_functions:
            self.current_function = node.name
            self.generic_visit(node)
            self.current_function = None
        else:
            self.generic_visit(node)

    def visit_Call(self, node):
        if self.current_function:
            if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
                called_func_name = node.func.attr
                if called_func_name in self.tool_functions and called_func_name != self.current_function:
                    self.internal_calls.append({"caller": self.current_function, "callee": called_func_name})
        self.generic_visit(node)


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
                        if isinstance(statement, ast.Return):
                            if isinstance(statement.value, (ast.List, ast.Tuple)):
                                for elt in statement.value.elts:
                                    if isinstance(elt, ast.Attribute):
                                        tool_functions.add(elt.attr)
    return list(tool_functions)


def process_file(file_path):
    """
    Reads and processes a single app.py file to find internal calls.
    """
    with open(file_path, "r") as f:
        source = f.read()
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"Error parsing {file_path}: {e}")
        return []

    tool_functions = get_tool_function_names(tree)
    if not tool_functions:
        return []

    finder = InternalCallFinder(tool_functions)
    finder.visit(tree)
    return finder.internal_calls


def main():
    """
    Main function to iterate through specified applications and check for internal calls.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "universal_mcp", "applications"))

    apps_with_internal_calls = {}

    for app in APPS:
        app_path = os.path.join(base_path, app, "app.py")
        if os.path.exists(app_path):
            internal_calls = process_file(app_path)
            if internal_calls:
                apps_with_internal_calls[app] = internal_calls
        else:
            print(f"Could not find {app_path} for application {app}")

    if apps_with_internal_calls:
        print("Applications with internal tool function calls:")
        for app, calls in apps_with_internal_calls.items():
            print(f"- {app}:")
            unique_calls = {(call["caller"], call["callee"]) for call in calls}
            for caller, callee in sorted(list(unique_calls)):
                print(f"  - '{caller}' calls '{callee}'")
    else:
        print("No applications with internal tool function calls found in the specified APPS list.")


if __name__ == "__main__":
    main()
