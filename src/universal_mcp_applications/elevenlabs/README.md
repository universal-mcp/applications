# ElevenlabsApp MCP Server

An MCP Server for the ElevenlabsApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the ElevenlabsApp API.


| Tool | Description |
|------|-------------|
| `get_generated_items` | Retrieves historical data based on specified parameters, including page size and voice ID, using the "GET" method at the "/v1/history" endpoint. |
| `get_history_item_by_id` | Retrieves a specific history item by its identifier using the API defined at "/v1/history/{history_item_id}" with the GET method. |
| `delete_history_item` | Deletes a specific history item identified by its ID using the DELETE method. |
| `get_audio_from_history_item` | Retrieves audio data for a specific history item identified by `{history_item_id}` using the `GET` method at the `/v1/history/{history_item_id}/audio` endpoint. |
| `download_history_items` | Initiates a historical data download process and returns a success status upon completion. |
| `delete_sample` | Deletes a specific voice sample identified by the `sample_id` from a voice with the given `voice_id` using the DELETE method. |
| `get_audio_from_sample` | Retrieves the audio file for a specific sample associated with a given voice using the specified voice_id and sample_id. |
| `convert` | Converts text into speech using a specified voice, allowing for optimization of streaming latency and selection of output format. |
| `text_to_speech_with_timestamps` | Generates speech from text with precise character or word-level timing information using the specified voice, supporting audio-text synchronization through timestamps. |
| `convert_as_stream` | Converts text to speech stream using the specified voice ID with configurable latency and output format. |
| `stream_text_with_timestamps` | Converts text to speech using the specified voice ID, streaming the audio output with timestamps. |
| `voice_generation_parameters` | Retrieves the parameters required for generating voice using the specified API endpoint. |
| `generate_arandom_voice` | Generates an audio file by converting text into speech using a specified voice, allowing for customizable voice selection and text input. |
| `create_voice_model` | Generates a custom voice using the provided parameters via the "/v1/voice-generation/create-voice" endpoint by sending a POST request, allowing users to create unique voice models. |
| `create_previews` | Generates a voice preview from a given text prompt using the ElevenLabs API. |
| `create_voice_from_preview` | Creates a new voice entry in the voice library using a generated preview ID and returns voice details. |
| `get_user_subscription_info` | Retrieves the user's subscription details from the API. |
| `get_user_info` | Retrieves user information from the API. |
| `get_voices` | Retrieves a list of voices using the "GET" method at the "/v1/voices" API endpoint. |
| `get_default_voice_settings` | Retrieves the default voice settings using the "GET" method at the "/v1/voices/settings/default" endpoint. |
| `get_voice_settings` | Retrieves voice settings for a specific voice identified by `{voice_id}` using the "GET" method, returning the current configuration for that voice. |
| `get_voice` | Retrieves the details of a specific voice by its ID using the "GET" method at the "/v1/voices/{voice_id}" endpoint. |
| `delete_voice` | Deletes a voice with the specified ID using the DELETE method at the "/v1/voices/{voice_id}" endpoint. |
| `edit_voice_settings` | Updates voice settings for a specified voice ID and returns a success status. |
| `add_voice` | Adds a new voice entry to the voices collection using the provided data. |
| `edit_voice` | Updates the specified voice by ID using a POST request and returns a success status upon completion. |
| `add_sharing_voice` | Adds a voice associated with a public user ID and voice ID using the specified API endpoint. |
| `get_shared_voices` | Retrieves a list of shared voices filtered by parameters like gender and language, with pagination support via page_size. |
| `get_similar_library_voices` | Generates a list of similar voices using the POST method at the "/v1/similar-voices" endpoint. |
| `get_aprofile_page` | Retrieves a unified customer profile by handle and returns the associated attributes, identifiers, and traits. |
| `get_projects` | Retrieves a list of projects using the API defined at the "/v1/projects" endpoint via the GET method. |
| `add_project` | Creates a new project and returns a status message. |
| `get_project_by_id` | Retrieves information for a specific project identified by `{project_id}` using the API endpoint at "/v1/projects/{project_id}" via the GET method. |
| `edit_basic_project_info` | Creates a new project resource by sending data to the specified project identifier using the POST method at the "/v1/projects/{project_id}" endpoint. |
| `delete_project` | Deletes the specified project and returns a success status upon completion. |
| `convert_project` | Converts a specified project identified by project_id and returns the conversion result. |
| `get_project_snapshots` | Retrieves a list of snapshots associated with a specified project. |
| `streams_archive_with_project_audio` | Archives a project snapshot using the specified project ID and snapshot ID and returns a success status. |
| `add_chapter_to_aproject` | Adds a new chapter to a specified project using the provided project identifier and returns a success status upon completion. |
| `update_project_pronunciations` | Updates pronunciation dictionaries for a specified project using the POST method, returning a successful status message upon completion. |
| `get_chapters` | Retrieves a chapter for a specified project by ID using the GET method. |
| `get_chapter_by_id` | Retrieves a specific chapter within a project identified by project_id and chapter_id. |
| `delete_chapter` | Deletes a specific chapter within a project using the "DELETE" method. |
| `convert_chapter` | Converts a chapter in a project using the POST method and returns a response upon successful conversion. |
| `get_chapter_snapshots` | Retrieves a snapshot for a specific chapter within a project using the provided project and chapter IDs. |
| `stream_chapter_audio` | Streams data from a specific chapter snapshot in a project using the API and returns a response indicating success. |
| `dub_avideo_or_an_audio_file` | Initiates a dubbing process and returns a status message using the API defined at the "/v1/dubbing" endpoint via the POST method. |
| `get_dubbing_project_metadata` | Retrieves the details of a specific dubbing job using the provided dubbing ID. |
| `delete_dubbing_project` | Deletes a dubbing project with the specified ID and returns a success status upon completion. |
| `get_transcript_for_dub` | Retrieves the transcript for a specific dubbing task in the requested language using the "GET" method. |
| `get_models` | Retrieves a list of models using the GET method at the "/v1/models" endpoint. |
| `post_audio_native` | Processes audio data using the audio-native API and returns a response. |
| `get_characters_usage_metrics` | Retrieves character statistics within a specified time frame using the start and end Unix timestamps provided in the query parameters. |
| `add_apronunciation_dictionary` | Creates a pronunciation dictionary from a lexicon file and returns its ID and metadata. |
| `add_rules_to_dictionary` | Adds pronunciation rules to a specific pronunciation dictionary identified by its ID using the POST method. |
| `remove_pronunciation_rules` | Removes specified pronunciation rules from a pronunciation dictionary using a POST request. |
| `get_dictionary_version_file` | Retrieves and downloads a specific version of a pronunciation dictionary file using its dictionary ID and version ID. |
| `get_pronunciation_dictionary` | Retrieves a specific pronunciation dictionary by its ID using the "GET" method from the "/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}" endpoint. |
| `get_pronunciation_dictionaries` | Retrieves a list of pronunciation dictionaries using the GET method at the "/v1/pronunciation-dictionaries" endpoint, allowing users to specify the number of items per page via the "page_size" query parameter. |
| `invite_user` | Invites a user to join a workspace by sending an invitation, allowing them to access the specified workspace upon acceptance. |
| `delete_existing_invitation` | Deletes a workspace invite and returns a success response upon completion. |
| `update_member` | Adds members to a workspace and returns the updated member list upon success. |
| `get_signed_url` | Generates a signed URL for initiating a conversation with a specific conversational AI agent, identified by the provided `agent_id`, using the ElevenLabs API. |
| `create_agent` | Creates a conversational AI agent with specified configuration settings and returns the agent details. |
| `get_agent` | Retrieves information about a specific conversational AI agent by its unique identifier using the GET method at the "/v1/convai/agents/{agent_id}" API endpoint. |
| `delete_agent` | Deletes a specified Conversational AI agent using the DELETE method. |
| `patches_an_agent_settings` | Updates an existing conversational AI agent's settings using the specified agent ID, allowing changes to properties such as the agent's name and tool configurations. |
| `get_agent_widget_config` | Retrieves and configures the Convai widget for the specified agent, but the provided details do not specify the exact functionality of this specific endpoint, suggesting it may relate to integrating or customizing Convai's character interaction capabilities. |
| `get_shareable_agent_link` | Retrieves and establishes a link for a Convai agent using the specified agent ID, facilitating integration or connectivity operations. |
| `post_agent_avatar` | Creates and configures a Convai avatar for a specific agent using the POST method, though the exact details of this endpoint are not provided in the available documentation. |
| `get_agent_knowledge_base` | Retrieves specific documentation for a knowledge base associated with an agent in Convai. |
| `add_agent_secret` | Adds a secret to a specified conversational AI agent through the API and returns a status confirmation. |
| `add_to_agent_sknowledge_base` | Adds new content to an agent's knowledge base by uploading a file or resource, which can be used to enhance the agent's conversational capabilities. |
| `get_agents_page` | Retrieves a list of conversational AI agents available in the Convai system. |
| `get_conversations` | Retrieves conversation history for a specified agent ID. |
| `get_conversation_details` | Retrieves and formats the details of a specific conversation based on the provided conversation ID. |
| `get_conversation_audio` | Retrieves the audio from a specific conversation using the ElevenLabs Conversational AI API. |
