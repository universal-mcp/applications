from typing import Annotated, Any

from loguru import logger

try:
    from e2b_code_interpreter import Sandbox

except ImportError:
    Sandbox = None
    logger.error(
        "Failed to import E2B Sandbox. Please ensure 'e2b_code_interpreter' is installed."
    )

from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration


class E2bApp(APIApplication):
    """
    Application for interacting with the E2B (Code Interpreter Sandbox) platform.
    Provides tools to execute Python code in a sandboxed environment.
    Authentication is handled by the configured Integration, fetching the API key.
    """

    def __init__(self, integration: Integration | None = None, **kwargs: Any) -> None:
        super().__init__(name="e2b", integration=integration, **kwargs)
        self._e2b_api_key: str | None = None  # Cache for the API key
        if Sandbox is None:
            logger.warning(
                "E2B Sandbox SDK is not available. E2B tools will not function."
            )

    @property
    def e2b_api_key(self) -> str:
        """
        Retrieves and caches the E2B API key from the integration.
        Raises NotAuthorizedError if the key cannot be obtained.
        """
        if self._e2b_api_key is None:
            if not self.integration:
                logger.error("E2B App: Integration not configured.")
                raise NotAuthorizedError(
                    "Integration not configured for E2B App. Cannot retrieve API key."
                )

            try:
                credentials = self.integration.get_credentials()
            except NotAuthorizedError as e:
                logger.error(
                    f"E2B App: Authorization error when fetching credentials: {e.message}"
                )
                raise  # Re-raise the original NotAuthorizedError
            except Exception as e:
                logger.error(
                    f"E2B App: Unexpected error when fetching credentials: {e}",
                    exc_info=True,
                )
                raise NotAuthorizedError(f"Failed to get E2B credentials: {e}")

            api_key = (
                credentials.get("api_key")
                or credentials.get("API_KEY")  # Check common variations
                or credentials.get("apiKey")
            )

            if not api_key:
                logger.error("E2B App: API key not found in credentials.")
                action_message = "API key for E2B is missing. Please ensure it's set in the store via MCP frontend or configuration."
                if hasattr(self.integration, "authorize") and callable(
                    self.integration.authorize
                ):
                    try:
                        auth_details = self.integration.authorize()
                        if isinstance(auth_details, str):
                            action_message = auth_details
                        elif isinstance(auth_details, dict) and "url" in auth_details:
                            action_message = (
                                f"Please authorize via: {auth_details['url']}"
                            )
                        elif (
                            isinstance(auth_details, dict) and "message" in auth_details
                        ):
                            action_message = auth_details["message"]
                    except Exception as auth_e:
                        logger.warning(
                            f"Could not retrieve specific authorization action for E2B: {auth_e}"
                        )
                raise NotAuthorizedError(action_message)

            self._e2b_api_key = api_key
            logger.info("E2B API Key successfully retrieved and cached.")
        return self._e2b_api_key

    def _format_execution_output(self, logs: Any) -> str:
        """Helper function to format the E2B execution logs nicely."""
        output_parts = []

        # Safely access stdout and stderr
        stdout_log = getattr(logs, "stdout", [])
        stderr_log = getattr(logs, "stderr", [])

        if stdout_log:
            stdout_content = "".join(stdout_log).strip()
            if stdout_content:
                output_parts.append(f"{stdout_content}")

        if stderr_log:
            stderr_content = "".join(stderr_log).strip()
            if stderr_content:
                output_parts.append(f"--- ERROR ---\n{stderr_content}")

        if not output_parts:
            return "Execution finished with no output (stdout/stderr)."
        return "\n\n".join(output_parts)

    def execute_python_code(
        self, code: Annotated[str, "The Python code to execute."]
    ) -> str:
        """
        Executes Python code in a sandbox environment and returns the formatted output.

        Args:
            code: String containing the Python code to be executed in the sandbox.

        Returns:
            A string containing the formatted execution output/logs from running the code.

        Raises:
            ToolError: When there are issues with sandbox initialization or code execution,
                       or if the E2B SDK is not installed.
            NotAuthorizedError: When API key authentication fails during sandbox setup.
            ValueError: When provided code string is empty or invalid.

        Tags:
            execute, sandbox, code-execution, security, important
        """
        if Sandbox is None:
            logger.error(
                "E2B Sandbox SDK is not available. Cannot execute_python_code."
            )
            raise ToolError(
                "E2B Sandbox SDK (e2b_code_interpreter) is not installed or failed to import."
            )

        if not code or not isinstance(code, str):
            raise ValueError("Provided code must be a non-empty string.")

        logger.info("Attempting to execute Python code in E2B Sandbox.")
        try:
            current_api_key = self.e2b_api_key

            with Sandbox(api_key=current_api_key) as sandbox:
                logger.info(
                    f"E2B Sandbox (ID: {sandbox.sandbox_id}) initialized. Running code."
                )
                execution = sandbox.run_code(
                    code=code
                )  # run_python is the method in e2b-code-interpreter
                result = self._format_execution_output(
                    execution.logs
                )  # execution_result directly has logs
                logger.info("E2B code execution successful.")
                return result
        except NotAuthorizedError:  # Re-raise if caught from self.e2b_api_key
            raise
        except Exception as e:
            if (
                "authentication" in str(e).lower()
                or "api key" in str(e).lower()
                or "401" in str(e)
                or "unauthorized" in str(e).lower()
            ):
                logger.error(
                    f"E2B authentication/authorization error: {e}", exc_info=True
                )
                raise NotAuthorizedError(
                    f"E2B authentication failed or access denied: {e}"
                )
            logger.error(f"Error during E2B code execution: {e}", exc_info=True)
            raise ToolError(f"E2B code execution failed: {e}")

    def list_tools(self) -> list[callable]:
        """Lists the tools available from the E2bApp."""
        return [
            self.execute_python_code,
        ]
