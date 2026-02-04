"""
Check the status of a video generation operation.

Usage:
    uv run src/universal_mcp/applications/google_gemini/check_video_operation.py
"""

import asyncio
import base64
from pathlib import Path
from universal_mcp.applications.google_gemini.app import GoogleGeminiApp
from universal_mcp.agentr import AgentrIntegration


async def main():
    print("Checking Video Generation Operation Status")
    print("=" * 60)

    # Initialize app with credentials
    integration = AgentrIntegration(name="google_gemini")
    app = GoogleGeminiApp(integration=integration)

    # Operation ID from the previous test
    operation_name = "models/veo-3.1-fast-generate-preview/operations/83otyw4tvgl9"

    print(f"\nOperation ID: {operation_name}")
    print("\nChecking status...")

    try:
        # Check operation status
        result = await app.check_video_operation(operation_name)

        print(f"\nStatus: {result['status']}")
        print(f"Done: {result['done']}")
        print(f"\n{result['message']}")

        # Debug: print full result
        print(f"\n\nDEBUG - Full result:")
        import json
        print(json.dumps(result, indent=2, default=str))

        # If completed, save the video
        if result['done'] and result['status'] == 'COMPLETED':
            print("\n" + "-" * 60)
            print("Saving video file...")
            print("-" * 60)

            video_data = result['video_data']
            file_name = result['file_name']

            # Decode and save
            video_bytes = base64.b64decode(video_data)

            # Save to current directory
            output_path = Path.cwd() / file_name
            with open(output_path, "wb") as f:
                f.write(video_bytes)

            print(f"\n✓ Video saved to: {output_path}")
            print(f"  File size: {len(video_bytes):,} bytes")
            print(f"  MIME type: {result['mime_type']}")
            print(f"  Original URI: {result['video_uri']}")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
