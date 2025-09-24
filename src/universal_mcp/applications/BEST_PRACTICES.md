# Best Practices for Creating MCP Applications

This guide provides best practices for developing new applications for the Universal MCP. We will use the `google_gemini` application as a reference to illustrate key concepts.

## 1. Application Structure

Every application should be a class that inherits from `APIApplication`. This base class provides the necessary foundation for integration with the MCP.

### Basic Class Definition

Your `app.py` file should contain a class definition similar to this:

```python
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

class YourApplicationName(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="your_application_name", integration=integration, **kwargs)
        self._api_client = None # Lazy-loaded client

    # ... your tool methods will go here
```

- **`__init__`**: The constructor initializes the base application with a unique `name` (usually matching the folder name) and the `integration` object, which holds credentials.
- **`_api_client`**: It's a best practice to lazy-load your API client. Initialize it as `None` and create the client instance only when it's first needed.

## 2. Authentication and API Clients

Credentials should never be hard-coded. They are managed through the `integration` object. Use a property to initialize your API client on its first use. This prevents unnecessary setup if the application is loaded but not used.

```python
from google import genai

class GoogleGeminiApp(APIApplication):
    # ... (init method)

    @property
    def genai_client(self) -> genai.Client:
        if self._genai_client is not None:
            return self._genai_client
        
        credentials = self.integration.get_credentials()
        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )
        if not api_key:
            raise ValueError("API key not found in integration credentials")
        
        self._genai_client = genai.Client(api_key=api_key)
        return self._genai_client
```

This `genai_client` property ensures the client is created only once, the first time a tool tries to access it.

## 3. Defining Tools

Public methods within your application class are exposed as tools that the AI can use. For a method to be a valid tool, it must have a detailed docstring and proper type hints.

### Docstrings: The AI's Guide

A well-written docstring is crucial. It's how the AI understands what your tool does, what inputs it needs, and what it returns.

```python
async def generate_text(
    self,
    prompt: Annotated[str, "The prompt to generate text from"],
    model: str = "gemini-2.5-flash",
) -> str:
    """Generates text using the Google Gemini model based on a given prompt.
    This tool is suitable for various natural language processing tasks such as content generation, summarization, translation, and question answering.

    Args:
        prompt (str): The text prompt or instruction for the model to follow. For example: "Write a short story about a robot who learns to love."
        model (str, optional): The Gemini model to use for text generation. Defaults to "gemini-2.5-flash".

    Returns:
        str: The generated text response from the Gemini model.

    Raises:
        ValueError: If the API key is not found in the integration credentials.
        Exception: If the underlying client or API call fails.

    Tags:
        text, generate, llm, important
    """
    response = self.genai_client.models.generate_content(
        contents=prompt, model=model
    )
    return response.text
```

**Docstring Breakdown:**
1.  **Summary Line**: A single, concise sentence describing the tool's main function.
2.  **Detailed Description**: An optional paragraph providing more context, use cases, and why the tool is useful.
3.  **`Args`**: Describe each parameter. For clarity, use `typing.Annotated` to provide a short, user-friendly description directly in the function signature.
4.  **`Returns`**: Clearly describe the output of the function.
5.  **`Raises`**: List any potential exceptions the tool might raise.
6.  **`Tags`**: A comma-separated list of keywords that help in categorizing and discovering the tool. Use `important` for core tools.

### Return Types

-   **Simple Types**: For simple text or data, return standard Python types like `str`, `dict`, or `list`.

-   **Files/Media (Images, Audio, etc.)**: When a tool generates content that should be treated as a file, return a specific dictionary structure. This allows the MCP to handle the data correctly (e.g., saving it to a file or displaying it).

    The structure is:
    ```json
    {
        "type": "image" | "audio" | "video" | "file",
        "data": "<base64_encoded_string>",
        "mime_type": "image/png",
        "file_name": "suggested_filename.png"
    }
    ```

    **Example from `generate_image`:**
    ```python
    return {
        "type": "image",
        "data": img_base64,
        "mime_type": "image/png",
        "file_name": file_name,
        "text": text, # Optional: any accompanying text
    }
    ```

## 4. Listing and Registering Tools

To make your tools available to the MCP, you must list them in the `list_tools` method.

```python
class GoogleGeminiApp(APIApplication):
    # ... (tool methods)

    def list_tools(self):
        return [
            self.generate_text,
            self.generate_image,
            self.generate_audio,
        ]
```

This method should return a list of the function objects you want to expose.

## 5. Local Testing

To facilitate rapid development and testing, include a runnable block in your `app.py`. This allows you to test your application's functionality directly without needing the full MCP environment.

```python
if __name__ == "__main__":
    import asyncio

    async def test_google_gemini():
        # NOTE: You may need to set up credentials locally for this to work
        # e.g., os.environ["GOOGLE_API_KEY"] = "..."
        app = GoogleGeminiApp()
        response = await app.generate_text(
            "Tell me a fun fact about the Roman Empire."
        )
        print(response)

    asyncio.run(test_google_gemini())
```
