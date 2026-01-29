"""
Comprehensive test script for Twitter API non-destructive tools.
Tests all read-only operations to verify they work correctly.
"""
import asyncio
import sys
from typing import Any
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.twitter.app import TwitterApp


class TwitterToolTester:
    def __init__(self):
        self.integration = AgentrIntegration(name='twitter')
        self.app = TwitterApp(integration=self.integration)
        self.results = {}
        self.user_id = None  # Will be populated from get_authenticated_user

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
            result = await self.app.get_authenticated_user(
                user_fields=["id", "name", "username", "created_at", "public_metrics"]
            )
            if "data" in result and "id" in result["data"]:
                self.user_id = result["data"]["id"]
                username = result["data"].get("username", "unknown")
                self.log_result(
                    "get_authenticated_user",
                    True,
                    f"Retrieved user @{username} (ID: {self.user_id})",
                    result["data"]
                )
                return True
            else:
                self.log_result("get_authenticated_user", False, "No data in response", result)
                return False
        except Exception as e:
            self.log_result("get_authenticated_user", False, f"Error: {str(e)}")
            return False

    async def test_get_user_by_username(self):
        """Test getting user by username."""
        try:
            # Test with a known public account
            result = await self.app.get_user_by_username(
                username="Twitter",
                user_fields=["id", "name", "username", "public_metrics"]
            )
            if "data" in result:
                self.log_result(
                    "get_user_by_username",
                    True,
                    f"Retrieved user @{result['data'].get('username')}",
                    result["data"]
                )
                return True
            else:
                self.log_result("get_user_by_username", False, "No data in response", result)
                return False
        except Exception as e:
            self.log_result("get_user_by_username", False, f"Error: {str(e)}")
            return False

    async def test_get_user_by_id(self):
        """Test getting user by ID."""
        if not self.user_id:
            self.log_result("get_user_by_id", False, "Skipped - no user_id available")
            return False

        try:
            result = await self.app.get_user_by_id(
                user_id=self.user_id,
                user_fields=["id", "name", "username"]
            )
            if "data" in result:
                self.log_result(
                    "get_user_by_id",
                    True,
                    f"Retrieved user by ID {self.user_id}",
                    result["data"]
                )
                return True
            else:
                self.log_result("get_user_by_id", False, "No data in response", result)
                return False
        except Exception as e:
            self.log_result("get_user_by_id", False, f"Error: {str(e)}")
            return False

    async def test_search_users(self):
        """Test searching for users."""
        try:
            result = await self.app.search_users(
                query="developer",
                max_results=5,
                user_fields=["username", "name"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "search_users",
                    True,
                    f"Found {count} users matching 'developer'",
                    result["data"][0] if result["data"] else None
                )
                return True
            else:
                self.log_result("search_users", False, "No data in response", result)
                return False
        except Exception as e:
            self.log_result("search_users", False, f"Error: {str(e)}")
            return False

    async def test_get_user_tweets(self):
        """Test getting user's tweets."""
        if not self.user_id:
            self.log_result("get_user_tweets", False, "Skipped - no user_id available")
            return False

        try:
            result = await self.app.get_user_tweets(
                user_id=self.user_id,
                max_results=5,
                tweet_fields=["created_at", "text"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_user_tweets",
                    True,
                    f"Retrieved {count} tweets",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                # No tweets but valid response
                self.log_result("get_user_tweets", True, "No tweets found (valid response)")
                return True
            else:
                self.log_result("get_user_tweets", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_user_tweets", False, f"Error: {str(e)}")
            return False

    async def test_get_user_mentions(self):
        """Test getting user mentions."""
        if not self.user_id:
            self.log_result("get_user_mentions", False, "Skipped - no user_id available")
            return False

        try:
            result = await self.app.get_user_mentions(
                user_id=self.user_id,
                max_results=5,
                tweet_fields=["created_at", "text"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_user_mentions",
                    True,
                    f"Retrieved {count} mentions",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                self.log_result("get_user_mentions", True, "No mentions found (valid response)")
                return True
            else:
                self.log_result("get_user_mentions", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_user_mentions", False, f"Error: {str(e)}")
            return False

    async def test_search_recent_tweets(self):
        """Test searching recent tweets."""
        try:
            result = await self.app.search_recent_tweets(
                query="python",
                max_results=5,
                tweet_fields=["created_at", "text", "author_id"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "search_recent_tweets",
                    True,
                    f"Found {count} tweets matching 'python'",
                    result["data"][0] if result["data"] else None
                )
                return True
            else:
                self.log_result("search_recent_tweets", False, "No data in response", result)
                return False
        except Exception as e:
            self.log_result("search_recent_tweets", False, f"Error: {str(e)}")
            return False

    async def test_get_tweet(self):
        """Test getting a specific tweet."""
        # Use a well-known public tweet ID (Twitter's first tweet)
        tweet_id = "20"  # Jack Dorsey's first tweet
        try:
            result = await self.app.get_tweet(
                tweet_id=tweet_id,
                tweet_fields=["created_at", "text", "author_id", "public_metrics"]
            )
            if "data" in result:
                self.log_result(
                    "get_tweet",
                    True,
                    f"Retrieved tweet {tweet_id}",
                    result["data"]
                )
                return True
            else:
                self.log_result("get_tweet", False, "No data in response", result)
                return False
        except Exception as e:
            self.log_result("get_tweet", False, f"Error: {str(e)}")
            return False

    async def test_get_followers(self):
        """Test getting user followers."""
        if not self.user_id:
            self.log_result("get_followers", False, "Skipped - no user_id available")
            return False

        try:
            result = await self.app.get_followers(
                user_id=self.user_id,
                max_results=5,
                user_fields=["username", "name"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_followers",
                    True,
                    f"Retrieved {count} followers",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                self.log_result("get_followers", True, "No followers found (valid response)")
                return True
            else:
                self.log_result("get_followers", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_followers", False, f"Error: {str(e)}")
            return False

    async def test_get_following(self):
        """Test getting users the account is following."""
        if not self.user_id:
            self.log_result("get_following", False, "Skipped - no user_id available")
            return False

        try:
            result = await self.app.get_following(
                user_id=self.user_id,
                max_results=5,
                user_fields=["username", "name"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_following",
                    True,
                    f"Retrieved {count} following",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                self.log_result("get_following", True, "Not following anyone (valid response)")
                return True
            else:
                self.log_result("get_following", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_following", False, f"Error: {str(e)}")
            return False

    async def test_get_liked_tweets(self):
        """Test getting liked tweets."""
        try:
            result = await self.app.get_liked_tweets(
                max_results=5,
                tweet_fields=["created_at", "text"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_liked_tweets",
                    True,
                    f"Retrieved {count} liked tweets",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                self.log_result("get_liked_tweets", True, "No liked tweets (valid response)")
                return True
            else:
                self.log_result("get_liked_tweets", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_liked_tweets", False, f"Error: {str(e)}")
            return False

    async def test_get_bookmarks(self):
        """Test getting bookmarked tweets."""
        if not self.user_id:
            self.log_result("get_bookmarks", False, "Skipped - no user_id available")
            return False

        try:
            result = await self.app.get_bookmarks(
                user_id=self.user_id,
                max_results=5,
                tweet_fields=["created_at", "text"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_bookmarks",
                    True,
                    f"Retrieved {count} bookmarked tweets",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                self.log_result("get_bookmarks", True, "No bookmarks (valid response)")
                return True
            else:
                self.log_result("get_bookmarks", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_bookmarks", False, f"Error: {str(e)}")
            return False

    async def test_get_dm_events(self):
        """Test getting DM events."""
        try:
            result = await self.app.get_dm_events(
                max_results=5,
                dm_event_fields=["created_at", "text"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_dm_events",
                    True,
                    f"Retrieved {count} DM events",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                self.log_result("get_dm_events", True, "No DM events (valid response)")
                return True
            else:
                self.log_result("get_dm_events", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_dm_events", False, f"Error: {str(e)}")
            return False

    async def test_get_retweeters(self):
        """Test getting users who retweeted a tweet."""
        tweet_id = "20"  # Use a well-known tweet
        try:
            result = await self.app.get_retweeters(
                tweet_id=tweet_id,
                max_results=5,
                user_fields=["username", "name"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_retweeters",
                    True,
                    f"Retrieved {count} retweeters",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                self.log_result("get_retweeters", True, "No retweeters (valid response)")
                return True
            else:
                self.log_result("get_retweeters", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_retweeters", False, f"Error: {str(e)}")
            return False

    async def test_get_liking_users(self):
        """Test getting users who liked a tweet."""
        tweet_id = "20"  # Use a well-known tweet
        try:
            result = await self.app.get_liking_users(
                tweet_id=tweet_id,
                max_results=5,
                user_fields=["username", "name"]
            )
            if "data" in result:
                count = len(result["data"])
                self.log_result(
                    "get_liking_users",
                    True,
                    f"Retrieved {count} liking users",
                    result["data"][0] if result["data"] else None
                )
                return True
            elif "meta" in result:
                self.log_result("get_liking_users", True, "No liking users (valid response)")
                return True
            else:
                self.log_result("get_liking_users", False, "Unexpected response format", result)
                return False
        except Exception as e:
            self.log_result("get_liking_users", False, f"Error: {str(e)}")
            return False

    async def run_all_tests(self):
        """Run all non-destructive tests."""
        print("\n" + "="*80)
        print("TWITTER API NON-DESTRUCTIVE TOOLS TEST")
        print("="*80 + "\n")

        # Test in order, some tests depend on earlier ones
        tests = [
            ("Authentication & User Info", [
                self.test_get_authenticated_user,
                self.test_get_user_by_username,
                self.test_get_user_by_id,
                self.test_search_users,
            ]),
            ("Tweet Operations", [
                self.test_get_tweet,
                self.test_search_recent_tweets,
                self.test_get_user_tweets,
                self.test_get_user_mentions,
            ]),
            ("Social Interactions", [
                self.test_get_liked_tweets,
                self.test_get_followers,
                self.test_get_following,
                self.test_get_retweeters,
                self.test_get_liking_users,
            ]),
            ("Other Features", [
                self.test_get_bookmarks,
                self.test_get_dm_events,
            ]),
        ]

        for category, test_funcs in tests:
            print(f"\n{category}")
            print("-" * 80)
            for test_func in test_funcs:
                await test_func()

        # Print summary
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

        return passed == total


async def main():
    """Main test runner."""
    tester = TwitterToolTester()

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
