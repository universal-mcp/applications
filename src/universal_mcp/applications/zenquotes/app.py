from universal_mcp.applications.application import APIApplication


class ZenquotesApp(APIApplication):
    def __init__(self, **kwargs) -> None:
        super().__init__(name="zenquotes")

    async def get_random_quote(self) -> str:
        """
        Fetches a random inspirational quote from the Zen Quotes API via an HTTP request. It parses the JSON response to extract the quote and author, returning them as a single formatted string ('quote - author'). This function is the primary tool provided by the ZenquotesApp.

        Returns:
            A formatted string containing the quote and its author in the format 'quote - author'

        Raises:
            RequestException: If the HTTP request to the Zen Quotes API fails
            JSONDecodeError: If the API response contains invalid JSON
            IndexError: If the API response doesn't contain any quotes
            KeyError: If the quote data doesn't contain the expected 'q' or 'a' fields

        Tags:
            fetch, quotes, api, http, important
        """
        url = "https://zenquotes.io/api/random"
        response = await self._aget(url)
        data = response.json()
        quote = data[0]
        return {"quote": quote["q"], "author": quote["a"]}

    def list_tools(self):
        return [self.get_random_quote]
