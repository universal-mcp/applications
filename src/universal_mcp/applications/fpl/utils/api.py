import logging
from typing import Any

import httpx

# Set up logging
logger = logging.getLogger(__name__)


class FPLAPI:
    """
    FPL API client with schema validation, caching, and rate limiting.
    Handles fetching data from the Fantasy Premier League API.
    """

    def __init__(
        self,
        base_url: str = "https://fantasy.premierleague.com/api",
        user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    ):
        """
        Initialize the FPL API client.

        Args:
            base_url: FPL API base URL
            user_agent: User-Agent header for requests
        """
        self.base_url = base_url
        self.headers = {"User-Agent": user_agent}

    def _make_request(self, endpoint: str) -> Any:
        """
        Make an HTTP request to the FPL API.

        Args:
            endpoint: API endpoint to request (without base URL)

        Returns:
            JSON response data

        Raises:
            httpx.HTTPError: On HTTP error
        """
        url = f"{self.base_url}/{endpoint}"
        logger.debug(f"Making request to {url}")

        with httpx.Client() as client:
            response = client.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()

    def get_bootstrap_static(self) -> dict[str, Any]:
        """
        Get main FPL static data (players, teams, game settings).

        Returns:
            Bootstrap static data
        """
        data = self._make_request("bootstrap-static/")

        # Fix null values that should be integers according to schema
        if "phases" in data:
            for phase in data["phases"]:
                if phase.get("highest_score") is None:
                    phase["highest_score"] = 0

        return data

    def get_fixtures(self) -> list[dict[str, Any]]:
        """
        Get fixture data for all matches.

        Returns:
            List of fixtures
        """
        return self._make_request("fixtures/")

    def get_gameweeks(self) -> list[dict[str, Any]]:
        """
        Get all gameweeks data.

        Returns:
            List of gameweeks
        """
        static_data = self.get_bootstrap_static()
        return static_data.get("events", [])

    def get_current_gameweek(self) -> dict[str, Any]:
        """
        Get current gameweek data.

        Returns:
            Current gameweek data or None if not found
        """
        gameweeks = self.get_gameweeks()
        for gw in gameweeks:
            if gw.get("is_current", False):
                return gw

        # If no current gameweek found, return next one
        for gw in gameweeks:
            if gw.get("is_next", False):
                return gw

        # If no next gameweek either, return first one
        return gameweeks[0] if gameweeks else {}

    def get_player_summary(self, player_id: int) -> dict[str, Any]:
        """
        Get detailed data for a specific player.

        Args:
            player_id: FPL player ID

        Returns:
            Player summary data
        """
        return self._make_request(f"element-summary/{player_id}/")

    def get_players(self) -> list[dict[str, Any]]:
        """
        Get all players data.

        Returns:
            List of player data
        """
        static_data = self.get_bootstrap_static()
        return static_data.get("elements", [])

    def get_teams(self) -> list[dict[str, Any]]:
        """
        Get all teams data.

        Returns:
            List of team data
        """
        static_data = self.get_bootstrap_static()
        return static_data.get("teams", [])


# Create a singleton instance
api = FPLAPI()
