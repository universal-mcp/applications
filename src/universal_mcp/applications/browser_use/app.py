from typing import Annotated

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from browser_use import BrowserUseClient


class BrowserUseApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="browser_use", integration=integration, **kwargs)
        self._client = None

    @property
    def client(self) -> BrowserUseClient:
        if self._client is not None:
            return self._client
        credentials = self.integration.get_credentials()
        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )
        if not api_key:
            raise ValueError("API key not found in integration credentials")
        self._client = BrowserUseClient(api_key=api_key)
        return self._client

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
        created_task = self.client.tasks.create_task(
            llm=llm, task=task, max_steps=max_steps
        )
        result = created_task.complete()
        return result.to_dict()

    async def get_browser_task_status(
        self,
        task_id: Annotated[str, "Task ID to check"],
        enable_polling: Annotated[bool, "Auto-poll for 28s (default: true)"] = True,
    ) -> dict:
        """
        Checks task progress with smart polling.

        Args:
            task_id (str): The ID of the task to check.
            enable_polling (bool, optional): If true, polls for the task status for up to 28 seconds. Defaults to True.

        Returns:
            dict: The current status and details of the task.
        """
        if enable_polling:
            task = self.client.tasks.get(task_id)
            result = task.poll()
            return result.to_dict()
        else:
            task = self.client.tasks.get(task_id)
            return task.to_dict()

    def list_tools(self):
        return [self.browser_task, self.get_browser_task_status]
