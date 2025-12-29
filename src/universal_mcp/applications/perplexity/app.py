from typing import Any, Literal
from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration

try:
    from perplexity import AsyncPerplexity
except ImportError:
    AsyncPerplexity = None  # type: ignore
    logger.error("Failed to import perplexity. Please ensure 'perplexityai' is installed.")


class PerplexityApp(APIApplication):
    def __init__(self, integration: Integration | None = None) -> None:
        super().__init__(name="perplexity", integration=integration)
        self._perplexity_api_key: str | None = None
        if AsyncPerplexity is None:
            logger.warning("Perplexity SDK is not available. Perplexity tools will not function.")

    async def get_perplexity_api_key(self) -> str:
        """
        A property that lazily retrieves and caches the Perplexity API key from the configured integration.
        """
        if self._perplexity_api_key is None:
            if not self.integration:
                logger.error(f"{self.name.capitalize()} App: Integration not configured.")
                raise NotAuthorizedError(f"Integration not configured for {self.name.capitalize()} App. Cannot retrieve API key.")
            try:
                credentials = await self.integration.get_credentials_async()
            except NotAuthorizedError as e:
                logger.error(f"{self.name.capitalize()} App: Authorization error when fetching credentials: {e.message}")
                raise
            except Exception as e:
                logger.error(f"{self.name.capitalize()} App: Unexpected error when fetching credentials: {e}", exc_info=True)
                raise NotAuthorizedError(f"Failed to get {self.name.capitalize()} credentials: {e}")
            
            # Check for common key names
            api_key = credentials.get("api_key") or credentials.get("API_KEY") or credentials.get("apiKey") or credentials.get("PPLX_API_KEY")
            
            if not api_key:
                logger.error(f"{self.name.capitalize()} App: API key not found in credentials.")
                action_message = f"API key for {self.name.capitalize()} is missing. Please ensure it's set in the store."
                if hasattr(self.integration, "authorize") and callable(self.integration.authorize):
                    try:
                        auth_details = self.integration.authorize()
                        if isinstance(auth_details, str):
                            action_message = auth_details
                        elif isinstance(auth_details, dict) and "url" in auth_details:
                            action_message = f"Please authorize via: {auth_details['url']}"
                        elif isinstance(auth_details, dict) and "message" in auth_details:
                            action_message = auth_details["message"]
                    except Exception as auth_e:
                        logger.warning(f"Could not retrieve specific authorization action for {self.name.capitalize()}: {auth_e}")
                raise NotAuthorizedError(action_message)
            self._perplexity_api_key = api_key
            logger.info(f"{self.name.capitalize()} API Key successfully retrieved and cached.")
        assert self._perplexity_api_key is not None
        return self._perplexity_api_key

    async def _get_client(self) -> AsyncPerplexity:
        """
        Initializes and returns the Perplexity client after ensuring API key is set.
        """
        if AsyncPerplexity is None:
            logger.error("Perplexity SDK is not available.")
            raise ToolError("Perplexity SDK is not installed or failed to import.")
        current_api_key = await self.get_perplexity_api_key()
        return AsyncPerplexity(api_key=current_api_key)

    async def answer_with_search(
        self,
        query: str,
        model: Literal[
            "r1-1776",
            "sonar",
            "sonar-pro",
            "sonar-reasoning",
            "sonar-reasoning-pro",
            "sonar-deep-research",
        ] = "sonar-pro",
        temperature: float = 1,
        system_prompt: str = "You are a helpful AI assistant that answers questions using real-time information from the web.",
        response_format: dict[str, Any] | None = None,
        json_schema: dict[str, Any] | None = None,
        regex: str | None = None,
    ) -> dict[str, Any] | str:
        """
        Queries the Perplexity Chat Completions API for a web-search-grounded answer. It sends the user's prompt and model parameters to the `/chat/completions` endpoint, then parses the response to return the synthesized content and a list of supporting source citations.

        This method supports **Structured Outputs** using `json_schema` or `regex` to enforce specific response formats.

        Args:
            query: The search query or question to ask.
            model: The Perplexity model to use.
            temperature: Controls randomness in the model's output.
            system_prompt: The initial system message to guide the model's behavior.
            response_format: A dict specifying the response format (e.g. `{"type": "json_schema", ...}`).
            json_schema: A dictionary for the JSON schema to enforce (shortcut for `response_format`).
            regex: A regex string to enforce (shortcut for `response_format`, only available for 'sonar').

        Returns:
            A dictionary containing the generated 'content' (str) and a list of 'citations' (list) from the web search.

        Examples:
            **1. Financial Analysis with JSON Schema**
            ```python
            from pydantic import BaseModel
            class FinancialMetrics(BaseModel):
                company: str
                revenue: float
                net_income: float

            app.answer_with_search(
                "Analyze Apple's latest earnings",
                model="sonar-pro",
                json_schema={"schema": FinancialMetrics.model_json_schema()}
            )
            ```

            **2. Extract Contact Information with Regex**
            ```python
            app.answer_with_search(
                "Find the investor relations email for Tesla",
                model="sonar",
                regex=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
            )
            ```

        Raises:
            AuthenticationError: Raised when API authentication fails.
            HTTPError: Raised when the API request fails.
            ValueError: If conflicting structured output parameters are provided.

        Tags:
            chat, answer, search, web, research, citations, structured_output, extraction, important
        """
        if sum(x is not None for x in [response_format, json_schema, regex]) > 1:
            raise ValueError("Only one of 'response_format', 'json_schema', or 'regex' can be provided.")

        if json_schema:
            response_format = {"type": "json_schema", "json_schema": json_schema}
        elif regex:
            response_format = {"type": "regex", "regex": {"regex": regex}}

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": query})

        client = await self._get_client()
        # client.chat.completions.create supports response_format
        kwargs: dict[str, Any] = {
            "model": model,
            "messages": messages,  # type: ignore
            "temperature": temperature,
        }
        if response_format:
            kwargs["response_format"] = response_format

        response = await client.chat.completions.create(**kwargs)
        
        # Assuming response structure matches OpenAI-like usage or Custom as per SDK docs
        content = response.choices[0].message.content
        citations = getattr(response, "citations", [])
        return {"content": content, "citations": citations}

    async def search(
        self,
        query: str,
        max_results: int = 5,
        country: str = "US",
    ) -> list[dict[str, Any]]:
        """
        Performs a real-time web search using Perplexity AI to answer a query with up-to-date information and citations.
        This tool is ideal for questions about current events, facts, or any topic that requires access to the latest information from the internet.

        Args:
            query: The search query or question to ask.
            max_results: Maximum number of results to return.
            country: ISO 3166-1 alpha-2 country code for localized results.

        Returns:
            A list of search results.

        Tags:
            search, web, research, citations, current events, important
        """
        client = await self._get_client()
        response = await client.search.create(
            query=query,
            max_results=max_results,
            country=country,
        )
        results = []
        for result in response.results:
            results.append({
                "title": result.title,
                "url": result.url,
                "snippet": result.snippet,
                "date": result.date,
            })
        return results

    def list_tools(self):
        return [self.answer_with_search, self.search]
