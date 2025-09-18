# FirecrawlApp MCP Server

An MCP Server for the FirecrawlApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the FirecrawlApp API.


| Tool | Description |
|------|-------------|
| `scrape_url` | Synchronously scrapes a single URL, immediately returning its content. This provides a direct method for single-page scraping, contrasting with asynchronous, job-based functions like `start_crawl` (for entire sites) and `start_batch_scrape` (for multiple URLs). |
| `search` | Executes a synchronous web search using the Firecrawl service for a given query. Unlike scrape_url which fetches a single page, this function discovers web content. It returns a dictionary of results on success or an error string on failure, raising exceptions for authorization or SDK issues. |
| `start_crawl` | Starts an asynchronous Firecrawl job to crawl a website from a given URL, returning a job ID. Unlike the synchronous `scrape_url` for single pages, this function initiates a comprehensive, link-following crawl. Progress can be monitored using the `check_crawl_status` function with the returned ID. |
| `check_crawl_status` | Retrieves the status of an asynchronous Firecrawl job using its unique ID. As the counterpart to `start_crawl`, this function exclusively monitors website crawl progress, distinct from status checkers for batch scraping or data extraction jobs. Returns job details on success or an error message on failure. |
| `cancel_crawl` | Cancels a running asynchronous Firecrawl crawl job using its unique ID. As a lifecycle management tool for jobs initiated by `start_crawl`, it returns a confirmation status upon success or an error message on failure, distinguishing it from controls for other job types. |
| `start_batch_scrape` | Initiates an asynchronous Firecrawl job to scrape a list of URLs. It returns a job ID for tracking with `check_batch_scrape_status`. Unlike the synchronous `scrape_url` which processes a single URL, this function handles bulk scraping and doesn't wait for completion. |
| `check_batch_scrape_status` | Checks the status of an asynchronous batch scrape job using its job ID. As the counterpart to `start_batch_scrape`, it specifically monitors multi-URL scraping tasks, distinct from checkers for site-wide crawls (`check_crawl_status`) or AI-driven extractions (`check_extract_status`). Returns detailed progress or an error message. |
| `quick_web_extract` | Performs synchronous, AI-driven data extraction from URLs using an optional prompt or schema. Unlike asynchronous jobs like `start_crawl`, it returns structured data directly. This function raises an exception on failure, contrasting with other methods in the class that return an error string upon failure. |
| `check_extract_status` | Checks the status of an asynchronous, AI-powered Firecrawl data extraction job using its ID. Unlike `check_crawl_status` or `check_batch_scrape_status`, this function specifically monitors structured data extraction tasks, returning the job's progress or an error message on failure. |
