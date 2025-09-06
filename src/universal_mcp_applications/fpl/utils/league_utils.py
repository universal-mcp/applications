from typing import Any


def parse_league_standings(data: dict[str, Any]) -> dict[str, Any]:
    """
    Parse league standings data into a more usable format

    Args:
        data: Raw league data from the API

    Returns:
        Parsed league data
    """
    # Handle error responses
    if "error" in data:
        return data

    # Parse league info
    league_info = {
        "id": data.get("league", {}).get("id"),
        "name": data.get("league", {}).get("name"),
        "created": data.get("league", {}).get("created"),
        "type": "Public"
        if data.get("league", {}).get("league_type") == "s"
        else "Private",
        "scoring": "Classic"
        if data.get("league", {}).get("scoring") == "c"
        else "Head-to-Head",
        "admin_entry": data.get("league", {}).get("admin_entry"),
        "start_event": data.get("league", {}).get("start_event"),
    }

    # Parse standings
    standings = data.get("standings", {}).get("results", [])

    # Get total count
    total_count = len(standings)

    # Format standings
    formatted_standings = []
    for standing in standings:
        team = {
            "id": standing.get("id"),
            "team_id": standing.get("entry"),
            "team_name": standing.get("entry_name"),
            "manager_name": standing.get("player_name"),
            "rank": standing.get("rank"),
            "last_rank": standing.get("last_rank"),
            "rank_change": standing.get("last_rank", 0) - standing.get("rank", 0)
            if standing.get("last_rank") and standing.get("rank")
            else 0,
            "total_points": standing.get("total"),
            "event_total": standing.get("event_total"),
        }
        formatted_standings.append(team)

    response = {
        "league_info": league_info,
        "standings": formatted_standings[:25],  # Limit to top 25 teams
        "total_teams": total_count,
    }

    if len(formatted_standings) > 25:
        response["disclaimers"] = ["Limited to top 25 teams"]

    return response


def get_teams_historical_data(
    team_ids: list[int], api, start_gw: int | None = None, end_gw: int | None = None
) -> dict[str, Any]:
    """Get historical data for multiple teams"""
    results = {}
    errors = {}

    # Validate and process gameweek range
    try:
        if end_gw is None or end_gw == "current":
            current_gw_data = api.get_current_gameweek()
            current_gw = current_gw_data.get("id", 38)
            end_gw = current_gw
        elif isinstance(end_gw, str) and end_gw.startswith("current-"):
            current_gw_data = api.get_current_gameweek()
            current_gw = current_gw_data.get("id", 38)
            offset = int(end_gw.split("-")[1])
            end_gw = max(1, current_gw - offset)

        if start_gw is None:
            start_gw = 1
        elif isinstance(start_gw, str) and start_gw.startswith("current-"):
            current_gw_data = api.get_current_gameweek()
            current_gw = current_gw_data.get("id", 38)
            offset = int(start_gw.split("-")[1])
            start_gw = max(1, current_gw - offset)

        start_gw = int(start_gw) if start_gw is not None else 1
        end_gw = int(end_gw) if end_gw is not None else 38

        start_gw = max(start_gw, 1)
        end_gw = min(end_gw, 38)
        if start_gw > end_gw:
            start_gw, end_gw = end_gw, start_gw

    except Exception as e:
        return {
            "error": f"Invalid gameweek range: {str(e)}",
            "suggestion": "Use numeric values or 'current'/'current-N' format",
        }

    # Get history data for each team
    for team_id in team_ids:
        try:
            # Use the API class to make the request
            history_data = api._make_request(f"entry/{team_id}/history/")

            if "current" in history_data:
                current = [
                    gw
                    for gw in history_data["current"]
                    if start_gw <= gw.get("event", 0) <= end_gw
                ]

                filtered_data = {
                    "current": current,
                    "past": history_data.get("past", []),
                    "chips": history_data.get("chips", []),
                }

                results[team_id] = filtered_data
            else:
                errors[team_id] = "No historical data found"

        except Exception as e:
            errors[team_id] = str(e)

    return {
        "teams_data": results,
        "errors": errors,
        "gameweek_range": {"start": start_gw, "end": end_gw},
        "success_rate": len(results) / len(team_ids) if team_ids else 0,
    }


def _get_league_standings(league_id: int, api) -> dict[str, Any]:
    """Get standings for a specified FPL league"""
    try:
        # Use the API class to make the request
        data = api._make_request(f"leagues-classic/{league_id}/standings/")
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}

    # Import parse_league_standings from the user's api.py or define a simple version here
    # For now, we'll define a simple version
    if "error" in data:
        return data

    league_info = {
        "id": data.get("league", {}).get("id"),
        "name": data.get("league", {}).get("name"),
        "created": data.get("league", {}).get("created"),
        "type": "Public"
        if data.get("league", {}).get("league_type") == "s"
        else "Private",
        "scoring": "Classic"
        if data.get("league", {}).get("scoring") == "c"
        else "Head-to-Head",
        "admin_entry": data.get("league", {}).get("admin_entry"),
        "start_event": data.get("league", {}).get("start_event"),
    }

    standings = data.get("standings", {}).get("results", [])
    total_count = len(standings)

    formatted_standings = []
    for standing in standings:
        team = {
            "id": standing.get("id"),
            "team_id": standing.get("entry"),
            "team_name": standing.get("entry_name"),
            "manager_name": standing.get("player_name"),
            "rank": standing.get("rank"),
            "last_rank": standing.get("last_rank"),
            "rank_change": standing.get("last_rank", 0) - standing.get("rank", 0)
            if standing.get("last_rank") and standing.get("rank")
            else 0,
            "total_points": standing.get("total"),
            "event_total": standing.get("event_total"),
        }
        formatted_standings.append(team)

    response_data = {
        "league_info": league_info,
        "standings": formatted_standings[:25],
        "total_teams": total_count,
    }

    if len(formatted_standings) > 25:
        response_data["disclaimers"] = ["Limited to top 25 teams"]

    return response_data


def _get_league_historical_performance(
    league_id: int,
    api,  # noqa: F821
    start_gw: int | None = None,
    end_gw: int | None = None,
) -> dict[str, Any]:
    """Get historical performance data for teams in a league"""
    league_data = _get_league_standings(league_id, api)

    if "error" in league_data:
        return league_data

    if "standings" in league_data and len(league_data["standings"]) > 25:
        league_data["standings"] = league_data["standings"][:25]
        league_data["limited_to_top"] = 25

    team_ids = [team["team_id"] for team in league_data["standings"]]

    historical_data = get_teams_historical_data(team_ids, api, start_gw, end_gw)

    if "error" in historical_data:
        return historical_data

    teams_data = historical_data["teams_data"]
    gameweek_range = historical_data["gameweek_range"]

    gameweeks = list(range(gameweek_range["start"], gameweek_range["end"] + 1))

    series = []
    for team in league_data["standings"]:
        team_id = team["team_id"]

        if team_id not in teams_data:
            continue

        current = teams_data[team_id].get("current", [])

        points_series = []
        rank_series = []
        value_series = []

        for gw in gameweeks:
            gw_data = next((g for g in current if g.get("event") == gw), None)

            if gw_data:
                points_series.append(gw_data.get("points", 0))
                rank_series.append(gw_data.get("overall_rank", 0))
                value_series.append(
                    gw_data.get("value", 0) / 10.0 if gw_data.get("value") else 0
                )
            else:
                points_series.append(0)
                rank_series.append(0)
                value_series.append(0)

        series.append(
            {
                "team_id": team_id,
                "name": team["team_name"],
                "manager": team["manager_name"],
                "points_series": points_series,
                "rank_series": rank_series,
                "value_series": value_series,
                "current_rank": team["rank"],
                "total_points": team["total_points"],
            }
        )

    gameweek_winners = {}
    for gw_index, gw in enumerate(gameweeks):
        max_points = 0
        winner = None

        for team in series:
            points = team["points_series"][gw_index]
            if points > max_points:
                max_points = points
                winner = {
                    "team_id": team["team_id"],
                    "name": team["name"],
                    "points": points,
                }

        if winner:
            gameweek_winners[str(gw)] = winner

    for team in series:
        rank_variance = 0
        valid_ranks = [r for r in team["rank_series"] if r > 0]

        if valid_ranks:
            mean_rank = sum(valid_ranks) / len(valid_ranks)
            rank_variance = sum((r - mean_rank) ** 2 for r in valid_ranks) / len(
                valid_ranks
            )
            consistency_score = 10.0 - min(10.0, (rank_variance / 1000000) * 10)
            team["consistency_score"] = round(consistency_score, 1)
        else:
            team["consistency_score"] = 0

    return {
        "league_info": league_data["league_info"],
        "gameweeks": gameweeks,
        "teams": series,
        "gameweek_winners": gameweek_winners,
        "errors": historical_data["errors"],
        "success_rate": historical_data["success_rate"],
    }


def _get_league_team_composition(
    league_id: int,
    api,  # noqa: F821
    gameweek: int | None = None,
) -> dict[str, Any]:
    """Get team composition analysis for a league"""
    league_data = _get_league_standings(league_id, api)

    if "error" in league_data:
        return league_data

    if "standings" in league_data and len(league_data["standings"]) > 25:
        league_data["standings"] = league_data["standings"][:25]
        league_data["limited_to_top"] = 25

    team_ids = [team["team_id"] for team in league_data["standings"]]

    if gameweek is None:
        current_gw_data = api.get_current_gameweek()
        gameweek = current_gw_data.get("id", 1)

    try:
        gameweek = int(gameweek) if gameweek is not None else 1
    except (ValueError, TypeError):
        return {"error": f"Invalid gameweek value: {gameweek}"}

    static_data = api.get_bootstrap_static()
    all_players = static_data.get("elements", [])

    teams_map = {t["id"]: t for t in static_data.get("teams", [])}
    positions_map = {p["id"]: p for p in static_data.get("element_types", [])}

    players_map = {}
    for p in all_players:
        player = dict(p)

        team_id = player.get("team")
        if team_id and team_id in teams_map:
            player["team_short"] = teams_map[team_id].get("short_name")

        position_id = player.get("element_type")
        if position_id and position_id in positions_map:
            player["position"] = positions_map[position_id].get("singular_name_short")

        players_map[player["id"]] = player

    teams_data = {}
    errors = {}

    for team_id in team_ids:
        try:
            # Use the API class to make the request
            picks_data = api._make_request(f"entry/{team_id}/event/{gameweek}/picks/")
            teams_data[team_id] = picks_data

        except Exception as e:
            errors[team_id] = str(e)

    if not teams_data:
        return {
            "error": "Failed to retrieve team data for any teams in the league",
            "errors": errors,
        }

    player_ownership = {}
    captain_picks = {}
    vice_captain_picks = {}
    position_distribution = {"GKP": {}, "DEF": {}, "MID": {}, "FWD": {}}
    team_values = {}

    for team_id, team_data in teams_data.items():
        team_info = next(
            (t for t in league_data["standings"] if t["team_id"] == team_id), None
        )
        if not team_info:
            continue

        picks = team_data.get("picks", [])
        entry_history = team_data.get("entry_history", {})

        team_values[team_id] = {
            "team_name": team_info["team_name"],
            "manager_name": team_info["manager_name"],
            "bank": entry_history.get("bank", 0) / 10.0 if entry_history else 0,
            "value": entry_history.get("value", 0) / 10.0 if entry_history else 0,
        }

        for pick in picks:
            player_id = pick.get("element")
            if not player_id:
                continue

            player_data = players_map.get(player_id, {})
            if not player_data:
                continue

            if player_id not in player_ownership:
                position = player_data.get("position", "UNK")
                full_name = f"{player_data.get('first_name', '')} {player_data.get('second_name', '')}"
                player_ownership[player_id] = {
                    "id": player_id,
                    "name": player_data.get("web_name", "Unknown"),
                    "full_name": full_name.strip() or "Unknown",
                    "position": position,
                    "team": player_data.get("team_short", "UNK"),
                    "price": player_data.get("now_cost", 0) / 10.0
                    if player_data.get("now_cost")
                    else 0,
                    "form": float(player_data.get("form", "0.0"))
                    if player_data.get("form")
                    else 0,
                    "total_points": player_data.get("total_points", 0),
                    "points_per_game": float(player_data.get("points_per_game", "0.0"))
                    if player_data.get("points_per_game")
                    else 0,
                    "ownership_count": 0,
                    "ownership_percent": 0,
                    "captain_count": 0,
                    "vice_captain_count": 0,
                    "teams": [],
                }

            player_ownership[player_id]["ownership_count"] += 1
            player_ownership[player_id]["teams"].append(
                {
                    "team_id": team_id,
                    "team_name": team_info["team_name"],
                    "manager_name": team_info["manager_name"],
                    "is_captain": pick.get("is_captain", False),
                    "is_vice_captain": pick.get("is_vice_captain", False),
                    "multiplier": pick.get("multiplier", 0),
                    "position": pick.get("position", 0),
                }
            )

            if pick.get("is_captain", False):
                if player_id not in captain_picks:
                    captain_picks[player_id] = 0
                captain_picks[player_id] += 1
                player_ownership[player_id]["captain_count"] += 1

            if pick.get("is_vice_captain", False):
                if player_id not in vice_captain_picks:
                    vice_captain_picks[player_id] = 0
                vice_captain_picks[player_id] += 1
                player_ownership[player_id]["vice_captain_count"] += 1

            position = player_data.get("position", "UNK")
            if position in position_distribution:
                if player_id not in position_distribution[position]:
                    position_distribution[position][player_id] = 0
                position_distribution[position][player_id] += 1

    team_count = len(teams_data)
    for player_id, player in player_ownership.items():
        player["ownership_percent"] = round(
            (player["ownership_count"] / team_count) * 100, 1
        )

    players_by_ownership = sorted(
        player_ownership.values(),
        key=lambda p: (p["ownership_percent"], p["total_points"]),
        reverse=True,
    )

    template_threshold = 30.0
    differential_threshold = 10.0

    template_players = [
        p for p in players_by_ownership if p["ownership_percent"] > template_threshold
    ]
    differential_players = [
        p
        for p in players_by_ownership
        if 0 < p["ownership_percent"] < differential_threshold
    ]

    position_order = {"GKP": 1, "DEF": 2, "MID": 3, "FWD": 4, "UNK": 5}
    template_players.sort(
        key=lambda p: (position_order.get(p["position"], 5), -p["ownership_percent"])
    )
    differential_players.sort(
        key=lambda p: (position_order.get(p["position"], 5), -p["total_points"])
    )

    captain_data = []
    for player_id, count in sorted(
        captain_picks.items(), key=lambda x: x[1], reverse=True
    ):
        if player_id in player_ownership:
            player = player_ownership[player_id]
            captain_data.append(
                {
                    "id": player_id,
                    "name": player["name"],
                    "count": count,
                    "percent": round((count / team_count) * 100, 1),
                    "position": player["position"],
                    "team": player["team"],
                    "points": player["total_points"],
                }
            )

    value_stats = {}
    for team_id, value_data in team_values.items():
        value_stats[team_id] = {
            "team_name": value_data["team_name"],
            "manager_name": value_data["manager_name"],
            "bank": value_data["bank"],
            "team_value": value_data["value"],
        }

    sorted_value_stats = sorted(
        value_stats.values(), key=lambda v: v["team_value"], reverse=True
    )

    PLAYER_LIMIT = 25

    return {
        "league_info": league_data["league_info"],
        "gameweek": gameweek,
        "teams_analyzed": team_count,
        "player_ownership": {
            "all_players": players_by_ownership[:PLAYER_LIMIT],
            "template_players": template_players[:PLAYER_LIMIT],
            "differential_players": differential_players[:PLAYER_LIMIT],
            "captain_picks": captain_data[:PLAYER_LIMIT]
            if len(captain_data) > PLAYER_LIMIT
            else captain_data,
        },
        "team_values": sorted_value_stats,
        "errors": errors,
        "success_rate": len(teams_data) / len(team_ids) if team_ids else 0,
    }
