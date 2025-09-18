# FirefliesApp MCP Server

An MCP Server for the FirefliesApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the FirefliesApp API.


| Tool | Description |
|------|-------------|
| `get_team_conversation_analytics` | Queries the Fireflies.ai API for team conversation analytics, specifically the average number of filler words. The data retrieval can optionally be filtered by a start and end time. Returns a dictionary containing the fetched analytics. |
| `get_transcript_ai_outputs` | Retrieves all AI-generated application outputs, such as summaries or analyses, associated with a specific transcript ID. It fetches the detailed prompt and response data for each AI app that has processed the transcript, providing a complete record of AI-generated content. |
| `get_user_details` | Fetches details, such as name and integrations, for a single user identified by their unique ID. This function queries for a specific user, differentiating it from `list_users` which retrieves a list of all users in the workspace. |
| `list_users` | Retrieves a list of all users in the workspace, returning each user's name and configured integrations. It provides a complete team roster, differing from `get_user_details`, which fetches information for a single user by their ID. |
| `get_transcript_details` | Queries the Fireflies API for a single transcript's details, such as title and ID, using its unique identifier. It fetches one specific entry, distinguishing it from `list_transcripts`, which retrieves a collection, and from `get_ai_apps_outputs` which gets AI data from a transcript. |
| `list_transcripts` | Fetches a list of meeting transcripts, returning the title and ID for each. The list can be filtered to return only transcripts for a specific user. This function complements `get_transcript_details`, which retrieves a single transcript by its unique ID. |
| `get_bite_details` | Retrieves detailed information for a specific bite (soundbite/clip) using its unique ID. It fetches data including the user ID, name, processing status, and summary. This provides a focused view of a single bite, distinguishing it from `list_bites` which fetches a collection of bites. |
| `list_bites` | Retrieves a list of soundbites (clips) from the Fireflies API. An optional 'mine' parameter filters for soundbites belonging only to the authenticated user. Differentiates from 'get_bite_details' by fetching multiple items rather than a single one by ID. |
| `add_to_live_meeting` | Executes a GraphQL mutation to make the Fireflies.ai notetaker join a live meeting specified by its URL. This action initiates the bot's recording and transcription process for the ongoing session and returns a success confirmation. |
| `create_soundbite_from_transcript` | Creates a soundbite/clip from a specified segment of a transcript using its ID, start, and end times. This function executes a GraphQL mutation, returning details of the newly created bite, such as its ID and processing status. |
| `delete_transcript` | Permanently deletes a specific transcript from Fireflies.ai using its ID. This destructive operation executes a GraphQL mutation and returns a dictionary containing the details of the transcript (e.g., title, date) as it existed just before being removed, confirming the action. |
| `set_user_role` | Assigns a new role (e.g., 'admin', 'member') to a user specified by their ID. This function executes a GraphQL mutation to modify user data and returns a dictionary with the user's updated name and admin status to confirm the change. |
| `transcribe_audio_from_url` | Submits an audio file from a URL to the Fireflies.ai API for transcription. It can optionally associate a title and a list of attendees with the audio, returning the upload status and details upon completion. |
| `update_transcript_title` | Updates the title of a specific transcript, identified by its ID, to a new value. This function executes a GraphQL mutation and returns a dictionary containing the newly assigned title upon successful completion of the request. |
