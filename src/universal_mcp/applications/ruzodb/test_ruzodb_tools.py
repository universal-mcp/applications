"""
Comprehensive test script for Ruzodb API non-destructive tools.
Tests all read-only operations to verify they work correctly.
"""
import asyncio
import sys
from typing import Any
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.ruzodb.app import RuzodbApp


class RuzodbToolTester:
    def __init__(self):
        self.integration = AgentrIntegration(name='ruzodb')
        self.app = RuzodbApp(integration=self.integration)
        self.results = {}
        # Store frequently used IDs
        self.workspace_id = None
        self.base_id = None
        self.table_id = None
        self.view_id = None
        self.record_id = None

    def log_result(self, tool_name: str, success: bool, message: str = "", data: Any = None):
        """Log test result for a tool."""
        status = "✓ PASS" if success else "✗ FAIL"
        self.results[tool_name] = {"success": success, "message": message, "data": data}
        print(f"{status} | {tool_name}: {message}")
        if data and success:
            print(f"    Sample data: {str(data)[:200]}...")

    async def test_list_bases(self):
        """Test listing all bases in the workspace."""
        try:
            result = await self.app.list_bases()

            if "list" in result:
                bases = result["list"]
                count = len(bases) if isinstance(bases, list) else 0
                # Store first base_id for later tests
                if count > 0 and isinstance(bases[0], dict) and "id" in bases[0]:
                    self.base_id = bases[0]["id"]
                self.log_result("list_bases", True, f"Retrieved {count} bases", bases[:2] if count > 0 else None)
                return True
            else:
                self.log_result("list_bases", False, "No 'list' key in response", result)
                return False

        except Exception as e:
            self.log_result("list_bases", False, f"Error: {str(e)}")
            return False

    async def test_get_base(self):
        """Test getting details of a specific base."""
        if not self.base_id:
            self.log_result("get_base", False, "Skipped - no base_id available")
            return False

        try:
            result = await self.app.get_base(base_id=self.base_id)

            if "id" in result:
                title = result.get("title", "unknown")
                self.log_result("get_base", True, f"Retrieved base: {title}", result)
                return True
            else:
                self.log_result("get_base", False, "No 'id' in response", result)
                return False

        except Exception as e:
            self.log_result("get_base", False, f"Error: {str(e)}")
            return False

    async def test_list_tables(self):
        """Test listing all tables in a base."""
        if not self.base_id:
            self.log_result("list_tables", False, "Skipped - no base_id available")
            return False

        try:
            result = await self.app.list_tables(base_id=self.base_id)

            if "list" in result:
                tables = result["list"]
                count = len(tables) if isinstance(tables, list) else 0
                # Store first table_id for later tests
                if count > 0 and isinstance(tables[0], dict) and "id" in tables[0]:
                    self.table_id = tables[0]["id"]
                self.log_result("list_tables", True, f"Retrieved {count} tables", tables[:2] if count > 0 else None)
                return True
            else:
                self.log_result("list_tables", False, "No 'list' key in response", result)
                return False

        except Exception as e:
            self.log_result("list_tables", False, f"Error: {str(e)}")
            return False

    async def test_list_views(self):
        """Test listing all views for a table."""
        if not self.base_id or not self.table_id:
            self.log_result("list_views", False, "Skipped - no base_id or table_id available")
            return False

        try:
            result = await self.app.list_views(base_id=self.base_id, table_id=self.table_id)

            if "list" in result:
                views = result["list"]
                count = len(views) if isinstance(views, list) else 0
                # Store first view_id for shared view tests
                if count > 0 and isinstance(views[0], dict) and "id" in views[0]:
                    self.view_id = views[0]["id"]
                self.log_result("list_views", True, f"Retrieved {count} views", views[:2] if count > 0 else None)
                return True
            else:
                self.log_result("list_views", False, "No 'list' key in response", result)
                return False

        except Exception as e:
            self.log_result("list_views", False, f"Error: {str(e)}")
            return False

    async def test_get_shared_view(self):
        """Test getting shared view details (read-only check)."""
        if not self.base_id or not self.table_id or not hasattr(self, 'view_id') or not self.view_id:
            self.log_result("get_shared_view", False, "Skipped - no base_id, table_id, or view_id available")
            return False

        try:
            result = await self.app.get_shared_view(
                base_id=self.base_id,
                table_id=self.table_id,
                view_id=self.view_id
            )

            # Result can be empty dict if not shared, which is still a valid response
            if result is not None:
                if "uuid" in result and "shareable_url" in result:
                    self.log_result("get_shared_view", True, f"View is shared: {result.get('shareable_url')}", result)
                else:
                    self.log_result("get_shared_view", True, "View is not currently shared (valid response)", result)
                return True
            else:
                self.log_result("get_shared_view", False, "Unexpected null response", result)
                return False

        except Exception as e:
            self.log_result("get_shared_view", False, f"Error: {str(e)}")
            return False

    async def test_list_records(self):
        """Test listing records from a table."""
        if not self.base_id or not self.table_id:
            self.log_result("list_records", False, "Skipped - no base_id or table_id available")
            return False

        try:
            result = await self.app.list_records(
                base_id=self.base_id,
                table_id=self.table_id,
                limit=10
            )

            # Check for both 'list' and 'records' keys (V3 API variations)
            records = result.get("list") or result.get("records")
            if records is not None:
                count = len(records) if isinstance(records, list) else 0
                # Store first record_id for later tests
                if count > 0 and isinstance(records[0], dict):
                    self.record_id = records[0].get("Id") or records[0].get("id")
                self.log_result("list_records", True, f"Retrieved {count} records", records[:1] if count > 0 else None)
                return True
            else:
                self.log_result("list_records", False, "No 'list' or 'records' key in response", result)
                return False

        except Exception as e:
            self.log_result("list_records", False, f"Error: {str(e)}")
            return False

    async def test_get_record(self):
        """Test retrieving a single record by ID."""
        if not self.base_id or not self.table_id or not self.record_id:
            self.log_result("get_record", False, "Skipped - no base_id, table_id, or record_id available")
            return False

        try:
            result = await self.app.get_record(
                base_id=self.base_id,
                table_id=self.table_id,
                record_id=self.record_id
            )

            if "id" in result or "Id" in result or "fields" in result:
                self.log_result("get_record", True, f"Retrieved record {self.record_id}", result)
                return True
            else:
                self.log_result("get_record", False, "Unexpected response format", result)
                return False

        except Exception as e:
            self.log_result("get_record", False, f"Error: {str(e)}")
            return False

    async def test_get_record_count(self):
        """Test getting record count for a table."""
        if not self.base_id or not self.table_id:
            self.log_result("get_record_count", False, "Skipped - no base_id or table_id available")
            return False

        try:
            result = await self.app.get_record_count(
                base_id=self.base_id,
                table_id=self.table_id
            )

            if "count" in result:
                count = result["count"]
                self.log_result("get_record_count", True, f"Record count: {count}", result)
                return True
            else:
                self.log_result("get_record_count", False, "No 'count' key in response", result)
                return False

        except Exception as e:
            self.log_result("get_record_count", False, f"Error: {str(e)}")
            return False

    async def run_all_tests(self):
        """Run all non-destructive tests in logical order."""
        print("\n" + "="*80)
        print("RUZODB API NON-DESTRUCTIVE TOOLS TEST")
        print("="*80 + "\n")

        # Group tests by category
        tests = [
            ("Base Operations", [
                self.test_list_bases,
                self.test_get_base,
            ]),
            ("Table & View Operations", [
                self.test_list_tables,
                self.test_list_views,
            ]),
            ("Record Operations", [
                self.test_list_records,
                self.test_get_record,
                self.test_get_record_count,
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
    tester = RuzodbToolTester()
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
