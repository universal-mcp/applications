---
name: exa
description: Application for interacting with the Exa API (exa.ai) using the official SDK. Provides advanced search, find similar links, page contents retrieval, knowledge synthesis (answer), and multi-step research tasks.
---

# Exa Integration

Application for interacting with the Exa API (exa.ai) using the official SDK. Provides advanced search, find similar links, page contents retrieval, knowledge synthesis (answer), and multi-step research tasks.

## Available Tools

| Tool | Description |
|------|-------------|
| `search` | Performs a semantic or keyword search across the web and returns ranked results. Ideal for finding high-quality links, research papers, news, or general information. |
| `find_similar` | Retrieves webpages that are semantically similar to a provided URL. Useful for finding "more like this", competitors, or related research. |
| `get_contents` | Deep-fetches the actual content of specific URLs or Result IDs. Provides robust data extraction including text, snippets, and structured summaries. |
| `answer` | Synthesizes a direct, objective answer to a research question based on multiple web sources. Includes inline citations linked to the original pages. |
| `create_research_task` | Initiates a long-running, autonomous research task that explores the web to fulfill complex instructions. Ideal for tasks that require multiple searches and deep analysis. |
| `get_research_task` | Retrieves the current status, metadata, and (if finished) final results of a research task. |
| `poll_research_task` | Blocks until a research task completes, fails, or times out. Provides a convenient way to wait for results without manual looping. |
| `list_research_tasks` | Provides a paginated list of all past and current research tasks for auditing or recovery. |
