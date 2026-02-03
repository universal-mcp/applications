# Testing Applications and API Integrations

After building an application with API integration, comprehensive testing ensures all tools function correctly before deployment. This section covers testing philosophy, setup, and best practices learned from real-world API testing.

## Testing Philosophy

**Test Early and Often:**
- Test non-destructive (read-only) operations first before testing any write operations
- Verify authentication and basic connectivity before testing complex workflows
- Use real API credentials in a controlled test environment to catch integration issues

**Categorize Your Tests:**
1. **Authentication Tests** - Verify credentials and API access
2. **Read Operations** - Test all GET endpoints that don't modify data
3. **Write Operations** - Test POST/PUT/DELETE endpoints (after read tests pass)
4. **Error Handling** - Test API error responses and rate limiting
5. **Edge Cases** - Test with missing parameters, invalid data, etc.

## Test Script Structure

**Best Practice:** Always create test files in the same directory as the application code to keep related files together.

Create a dedicated test file `test_<app_name>_tools.py` in the same directory as `app.py` that systematically tests all tools:

**Location:** `src/universal_mcp/applications/<app_name>/test_<app_name>_tools.py`

```python
"""
Comprehensive test script for <App> API non-destructive tools.
Tests all read-only operations to verify they work correctly.
"""
import asyncio
from typing import Any
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.<app_name>.app import <AppClass>


class <App>ToolTester:
    def __init__(self):
        # Initialize integration and app
        self.integration = AgentrIntegration(name='<app_name>')
        self.app = <AppClass>(integration=self.integration)
        self.results = {}
        # Store frequently used IDs or data
        self.user_id = None

    def log_result(self, tool_name: str, success: bool, message: str = "", data: Any = None):
        """Log test result for a tool."""
        status = "✓ PASS" if success else "✗ FAIL"
        self.results[tool_name] = {"success": success, "message": message, "data": data}
        print(f"{status} | {tool_name}: {message}")
        if data and success:
            print(f"    Sample data: {str(data)[:200]}...")

    async def test_<operation_name>(self):
        """Test <operation> functionality."""
        try:
            result = await self.app.<method_name>(
                param1="value1",
                param2=["field1", "field2"]  # List parameters
            )

            # Check for successful response
            if "data" in result:
                self.log_result("<operation_name>", True, "Success message", result["data"])
                return True
            elif "meta" in result:
                # Empty but valid response
                self.log_result("<operation_name>", True, "No data (valid response)")
                return True
            else:
                self.log_result("<operation_name>", False, "Unexpected response", result)
                return False

        except Exception as e:
            self.log_result("<operation_name>", False, f"Error: {str(e)}")
            return False

    async def run_all_tests(self):
        """Run all non-destructive tests in logical order."""
        print("\n" + "="*80)
        print("<APP NAME> API NON-DESTRUCTIVE TOOLS TEST")
        print("="*80 + "\n")

        # Group tests by category
        tests = [
            ("Category 1", [
                self.test_operation1,
                self.test_operation2,
            ]),
            ("Category 2", [
                self.test_operation3,
                self.test_operation4,
            ]),
        ]

        for category, test_funcs in tests:
            print(f"\n{category}")
            print("-" * 80)
            for test_func in test_funcs:
                await test_func()

        # Print summary
        self._print_summary()

        total = len(self.results)
        passed = sum(1 for r in self.results.values() if r["success"])
        return passed == total

    def _print_summary(self):
        """Print test summary."""
        print("\n" + "="*80)
        print("TEST SUMMARY")
        print("="*80)

        total = len(self.results)
        passed = sum(1 for r in self.results.values() if r["success"])
        failed = total - passed

        print(f"\nTotal Tests: {total}")
        print(f"Passed: {passed} ✓")
        print(f"Failed: {failed} ✗")
        print(f"Success Rate: {(passed/total*100):.1f}%\n")

        if failed > 0:
            print("Failed Tests:")
            for name, result in self.results.items():
                if not result["success"]:
                    print(f"  - {name}: {result['message']}")

        print("="*80 + "\n")


async def main():
    """Main test runner."""
    tester = <App>ToolTester()
    try:
        success = await tester.run_all_tests()
        return 0 if success else 1
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(asyncio.run(main()))
```

## Key Testing Patterns

**1. Integration Setup:**
```python
# Always initialize with AgentrIntegration
integration = AgentrIntegration(name='app_name')
app = AppClass(integration=integration)
```

**2. Handling API Response Types:**
```python
# Most APIs return different response structures
if "data" in result:
    # Primary data found
    count = len(result["data"]) if isinstance(result["data"], list) else 1
    process_data(result["data"])

elif "meta" in result:
    # Valid empty response
    print("No data found (valid response)")

elif "errors" in result:
    # API returned errors
    handle_errors(result["errors"])

else:
    # Unexpected format
    print(f"Unexpected response: {result}")
```

**3. Testing List Parameters:**
```python
# Many APIs require comma-separated lists
result = await app.get_item(
    item_id="123",
    fields=["field1", "field2", "field3"]  # Pass as Python list
)
# The app should handle conversion to API format (e.g., "field1,field2,field3")
```

**4. Error Handling and Interpretation:**
```python
try:
    result = await app.some_operation()
except Exception as e:
    error_msg = str(e)

    # Rate limiting
    if "429" in error_msg:
        print("Rate limit exceeded - wait before retrying")

    # Permission denied
    elif "403" in error_msg:
        print("Insufficient API access level or permissions")

    # Bad request
    elif "400" in error_msg:
        print("Invalid parameters - check API documentation")

    # Authentication failed
    elif "401" in error_msg:
        print("Authentication failed - check credentials")
```

**5. Dependent Tests:**
```python
async def test_get_user_info(self):
    """Get authenticated user - stores ID for later tests."""
    result = await self.app.get_authenticated_user()
    if "data" in result and "id" in result["data"]:
        self.user_id = result["data"]["id"]  # Store for other tests
        return True
    return False

async def test_get_user_tweets(self):
    """Get user tweets - requires user_id from previous test."""
    if not self.user_id:
        self.log_result("get_user_tweets", False, "Skipped - no user_id available")
        return False

    result = await self.app.get_tweets(user_id=self.user_id)
    # ... test logic
```

## Common API Testing Issues and Solutions

**Issue 1: List Parameters Not Working**
```python
# PROBLEM: API receives ?fields=field1&fields=field2&fields=field3
# SOLUTION: Convert list to comma-separated string

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

# Use in every method that accepts query parameters
async def get_data(self, fields: list = None):
    query_params = {"fields": fields} if fields else {}
    query_params = self._prepare_params(query_params)  # Convert lists
    response = await self._aget(url, params=query_params)
```

**Issue 2: Authentication Failures**
```python
# Check if integration is properly initialized
integration = AgentrIntegration(name='app_name')  # Must match registered name
app = AppClass(integration=integration)

# Test authentication explicitly first
try:
    result = await app.get_authenticated_user()  # Or similar auth test endpoint
    print(f"✓ Authentication successful: {result}")
except Exception as e:
    print(f"✗ Authentication failed: {e}")
    # User will be prompted to authorize via OAuth flow
```

**Issue 3: Rate Limiting**
```python
# Add delays between test runs or use focused tests
import time

for test in tests:
    result = await test()
    time.sleep(0.5)  # Small delay to avoid rate limits

# Or create focused test scripts for specific endpoints
# test_dm_events.py - tests only DM functionality
```

## Testing Workflow

**Step 1: Basic Tool Listing**
```python
# Quick check to see all available tools
async def main():
    integration = AgentrIntegration(name='app_name')
    app = AppClass(integration=integration)
    tools = app.list_tools()
    print(f"Available tools: {[t.__name__ for t in tools]}")
```

**Step 2: Authentication Test**
```python
# Verify credentials work before running full suite
uv run python test_auth.py
```

**Step 3: Non-Destructive Tests**
```python
# Test all read operations
uv run python test_<app>_tools.py
```

**Step 4: Focused Testing**
```python
# Test specific functionality in isolation
uv run python test_specific_feature.py
```

**Step 5: Review Results**
- Check success rate (aim for 100% on accessible endpoints)
- Identify API access level issues (403 Forbidden)
- Note rate limiting (429 Too Many Requests)
- Fix code issues (400 Bad Request often means parameter problems)

## Best Practices Summary

**DO:**
- ✅ Test non-destructive operations first
- ✅ Use AgentrIntegration for authentication
- ✅ Handle different response structures (data, meta, errors)
- ✅ Convert list parameters to API-expected format
- ✅ Log both successes and failures with clear messages
- ✅ Group tests by functionality category
- ✅ Store reusable data (IDs, tokens) for dependent tests
- ✅ Print summary statistics at the end

**DON'T:**
- ❌ Test destructive operations without safeguards
- ❌ Assume all endpoints have same response structure
- ❌ Ignore rate limits - add delays if needed
- ❌ Skip error handling in tests
- ❌ Test in production without understanding API limits
- ❌ Forget to check API documentation for required access levels

## Example Test Execution

```bash
# Run full test suite
uv run python test_twitter_tools.py

# Output:
# ================================================================================
# TWITTER API NON-DESTRUCTIVE TOOLS TEST
# ================================================================================
#
# Authentication & User Info
# --------------------------------------------------------------------------------
# ✓ PASS | get_authenticated_user: Retrieved user @username (ID: 12345)
# ✓ PASS | get_user_by_username: Retrieved user @twitter
# ✓ PASS | get_user_by_id: Retrieved user by ID 12345
# ✗ FAIL | search_users: Error: 403 Forbidden (requires elevated access)
#
# ... (more test output)
#
# ================================================================================
# TEST SUMMARY
# ================================================================================
#
# Total Tests: 15
# Passed: 10 ✓
# Failed: 5 ✗
# Success Rate: 66.7%
```

This testing approach ensures robust, well-tested applications that handle real-world API scenarios gracefully.

## Test File Template

**IMPORTANT:** Always create the test file in the same directory as `app.py` to keep related code together.

**Location:** `src/universal_mcp/applications/<app_name>/test_<app_name>_tools.py`

```python
"""
Comprehensive test script for <AppName> API non-destructive tools.
Tests all read-only operations to verify they work correctly.
"""
import asyncio
import sys
from typing import Any
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.<app_name>.app import <AppClass>


class <AppName>ToolTester:
    def __init__(self):
        self.integration = AgentrIntegration(name='<app_name>')
        self.app = <AppClass>(integration=self.integration)
        self.results = {}
        self.user_id = None  # Populated from get_authenticated_user

    def log_result(self, tool_name: str, success: bool, message: str = "", data: Any = None):
        """Log test result for a tool."""
        status = "✓ PASS" if success else "✗ FAIL"
        self.results[tool_name] = {"success": success, "message": message, "data": data}
        print(f"{status} | {tool_name}: {message}")
        if data and success:
            print(f"    Sample data: {str(data)[:200]}...")

    async def test_get_authenticated_user(self):
        """Test getting authenticated user information."""
        try:
            result = await self.app.get_authenticated_user()
            if "data" in result and "id" in result["data"]:
                self.user_id = result["data"]["id"]
                username = result["data"].get("username", "unknown")
                self.log_result(
                    "get_authenticated_user",
                    True,
                    f"Retrieved user {username} (ID: {self.user_id})",
                    result["data"]
                )
                return True
            else:
                self.log_result("get_authenticated_user", False, "No data in response", result)
                return False
        except Exception as e:
            self.log_result("get_authenticated_user", False, f"Error: {str(e)}")
            return False

    async def run_all_tests(self):
        """Run all non-destructive tests in logical order."""
        print("\n" + "="*80)
        print("<APP NAME> API NON-DESTRUCTIVE TOOLS TEST")
        print("="*80 + "\n")

        tests = [
            ("Authentication & User Info", [
                self.test_get_authenticated_user,
                # Add more tests...
            ]),
        ]

        for category, test_funcs in tests:
            print(f"\n{category}")
            print("-" * 80)
            for test_func in test_funcs:
                await test_func()

        # Print summary
        self._print_summary()

        total = len(self.results)
        passed = sum(1 for r in self.results.values() if r["success"])
        return passed == total

    def _print_summary(self):
        """Print test summary."""
        print("\n" + "="*80)
        print("TEST SUMMARY")
        print("="*80)

        total = len(self.results)
        passed = sum(1 for r in self.results.values() if r["success"])
        failed = total - passed

        print(f"\nTotal Tests: {total}")
        print(f"Passed: {passed} ✓")
        print(f"Failed: {failed} ✗")
        print(f"Success Rate: {(passed/total*100):.1f}%\n")

        if failed > 0:
            print("Failed Tests:")
            for name, result in self.results.items():
                if not result["success"]:
                    print(f"  - {name}: {result['message']}")

        print("="*80 + "\n")


async def main():
    """Main test runner."""
    tester = <AppName>ToolTester()
    try:
        success = await tester.run_all_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
```

Run tests with:
```bash
uv run python src/universal_mcp/applications/<app_name>/test_<app_name>_tools.py
```

Or navigate to the application directory first:
```bash
cd src/universal_mcp/applications/<app_name>
uv run python test_<app_name>_tools.py
```
