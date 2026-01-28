# Agent.md — Python + uv

Purpose
- This repository uses Python managed by uv for dependency resolution, virtual environments, locking, and execution. Always prefer uv subcommands (add/remove/run/sync/export) over raw pip/venv commands.

Core rules
- Use `uv add` to add or upgrade dependencies so that both `pyproject.toml` and `uv.lock` stay in sync; do not use `pip install` directly.
- Keep runtime dependencies in `[project.dependencies]` and development-only tools in the `dev` group via `uv add --dev ...`.
- Use `uv run` to execute Python, test, and tooling commands without manually activating a virtual environment.

Project bootstrap
- New project (scaffold files): `uv init`
- First install or clean install: `uv sync`
- Run the app: `uv run python -m <your_module>` or `uv run main.py`
- REPL: `uv run python`
- Scripts in pyproject: prefer `uv run <command>` to ensure the correct environment is used

Managing dependencies
- Add runtime dependency: `uv add <name>` (e.g., `uv add httpx`)
- Add dev dependencies: `uv add --dev pytest ruff`
- Pin/upgrade by constraint: `uv add "httpx>=0.27"` or adjust `pyproject.toml` and then `uv sync`
- Remove dependency: `uv remove <name>`
- Export lock for external tooling: `uv export --format requirements-txt --output-file requirements.txt`

Locking and environments
- `uv run` and `uv sync` will ensure the environment matches `pyproject.toml` and `uv.lock`
- Avoid manual `pip install` or manual `venv` activation; let uv manage the environment
- Commit `uv.lock` to version control for reproducible installs

pyproject guidance
- Dependencies live under `[project]` → `dependencies = [...]`
- Development-only tooling should go under a dev group (e.g., `uv add --dev ruff pytest`) for clean separation
- Keep `requires-python` current (e.g., `>=3.12`) to match the team’s baseline

Usage in this repo
- When adding libraries or changing versions, propose `uv add ...` changes that update both `pyproject.toml` and `uv.lock`, then run `uv run pytest -q` to validate
- Prefer minimal diffs, explain the plan, apply changes, and run tests/tooling via `uv run`
- If build/test fails, inspect error context, adjust constraints or code, and re-run via `uv run`

Common commands (copy/paste)
- Initialize: `uv init`  |  Install deps: `uv sync`
- Add runtime: `uv add <pkg>`  |  Add dev: `uv add --dev <pkg>`
- Remove: `uv remove <pkg>`
- Run app: `uv run python -m <your_module>` or `uv run main.py`
- Tests: `uv run pytest -q`
- Lint/format: `uv run ruff check .` and/or `uv run ruff format .`
- Export: `uv export --format requirements-txt --output-file requirements.txt`

Of course. Based on your request and the example `app.py` you provided, here is a new section that you can append to your `gemini.md` file. This section provides clear guidance on how to write effective tool names and descriptions, using the Perplexity `chat` function as a concrete example.

The proposed changes will make the function's purpose much clearer, especially its ability to access and cite real-time web information, which is a key feature.

***

### Tool Function Naming and Descriptions

To ensure the AI agent can effectively understand and use the tools available, function names and their descriptions (docstrings) must be clear, descriptive, and accurate. A good description outlines the tool's purpose, its key capabilities, and what it returns.

**Core Principles:**
- **Use Action-Oriented Names:** Function names should be verbs that clearly state what the tool *does* (e.g., `search`, `create_file`, `list_users`).
- **Be Specific in Descriptions:** The docstring is the primary source of context for the AI. It should explicitly mention the service it interacts with (e.g., "Perplexity AI") and its unique features (e.g., "performs real-time web searches," "provides citations").
- **Detail Inputs and Outputs:** Clearly describe the purpose of each argument and what the function returns, as this helps the agent formulate correct calls.

**Example: Improving the Perplexity Tool**

Let's refine the tool in `app.py` to be more descriptive and unlock its full potential. The original `chat` function is too generic. We will rename it to `search` and significantly improve its docstring.

**BEFORE:** The original function name and description are too simple.

```python
# from app.py
def chat(
    self,
    query: str,
    model: Literal[...] = "sonar",
    temperature: float = 1,
    system_prompt: str = "Be precise and concise.",
) -> dict[str, Any] | str:
    """
    Initiates a chat completion request to generate AI responses using various models with customizable parameters.
    ...
    Tags:
        chat, generate, ai, completion, important
    """
```

**AFTER:** The updated name and description are highly specific, highlighting the core web search and citation capabilities. Do not leave any empty lines between the descriptions.

```python
# from app.py
def search(
    self,
    query: str,
    model: Literal[
        "r1-1776",
        "sonar",
        "sonar-pro",
        "sonar-reasoning",
        "sonar-reasoning-pro",
        "sonar-deep-research",
    ] = "sonar-pro",
    temperature: float = 1,
    system_prompt: str = "You are a helpful AI assistant that answers questions using real-time information from the web.",
) -> dict[str, Any] | str:
    """
    Performs a real-time web search using Perplexity AI to answer a query with up-to-date information and citations.
    This tool is ideal for questions about current events, facts, or any topic that requires access to the latest information from the internet. It returns a natural language answer along with the sources used.

    Args:
        query: The search query or question to ask. For example: "What are the latest developments in AI regulation?"
        model: The Perplexity model to use. 'sonar-pro' is recommended for comprehensive, up-to-date answers.
        temperature: Controls randomness in the model's output. Higher values make the output more random, lower values make it more deterministic. Defaults to 1.
        system_prompt: The initial system message to guide the model's behavior.

    Returns:
        A dictionary containing the generated 'content' (str) and a list of 'citations' (list) from the web search.

    Raises:
        AuthenticationError: Raised when API authentication fails due to missing or invalid credentials.
        HTTPError: Raised when the API request fails or returns an error status.

    Tags:
        search, web, research, citations, current events, important
    """
```