from collections import Counter
from datetime import datetime
from typing import Any

import requests
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from universal_mcp.applications.fpl.utils.api import api
from universal_mcp.applications.fpl.utils.fixtures import (
    analyze_player_fixtures,
    get_blank_gameweeks,
    get_double_gameweeks,
    get_fixtures_resource,
    get_player_fixtures,
    get_player_gameweek_history,
)
from universal_mcp.applications.fpl.utils.helper import (
    find_players_by_name,
    get_player_info,
    get_players_resource,
    get_team_by_name,
    search_players,
)
from universal_mcp.applications.fpl.utils.league_utils import (
    _get_league_historical_performance,
    _get_league_standings,
    _get_league_team_composition,
    parse_league_standings,
)
from universal_mcp.applications.fpl.utils.position_utils import normalize_position


class FplApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """

    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="fpl", integration=integration, **kwargs)

    def analyze_league(
        self,
        league_id: int,
        analysis_type: str = "overview",
        start_gw: int | None = None,
        end_gw: int | None = None,
    ) -> dict[str, Any]:
        """
        Performs advanced analysis on an FPL league for a given gameweek range. It routes requests based on the analysis type ('overview', 'historical', 'team_composition') to provide deeper insights beyond the basic rankings from `get_league_standings`, such as historical performance or team composition.

        Returns visualization-optimized data for various types of league analysis.

        Args:
            league_id: ID of the league to analyze
            analysis_type: Type of analysis to perform:
                - "overview": General league overview (default)
                - "historical": Historical performance analysis
                - "team_composition": Team composition analysis
            start_gw: Starting gameweek (defaults to 1)
            end_gw: Ending gameweek (defaults to current)
            api: FPL API instance (import from your api.py)

        Returns:
            Rich analytics data structured for visualization

        Raises:
            ValueError: Raised when analysis_type is invalid.
            RuntimeError: Raised when API request fails.

        Tags:
            leagues, analytics, important
        """
        try:
            # Validate analysis type
            valid_types = ["overview", "historical", "team_composition"]
            if analysis_type not in valid_types:
                return {
                    "error": f"Invalid analysis type: {analysis_type}",
                    "valid_types": valid_types,
                }

            # Get current gameweek
            try:
                current_gw_data = api.get_current_gameweek()
                current_gw = current_gw_data.get("id", 1)
            except Exception:
                current_gw = 1

            # Process gameweek range
            effective_start_gw = start_gw
            effective_end_gw = end_gw

            DEFAULT_GW_LOOKBACK = 5

            if effective_start_gw is None:
                effective_start_gw = max(1, current_gw - DEFAULT_GW_LOOKBACK + 1)
            elif isinstance(effective_start_gw, str) and effective_start_gw.startswith(
                "current-"
            ):
                try:
                    offset = int(effective_start_gw.split("-")[1])
                    effective_start_gw = max(1, current_gw - offset)
                except ValueError:
                    effective_start_gw = max(1, current_gw - DEFAULT_GW_LOOKBACK + 1)

            if effective_end_gw is None or effective_end_gw == "current":
                effective_end_gw = current_gw
            elif isinstance(effective_end_gw, str) and effective_end_gw.startswith(
                "current-"
            ):
                try:
                    offset = int(effective_end_gw.split("-")[1])
                    effective_end_gw = max(1, current_gw - offset)
                except ValueError:
                    effective_end_gw = current_gw

            try:
                effective_start_gw = int(effective_start_gw)
                effective_end_gw = int(effective_end_gw)
            except (ValueError, TypeError):
                return {"error": "Invalid gameweek values"}

            effective_start_gw = max(effective_start_gw, 1)
            effective_end_gw = min(effective_end_gw, current_gw)
            if effective_start_gw > effective_end_gw:
                effective_start_gw, effective_end_gw = (
                    effective_end_gw,
                    effective_start_gw,
                )

            # Get league standings first
            try:
                league_data = _get_league_standings(league_id, api)

                if "error" in league_data:
                    return league_data

            except Exception as e:
                return {"error": f"Failed to get league standings: {str(e)}"}

            # Route to the appropriate analysis function
            try:
                if analysis_type in {"overview", "historical"}:
                    return _get_league_historical_performance(
                        league_id, api, effective_start_gw, effective_end_gw
                    )

                elif analysis_type == "team_composition":
                    return _get_league_team_composition(
                        league_id, api, effective_end_gw
                    )

            except Exception as e:
                return {
                    "error": f"Analysis failed: {str(e)}",
                    "league_info": league_data["league_info"],
                    "standings": league_data["standings"],
                    "status": "error",
                }

            return {"error": "Unknown analysis type"}

        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}

    def get_league_standings(self, league_id: int) -> dict[str, Any]:
        """
        Retrieves current standings for a specified FPL classic mini-league by its ID. It fetches and parses raw API data to provide a direct snapshot of the league table, distinguishing it from `get_league_analytics` which performs deeper, historical analysis.

        Args:
            league_id: ID of the league to fetch

        Returns:
            League information with standings and team details

        Raises:
            ValueError: Raised when league_id is invalid.
            RuntimeError: Raised when API request fails.

        Tags:
            leagues, standings, important
        """
        try:
            # Construct the URL
            url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/"

            # Make unauthenticated request for public leagues
            response = requests.get(url)
            response.raise_for_status()
            league_data = response.json()

            # Check for errors
            if "error" in league_data:
                return league_data

            # Parse league standings
            parsed_data = parse_league_standings(league_data)

            return parsed_data

        except Exception as e:
            return {
                "error": f"Failed to retrieve league standings: {str(e)}",
                "league_id": league_id,
            }

    def get_player_information(
        self,
        player_id: int | None = None,
        player_name: str | None = None,
        start_gameweek: int | None = None,
        end_gameweek: int | None = None,
        include_history: bool = True,
        include_fixtures: bool = True,
    ) -> dict[str, Any]:
        """
        Fetches a detailed profile for a specific FPL player, identified by ID or name. It can include gameweek performance history, filterable by range, and future fixtures. This provides an in-depth look at one player, differing from broader search or analysis functions like `search_fpl_players`.

        Args:
            player_id: FPL player ID (if provided, takes precedence over player_name)
            player_name: Player name to search for (used if player_id not provided)
            start_gameweek: Starting gameweek for filtering player history
            end_gameweek: Ending gameweek for filtering player history
            include_history: Whether to include gameweek-by-gameweek history
            include_fixtures: Whether to include upcoming fixtures

        Returns:
            Comprehensive player information including stats and history

        Raises:
            ValueError: Raised when both player_id and player_name are missing.
            KeyError: Raised when player is not found in the database.

        Tags:
            players, important
        """
        return get_player_info(
            player_id,
            player_name,
            start_gameweek,
            end_gameweek,
            include_history,
            include_fixtures,
        )

    def find_players(
        self,
        query: str,
        position: str | None = None,
        team: str | None = None,
        limit: int = 5,
    ) -> dict[str, Any]:
        """
        Searches for FPL players by full or partial name with optional filtering by team and position. This is a discovery tool, differentiating it from `get_player_information` which fetches a specific known player. It serves as a public interface to the internal `search_players` utility.

        Args:
            query: Player name or partial name to search for
            position: Optional position filter (GKP, DEF, MID, FWD)
            team: Optional team name filter
            limit: Maximum number of results to return

        Returns:
            List of matching players with details

        Raises:
            ValueError: Raised when query parameter is empty or invalid.
            TypeError: Raised when position or team filters are invalid.

        Tags:
            players, search, important
        """
        return search_players(query, position, team, limit)

    def get_gameweek_snapshot(self) -> dict[str, Any]:
        """
        Provides a detailed snapshot of the FPL schedule by identifying the current, previous, and next gameweeks. It calculates the precise real-time status of the current gameweek (e.g., 'Imminent', 'In Progress') and returns key deadline times and overall season progress.

        Returns:
            Detailed information about gameweek timing, including exact status.

        Raises:
            RuntimeError: If gameweek data cannot be retrieved.
            ValueError: If gameweek data is malformed or incomplete.

        Tags:
            gameweek, status, timing, important
        """

        gameweeks = api.get_gameweeks()

        # Find current, previous, and next gameweeks
        current_gw = next((gw for gw in gameweeks if gw.get("is_current")), None)
        previous_gw = next((gw for gw in gameweeks if gw.get("is_previous")), None)
        next_gw = next((gw for gw in gameweeks if gw.get("is_next")), None)

        # Determine exact current gameweek status
        current_status = "Not Started"
        if current_gw:
            deadline = datetime.strptime(
                current_gw["deadline_time"], "%Y-%m-%dT%H:%M:%SZ"
            )
            now = datetime.utcnow()

            if now < deadline:
                current_status = "Upcoming"
                time_until = deadline - now
                hours_until = time_until.total_seconds() / 3600

                if hours_until < 24:
                    current_status = "Imminent (< 24h)"
            elif current_gw.get("finished"):
                current_status = "Complete"
            else:
                current_status = "In Progress"

        return {
            "current_gameweek": current_gw and current_gw["id"],
            "current_status": current_status,
            "previous_gameweek": previous_gw and previous_gw["id"],
            "next_gameweek": next_gw and next_gw["id"],
            "season_progress": f"GW {current_gw['id']}/38" if current_gw else "Unknown",
            "exact_timing": {
                "current_deadline": current_gw and current_gw.get("deadline_time"),
                "next_deadline": next_gw and next_gw.get("deadline_time"),
            },
        }

    def screen_players(
        self,
        position: str | None = None,
        team: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_points: int | None = None,
        min_ownership: float | None = None,
        max_ownership: float | None = None,
        form_threshold: float | None = None,
        include_gameweeks: bool = False,
        num_gameweeks: int = 5,
        sort_by: str = "total_points",
        sort_order: str = "desc",
        limit: int = 20,
    ) -> dict[str, Any]:
        """
        Filters the FPL player database using multiple criteria like position, price, points, and form. Returns a sorted list of matching players, summary statistics for the filtered group, and optional recent gameweek performance data to aid in player discovery and analysis.

        Args:
            position: Player position (e.g., "midfielders", "defenders")
            team: Team name filter
            min_price: Minimum player price in millions
            max_price: Maximum player price in millions
            min_points: Minimum total points
            min_ownership: Minimum ownership percentage
            max_ownership: Maximum ownership percentage
            form_threshold: Minimum form rating
            include_gameweeks: Whether to include gameweek-by-gameweek data
            num_gameweeks: Number of recent gameweeks to include
            sort_by: Metric to sort results by (default: total_points)
            sort_order: Sort direction ("asc" or "desc")
            limit: Maximum number of players to return

        Returns:
            Filtered player data with summary statistics

        Raises:
            ValueError: Raised when query parameter is empty or invalid.
            TypeError: Raised when position or team filters are invalid.

        Tags:
            players, analyze, important
        """
        # Get cached complete player dataset
        all_players = get_players_resource()

        # Normalize position if provided
        normalized_position = normalize_position(position) if position else None
        position_changed = normalized_position != position if position else False

        # Apply all filters
        filtered_players = []
        for player in all_players:
            # Check position filter
            if normalized_position and player.get("position") != normalized_position:
                continue

            # Check team filter
            if team and not (
                team.lower() in player.get("team", "").lower()
                or team.lower() in player.get("team_short", "").lower()
            ):
                continue

            # Check price range
            if min_price is not None and player.get("price", 0) < min_price:
                continue
            if max_price is not None and player.get("price", 0) > max_price:
                continue

            # Check points threshold
            if min_points is not None and player.get("points", 0) < min_points:
                continue

            # Check ownership range
            try:
                ownership = float(player.get("selected_by_percent", 0).replace("%", ""))
                if min_ownership is not None and ownership < min_ownership:
                    continue
                if max_ownership is not None and ownership > max_ownership:
                    continue
            except (ValueError, TypeError):
                # Skip ownership check if value can't be converted
                pass

            # Check form threshold
            try:
                form = float(player.get("form", 0))
                if form_threshold is not None and form < form_threshold:
                    continue
            except (ValueError, TypeError):
                # Skip form check if value can't be converted
                pass

            player["status"] = (
                "available" if player.get("status") == "a" else "unavailable"
            )

            # Player passed all filters
            filtered_players.append(player)

        # Sort results
        reverse = sort_order.lower() != "asc"
        try:
            # Handle numeric sorting properly
            numeric_fields = ["points", "price", "form", "selected_by_percent", "value"]
            if sort_by in numeric_fields:
                filtered_players.sort(
                    key=lambda p: float(p.get(sort_by, 0))
                    if p.get(sort_by) is not None
                    else 0,
                    reverse=reverse,
                )
            else:
                filtered_players.sort(key=lambda p: p.get(sort_by, ""), reverse=reverse)
        except (KeyError, ValueError):
            # Fall back to points sorting
            filtered_players.sort(key=lambda p: float(p.get("points", 0)), reverse=True)

        # Calculate summary statistics
        total_players = len(filtered_players)
        average_points = sum(float(p.get("points", 0)) for p in filtered_players) / max(
            1, total_players
        )
        average_price = sum(float(p.get("price", 0)) for p in filtered_players) / max(
            1, total_players
        )

        # Count position and team distributions
        position_counts = Counter(p.get("position") for p in filtered_players)
        team_counts = Counter(p.get("team") for p in filtered_players)

        # Build filter description
        applied_filters = []
        if normalized_position:
            applied_filters.append(f"Position: {normalized_position}")
        if team:
            applied_filters.append(f"Team: {team}")
        if min_price is not None:
            applied_filters.append(f"Min price: £{min_price}m")
        if max_price is not None:
            applied_filters.append(f"Max price: £{max_price}m")
        if min_points is not None:
            applied_filters.append(f"Min points: {min_points}")
        if min_ownership is not None:
            applied_filters.append(f"Min ownership: {min_ownership}%")
        if max_ownership is not None:
            applied_filters.append(f"Max ownership: {max_ownership}%")
        if form_threshold is not None:
            applied_filters.append(f"Min form: {form_threshold}")

        # Build results with summary and detail sections
        result = {
            "summary": {
                "total_matches": total_players,
                "filters_applied": applied_filters,
                "average_points": round(average_points, 1),
                "average_price": round(average_price, 2),
                "position_distribution": dict(position_counts),
                "team_distribution": dict(
                    sorted(team_counts.items(), key=lambda x: x[1], reverse=True)[:10]
                ),  # Top 10 teams
            },
            "players": filtered_players[:limit],  # Apply limit to detailed results
        }

        # Add position normalization note if relevant
        if position_changed:
            result["summary"]["position_note"] = (
                f"'{position}' was interpreted as '{normalized_position}'"
            )

        # Include gameweek history if requested
        if include_gameweeks and filtered_players:
            try:
                # Get history for top players (limit)
                player_ids = [p.get("id") for p in filtered_players[:limit]]
                gameweek_data = get_player_gameweek_history(player_ids, num_gameweeks)

                # Add gameweek data to the result
                result["gameweek_data"] = gameweek_data

                # Calculate and add recent form stats based on gameweek history
                recent_form_stats = {}

                if "players" in gameweek_data:
                    for player_id, history in gameweek_data["players"].items():
                        player_id = int(player_id)

                        # Find matching player in our filtered list
                        player_info = next(
                            (p for p in filtered_players if p.get("id") == player_id),
                            None,
                        )
                        if not player_info:
                            continue

                        # Initialize stats
                        recent_stats = {
                            "player_name": player_info.get("name", "Unknown"),
                            "matches": len(history),
                            "minutes": 0,
                            "points": 0,
                            "goals": 0,
                            "assists": 0,
                            "clean_sheets": 0,
                            "bonus": 0,
                            "expected_goals": 0,
                            "expected_assists": 0,
                            "expected_goal_involvements": 0,
                            "points_per_game": 0,
                            "gameweeks_analyzed": gameweek_data.get("gameweeks", []),
                        }

                        # Sum up stats from gameweek history
                        for gw in history:
                            recent_stats["minutes"] += gw.get("minutes", 0)
                            recent_stats["points"] += gw.get("points", 0)
                            recent_stats["goals"] += gw.get("goals", 0)
                            recent_stats["assists"] += gw.get("assists", 0)
                            recent_stats["clean_sheets"] += gw.get("clean_sheets", 0)
                            recent_stats["bonus"] += gw.get("bonus", 0)
                            recent_stats["expected_goals"] += float(
                                gw.get("expected_goals", 0)
                            )
                            recent_stats["expected_assists"] += float(
                                gw.get("expected_assists", 0)
                            )
                            recent_stats["expected_goal_involvements"] += float(
                                gw.get("expected_goal_involvements", 0)
                            )

                        # Calculate averages
                        if recent_stats["matches"] > 0:
                            recent_stats["points_per_game"] = round(
                                recent_stats["points"] / recent_stats["matches"], 1
                            )

                        # Round floating point values
                        recent_stats["expected_goals"] = round(
                            recent_stats["expected_goals"], 2
                        )
                        recent_stats["expected_assists"] = round(
                            recent_stats["expected_assists"], 2
                        )
                        recent_stats["expected_goal_involvements"] = round(
                            recent_stats["expected_goal_involvements"], 2
                        )

                        recent_form_stats[str(player_id)] = recent_stats

                # Add recent form stats to result
                result["recent_form"] = {
                    "description": f"Stats for the last {num_gameweeks} gameweeks only",
                    "player_stats": recent_form_stats,
                }

                # Add labels to clarify which stats are season-long vs. recent
                for player in result["players"]:
                    player["stats_type"] = "season_totals"

            except Exception as e:
                result["gameweek_data_error"] = str(e)

        return result

    def compare_players(
        self,
        player_names: list[str],
        metrics: list[str] = [
            "total_points",
            "form",
            "goals_scored",
            "assists",
            "bonus",
        ],
        include_gameweeks: bool = False,
        num_gameweeks: int = 5,
        include_fixture_analysis: bool = True,
    ) -> dict[str, Any]:
        """
        Performs a detailed comparison of multiple players based on specified metrics, recent gameweek history, and upcoming fixture analysis. It provides a side-by-side breakdown, identifies the best performer per metric, and determines an overall winner, considering fixture difficulty, blanks, and doubles for a comprehensive overview.

        Args:
            player_names: List of player names to compare (2-5 players recommended)
            metrics: List of metrics to compare
            include_gameweeks: Whether to include gameweek-by-gameweek comparison
            num_gameweeks: Number of recent gameweeks to include in comparison
            include_fixture_analysis: Whether to include fixture analysis including blanks and doubles

        Returns:
            Detailed comparison of players across the specified metrics

        Raises:
            ValueError: Raised when player_names parameter is empty or invalid.
            TypeError: Raised when metrics parameter is invalid.

        Tags:
            players, compare, important
        """

        if not player_names or len(player_names) < 2:
            return {"error": "Please provide at least two player names to compare"}

        # Find all players by name
        players_data = {}
        for name in player_names:
            matches = find_players_by_name(
                name, limit=3
            )  # Get more matches to find active players
            if not matches:
                return {"error": f"No player found matching '{name}'"}

            # Filter to active players
            active_matches = [p for p in matches]

            # Use first active match
            player = active_matches[0]
            players_data[name] = player

        # Build comparison structure
        comparison = {
            "players": {
                name: {
                    "id": player["id"],
                    "name": player["name"],
                    "team": player["team"],
                    "position": player["position"],
                    "price": player["price"],
                    "status": "available" if player["status"] == "a" else "unavailable",
                    "news": player.get("news", ""),
                }
                for name, player in players_data.items()
            },
            "metrics_comparison": {},
        }

        # Compare all requested metrics
        for metric in metrics:
            metric_values = {}

            for name, player in players_data.items():
                if metric in player:
                    # Try to convert to numeric if possible
                    try:
                        value = float(player[metric])
                    except (ValueError, TypeError):
                        value = player[metric]

                    metric_values[name] = value

            if metric_values:
                comparison["metrics_comparison"][metric] = metric_values

        # Include gameweek comparison if requested
        if include_gameweeks:
            try:
                gameweek_comparison = {}
                recent_form_comparison = {}
                gameweek_range = []

                # Get gameweek data for each player
                for name, player in players_data.items():
                    player_history = get_player_gameweek_history(
                        [player["id"]], num_gameweeks
                    )

                    if (
                        "players" in player_history
                        and player["id"] in player_history["players"]
                    ):
                        history = player_history["players"][player["id"]]
                        gameweek_comparison[name] = history

                        # Store gameweek range
                        if "gameweeks" in player_history and not gameweek_range:
                            gameweek_range = player_history["gameweeks"]

                        # Calculate aggregated recent form stats
                        recent_stats = {
                            "matches": len(history),
                            "minutes": 0,
                            "points": 0,
                            "goals": 0,
                            "assists": 0,
                            "clean_sheets": 0,
                            "bonus": 0,
                            "expected_goals": 0,
                            "expected_assists": 0,
                            "expected_goal_involvements": 0,
                            "points_per_game": 0,
                        }

                        # Sum up stats from gameweek history
                        for gw in history:
                            recent_stats["minutes"] += gw.get("minutes", 0)
                            recent_stats["points"] += gw.get("points", 0)
                            recent_stats["goals"] += gw.get("goals", 0)
                            recent_stats["assists"] += gw.get("assists", 0)
                            recent_stats["clean_sheets"] += gw.get("clean_sheets", 0)
                            recent_stats["bonus"] += gw.get("bonus", 0)
                            recent_stats["expected_goals"] += int(
                                float(gw.get("expected_goals", 0))
                            )
                            recent_stats["expected_assists"] += int(
                                float(gw.get("expected_assists", 0))
                            )
                            recent_stats["expected_goal_involvements"] += int(
                                float(gw.get("expected_goal_involvements", 0))
                            )
                        if recent_stats["matches"] > 0:
                            recent_stats["points_per_game"] = int(
                                round(
                                    recent_stats["points"] / recent_stats["matches"], 1
                                )
                            )

                        # Round floating point values
                        recent_stats["expected_goals"] = round(
                            recent_stats["expected_goals"], 2
                        )
                        recent_stats["expected_assists"] = round(
                            recent_stats["expected_assists"], 2
                        )
                        recent_stats["expected_goal_involvements"] = round(
                            recent_stats["expected_goal_involvements"], 2
                        )

                        recent_form_comparison[name] = recent_stats

                # Only add to result if we have data
                if gameweek_comparison:
                    comparison["gameweek_comparison"] = gameweek_comparison
                    comparison["gameweek_range"] = gameweek_range

                    # Add recent form comparison section
                    comparison["recent_form_comparison"] = {
                        "description": f"Aggregated stats for the last {num_gameweeks} gameweeks only",
                        "gameweeks_analyzed": gameweek_range,
                        "player_stats": recent_form_comparison,
                    }

                    # Add best performer for recent form metrics
                    comparison["recent_form_best"] = {}

                    # Compare players on key recent form metrics
                    for metric in [
                        "points",
                        "goals",
                        "assists",
                        "expected_goals",
                        "expected_assists",
                    ]:
                        values = {
                            name: stats[metric]
                            for name, stats in recent_form_comparison.items()
                        }
                        if values and all(
                            isinstance(v, int | float) for v in values.values()
                        ):
                            best_player = max(values.items(), key=lambda x: x[1])[0]
                            comparison["recent_form_best"][metric] = best_player

                    # Add label to metrics to indicate they're season-long stats
                    for metric, values in comparison["metrics_comparison"].items():
                        comparison["metrics_comparison"][metric] = {
                            "stats_type": "season_totals",
                            "values": values,
                        }
            except Exception as e:
                comparison["gameweek_comparison_error"] = str(e)

        # Include fixture analysis if requested
        if include_fixture_analysis:
            fixture_comparison = {}
            fixture_scores = {}
            blank_gameweek_impacts = {}
            double_gameweek_impacts = {}

            # Get upcoming fixtures for each player
            for name, player in players_data.items():
                try:
                    # Get fixture analysis
                    player_fixture_analysis = analyze_player_fixtures(
                        player["id"], num_gameweeks
                    )

                    # Format fixture data
                    fixtures_data = []
                    if (
                        "fixture_analysis" in player_fixture_analysis
                        and "fixtures_analyzed"
                        in player_fixture_analysis["fixture_analysis"]
                    ):
                        fixtures_data = player_fixture_analysis["fixture_analysis"][
                            "fixtures_analyzed"
                        ]

                    fixture_comparison[name] = fixtures_data

                    # Store fixture difficulty score
                    if (
                        "fixture_analysis" in player_fixture_analysis
                        and "difficulty_score"
                        in player_fixture_analysis["fixture_analysis"]
                    ):
                        fixture_scores[name] = player_fixture_analysis[
                            "fixture_analysis"
                        ]["difficulty_score"]

                    # Check for blank gameweeks
                    team_name = player["team"]
                    blank_gws = get_blank_gameweeks(num_gameweeks)
                    blank_impact = []

                    for blank_gw in blank_gws:
                        for team_info in blank_gw.get("teams_without_fixtures", []):
                            if team_info.get("name") == team_name:
                                blank_impact.append(blank_gw["gameweek"])

                    blank_gameweek_impacts[name] = blank_impact

                    # Check for double gameweeks
                    double_gws = get_double_gameweeks(num_gameweeks)
                    double_impact = []

                    for double_gw in double_gws:
                        for team_info in double_gw.get("teams_with_doubles", []):
                            if team_info.get("name") == team_name:
                                double_impact.append(
                                    {
                                        "gameweek": double_gw["gameweek"],
                                        "fixture_count": team_info.get(
                                            "fixture_count", 2
                                        ),
                                    }
                                )

                    double_gameweek_impacts[name] = double_impact
                except Exception:
                    pass

            # Add fixture data to comparison
            if fixture_comparison:
                comparison["fixture_comparison"] = {
                    "upcoming_fixtures": fixture_comparison,
                    "fixture_scores": fixture_scores,
                    "blank_gameweeks": blank_gameweek_impacts,
                    "double_gameweeks": double_gameweek_impacts,
                }

                # Add fixture advantage assessment
                if len(fixture_scores) >= 2:
                    best_fixtures_player = max(
                        fixture_scores.items(), key=lambda x: x[1]
                    )[0]
                    worst_fixtures_player = min(
                        fixture_scores.items(), key=lambda x: x[1]
                    )[0]

                    comparison["fixture_comparison"]["fixture_advantage"] = {
                        "best_fixtures": best_fixtures_player,
                        "worst_fixtures": worst_fixtures_player,
                        "advantage": f"{best_fixtures_player} has easier upcoming fixtures than {worst_fixtures_player}",
                    }

        # Add summary of who's best for each metric
        comparison["best_performers"] = {}

        for metric, values in comparison["metrics_comparison"].items():
            # Determine which metrics should be ranked with higher values as better
            higher_is_better = metric not in ["price"]

            # Find the best player for this metric
            if all(isinstance(v, int | float) for v in values.values()):
                if higher_is_better:
                    best_name = max(values.items(), key=lambda x: x[1])[0]
                else:
                    best_name = min(values.items(), key=lambda x: x[1])[0]

                comparison["best_performers"][metric] = best_name

        # Overall comparison summary
        player_wins = {name: 0 for name in players_data.keys()}

        for metric, best_name in comparison["best_performers"].items():
            player_wins[best_name] = player_wins.get(best_name, 0) + 1

        # Add fixture advantage to wins if available
        if (
            include_fixture_analysis
            and "fixture_comparison" in comparison
            and "fixture_advantage" in comparison["fixture_comparison"]
        ):
            best_fixtures_player = comparison["fixture_comparison"][
                "fixture_advantage"
            ]["best_fixtures"]
            player_wins[best_fixtures_player] = (
                player_wins.get(best_fixtures_player, 0) + 1
            )

        comparison["summary"] = {
            "metrics_won": player_wins,
            "overall_best": max(player_wins.items(), key=lambda x: x[1])[0]
            if player_wins
            else None,
        }

        return comparison

    def analyze_player_fixtures(
        self, player_name: str, num_fixtures: int = 5
    ) -> dict[str, Any]:
        """
        Analyzes a player's upcoming fixture difficulty. Given a player's name, it retrieves their schedule for a set number of matches, returning a detailed list and a calculated difficulty rating. This method is a focused alternative to the more comprehensive `analyze_fixtures` function.

        Args:
            player_name: Player name to search for
            num_fixtures: Number of upcoming fixtures to analyze (default: 5)

        Returns:
            Analysis of player's upcoming fixtures with difficulty ratings

        Raises:
            ValueError: Raised when player_name parameter is empty or invalid.
            TypeError: Raised when num_fixtures parameter is invalid.

        Tags:
            players, fixtures, important
        """

        # Find the player
        player_matches = find_players_by_name(player_name)
        if not player_matches:
            return {"error": f"No player found matching '{player_name}'"}

        player = player_matches[0]
        analysis = analyze_player_fixtures(player["id"], num_fixtures)

        return analysis

    def analyze_entity_fixtures(
        self,
        entity_type: str = "player",
        entity_name: str | None = None,
        num_gameweeks: int = 5,
        include_blanks: bool = True,
        include_doubles: bool = True,
    ) -> dict[str, Any]:
        """
        Provides a detailed fixture difficulty analysis for a specific player, team, or an entire position over a set number of gameweeks. It calculates a difficulty score and can include blank/double gameweek data, offering broader analysis than the player-only `analyze_player_fixtures`.

        Args:
            entity_type: Type of entity to analyze ("player", "team", or "position")
            entity_name: Name of the specific entity
            num_gameweeks: Number of gameweeks to look ahead
            include_blanks: Whether to include blank gameweek info
            include_doubles: Whether to include double gameweek info

        Returns:
            Fixture analysis with difficulty ratings and summary

        Raises:
            ValueError: Raised when entity_type parameter is invalid.
            TypeError: Raised when num_gameweeks parameter is invalid.

        Tags:
            players, fixtures, important
        """

        # Normalize entity type
        entity_type = entity_type.lower()
        if entity_type not in ["player", "team", "position"]:
            return {
                "error": f"Invalid entity type: {entity_type}. Must be 'player', 'team', or 'position'"
            }

        # Get current gameweek
        gameweeks_data = api.get_gameweeks()
        current_gameweek = None

        for gw in gameweeks_data:
            if gw.get("is_current"):
                current_gameweek = gw.get("id")
                break

        if current_gameweek is None:
            # If no current gameweek found, try to find next gameweek
            for gw in gameweeks_data:
                if gw.get("is_next"):
                    gw_id = gw.get("id")
                    if gw_id is not None:
                        current_gameweek = gw_id - 1
                    break

        if current_gameweek is None:
            return {"error": "Could not determine current gameweek"}

        # Base result structure
        result = {
            "entity_type": entity_type,
            "entity_name": entity_name,
            "current_gameweek": current_gameweek,
            "analysis_range": list(
                range(current_gameweek + 1, current_gameweek + num_gameweeks + 1)
            ),
        }

        # Handle each entity type
        if entity_type == "player":
            # Find player and their team
            if entity_name is None:
                return {"error": "Entity name is required for player analysis"}
            player_matches = find_players_by_name(entity_name)
            if not player_matches:
                return {"error": f"No player found matching '{entity_name}'"}

            active_players = [p for p in player_matches]

            player = active_players[0]
            result["player"] = {
                "id": player["id"],
                "name": player["name"],
                "team": player["team"],
                "position": player["position"],
                "status": "available" if player["status"] == "a" else "unavailable",
            }

            # Get fixtures for player's team
            player_fixtures = get_player_fixtures(player["id"], num_gameweeks)

            # Calculate difficulty score
            total_difficulty = sum(f["difficulty"] for f in player_fixtures)
            avg_difficulty = (
                total_difficulty / len(player_fixtures) if player_fixtures else 0
            )

            # Scale difficulty (5 is hardest, 1 is easiest - invert so 10 is best)
            fixture_score = (6 - avg_difficulty) * 2 if player_fixtures else 0

            result["fixtures"] = player_fixtures
            result["fixture_analysis"] = {
                "difficulty_score": round(fixture_score, 1),
                "fixtures_analyzed": len(player_fixtures),
                "home_matches": sum(
                    1 for f in player_fixtures if f["location"] == "home"
                ),
                "away_matches": sum(
                    1 for f in player_fixtures if f["location"] == "away"
                ),
            }

            # Add fixture difficulty assessment
            if fixture_score >= 8:
                result["fixture_analysis"]["assessment"] = "Excellent fixtures"
            elif fixture_score >= 6:
                result["fixture_analysis"]["assessment"] = "Good fixtures"
            elif fixture_score >= 4:
                result["fixture_analysis"]["assessment"] = "Average fixtures"
            else:
                result["fixture_analysis"]["assessment"] = "Difficult fixtures"

        elif entity_type == "team":
            # Find team
            if entity_name is None:
                return {"error": "Entity name is required for team analysis"}
            team = get_team_by_name(entity_name)
            if not team:
                return {"error": f"No team found matching '{entity_name}'"}

            result["team"] = {
                "id": team["id"],
                "name": team["name"],
                "short_name": team["short_name"],
            }

            # Get fixtures for team
            team_fixtures = get_fixtures_resource(team_name=team["name"])

            # Filter to upcoming fixtures
            upcoming_fixtures = [
                f for f in team_fixtures if f["gameweek"] in result["analysis_range"]
            ]

            # Format fixtures
            formatted_fixtures = []
            for fixture in upcoming_fixtures:
                is_home = fixture["home_team"]["name"] == team["name"]
                opponent = fixture["away_team"] if is_home else fixture["home_team"]
                difficulty = fixture["difficulty"]["home" if is_home else "away"]

                formatted_fixtures.append(
                    {
                        "gameweek": fixture["gameweek"],
                        "opponent": opponent["name"],
                        "location": "home" if is_home else "away",
                        "difficulty": difficulty,
                    }
                )

            result["fixtures"] = formatted_fixtures

            # Calculate difficulty metrics
            if formatted_fixtures:
                total_difficulty = sum(f["difficulty"] for f in formatted_fixtures)
                avg_difficulty = total_difficulty / len(formatted_fixtures)
                fixture_score = (6 - avg_difficulty) * 2

                result["fixture_analysis"] = {
                    "difficulty_score": round(fixture_score, 1),
                    "fixtures_analyzed": len(formatted_fixtures),
                    "home_matches": sum(
                        1 for f in formatted_fixtures if f["location"] == "home"
                    ),
                    "away_matches": sum(
                        1 for f in formatted_fixtures if f["location"] == "away"
                    ),
                }

                # Add fixture difficulty assessment
                if fixture_score >= 8:
                    result["fixture_analysis"]["assessment"] = "Excellent fixtures"
                elif fixture_score >= 6:
                    result["fixture_analysis"]["assessment"] = "Good fixtures"
                elif fixture_score >= 4:
                    result["fixture_analysis"]["assessment"] = "Average fixtures"
                else:
                    result["fixture_analysis"]["assessment"] = "Difficult fixtures"
            else:
                result["fixture_analysis"] = {
                    "difficulty_score": 0,
                    "fixtures_analyzed": 0,
                    "assessment": "No upcoming fixtures found",
                }

        elif entity_type == "position":
            # Normalize position
            normalized_position = normalize_position(entity_name)
            if not normalized_position or normalized_position not in [
                "GKP",
                "DEF",
                "MID",
                "FWD",
            ]:
                return {"error": f"Invalid position: {entity_name}"}

            result["position"] = normalized_position

            # Get all players in this position
            all_players = get_players_resource()
            position_players = [
                p for p in all_players if p.get("position") == normalized_position
            ]

            # Get teams with players in this position
            teams_with_position = set(p.get("team") for p in position_players)

            # Get upcoming fixtures for these teams
            all_fixtures = get_fixtures_resource()
            upcoming_fixtures = [
                f for f in all_fixtures if f["gameweek"] in result["analysis_range"]
            ]

            # Calculate average fixture difficulty by team
            team_difficulties = {}

            for team in teams_with_position:
                team_fixtures = []

                for fixture in upcoming_fixtures:
                    is_home = fixture["home_team"]["name"] == team
                    is_away = fixture["away_team"]["name"] == team

                    if is_home or is_away:
                        difficulty = fixture["difficulty"][
                            "home" if is_home else "away"
                        ]
                        team_fixtures.append(
                            {
                                "gameweek": fixture["gameweek"],
                                "opponent": fixture["away_team"]["name"]
                                if is_home
                                else fixture["home_team"]["name"],
                                "location": "home" if is_home else "away",
                                "difficulty": difficulty,
                            }
                        )

                if team_fixtures:
                    total_diff = sum(f["difficulty"] for f in team_fixtures)
                    avg_diff = total_diff / len(team_fixtures)
                    fixture_score = (6 - avg_diff) * 2

                    team_difficulties[team] = {
                        "fixtures": team_fixtures,
                        "difficulty_score": round(fixture_score, 1),
                        "fixtures_analyzed": len(team_fixtures),
                    }

            # Sort teams by fixture difficulty (best first)
            sorted_teams = sorted(
                team_difficulties.items(),
                key=lambda x: x[1]["difficulty_score"],
                reverse=True,
            )

            result["team_fixtures"] = {
                team: data
                for team, data in sorted_teams[:10]  # Top 10 teams with best fixtures
            }

            # Add recommendation of teams with best fixtures
            if sorted_teams:
                best_teams = [team for team, data in sorted_teams[:3]]
                result["recommendations"] = {
                    "teams_with_best_fixtures": best_teams,
                    "analysis": f"Teams with players in position {normalized_position} with the best upcoming fixtures: {', '.join(best_teams)}",
                }

        # Add blank and double gameweek information if requested
        if include_blanks:
            blank_gameweeks = get_blank_gameweeks(num_gameweeks)
            result["blank_gameweeks"] = blank_gameweeks

        if include_doubles:
            double_gameweeks = get_double_gameweeks(num_gameweeks)
            result["double_gameweeks"] = double_gameweeks

        return result

    def get_blank_gameweeks(self, num_weeks: int = 5) -> list[dict[str, Any]]:
        """
        Identifies upcoming 'blank' gameweeks where teams lack a scheduled fixture. The function returns a list detailing each blank gameweek and the affected teams within a specified number of weeks, which is essential for strategic planning. It is distinct from `get_double_gameweeks`.

        Args:
            num_weeks: Number of upcoming gameweeks to check (default: 5)

        Returns:
            Information about blank gameweeks and affected teams

        Raises:
            ValueError: Raised when num_weeks parameter is invalid.
            TypeError: Raised when num_weeks parameter has incorrect type.

        Tags:
            gameweeks, blanks, important
        """
        return get_blank_gameweeks(num_weeks)

    def get_double_gameweeks(self, num_weeks: int = 5) -> list[dict[str, Any]]:
        """
        Identifies upcoming double gameweeks where teams have multiple fixtures within a specified number of weeks. It returns a list detailing each double gameweek and the teams involved. This function specifically finds gameweeks with extra matches, unlike `get_blank_gameweeks` which finds those with none.

        Args:
            num_weeks: Number of upcoming gameweeks to check (default: 5)

        Returns:
            Information about double gameweeks and affected teams

        Raises:
            ValueError: Raised when num_weeks parameter is invalid.
            TypeError: Raised when num_weeks parameter has incorrect type.

        Tags:
            gameweeks, doubles, important
        """
        return get_double_gameweeks(num_weeks)

    def get_manager_team_info(self, team_id: str) -> dict[str, Any]:
        """
        Retrieves detailed information for a specific FPL manager's team (an "entry") using its unique ID. This is distinct from functions analyzing Premier League clubs, as it targets an individual user's fantasy squad and its performance details within the game.

        Args:
            team_id: The ID of the team to get information about

        Returns:
            Information about the team

        Raises:
            ValueError: Raised when team_id parameter is invalid.


        Tags:
            teams, important
        """
        url = f"https://fantasy.premierleague.com/api/entry/{team_id}/"
        response = self._get(url)
        return self._handle_response(response)

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [
            self.get_player_information,
            self.find_players,
            self.get_gameweek_snapshot,
            self.screen_players,
            self.compare_players,
            self.analyze_player_fixtures,
            self.analyze_entity_fixtures,
            self.get_blank_gameweeks,
            self.get_double_gameweeks,
            self.get_league_standings,
            self.analyze_league,
            self.get_manager_team_info,
        ]
