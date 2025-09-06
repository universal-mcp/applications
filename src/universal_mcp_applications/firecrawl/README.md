# FirecrawlApp MCP Server

An MCP Server for the FirecrawlApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the FirecrawlApp API.


| Tool | Description |
|------|-------------|
| `scrape_url` | Scrapes a single URL using Firecrawl and returns the extracted data. |
| `search` | Performs a web search using Firecrawl's search capability. |
| `start_crawl` | Starts a async crawl job for a given URL using Firecrawl. Returns the job ID immediately. |
| `check_crawl_status` | Checks the status of a previously initiated async Firecrawl crawl job. |
| `cancel_crawl` | Cancels a currently running Firecrawl crawl job. |
| `start_batch_scrape` | Starts a batch scrape job for multiple URLs using Firecrawl. (Note: May map to multiple individual scrapes or a specific batch API endpoint if available) |
| `check_batch_scrape_status` | Checks the status of a previously initiated Firecrawl batch scrape job. |
| `quick_web_extract` | Performs a quick, synchronous extraction of data from one or more URLs using Firecrawl and returns the results directly. |
| `check_extract_status` | Checks the status of a previously initiated Firecrawl extraction job. |
