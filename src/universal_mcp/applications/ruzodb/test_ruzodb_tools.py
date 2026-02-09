import asyncio
from universal_mcp.agentr import AgentrClient, AgentrIntegration
from universal_mcp.applications.ruzodb import RuzodbApp

client = AgentrClient(api_key="key-1f5983ba-f433-4337-b652-dc40f8712660")
integration = AgentrIntegration(client=client, name="ruzodb")
app = RuzodbApp(integration=integration)

async def main():
    base_id = "ptavpu80q5x0pv4"
    
    print(f"Testing share_base for base: {base_id}")
    try:
        result = await app.share_base(base_id=base_id)
        print("Share Base Result:")
        print(result)
        
        # Verify URL format logic
        if "url" in result and "shareable_url" in result:
            print(f"Original URL (implied): {result.get('url')}")
            print(f"Shareable URL: {result['shareable_url']}")
            
            # Simple check
            if "/nc" not in result['shareable_url'] and "/#/base/" in result['shareable_url']:
                print("URL format check: PASS")
            else:
                print("URL format check: FAIL")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":  
    asyncio.run(main())
