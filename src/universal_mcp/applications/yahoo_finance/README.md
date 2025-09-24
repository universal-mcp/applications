# YahooFinanceApp MCP Server

An MCP Server for Yahoo Finance data using the yfinance library.

## 🛠️ Tool List

This provides access to Yahoo Finance data including stock information, historical prices, news, and financial statements.

| Tool | Description |
|------|-------------|
| `get_stock_info` | Gets real-time stock information including current price, market cap, financial ratios, and company details. Returns the complete raw data from Yahoo Finance for maximum flexibility. |
| `get_stock_history` | Gets historical price data for a stock with OHLCV data, dividends, and stock splits. Returns complete DataFrame with all available historical data. |
| `get_stock_news` | Gets latest news articles for a stock from Yahoo Finance. Returns raw list of news articles. |
| `get_financial_statements` | Gets financial statements for a stock from Yahoo Finance. Returns dictionary with financial statement data for income, balance, cashflow, or earnings statements. |
| `get_stock_recommendations` | Gets analyst recommendations for a stock from Yahoo Finance. Returns list of dictionaries with analyst recommendation data or upgrades/downgrades. |
| `search` | Search Yahoo Finance for quotes, news, and research using yfinance Search. Returns dictionary containing all available search data. |
| `lookup_ticker` | Look up ticker symbols by type using yfinance Lookup. Returns list of dictionaries with ticker lookup results filtered by security type (stock, etf, mutualfund, etc). | 
