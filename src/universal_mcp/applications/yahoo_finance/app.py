from typing import Any

import yfinance as yf
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class YahooFinanceApp(APIApplication):
    """
    Application for interacting with Yahoo Finance data using yfinance library.
    Provides tools to retrieve stock information, historical data, news, and financial statements.
    """

    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="yahoo_finance", integration=integration, **kwargs)

    def get_stock_info(self, symbol: str) -> dict[str, Any]:
        """
        Gets real-time stock information including current price, market cap, financial ratios, and company details.

        Args:
            symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'MSFT')

        Returns:
            Complete dictionary with all available stock data fields from Yahoo Finance

        Raises:
            ValueError: Invalid or empty symbol
            KeyError: Stock symbol not found
            ConnectionError: Network or API issues

        Tags:
            stock, info, real-time, price, financials, company-data, important
        """
        if not symbol:
            raise ValueError("Stock symbol cannot be empty")

        symbol = symbol.upper().strip()
        ticker = yf.Ticker(symbol)

        info = ticker.info
        if not info or info.get("regularMarketPrice") is None:
            raise KeyError(f"Stock symbol '{symbol}' not found or invalid")

        return info

    def get_stock_history(
        self,
        symbol: str,
        period: str = "1mo",
        interval: str = "1d",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> dict:
        """
        Gets historical price data for a stock with OHLCV data, dividends, and stock splits.

        Args:
            symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'MSFT')
            period: Time period ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
            interval: Data interval ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')
            start_date: Start date in 'YYYY-MM-DD' format (overrides period)
            end_date: End date in 'YYYY-MM-DD' format (used with start_date)

        Returns:
            Dictionary with historical stock data, dates as string keys

        Tags:
            stock, history, ohlcv, price-data, time-series, important
        """
        if not symbol:
            raise ValueError("Stock symbol cannot be empty")

        symbol = symbol.upper().strip()
        ticker = yf.Ticker(symbol)

        df = ticker.history(
            period=period, interval=interval, start=start_date, end=end_date
        )
        
        try:
            data = df.to_dict("index")  # type: ignore
            if data:
                converted_data = {}
                for key, value in data.items():
                    if hasattr(key, 'strftime'):
                        converted_key = key.strftime('%Y-%m-%d')
                    else:
                        converted_key = str(key)
                    converted_data[converted_key] = value
                return converted_data
            return data
        except:
            return {}

    def get_stock_news(self, symbol: str, limit: int = 10) -> list[Any]:
        """
        Gets latest news articles for a stock from Yahoo Finance.

        Args:
            symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'MSFT')
            limit: Maximum number of articles to return (1-50). Defaults to 10

        Returns:
            Raw list of news articles from Yahoo Finance

        Tags:
            stock, news, articles, sentiment, important
        """
        if not symbol:
            raise ValueError("Stock symbol cannot be empty")

        symbol = symbol.upper().strip()
        ticker = yf.Ticker(symbol)

        news = ticker.news
        return news[:limit] if news else []

    def get_financial_statements(
        self, symbol: str, statement_type: str = "income"
    ) -> dict:
        """
        Gets financial statements for a stock from Yahoo Finance.

        Args:
            symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'MSFT')
            statement_type: Type of statement ('income', 'balance', 'cashflow', 'earnings'). Defaults to 'income'

        Returns:
            Dictionary with financial statement data

        Tags:
            stock, financial-statements, earnings, important
        """
        if not symbol:
            raise ValueError("Stock symbol cannot be empty")

        symbol = symbol.upper().strip()
        ticker = yf.Ticker(symbol)

        if statement_type == "income":
            df = ticker.income_stmt
        elif statement_type == "balance":
            df = ticker.balance_sheet
        elif statement_type == "cashflow":
            df = ticker.cashflow
        elif statement_type == "earnings":
            df = ticker.earnings
        else:
            df = ticker.income_stmt

        try:
            data = df.to_dict("dict")  # type: ignore
            if data:
                converted_data = {}
                for key, value in data.items():
                    if hasattr(key, 'strftime'):
                        converted_key = key.strftime('%Y-%m-%d')
                    else:
                        converted_key = str(key)
                    converted_data[converted_key] = value
                return converted_data
            return data
        except:
            return {}

    def get_stock_recommendations(
        self, symbol: str, rec_type: str = "recommendations"
    ) -> list[dict]:
        """
        Gets analyst recommendations for a stock from Yahoo Finance.

        Args:
            symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'MSFT')
            rec_type: Type of recommendation data ('recommendations', 'upgrades_downgrades'). Defaults to 'recommendations'

        Returns:
            List of dictionaries with analyst recommendation data

        Tags:
            stock, recommendations, analyst-ratings, important
        """
        if not symbol:
            raise ValueError("Stock symbol cannot be empty")

        symbol = symbol.upper().strip()
        ticker = yf.Ticker(symbol)

        if rec_type == "upgrades_downgrades":
            df = ticker.upgrades_downgrades
        else:
            df = ticker.recommendations

        try:
            return df.to_dict("records")  # type: ignore
        except:
            return []

    def search(
        self,
        query: str,
        max_results: int = 10,
        news_count: int = 5,
        include_research: bool = False,
    ) -> dict[str, Any]:
        """
        Search Yahoo Finance for quotes, news, and research using yfinance Search.

        Args:
            query: Search query (company name, ticker symbol, or keyword)
            max_results: Maximum number of quote results to return. Defaults to 10
            news_count: Number of news articles to return. Defaults to 5
            include_research: Whether to include research data. Defaults to False

        Returns:
            Dictionary containing quotes, news, and optionally research data

        Tags:
            search, quotes, news, research, important
        """
        if not query:
            raise ValueError("Search query cannot be empty")

        search = yf.Search(
            query,
            max_results=max_results,
            news_count=news_count,
            include_research=include_research,
        )

        result = {}
        for attr in dir(search):
            if not attr.startswith("_"):
                try:
                    value = getattr(search, attr)
                    if not callable(value):
                        result[attr] = value
                except:
                    continue

        return result

    def lookup_ticker(
        self, query: str, lookup_type: str = "all", count: int = 25
    ) -> list[dict]:
        """
        Look up ticker symbols by type using yfinance Lookup.

        Args:
            query: Search query for ticker lookup
            lookup_type: Type of lookup ('all', 'stock', 'mutualfund', 'etf', 'index', 'future', 'currency', 'cryptocurrency'). Defaults to 'all'
            count: Maximum number of results to return. Defaults to 25

        Returns:
            List of dictionaries with ticker lookup results

        Tags:
            lookup, ticker, symbols, important
        """
        if not query:
            raise ValueError("Lookup query cannot be empty")

        try:
            lookup = yf.Lookup(query)

            if lookup_type == "stock":
                results = lookup.get_stock(count=count)
            elif lookup_type == "mutualfund":
                results = lookup.get_mutualfund(count=count)
            elif lookup_type == "etf":
                results = lookup.get_etf(count=count)
            elif lookup_type == "index":
                results = lookup.get_index(count=count)
            elif lookup_type == "future":
                results = lookup.get_future(count=count)
            elif lookup_type == "currency":
                results = lookup.get_currency(count=count)
            elif lookup_type == "cryptocurrency":
                results = lookup.get_cryptocurrency(count=count)
            else:  # default to 'all'
                results = lookup.get_all(count=count)

            try:
                return results.to_dict("records")  # type: ignore
            except:
                return []

        except Exception as e:
            return [{"query": query, "error": f"Lookup failed: {str(e)}"}]

    def list_tools(self):
        return [
            self.get_stock_info,
            self.get_stock_history,
            self.get_stock_news,
            self.get_financial_statements,
            self.get_stock_recommendations,
            self.search,
            self.lookup_ticker,
        ]
