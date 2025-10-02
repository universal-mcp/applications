from typing import Annotated

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from browser_use_sdk import BrowserUse


class BrowserUseApp(APIApplication):
    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="browser_use", integration=integration, **kwargs)
        self._browser_client = None

    @property
    def browser_client(self) -> BrowserUse:
        if self._browser_client is not None:
            return self._browser_client
        if not self.integration:
            raise ValueError("Integration is required but not provided")
        credentials = self.integration.get_credentials()
        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )
        if not api_key:
            raise ValueError("API key not found in integration credentials")
        self._browser_client = BrowserUse(api_key=api_key)
        return self._browser_client

    async def browser_task(
        self,
        task: Annotated[str, "What you want the browser to do"],
        max_steps: Annotated[int, "Max actions to take (1-10, default: 8)"] = 8,
        llm: Annotated[str, "The LLM to use for the task"] = "gpt-4.1",
    ) -> dict:
        """
        Creates and runs a browser automation task.

        Args:
            task (str): The detailed description of the task for the browser to perform.
            max_steps (int, optional): The maximum number of actions the browser can take. Defaults to 8.
            llm (str, optional): The language model to use for interpreting the task. Defaults to "gpt-4.1".

        Returns:
            dict: The result of the completed task, including output and other metadata.
        """
        created_task = self.browser_client.tasks.create_task(
            llm=llm, task=task, max_steps=max_steps
        )
        result = created_task.complete()
        return result.model_dump()

    async def get_browser_task_status(
        self,
        task_id: Annotated[str, "Task ID to check"],
    ) -> dict:
        """
        Checks task progress with smart polling.

        Args:
            task_id (str): The ID of the task to check.

        Returns:
            dict: The current status and details of the task.
        """
        task = self.browser_client.tasks.get_task(task_id)
        return task.model_dump()

    def list_tools(self):
        return [self.browser_task, self.get_browser_task_status]
