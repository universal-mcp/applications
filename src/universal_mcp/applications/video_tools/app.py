"""
Video Tools Application

Provides video manipulation capabilities including stitching, trimming, resizing, audio extraction/addition, and more.
Supports both local file paths and remote URLs for input files.
"""

import os
import tempfile
import urllib.parse
from pathlib import Path
from typing import Any, List, Tuple, Optional
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class VideoToolsApp(APIApplication):
    """
    Video manipulation tools for common operations.

    Supports video stitching, trimming, resizing, audio operations, format conversion,
    and other transformations using moviepy library.
    Accepts both local file paths and remote URLs for input files.
    """

    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="video_tools", integration=integration, **kwargs)
        self.supported_formats = {".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm", ".m4v", ".mpg", ".mpeg"}
        self._temp_files = []  # Track temporary downloaded files for cleanup

    def _is_url(self, path: str) -> bool:
        """
        Checks if a path is a URL.

        Args:
            path: Path or URL string to check

        Returns:
            bool: True if the path is a URL, False otherwise
        """
        try:
            result = urllib.parse.urlparse(path)
            return all([result.scheme, result.netloc]) and result.scheme in ["http", "https"]
        except Exception:
            return False

    async def _download_file(self, url: str, suffix: str = None) -> Path:
        """
        Downloads a file from a URL to a temporary location.

        Args:
            url: URL of the file to download
            suffix: Optional file extension (e.g., '.mp4'). If not provided, inferred from URL

        Returns:
            Path: Path to the downloaded temporary file

        Raises:
            ValueError: If the URL is invalid or download fails
            IOError: If the file cannot be written
        """
        try:
            import httpx
        except ImportError:
            raise ImportError("httpx library is required for downloading files from URLs. Install it with: pip install httpx")

        # Infer suffix from URL if not provided
        if suffix is None:
            parsed_url = urllib.parse.urlparse(url)
            path_part = parsed_url.path
            suffix = Path(path_part).suffix
            if not suffix:
                suffix = ".tmp"

        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        temp_path = Path(temp_file.name)
        temp_file.close()

        # Track for cleanup
        self._temp_files.append(temp_path)

        try:
            # Download file
            async with httpx.AsyncClient(timeout=300.0) as client:  # 5 minute timeout
                response = await client.get(url, follow_redirects=True)
                response.raise_for_status()

                # Write to temp file
                temp_path.write_bytes(response.content)

            return temp_path

        except Exception as e:
            # Clean up on error
            if temp_path.exists():
                temp_path.unlink()
            if temp_path in self._temp_files:
                self._temp_files.remove(temp_path)
            raise ValueError(f"Failed to download file from URL: {url}. Error: {str(e)}")

    def _cleanup_temp_files(self):
        """Removes all temporary downloaded files."""
        for temp_file in self._temp_files:
            try:
                if temp_file.exists():
                    temp_file.unlink()
            except Exception:
                pass  # Ignore cleanup errors
        self._temp_files.clear()

    async def _validate_video_url(self, video_url: str) -> Path:
        """
        Validates that the video URL (mandatory) and downloads it.

        Args:
            video_url: URL to the video file

        Returns:
            Path: Validated Path object (temporary file)

        Raises:
            ValueError: If input is not a URL or download fails or format is unsupported
        """
        # Check if it's a URL
        if self._is_url(video_url):
            path = await self._download_file(video_url)
        elif Path(video_url).exists():
            path = Path(video_url)
            if not path.is_file():
                raise ValueError(f"Path exists but is not a file: {video_url}")
        else:
            raise ValueError(f"Video input must be a URL. Local file paths are not supported: {video_url}")

        if path.suffix.lower() not in self.supported_formats:
            # Cleanup downloaded file if invalid format
            if path in self._temp_files:
                try:
                    os.unlink(path)
                    self._temp_files.remove(path)
                except:
                    pass

            raise ValueError(f"Unsupported video format: {path.suffix}. Supported formats: {', '.join(self.supported_formats)}")

        return path

    def _ensure_output_directory(self, output_path: str) -> Path:
        """
        Ensures the output directory exists.

        Args:
            output_path: Path where the output video will be saved

        Returns:
            Path: Validated output Path object
        """
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path

    async def stitch_videos(
        self,
        video_urls: List[str],
        output_path: str,
        method: str = "concatenate",
        transition_duration: float = 0.0,
        resize_mode: str = "first",
    ) -> dict[str, Any]:
        """
        Stitches multiple video files together into a single video file in the order provided.
        Videos can be concatenated directly or with optional crossfade transitions between clips.
        The output video resolution can match the first video, largest video, or smallest video.
        **Supports ONLY URLs for input videos.**

        Args:
            video_urls: List of URLs to input video files in the order they should be stitched. Must contain at least 2 videos. Example: ['https://example.com/video1.mp4', 'https://example.com/video2.mp4']
            output_path: Path where the stitched video will be saved. Example: '/path/to/output.mp4'
            method: Stitching method. Options: 'concatenate' (direct join, default), 'crossfade' (smooth transition). Example: 'concatenate'
            transition_duration: Duration of crossfade transition in seconds (only used if method='crossfade'). Example: 1.0 for 1 second fade. Default: 0.0
            resize_mode: How to handle videos with different resolutions. Options: 'first' (match first video, default), 'largest' (match largest resolution), 'smallest' (match smallest resolution). Example: 'first'

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the stitched video
                - 'num_videos' (int): Number of videos stitched together
                - 'total_duration' (float): Total duration of output video in seconds
                - 'output_resolution' (tuple): Output video resolution (width, height)
                - 'method' (str): Stitching method used

        Raises:
            ValueError: Raised when input_paths has fewer than 2 videos, any video doesn't exist, URL is invalid, or format is unsupported.
            IOError: Raised when videos cannot be opened or output cannot be saved.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, stitch, concatenate, merge, join, important, slow
        """
        # Validate input
        if len(video_urls) < 2:
            raise ValueError("At least 2 videos are required for stitching")

        # Import moviepy (lazy import)
        try:
            from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Validate paths (and download)
        validated_paths = []
        for path in video_urls:
            input_path_obj = await self._validate_video_url(path)
            validated_paths.append(input_path_obj)

        output_path_obj = self._ensure_output_directory(output_path)

        # Load all video clips
        clips = [VideoFileClip(str(path)) for path in validated_paths]

        try:
            # Determine target resolution
            if resize_mode == "first":
                target_size = clips[0].size
            elif resize_mode == "largest":
                target_size = max((clip.size for clip in clips), key=lambda s: s[0] * s[1])
            elif resize_mode == "smallest":
                target_size = min((clip.size for clip in clips), key=lambda s: s[0] * s[1])
            else:
                raise ValueError(f"Invalid resize_mode: {resize_mode}. Must be 'first', 'largest', or 'smallest'")

            # Resize clips if needed
            resized_clips = []
            for clip in clips:
                if clip.size != target_size:
                    resized_clips.append(clip.resize(target_size))
                else:
                    resized_clips.append(clip)

            # Stitch videos
            if method == "concatenate":
                final_clip = concatenate_videoclips(resized_clips, method="compose")
            elif method == "crossfade":
                if transition_duration <= 0:
                    raise ValueError("transition_duration must be > 0 for crossfade method")
                final_clip = concatenate_videoclips(resized_clips, method="compose", padding=-transition_duration)
            else:
                raise ValueError(f"Invalid method: {method}. Must be 'concatenate' or 'crossfade'")

            # Get output info
            total_duration = final_clip.duration
            output_resolution = final_clip.size

            # Write output
            final_clip.write_videofile(
                str(output_path_obj),
                codec="libx264",
                audio_codec="aac",
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
            )

            # Cleanup
            final_clip.close()
            for clip in clips:
                clip.close()

            # Clean up temporary downloaded files
            self._cleanup_temp_files()

            return {
                "success": True,
                "output_path": str(output_path_obj),
                "num_videos": len(video_urls),
                "total_duration": round(total_duration, 2),
                "output_resolution": output_resolution,
                "method": method,
            }

        except Exception as e:
            # Cleanup on error
            for clip in clips:
                try:
                    clip.close()
                except:
                    pass
            # Clean up temporary downloaded files
            self._cleanup_temp_files()
            raise

    async def trim_video(
        self,
        video_url: str,
        output_path: str,
        start_time: float = 0.0,
        end_time: Optional[float] = None,
        duration: Optional[float] = None,
    ) -> dict[str, Any]:
        """
        Trims a video to a specific time range, creating a shorter clip from the original video.
        You can specify either the end time or the duration, but not both.
        **Supports ONLY URLs for input video.**

        Args:
            video_url: URL to the input video file. Example: 'https://example.com/video.mp4'
            output_path: Path where the trimmed video will be saved. Example: '/path/to/trimmed.mp4'
            start_time: Start time in seconds. Example: 10.0 for starting at 10 seconds. Default: 0.0
            end_time: End time in seconds (optional, cannot be used with duration). Example: 30.0 for ending at 30 seconds
            duration: Duration of output clip in seconds (optional, cannot be used with end_time). Example: 15.0 for 15 second clip

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the trimmed video
                - 'original_duration' (float): Original video duration in seconds
                - 'output_duration' (float): Trimmed video duration in seconds
                - 'start_time' (float): Start time used in seconds
                - 'end_time' (float): End time used in seconds
                - 'resolution' (tuple): Video resolution (width, height)

        Raises:
            ValueError: Raised when both end_time and duration are specified, times are invalid, or input video doesn't exist.
            IOError: Raised when video cannot be opened or output cannot be saved.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, trim, cut, clip, extract, important
        """
        # Validate input
        if end_time is not None and duration is not None:
            raise ValueError("Cannot specify both end_time and duration")

        if end_time is None and duration is None:
            raise ValueError("Must specify either end_time or duration")

        # Import moviepy
        try:
            from moviepy.editor import VideoFileClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Validate paths (may download from URL)
        input_path_obj = await self._validate_video_url(video_url)
        output_path_obj = self._ensure_output_directory(output_path)

        # Load video
        clip = VideoFileClip(str(input_path_obj))

        try:
            original_duration = clip.duration

            # Calculate end_time
            if duration is not None:
                end_time = start_time + duration

            # Validate times
            if start_time < 0:
                raise ValueError(f"start_time must be >= 0, got {start_time}")

            if end_time > original_duration:
                raise ValueError(f"end_time ({end_time}s) exceeds video duration ({original_duration}s)")

            if start_time >= end_time:
                raise ValueError(f"start_time ({start_time}s) must be less than end_time ({end_time}s)")

            # Trim video
            trimmed_clip = clip.subclip(start_time, end_time)
            output_duration = trimmed_clip.duration
            resolution = trimmed_clip.size

            # Write output
            trimmed_clip.write_videofile(
                str(output_path_obj),
                codec="libx264",
                audio_codec="aac",
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
            )

            # Cleanup
            trimmed_clip.close()
            clip.close()

            # Clean up temporary downloaded files
            self._cleanup_temp_files()

            return {
                "success": True,
                "output_path": str(output_path_obj),
                "original_duration": round(original_duration, 2),
                "output_duration": round(output_duration, 2),
                "start_time": start_time,
                "end_time": end_time,
                "resolution": resolution,
            }

        except Exception as e:
            clip.close()
            # Clean up temporary downloaded files
            self._cleanup_temp_files()
            raise

    async def get_video_info(
        self,
        input_url: str,
    ) -> dict[str, Any]:
        """
        Retrieves detailed information about a video file including duration, resolution, fps, codec, and file size.
        Useful for understanding video properties before performing transformations.
        **Supports ONLY URLs.**

        Args:
            input_url: URL to the input video file. Example: 'https://example.com/video.mp4'

        Returns:
            dict[str, Any]: Video information containing:
                - 'success' (bool): Whether the operation succeeded
                - 'path' (str): Full path to the video file
                - 'duration' (float): Video duration in seconds
                - 'resolution' (tuple): Video resolution (width, height) in pixels
                - 'width' (int): Video width in pixels
                - 'height' (int): Video height in pixels
                - 'fps' (float): Frames per second
                - 'has_audio' (bool): Whether video has audio track
                - 'file_size_bytes' (int): File size in bytes
                - 'file_size_mb' (float): File size in megabytes (rounded to 2 decimals)

        Raises:
            ValueError: Raised when input video doesn't exist or format is unsupported.
            IOError: Raised when video cannot be opened.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, info, metadata, properties, important
        """
        # Import moviepy
        try:
            from moviepy.editor import VideoFileClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Validate path (may download from URL)
        input_path_obj = await self._validate_video_url(input_url)

        # Get file size
        file_size_bytes = input_path_obj.stat().st_size
        file_size_mb = round(file_size_bytes / (1024 * 1024), 2)

        # Load video and get properties
        clip = VideoFileClip(str(input_path_obj))

        try:
            info = {
                "success": True,
                "path": str(input_path_obj),
                "duration": round(clip.duration, 2),
                "resolution": clip.size,
                "width": clip.w,
                "height": clip.h,
                "fps": round(clip.fps, 2),
                "has_audio": clip.audio is not None,
                "file_size_bytes": file_size_bytes,
                "file_size_mb": file_size_mb,
            }

            clip.close()

            # Clean up temporary downloaded files
            self._cleanup_temp_files()

            return info

        except Exception as e:
            clip.close()
            raise

    async def resize_video(
        self,
        input_url: str,
        output_path: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
        maintain_aspect_ratio: bool = True,
        scale: Optional[float] = None,
    ) -> dict[str, Any]:
        """
        Resizes a video to specified dimensions or scale factor with optional aspect ratio preservation.
        You can specify width/height, or use a scale factor (e.g., 0.5 for half size, 2.0 for double size).
        **Supports ONLY URLs.**

        Args:
            input_url: URL to the input video file. Example: 'https://example.com/video.mp4'
            output_path: Path where the resized video will be saved. Example: '/path/to/resized.mp4'
            width: Target width in pixels (optional if height or scale provided). Example: 1920
            height: Target height in pixels (optional if width or scale provided). Example: 1080
            maintain_aspect_ratio: If True and only one dimension specified, calculates the other to preserve aspect ratio. Default: True
            scale: Scale factor for resizing (e.g., 0.5 = half size, 2.0 = double size). If provided, width/height are ignored. Example: 0.5

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the resized video
                - 'original_resolution' (tuple): Original video resolution (width, height)
                - 'output_resolution' (tuple): New video resolution (width, height)
                - 'duration' (float): Video duration in seconds
                - 'aspect_ratio_maintained' (bool): Whether aspect ratio was preserved

        Raises:
            ValueError: Raised when neither width/height nor scale is specified, or input video doesn't exist.
            IOError: Raised when video cannot be opened or output cannot be saved.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, resize, scale, resolution, important, slow
        """
        # Validate input
        if scale is None and width is None and height is None:
            raise ValueError("Must specify either scale or at least one of width/height")

        # Import moviepy
        try:
            from moviepy.editor import VideoFileClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Validate paths
        input_path_obj = await self._validate_video_url(input_url)
        output_path_obj = self._ensure_output_directory(output_path)

        # Load video
        clip = VideoFileClip(str(input_path_obj))

        try:
            original_resolution = clip.size
            original_width, original_height = original_resolution

            # Calculate new dimensions
            if scale is not None:
                # Use scale factor
                new_width = int(original_width * scale)
                new_height = int(original_height * scale)
                aspect_ratio_maintained = True
            else:
                # Use width/height
                if maintain_aspect_ratio:
                    if width is None:
                        # Calculate width from height
                        aspect_ratio = original_width / original_height
                        new_width = int(height * aspect_ratio)
                        new_height = height
                    elif height is None:
                        # Calculate height from width
                        aspect_ratio = original_height / original_width
                        new_height = int(width * aspect_ratio)
                        new_width = width
                    else:
                        # Both specified, use them
                        new_width = width
                        new_height = height
                    aspect_ratio_maintained = True
                else:
                    # Don't maintain aspect ratio
                    new_width = width if width is not None else original_width
                    new_height = height if height is not None else original_height
                    aspect_ratio_maintained = False

            new_resolution = (new_width, new_height)

            # Resize video
            resized_clip = clip.resize(newsize=new_resolution)
            duration = resized_clip.duration

            # Write output
            resized_clip.write_videofile(
                str(output_path_obj),
                codec="libx264",
                audio_codec="aac",
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
            )

            # Cleanup
            resized_clip.close()
            clip.close()

            # Clean up temporary downloaded files
            self._cleanup_temp_files()

            return {
                "success": True,
                "output_path": str(output_path_obj),
                "original_resolution": original_resolution,
                "output_resolution": new_resolution,
                "duration": round(duration, 2),
                "aspect_ratio_maintained": aspect_ratio_maintained,
            }

        except Exception as e:
            clip.close()
            # Clean up temporary downloaded files
            self._cleanup_temp_files()
            raise

    async def extract_audio(
        self,
        input_url: str,
        output_path: str,
        audio_format: str = "mp3",
    ) -> dict[str, Any]:
        """
        Extracts the audio track from a video file and saves it as a separate audio file.
        Supports multiple audio formats including MP3, WAV, AAC, and FLAC.
        **Supports ONLY URLs.**

        Args:
            input_url: URL to the input video file. Example: 'https://example.com/video.mp4'
            output_path: Path where the extracted audio will be saved. Example: '/path/to/audio.mp3'
            audio_format: Output audio format. Options: 'mp3' (default), 'wav', 'aac', 'flac', 'm4a'. Example: 'mp3'

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the extracted audio file
                - 'video_duration' (float): Original video duration in seconds
                - 'audio_format' (str): Output audio format used
                - 'has_audio' (bool): Whether the video had an audio track

        Raises:
            ValueError: Raised when input video doesn't exist or has no audio track.
            IOError: Raised when video cannot be opened or audio cannot be saved.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, audio, extract, separate, important
        """
        # Import moviepy
        try:
            from moviepy.editor import VideoFileClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Validate paths
        input_path_obj = await self._validate_video_url(input_url)
        output_path_obj = self._ensure_output_directory(output_path)

        # Load video
        clip = VideoFileClip(str(input_path_obj))

        try:
            # Check if video has audio
            if clip.audio is None:
                clip.close()
                raise ValueError("Video has no audio track to extract")

            duration = clip.duration

            # Extract audio
            audio = clip.audio
            audio.write_audiofile(
                str(output_path_obj),
                codec="libmp3lame" if audio_format == "mp3" else None,
            )

            # Cleanup
            clip.close()

            return {
                "success": True,
                "output_path": str(output_path_obj),
                "video_duration": round(duration, 2),
                "audio_format": audio_format,
                "has_audio": True,
            }

        except Exception as e:
            clip.close()
            # Clean up temporary downloaded files
            self._cleanup_temp_files()
            raise

    async def add_audio(
        self,
        video_url: str,
        audio_url: str,
        output_path: str,
        replace_audio: bool = True,
    ) -> dict[str, Any]:
        """
        Adds or replaces the audio track in a video file with audio from a separate audio file.
        The audio will be trimmed or looped to match the video duration.

        Args:
            video_url: URL to the input video file. Example: 'https://example.com/video.mp4'
            audio_url: URL to the audio file to add. Example: 'https://example.com/audio.mp3'
            output_path: Path where the video with new audio will be saved. Example: '/path/to/output.mp4'
            replace_audio: If True, replaces existing audio. If False, mixes with existing audio. Default: True

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the output video
                - 'video_duration' (float): Video duration in seconds
                - 'audio_adjusted' (bool): Whether audio was trimmed or looped to match video
                - 'replaced_audio' (bool): Whether original audio was replaced

        Raises:
            ValueError: Raised when video or audio file doesn't exist.
            IOError: Raised when files cannot be opened or output cannot be saved.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, audio, add, replace, soundtrack, important, slow
        """
        # Import moviepy
        try:
            from moviepy.editor import VideoFileClip, AudioFileClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Validate paths
        video_path_obj = await self._validate_video_url(video_url)

        # Validate audio path (must be URL)
        if self._is_url(audio_url):
            audio_path_obj = await self._download_file(audio_url)
        else:
            raise ValueError(f"Audio input must be a URL. Local file paths are not supported: {audio_url}")

        if not audio_path_obj.exists():
            raise ValueError(f"Audio file failed to download: {audio_url}")

        output_path_obj = self._ensure_output_directory(output_path)

        # Load video and audio
        video_clip = VideoFileClip(str(video_path_obj))
        audio_clip = AudioFileClip(str(audio_path_obj))

        try:
            video_duration = video_clip.duration
            audio_duration = audio_clip.duration

            # Adjust audio to match video duration
            audio_adjusted = False
            if audio_duration > video_duration:
                # Trim audio
                audio_clip = audio_clip.subclip(0, video_duration)
                audio_adjusted = True
            elif audio_duration < video_duration:
                # Loop audio
                num_loops = int(video_duration / audio_duration) + 1
                from moviepy.audio.AudioClip import concatenate_audioclips

                audio_clip = concatenate_audioclips([audio_clip] * num_loops).subclip(0, video_duration)
                audio_adjusted = True

            # Set audio on video
            if replace_audio:
                final_clip = video_clip.set_audio(audio_clip)
            else:
                # Mix audio (if video has existing audio)
                if video_clip.audio is not None:
                    from moviepy.audio.AudioClip import CompositeAudioClip

                    mixed_audio = CompositeAudioClip([video_clip.audio, audio_clip])
                    final_clip = video_clip.set_audio(mixed_audio)
                else:
                    final_clip = video_clip.set_audio(audio_clip)

            # Write output
            final_clip.write_videofile(
                str(output_path_obj),
                codec="libx264",
                audio_codec="aac",
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
            )

            # Cleanup
            final_clip.close()
            video_clip.close()
            audio_clip.close()

            return {
                "success": True,
                "output_path": str(output_path_obj),
                "video_duration": round(video_duration, 2),
                "audio_adjusted": audio_adjusted,
                "replaced_audio": replace_audio,
            }

        except Exception as e:
            video_clip.close()
            audio_clip.close()
            # Clean up temporary downloaded files
            self._cleanup_temp_files()
            raise

    async def convert_video(
        self,
        input_url: str,
        output_path: str,
        output_format: str = "mp4",
        video_codec: str = "libx264",
        audio_codec: str = "aac",
    ) -> dict[str, Any]:
        """
        Converts a video file to a different format with specified codecs.
        Useful for compatibility, compression, or quality adjustments.

        Args:
            input_url: URL to the input video file. Example: 'https://example.com/video.avi'
            output_path: Path where the converted video will be saved. Example: '/path/to/video.mp4'
            output_format: Output video format (inferred from output_path extension, this is for validation). Example: 'mp4'
            video_codec: Video codec to use. Options: 'libx264' (H.264, default), 'libx265' (H.265/HEVC), 'mpeg4', 'libvpx' (VP8), 'libvpx-vp9' (VP9). Example: 'libx264'
            audio_codec: Audio codec to use. Options: 'aac' (default), 'mp3', 'libvorbis', 'pcm_s16le' (WAV). Example: 'aac'

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the converted video
                - 'original_format' (str): Original video format
                - 'output_format' (str): Output video format
                - 'video_codec' (str): Video codec used
                - 'audio_codec' (str): Audio codec used
                - 'duration' (float): Video duration in seconds
                - 'resolution' (tuple): Video resolution (width, height)

        Raises:
            ValueError: Raised when input video doesn't exist or format is unsupported.
            IOError: Raised when video cannot be opened or output cannot be saved.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, convert, format, codec, transcode, important, slow
        """
        # Import moviepy
        try:
            from moviepy.editor import VideoFileClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Validate paths
        input_path_obj = await self._validate_video_url(input_url)
        output_path_obj = self._ensure_output_directory(output_path)

        # Load video
        clip = VideoFileClip(str(input_path_obj))

        try:
            original_format = input_path_obj.suffix.lower()
            duration = clip.duration
            resolution = clip.size

            # Write output with specified codecs
            clip.write_videofile(
                str(output_path_obj),
                codec=video_codec,
                audio_codec=audio_codec,
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
            )

            # Cleanup
            clip.close()

            return {
                "success": True,
                "output_path": str(output_path_obj),
                "original_format": original_format,
                "output_format": output_format,
                "video_codec": video_codec,
                "audio_codec": audio_codec,
                "duration": round(duration, 2),
                "resolution": resolution,
            }

        except Exception as e:
            clip.close()
            # Clean up temporary downloaded files
            self._cleanup_temp_files()
            raise

    async def change_video_speed(
        self,
        input_url: str,
        output_path: str,
        speed_factor: float,
        preserve_pitch: bool = True,
    ) -> dict[str, Any]:
        """
        Changes the playback speed of a video by a specified factor, making it faster or slower.
        Audio pitch can be preserved or adjusted proportionally with the speed change.

        Args:
            input_url: URL to the input video file. Example: 'https://example.com/video.mp4'
            output_path: Path where the speed-adjusted video will be saved. Example: '/path/to/fast_video.mp4'
            speed_factor: Speed multiplication factor. Values > 1.0 speed up the video (e.g., 2.0 = 2x speed, twice as fast), values < 1.0 slow it down (e.g., 0.5 = half speed, slow motion). Example: 2.0 for double speed
            preserve_pitch: If True, attempts to preserve audio pitch when changing speed. If False, audio pitch changes with speed (chipmunk effect when faster, deep voice when slower). Default: True

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the speed-adjusted video
                - 'original_duration' (float): Original video duration in seconds
                - 'output_duration' (float): New video duration in seconds
                - 'speed_factor' (float): Speed factor applied
                - 'preserve_pitch' (bool): Whether pitch preservation was attempted
                - 'resolution' (tuple): Video resolution (width, height)
                - 'has_audio' (bool): Whether the video has audio

        Raises:
            ValueError: Raised when speed_factor is <= 0, or input video doesn't exist.
            IOError: Raised when video cannot be opened or output cannot be saved.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, speed, fast, slow, timelapse, slowmotion, important, slow
        """
        # Validate input
        if speed_factor <= 0:
            raise ValueError(f"speed_factor must be > 0, got {speed_factor}")

        # Import moviepy
        try:
            from moviepy.editor import VideoFileClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Validate paths
        input_path_obj = await self._validate_video_url(input_url)
        output_path_obj = self._ensure_output_directory(output_path)

        # Load video
        clip = VideoFileClip(str(input_path_obj))

        try:
            original_duration = clip.duration
            resolution = clip.size
            has_audio = clip.audio is not None

            # Change speed
            # Note: moviepy's speedx with final_duration parameter
            final_duration = original_duration / speed_factor

            # Apply speed change
            if has_audio and preserve_pitch:
                # Use fx to change speed while preserving pitch
                try:
                    from moviepy.editor import vfx

                    speed_clip = clip.fx(vfx.speedx, speed_factor)
                except Exception:
                    # Fallback if pitch preservation fails
                    speed_clip = clip.speedx(speed_factor)
            else:
                # Simple speed change (audio pitch will change)
                speed_clip = clip.speedx(speed_factor)

            output_duration = speed_clip.duration

            # Write output
            speed_clip.write_videofile(
                str(output_path_obj),
                codec="libx264",
                audio_codec="aac" if has_audio else None,
                temp_audiofile="temp-audio.m4a" if has_audio else None,
                remove_temp=True,
            )

            # Cleanup
            speed_clip.close()
            clip.close()

            return {
                "success": True,
                "output_path": str(output_path_obj),
                "original_duration": round(original_duration, 2),
                "output_duration": round(output_duration, 2),
                "speed_factor": speed_factor,
                "preserve_pitch": preserve_pitch,
                "resolution": resolution,
                "has_audio": has_audio,
            }

        except Exception as e:
            clip.close()
            # Clean up temporary downloaded files
            self._cleanup_temp_files()
            raise

    async def create_slideshow_from_images(
        self,
        image_urls: List[str],
        output_path: str,
        duration_per_image: float = 3.0,
        fps: int = 24,
        transition_duration: float = 0.0,
        resize_mode: str = "first",
        background_color: Tuple[int, int, int] = (0, 0, 0),
    ) -> dict[str, Any]:
        """
        Creates a video slideshow from a sequence of images with configurable display duration and optional transitions.
        Each image is displayed for the specified duration, and images can be resized to match a common resolution.
        Optional crossfade transitions can be added between images for a smoother viewing experience.

        Args:
            image_urls: List of URLs to input image files in the order they should appear. Must contain at least 1 image. Example: ['https://example.com/img1.jpg', 'https://example.com/img2.png']
            output_path: Path where the slideshow video will be saved. Example: '/path/to/slideshow.mp4'
            duration_per_image: Duration each image is displayed in seconds. Example: 3.0 for 3 seconds per image. Default: 3.0
            fps: Frames per second for the output video. Higher values create smoother transitions. Example: 24 (standard), 30 (smooth). Default: 24
            transition_duration: Duration of crossfade transition between images in seconds. Set to 0 for no transitions. Example: 0.5 for half-second fade. Default: 0.0
            resize_mode: How to handle images with different resolutions. Options: 'first' (match first image, default), 'largest' (match largest resolution), 'smallest' (match smallest resolution), 'fixed' (use a fixed resolution like 1920x1080). Example: 'first'
            background_color: RGB color tuple (R, G, B) for padding/background when images don't match aspect ratio, where each value is 0-255. Example: (0, 0, 0) for black, (255, 255, 255) for white. Default: (0, 0, 0)

        Returns:
            dict[str, Any]: Operation result containing:
                - 'success' (bool): Whether the operation succeeded
                - 'output_path' (str): Path to the slideshow video
                - 'num_images' (int): Number of images in the slideshow
                - 'total_duration' (float): Total duration of the video in seconds
                - 'output_resolution' (tuple): Output video resolution (width, height)
                - 'fps' (int): Frames per second used
                - 'transition_duration' (float): Transition duration used in seconds

        Raises:
            ValueError: Raised when image_paths is empty, any image doesn't exist, or format is unsupported.
            IOError: Raised when images cannot be opened or output cannot be saved.
            ImportError: Raised when moviepy library is not installed.

        Tags:
            video, slideshow, images, create, timelapse, important, slow
        """
        # Validate input
        if len(image_urls) < 1:
            raise ValueError("At least 1 image is required to create a slideshow")

        if duration_per_image <= 0:
            raise ValueError(f"duration_per_image must be > 0, got {duration_per_image}")

        # Import moviepy
        try:
            from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip
        except ImportError:
            raise ImportError("moviepy library is required for video operations. Install it with: pip install moviepy")

        # Import PIL for image validation
        try:
            from PIL import Image
        except ImportError:
            raise ImportError("PIL/Pillow library is required for image operations. Install it with: pip install Pillow")

        # Validate all image paths
        validated_paths = []
        for img_path in image_urls:
            if self._is_url(img_path):
                validated_path = await self._download_file(img_path)
                validated_paths.append(validated_path)
            else:
                raise ValueError(f"Image input must be a URL: {img_path}")

        output_path_obj = self._ensure_output_directory(output_path)

        # Get image sizes to determine target resolution
        image_sizes = []
        for img_path in validated_paths:
            with Image.open(img_path) as img:
                image_sizes.append(img.size)

        # Determine target resolution
        if resize_mode == "first":
            target_size = image_sizes[0]
        elif resize_mode == "largest":
            target_size = max(image_sizes, key=lambda s: s[0] * s[1])
        elif resize_mode == "smallest":
            target_size = min(image_sizes, key=lambda s: s[0] * s[1])
        elif resize_mode == "fixed":
            target_size = (1920, 1080)  # Full HD default
        else:
            raise ValueError(f"Invalid resize_mode: {resize_mode}. Must be 'first', 'largest', 'smallest', or 'fixed'")

        # Create image clips
        clips = []
        for img_path in validated_paths:
            # Create clip from image
            clip = ImageClip(str(img_path), duration=duration_per_image)

            # Resize to target size while maintaining aspect ratio
            clip = clip.resize(height=target_size[1] if clip.h > clip.w else None, width=target_size[0] if clip.w >= clip.h else None)

            # Center the clip on a background of target size if needed
            if clip.size != target_size:
                from moviepy.video.VideoClip import ColorClip

                bg = ColorClip(size=target_size, color=background_color, duration=duration_per_image)
                clip = CompositeVideoClip([bg, clip.set_position("center")])

            clip = clip.set_fps(fps)
            clips.append(clip)

        try:
            # Concatenate clips
            if transition_duration > 0:
                # Apply crossfade transitions
                final_clip = concatenate_videoclips(clips, method="compose", padding=-transition_duration)
            else:
                # Direct concatenation
                final_clip = concatenate_videoclips(clips, method="compose")

            # Calculate total duration
            total_duration = final_clip.duration

            # Write output
            final_clip.write_videofile(
                str(output_path_obj),
                codec="libx264",
                fps=fps,
                audio=False,  # No audio for slideshow
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
            )

            # Cleanup
            final_clip.close()
            for clip in clips:
                try:
                    clip.close()
                except:
                    pass

            return {
                "success": True,
                "output_path": str(output_path_obj),
                "num_images": len(image_urls),
                "total_duration": round(total_duration, 2),
                "output_resolution": target_size,
                "fps": fps,
                "transition_duration": transition_duration,
            }

        except Exception as e:
            # Cleanup on error
            for clip in clips:
                try:
                    clip.close()
                except:
                    pass
            # Clean up temporary downloaded files
            self._cleanup_temp_files()
            raise

    def list_tools(self):
        """Returns list of available video manipulation tools."""
        return [
            self.stitch_videos,
            self.trim_video,
            self.get_video_info,
            self.resize_video,
            self.extract_audio,
            self.add_audio,
            self.convert_video,
            self.change_video_speed,
            self.create_slideshow_from_images,
        ]
