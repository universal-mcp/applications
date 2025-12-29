from typing import Annotated, Literal

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from browser_use_sdk import AsyncBrowserUse


class BrowserUseApp(APIApplication):
    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="browser_use", integration=integration, **kwargs)
        self._browser_client = None

    async def get_client(self) -> AsyncBrowserUse:
        if self._browser_client is not None:
            return self._browser_client
        if not self.integration:
            raise ValueError("Integration is required but not provided")
        credentials = await self.integration.get_credentials_async()
        api_key = credentials.get("api_key") or credentials.get("API_KEY") or credentials.get("apiKey")
        if not api_key:
            raise ValueError("API key not found in integration credentials")
        self._browser_client = AsyncBrowserUse(api_key=api_key)
        return self._browser_client

    async def browser_task(
        self,
        task: Annotated[str, "The objective of the task"],
        max_steps: Annotated[int, "Max actions to take (default: 8)"] = 8,
        llm: Annotated[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "o4-mini",
                "o3",
                "gemini-2.5-flash",
                "gemini-2.5-pro",
                "claude-sonnet-4-20250514",
                "gpt-4o",
                "gpt-4o-mini",
                "llama-4-maverick-17b-128e-instruct",
                "claude-3-7-sonnet-20250219",
            ],
            "The LLM to use",
        ] = "gpt-4o",
        session_id: Annotated[str | None, "Session ID to continue an existing session"] = None,
    ) -> dict:
        """
        Creates and starts a browser automation task in the background. Unlike synchronous tools, this returns immediately with a Task ID so the agent does not block while the browser works. You must use `get_browser_task_status` to check progress and retrieve the final result.

        Args:
            task (str): The detailed description of the task for the browser to perform.
            max_steps (int, optional): The maximum number of actions the browser can take. Defaults to 8.
            llm (str, optional): The language model to use. Defaults to "gpt-4o".
            session_id (str, optional): The ID of an existing session to use.

        Returns:
            dict: The task creation details including the task ID.
        
        Tags:
            browser, automation, background, task, web, research, create, important
        """
        client = await self.get_client()
        created_task = await client.tasks.create_task(
            llm=llm, task=task, max_steps=max_steps, session_id=session_id
        )

        return created_task.model_dump()

    async def get_browser_task_status(
        self,
        task_id: Annotated[str, "Task ID to check"],
    ) -> dict:
        """
        Checks the status of a browser automation task. Use this to poll for completion and retrieve the final output of a background task.
        
        Args:
            task_id (str): The ID of the task to check.

        Returns:
            dict: The current task details including status ('created', 'running', 'completed', 'stopped', 'failed') and output (if completed).

        Tags:
            status, poll, browser, task, monitoring, output, important
        """
        client = await self.get_client()
        task = await client.tasks.get_task(task_id)
        return task.model_dump()

    async def list_tasks(
        self,
        page_size: Annotated[int, "Number of tasks to return (default: 10)"] = 10,
    ) -> dict:
        """
        Lists recent browser automation tasks. Useful for finding lost task IDs or auditing recent activity.

        Args:
            page_size (int, optional): The number of tasks to retrieve. Defaults to 10.

        Returns:
            dict: A list of tasks with their basic details.

        Tags:
            list, history, browser, tasks, audit
        """
        client = await self.get_client()
        tasks = await client.tasks.list_tasks(page_size=page_size)
        return tasks.model_dump()

    async def stop_task(
        self,
        task_id: Annotated[str, "Task ID to stop"],
    ) -> dict:
        """
        Stops a running browser automation task. Use this to cancel a stuck or long-running task.

        Args:
            task_id (str): The ID of the task to stop.

        Returns:
            dict: The updated task details showing the stopped status.

        Tags:
            stop, cancel, browser, task, control
        """
        client = await self.get_client()
        updated_task = await client.tasks.update_task(task_id, action="stop")
        return updated_task.model_dump()

    def list_tools(self):
        return [
            self.browser_task,
            self.get_browser_task_status,
            self.list_tasks,
            self.stop_task,
        ]
