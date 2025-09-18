# ReplicateApp MCP Server

An MCP Server for the ReplicateApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ReplicateApp API.


| Tool | Description |
|------|-------------|
| `run` | Executes a Replicate model synchronously, blocking until it completes and returns the final output. This abstracts the polling logic required by asynchronous jobs. If a model streams results, this function conveniently collects all items into a list before returning, unlike the non-blocking `submit_prediction` method. |
| `submit_prediction` | Submits a model execution request to Replicate for non-blocking, asynchronous processing. It immediately returns a prediction ID for tracking, unlike the synchronous `run` method which waits for the final result. The returned ID can be used with `get_prediction` or `fetch_prediction_output` to monitor the job. |
| `get_prediction` | Retrieves the full details and current state of a Replicate prediction by its ID. This function performs a non-blocking status check, returning the prediction object immediately. Unlike `fetch_prediction_output`, it does not wait for the job to complete and is used for monitoring progress. |
| `await_prediction_result` | Retrieves the final output for a given prediction ID, waiting for the job to complete if it is still running. This function complements `submit_prediction` by blocking until the asynchronous task finishes, raising an error if the prediction fails or is canceled. |
| `cancel_prediction` | Sends a request to cancel a running or queued Replicate prediction. It first checks the prediction's status, only proceeding if it is not already in a terminal state (e.g., succeeded, failed), and gracefully handles jobs that cannot be canceled. |
| `upload_file` | Uploads a local file from a given path to Replicate's storage, returning a public URL. This URL is essential for providing file-based inputs to Replicate models via functions like `run` or `submit_prediction`. Fails if the file is not found or the upload encounters an error. |
| `generate_image` | Generates images synchronously using a specified model, defaulting to SDXL. As a convenience wrapper around the generic `run` function, it simplifies image creation by exposing common parameters like `prompt` and `width`, and waits for the model to complete before returning the resulting image URLs. |
