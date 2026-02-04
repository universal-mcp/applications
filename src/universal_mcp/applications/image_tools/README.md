# Image Tools Application

A comprehensive image manipulation application providing tools for cropping, rotating, resizing, flipping, background removal, and image inspection.

## Features

### Core Operations
- **Crop Image** - Crop images to specified rectangular regions
- **Rotate Image** - Rotate images by any angle with optional expansion
- **Resize Image** - Resize images with aspect ratio preservation
- **Flip Image** - Flip images horizontally or vertically
- **Get Image Info** - Retrieve detailed image metadata and properties

### Advanced Operations
- **Remove Background** - AI-powered background removal (requires `rembg`)

## Installation

The application requires Pillow for basic image operations:

```bash
uv add pillow
```

For background removal functionality, install the optional dependency:

```bash
pip install rembg
```

**Note:** `rembg` requires Python <3.10 due to dependency constraints. If you're using Python 3.10+, background removal will not be available.

## Usage

### Basic Usage

```python
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.image_tools.app import ImageToolsApp

# Initialize the application
integration = AgentrIntegration(name='image_tools')
app = ImageToolsApp(integration=integration)

# Get image information
info = await app.get_image_info(input_path='/path/to/image.jpg')
print(f"Image size: {info['width']}x{info['height']}")

# Crop an image
result = await app.crop_image(
    input_path='/path/to/image.jpg',
    output_path='/path/to/cropped.jpg',
    left=100,
    top=100,
    right=500,
    bottom=400,
)

# Rotate an image
result = await app.rotate_image(
    input_path='/path/to/image.jpg',
    output_path='/path/to/rotated.jpg',
    angle=45,  # Counter-clockwise rotation
    expand=True,  # Expand canvas to fit rotated image
)

# Resize an image (maintaining aspect ratio)
result = await app.resize_image(
    input_path='/path/to/image.jpg',
    output_path='/path/to/resized.jpg',
    width=800,  # Height calculated automatically
    maintain_aspect_ratio=True,
)

# Flip an image
result = await app.flip_image(
    input_path='/path/to/image.jpg',
    output_path='/path/to/flipped.jpg',
    direction='horizontal',  # or 'vertical'
)

# Remove background (requires rembg)
result = await app.remove_background(
    input_path='/path/to/photo.jpg',
    output_path='/path/to/no_background.png',
    model='u2net',  # AI model for segmentation
    alpha_matting=False,  # Set to True for refined edges
)
```

## Tool Reference

### crop_image

Crops an image to a specified rectangular region.

**Parameters:**
- `input_path` (str): Path to input image
- `output_path` (str): Path for output image
- `left` (int): X coordinate of left edge
- `top` (int): Y coordinate of top edge
- `right` (int): X coordinate of right edge
- `bottom` (int): Y coordinate of bottom edge

**Returns:** Dict with `success`, `output_path`, `original_size`, `cropped_size`, `crop_box`

### rotate_image

Rotates an image by specified angle (counter-clockwise).

**Parameters:**
- `input_path` (str): Path to input image
- `output_path` (str): Path for output image
- `angle` (float): Rotation angle in degrees (positive = counter-clockwise)
- `expand` (bool): Expand canvas to fit rotated image (default: True)
- `fill_color` (tuple): RGBA color for empty areas (default: transparent for PNG, white for others)

**Returns:** Dict with `success`, `output_path`, `original_size`, `rotated_size`, `angle`, `expanded`

### resize_image

Resizes an image with optional aspect ratio preservation.

**Parameters:**
- `input_path` (str): Path to input image
- `output_path` (str): Path for output image
- `width` (int): Target width in pixels (optional if height provided)
- `height` (int): Target height in pixels (optional if width provided)
- `maintain_aspect_ratio` (bool): Preserve aspect ratio (default: True)
- `resample_filter` (str): Quality filter - 'lanczos', 'bicubic', 'bilinear', 'nearest' (default: 'lanczos')

**Returns:** Dict with `success`, `output_path`, `original_size`, `resized_size`, `aspect_ratio_maintained`

### flip_image

Flips an image horizontally or vertically.

**Parameters:**
- `input_path` (str): Path to input image
- `output_path` (str): Path for output image
- `direction` (str): 'horizontal' (mirror) or 'vertical' (upside down)

**Returns:** Dict with `success`, `output_path`, `original_size`, `direction`

### remove_background

Removes background using AI-powered segmentation (requires `rembg`).

**Parameters:**
- `input_path` (str): Path to input image
- `output_path` (str): Path for output image (should be .png)
- `model` (str): AI model - 'u2net' (default), 'u2netp', 'u2net_human_seg', 'u2net_cloth_seg', 'silueta', 'isnet-general-use'
- `alpha_matting` (bool): Use alpha matting for refined edges (default: False, slower but better quality)

**Returns:** Dict with `success`, `output_path`, `original_size`, `model_used`, `alpha_matting`

### get_image_info

Retrieves detailed information about an image.

**Parameters:**
- `input_path` (str): Path to input image

**Returns:** Dict with `success`, `path`, `format`, `mode`, `size`, `width`, `height`, `file_size_bytes`, `file_size_mb`

## Supported Image Formats

- JPEG/JPG
- PNG
- BMP
- GIF
- TIFF
- WebP

## Testing

Run the comprehensive test suite:

```bash
cd src/universal_mcp/applications/image_tools
uv run python test_image_tools.py
```

The test suite will:
1. Create a test image with visual patterns
2. Run all image manipulation operations
3. Save output images to a temporary directory for manual inspection
4. Report success/failure for each operation

## Error Handling

All tools raise appropriate exceptions:

- `ValueError`: Invalid parameters or unsupported image format
- `IOError`: Cannot open or save image file
- `ImportError`: Required library not installed (e.g., `rembg`)

## Performance Notes

- **Fast Operations**: crop, rotate, resize, flip, get_info (< 1 second)
- **Slow Operations**: remove_background (2-10 seconds depending on image size and model)

## Tags

Each tool is tagged for easy discovery:

- `image` - All image operations
- `crop`, `rotate`, `resize`, `flip` - Transformation operations
- `important` - Frequently used tools
- `slow` - Operations that take >2 seconds
- `ai`, `segmentation` - AI-powered operations

## Example Workflows

### Prepare Image for Web

```python
# 1. Get original info
info = await app.get_image_info(input_path='photo.jpg')
print(f"Original: {info['width']}x{info['height']} ({info['file_size_mb']} MB)")

# 2. Resize for web (800px wide, maintain aspect ratio)
await app.resize_image(
    input_path='photo.jpg',
    output_path='photo_web.jpg',
    width=800,
    maintain_aspect_ratio=True,
    resample_filter='lanczos',
)

# 3. Verify new size
info = await app.get_image_info(input_path='photo_web.jpg')
print(f"Web: {info['width']}x{info['height']} ({info['file_size_mb']} MB)")
```

### Create Thumbnail

```python
# Resize to thumbnail (200x200, crop to square)
# First resize maintaining aspect ratio
await app.resize_image(
    input_path='photo.jpg',
    output_path='photo_200.jpg',
    width=200,
    maintain_aspect_ratio=True,
)

# Then crop to square
info = await app.get_image_info(input_path='photo_200.jpg')
height = info['height']
crop_top = (height - 200) // 2

await app.crop_image(
    input_path='photo_200.jpg',
    output_path='thumbnail.jpg',
    left=0,
    top=crop_top,
    right=200,
    bottom=crop_top + 200,
)
```

### Remove Background for Product Photo

```python
# Remove background from product photo
await app.remove_background(
    input_path='product.jpg',
    output_path='product_nobg.png',
    model='u2net',  # General purpose
    alpha_matting=True,  # Better edge quality
)

# Resize for web
await app.resize_image(
    input_path='product_nobg.png',
    output_path='product_web.png',
    width=600,
    maintain_aspect_ratio=True,
)
```

### Rotate and Crop

```python
# Rotate image
await app.rotate_image(
    input_path='photo.jpg',
    output_path='photo_rotated.jpg',
    angle=15,  # Slight rotation
    expand=True,
)

# Crop to remove empty edges
info = await app.get_image_info(input_path='photo_rotated.jpg')
width, height = info['width'], info['height']
margin = 50

await app.crop_image(
    input_path='photo_rotated.jpg',
    output_path='photo_final.jpg',
    left=margin,
    top=margin,
    right=width - margin,
    bottom=height - margin,
)
```

## Contributing

When adding new image manipulation tools:

1. Follow the async function pattern
2. Include comprehensive docstrings with Args, Returns, Raises, Tags
3. Validate input parameters and file paths
4. Handle errors gracefully
5. Return consistent dict structure with `success` field
6. Add test cases to `test_image_tools.py`
7. Update this README with new tool documentation

## License

MIT License - See main project LICENSE file
