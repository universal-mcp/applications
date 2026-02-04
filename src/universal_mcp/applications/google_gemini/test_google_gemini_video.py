"""
Test script for Google Gemini video generation capabilities.

This script demonstrates how to:
1. Generate a video from a text prompt
2. Poll the operation status
3. Save the resulting video file

Usage:
    uv run src/universal_mcp/applications/google_gemini/test_google_gemini_video.py
"""

import asyncio
import base64
import os
import time
from pathlib import Path

from universal_mcp.applications.google_gemini.app import GoogleGeminiApp
from universal_mcp.integrations import AgentrIntegration


async def test_generate_video():
    """Test basic video generation from a text prompt."""
    print("=" * 80)
    print("Testing Google Gemini Video Generation")
    print("=" * 80)

    # Initialize the app with credentials from integration
    integration = AgentrIntegration(integration_name="google_gemini")
    app = GoogleGeminiApp(integration=integration)

    # Test prompt with audio cues
    prompt = (
        'A serene beach at sunset with gentle waves. '
        'A seagull cries in the distance. '
        'Soft wind rustling through palm trees.'
    )

    print(f"\nPrompt: {prompt}")
    print("\n" + "-" * 80)
    print("Step 1: Starting video generation...")
    print("-" * 80)

    try:
        # Start video generation
        result = await app.generate_video(
            prompt=prompt,
            model="veo-3.1-fast-generate-preview",  # Use fast model for testing
            aspect_ratio="16:9",
            resolution="720p",
            duration_seconds="4",
        )

        print(f"✓ Video generation started")
        print(f"  Operation ID: {result['operation_name']}")
        print(f"  Status: {result['status']}")
        print(f"  Message: {result['message']}")

        # Poll for completion
        print("\n" + "-" * 80)
        print("Step 2: Polling for completion (this may take 1-2 minutes)...")
        print("-" * 80)

        operation_name = result["operation_name"]
        max_attempts = 60  # 10 minutes max (60 * 10s)
        attempt = 0

        while attempt < max_attempts:
            attempt += 1
            print(f"  Checking status (attempt {attempt}/{max_attempts})...", end="")

            status_result = await app.check_video_operation(operation_name)

            if status_result["done"]:
                print(" DONE!")
                if status_result["status"] == "COMPLETED":
                    print("\n✓ Video generation completed successfully!")

                    # Save the video
                    print("\n" + "-" * 80)
                    print("Step 3: Saving video file...")
                    print("-" * 80)

                    video_data = status_result["video_data"]
                    file_name = status_result["file_name"]

                    # Decode and save
                    video_bytes = base64.b64decode(video_data)

                    # Save to current directory
                    output_path = Path.cwd() / file_name
                    with open(output_path, "wb") as f:
                        f.write(video_bytes)

                    print(f"✓ Video saved to: {output_path}")
                    print(f"  File size: {len(video_bytes):,} bytes")
                    print(f"  MIME type: {status_result['mime_type']}")

                    break
                elif status_result["status"] == "FAILED":
                    print(f"\n✗ Video generation failed: {status_result.get('error', 'Unknown error')}")
                    break
                else:
                    print(f"\n? Unexpected status: {status_result['status']}")
                    break
            else:
                print(" still running")
                await asyncio.sleep(10)  # Wait 10 seconds before next check

        if attempt >= max_attempts:
            print("\n✗ Timed out waiting for video generation")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "=" * 80)
    print("Test completed")
    print("=" * 80)


async def test_generate_video_with_audio_cues():
    """Test video generation with explicit audio cues."""
    print("\n\n" + "=" * 80)
    print("Testing Video Generation with Audio Cues")
    print("=" * 80)

    integration = AgentrIntegration(integration_name="google_gemini")
    app = GoogleGeminiApp(integration=integration)

    # Prompt with dialogue and sound effects
    prompt = (
        'A busy city street. '
        'A person walks up and says "Good morning!" with a smile. '
        'Cars honking in the background. '
        'The sound of footsteps on pavement.'
    )

    print(f"\nPrompt: {prompt}")

    try:
        result = await app.generate_video(
            prompt=prompt,
            model="veo-3.1-fast-generate-preview",
            duration_seconds="4",
        )

        print(f"\n✓ Video generation with audio started")
        print(f"  Operation ID: {result['operation_name']}")
        print(f"\nNote: Use check_video_operation to poll for completion")

    except Exception as e:
        print(f"\n✗ Error: {e}")


async def main():
    """Run all tests."""
    # Run basic video generation test
    await test_generate_video()

    # Run audio-focused test (just start it, don't wait)
    await test_generate_video_with_audio_cues()


if __name__ == "__main__":
    asyncio.run(main())
