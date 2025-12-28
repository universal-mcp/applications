import ast
import os

# List of applications to be converted to async
APPS = [
    "hubspot"
]


class AsyncHttpConverter(ast.NodeTransformer):
    """
    An AST transformer that converts synchronous HTTP calls to asynchronous ones
    within specified tool functions.
    """

    def __init__(self, tool_functions):
        self.tool_functions = tool_functions
        self.current_function = None

    def visit_FunctionDef(self, node):
        if node.name in self.tool_functions:
            self.current_function = node.name
            self.generic_visit(node)
            self.current_function = None
        return node

    def visit_AsyncFunctionDef(self, node):
        if node.name in self.tool_functions:
            self.current_function = node.name
            self.generic_visit(node)
            self.current_function = None
        return node

    def visit_Call(self, node):
        if self.current_function and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
                sync_method_names = {"_get", "_post", "_put", "_delete", "_patch"}
                if node.func.attr in sync_method_names:
                    async_method_name = f"_a{node.func.attr[1:]}"
                    new_func = ast.Attribute(value=node.func.value, attr=async_method_name, ctx=node.func.ctx)
                    new_call = ast.Call(func=new_func, args=node.args, keywords=node.keywords)
                    return ast.Await(value=new_call)
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
                        if isinstance(statement, ast.Return):
                            for elt in statement.value.elts:
                                if isinstance(elt, ast.Attribute):
                                    tool_functions.add(elt.attr)
    return list(tool_functions)


def process_file(file_path):
    """
    Reads, transforms, and writes back the Python source file to make HTTP calls async.
    """
    with open(file_path, "r") as f:
        source = f.read()

    tree = ast.parse(source)
    tool_functions = get_tool_function_names(tree)

    if not tool_functions:
        print(f"No tool functions found in {file_path}")
        return

    converter = AsyncHttpConverter(tool_functions)
    new_tree = converter.visit(tree)
    ast.fix_missing_locations(new_tree)

    new_source = ast.unparse(new_tree)

    with open(file_path, "w") as f:
        f.write(new_source)
    print(f"Successfully converted HTTP calls in {file_path} to async.")


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
