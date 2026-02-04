"""
Simple test for Google Gemini video generation.

Usage:
    uv run src/universal_mcp/applications/google_gemini/simple_video_test.py
"""

import asyncio
from universal_mcp.applications.google_gemini.app import GoogleGeminiApp
from universal_mcp.agentr import AgentrIntegration


async def main():
    print("Testing Google Gemini Video Generation")
    print("=" * 60)

    # Initialize app with credentials
    integration = AgentrIntegration(name="google_gemini")
    app = GoogleGeminiApp(integration=integration)

    # Simple prompt
    prompt = "A cat playing with a ball of yarn in slow motion"

    print(f"\nPrompt: {prompt}")
    print("\nGenerating video...")

    try:
        # Generate video
        result = await app.generate_video(
            prompt=prompt,
            duration_seconds="4",
            resolution="720p",
        )

        print(f"\n✓ Success!")
        print(f"  Operation ID: {result['operation_name']}")
        print(f"  Status: {result['status']}")
        print(f"\n{result['message']}")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
