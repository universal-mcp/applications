from typing import Any, Literal

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class PerplexityApp(APIApplication):
    def __init__(self, integration: Integration | None = None) -> None:
        super().__init__(name="perplexity", integration=integration)
        self.base_url = "https://api.perplexity.ai"

    def answer_with_search(
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
    ) -> dict[str, Any] | str:
        """
        Queries the Perplexity Chat Completions API for a web-search-grounded answer. It sends the user's prompt and model parameters to the `/chat/completions` endpoint, then parses the response to return the synthesized content and a list of supporting source citations, ideal for real-time information retrieval.

        Args:
            query: The search query or question to ask. For example: "What are the latest developments in AI regulation?"
            model: The Perplexity model to use.
            temperature: Controls randomness in the model's output. Higher values make the output more random, lower values make it more deterministic. Defaults to 1.
            system_prompt: The initial system message to guide the model's behavior.

        Returns:
            A dictionary containing the generated 'content' (str) and a list of 'citations' (list) from the web search.

        Raises:
            AuthenticationError: Raised when API authentication fails due to missing or invalid credentials.
            HTTPError: Raised when the API request fails or returns an error status.

        Tags:
            search, web, research, citations, current events, important
        """
        endpoint = f"{self.base_url}/chat/completions"
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": query})
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            # "max_tokens": 512,
        }
        data = self._post(endpoint, data=payload)
        response = data.json()
        content = response["choices"][0]["message"]["content"]
        citations = response.get("citations", [])
        return {"content": content, "citations": citations}

    def list_tools(self):
        return [
            self.answer_with_search,
        ]
