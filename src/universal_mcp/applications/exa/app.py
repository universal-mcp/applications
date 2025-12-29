from typing import Any, Literal

from loguru import logger

try:
    from exa_py import AsyncExa

    ExaClient: type[AsyncExa] | None = AsyncExa
except ImportError:
    ExaClient = None
    logger.error("Failed to import Exa. Please ensure 'exa-py' is installed.")

from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration


class ExaApp(APIApplication):
    """
    Application for interacting with the Exa API (exa.ai) using the official SDK.
    Provides advanced search, find similar links, page contents retrieval,
    knowledge synthesis (answer), and multi-step research tasks.
    """

    def __init__(self, integration: Integration | None = None, **kwargs: Any) -> None:
        super().__init__(name="exa", integration=integration, **kwargs)
        self._exa_client: AsyncExa | None = None

    async def get_exa_client(self) -> AsyncExa:
        """
        Lazily initializes and returns the Exa client.
        """
        if self._exa_client is None:
            if ExaClient is None:
                raise ToolError("Exa SDK (exa-py) is not installed.")

            if not self.integration:
                raise NotAuthorizedError("Exa App: Integration not configured.")

            credentials = await self.integration.get_credentials_async()
            api_key = credentials.get("api_key") or credentials.get("API_KEY") or credentials.get("apiKey")

            if not api_key:
                raise NotAuthorizedError("Exa API key not found in credentials.")

            self._exa_client = ExaClient(api_key=api_key)
            logger.info("Exa client successfully initialized.")

        return self._exa_client

    def _to_serializable(self, obj: Any) -> Any:
        """
        Recursively converts objects to dictionaries for JSON serialization.
        """
        if isinstance(obj, list):
            return [self._to_serializable(item) for item in obj]
        if hasattr(obj, "to_dict"):
            return obj.to_dict()
        if hasattr(obj, "dict"):
            return obj.dict()
        if hasattr(obj, "__dict__"):
            return {k: self._to_serializable(v) for k, v in obj.__dict__.items() if not k.startswith("_")}
        return obj

    async def search(  # noqa: PLR0913
        self,
        query: str,
        num_results: int | None = 10,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        start_crawl_date: str | None = None,
        end_crawl_date: str | None = None,
        start_published_date: str | None = None,
        end_published_date: str | None = None,
        type: Literal["auto", "neural", "fast", "deep", "hybrid"] | None = "auto",
        category: str | None = None,
        include_text: list[str] | None = None,
        exclude_text: list[str] | None = None,
        additional_queries: list[str] | None = None,
        text: bool = True,
        highlights: bool = False,
        summary: dict[str, Any] | None = None,
        context: dict[str, Any] | bool | None = None,
        flags: list[str] | None = None,
        moderation: bool | None = None,
        user_location: str | None = None,
    ) -> Any:
        """
        Performs a semantic or keyword search across the web and returns ranked results.
        Ideal for finding high-quality links, research papers, news, or general information.

        Args:
            query: The search query. For best results with 'neural' or 'deep' search, use a
                descriptive natural language statement (e.g., "Check out this amazing new
                AI tool for developers:").
            num_results: Total results to return (default: 10). For 'deep' search, leave blank
                to let the model determine the optimal number of results dynamically.
            include_domains: Restrict search to these domains (e.g., ['github.com', 'arxiv.org']).
            exclude_domains: Block these domains from appearing in results.
            start_crawl_date: ISO 8601 date. Only results crawled after this (e.g., '2024-01-01').
            end_crawl_date: ISO 8601 date. Only results crawled before this.
            start_published_date: ISO 8601 date. Only results published after this.
            end_published_date: ISO 8601 date. Only results published before this.
            type: The search methodology:
                - 'auto' (default): Automatically selects the best type based on query.
                - 'neural': Semantic search using embeddings. Best for concept-based queries.
                - 'fast': Keyword-based search. Best for specific names or terms.
                - 'deep': Multi-query expansion and reasoning. Best for complex, multi-faceted research.
                - 'hybrid': Combines neural and fast for balanced results.
            category: Filter by content type (e.g., 'company', 'research paper', 'news', 'pdf', 'tweet').
            include_text: Webpage MUST contain these exact strings (max 5 words per string).
            exclude_text: Webpage MUST NOT contain these exact strings.
            additional_queries: (Deep only) Up to 5 manually specified queries to skip automatic expansion.
            text: Include the full webpage text in the response (default: True).
            highlights: Include high-relevance snippets (highlights) from each result.
            summary: Generate a concise summary of each page. Can be a boolean or a dict:
                {"query": "Refining summary...", "schema": {"type": "object", "properties": {...}}}.
            context: Optimized for RAG. Returns a combined context object instead of raw results.
            flags: Experimental feature flags for specialized Exa behavior.
            moderation: Enable safety filtering for sensitive content.
            user_location: ISO country code (e.g., 'US') to personalize results.

        Returns:
            A serialized SearchResponse containing 'results' (list of Result objects with url, title, text, etc.).

        Tags:
            search, semantic, keyword, neural, important
        """
        logger.info(f"Exa search for: {query}")

        # Build contents options
        contents = {}
        if text:
            contents["text"] = True
        if highlights:
            contents["highlights"] = True
        if summary:
            contents["summary"] = summary
        if context:
            contents["context"] = context

        client = await self.get_exa_client()
        response = await client.search(
            query=query,
            num_results=num_results,
            include_domains=include_domains,
            exclude_domains=exclude_domains,
            start_crawl_date=start_crawl_date,
            end_crawl_date=end_crawl_date,
            start_published_date=start_published_date,
            end_published_date=end_published_date,
            type=type,
            category=category,
            include_text=include_text,
            exclude_text=exclude_text,
            additional_queries=additional_queries,
            contents=contents if contents else None,
            flags=flags,
            moderation=moderation,
            user_location=user_location,
        )
        return self._to_serializable(response)

    async def find_similar(  # noqa: PLR0913
        self,
        url: str,
        num_results: int | None = 10,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        start_crawl_date: str | None = None,
        end_crawl_date: str | None = None,
        start_published_date: str | None = None,
        end_published_date: str | None = None,
        exclude_source_domain: bool | None = None,
        category: str | None = None,
        include_text: list[str] | None = None,
        exclude_text: list[str] | None = None,
        text: bool = True,
        highlights: bool = False,
        summary: dict[str, Any] | None = None,
        flags: list[str] | None = None,
    ) -> Any:
        """
        Retrieves webpages that are semantically similar to a provided URL.
        Useful for finding "more like this", competitors, or related research.

        Args:
            url: The source URL to find similarity for.
            num_results: Number of similar results to return (default: 10).
            include_domains: List of domains to include in results.
            exclude_domains: List of domains to block.
            start_crawl_date: ISO 8601 date. Only results crawled after this.
            end_crawl_date: ISO 8601 date. Only results crawled before this.
            start_published_date: ISO 8601 date. Only results published after this.
            end_published_date: ISO 8601 date. Only results published before this.
            exclude_source_domain: If True, do not return results from the same domain as the input URL.
            category: Filter similar results by content type (e.g., 'personal site', 'github').
            include_text: Webpage MUST contain these exact strings.
            exclude_text: Webpage MUST NOT contain these exact strings.
            text: Include full text content in the response (default: True).
            highlights: Include relevance snippets (highlights).
            summary: Generate a summary for each similar page.
            flags: Experimental feature flags.

        Returns:
            A serialized SearchResponse with results semantically ranked by similarity to the input URL.

        Tags:
            similar, related, mapping, semantic
        """
        logger.info(f"Exa find_similar for URL: {url}")

        contents = {}
        if text:
            contents["text"] = True
        if highlights:
            contents["highlights"] = True
        if summary:
            contents["summary"] = summary

        client = await self.get_exa_client()
        response = await client.find_similar(
            url=url,
            num_results=num_results,
            include_domains=include_domains,
            exclude_domains=exclude_domains,
            start_crawl_date=start_crawl_date,
            end_crawl_date=end_crawl_date,
            start_published_date=start_published_date,
            end_published_date=end_published_date,
            exclude_source_domain=exclude_source_domain,
            category=category,
            include_text=include_text,
            exclude_text=exclude_text,
            contents=contents if contents else None,
            flags=flags,
        )
        return self._to_serializable(response)

    async def get_contents(  # noqa: PLR0913
        self,
        urls: list[str],
        text: bool = True,
        summary: dict[str, Any] | None = None,
        subpages: int | None = None,
        subpage_target: str | list[str] | None = None,
        livecrawl: Literal["always", "never", "fallback", "auto"] | None = None,
        livecrawl_timeout: int | None = None,
        filter_empty_results: bool | None = None,
        extras: dict[str, Any] | None = None,
        flags: list[str] | None = None,
    ) -> Any:
        """
        Deep-fetches the actual content of specific URLs or Result IDs.
        Provides robust data extraction including text, snippets, and structured summaries.

        Args:
            urls: List of URLs or Exa Result IDs to retrieve.
            text: Include full page text (default: True).
            summary: Generate structured or unstructured summaries of each URL.
            subpages: Number of additional pages to crawl automatically from the same domain.
            subpage_target: Focus subpage crawling on specific terms (e.g., 'pricing', 'technical doc').
            livecrawl: Controls real-time crawling behavior:
                - 'auto' (default): Uses Exa's cache first, crawls if data is missing or stale.
                - 'always': Forces a fresh crawl, bypassing cache entirely.
                - 'never': Strictly uses cached data.
                - 'fallback': Uses cache, only crawls if cache retrieval fails.
            livecrawl_timeout: Maximum time allowed for fresh crawls (in milliseconds).
            filter_empty_results: Automatically remove results where no meaningful content was found.
            extras: Advanced extraction features (e.g., {'links': 20, 'image_links': 10}).
            flags: Experimental feature flags.

        Returns:
            A serialized SearchResponse containing enriched content for each URL.

        Tags:
            content, fetch, crawl, subpages, extract
        """
        logger.info(f"Exa get_contents for {len(urls)} URLs.")
        client = await self.get_exa_client()
        response = await client.get_contents(
            urls=urls,
            text=text,
            summary=summary,
            subpages=subpages,
            subpage_target=subpage_target,
            livecrawl=livecrawl,
            livecrawl_timeout=livecrawl_timeout,
            filter_empty_results=filter_empty_results,
            extras=extras,
            flags=flags,
        )
        return self._to_serializable(response)

    async def answer(  # noqa: PLR0913
        self,
        query: str,
        text: bool = False,
        system_prompt: str | None = None,
        model: Literal["exa", "exa-pro"] | None = None,
        output_schema: dict[str, Any] | None = None,
        user_location: str | None = None,
    ) -> Any:
        """
        Synthesizes a direct, objective answer to a research question based on multiple web sources.
        Includes inline citations linked to the original pages.

        Args:
            query: The research question (e.g., "What are the latest breakthroughs in fusion power?").
            text: Include the full text of cited pages in the response (default: False).
            system_prompt: Guiding prompt to control the LLM's persona or formatting style.
            model: Answer engine:
                - 'exa-pro' (default): High-performance, multi-query reasoning for deep answers.
                - 'exa': Faster, single-pass answer generation.
            output_schema: Optional JSON Schema to force the result into a specific JSON structure.
            user_location: ISO country code for localized answers.

        Returns:
            A serialized AnswerResponse with the 'answer' text and 'citations' list.

        Tags:
            answer, synthesis, knowledge, citations, research, important
        """
        logger.info(f"Exa answer for query: {query}")
        client = await self.get_exa_client()
        response = await client.answer(
            query=query,
            text=text,
            system_prompt=system_prompt,
            model=model,
            output_schema=output_schema,
            user_location=user_location,
        )
        return self._to_serializable(response)

    async def create_research_task(
        self,
        instructions: str,
        output_schema: dict[str, Any] | None = None,
        model: Literal["exa-research", "exa-research-pro", "exa-research-fast"] | None = "exa-research-fast",
    ) -> Any:
        """
        Initiates a long-running, autonomous research task that explores the web to fulfill complex instructions.
        Ideal for tasks that require multiple searches and deep analysis.

        Args:
            instructions: Detailed briefing for the research goal (e.g., "Find all AI unicorns founded
                in 2024 and summarize their lead investors and core technology.").
            output_schema: Optional JSON Schema to structure the final researched output.
            model: Research intelligence level:
                - 'exa-research-fast' (default): Quick, focused investigation.
                - 'exa-research': Standard depth, balanced speed.
                - 'exa-research-pro': Maximum depth, exhaustive exploration.

        Returns:
            A serialized ResearchDto containing the 'research_id' (Task ID) used for polling and status checks.

        Tags:
            research, task, async, create
        """
        logger.info(f"Exa create_research_task: {instructions}")
        client = await self.get_exa_client()
        response = await client.research.create(
            instructions=instructions,
            output_schema=output_schema,
            model=model,
        )
        return self._to_serializable(response)

    async def get_research_task(self, task_id: str, events: bool = False) -> Any:
        """
        Retrieves the current status, metadata, and (if finished) final results of a research task.

        Args:
            task_id: The unique ID assigned during task creation.
            events: If True, returns a chronological log of all actions the researcher has taken.

        Returns:
            A serialized ResearchDto with status ('queued', 'running', 'completed', etc.) and data.

        Tags:
            research, status, task, check
        """
        logger.info(f"Exa get_research_task: {task_id}")
        client = await self.get_exa_client()
        response = await client.research.get(research_id=task_id, events=events)
        return self._to_serializable(response)

    async def poll_research_task(
        self,
        task_id: str,
        poll_interval_ms: int = 1000,
        timeout_ms: int = 600000,
        events: bool = False,
    ) -> Any:
        """
        Blocks until a research task completes, fails, or times out.
        Provides a convenient way to wait for results without manual looping.

        Args:
            task_id: The ID of the task to monitor.
            poll_interval_ms: Frequency of status checks in milliseconds (default: 1000).
            timeout_ms: Maximum duration to block before giving up (default: 10 minutes).
            events: If True, include activity logs in the final response.

        Returns:
            The terminal ResearchDto state containing the final research findings.

        Tags:
            research, poll, wait, task, terminal
        """
        logger.info(f"Exa poll_research_task: {task_id}")
        client = await self.get_exa_client()
        response = await client.research.poll_until_finished(
            research_id=task_id,
            poll_interval=poll_interval_ms,
            timeout_ms=timeout_ms,
            events=events,
        )
        return self._to_serializable(response)

    async def list_research_tasks(
        self,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> Any:
        """
        Provides a paginated list of all past and current research tasks for auditing or recovery.

        Args:
            cursor: Token for retrieving the next page of task history.
            limit: Maximum number of records to return in this call.

        Returns:
            A ListResearchResponseDto containing an array of research tasks.

        Tags:
            research, list, tasks, history
        """
        logger.info(f"Exa list_research_tasks (limit: {limit})")
        client = await self.get_exa_client()
        response = await client.research.list(cursor=cursor, limit=limit)
        return self._to_serializable(response)

    def list_tools(self):
        return [
            self.search,
            self.find_similar,
            self.get_contents,
            self.answer,
            self.create_research_task,
            self.get_research_task,
            self.poll_research_task,
            self.list_research_tasks,
        ]
