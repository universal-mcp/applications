"""
Image Tools Application

Provides image manipulation capabilities including cropping, background removal, and rotation.
"""
import os
from pathlib import Path
from typing import Any, Tuple
from PIL import Image, ImageOps
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class ImageToolsApp(APIApplication):
    """
    Image manipulation tools for common operations.

    Supports cropping, background removal, rotation, and other image transformations
    using PIL/Pillow and rembg libraries.
    """

    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="image_tools", integration=integration, **kwargs)
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}

    def _validate_image_path(self, image_path: str) -> Path:
        """
        Validates that the image path exists and is a supported format.

        Args:
            image_path: Path to the image file

        Returns:
            Path: Validated Path object

        Raises:
            ValueError: If the image doesn't exist or has unsupported format
        """
        path = Path(image_path)
        if not path.exists():
            raise ValueError(f"Image file not found: {image_path}")

        if path.suffix.lower() not in self.supported_formats:
            raise ValueError(
                f"Unsupported image format: {path.suffix}. "
                f"Supported formats: {', '.join(self.supported_formats)}"
            )

        return path

    def _ensure_output_directory(self, output_path: str) -> Path:
        """
        Ensures the output directory exists.

        Args:
            output_path: Path where the output image will be saved

        Returns:
            Path: Validated output Path object
        """
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path

    async def crop_image(
        self,
        input_path: str,
        output_path: str,
        left: int,
        top: int,
        right: int,
        bottom: int,
    ) -> dict[str, Any]:
        """
        Crops an image to the specified rectangular region defined by pixel coordinates.
        The crop region is defined by (left, top, right, bottom) where (left, top) is the upper-left corner
        and (right, bottom) is the lower-right corner of the crop box.

        Args:
            input_path: Path to the input image file. Example: '/path/to/image.jpg'
            output_path: Path where the cropped image will be saved. Example: '/path/to/cropped.jpg'
            left: X coordinate of the left edge of the crop box in pixels. Example: 100
            top: Y coordinate of the top edge of the crop box in pixels. Example: 50
            right: X coordinate of the right edge of the crop box in pixels. Example: 500
            bottom: Y coordinate of the bottom edge of the crop box in pixels. Example: 400

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the cropped image
                - 'original_size' (tuple): Original image dimensions (width, height)
                - 'cropped_size' (tuple): Cropped image dimensions (width, height)
                - 'crop_box' (tuple): The crop coordinates used (left, top, right, bottom)

        Raises:
            ValueError: Raised when input image doesn't exist, format is unsupported, or crop coordinates are invalid.
            IOError: Raised when the image cannot be opened or saved.

        Tags:
            image, crop, edit, transform, important
        """
        # Validate input
        input_path_obj = self._validate_image_path(input_path)
        output_path_obj = self._ensure_output_directory(output_path)

        # Open image
        with Image.open(input_path_obj) as img:
            original_size = img.size

            # Validate crop box
            if left < 0 or top < 0 or right > img.width or bottom > img.height:
                raise ValueError(
                    f"Invalid crop coordinates. Image size: {img.width}x{img.height}, "
                    f"Crop box: ({left}, {top}, {right}, {bottom})"
                )

            if left >= right or top >= bottom:
                raise ValueError(
                    f"Invalid crop box: left must be < right and top must be < bottom. "
                    f"Got: ({left}, {top}, {right}, {bottom})"
                )

            # Crop image
            crop_box = (left, top, right, bottom)
            cropped_img = img.crop(crop_box)
            cropped_size = cropped_img.size

            # Save cropped image
            cropped_img.save(output_path_obj)

        return {
            "success": True,
            "output_path": str(output_path_obj),
            "original_size": original_size,
            "cropped_size": cropped_size,
            "crop_box": crop_box,
        }

    async def remove_background(
        self,
        input_path: str,
        output_path: str,
        model: str = "u2net",
        alpha_matting: bool = False,
    ) -> dict[str, Any]:
        """
        Removes the background from an image using AI-powered segmentation, creating a transparent PNG.
        This tool uses the rembg library with various AI models to intelligently detect and remove backgrounds
        from photos of people, products, animals, and other subjects.

        Args:
            input_path: Path to the input image file. Example: '/path/to/photo.jpg'
            output_path: Path where the output image with transparent background will be saved. Should end with .png. Example: '/path/to/no_bg.png'
            model: The AI model to use for background removal. Options: 'u2net' (default, general purpose), 'u2netp' (lightweight), 'u2net_human_seg' (optimized for people), 'u2net_cloth_seg' (clothing), 'silueta' (high quality), 'isnet-general-use' (high accuracy). Example: 'u2net'
            alpha_matting: Whether to use alpha matting for more refined edges. Slower but produces better edge quality. Default: False

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the image with removed background
                - 'original_size' (tuple): Original image dimensions (width, height)
                - 'model_used' (str): The AI model used for background removal
                - 'alpha_matting' (bool): Whether alpha matting was applied

        Raises:
            ValueError: Raised when input image doesn't exist or format is unsupported.
            IOError: Raised when the image cannot be opened or saved.
            ImportError: Raised when rembg library is not installed.

        Tags:
            image, background, remove, ai, segmentation, important, slow
        """
        # Validate input
        input_path_obj = self._validate_image_path(input_path)
        output_path_obj = self._ensure_output_directory(output_path)

        # Import rembg (lazy import to avoid requiring it for other operations)
        try:
            from rembg import remove
        except ImportError:
            raise ImportError(
                "rembg library is required for background removal. "
                "Install it with: pip install rembg"
            )

        # Open image
        with Image.open(input_path_obj) as img:
            original_size = img.size

            # Remove background
            output = remove(
                img,
                session=model,
                alpha_matting=alpha_matting,
            )

            # Save output
            output.save(output_path_obj)

        return {
            "success": True,
            "output_path": str(output_path_obj),
            "original_size": original_size,
            "model_used": model,
            "alpha_matting": alpha_matting,
        }

    async def rotate_image(
        self,
        input_path: str,
        output_path: str,
        angle: float,
        expand: bool = True,
        fill_color: Tuple[int, int, int, int] = None,
    ) -> dict[str, Any]:
        """
        Rotates an image by the specified angle in degrees (counter-clockwise).
        Supports arbitrary rotation angles with optional expansion to fit the entire rotated image
        and customizable fill color for empty areas.

        Args:
            input_path: Path to the input image file. Example: '/path/to/image.jpg'
            output_path: Path where the rotated image will be saved. Example: '/path/to/rotated.jpg'
            angle: Rotation angle in degrees, counter-clockwise. Positive values rotate counter-clockwise, negative values rotate clockwise. Example: 90 for 90° counter-clockwise, -45 for 45° clockwise
            expand: If True, expands the output image to fit the entire rotated image. If False, keeps the original image dimensions and may crop edges. Default: True
            fill_color: RGBA color tuple (R, G, B, A) for filling empty areas created by rotation, where each value is 0-255. If None, uses transparent for PNG or white for other formats. Example: (255, 255, 255, 255) for white, (0, 0, 0, 0) for transparent

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the rotated image
                - 'original_size' (tuple): Original image dimensions (width, height)
                - 'rotated_size' (tuple): Rotated image dimensions (width, height)
                - 'angle' (float): The rotation angle used in degrees
                - 'expanded' (bool): Whether the image was expanded to fit rotation

        Raises:
            ValueError: Raised when input image doesn't exist or format is unsupported.
            IOError: Raised when the image cannot be opened or saved.

        Tags:
            image, rotate, transform, orientation, important
        """
        # Validate input
        input_path_obj = self._validate_image_path(input_path)
        output_path_obj = self._ensure_output_directory(output_path)

        # Open image
        with Image.open(input_path_obj) as img:
            original_size = img.size

            # Determine fill color
            if fill_color is None:
                # Use transparent for PNG, white for others
                if output_path_obj.suffix.lower() == '.png':
                    fill_color = (0, 0, 0, 0)  # Transparent
                else:
                    fill_color = (255, 255, 255, 255)  # White

            # Rotate image
            rotated_img = img.rotate(
                angle=-angle,  # PIL rotates clockwise, so negate for counter-clockwise
                expand=expand,
                fillcolor=fill_color,
            )
            rotated_size = rotated_img.size

            # Save rotated image
            rotated_img.save(output_path_obj)

        return {
            "success": True,
            "output_path": str(output_path_obj),
            "original_size": original_size,
            "rotated_size": rotated_size,
            "angle": angle,
            "expanded": expand,
        }

    async def resize_image(
        self,
        input_path: str,
        output_path: str,
        width: int = None,
        height: int = None,
        maintain_aspect_ratio: bool = True,
        resample_filter: str = "lanczos",
    ) -> dict[str, Any]:
        """
        Resizes an image to the specified dimensions with optional aspect ratio preservation.
        If only width or height is provided with maintain_aspect_ratio=True, the other dimension
        is calculated automatically to preserve the original aspect ratio.

        Args:
            input_path: Path to the input image file. Example: '/path/to/image.jpg'
            output_path: Path where the resized image will be saved. Example: '/path/to/resized.jpg'
            width: Target width in pixels. If None and maintain_aspect_ratio=True, calculated from height. Example: 800
            height: Target height in pixels. If None and maintain_aspect_ratio=True, calculated from width. Example: 600
            maintain_aspect_ratio: If True and only one dimension is specified, calculates the other to preserve aspect ratio. Default: True
            resample_filter: Resampling filter for quality. Options: 'lanczos' (highest quality, default), 'bicubic', 'bilinear', 'nearest' (fastest). Example: 'lanczos'

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the resized image
                - 'original_size' (tuple): Original image dimensions (width, height)
                - 'resized_size' (tuple): New image dimensions (width, height)
                - 'aspect_ratio_maintained' (bool): Whether aspect ratio was preserved

        Raises:
            ValueError: Raised when input image doesn't exist, format is unsupported, or both dimensions are None.
            IOError: Raised when the image cannot be opened or saved.

        Tags:
            image, resize, scale, transform, important
        """
        # Validate input
        if width is None and height is None:
            raise ValueError("At least one of width or height must be specified")

        input_path_obj = self._validate_image_path(input_path)
        output_path_obj = self._ensure_output_directory(output_path)

        # Map filter names to PIL constants
        filter_map = {
            "lanczos": Image.Resampling.LANCZOS,
            "bicubic": Image.Resampling.BICUBIC,
            "bilinear": Image.Resampling.BILINEAR,
            "nearest": Image.Resampling.NEAREST,
        }
        resample = filter_map.get(resample_filter.lower(), Image.Resampling.LANCZOS)

        # Open image
        with Image.open(input_path_obj) as img:
            original_size = img.size
            original_width, original_height = original_size

            # Calculate dimensions
            if maintain_aspect_ratio:
                if width is None:
                    # Calculate width from height
                    aspect_ratio = original_width / original_height
                    width = int(height * aspect_ratio)
                elif height is None:
                    # Calculate height from width
                    aspect_ratio = original_height / original_width
                    height = int(width * aspect_ratio)
            else:
                # Use original dimensions if not specified
                if width is None:
                    width = original_width
                if height is None:
                    height = original_height

            new_size = (width, height)

            # Resize image
            resized_img = img.resize(new_size, resample=resample)

            # Save resized image
            resized_img.save(output_path_obj)

        return {
            "success": True,
            "output_path": str(output_path_obj),
            "original_size": original_size,
            "resized_size": new_size,
            "aspect_ratio_maintained": maintain_aspect_ratio,
        }

    async def flip_image(
        self,
        input_path: str,
        output_path: str,
        direction: str = "horizontal",
    ) -> dict[str, Any]:
        """
        Flips an image horizontally (left-right mirror) or vertically (top-bottom mirror).
        Horizontal flip creates a mirror image, while vertical flip inverts the image upside down.

        Args:
            input_path: Path to the input image file. Example: '/path/to/image.jpg'
            output_path: Path where the flipped image will be saved. Example: '/path/to/flipped.jpg'
            direction: Flip direction. Options: 'horizontal' (left-right mirror, default), 'vertical' (top-bottom invert). Example: 'horizontal'

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the flipped image
                - 'original_size' (tuple): Image dimensions (width, height)
                - 'direction' (str): The flip direction used

        Raises:
            ValueError: Raised when input image doesn't exist, format is unsupported, or direction is invalid.
            IOError: Raised when the image cannot be opened or saved.

        Tags:
            image, flip, mirror, transform, important
        """
        # Validate input
        input_path_obj = self._validate_image_path(input_path)
        output_path_obj = self._ensure_output_directory(output_path)

        direction = direction.lower()
        if direction not in ["horizontal", "vertical"]:
            raise ValueError(f"Invalid direction: {direction}. Must be 'horizontal' or 'vertical'")

        # Open image
        with Image.open(input_path_obj) as img:
            original_size = img.size

            # Flip image
            if direction == "horizontal":
                flipped_img = ImageOps.mirror(img)
            else:  # vertical
                flipped_img = ImageOps.flip(img)

            # Save flipped image
            flipped_img.save(output_path_obj)

        return {
            "success": True,
            "output_path": str(output_path_obj),
            "original_size": original_size,
            "direction": direction,
        }

    async def get_image_info(
        self,
        input_path: str,
    ) -> dict[str, Any]:
        """
        Retrieves detailed information about an image file including dimensions, format, mode, and file size.
        Useful for understanding image properties before performing transformations.

        Args:
            input_path: Path to the input image file. Example: '/path/to/image.jpg'

        Returns:
            dict[str, Any]: Image information containing:
                - 'success' (bool): Whether the operation succeeded
                - 'path' (str): Full path to the image file
                - 'format' (str): Image format (e.g., 'JPEG', 'PNG')
                - 'mode' (str): Image mode (e.g., 'RGB', 'RGBA', 'L' for grayscale)
                - 'size' (tuple): Image dimensions (width, height) in pixels
                - 'width' (int): Image width in pixels
                - 'height' (int): Image height in pixels
                - 'file_size_bytes' (int): File size in bytes
                - 'file_size_mb' (float): File size in megabytes (rounded to 2 decimals)

        Raises:
            ValueError: Raised when input image doesn't exist or format is unsupported.
            IOError: Raised when the image cannot be opened.

        Tags:
            image, info, metadata, properties, important
        """
        # Validate input
        input_path_obj = self._validate_image_path(input_path)

        # Get file size
        file_size_bytes = input_path_obj.stat().st_size
        file_size_mb = round(file_size_bytes / (1024 * 1024), 2)

        # Open image and get properties
        with Image.open(input_path_obj) as img:
            return {
                "success": True,
                "path": str(input_path_obj),
                "format": img.format,
                "mode": img.mode,
                "size": img.size,
                "width": img.width,
                "height": img.height,
                "file_size_bytes": file_size_bytes,
                "file_size_mb": file_size_mb,
            }

    def list_tools(self):
        """Returns list of available image manipulation tools."""
        return [
            self.crop_image,
            self.remove_background,
            self.rotate_image,
            self.resize_image,
            self.flip_image,
            self.get_image_info,
        ]
