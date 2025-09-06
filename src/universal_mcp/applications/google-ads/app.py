from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class GoogleAdsApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """

    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="google-ads", integration=integration, **kwargs)

    def run(self):
        """
        Example tool implementation.
        """
        return "Task completed successfully."

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.run]
