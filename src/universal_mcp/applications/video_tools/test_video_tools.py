"""
Comprehensive test script for Video Tools application.
Tests all video manipulation operations with sample videos.
"""
import asyncio
import os
import sys
import tempfile
from pathlib import Path
from typing import Any
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.video_tools.app import VideoToolsApp


class VideoToolsTester:
    def __init__(self):
        self.integration = AgentrIntegration(name='video_tools')
        self.app = VideoToolsApp(integration=self.integration)
        self.results = {}
        self.temp_dir = tempfile.mkdtemp()
        self.test_video1_path = None
        self.test_video2_path = None
        self.test_audio_path = None

    def log_result(self, tool_name: str, success: bool, message: str = "", data: Any = None):
        """Log test result for a tool."""
        status = "✓ PASS" if success else "✗ FAIL"
        self.results[tool_name] = {"success": success, "message": message, "data": data}
        print(f"{status} | {tool_name}: {message}")
        if data and success:
            # Show relevant data fields
            if isinstance(data, dict):
                display_fields = ['output_path', 'duration', 'original_duration', 'total_duration',
                                'resolution', 'output_resolution', 'original_resolution', 'num_videos',
                                'fps', 'has_audio', 'file_size_mb']
                display_data = {k: v for k, v in data.items() if k in display_fields}
                if display_data:
                    print(f"    Data: {display_data}")

    def create_test_videos(self):
        """Create test videos for testing."""
        try:
            # Check if moviepy is installed
            try:
                from moviepy.editor import ColorClip, AudioClip
                import numpy as np
            except ImportError:
                print("✗ moviepy not installed - cannot create test videos")
                print("  Install with: pip install moviepy")
                return False

            # Create first test video (3 seconds, blue background, 640x480)
            print("Creating test video 1...")
            clip1 = ColorClip(size=(640, 480), color=(0, 0, 255), duration=3)

            # Add audio (simple tone)
            def make_frame_audio(t):
                return np.sin(2 * np.pi * 440 * t)  # 440 Hz tone

            audio1 = AudioClip(make_frame_audio, duration=3, fps=44100)
            clip1 = clip1.set_audio(audio1)

            self.test_video1_path = os.path.join(self.temp_dir, "test_video1.mp4")
            clip1.write_videofile(
                self.test_video1_path,
                codec='libx264',
                audio_codec='aac',
                fps=24,
                verbose=False,
                logger=None,
            )
            clip1.close()
            print(f"  Created: {self.test_video1_path}")

            # Create second test video (2 seconds, green background, 640x480)
            print("Creating test video 2...")
            clip2 = ColorClip(size=(640, 480), color=(0, 255, 0), duration=2)

            def make_frame_audio2(t):
                return np.sin(2 * np.pi * 880 * t)  # 880 Hz tone

            audio2 = AudioClip(make_frame_audio2, duration=2, fps=44100)
            clip2 = clip2.set_audio(audio2)

            self.test_video2_path = os.path.join(self.temp_dir, "test_video2.mp4")
            clip2.write_videofile(
                self.test_video2_path,
                codec='libx264',
                audio_codec='aac',
                fps=24,
                verbose=False,
                logger=None,
            )
            clip2.close()
            print(f"  Created: {self.test_video2_path}")

            # Create test audio file
            print("Creating test audio...")
            def make_frame_audio3(t):
                return np.sin(2 * np.pi * 220 * t)  # 220 Hz tone

            audio3 = AudioClip(make_frame_audio3, duration=5, fps=44100)
            self.test_audio_path = os.path.join(self.temp_dir, "test_audio.mp3")
            audio3.write_audiofile(
                self.test_audio_path,
                codec='libmp3lame',
                verbose=False,
                logger=None,
            )
            audio3.close()
            print(f"  Created: {self.test_audio_path}")

            return True

        except Exception as e:
            print(f"✗ Error creating test videos: {str(e)}")
            return False

    async def test_get_video_info(self):
        """Test getting video information."""
        try:
            result = await self.app.get_video_info(input_path=self.test_video1_path)

            if result.get("success") and result.get("duration") and result.get("resolution"):
                self.log_result(
                    "get_video_info",
                    True,
                    f"Retrieved info: {result['width']}x{result['height']} @ {result['fps']}fps, {result['duration']}s ({result['file_size_mb']} MB)",
                    result
                )
                return True
            else:
                self.log_result("get_video_info", False, "Invalid response", result)
                return False
        except Exception as e:
            self.log_result("get_video_info", False, f"Error: {str(e)}")
            return False

    async def test_stitch_videos(self):
        """Test stitching multiple videos together."""
        try:
            output_path = os.path.join(self.temp_dir, "stitched_video.mp4")
            result = await self.app.stitch_videos(
                input_paths=[self.test_video1_path, self.test_video2_path],
                output_path=output_path,
                method="concatenate",
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "stitch_videos",
                    True,
                    f"Stitched {result['num_videos']} videos, total duration: {result['total_duration']}s",
                    result
                )
                return True
            else:
                self.log_result("stitch_videos", False, "Stitch failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("stitch_videos", False, f"Error: {str(e)}")
            return False

    async def test_trim_video(self):
        """Test trimming a video."""
        try:
            output_path = os.path.join(self.temp_dir, "trimmed_video.mp4")
            result = await self.app.trim_video(
                input_path=self.test_video1_path,
                output_path=output_path,
                start_time=0.5,
                end_time=2.0,
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "trim_video",
                    True,
                    f"Trimmed from {result['original_duration']}s to {result['output_duration']}s",
                    result
                )
                return True
            else:
                self.log_result("trim_video", False, "Trim failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("trim_video", False, f"Error: {str(e)}")
            return False

    async def test_resize_video(self):
        """Test resizing a video."""
        try:
            output_path = os.path.join(self.temp_dir, "resized_video.mp4")
            result = await self.app.resize_video(
                input_path=self.test_video1_path,
                output_path=output_path,
                width=320,
                maintain_aspect_ratio=True,
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "resize_video",
                    True,
                    f"Resized from {result['original_resolution']} to {result['output_resolution']}",
                    result
                )
                return True
            else:
                self.log_result("resize_video", False, "Resize failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("resize_video", False, f"Error: {str(e)}")
            return False

    async def test_extract_audio(self):
        """Test extracting audio from a video."""
        try:
            output_path = os.path.join(self.temp_dir, "extracted_audio.mp3")
            result = await self.app.extract_audio(
                input_path=self.test_video1_path,
                output_path=output_path,
                audio_format="mp3",
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "extract_audio",
                    True,
                    f"Extracted {result['audio_format']} audio from {result['video_duration']}s video",
                    result
                )
                return True
            else:
                self.log_result("extract_audio", False, "Extraction failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("extract_audio", False, f"Error: {str(e)}")
            return False

    async def test_add_audio(self):
        """Test adding audio to a video."""
        try:
            output_path = os.path.join(self.temp_dir, "video_with_new_audio.mp4")
            result = await self.app.add_audio(
                video_path=self.test_video1_path,
                audio_path=self.test_audio_path,
                output_path=output_path,
                replace_audio=True,
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "add_audio",
                    True,
                    f"Added audio to {result['video_duration']}s video (adjusted: {result['audio_adjusted']})",
                    result
                )
                return True
            else:
                self.log_result("add_audio", False, "Adding audio failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("add_audio", False, f"Error: {str(e)}")
            return False

    async def test_convert_video(self):
        """Test converting a video format."""
        try:
            output_path = os.path.join(self.temp_dir, "converted_video.avi")
            result = await self.app.convert_video(
                input_path=self.test_video1_path,
                output_path=output_path,
                output_format="avi",
                video_codec="mpeg4",
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "convert_video",
                    True,
                    f"Converted from {result['original_format']} to {result['output_format']} using {result['video_codec']}",
                    result
                )
                return True
            else:
                self.log_result("convert_video", False, "Conversion failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("convert_video", False, f"Error: {str(e)}")
            return False

    async def run_all_tests(self):
        """Run all video manipulation tests."""
        print("\n" + "="*80)
        print("VIDEO TOOLS APPLICATION TEST")
        print("="*80 + "\n")

        # Create test videos
        print("Creating test videos and audio...")
        if not self.create_test_videos():
            print("\n✗ Failed to create test files. Cannot proceed with tests.")
            print("Make sure moviepy is installed: pip install moviepy\n")
            return False

        print()

        tests = [
            ("Video Information", [
                self.test_get_video_info,
            ]),
            ("Video Stitching (Primary Feature)", [
                self.test_stitch_videos,
            ]),
            ("Basic Transformations", [
                self.test_trim_video,
                self.test_resize_video,
            ]),
            ("Audio Operations", [
                self.test_extract_audio,
                self.test_add_audio,
            ]),
            ("Format Conversion", [
                self.test_convert_video,
            ]),
        ]

        for category, test_funcs in tests:
            print(f"\n{category}")
            print("-" * 80)
            for test_func in test_funcs:
                await test_func()

        # Print summary
        self._print_summary()

        # Cleanup
        print(f"\nTest outputs saved in: {self.temp_dir}")
        print("You can inspect the generated videos manually.")

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
    tester = VideoToolsTester()
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
