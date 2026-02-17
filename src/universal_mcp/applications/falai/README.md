---
name: falai
description: Application for interacting with the Fal AI platform. Provides tools to run, submit, check status, retrieve results, cancel jobs, upload files to the Fal CDN, and a specialized tool for generating images. Authentication is handled by the configured Integration provided by the Universal MCP server, fetching the necessary API key.
---

# Falai Integration

Application for interacting with the Fal AI platform. Provides tools to run, submit, check status, retrieve results, cancel jobs, upload files to the Fal CDN, and a specialized tool for generating images. Authentication is handled by the configured Integration provided by the Universal MCP server, fetching the necessary API key.

## Available Tools

| Tool | Description |
|------|-------------|
| `generate_image` | Generates an image from a text prompt using specified Fal AI models. This tool supports state-of-the-art models like Flux, Recraft V3, and Stable Diffusion 3.5. |
| `submit_video_generation` | Submits a video generation task using Fal AI models and returns a request ID. This is an asynchronous operation. Use `get_generation_status` and `get_generation_result` with the returned ID. |
| `submit_start_end_video_generation` | Submits a video generation task using start and end images. |
| `get_generation_status` | Checks the status of a video generation task. |
| `get_generation_result` | Retrieves the result of a completed video generation task. This method will block until the task is complete if it is not already. |
| `transcribe_audio` | Converts speech to text from an audio file URL using Fal AI models. |
