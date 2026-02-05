"""
Simple demo script to create a base, table, add records, and create a shared view.
Run this to manually test the shared view functionality.
"""
import asyncio
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.ruzodb.app import RuzodbApp


async def main():
    print("\n" + "="*80)
    print("RUZODB SHARED VIEW DEMO")
    print("="*80 + "\n")

    # Initialize the app
    integration = AgentrIntegration(name='ruzodb')
    app = RuzodbApp(integration=integration)

    base_id = None

    try:
        # Step 1: Create a new base
        print("Step 1: Creating a new base...")
        base = await app.create_base(title="Demo Shared View Base")
        base_id = base["id"]
        print(f"✓ Created base: {base['title']} (ID: {base_id})")

        # Step 2: Create a table with simple columns first
        print("\nStep 2: Creating a table with columns...")
        table = await app.create_table(
            base_id=base_id,
            title="Products",
            columns=[
                {"title": "Name", "uidt": "SingleLineText"},
                {"title": "Price", "uidt": "Number"},
                {"title": "InStock", "uidt": "Checkbox"}
            ]
        )
        table_id = table["id"]
        print(f"✓ Created table: {table['title']} (ID: {table_id})")

        # Step 3: Add some sample records using simpler field names
        print("\nStep 3: Adding sample records...")
        sample_records = [
            {"Name": "Laptop Pro 15", "Price": 1299, "InStock": True},
            {"Name": "Wireless Mouse", "Price": 29, "InStock": True},
            {"Name": "USB Cable", "Price": 12, "InStock": False},
        ]

        # Create records one at a time
        created_count = 0
        for record_data in sample_records:
            try:
                await app.create_records(
                    base_id=base_id,
                    table_id=table_id,
                    data=record_data
                )
                created_count += 1
                print(f"  ✓ Created: {record_data['Name']}")
            except Exception as e:
                print(f"  ✗ Failed to create: {record_data['Name']} - {str(e)[:100]}")

        print(f"✓ Successfully created {created_count}/{len(sample_records)} records")

        # Step 4: Get the first view from the table
        print("\nStep 4: Getting views from the table...")
        views_result = await app.list_views(base_id=base_id, table_id=table_id)
        views = views_result.get("list", [])

        if not views:
            raise Exception("No views found. Cannot create shared view.")

        view_id = views[0]["id"]
        view_title = views[0].get("title", "Default View")
        print(f"✓ Found view: {view_title} (ID: {view_id})")

        # Step 5: Create a shared view
        print("\nStep 5: Creating shared view...")
        shared_view = await app.create_shared_view(
            base_id=base_id,
            table_id=table_id,
            view_id=view_id
        )

        # Display results
        print("\n" + "="*80)
        print("SHARED VIEW CREATED SUCCESSFULLY!")
        print("="*80)
        print(f"\nBase: {base['title']}")
        print(f"Table: {table['title']}")
        print(f"View: {view_title}")
        print(f"\nShareable URL: {shared_view.get('shareable_url', 'N/A')}")
        print(f"UUID: {shared_view.get('uuid', 'N/A')}")
        print("\nYou can now access this view publicly at the URL above!")
        print("="*80 + "\n")

        # Save the IDs for reference
        print("IDs for reference:")
        print(f"  Base ID: {base_id}")
        print(f"  Table ID: {table_id}")
        print(f"  View ID: {view_id}")
        print()

        return True

    except Exception as e:
        print(f"\n\n✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

        # Cleanup: Delete the base if it was created
        if base_id:
            try:
                print(f"\nCleaning up: Deleting base {base_id}...")
                await app.delete_base(base_id=base_id)
                print("✓ Base deleted successfully")
            except Exception as cleanup_error:
                print(f"✗ Failed to delete base: {str(cleanup_error)}")

        return False


if __name__ == "__main__":
    try:
        success = asyncio.run(main())
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        exit(1)
