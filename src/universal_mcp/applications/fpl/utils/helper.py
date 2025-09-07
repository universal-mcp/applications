import datetime
import logging
from typing import Any

logger = logging.getLogger("fpl-mcp-server.fixtures")
from .api import api

# Resources


def get_players_resource(
    name_filter: str | None = None, team_filter: str | None = None
) -> list[dict[str, Any]]:
    """
    Format player data for the MCP resource.

    Args:
        name_filter: Optional filter for player name (case-insensitive partial match)
        team_filter: Optional filter for team name (case-insensitive partial match)

    Returns:
        Formatted player data
    """
    # Get raw data from API
    data = api.get_bootstrap_static()

    # Create team and position lookup maps
    team_map = {t["id"]: t for t in data["teams"]}
    position_map = {p["id"]: p for p in data["element_types"]}
    logging.info(f"Team map: {team_map}")
    logging.info(f"Position map: {position_map}")

    # Format player data
    players = []
    for player in data["elements"]:
        # Extract team and position info
        team = team_map.get(player["team"], {})
        position = position_map.get(player["element_type"], {})

        player_name = f"{player['first_name']} {player['second_name']}"
        team_name = team.get("name", "Unknown")

        # Apply filters if specified
        if name_filter and name_filter.lower() not in player_name.lower():
            continue

        if team_filter and team_filter.lower() not in team_name.lower():
            continue

        # Build comprehensive player object with all available stats
        player_data = {
            "id": player["id"],
            "name": player_name,
            "web_name": player["web_name"],
            "team": team_name,
            "team_short": team.get("short_name", "UNK"),
            "position": position.get("singular_name_short", "UNK"),
            "price": player["now_cost"] / 10.0,
            "form": player["form"],
            "points": player["total_points"],
            "points_per_game": player["points_per_game"],
            # Playing time
            "minutes": player["minutes"],
            "starts": player["starts"],
            # Key stats
            "goals": player["goals_scored"],
            "assists": player["assists"],
            "clean_sheets": player["clean_sheets"],
            "goals_conceded": player["goals_conceded"],
            "own_goals": player["own_goals"],
            "penalties_saved": player["penalties_saved"],
            "penalties_missed": player["penalties_missed"],
            "yellow_cards": player["yellow_cards"],
            "red_cards": player["red_cards"],
            "saves": player["saves"],
            "bonus": player["bonus"],
            "bps": player["bps"],
            # Advanced metrics
            "influence": player["influence"],
            "creativity": player["creativity"],
            "threat": player["threat"],
            "ict_index": player["ict_index"],
            # Expected stats (if available)
            "expected_goals": player.get("expected_goals", "N/A"),
            "expected_assists": player.get("expected_assists", "N/A"),
            "expected_goal_involvements": player.get(
                "expected_goal_involvements", "N/A"
            ),
            "expected_goals_conceded": player.get("expected_goals_conceded", "N/A"),
            # Ownership & transfers
            "selected_by_percent": player["selected_by_percent"],
            "transfers_in_event": player["transfers_in_event"],
            "transfers_out_event": player["transfers_out_event"],
            # Price changes
            "cost_change_event": player["cost_change_event"] / 10.0,
            "cost_change_start": player["cost_change_start"] / 10.0,
            # Status info
            "status": player["status"],
            "news": player["news"],
            "chance_of_playing_next_round": player["chance_of_playing_next_round"],
        }

        players.append(player_data)
    logging.info(f"Formatted {len(players)} players")
    return players


def get_team_name_by_id(team_id: int | None) -> str:
    """Get team name from team ID.

    Args:
        team_id: Team ID

    Returns:
        Team name or "Unknown team" if not found
    """
    if team_id is None:
        return "Unknown team"

    teams_data = api.get_teams()

    for team in teams_data:
        if team.get("id") == team_id:
            return team.get("name", "Unknown team")

    return "Unknown team"


def get_player_by_id(player_id: int) -> dict[str, Any] | None:
    """
    Get detailed information for a specific player by ID.

    Args:
        player_id: FPL player ID

    Returns:
        Player data or None if not found
    """
    # Get all players
    all_players = get_players_resource()

    # Find player by ID
    for player in all_players:
        if player["id"] == player_id:
            # Get additional detail data
            try:
                summary = api.get_player_summary(player_id)

                # Add fixture history
                player["history"] = summary.get("history", [])

                # Add upcoming fixtures
                player["fixtures"] = summary.get("fixtures", [])

                return player
            except Exception:
                # Return basic player data if detailed data not available
                return player

    return None


def find_players_by_name(name: str, limit: int = 5) -> list[dict[str, Any]]:
    """
    Find players by partial name match with advanced matching.

    Args:
        name: Player name to search for (supports partial names, nicknames, and initials)
        limit: Maximum number of results to return

    Returns:
        List of matching players sorted by relevance and points
    """
    # Get all players
    logger = logging.getLogger(__name__)
    logger.info(f"Finding players by name: {name}")
    all_players = get_players_resource()
    logger.info(f"Found {len(all_players)} players")

    # Normalize search term
    search_term = name.lower().strip()
    if not search_term:
        return []

    # Common nickname and abbreviation mapping
    nicknames = {
        "kdb": "kevin de bruyne",
        "vvd": "virgil van dijk",
        "taa": "trent alexander-arnold",
        "cr7": "cristiano ronaldo",
        "bobby": "roberto firmino",
        "mo salah": "mohamed salah",
        "mane": "sadio mane",
        "auba": "aubameyang",
        "lewa": "lewandowski",
        "kane": "harry kane",
        "rashford": "marcus rashford",
        "son": "heung-min son",
    }

    # Check for nickname match
    if search_term in nicknames:
        search_term = nicknames[search_term]

    # Split search term into parts for multi-part matching
    search_parts = search_term.split()

    # Store scored results
    scored_players = []

    for player in all_players:
        # Extract player name components
        full_name = player["name"].lower()
        web_name = player.get("web_name", "").lower()

        # Try to extract first and last name
        name_parts = full_name.split()
        first_name = name_parts[0] if name_parts else ""
        last_name = name_parts[-1] if len(name_parts) > 1 else ""

        # Initialize score and tracking reasons
        score = 0

        # 1. Exact full name match
        if search_term == full_name:
            score += 100

        # 2. Exact match on web_name (common name)
        elif search_term == web_name:
            score += 90

        # 3. Exact match on last name
        elif len(search_parts) == 1 and search_term == last_name:
            score += 80

        # 4. Exact match on first name
        elif len(search_parts) == 1 and search_term == first_name:
            score += 70

        # 5. Check for initials match (e.g., "KDB")
        if len(search_term) <= 5 and all(c.isalpha() for c in search_term):
            # Try to match initials
            initials = "".join(part[0] for part in full_name.split() if part)
            if search_term.lower() == initials.lower():
                score += 85

        # 6. Multi-part name matching (e.g., "Mo Salah")
        if len(search_parts) > 1:
            # Check if first part matches first name and last part matches last name
            if search_parts[0] in first_name and search_parts[-1] in last_name:
                score += 75

            # Check if parts appear in order in the full name
            search_combined = "".join(search_parts)
            full_combined = "".join(full_name.split())
            if search_combined in full_combined:
                score += 50

        # 7. Substring matches
        if search_term in full_name:
            score += 40

        # 8. Partial word matches in full name
        for part in search_parts:
            if part in full_name:
                score += 30

        # 9. Partial word matches in web name
        for part in search_parts:
            if part in web_name:
                score += 25

        # 10. Add a bonus score for high-point players (tiebreaker)
        points_score = min(20, float(player["points"]) / 50)  # Up to 20 extra points

        # Total score
        total_score = score + (points_score if score > 0 else 0)

        # Add to results if there's any match
        if score > 0:
            scored_players.append((total_score, player))

    # Sort by score (highest first)
    sorted_players = [
        player for _, player in sorted(scored_players, key=lambda x: x[0], reverse=True)
    ]
    # If no matches with good confidence, fall back to simple contains match
    if not sorted_players or (sorted_players and scored_players[0][0] < 30):
        fallback_players = [
            p
            for p in all_players
            if search_term in p["name"].lower()
            or search_term in p.get("web_name", "").lower()
        ]
        # Sort fallback by points
        fallback_players.sort(key=lambda p: float(p["points"]), reverse=True)

        # Merge results, prioritizing scored results
        merged = []
        seen_ids = set(p["id"] for p in sorted_players)

        merged.extend(sorted_players)
        for p in fallback_players:
            if p["id"] not in seen_ids:
                merged.append(p)
                seen_ids.add(p["id"])

        sorted_players = merged

    # Return limited results
    return sorted_players[:limit]


def get_current_gameweek_resource() -> dict[str, Any]:
    """
    Get current gameweek data with additional details.

    Returns:
        Current gameweek data with enhanced information
    """
    # Get current gameweek
    current_gw = api.get_current_gameweek()

    # Get raw data to extract player details
    all_data = api.get_bootstrap_static()

    # Create enhanced gameweek data
    gw_data = {
        "id": current_gw["id"],
        "name": current_gw["name"],
        "deadline_time": current_gw["deadline_time"],
        "is_current": current_gw["is_current"],
        "is_next": current_gw["is_next"],
        "finished": current_gw["finished"],
        "data_checked": current_gw["data_checked"],
        "status": "Current" if current_gw.get("is_current", False) else "Next",
    }

    # Format deadline time to be more readable
    try:
        deadline = datetime.datetime.strptime(
            current_gw["deadline_time"], "%Y-%m-%dT%H:%M:%SZ"
        )
        gw_data["deadline_formatted"] = deadline.strftime("%A, %d %B %Y at %H:%M UTC")

        # Calculate time until deadline
        now = datetime.datetime.utcnow()
        if deadline > now:
            delta = deadline - now
            days = delta.days
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60

            time_parts = []
            if days > 0:
                time_parts.append(f"{days} day{'s' if days != 1 else ''}")
            if hours > 0:
                time_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
            if minutes > 0:
                time_parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

            gw_data["time_until_deadline"] = ", ".join(time_parts)
        else:
            gw_data["time_until_deadline"] = "Deadline passed"
    except (ValueError, TypeError):
        gw_data["deadline_formatted"] = current_gw["deadline_time"]

    # Add stats if available
    if current_gw.get("highest_score") is not None:
        gw_data["stats"] = {
            "highest_score": current_gw["highest_score"],
            "average_score": current_gw.get("average_entry_score", "N/A"),
            "chip_plays": current_gw.get("chip_plays", []),
        }

    # Add most popular players if available
    popular_players = {}
    player_map = {p["id"]: p for p in all_data.get("elements", [])}

    popular_fields = [
        ("most_selected", "Most Selected"),
        ("most_transferred_in", "Most Transferred In"),
        ("most_captained", "Most Captained"),
        ("most_vice_captained", "Most Vice Captained"),
    ]

    for field_key, field_name in popular_fields:
        player_id = current_gw.get(field_key)
        if player_id:
            player = player_map.get(player_id)
            if player:
                popular_players[field_name] = {
                    "id": player["id"],
                    "name": f"{player['first_name']} {player['second_name']}",
                    "web_name": player["web_name"],
                    "team": player["team"],
                }

    if popular_players:
        gw_data["popular_players"] = popular_players

    # Add fixtures if the API has them
    fixtures = api.get_fixtures()
    if fixtures:
        gw_fixtures = [f for f in fixtures if f.get("event") == current_gw["id"]]
        if gw_fixtures:
            gw_data["fixture_count"] = len(gw_fixtures)

    return gw_data


def get_player_fixtures(player_id: int, num_fixtures: int = 5) -> list[dict[str, Any]]:
    """Get upcoming fixtures for a specific player

    Args:
        player_id: FPL ID of the player
        num_fixtures: Number of upcoming fixtures to return

    Returns:
        List of upcoming fixtures for the player
    """
    logger.info(
        f"Getting player fixtures (player_id={player_id}, num_fixtures={num_fixtures})"
    )

    # Get player data to find their team
    players_data = api.get_players()
    player = None
    for p in players_data:
        if p.get("id") == player_id:
            player = p
            break

    if not player:
        logger.warning(f"Player with ID {player_id} not found")
        return []

    team_id = player.get("team")
    if not team_id:
        logger.warning(f"Team ID not found for player {player_id}")
        return []

    # Get all fixtures
    all_fixtures = api.get_fixtures()
    if not all_fixtures:
        logger.warning("No fixtures data found")
        return []

    # Get gameweeks to determine current gameweek
    gameweeks = api.get_gameweeks()
    current_gameweek = None
    for gw in gameweeks:
        if gw.get("is_current"):
            current_gameweek = gw.get("id")
            break

    if not current_gameweek:
        for gw in gameweeks:
            if gw.get("is_next"):
                gw_id = gw.get("id")
                if gw_id is not None:
                    current_gameweek = gw_id - 1
                break

    if not current_gameweek:
        logger.warning("Could not determine current gameweek")
        return []

    # Filter upcoming fixtures for player's team
    upcoming_fixtures = []

    for fixture in all_fixtures:
        # Only include fixtures from current gameweek onwards
        if fixture.get("event") and fixture.get("event") >= current_gameweek:
            # Check if player's team is involved
            if fixture.get("team_h") == team_id or fixture.get("team_a") == team_id:
                upcoming_fixtures.append(fixture)

    # Sort by gameweek
    upcoming_fixtures.sort(key=lambda x: x.get("event", 0))

    # Limit to requested number of fixtures
    upcoming_fixtures = upcoming_fixtures[:num_fixtures]

    # Get teams data for mapping IDs to names
    teams_data = api.get_teams()
    team_map = {t["id"]: t for t in teams_data}

    # Format fixtures
    formatted_fixtures = []
    for fixture in upcoming_fixtures:
        home_id = fixture.get("team_h", 0)
        away_id = fixture.get("team_a", 0)

        # Determine if player's team is home or away
        is_home = home_id == team_id

        # Get opponent team data
        opponent_id = away_id if is_home else home_id
        opponent_team = team_map.get(opponent_id, {})

        # Determine difficulty - higher is more difficult
        difficulty = fixture.get(
            "team_h_difficulty" if is_home else "team_a_difficulty", 3
        )

        formatted_fixture = {
            "gameweek": fixture.get("event"),
            "kickoff_time": fixture.get("kickoff_time", ""),
            "location": "home" if is_home else "away",
            "opponent": opponent_team.get("name", f"Team {opponent_id}"),
            "opponent_short": opponent_team.get("short_name", ""),
            "difficulty": difficulty,
        }

        formatted_fixtures.append(formatted_fixture)

    return formatted_fixtures


def get_player_gameweek_history(
    player_ids: list[int], num_gameweeks: int = 5
) -> dict[str, Any]:
    """Get recent gameweek history for multiple players.

    Args:
        player_ids: List of player IDs to fetch history for
        num_gameweeks: Number of recent gameweeks to include

    Returns:
        Dictionary mapping player IDs to their gameweek histories
    """
    logger = logging.getLogger(__name__)
    logger.info(
        f"Getting gameweek history for {len(player_ids)} players, {num_gameweeks} gameweeks"
    )

    # Get current gameweek to determine range
    gameweeks = api.get_gameweeks()
    current_gameweek = None

    for gw in gameweeks:
        if gw.get("is_current"):
            current_gameweek = gw.get("id")
            break

    if current_gameweek is None:
        # If no current gameweek found, try to find next gameweek
        for gw in gameweeks:
            if gw.get("is_next"):
                gw_id = gw.get("id")
                if gw_id is not None:
                    current_gameweek = gw_id - 1
                break

    if current_gameweek is None:
        logger.warning("Could not determine current gameweek")
        return {"error": "Could not determine current gameweek"}

    # Calculate gameweek range
    start_gameweek = max(1, current_gameweek - num_gameweeks + 1)
    gameweek_range = list(range(start_gameweek, current_gameweek + 1))
    logger.info(f"Analyzing gameweek range: {gameweek_range}")

    # Fetch history for each player
    result = {}

    for player_id in player_ids:
        try:
            # Get player summary which includes history
            player_summary = api.get_player_summary(player_id)

            if not player_summary or "history" not in player_summary:
                logger.warning(f"No history data found for player {player_id}")
                continue

            # Filter to requested gameweeks and format
            player_history = []

            for entry in player_summary["history"]:
                round_num = entry.get("round")
                if round_num in gameweek_range:
                    player_history.append(
                        {
                            "gameweek": round_num,
                            "minutes": entry.get("minutes", 0),
                            "points": entry.get("total_points", 0),
                            "goals": entry.get("goals_scored", 0),
                            "assists": entry.get("assists", 0),
                            "clean_sheets": entry.get("clean_sheets", 0),
                            "bonus": entry.get("bonus", 0),
                            "opponent": get_team_name_by_id(entry.get("opponent_team")),
                            "was_home": entry.get("was_home", False),
                            # Added additional stats as requested
                            "expected_goals": entry.get("expected_goals", 0),
                            "expected_assists": entry.get("expected_assists", 0),
                            "expected_goal_involvements": entry.get(
                                "expected_goal_involvements", 0
                            ),
                            "expected_goals_conceded": entry.get(
                                "expected_goals_conceded", 0
                            ),
                            "transfers_in": entry.get("transfers_in", 0),
                            "transfers_out": entry.get("transfers_out", 0),
                            "selected": entry.get("selected", 0),
                            "value": entry.get("value", 0) / 10.0
                            if "value" in entry
                            else 0,
                            "team_score": entry.get(
                                "team_h_score"
                                if entry.get("was_home")
                                else "team_a_score",
                                0,
                            ),
                            "opponent_score": entry.get(
                                "team_a_score"
                                if entry.get("was_home")
                                else "team_h_score",
                                0,
                            ),
                        }
                    )

            # Sort by gameweek
            player_history.sort(key=lambda x: x["gameweek"])
            result[player_id] = player_history

        except Exception as e:
            logger.error(f"Error fetching history for player {player_id}: {e}")

    return {"players": result, "gameweeks": gameweek_range}


# Tools
def get_player_info(
    player_id: int | None = None,
    player_name: str | None = None,
    start_gameweek: int | None = None,
    end_gameweek: int | None = None,
    include_history: bool = True,
    include_fixtures: bool = True,
) -> dict[str, Any]:
    """
    Get detailed information for a specific player, optionally filtering stats by gameweek range.

    Args:
        player_id: FPL player ID (if provided, takes precedence over player_name)
        player_name: Player name to search for (used if player_id not provided)
        start_gameweek: Starting gameweek for filtering player history
        end_gameweek: Ending gameweek for filtering player history
        include_history: Whether to include gameweek-by-gameweek history
        include_fixtures: Whether to include upcoming fixtures

    Returns:
        Detailed player information including stats and history
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Getting player info: ID={player_id}, name={player_name}")

    # Get current gameweek
    current_gw_info = get_current_gameweek_resource()
    current_gw = current_gw_info.get("id", 1)

    # Find player by ID or name
    player = None
    if player_id is not None:
        player = get_player_by_id(player_id)
    elif player_name:
        matches = find_players_by_name(player_name)
        if matches:
            player = matches[0]
            player_id = player.get("id")

    if not player:
        return {"error": f"Player not found: ID={player_id}, name={player_name}"}

    # Prepare result with basic player info
    result = {
        "player_id": player.get("id"),
        "name": player.get("name"),
        "web_name": player.get("web_name"),
        "team": player.get("team"),
        "team_short": player.get("team_short"),
        "position": player.get("position"),
        "price": player.get("price"),
        "season_stats": {
            "total_points": player.get("points"),
            "points_per_game": player.get("points_per_game"),
            "minutes": player.get("minutes"),
            "goals": player.get("goals"),
            "assists": player.get("assists"),
            "clean_sheets": player.get("clean_sheets"),
            "bonus": player.get("bonus"),
            "form": player.get("form"),
        },
        "ownership": {
            "selected_by_percent": player.get("selected_by_percent"),
            "transfers_in_event": player.get("transfers_in_event"),
            "transfers_out_event": player.get("transfers_out_event"),
        },
        "status": {
            "status": "available" if player.get("status") == "a" else "unavailable",
            "news": player.get("news"),
            "chance_of_playing_next_round": player.get("chance_of_playing_next_round"),
        },
    }

    # Add expected stats if available
    if "expected_goals" in player:
        result["expected_stats"] = {
            "expected_goals": player.get("expected_goals"),
            "expected_assists": player.get("expected_assists"),
            "expected_goal_involvements": player.get("expected_goal_involvements"),
            "expected_goals_conceded": player.get("expected_goals_conceded"),
        }

    # Add advanced metrics
    result["advanced_metrics"] = {
        "influence": player.get("influence"),
        "creativity": player.get("creativity"),
        "threat": player.get("threat"),
        "ict_index": player.get("ict_index"),
        "bps": player.get("bps"),
    }

    # Determine and validate gameweek range
    # Convert Optional[int] to int with defaults
    start_gw: int = 1 if start_gameweek is None else max(1, start_gameweek)
    end_gw: int = current_gw if end_gameweek is None else min(current_gw, end_gameweek)

    # Ensure start <= end
    start_gw = min(start_gw, end_gw)

    # Set the validated values as int (not Optional[int])
    start_gameweek = start_gw
    end_gameweek = end_gw

    # Include gameweek history if requested
    if include_history and "history" in player:
        # Filter history by gameweek range
        filtered_history = [
            gw
            for gw in player.get("history", [])
            if start_gameweek <= gw.get("round", 0) <= end_gameweek
        ]

        # Get detailed gameweek history
        player_id_value = player.get("id")
        if player_id_value is not None:
            gw_count = max(1, end_gameweek - start_gameweek + 1)
            gameweek_history = get_player_gameweek_history([player_id_value], gw_count)
        else:
            gameweek_history = None

        # Combine data
        history_data = filtered_history

        if gameweek_history and "players" in gameweek_history:
            player_id_str = str(player.get("id", ""))
            if player_id_str in gameweek_history["players"]:
                detailed_history = gameweek_history["players"][player_id_str]

                # Enrich with additional stats if available
                for gw_data in history_data:
                    gw_num = gw_data.get("round")
                    # Find matching detailed gameweek
                    matching_detailed = next(
                        (
                            gw
                            for gw in detailed_history
                            if gw.get("round") == gw_num or gw.get("gameweek") == gw_num
                        ),
                        None,
                    )

                    if matching_detailed:
                        for key, value in matching_detailed.items():
                            # Don't overwrite existing keys
                            if key not in gw_data:
                                gw_data[key] = value

        # Add summary stats for the filtered period
        period_stats = {}
        if history_data:
            # Calculate sums
            minutes = sum(gw.get("minutes", 0) for gw in history_data)
            points = sum(gw.get("total_points", 0) for gw in history_data)
            goals = sum(gw.get("goals_scored", 0) for gw in history_data)
            assists = sum(gw.get("assists", 0) for gw in history_data)
            bonus = sum(gw.get("bonus", 0) for gw in history_data)
            clean_sheets = sum(gw.get("clean_sheets", 0) for gw in history_data)

            # Calculate averages
            games_played = len(history_data)
            games_started = sum(1 for gw in history_data if gw.get("minutes", 0) >= 60)
            points_per_game = points / games_played if games_played > 0 else 0

            period_stats = {
                "gameweeks_analyzed": games_played,
                "games_started": games_started,
                "minutes": minutes,
                "total_points": points,
                "points_per_game": round(points_per_game, 1),
                "goals": goals,
                "assists": assists,
                "goal_involvements": goals + assists,
                "clean_sheets": clean_sheets,
                "bonus": bonus,
            }

        result["gameweek_range"] = {
            "start": start_gameweek,
            "end": end_gameweek,
        }

        result["gameweek_history"] = history_data
        result["period_stats"] = period_stats

    # Include upcoming fixtures if requested
    if include_fixtures and player_id is not None:
        fixtures_data = get_player_fixtures(player_id, 5)  # Next 5 fixtures

        if fixtures_data:
            result["upcoming_fixtures"] = fixtures_data

            # Calculate average fixture difficulty
            difficulty_values = [f.get("difficulty", 3) for f in fixtures_data]
            avg_difficulty = (
                sum(difficulty_values) / len(difficulty_values)
                if difficulty_values
                else 3
            )

            # Convert to a 1-10 scale where 10 is best (easiest fixtures)
            fixture_score = (6 - avg_difficulty) * 2

            result["fixture_analysis"] = {
                "difficulty_score": round(fixture_score, 1),
                "fixtures_analyzed": len(fixtures_data),
                "home_matches": sum(
                    1 for f in fixtures_data if f.get("location") == "home"
                ),
                "away_matches": sum(
                    1 for f in fixtures_data if f.get("location") == "away"
                ),
            }

            # Add fixture difficulty assessment
            if "fixture_analysis" in result and isinstance(
                result["fixture_analysis"], dict
            ):
                fixture_analysis = result["fixture_analysis"]
                if fixture_score >= 8:
                    fixture_analysis["assessment"] = "Excellent fixtures"
                elif fixture_score >= 6:
                    fixture_analysis["assessment"] = "Good fixtures"
                elif fixture_score >= 4:
                    fixture_analysis["assessment"] = "Average fixtures"
                else:
                    fixture_analysis["assessment"] = "Difficult fixtures"

    return result


def search_players(
    query: str, position: str | None = None, team: str | None = None, limit: int = 5
) -> dict[str, Any]:
    """
    Search for players by name with optional filtering by position and team.

    Args:
        query: Player name or partial name to search for
        position: Optional position filter (GKP, DEF, MID, FWD)
        team: Optional team name filter
        limit: Maximum number of results to return

    Returns:
        List of matching players with details
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Searching players: query={query}, position={position}, team={team}")

    # Find players by name
    matches = find_players_by_name(
        query, limit=limit * 2
    )  # Get more than needed for filtering

    # Apply position filter if specified
    if position and matches:
        matches = [p for p in matches if p.get("position") == position.upper()]

    # Apply team filter if specified
    if team and matches:
        matches = [
            p
            for p in matches
            if team.lower() in p.get("team", "").lower()
            or team.lower() in p.get("team_short", "").lower()
        ]

    # Limit results
    matches = matches[:limit]

    return {
        "query": query,
        "filters": {
            "position": position,
            "team": team,
        },
        "total_matches": len(matches),
        "players": matches,
    }


def get_teams_resource() -> list[dict[str, Any]]:
    """
    Format teams data for the MCP resource.

    Returns:
        Formatted teams data
    """
    # Get raw data from API
    data = api.get_bootstrap_static()

    # Format team data
    teams = []
    for team in data["teams"]:
        team_data = {
            "id": team["id"],
            "name": team["name"],
            "short_name": team["short_name"],
            "code": team["code"],
            # Strength ratings
            "strength": team["strength"],
            "strength_overall_home": team["strength_overall_home"],
            "strength_overall_away": team["strength_overall_away"],
            "strength_attack_home": team["strength_attack_home"],
            "strength_attack_away": team["strength_attack_away"],
            "strength_defence_home": team["strength_defence_home"],
            "strength_defence_away": team["strength_defence_away"],
            # Performance stats
            "position": team["position"],
        }

        teams.append(team_data)

    # Sort by position (league standing)
    teams.sort(key=lambda t: t["position"])

    return teams


def get_team_by_name(name: str) -> dict[str, Any] | None:
    """
    Get team data by name (full or partial match).

    Args:
        name: Team name to search for

    Returns:
        Team data or None if not found
    """
    teams = get_teams_resource()
    name_lower = name.lower()

    # Try exact match first
    for team in teams:
        if (
            team["name"].lower() == name_lower
            or team["short_name"].lower() == name_lower
        ):
            return team

    # Then try partial match
    for team in teams:
        if (
            name_lower in team["name"].lower()
            or name_lower in team["short_name"].lower()
        ):
            return team

    return None
