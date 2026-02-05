import asyncio
from universal_mcp.agentr import AgentrClient, AgentrIntegration
from universal_mcp.applications.ruzodb import RuzodbApp

client = AgentrClient(api_key="key-1f5983ba-f433-4337-b652-dc40f8712660")
integration = AgentrIntegration(client=client, name="ruzodb")
app = RuzodbApp(integration=integration)

async def main():
    table_id = "mh3suep3drk3ohs"
    base_id = "prx1mkflfxn86fg"
    # print(await app.list_views(base_id=base_id, table_id=table_id))    
    # print(await app.create_shared_view(base_id=base_id, table_id=table_id, view_id="vwyt56hj8uqq67sy"))
    # print(await app.get_shared_view(base_id=base_id, table_id=table_id, view_id="vwyt56hj8uqq67sy"))
    # print(await app.delete_shared_view(base_id=base_id, table_id=table_id, view_id="vwyt56hj8uqq67sy"))
    print(await app.create_table(base_id=base_id, title ="Shareable view"))

if __name__ == "__main__":  
    asyncio.run(main())
