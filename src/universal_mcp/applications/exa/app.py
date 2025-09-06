from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class ExaApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="exa", integration=integration, **kwargs)
        self.base_url = "https://api.exa.ai"

    def search(
        self,
        query,
        useAutoprompt=None,
        type=None,
        category=None,
        numResults=None,
        includeDomains=None,
        excludeDomains=None,
        startCrawlDate=None,
        endCrawlDate=None,
        startPublishedDate=None,
        endPublishedDate=None,
        includeText=None,
        excludeText=None,
        contents=None,
    ) -> dict[str, Any]:
        """
        Searches for data using the specified criteria and returns a list of results.

        Args:
            query (string): The query string for the search. Example: 'Latest developments in LLM capabilities'.
            useAutoprompt (boolean): Autoprompt converts your query to an Exa-style query. Enabled by default for auto search, optional for neural search, and not available for keyword search. Example: 'True'.
            type (string): The type of search. Neural uses an embeddings-based model, keyword is google-like SERP. Default is auto, which automatically decides between keyword and neural. Example: 'auto'.
            category (string): A data category to focus on. Example: 'research paper'.
            numResults (integer): Number of results to return (up to thousands of results available for custom plans) Example: '10'.
            includeDomains (array): List of domains to include in the search. If specified, results will only come from these domains. Example: "['arxiv.org', 'paperswithcode.com']".
            excludeDomains (array): List of domains to exclude from search results. If specified, no results will be returned from these domains.
            startCrawlDate (string): Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled after this date. Must be specified in ISO 8601 format. Example: '2023-01-01'.
            endCrawlDate (string): Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled before this date. Must be specified in ISO 8601 format. Example: '2023-12-31'.
            startPublishedDate (string): Only links with a published date after this will be returned. Must be specified in ISO 8601 format. Example: '2023-01-01'.
            endPublishedDate (string): Only links with a published date before this will be returned. Must be specified in ISO 8601 format. Example: '2023-12-31'.
            includeText (array): List of strings that must be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words. Example: "['large language model']".
            excludeText (array): List of strings that must not be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words. Example: "['course']".
            contents (object): contents

        Returns:
            dict[str, Any]: OK

        Tags:
            important
        """
        request_body = {
            "query": query,
            "useAutoprompt": useAutoprompt,
            "type": type,
            "category": category,
            "numResults": numResults,
            "includeDomains": includeDomains,
            "excludeDomains": excludeDomains,
            "startCrawlDate": startCrawlDate,
            "endCrawlDate": endCrawlDate,
            "startPublishedDate": startPublishedDate,
            "endPublishedDate": endPublishedDate,
            "includeText": includeText,
            "excludeText": excludeText,
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/search"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_similar(
        self,
        url,
        numResults=None,
        includeDomains=None,
        excludeDomains=None,
        startCrawlDate=None,
        endCrawlDate=None,
        startPublishedDate=None,
        endPublishedDate=None,
        includeText=None,
        excludeText=None,
        contents=None,
    ) -> dict[str, Any]:
        """
        Finds and returns similar items using the API at "/findSimilar" via the POST method.

        Args:
            url (string): The url for which you would like to find similar links. Example: 'https://arxiv.org/abs/2307.06435'.
            numResults (integer): Number of results to return (up to thousands of results available for custom plans) Example: '10'.
            includeDomains (array): List of domains to include in the search. If specified, results will only come from these domains. Example: "['arxiv.org', 'paperswithcode.com']".
            excludeDomains (array): List of domains to exclude from search results. If specified, no results will be returned from these domains.
            startCrawlDate (string): Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled after this date. Must be specified in ISO 8601 format. Example: '2023-01-01'.
            endCrawlDate (string): Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled before this date. Must be specified in ISO 8601 format. Example: '2023-12-31'.
            startPublishedDate (string): Only links with a published date after this will be returned. Must be specified in ISO 8601 format. Example: '2023-01-01'.
            endPublishedDate (string): Only links with a published date before this will be returned. Must be specified in ISO 8601 format. Example: '2023-12-31'.
            includeText (array): List of strings that must be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words. Example: "['large language model']".
            excludeText (array): List of strings that must not be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words. Example: "['course']".
            contents (object): contents

        Returns:
            dict[str, Any]: OK

        Tags:
            important
        """
        request_body = {
            "url": url,
            "numResults": numResults,
            "includeDomains": includeDomains,
            "excludeDomains": excludeDomains,
            "startCrawlDate": startCrawlDate,
            "endCrawlDate": endCrawlDate,
            "startPublishedDate": startPublishedDate,
            "endPublishedDate": endPublishedDate,
            "includeText": includeText,
            "excludeText": excludeText,
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/findSimilar"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_contents(
        self,
        urls,
        ids=None,
        text=None,
        highlights=None,
        summary=None,
        livecrawl=None,
        livecrawlTimeout=None,
        subpages=None,
        subpageTarget=None,
        extras=None,
    ) -> dict[str, Any]:
        """
        Creates new content entries via a POST request to the "/contents" endpoint.

        Args:
            urls (array): Array of URLs to crawl (backwards compatible with 'ids' parameter). Example: "['https://arxiv.org/pdf/2307.06435']".
            ids (array): Deprecated - use 'urls' instead. Array of document IDs obtained from searches. Example: "['https://arxiv.org/pdf/2307.06435']".
            text (string): text
            highlights (object): Text snippets the LLM identifies as most relevant from each page.
            summary (object): Summary of the webpage
            livecrawl (string): Options for livecrawling pages.
        'never': Disable livecrawling (default for neural search).
        'fallback': Livecrawl when cache is empty (default for keyword search).
        'always': Always livecrawl.
        'auto': Use an LLM to detect if query needs real-time content.
         Example: 'always'.
            livecrawlTimeout (integer): The timeout for livecrawling in milliseconds. Example: '1000'.
            subpages (integer): The number of subpages to crawl. The actual number crawled may be limited by system constraints. Example: '1'.
            subpageTarget (string): Keyword to find specific subpages of search results. Can be a single string or an array of strings, comma delimited. Example: 'sources'.
            extras (object): Extra parameters to pass.

        Returns:
            dict[str, Any]: OK

        Tags:
            important
        """
        request_body = {
            "urls": urls,
            "ids": ids,
            "text": text,
            "highlights": highlights,
            "summary": summary,
            "livecrawl": livecrawl,
            "livecrawlTimeout": livecrawlTimeout,
            "subpages": subpages,
            "subpageTarget": subpageTarget,
            "extras": extras,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/contents"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def answer(self, query, stream=None, text=None, model=None) -> dict[str, Any]:
        """
        Provides an answer to a query using the API endpoint at "/answer" via the POST method.

        Args:
            query (string): The question or query to answer. Example: 'What is the latest valuation of SpaceX?'.
            stream (boolean): If true, the response is returned as a server-sent events (SSS) stream.
            text (boolean): If true, the response includes full text content in the search results
            model (string): The search model to use for the answer. Exa passes only one query to exa, while exa-pro also passes 2 expanded queries to our search model.

        Returns:
            dict[str, Any]: OK

        Tags:
            important
        """
        request_body = {
            "query": query,
            "stream": stream,
            "text": text,
            "model": model,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/answer"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [self.search, self.find_similar, self.get_contents, self.answer]
