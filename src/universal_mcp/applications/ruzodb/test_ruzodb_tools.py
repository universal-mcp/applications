import asyncio
from universal_mcp.agentr import AgentrClient, AgentrIntegration
from universal_mcp.applications.ruzodb import RuzodbApp

client = AgentrClient(api_key="key-1f5983ba-f433-4337-b652-dc40f8712660")
integration = AgentrIntegration(client=client, name="ruzodb")
app = RuzodbApp(integration=integration)

async def main():
    base_id = "prx1mkflfxn86fg"
    
    # 1. Create table with description
    print("Creating table...")
    table = await app.create_table(
        base_id=base_id, 
        title="Test Table", 
        description="Initial description"
    )
    table_id = table["id"]
    print(f"Created table: {table_id}")

    # 2. Verify description using get_table
    print("Verifying initial state...")
    fetched_table = await app.get_table(base_id=base_id, table_id=table_id)
    print(f"Initial Title: {fetched_table.get('title')}")
    print(f"Initial Description: {fetched_table.get('description')}")

    # 3. Update table (Title only)
    print("Updating title...")
    await app.update_table(base_id=base_id, table_id=table_id, title="Updated Title")
    
    # 4. Update table (Description only)
    print("Updating description...")
    await app.update_table(base_id=base_id, table_id=table_id, description="Updated description")

    # 5. Verify updates
    print("Verifying updates...")
    updated_table = await app.get_table(base_id=base_id, table_id=table_id)
    print(f"Updated Title: {updated_table.get('title')}")
    print(f"Updated Description: {updated_table.get('description')}")
    
    # 6. Cleanup
    print("Cleaning up...")
    await app.delete_table(base_id=base_id, table_id=table_id)
    print("Table deleted.")

if __name__ == "__main__":  
    asyncio.run(main())
