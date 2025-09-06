import logging
from typing import Any, Literal  # Added Literal for type hinting

import httpx
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


class GoogleGeminiApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="google-gemini", integration=integration, **kwargs)
        self.base_url = "https://generativelanguage.googleapis.com"

    def _get_headers(self) -> dict[str, str]:
        """
        Override the base method to return empty headers.
        The Gemini API key is passed as a query parameter ('key'),
        not in an Authorization header for these endpoints.
        """
        logger.debug(
            f"Overriding _get_headers for {self.name}. Returning empty dict to prevent default auth header."
        )
        return {}

    def _add_api_key_param(self, params: dict[str, Any] | None) -> dict[str, Any]:
        """Helper to add the API key as a 'key' query parameter."""
        actual_params = params.copy() if params else {}
        if "key" not in actual_params and self.integration:
            try:
                credentials = self.integration.get_credentials()
                if not isinstance(credentials, dict):
                    logger.warning(
                        f"Integration credentials for {self.name} are not a dictionary. Cannot retrieve API key."
                    )
                    return actual_params  # or raise error

                api_key = (
                    credentials.get("api_key")
                    or credentials.get("API_KEY")
                    or credentials.get("apiKey")
                )
                if api_key:
                    actual_params["key"] = api_key
                    logger.debug("Added API key as query parameter.")
                else:
                    logger.warning(
                        f"API key not found in integration credentials for {self.name} using keys: api_key, API_KEY, apiKey."
                    )
            except Exception as e:
                logger.error(
                    f"Error retrieving API key from integration for {self.name}: {e}"
                )
        elif not self.integration:
            logger.warning(
                f"No integration provided for {self.name}. API key cannot be added automatically."
            )
        return actual_params

    def _get(self, url: str, params: dict[str, Any] | None = None) -> httpx.Response:
        """
        Make a GET request, ensuring the API key is added as a query parameter.
        """
        actual_params = self._add_api_key_param(params)
        logger.debug(f"Making GET request to {url} with params: {actual_params}")
        return super()._get(url, params=actual_params)

    def _post(
        self, url: str, data: dict[str, Any], params: dict[str, Any] | None = None
    ) -> httpx.Response:
        """
        Make a POST request, ensuring the API key is added as a query parameter
        and content_type is explicitly set to application/json.
        """
        actual_params = self._add_api_key_param(params)
        logger.debug(
            f"Making POST request to {url} with params: {actual_params} and data: {data}"
        )
        # Explicitly set content_type for clarity and robustness
        return super()._post(
            url, data=data, params=actual_params, content_type="application/json"
        )

    def _delete(self, url: str, params: dict[str, Any] | None = None) -> httpx.Response:
        """
        Make a DELETE request, ensuring the API key is added as a query parameter.
        """
        actual_params = self._add_api_key_param(params)
        logger.debug(f"Making DELETE request to {url} with params: {actual_params}")
        return super()._delete(url, params=actual_params)

    def fetch_model(self) -> dict[str, Any]:
        """
        Retrieves the configuration details of current model via a GET request.

        Returns:
            dict[str, Any]: model

        Tags:
            Models, important
        """
        url = f"{self.base_url}/v1beta/models/gemini-2.0-flash"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_models(self, pageSize=None, pageToken=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of available models, supporting page size and token parameters for result navigation.

        Args:
            pageSize (string): The `pageSize` parameter specifies the maximum number of items to include in each page of the response for the GET operation at the `/v1beta/models` path. Example: '5'.
            pageToken (string): Used in GET requests to specify the page token for fetching the next page of results. Example: 'Chxtb2RlbHMvZ2VtaW5pLTEuNS1wcm8tbGF0ZXN0'.

        Returns:
            dict[str, Any]: models

        Tags:
            Models, important
        """
        url = f"{self.base_url}/v1beta/models"
        query_params = {
            k: v
            for k, v in [("pageSize", pageSize), ("pageToken", pageToken)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def text_only_input(self, query: str) -> dict[str, Any]:
        """
        Generates content using the Gemini 1.5 Flash model via POST request,
        taking a simple string query.

        Args:
            query (str): The text prompt for the model.
                         Example: "Write a story about a magic backpack."

        Returns:
            Dict[str, Any]: The JSON response from the API.

        Raises:
            ValueError: If the query is empty or not a string.
            httpx.HTTPStatusError: If the API returns an error status.

        Tags:
            important
        """
        if not query or not isinstance(query, str):
            raise ValueError("Query must be a non-empty string.")

        contents_payload = [{"parts": [{"text": query}]}]

        request_body = {
            "contents": contents_payload,
        }
        model_name = "gemini-2.0-flash"

        url = f"{self.base_url}/v1beta/models/{model_name}:generateContent"

        query_params = {}

        logger.info(
            f'Calling Gemini API for model: {model_name} with query: "{query[:70]}{"..." if len(query) > 70 else ""}"'
        )

        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        data = response.json()
        try:
            extracted_text = data["candidates"][0]["content"]["parts"][0]["text"]
            return extracted_text
        except (KeyError, IndexError, TypeError):
            return data

    def generate_atext_stream(self, query: str) -> dict[str, Any]:
        """
        Generates a streaming response from the Gemini 1.5 Flash model for multimodal input content.

        Args:
            query (str): The text prompt for the model.

        Returns:
            Any: generate a text stream

        Tags:
            Text Generation
        """
        if not query or not isinstance(query, str):
            raise ValueError("Query must be a non-empty string.")

        contents_payload = [{"parts": [{"text": query}]}]

        request_body = {
            "contents": contents_payload,
        }
        model_name = "gemini-2.0-flash"
        url = f"{self.base_url}/v1beta/models/{model_name}:streamGenerateContent"
        query_params = {}

        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        data = response.json()
        try:
            extracted_text = data["candidates"][0]["content"]["parts"][0]["text"]
            return extracted_text
        except (KeyError, IndexError, TypeError):
            return data

    def resumable_upload_request(
        self, file_metadata: dict[str, Any] | None = None
    ) -> Any:
        """
        Initiates a file upload by sending file metadata.
        This typically returns an upload URL or session URI for subsequent data upload.

        Args:
            file_metadata (Optional[Dict[str, Any]]): Metadata for the file to be uploaded.
                Example: {"display_name": "my_audio_file.mp3"}
                If None, the 'file' field will be omitted from the request if the API supports that,
                or it might result in an error if the 'file' field is mandatory.

        Returns:
            Any: The JSON response from the API, typically containing upload instructions
                 or a file resource representation.

        Tags:
            Document Processing
        """
        request_body: dict[str, Any] = {}
        if file_metadata is not None:
            request_body["file"] = file_metadata

        if not request_body and file_metadata is None:
            pass
            # request_body will be {} if file_metadata is None

        url = f"{self.base_url}/upload/v1beta/files"

        query_params = {}

        response = self._post(
            url, data=request_body if request_body else None, params=query_params
        )
        response_json = None
        response_json = response.json()

        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
        return response_json if response_json else {}

    def prompt_document(self, contents=None) -> dict[str, Any]:
        """
        Generates content using the Gemini model, accepting input prompts and returning a streamed response across various media types, such as text, images, and audio.

        Args:
            contents (array): contents
                Example:
                ```json
                {
                  "contents": [
                    {
                      "parts": [
                        {
                          "text": "Summarize the uploaded document."
                        },
                        {
                          "file_data": {
                            "file_uri": "{{FILE_URI}}",
                            "mime_type": "application/pdf"
                          }
                        }
                      ]
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: prompt document

        Tags:
            Document Processing
        """
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/gemini-1.5-pro-latest:generateContent"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_document(
        self, contents: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Generates content using the Gemini model with document context.

        Args:
            contents (Optional[List[Dict[str, Any]]]): List of content parts, including text and file data.
                Example:
                ```json
                [
                  {
                    "parts": [
                      {"text": "Summarize the uploaded document."},
                      {"file_data": {"file_uri": "files/your_file_id", "mime_type": "application/pdf"}}
                    ]
                  }
                ]
                ```

        Returns:
            dict[str, Any]: The model's response.
        """
        request_body = {"contents": contents}
        request_body = {k: v for k, v in request_body.items() if v is not None}
        if not request_body.get("contents"):  # API might require contents
            raise ValueError(
                "Missing required parameter 'contents' for prompt_document."
            )

        url = f"{self.base_url}/v1beta/models/gemini-:generateContent"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        return response.json()

    def text_tokens(self, query: str) -> dict[str, Any]:
        """
        Calculates the number of tokens and billable characters for input content using a gemini-2.0-flash.

        Args:
            query (str): The text prompt for the model.

        Returns:
            dict[str, Any]: text tokens / chat tokens / media tokens

        Tags:
            Count Tokens, important
        """
        if not query or not isinstance(query, str):
            raise ValueError("Query must be a non-empty string.")

        contents = [{"parts": [{"text": query}]}]
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        model_name = "gemini-2.0-flash"
        url = f"{self.base_url}/v1beta/models/{model_name}:countTokens"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_tuned_models(self, page_size=None) -> dict[str, Any]:
        """
        Retrieves a list of tuned models at the specified page size using the GET method.

        Args:
            page_size (string): Specifies the maximum number of items to return in a single response page. Example: '10'.

        Returns:
            dict[str, Any]: fetch models Copy

        Tags:
            Fine Tunning
        """
        url = f"{self.base_url}/v1beta/tunedModels"
        query_params = {k: v for k, v in [("page_size", page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atuned_model(
        self, base_model=None, display_name=None, tuning_task=None
    ) -> dict[str, Any]:
        """
        Creates a tuned model using the "POST" method at the "/v1beta/tunedModels" endpoint and returns a response upon successful creation.

        Args:
            base_model (string): base_model Example: 'models/gemini-1.5-flash-001-tuning'.
            display_name (string): display_name Example: 'number generator model'.
            tuning_task (object): tuning_task
                Example:
                ```json
                {
                  "base_model": "models/gemini-1.5-flash-001-tuning",
                  "display_name": "number generator model",
                  "tuning_task": {
                    "hyperparameters": {
                      "batch_size": 2,
                      "epoch_count": 5,
                      "learning_rate": 0.001
                    },
                    "training_data": {
                      "examples": {
                        "examples": [
                          {
                            "output": "2",
                            "text_input": "1"
                          },
                          {
                            "output": "4",
                            "text_input": "3"
                          },
                          {
                            "output": "-2",
                            "text_input": "-3"
                          },
                          {
                            "output": "twenty three",
                            "text_input": "twenty two"
                          },
                          {
                            "output": "two hundred one",
                            "text_input": "two hundred"
                          },
                          {
                            "output": "one hundred",
                            "text_input": "ninety nine"
                          },
                          {
                            "output": "9",
                            "text_input": "8"
                          },
                          {
                            "output": "-97",
                            "text_input": "-98"
                          },
                          {
                            "output": "1,001",
                            "text_input": "1,000"
                          },
                          {
                            "output": "10,100,001",
                            "text_input": "10,100,000"
                          },
                          {
                            "output": "fourteen",
                            "text_input": "thirteen"
                          },
                          {
                            "output": "eighty one",
                            "text_input": "eighty"
                          },
                          {
                            "output": "two",
                            "text_input": "one"
                          },
                          {
                            "output": "four",
                            "text_input": "three"
                          },
                          {
                            "output": "eight",
                            "text_input": "seven"
                          }
                        ]
                      }
                    }
                  }
                }
                ```

        Returns:
            dict[str, Any]: create a tuned model

        Tags:
            Fine Tunning
        """
        request_body = {
            "base_model": base_model,
            "display_name": display_name,
            "tuning_task": tuning_task,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/tunedModels"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_the_tuned_model(self, tunedModel, contents=None) -> dict[str, Any]:
        """
        Generates content using a specified tuned model defined at path "/v1beta/{tunedModel}:generateContent" by sending a POST request.

        Args:
            tunedModel (string): tunedModel
            contents (array): contents
                Example:
                ```json
                {
                  "contents": [
                    {
                      "parts": [
                        {
                          "text": "LXIII"
                        }
                      ]
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: prompt the tuned model

        Tags:
            Fine Tunning
        """
        if tunedModel is None:
            raise ValueError("Missing required parameter 'tunedModel'")
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/{tunedModel}:generateContent"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tuned_model(self, tunedModel) -> dict[str, Any]:
        """
        Deletes a specified tuned model and returns a success status upon removal.

        Args:
            tunedModel (string): tunedModel

        Returns:
            dict[str, Any]: delete tuned model

        Tags:
            Fine Tunning
        """
        if tunedModel is None:
            raise ValueError("Missing required parameter 'tunedModel'")
        url = f"{self.base_url}/v1beta/{tunedModel}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_embeddings(
        self,
        query: str,
        model_name: Literal[
            "gemini-embedding-exp-03-07", "text-embedding-004", "embedding-001"
        ] = "gemini-embedding-exp-03-07",
    ) -> dict[str, Any]:
        """
        Generates a text embedding vector from input text using the specified Gemini Embedding model, allowing for semantic analysis and comparison of textual content.

        Args:
            query (str): The text to generate an embedding.
            model_name (string): The name of the embedding model to use. Default is "gemini-embedding-exp-03-07".

        Returns:
            dict[str, Any]: generate embeddings

        Tags:
            Embeddings
        """
        if not query or not isinstance(query, str):
            raise ValueError("Query must be a non-empty string.")

        request_body = {
            "model": f"models/{model_name}",  # Fully qualified model name for the body
            "content": {  # 'content' is a dictionary (JSON object)
                "parts": [{"text": query}]  # 'parts' is a list of dictionaries
            },
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/{model_name}:embedContent"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_embeddings(
        self,
        queries: list[str],
        model_name: Literal[
            "gemini-embedding-exp-03-07", "text-embedding-004", "embedding-001"
        ] = "gemini-embedding-exp-03-07",
    ) -> dict[str, Any]:
        """
        Generates batch embeddings for a list of text inputs using the "gemini-embedding-exp-03-07" model via a POST request to the "/v1beta/models/text-embedding-004:batchEmbedContents" endpoint.

        Args:
            queries (List[str]): A list of texts to generate embeddings for.
            model_name (string): The name of the embedding model to use. Default is "gemini-embedding-exp-03-07".

        Returns:
            dict[str, Any]: batch embeddings

        Tags:
            Embeddings
        """
        if not queries:
            raise ValueError("Queries list cannot be empty.")
        if not all(isinstance(q, str) and q for q in queries):
            raise ValueError("All items in the queries list must be non-empty strings.")

        individual_requests = []
        for query_text in queries:
            individual_requests.append(
                {
                    "model": f"models/{model_name}",  # Model specified for each request
                    "content": {"parts": [{"text": query_text}]},
                }
            )
        request_body = {"requests": individual_requests}

        url = f"{self.base_url}/v1beta/models/{model_name}:batchEmbedContents"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def discovery_document(self, version=None) -> dict[str, Any]:
        """
        Retrieves discovery metadata for REST APIs, including available endpoints and parameters, based on the specified version.

        Args:
            version (string): Specifies the API version to use for the request, allowing clients to target a specific release without modifying the URI structure. Example: 'v1beta'.

        Returns:
            dict[str, Any]: Get Discovery Document
        """
        url = f"{self.base_url}/$discovery/rest"
        query_params = {k: v for k, v in [("version", version)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.fetch_model,
            self.fetch_models,
            self.text_only_input,
            self.generate_atext_stream,
            self.resumable_upload_request,
            self.prompt_document,
            self.text_tokens,
            self.fetch_tuned_models,
            self.create_atuned_model,
            self.prompt_the_tuned_model,
            self.delete_tuned_model,
            self.generate_embeddings,
            self.batch_embeddings,
            self.discovery_document,
        ]
