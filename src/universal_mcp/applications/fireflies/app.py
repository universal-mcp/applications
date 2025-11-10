from collections.abc import Callable
from typing import Any
from gql import gql
from universal_mcp.applications.application import GraphQLApplication
from universal_mcp.integrations import Integration


class FirefliesApp(GraphQLApplication):
    """
    Application for interacting with the Fireflies.ai GraphQL API.
    """

    def __init__(self, integration: Integration | None = None, **kwargs: Any) -> None:
        super().__init__(name="fireflies", base_url="https://api.fireflies.ai/graphql", **kwargs)
        self.integration = integration

    async def get_team_conversation_analytics(self, start_time: str | None = None, end_time: str | None = None) -> dict[str, Any]:
        """
        Queries the Fireflies.ai API for team conversation analytics, specifically the average number of filler words. The data retrieval can optionally be filtered by a start and end time. Returns a dictionary containing the fetched analytics.

        Args:
            start_time: Optional start time for analytics (ISO 8601 format, e.g., "2024-01-01T00:00:00Z").
            end_time: Optional end time for analytics (ISO 8601 format, e.g., "2024-01-31T23:59:59Z").

        Returns:
            A dictionary containing team analytics data.
            Example: {"team": {"conversation": {"average_filler_words": 0.5}}}

        Raises:
            Exception: If the API request fails.

        Tags:
            analytics, team, fireflies, query
        """
        query_gql = gql(
            "\n        query Analytics($startTime: String, $endTime: String) {\n          analytics(start_time: $startTime, end_time: $endTime) {\n            team {\n              conversation {\n                average_filler_words\n              }\n            }\n          }\n        }\n        "
        )
        variables: dict[str, Any] = {}
        if start_time:
            variables["startTime"] = start_time
        if end_time:
            variables["endTime"] = end_time
        result = self.query(query_gql, variables=variables if variables else None)
        return result.get("analytics", {})

    async def get_transcript_ai_outputs(self, transcript_id: str) -> list[dict[str, Any]]:
        """
        Retrieves all AI-generated application outputs, such as summaries or analyses, associated with a specific transcript ID. It fetches the detailed prompt and response data for each AI app that has processed the transcript, providing a complete record of AI-generated content.

        Args:
            transcript_id: The ID of the transcript.

        Returns:
            A list of dictionaries, each representing an AI app output.
            Example: [{"transcript_id": "...", "user_id": "...", ...}]

        Raises:
            Exception: If the API request fails.

        Tags:
            ai, apps, transcript, fireflies, query
        """
        query_gql = gql(
            "\n        query GetAIAppsOutputs($transcriptId: String!) {\n          apps(transcript_id: $transcriptId) {\n            outputs {\n              transcript_id\n              user_id\n              app_id\n              created_at\n              title\n              prompt\n              response\n            }\n          }\n        }\n        "
        )
        variables = {"transcriptId": transcript_id}
        result = self.query(query_gql, variables=variables)
        return result.get("apps", {})

    async def get_user_details(self, user_id: str) -> dict[str, Any]:
        """
        Fetches details, such as name and integrations, for a single user identified by their unique ID. This function queries for a specific user, differentiating it from `list_users` which retrieves a list of all users in the workspace.

        Args:
            user_id: The ID of the user.

        Returns:
            A dictionary containing user details (e.g., name, integrations).
            Example: {"name": "John Doe", "integrations": [...]}

        Raises:
            Exception: If the API request fails.

        Tags:
            user, details, fireflies, query, important
        """
        query_gql = gql(
            "\n        query User($userId: String!) {\n          user(id: $userId) {\n            name\n            integrations\n          }\n        }\n        "
        )
        variables = {"userId": user_id}
        result = self.query(query_gql, variables=variables)
        return result.get("user", {})

    async def list_users(self) -> list[dict[str, Any]]:
        """
        Retrieves a list of all users in the workspace, returning each user's name and configured integrations. It provides a complete team roster, differing from `get_user_details`, which fetches information for a single user by their ID.

        Returns:
            A list of dictionaries, each representing a user with their name and integrations.
            Example: [{"name": "Justin Fly", "integrations": ["zoom", "slack"]}, ...]

        Raises:
            Exception: If the API request fails.

        Tags:
            user, list, users, fireflies, query
        """
        query_str = "\n        query ListAllUsers {\n          users {\n            name\n            integrations\n            # You might want to add other available user fields here if needed, e.g.:\n            # id\n            # email\n            # role\n            # is_admin\n          }\n        }\n        "
        result = self.query(query_str)
        return result.get("users", [])

    async def get_transcript_details(self, transcript_id: str) -> dict[str, Any]:
        """
        Queries the Fireflies API for a single transcript's details, such as title and ID, using its unique identifier. It fetches one specific entry, distinguishing it from `list_transcripts`, which retrieves a collection, and from `get_ai_apps_outputs` which gets AI data from a transcript.

        Args:
            transcript_id: The ID of the transcript.

        Returns:
            A dictionary containing transcript details (e.g., title, id).
            Example: {"title": "Meeting Notes", "id": "..."}

        Raises:
            Exception: If the API request fails.

        Tags:
            transcript, details, fireflies, query, important
        """
        query_gql = gql(
            "\n        query Transcript($transcriptId: String!) {\n          transcript(id: $transcriptId) {\n            id\n            title\n            host_email\n            organizer_email\n            user {\n              user_id\n              email\n              name\n              num_transcripts\n              recent_meeting\n              minutes_consumed\n              is_admin\n              integrations\n            }\n            speakers {\n              id\n              name\n            }\n            transcript_url\n            participants\n            meeting_attendees {\n              displayName\n              email\n              phoneNumber\n              name\n              location\n            }\n            fireflies_users\n            duration\n            dateString\n            date\n            audio_url\n            video_url\n            sentences {\n              index\n              speaker_name\n              speaker_id\n              text\n              raw_text\n              start_time\n              end_time\n              ai_filters {\n                task\n                pricing\n                metric\n                question\n                date_and_time\n                text_cleanup\n                sentiment\n              }\n            }\n            calendar_id\n            summary {\n              action_items\n              keywords\n              outline\n              overview\n              shorthand_bullet\n              gist\n              bullet_gist\n              short_summary\n              short_overview\n              meeting_type\n              topics_discussed\n              transcript_chapters\n            }\n            meeting_info {\n              fred_joined\n              silent_meeting\n              summary_status\n            }\n            cal_id\n            calendar_type\n            apps_preview {\n              outputs {\n                transcript_id\n                user_id\n                app_id\n                created_at\n                title\n                prompt\n                response\n              }\n            }\n            meeting_link\n            analytics {\n              sentiments {\n                negative_pct\n                neutral_pct\n                positive_pct\n              }\n              categories {\n                questions\n                date_times\n                metrics\n                tasks\n              }\n              speakers {\n                speaker_id\n                name\n                duration\n                word_count\n                longest_monologue\n                monologues_count\n                filler_words\n                questions\n                duration_pct\n                words_per_minute\n              }\n            }\n          }\n        }\n        "
        )
        variables = {"transcriptId": transcript_id}
        result = self.query(query_gql, variables=variables)
        return result.get("transcript", {})

    async def list_transcripts(self, user_id: str | None = None) -> list[dict[str, Any]]:
        """
        Fetches a list of meeting transcripts, returning the title and ID for each. The list can be filtered to return only transcripts for a specific user. This function complements `get_transcript_details`, which retrieves a single transcript by its unique ID.

        Args:
            user_id: Optional ID of the user to filter transcripts for.

        Returns:
            A list of dictionaries, each representing a transcript (e.g., title, id).
            Example: [{"title": "Meeting 1", "id": "..."}, {"title": "Meeting 2", "id": "..."}]

        Raises:
            Exception: If the API request fails.

        Tags:
            transcript, list, fireflies, query
        """
        query_gql = gql(
            "\n        query Transcripts($userId: String) {\n          transcripts(user_id: $userId) {\n            title\n            id\n          }\n        }\n        "
        )
        variables: dict[str, Any] = {}
        if user_id:
            variables["userId"] = user_id
        result = self.query(query_gql, variables=variables if variables else None)
        return result.get("transcripts", [])

    async def get_bite_details(self, bite_id: str) -> dict[str, Any]:
        """
        Retrieves detailed information for a specific bite (soundbite/clip) using its unique ID. It fetches data including the user ID, name, processing status, and summary. This provides a focused view of a single bite, distinguishing it from `list_bites` which fetches a collection of bites.

        Args:
            bite_id: The ID of the bite.

        Returns:
            A dictionary containing bite details (e.g., user_id, name, status, summary).
            Example: {"user_id": "...", "name": "Key Moment", "status": "processed", "summary": "..."}

        Raises:
            Exception: If the API request fails.

        Tags:
            bite, details, fireflies, query
        """
        query_gql = gql(
            "\n        query Bite($biteId: ID!) {\n          bite(id: $biteId) {\n            user_id\n            name\n            status\n            summary\n          }\n        }\n        "
        )
        variables = {"biteId": bite_id}
        result = self.query(query_gql, variables=variables)
        return result.get("bite", {})

    async def list_bites(self, mine: bool | None = None) -> list[dict[str, Any]]:
        """
        Retrieves a list of soundbites (clips) from the Fireflies API. An optional 'mine' parameter filters for soundbites belonging only to the authenticated user. Differentiates from 'get_bite_details' by fetching multiple items rather than a single one by ID.

        Args:
            mine: Optional boolean to filter for the authenticated user's bites (default true if not specified by API).

        Returns:
            A list of dictionaries, each representing a bite (e.g., user_id, name, end_time).
            Example: [{"user_id": "...", "name": "Clip 1", "end_time": "..."}]

        Raises:
            Exception: If the API request fails.

        Tags:
            bite, list, fireflies, query
        """
        query_gql = gql(
            "\n        query Bites($mine: Boolean) {\n          bites(mine: $mine) {\n            user_id\n            name\n            end_time\n          }\n        }\n        "
        )
        variables: dict[str, Any] = {}
        if mine is not None:
            variables["mine"] = mine
        result = self.query(query_gql, variables=variables if variables else None)
        return result.get("bites", [])

    async def add_to_live_meeting(self, meeting_link: str) -> dict[str, Any]:
        """
        Executes a GraphQL mutation to make the Fireflies.ai notetaker join a live meeting specified by its URL. This action initiates the bot's recording and transcription process for the ongoing session and returns a success confirmation.

        Args:
            meeting_link: The URL of the live meeting (e.g., Google Meet link).

        Returns:
            A dictionary indicating the success of the operation.
            Example: {"success": true}

        Raises:
            Exception: If the API request fails.

        Tags:
            meeting, live, fireflies, mutation, important
        """
        mutation_gql = gql(
            "\n        mutation AddToLiveMeeting($meetingLink: String!) {\n          addToLiveMeeting(meeting_link: $meetingLink) {\n            success\n          }\n        }\n        "
        )
        variables = {"meetingLink": meeting_link}
        result = self.mutate(mutation_gql, variables=variables)
        return result.get("addToLiveMeeting", {})

    async def create_soundbite_from_transcript(self, transcript_id: str, start_time: float, end_time: float) -> dict[str, Any]:
        """
        Creates a soundbite/clip from a specified segment of a transcript using its ID, start, and end times. This function executes a GraphQL mutation, returning details of the newly created bite, such as its ID and processing status.

        Args:
            transcript_id: The ID of the transcript.
            start_time: The start time of the bite in seconds (or relevant float unit).
            end_time: The end time of the bite in seconds (or relevant float unit).

        Returns:
            A dictionary containing details of the created bite (e.g., summary, status, id).
            Example: {"summary": "...", "status": "processing", "id": "..."}

        Raises:
            Exception: If the API request fails.

        Tags:
            bite, create, transcript, fireflies, mutation
        """
        mutation_gql = gql(
            "\n        mutation CreateBite($transcriptId: ID!, $startTime: Float!, $endTime: Float!) {\n          createBite(transcript_id: $transcriptId, start_time: $startTime, end_time: $endTime) {\n            summary\n            status\n            id\n          }\n        }\n        "
        )
        variables = {"transcriptId": transcript_id, "startTime": start_time, "endTime": end_time}
        result = self.mutate(mutation_gql, variables=variables)
        return result.get("createBite", {})

    async def delete_transcript(self, transcript_id: str) -> dict[str, Any]:
        """
        Permanently deletes a specific transcript from Fireflies.ai using its ID. This destructive operation executes a GraphQL mutation and returns a dictionary containing the details of the transcript (e.g., title, date) as it existed just before being removed, confirming the action.

        Args:
            transcript_id: The ID of the transcript to delete.

        Returns:
            A dictionary containing details of the deleted transcript.
            Example: {"title": "Old Meeting", "date": "...", "duration": ..., "organizer_email": "..."}

        Raises:
            Exception: If the API request fails.

        Tags:
            transcript, delete, fireflies, mutation, destructive
        """
        mutation_gql = gql(
            "\n        mutation DeleteTranscript($transcriptId: String!) {\n          deleteTranscript(id: $transcriptId) {\n            title\n            date\n            duration\n            organizer_email\n          }\n        }\n        "
        )
        variables = {"transcriptId": transcript_id}
        result = self.mutate(mutation_gql, variables=variables)
        return result.get("deleteTranscript", {})

    async def set_user_role(self, user_id: str, role: str) -> dict[str, Any]:
        """
        Assigns a new role (e.g., 'admin', 'member') to a user specified by their ID. This function executes a GraphQL mutation to modify user data and returns a dictionary with the user's updated name and admin status to confirm the change.

        Args:
            user_id: The ID of the user.
            role: The role to assign (e.g., "admin", "member").

        Returns:
            A dictionary containing the updated user details (e.g., name, is_admin).
            Example: {"name": "Jane Doe", "is_admin": true}

        Raises:
            Exception: If the API request fails.

        Tags:
            user, role, admin, fireflies, mutation
        """
        mutation_gql = gql(
            "\n        mutation SetUserRole($user_id: String!, $role: Role!) {\n          setUserRole(user_id: $user_id, role: $role) {\n            name\n            is_admin\n          }\n        }\n        "
        )
        variables = {"user_id": user_id, "role": role}
        result = self.mutate(mutation_gql, variables=variables)
        return result.get("setUserRole", {})

    async def transcribe_audio_from_url(
        self, url: str, title: str | None = None, attendees: list[dict[str, str]] | None = None
    ) -> dict[str, Any]:
        """
        Submits an audio file from a URL to the Fireflies.ai API for transcription. It can optionally associate a title and a list of attendees with the audio, returning the upload status and details upon completion.

        Args:
            url: The URL of the audio file.
            title: Optional title for the uploaded audio.
            attendees: Optional list of attendees. Each attendee is a dict
                       with "displayName", "email", "phoneNumber".

        Returns:
            A dictionary indicating the success and details of the upload.
            Example: {"success": true, "title": "Uploaded Audio", "message": "..."}

        Raises:
            Exception: If the API request fails.

        Tags:
            audio, upload, transcript, fireflies, mutation
        """
        mutation_gql = gql(
            "\n        mutation UploadAudio($input: AudioUploadInput!) {\n          uploadAudio(input: $input) {\n            success\n            title\n            message\n          }\n        }\n        "
        )
        input_data: dict[str, Any] = {"url": url}
        if title:
            input_data["title"] = title
        if attendees:
            input_data["attendees"] = attendees
        variables = {"input": input_data}
        result = self.mutate(mutation_gql, variables=variables)
        return result.get("uploadAudio", {})

    async def update_transcript_title(self, transcript_id: str, new_title: str) -> dict[str, Any]:
        """
        Updates the title of a specific transcript, identified by its ID, to a new value. This function executes a GraphQL mutation and returns a dictionary containing the newly assigned title upon successful completion of the request.

        Args:
            transcript_id: The ID of the transcript to update.
            new_title: The new title for the meeting.

        Returns:
            A dictionary containing the updated title.
            Example: {"title": "New Meeting Title"}

        Raises:
            Exception: If the API request fails.

        Tags:
            transcript, meeting, title, update, fireflies, mutation
        """
        mutation_gql = gql(
            "\n        mutation UpdateMeetingTitle($input: UpdateMeetingTitleInput!) {\n          updateMeetingTitle(input: $input) {\n            title\n          }\n        }\n        "
        )
        variables = {"input": {"id": transcript_id, "title": new_title}}
        result = self.mutate(mutation_gql, variables=variables)
        return result.get("updateMeetingTitle", {})

    def list_tools(self) -> list[Callable[..., Any]]:
        """
        Lists all available tools (public methods) for the FirefliesApp.

        Returns:
            A list of callable tool methods.
        """
        return [
            self.get_team_conversation_analytics,
            self.get_transcript_ai_outputs,
            self.get_user_details,
            self.list_users,
            self.get_transcript_details,
            self.list_transcripts,
            self.get_bite_details,
            self.list_bites,
            self.add_to_live_meeting,
            self.create_soundbite_from_transcript,
            self.delete_transcript,
            self.set_user_role,
            self.transcribe_audio_from_url,
            self.update_transcript_title,
        ]
