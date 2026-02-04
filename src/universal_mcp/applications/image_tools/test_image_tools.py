"""
Comprehensive test script for Image Tools application.
Tests all image manipulation operations with sample images.
"""
import asyncio
import os
import sys
import tempfile
from pathlib import Path
from typing import Any
from PIL import Image
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.image_tools.app import ImageToolsApp


class ImageToolsTester:
    def __init__(self):
        self.integration = AgentrIntegration(name='image_tools')
        self.app = ImageToolsApp(integration=self.integration)
        self.results = {}
        self.temp_dir = tempfile.mkdtemp()
        self.test_image_path = None

    def log_result(self, tool_name: str, success: bool, message: str = "", data: Any = None):
        """Log test result for a tool."""
        status = "✓ PASS" if success else "✗ FAIL"
        self.results[tool_name] = {"success": success, "message": message, "data": data}
        print(f"{status} | {tool_name}: {message}")
        if data and success:
            # Show relevant data fields
            if isinstance(data, dict):
                display_fields = ['output_path', 'original_size', 'cropped_size', 'rotated_size',
                                'resized_size', 'format', 'mode', 'file_size_mb']
                display_data = {k: v for k, v in data.items() if k in display_fields}
                if display_data:
                    print(f"    Data: {display_data}")

    def create_test_image(self, width: int = 800, height: int = 600, color: str = "RGB") -> str:
        """Create a test image for testing."""
        img = Image.new(color, (width, height), color=(100, 150, 200))

        # Add some patterns to make operations visible
        from PIL import ImageDraw
        draw = ImageDraw.Draw(img)

        # Draw a rectangle
        draw.rectangle([100, 100, 300, 300], fill=(255, 0, 0), outline=(0, 0, 0), width=3)

        # Draw a circle
        draw.ellipse([400, 200, 600, 400], fill=(0, 255, 0), outline=(0, 0, 0), width=3)

        # Draw some text
        draw.text((width//2 - 50, height//2), "TEST", fill=(255, 255, 255))

        test_path = os.path.join(self.temp_dir, "test_image.png")
        img.save(test_path)
        return test_path

    async def test_get_image_info(self):
        """Test getting image information."""
        try:
            result = await self.app.get_image_info(input_path=self.test_image_path)

            if result.get("success") and result.get("width") and result.get("height"):
                self.log_result(
                    "get_image_info",
                    True,
                    f"Retrieved info: {result['width']}x{result['height']} {result['format']} ({result['file_size_mb']} MB)",
                    result
                )
                return True
            else:
                self.log_result("get_image_info", False, "Invalid response", result)
                return False
        except Exception as e:
            self.log_result("get_image_info", False, f"Error: {str(e)}")
            return False

    async def test_crop_image(self):
        """Test cropping an image."""
        try:
            output_path = os.path.join(self.temp_dir, "cropped_image.png")
            result = await self.app.crop_image(
                input_path=self.test_image_path,
                output_path=output_path,
                left=100,
                top=100,
                right=500,
                bottom=400,
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "crop_image",
                    True,
                    f"Cropped from {result['original_size']} to {result['cropped_size']}",
                    result
                )
                return True
            else:
                self.log_result("crop_image", False, "Crop failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("crop_image", False, f"Error: {str(e)}")
            return False

    async def test_rotate_image(self):
        """Test rotating an image."""
        try:
            output_path = os.path.join(self.temp_dir, "rotated_image.png")
            result = await self.app.rotate_image(
                input_path=self.test_image_path,
                output_path=output_path,
                angle=45,
                expand=True,
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "rotate_image",
                    True,
                    f"Rotated 45° from {result['original_size']} to {result['rotated_size']}",
                    result
                )
                return True
            else:
                self.log_result("rotate_image", False, "Rotation failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("rotate_image", False, f"Error: {str(e)}")
            return False

    async def test_resize_image(self):
        """Test resizing an image."""
        try:
            output_path = os.path.join(self.temp_dir, "resized_image.png")
            result = await self.app.resize_image(
                input_path=self.test_image_path,
                output_path=output_path,
                width=400,
                maintain_aspect_ratio=True,
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "resize_image",
                    True,
                    f"Resized from {result['original_size']} to {result['resized_size']}",
                    result
                )
                return True
            else:
                self.log_result("resize_image", False, "Resize failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("resize_image", False, f"Error: {str(e)}")
            return False

    async def test_flip_image_horizontal(self):
        """Test flipping an image horizontally."""
        try:
            output_path = os.path.join(self.temp_dir, "flipped_horizontal.png")
            result = await self.app.flip_image(
                input_path=self.test_image_path,
                output_path=output_path,
                direction="horizontal",
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "flip_image_horizontal",
                    True,
                    f"Flipped horizontally: {result['original_size']}",
                    result
                )
                return True
            else:
                self.log_result("flip_image_horizontal", False, "Flip failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("flip_image_horizontal", False, f"Error: {str(e)}")
            return False

    async def test_flip_image_vertical(self):
        """Test flipping an image vertically."""
        try:
            output_path = os.path.join(self.temp_dir, "flipped_vertical.png")
            result = await self.app.flip_image(
                input_path=self.test_image_path,
                output_path=output_path,
                direction="vertical",
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "flip_image_vertical",
                    True,
                    f"Flipped vertically: {result['original_size']}",
                    result
                )
                return True
            else:
                self.log_result("flip_image_vertical", False, "Flip failed or output not created", result)
                return False
        except Exception as e:
            self.log_result("flip_image_vertical", False, f"Error: {str(e)}")
            return False

    async def test_remove_background(self):
        """Test removing background from an image."""
        try:
            # Check if rembg is installed
            try:
                import rembg
            except ImportError:
                self.log_result(
                    "remove_background",
                    False,
                    "Skipped - rembg not installed (pip install rembg)"
                )
                return False

            output_path = os.path.join(self.temp_dir, "no_background.png")
            result = await self.app.remove_background(
                input_path=self.test_image_path,
                output_path=output_path,
                model="u2net",
            )

            if result.get("success") and os.path.exists(output_path):
                self.log_result(
                    "remove_background",
                    True,
                    f"Background removed using {result['model_used']}",
                    result
                )
                return True
            else:
                self.log_result("remove_background", False, "Background removal failed", result)
                return False
        except Exception as e:
            error_msg = str(e)
            if "rembg" in error_msg.lower():
                self.log_result(
                    "remove_background",
                    False,
                    "Skipped - rembg not installed (pip install rembg)"
                )
            else:
                self.log_result("remove_background", False, f"Error: {error_msg}")
            return False

    async def run_all_tests(self):
        """Run all image manipulation tests."""
        print("\n" + "="*80)
        print("IMAGE TOOLS APPLICATION TEST")
        print("="*80 + "\n")

        # Create test image
        print("Creating test image...")
        self.test_image_path = self.create_test_image()
        print(f"Test image created at: {self.test_image_path}\n")

        tests = [
            ("Image Information", [
                self.test_get_image_info,
            ]),
            ("Basic Transformations", [
                self.test_crop_image,
                self.test_rotate_image,
                self.test_resize_image,
            ]),
            ("Flip Operations", [
                self.test_flip_image_horizontal,
                self.test_flip_image_vertical,
            ]),
            ("Advanced Operations", [
                self.test_remove_background,
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
        print("You can inspect the generated images manually.")

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
    tester = ImageToolsTester()
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
