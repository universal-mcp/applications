# Video Tools Application

A comprehensive video manipulation application providing tools for stitching videos, trimming, resizing, audio operations, format conversion, and more.

## Features

### Primary Feature
- **Stitch Videos** ⭐ - Concatenate multiple videos into a single file with optional transitions

### Core Operations
- **Trim Video** - Cut videos to specific time ranges
- **Get Video Info** - Retrieve detailed video metadata and properties
- **Resize Video** - Change video resolution with aspect ratio preservation
- **Convert Video** - Convert between video formats and codecs

### Audio Operations
- **Extract Audio** - Extract audio track from video as separate file
- **Add Audio** - Replace or mix audio track in a video

## Installation

The application requires moviepy for video operations:

```bash
uv add moviepy
```

**Note:** moviepy will automatically install ffmpeg binaries via `imageio-ffmpeg`.

## Usage

### Basic Usage

```python
from universal_mcp.agentr import AgentrIntegration
from universal_mcp.applications.video_tools.app import VideoToolsApp

# Initialize the application
integration = AgentrIntegration(name='video_tools')
app = VideoToolsApp(integration=integration)

# Get video information
info = await app.get_video_info(input_path='/path/to/video.mp4')
print(f"Video: {info['width']}x{info['height']} @ {info['fps']}fps, {info['duration']}s")

# Stitch multiple videos together
result = await app.stitch_videos(
    input_paths=[
        '/path/to/video1.mp4',
        '/path/to/video2.mp4',
        '/path/to/video3.mp4',
    ],
    output_path='/path/to/stitched.mp4',
    method='concatenate',  # or 'crossfade' for smooth transitions
)

# Trim a video
result = await app.trim_video(
    input_path='/path/to/video.mp4',
    output_path='/path/to/trimmed.mp4',
    start_time=10.0,  # Start at 10 seconds
    end_time=30.0,    # End at 30 seconds
)

# Resize a video
result = await app.resize_video(
    input_path='/path/to/video.mp4',
    output_path='/path/to/resized.mp4',
    width=1280,  # Height calculated automatically
    maintain_aspect_ratio=True,
)

# Extract audio from video
result = await app.extract_audio(
    input_path='/path/to/video.mp4',
    output_path='/path/to/audio.mp3',
    audio_format='mp3',
)

# Add audio to video
result = await app.add_audio(
    video_path='/path/to/video.mp4',
    audio_path='/path/to/soundtrack.mp3',
    output_path='/path/to/video_with_audio.mp4',
    replace_audio=True,
)

# Convert video format
result = await app.convert_video(
    input_path='/path/to/video.avi',
    output_path='/path/to/video.mp4',
    video_codec='libx264',  # H.264
    audio_codec='aac',
)
```

## Tool Reference

### stitch_videos ⭐ (Primary Feature)

Stitches multiple video files together into a single video.

**Parameters:**
- `input_paths` (List[str]): List of video file paths in order (minimum 2)
- `output_path` (str): Path for output video
- `method` (str): Stitching method - 'concatenate' (direct join, default) or 'crossfade' (smooth transition)
- `transition_duration` (float): Crossfade duration in seconds (only for 'crossfade' method, default: 0.0)
- `resize_mode` (str): Resolution handling - 'first' (match first video, default), 'largest', 'smallest'

**Returns:** Dict with `success`, `output_path`, `num_videos`, `total_duration`, `output_resolution`, `method`

**Example:**
```python
# Simple concatenation
result = await app.stitch_videos(
    input_paths=['intro.mp4', 'main.mp4', 'outro.mp4'],
    output_path='complete.mp4',
)

# With crossfade transitions
result = await app.stitch_videos(
    input_paths=['clip1.mp4', 'clip2.mp4', 'clip3.mp4'],
    output_path='smooth.mp4',
    method='crossfade',
    transition_duration=1.0,  # 1 second fade between clips
)
```

### trim_video

Trims a video to a specific time range.

**Parameters:**
- `input_path` (str): Path to input video
- `output_path` (str): Path for output video
- `start_time` (float): Start time in seconds (default: 0.0)
- `end_time` (float): End time in seconds (optional, cannot use with duration)
- `duration` (float): Duration in seconds (optional, cannot use with end_time)

**Returns:** Dict with `success`, `output_path`, `original_duration`, `output_duration`, `start_time`, `end_time`, `resolution`

### get_video_info

Retrieves detailed information about a video file.

**Parameters:**
- `input_path` (str): Path to input video

**Returns:** Dict with `success`, `path`, `duration`, `resolution`, `width`, `height`, `fps`, `has_audio`, `file_size_bytes`, `file_size_mb`

### resize_video

Resizes a video with optional aspect ratio preservation.

**Parameters:**
- `input_path` (str): Path to input video
- `output_path` (str): Path for output video
- `width` (int): Target width in pixels (optional)
- `height` (int): Target height in pixels (optional)
- `maintain_aspect_ratio` (bool): Preserve aspect ratio (default: True)
- `scale` (float): Scale factor (e.g., 0.5 for half size, overrides width/height)

**Returns:** Dict with `success`, `output_path`, `original_resolution`, `output_resolution`, `duration`, `aspect_ratio_maintained`

**Note:** Currently has compatibility issues with newer Pillow versions. Will be fixed in future moviepy updates.

### extract_audio

Extracts audio track from a video.

**Parameters:**
- `input_path` (str): Path to input video
- `output_path` (str): Path for output audio file
- `audio_format` (str): Output format - 'mp3' (default), 'wav', 'aac', 'flac', 'm4a'

**Returns:** Dict with `success`, `output_path`, `video_duration`, `audio_format`, `has_audio`

### add_audio

Adds or replaces audio track in a video.

**Parameters:**
- `video_path` (str): Path to input video
- `audio_path` (str): Path to audio file
- `output_path` (str): Path for output video
- `replace_audio` (bool): Replace existing audio (default: True) or mix with it

**Returns:** Dict with `success`, `output_path`, `video_duration`, `audio_adjusted`, `replaced_audio`

**Note:** Audio is automatically trimmed or looped to match video duration.

### convert_video

Converts a video to a different format with specified codecs.

**Parameters:**
- `input_path` (str): Path to input video
- `output_path` (str): Path for output video
- `output_format` (str): Output format (default: 'mp4')
- `video_codec` (str): Video codec - 'libx264' (H.264, default), 'libx265' (H.265/HEVC), 'mpeg4', 'libvpx' (VP8), 'libvpx-vp9' (VP9)
- `audio_codec` (str): Audio codec - 'aac' (default), 'mp3', 'libvorbis', 'pcm_s16le' (WAV)

**Returns:** Dict with `success`, `output_path`, `original_format`, `output_format`, `video_codec`, `audio_codec`, `duration`, `resolution`

## Supported Video Formats

- MP4
- AVI
- MOV
- MKV
- FLV
- WMV
- WebM
- M4V
- MPG/MPEG

## Testing

Run the comprehensive test suite:

```bash
cd src/universal_mcp/applications/video_tools
uv run python test_video_tools.py
```

The test suite will:
1. Create sample test videos with colored backgrounds and audio
2. Run all video manipulation operations
3. Save output videos to a temporary directory for manual inspection
4. Report success/failure for each operation

## Performance Notes

- **Fast Operations**: get_video_info (< 1 second)
- **Medium Operations**: trim_video, extract_audio (1-5 seconds)
- **Slow Operations**: stitch_videos, resize_video, add_audio, convert_video (5-30+ seconds depending on video size)

All slow operations show progress bars during processing.

## Tags

Each tool is tagged for easy discovery:

- `video` - All video operations
- `stitch`, `concatenate`, `merge`, `join` - Video stitching
- `trim`, `cut`, `clip` - Trimming operations
- `audio`, `extract`, `add`, `soundtrack` - Audio operations
- `important` - Frequently used tools
- `slow` - Operations that take >2 seconds

## Example Workflows

### Create Video Montage

```python
# Stitch multiple clips with crossfade transitions
result = await app.stitch_videos(
    input_paths=[
        'vacation_1.mp4',
        'vacation_2.mp4',
        'vacation_3.mp4',
        'vacation_4.mp4',
    ],
    output_path='vacation_montage.mp4',
    method='crossfade',
    transition_duration=0.5,  # Half second transitions
    resize_mode='largest',  # Use highest resolution
)
print(f"Created montage: {result['total_duration']}s")
```

### Extract Highlight Clip

```python
# Get video info
info = await app.get_video_info(input_path='full_video.mp4')
print(f"Original duration: {info['duration']}s")

# Trim to highlight section
result = await app.trim_video(
    input_path='full_video.mp4',
    output_path='highlight.mp4',
    start_time=120.0,  # Start at 2 minutes
    duration=30.0,     # 30 second clip
)

# Resize for social media
result = await app.resize_video(
    input_path='highlight.mp4',
    output_path='highlight_720p.mp4',
    height=720,
    maintain_aspect_ratio=True,
)
```

### Add Soundtrack to Video

```python
# Extract original audio for backup
await app.extract_audio(
    input_path='video.mp4',
    output_path='original_audio.mp3',
)

# Add new soundtrack
result = await app.add_audio(
    video_path='video.mp4',
    audio_path='soundtrack.mp3',
    output_path='video_with_music.mp4',
    replace_audio=True,  # Replace original audio
)

# Audio will be automatically looped/trimmed to match video length
print(f"Audio adjusted: {result['audio_adjusted']}")
```

### Convert for Web

```python
# Convert to web-friendly format
result = await app.convert_video(
    input_path='raw_video.mov',
    output_path='web_video.mp4',
    video_codec='libx264',  # H.264 for compatibility
    audio_codec='aac',
)

# Optionally resize for faster loading
result = await app.resize_video(
    input_path='web_video.mp4',
    output_path='web_video_720p.mp4',
    scale=0.5,  # Half the size
)
```

### Create Multi-Part Series

```python
# Split long video into parts
info = await app.get_video_info(input_path='long_video.mp4')
total_duration = info['duration']
part_duration = 300  # 5 minutes per part

parts = []
for i, start_time in enumerate(range(0, int(total_duration), part_duration)):
    part_path = f'part_{i+1}.mp4'
    await app.trim_video(
        input_path='long_video.mp4',
        output_path=part_path,
        start_time=start_time,
        duration=part_duration,
    )
    parts.append(part_path)

print(f"Created {len(parts)} parts")
```

## Known Issues

1. **resize_video**: Currently has compatibility issues with Pillow 10+ due to deprecated `PIL.Image.ANTIALIAS`. This is a known moviepy issue that will be fixed in future versions.
   - **Workaround**: Use `scale` parameter or wait for moviepy 2.x release

2. **Progress bars**: Moviepy shows progress bars in console output. This is normal behavior.

3. **Temp files**: Moviepy creates temporary audio files during processing. These are automatically cleaned up.

## Contributing

When adding new video manipulation tools:

1. Follow the async function pattern
2. Include comprehensive docstrings with Args, Returns, Raises, Tags
3. Validate input parameters and file paths
4. Handle errors gracefully with proper cleanup
5. Return consistent dict structure with `success` field
6. Close video clips properly to prevent memory leaks
7. Add test cases to `test_video_tools.py`
8. Update this README with new tool documentation

## Dependencies

- **moviepy** (1.0.3+) - Main video processing library
- **imageio-ffmpeg** (auto-installed) - FFmpeg binaries for video encoding/decoding
- **numpy** (auto-installed) - Array operations for video frames
- **Pillow** (auto-installed) - Image processing for frames

## License

MIT License - See main project LICENSE file
