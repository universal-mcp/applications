# FplApp MCP Server

An MCP Server for the FplApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the FplApp API.


| Tool | Description |
|------|-------------|
| `get_player_information` | Fetches a detailed profile for a specific FPL player, identified by ID or name. It can include gameweek performance history, filterable by range, and future fixtures. This provides an in-depth look at one player, differing from broader search or analysis functions like `search_fpl_players`. |
| `find_players` | Searches for FPL players by full or partial name with optional filtering by team and position. This is a discovery tool, differentiating it from `get_player_information` which fetches a specific known player. It serves as a public interface to the internal `search_players` utility. |
| `get_gameweek_snapshot` | Provides a detailed snapshot of the FPL schedule by identifying the current, previous, and next gameweeks. It calculates the precise real-time status of the current gameweek (e.g., 'Imminent', 'In Progress') and returns key deadline times and overall season progress. |
| `screen_players` | Filters the FPL player database using multiple criteria like position, price, points, and form. Returns a sorted list of matching players, summary statistics for the filtered group, and optional recent gameweek performance data to aid in player discovery and analysis. |
| `compare_players` | Performs a detailed comparison of multiple players based on specified metrics, recent gameweek history, and upcoming fixture analysis. It provides a side-by-side breakdown, identifies the best performer per metric, and determines an overall winner, considering fixture difficulty, blanks, and doubles for a comprehensive overview. |
| `analyze_player_fixtures` | Analyzes a player's upcoming fixture difficulty. Given a player's name, it retrieves their schedule for a set number of matches, returning a detailed list and a calculated difficulty rating. This method is a focused alternative to the more comprehensive `analyze_fixtures` function. |
| `analyze_entity_fixtures` | Provides a detailed fixture difficulty analysis for a specific player, team, or an entire position over a set number of gameweeks. It calculates a difficulty score and can include blank/double gameweek data, offering broader analysis than the player-only `analyze_player_fixtures`. |
| `get_blank_gameweeks` | Identifies upcoming 'blank' gameweeks where teams lack a scheduled fixture. The function returns a list detailing each blank gameweek and the affected teams within a specified number of weeks, which is essential for strategic planning. It is distinct from `get_double_gameweeks`. |
| `get_double_gameweeks` | Identifies upcoming double gameweeks where teams have multiple fixtures within a specified number of weeks. It returns a list detailing each double gameweek and the teams involved. This function specifically finds gameweeks with extra matches, unlike `get_blank_gameweeks` which finds those with none. |
| `get_league_standings` | Retrieves current standings for a specified FPL classic mini-league by its ID. It fetches and parses raw API data to provide a direct snapshot of the league table, distinguishing it from `get_league_analytics` which performs deeper, historical analysis. |
| `analyze_league` | Performs advanced analysis on an FPL league for a given gameweek range. It routes requests based on the analysis type ('overview', 'historical', 'team_composition') to provide deeper insights beyond the basic rankings from `get_league_standings`, such as historical performance or team composition. |
| `get_manager_team_info` | Retrieves detailed information for a specific FPL manager's team (an "entry") using its unique ID. This is distinct from functions analyzing Premier League clubs, as it targets an individual user's fantasy squad and its performance details within the game. |
