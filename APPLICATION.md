# Application Development Guide

## Tool Function Naming and Descriptions

To ensure the AI agent can effectively understand and use the tools available, function names and their descriptions (docstrings) must be clear, descriptive, and accurate. A good description outlines the tool's purpose, its key capabilities, and what it returns.

### Core Principles
- **Use Action-Oriented Names:** Function names should be verbs that clearly state what the tool *does* (e.g., `search`, `create_file`, `list_users`).
- **Be Specific in Descriptions:** The docstring is the primary source of context for the AI. It should explicitly mention the service it interacts with (e.g., "Perplexity AI") and its unique features (e.g., "performs real-time web searches," "provides citations").
- **Detail Inputs and Outputs:** Clearly describe the purpose of each argument and what the function returns, as this helps the agent formulate correct calls.

### Example: Improving the Perplexity Tool

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

---

## Creating a New Application

This section provides a step-by-step workflow for creating a new API integration application from scratch.

### Application Creation Workflow

#### Step 1: Create the Application Structure

Create a new directory for your application with test file in the same location:
```bash
mkdir -p src/universal_mcp/applications/<app_name>
touch src/universal_mcp/applications/<app_name>/__init__.py
touch src/universal_mcp/applications/<app_name>/app.py
touch src/universal_mcp/applications/<app_name>/test_<app_name>_tools.py
```

**Directory Structure:**
```
src/universal_mcp/applications/<app_name>/
├── __init__.py
├── app.py                      # Application implementation
└── test_<app_name>_tools.py   # Tests (keep close to app.py)
```

**Basic Application Template:**
```python
from typing import Any
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class YourAppNameApp(APIApplication):
    """Brief description of what this API integration does."""

    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="your_app_name", integration=integration, **kwargs)
        self.base_url = "https://api.example.com"

    @staticmethod
    def _prepare_params(params: dict) -> dict:
        """Convert list values to comma-separated strings for API."""
        prepared = {}
        for key, value in params.items():
            if isinstance(value, list):
                prepared[key] = ','.join(str(v) for v in value)
            else:
                prepared[key] = value
        return prepared

    def list_tools(self):
        """Returns list of available tools (non-async)."""
        return [
            # Add your tool methods here
        ]
```

#### Step 2: List All Available API Endpoints

Before implementing tools, review the API documentation and create a comprehensive list of endpoints:

```python
# Document all available endpoints in comments first
# GET  /users/me - Get authenticated user info
# GET  /users/{id} - Get user by ID
# POST /posts - Create a new post
# GET  /posts/{id} - Get post by ID
# DELETE /posts/{id} - Delete a post
# etc.
```

Categorize endpoints by functionality:
- Authentication & User Operations
- Content Operations (Create, Read, Update, Delete)
- Social Interactions
- Settings & Configuration

#### Step 3: Implement Tools Using API Documentation

For each endpoint, create a tool method following these guidelines:

**Tool Implementation Pattern:**
```python
async def action_resource(
    self,
    required_param: str,
    optional_param: str = None,
    fields: list = None,
) -> dict[str, Any]:
    """
    Single-line summary of what this tool does (imperative mood).
    Additional context about the tool's purpose and when to use it.

    Args:
        required_param: Clear description with example. Example: 'user_12345'
        optional_param: Clear description with example. Example: 'filter_value'
        fields: Fields to include in response. Example: ['id', 'name', 'email']

    Returns:
        dict[str, Any]: Description of the return structure. Example: {'data': {...}, 'meta': {...}}

    Raises:
        ValueError: Raised when required parameters are missing.
        HTTPError: Raised when the API request fails (e.g., non-2XX status code).
        AuthenticationError: Raised when API authentication fails.

    Tags:
        category, action, important|slow|destructive
    """
    # Validate required parameters
    if required_param is None:
        raise ValueError("Missing required parameter 'required_param'.")

    # Build request body for POST/PUT/PATCH
    request_body_data = {
        "field1": optional_param,
        "field2": fields,
    }
    request_body_data = {k: v for k, v in request_body_data.items() if v is not None}

    # OR build query params for GET
    query_params = {
        k: v
        for k, v in [
            ("param1", optional_param),
            ("fields", fields),
        ]
        if v is not None
    }
    query_params = self._prepare_params(query_params) if query_params else {}

    # Make the API request (use appropriate async method)
    url = f"{self.base_url}/endpoint/{required_param}"
    response = await self._aget(url, params=query_params)  # GET
    # response = await self._apost(url, data=request_body_data, content_type="application/json")  # POST
    # response = await self._adelete(url)  # DELETE

    response.raise_for_status()
    return response.json()
```

#### Step 4: Write Tool Definitions Following Best Practices

**Best Practice 1: Use Proper Tags**

Tags help categorize and identify tool characteristics:
- `important` - Core functionality, frequently used
- `slow` - Operations that take significant time (>2 seconds)
- `destructive` - Operations that modify or delete data
- `elevated_access_required` - Requires premium/elevated API access
- Action tags: `create`, `read`, `update`, `delete`, `search`, `list`
- Resource tags: `user`, `post`, `message`, `file`, etc.

```python
# Example tags combinations:
# Tags: user, profile, me, authenticated, important
# Tags: post, create, destructive, important
# Tags: search, query, slow, elevated_access_required
# Tags: delete, remove, destructive, important
```

**Best Practice 2: Use Readable Names and Required Docstrings**

```python
# ✅ GOOD: Clear, action-oriented names
async def get_user_profile(self, user_id: str) -> dict[str, Any]:
async def create_post(self, text: str, media: list = None) -> dict[str, Any]:
async def delete_comment(self, comment_id: str) -> dict[str, Any]:
async def search_posts(self, query: str, max_results: int = 10) -> dict[str, Any]:

# ❌ BAD: Vague or confusing names
async def get_data(self, id: str) -> dict[str, Any]:
async def do_action(self, params: dict) -> dict[str, Any]:
async def process(self, input: str) -> dict[str, Any]:
```

Every tool MUST have a comprehensive docstring:
```python
async def create_post(
    self,
    text: str,
    media_ids: list = None,
    visibility: str = "public",
) -> dict[str, Any]:
    """
    Creates a new post with text content and optional media attachments.
    Posts are published immediately and appear on the user's profile and followers' timelines.

    Args:
        text: The content of the post. Example: 'Check out this amazing feature!'
        media_ids: Optional list of media IDs to attach. Example: ['media_123', 'media_456']
        visibility: Post visibility setting. Options: 'public', 'private', 'followers'. Default: 'public'

    Returns:
        dict[str, Any]: The created post object with 'id', 'text', 'created_at', and 'author' fields.

    Raises:
        ValueError: Raised when text is empty or exceeds character limit.
        HTTPError: Raised when the API request fails (e.g., non-2XX status code).

    Tags:
        post, create, publish, destructive, important
    """
```

**Best Practice 3: Specify Return Types in Docstrings**

Be explicit about what the tool returns:
```python
# ✅ GOOD: Detailed return type description
"""
Returns:
    dict[str, Any]: User object containing:
        - 'id' (str): Unique user identifier
        - 'username' (str): User's handle
        - 'email' (str): User's email address
        - 'created_at' (str): ISO 8601 timestamp
        - 'profile' (dict): Nested profile data
"""

# ✅ ALSO GOOD: Simple but clear
"""
Returns:
    dict[str, Any]: API response with 'data' containing user list and 'meta' with pagination info.
"""

# ❌ BAD: Vague or missing
"""
Returns:
    dict: The response
"""
```

**Best Practice 4: Include Only Necessary Parameters**

Only expose parameters that users need to control:

```python
# ✅ GOOD: Only essential user-facing parameters
async def get_user_posts(
    self,
    user_id: str,
    max_results: int = 10,
    include_retweets: bool = False,
) -> dict[str, Any]:
    """Get posts by a specific user."""
    # Internal implementation details hidden
    query_params = {
        "user_id": user_id,
        "count": max_results,
        "retweets": include_retweets,
        "api_version": "v2",  # Internal, not exposed as param
    }

# ❌ BAD: Exposing internal/unnecessary parameters
async def get_user_posts(
    self,
    user_id: str,
    max_results: int = 10,
    include_retweets: bool = False,
    api_version: str = "v2",  # Internal detail
    use_cache: bool = True,  # Internal optimization
    debug_mode: bool = False,  # Developer-only
) -> dict[str, Any]:
```

**Best Practice 5: One Tool = One Task**

Each tool should have a single, clear purpose:

```python
# ✅ GOOD: Single, focused tools
async def like_post(self, post_id: str) -> dict[str, Any]:
    """Likes a specific post."""

async def unlike_post(self, post_id: str) -> dict[str, Any]:
    """Removes a like from a post."""

async def get_post_likes(self, post_id: str, max_results: int = 10) -> dict[str, Any]:
    """Retrieves users who liked a post."""

# ❌ BAD: Multi-purpose tool with action parameter
async def manage_post_like(
    self,
    post_id: str,
    action: str,  # 'like', 'unlike', 'get_likes'
) -> dict[str, Any]:
    """Manages likes on a post."""
    if action == "like":
        # like logic
    elif action == "unlike":
        # unlike logic
    elif action == "get_likes":
        # get likes logic
```

**Best Practice 6: Inject Credentials via Integration**

All applications requiring authentication should use dependency injection:

```python
# ✅ GOOD: Integration-based authentication
class TwitterApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="twitter", integration=integration, **kwargs)
        self.base_url = "https://api.twitter.com"

    async def create_post(self, text: str) -> dict[str, Any]:
        """Creates a post using authenticated credentials."""
        url = f"{self.base_url}/2/tweets"
        # Credentials automatically injected via self._apost
        response = await self._apost(url, data={"text": text}, content_type="application/json")
        return response.json()

# ❌ BAD: Manual credential management
class TwitterApp(APIApplication):
    def __init__(self, api_key: str, api_secret: str, **kwargs):
        self.api_key = api_key
        self.api_secret = api_secret

    async def create_post(self, text: str, bearer_token: str) -> dict[str, Any]:
        """Creates a post."""
        headers = {"Authorization": f"Bearer {bearer_token}"}
        # Manual credential handling - bad!
```

**Best Practice 7: All Tools Should Be Async by Default**

Use async/await for all tool methods (except `list_tools`):

```python
# ✅ GOOD: Async methods using async HTTP calls
async def get_user(self, user_id: str) -> dict[str, Any]:
    """Retrieves user information."""
    url = f"{self.base_url}/users/{user_id}"
    response = await self._aget(url)  # Async GET
    response.raise_for_status()
    return response.json()

async def create_post(self, text: str) -> dict[str, Any]:
    """Creates a new post."""
    url = f"{self.base_url}/posts"
    response = await self._apost(url, data={"text": text}, content_type="application/json")  # Async POST
    response.raise_for_status()
    return response.json()

async def delete_post(self, post_id: str) -> dict[str, Any]:
    """Deletes a post."""
    url = f"{self.base_url}/posts/{post_id}"
    response = await self._adelete(url)  # Async DELETE
    response.raise_for_status()
    return response.json()

# ✅ EXCEPTION: list_tools is synchronous
def list_tools(self):
    """Returns list of available tools."""
    return [self.get_user, self.create_post, self.delete_post]

# ❌ BAD: Synchronous methods (deprecated)
def get_user(self, user_id: str) -> dict[str, Any]:
    response = self._get(url)  # Don't use synchronous _get
    return response.json()
```

**Best Practice 8: Provide Authenticated User Info Endpoint**

If the API supports getting the currently authenticated user, implement a dedicated method:

```python
async def get_authenticated_user(
    self,
    user_fields: list = None,
) -> dict[str, Any]:
    """
    Retrieves detailed information about the currently authenticated user making the API request.
    Returns profile data for the account whose credentials are being used.

    Args:
        user_fields: User fields to display. Example: ['id', 'name', 'email', 'created_at']

    Returns:
        dict[str, Any]: Authenticated user's profile data and requested fields.

    Raises:
        HTTPError: Raised when the API request fails (e.g., non-2XX status code).
        AuthenticationError: Raised when API authentication fails.

    Tags:
        user, profile, me, authenticated, important
    """
    url = f"{self.base_url}/users/me"  # or /me, /account, etc.
    query_params = {
        k: v
        for k, v in [
            ("fields", user_fields),
        ]
        if v is not None
    }
    query_params = self._prepare_params(query_params) if query_params else {}
    response = await self._aget(url, params=query_params)
    response.raise_for_status()
    return response.json()
```

This is especially useful for:
- Initializing tests with the user's ID
- Verifying authentication status
- Getting user-specific defaults
- Other methods that need the current user's ID

**Using authenticated user info internally:**
```python
async def get_my_posts(
    self,
    max_results: int = 10,
) -> dict[str, Any]:
    """
    Retrieves posts created by the authenticated user.

    Args:
        max_results: Maximum number of posts to return.

    Returns:
        dict[str, Any]: List of user's posts.
    """
    # Get authenticated user's ID
    user = await self.get_authenticated_user()
    user_id = user.get("data", {}).get("id")

    # Use the ID to fetch posts
    url = f"{self.base_url}/users/{user_id}/posts"
    query_params = {"max_results": max_results}
    response = await self._aget(url, params=query_params)
    response.raise_for_status()
    return response.json()
```

### Quick Reference Checklist

When creating a new application, ensure:

- [ ] Application class inherits from `APIApplication`
- [ ] Integration is injected via `__init__` parameter
- [ ] All tool methods are `async` (except `list_tools`)
- [ ] Each tool has comprehensive docstring with Args, Returns, Raises, Tags
- [ ] Tool names are action-oriented and descriptive
- [ ] Each tool performs one clear task
- [ ] Required parameters are validated
- [ ] List parameters are handled via `_prepare_params()`
- [ ] Appropriate HTTP methods used (`_aget`, `_apost`, `_adelete`)
- [ ] Tags include: action, resource, and modifiers (important/slow/destructive)
- [ ] `get_authenticated_user()` method implemented if API supports it
- [ ] Test file created in same directory as `app.py`
- [ ] Test file named `test_<app_name>_tools.py`
- [ ] Tests use `AgentrIntegration` for authentication
- [ ] All tests are `async` functions with `await` calls

### Example: Complete Minimal Application

```python
from typing import Any
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class MinimalApp(APIApplication):
    """Minimal example application demonstrating best practices."""

    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="minimal", integration=integration, **kwargs)
        self.base_url = "https://api.example.com/v1"

    async def get_authenticated_user(self) -> dict[str, Any]:
        """
        Retrieves information about the currently authenticated user.

        Returns:
            dict[str, Any]: User object with 'id', 'username', and 'email' fields.

        Raises:
            HTTPError: Raised when the API request fails.

        Tags:
            user, me, authenticated, important
        """
        url = f"{self.base_url}/me"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def get_item(self, item_id: str) -> dict[str, Any]:
        """
        Retrieves a specific item by its unique ID.

        Args:
            item_id: The unique identifier of the item. Example: 'item_12345'

        Returns:
            dict[str, Any]: Item object with 'id', 'name', 'description', and 'created_at' fields.

        Raises:
            ValueError: Raised when item_id is missing.
            HTTPError: Raised when the API request fails.

        Tags:
            item, get, retrieve, important
        """
        if item_id is None:
            raise ValueError("Missing required parameter 'item_id'.")

        url = f"{self.base_url}/items/{item_id}"
        response = await self._aget(url)
        response.raise_for_status()
        return response.json()

    async def create_item(
        self,
        name: str,
        description: str = None,
    ) -> dict[str, Any]:
        """
        Creates a new item with specified name and optional description.

        Args:
            name: The name of the item to create. Example: 'My New Item'
            description: Optional description. Example: 'This item is for testing'

        Returns:
            dict[str, Any]: The created item object with 'id' and other fields.

        Raises:
            ValueError: Raised when name is missing.
            HTTPError: Raised when the API request fails.

        Tags:
            item, create, destructive, important
        """
        if name is None:
            raise ValueError("Missing required parameter 'name'.")

        request_body_data = {
            "name": name,
            "description": description,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}

        url = f"{self.base_url}/items"
        response = await self._apost(url, data=request_body_data, content_type="application/json")
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        """Returns list of available tools."""
        return [
            self.get_authenticated_user,
            self.get_item,
            self.create_item,
        ]
```

This comprehensive guide ensures consistent, high-quality API integrations that are easy to use, test, and maintain.
