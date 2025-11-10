import ast
import os

# List of applications to be converted to async
APPS = [
    "whatsapp",
    "whatsapp_business",
    "wrike",  # not seeded
    "yahoo_finance",
    "youtube",
    "zenquotes",
]


class AsyncConverter(ast.NodeTransformer):
    """
    An AST transformer that converts specified synchronous functions to asynchronous ones.
    """

    def __init__(self, tool_functions):
        self.tool_functions = tool_functions

    def visit_FunctionDef(self, node):
        """
        Transforms a synchronous function definition to an asynchronous one
        if its name is in the list of tool functions.
        """
        if node.name in self.tool_functions:
            # Convert the function to an async function
            return ast.AsyncFunctionDef(
                name=node.name,
                args=node.args,
                body=node.body,
                decorator_list=node.decorator_list,
                returns=node.returns,
                type_comment=getattr(node, "type_comment", None),
            )
        return node


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

    converter = AsyncConverter(tool_functions)
    new_tree = converter.visit(tree)
    ast.fix_missing_locations(new_tree)

    new_source = ast.unparse(new_tree)

    with open(file_path, "w") as f:
        f.write(new_source)
    print(f"Successfully converted functions in {file_path} to async.")


def main():
    """
    Main function to process the applications listed in APPS.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "universal_mcp", "applications"))

    for app in APPS:
        app_path = os.path.join(base_path, app, "app.py")
        # app_path = "/Users/ankitranjan/Work/applications/src/universal_mcp/applications/hubspot/api_segments/marketing_api.py"
        if os.path.exists(app_path):
            process_file(app_path)
        else:
            print(f"Could not find {app_path}")


if __name__ == "__main__":
    main()
