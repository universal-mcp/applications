import asyncio
from universal_mcp.applications.nocodb.app import NocoDBApp
from universal_mcp.integrations import Integration

class MockIntegration(Integration):
    def __init__(self, api_key):
        self.api_key = api_key
        super().__init__(name="nocodb_mock")
        self.type = "mock"

    async def get_credentials(self):
        return {"xc-token": self.api_key}

    async def get_credentials_async(self):
        return {"xc-token": self.api_key}

# --- Configuration ---
API_KEY = "9wEYlDWJc4W8bgAY28PnV_k5fPTsIovHCxlHQtd8"
# Updated to V3
BASE_URL = "https://nocodb.agentr.dev/api/v3/meta"
BASE_ID = "prx1mkflfxn86fg"      
TABLE_ID = "m7j5to7f3cv55lg"    

async def main():
    print("--- Testing NocoDB Tools (V3) ---")
    
    mock_integration = MockIntegration(api_key=API_KEY)
    app = NocoDBApp(integration=mock_integration, base_url=BASE_URL)
    
    try:
        # 1. List Workspaces (New V3 Feature)
        try:
            print("\n[Test] list_workspaces()...")
            workspaces_resp = await app.list_workspaces()
            # Expecting dict with 'list' key
            workspaces = workspaces_resp.get('list', [])
            print(f"✅ Success! Found {len(workspaces)} workspaces.")
            if workspaces:
                print(f"  First Workspace: {workspaces[0].get('title')} ({workspaces[0].get('id')})")
        except Exception as e:
            print(f"❌ list_workspaces failed (might be permissions/OSS limit): {e}")

        # 2. Get Base
        print(f"\n[Test] get_base('{BASE_ID}')...")
        base = await app.get_base(BASE_ID)
        print(f"✅ Success! Base Title: {base.get('title')}")
        
        # 3. List Tables (V3 uses base_id in path now, consistent with before but good to retest)
        print(f"\n[Test] list_tables('{BASE_ID}')...")
        tables_resp = await app.list_tables(BASE_ID)
        tables = tables_resp.get('list', [])
        print(f"✅ Success! Found {len(tables)} tables.")
        
        # 4. Get Table (V3 requires base_id + table_id usually)
        target_tid = TABLE_ID
        print(f"\n[Test] get_table('{BASE_ID}', '{target_tid}')...")
        table = await app.get_table(BASE_ID, target_tid)
        print(f"✅ Success! Table Title: {table.get('title')}")
        
        # 5. List Fields
        print(f"\n[Test] list_fields('{BASE_ID}', '{target_tid}')...")
        fields = await app.list_fields(BASE_ID, target_tid)
        print(f"✅ Success! Found {len(fields)} fields.")
        
        if fields:
            first_field = fields[0]
            fid = first_field['id']
            print(f"  First Field: {first_field.get('title')} (ID: {fid})")
            
            # 6. Get Field (V3 requires base_id + field_id usually)
            print(f"\n[Test] get_field('{BASE_ID}', '{fid}')...")
            field_details = await app.get_field(BASE_ID, fid)
            print(f"✅ Success! Field Details Title: {field_details.get('title')}")

    except Exception as e:
        print("\n❌ Error Occurred:")
        print(e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
