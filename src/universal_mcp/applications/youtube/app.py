import os
from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig


class YoutubeApp(APIApplication):
    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        """
        Initializes an instance of a YouTube application integration.

        Args:
            integration: An optional Integration object to be used with the YouTube application integration.
            kwargs: Additional keyword arguments to be passed to the parent class initializer.

        Returns:
            None
        """
        super().__init__(name="youtube", integration=integration, **kwargs)
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def list_job_reports(
        self,
        jobId,
        createdAfter=None,
        onBehalfOfContentOwner=None,
        pageSize=None,
        pageToken=None,
        startTimeAtOrAfter=None,
        startTimeBefore=None,
    ) -> Any:
        """
        Retrieves a paginated list of all reports for a specific job ID, with options for filtering by date. Unlike `get_jobs_job_reports_report`, which fetches a single report by its ID, this function returns a collection of reports associated with a job.

        Args:
            jobId: The unique identifier for the job whose reports are to be retrieved.
            createdAfter: Optional; filter to include only reports created after this date (ISO 8601 format).
            onBehalfOfContentOwner: Optional; for content owners wanting to access reports on behalf of another user.
            pageSize: Optional; the maximum number of report entries to return per page.
            pageToken: Optional; a token identifying the page of results to return.
            startTimeAtOrAfter: Optional; filter to include only reports starting at or after this date-time (ISO 8601 format).
            startTimeBefore: Optional; filter to include only reports with a start time before this date-time (ISO 8601 format).

        Returns:
            A JSON object containing the job reports matching the provided criteria.

        Raises:
            ValueError: Raised if the required 'jobId' parameter is missing.

        Tags:
            retrieve, report, job-management, batch
        """
        if jobId is None:
            raise ValueError("Missing required parameter 'jobId'")
        url = f"{self.base_url}/v1/jobs/{jobId}/reports"
        query_params = {
            k: v
            for k, v in [
                ("createdAfter", createdAfter),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("startTimeAtOrAfter", startTimeAtOrAfter),
                ("startTimeBefore", startTimeBefore),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_job_report(self, jobId, reportId, onBehalfOfContentOwner=None) -> Any:
        """
        Fetches a single, specific report identified by its `reportId` from within a given `jobId`. This retrieves an individual record, distinguishing it from `get_jobs_job_reports`, which returns a list of reports for a job. The request can be made on behalf of a content owner.

        Args:
            jobId: The unique identifier for the job containing the report (required).
            reportId: The unique identifier for the report to fetch (required).
            onBehalfOfContentOwner: Optional; specifies the content owner for whom the request is made.

        Returns:
            A JSON object containing the fetched report details.

        Raises:
            ValueError: Raised if 'jobId' or 'reportId' is not provided.
            requests.HTTPError: Raised if the API request fails (e.g., invalid permissions or resource not found).

        Tags:
            retrieve, report, job, api, json
        """
        if jobId is None:
            raise ValueError("Missing required parameter 'jobId'")
        if reportId is None:
            raise ValueError("Missing required parameter 'reportId'")
        url = f"{self.base_url}/v1/jobs/{jobId}/reports/{reportId}"
        query_params = {
            k: v
            for k, v in [("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_job(self, jobId, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes a specific job resource using its unique `jobId`, optionally on behalf of a content owner. This action permanently removes the job itself, differentiating it from functions that only retrieve or manage job reports.

        Args:
            jobId: The unique identifier of the job to delete. Required.
            onBehalfOfContentOwner: Optional. Content owner ID for delegated authorization.

        Returns:
            JSON response from the API as a Python dictionary.

        Raises:
            ValueError: Raised when jobId is None.
            requests.exceptions.HTTPError: Raised for failed HTTP requests (e.g., invalid job ID, permission errors).

        Tags:
            delete, jobs, async_job, management
        """
        if jobId is None:
            raise ValueError("Missing required parameter 'jobId'")
        url = f"{self.base_url}/v1/jobs/{jobId}"
        query_params = {
            k: v
            for k, v in [("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_jobs(
        self,
        includeSystemManaged=None,
        onBehalfOfContentOwner=None,
        pageSize=None,
        pageToken=None,
    ) -> Any:
        """
        Retrieves a paginated list of asynchronous jobs from the YouTube Reporting API. Supports filtering by content owner and including system-managed jobs. This function lists multiple jobs, distinct from `get_jobs_job_reports` which retrieves reports for a single job.

        Args:
            includeSystemManaged: Optional boolean indicating whether to include system-managed jobs.
            onBehalfOfContentOwner: Optional string representing the content owner on behalf of which the request is made.
            pageSize: Optional integer specifying the number of jobs per page.
            pageToken: Optional string for paginated results page token.

        Returns:
            JSON-decoded response containing the list of jobs and related metadata.

        Raises:
            HTTPError: Raised if the server returns an unsuccessful status code.

        Tags:
            list, scrape, management
        """
        url = f"{self.base_url}/v1/jobs"
        query_params = {
            k: v
            for k, v in [
                ("includeSystemManaged", includeSystemManaged),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def download_report_media(self, resourceName) -> Any:
        """
        Downloads the content of a bulk data report from the YouTube Reporting API by its unique `resourceName`. This function retrieves the actual media file generated by a reporting job, distinct from functions that only fetch report metadata.

        Args:
            resourceName: The name of the media resource to retrieve. Required and cannot be None.

        Returns:
            JSON-formatted data representing the media resource.

        Raises:
            ValueError: If 'resourceName' is None.
            requests.exceptions.HTTPError: If the HTTP request fails, such as a 404 for a non-existent resource.

        Tags:
            retrieve, media, json, http, get
        """
        if resourceName is None:
            raise ValueError("Missing required parameter 'resourceName'")
        url = f"{self.base_url}/v1/media/{resourceName}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_reporttypes(
        self,
        includeSystemManaged=None,
        onBehalfOfContentOwner=None,
        pageSize=None,
        pageToken=None,
    ) -> Any:
        """
        Retrieves a list of available report types from the YouTube Reporting API, supporting pagination and filtering. This function returns metadata about what kinds of reports can be generated, distinct from functions like `get_reports` that fetch actual report content.

        Args:
            includeSystemManaged: Boolean indicating whether to include system-managed report types in results.
            onBehalfOfContentOwner: Content owner ID for delegated authority requests.
            pageSize: Maximum number of items to return per response page.
            pageToken: Token identifying a specific results page for pagination.

        Returns:
            Dictionary containing report type entries and pagination details, typically including 'items' list and 'nextPageToken' if applicable.

        Raises:
            HTTPError: If the API request fails due to network issues, authentication problems, or invalid parameters.

        Tags:
            retrieve, list, api-resource, filtering, pagination, report-management
        """
        url = f"{self.base_url}/v1/reportTypes"
        query_params = {
            k: v
            for k, v in [
                ("includeSystemManaged", includeSystemManaged),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_captions(
        self, id=None, onBehalfOf=None, onBehalfOfContentOwner=None
    ) -> Any:
        """
        Deletes a specific YouTube caption resource using its unique ID, with optional delegation for content owners. This management function removes the entire caption track, unlike `get_captions` which only retrieves the transcript text for a given video ID.

        Args:
            id: Optional unique identifier for the caption resource to delete.
            onBehalfOf: Optional parameter identifying the user on whose behalf the request is made.
            onBehalfOfContentOwner: Optional parameter specifying the content owner authorizing the request.

        Returns:
            JSON response containing the result of the DELETE operation from the YouTube API.

        Raises:
            HTTPError: Raised when the HTTP request fails, such as invalid ID, authentication failures, or API limitations exceeded.

        Tags:
            delete, captions, api, management
        """
        url = f"{self.base_url}/captions"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("onBehalfOf", onBehalfOf),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
            ]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_transcript_text(self, video_id: str) -> str:
        """
        Fetches the full text transcript for a YouTube video using its ID. Unlike other methods using the official API, this function utilizes the `youtube-transcript-api` library to extract and concatenate all caption snippets into a single, timestamp-free string of the video's spoken content.

        Args:
            video_id: The unique identifier for the target video (required)

        Returns:
            String containing the complete transcript text without timestamps

        Raises:
            ValueError: Raised when required 'video_id' parameter is missing
            Exception: Raised when transcript cannot be retrieved (e.g., no captions available)

        Tags:
            retrieve, transcript, text, captions
        """
        if video_id is None:
            raise ValueError("Missing required parameter 'video_id'")

        try:
            proxy_username = os.getenv("PROXY_USERNAME")
            proxy_password = os.getenv("PROXY_PASSWORD")
            proxy_port = int(os.getenv("PROXY_PORT", 80))

            if not proxy_username or not proxy_password:
                raise ValueError(
                    "PROXY_USERNAME and PROXY_PASSWORD must be set when using proxy"
                )
            api = YouTubeTranscriptApi(
                proxy_config=WebshareProxyConfig(
                    proxy_username=proxy_username,
                    proxy_password=proxy_password,
                    proxy_port=proxy_port,
                ),
            )
            transcript = api.fetch(video_id)

            transcript_text = " ".join(
                [snippet.text for snippet in transcript.snippets]
            )

            return transcript_text
        except Exception as e:
            raise Exception(
                f"Failed to retrieve transcript for video {video_id}: {str(e)}"
            )

    def delete_comments(self, id=None) -> Any:
        """
        Permanently removes a specific comment identified by its unique ID via a DELETE request. Unlike moderation functions like `add_comments_mark_as_spam`, which only alter a comment's state, this action is irreversible and deletes the resource. An `id` is required to specify the target comment.

        Args:
            id: Optional ID of the comment to be deleted. If not provided, and based on implementation, all comments may be deleted.

        Returns:
            The JSON response from the server after attempting to delete the comment(s).

        Raises:
            requests.RequestException: Raised if there is a network error or an invalid response from the server.

        Tags:
            delete, comments, management
        """
        url = f"{self.base_url}/comments"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def mark_comment_as_spam(self, id=None) -> Any:
        """
        Marks a specified YouTube comment as spam via a POST request to the API. This moderation action is distinct from deleting comments (`delete_comments`) or setting other statuses like 'approved' or 'rejected' (`add_comments_set_moderation_status`).

        Args:
            id: Optional unique identifier of the comment to mark as spam (included in request parameters when provided).

        Returns:
            JSON response from the API containing the operation result.

        Raises:
            HTTPError: If the POST request fails or returns a non-200 status code.

        Tags:
            comments, spam, post-request, api, moderation
        """
        url = f"{self.base_url}/comments/markAsSpam"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_comment_moderation_status(
        self, banAuthor=None, id=None, moderationStatus=None
    ) -> Any:
        """
        Sets the moderation status (e.g., 'approved', 'rejected') for specified comments and can optionally ban the author. Unlike `add_comments_mark_as_spam`, this function allows for various moderation states, providing more granular control over comment management.

        Args:
            banAuthor: Optional boolean indicating whether to ban the comment's author
            id: Optional string representing the unique identifier of the comment to moderate
            moderationStatus: Optional string specifying the new moderation status (e.g., 'approved', 'rejected')

        Returns:
            JSON response from the server containing the result of the moderation operation

        Raises:
            requests.HTTPError: Raised when the HTTP request fails (e.g., invalid parameters or server errors)

        Tags:
            moderation, comments, management, api-client, status-update, ban-author
        """
        url = f"{self.base_url}/comments/setModerationStatus"
        query_params = {
            k: v
            for k, v in [
                ("banAuthor", banAuthor),
                ("id", id),
                ("moderationStatus", moderationStatus),
            ]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_live_broadcasts(
        self, id=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None
    ) -> Any:
        """
        Deletes a YouTube live broadcast event by its unique ID via the API. This request can be made on behalf of a content owner or channel. It targets the `/liveBroadcasts` endpoint, distinguishing it from `delete_livestreams` which manages the actual content stream.

        Args:
            id: Optional; Unique identifier of the live broadcast to delete (str).
            onBehalfOfContentOwner: Optional; Content owner acting on behalf of (str).
            onBehalfOfContentOwnerChannel: Optional; Channel ID linked to content owner (str).

        Returns:
            Dict[str, Any] containing the JSON-parsed response from the API request.

        Raises:
            requests.HTTPError: Raised for any HTTP request failures or invalid status codes (4XX/5XX).

        Tags:
            delete, live-broadcast, management, api
        """
        url = f"{self.base_url}/liveBroadcasts"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("onBehalfOfContentOwnerChannel", onBehalfOfContentOwnerChannel),
            ]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bind_live_broadcast_to_stream(
        self,
        id=None,
        onBehalfOfContentOwner=None,
        onBehalfOfContentOwnerChannel=None,
        part=None,
        streamId=None,
    ) -> Any:
        """
        Binds a YouTube live broadcast to a video stream using their respective IDs. This action associates the broadcast's metadata with the content stream, optionally performing the action on behalf of a content owner, facilitating the link between a planned event and its live video feed.

        Args:
            id: The id of the live broadcast to bind.
            onBehalfOfContentOwner: The YouTube CMS content owner on behalf of whom the operation is performed.
            onBehalfOfContentOwnerChannel: The YouTube channel ID for which the live broadcast is operated.
            part: A comma-separated list of liveBroadcast resource properties to include in the API response.
            streamId: The id of the stream to which the live broadcast is to be bound.

        Returns:
            The JSON response object from the YouTube API after attempting to bind the live broadcast to the stream.

        Raises:
            HTTPError: Raised if the request to the YouTube API fails, typically due to server errors or invalid responses.

        Tags:
            bind, youtube-api, live-broadcast, stream
        """
        url = f"{self.base_url}/liveBroadcasts/bind"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("onBehalfOfContentOwnerChannel", onBehalfOfContentOwnerChannel),
                ("part", part),
                ("streamId", streamId),
            ]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def control_live_broadcast(
        self,
        displaySlate=None,
        id=None,
        offsetTimeMs=None,
        onBehalfOfContentOwner=None,
        onBehalfOfContentOwnerChannel=None,
        part=None,
        walltime=None,
    ) -> Any:
        """
        Sends control commands to a YouTube live broadcast, identified by its ID. It can display a slate or schedule an action using a time offset. Unlike `add_live_broadcasts_transition`, which alters broadcast status (e.g., 'live'), this function manages in-stream state.

        Args:
            displaySlate: Optional; Specifies whether or not to show a slate during the broadcast.
            id: Optional; The ID of the live broadcast to control.
            offsetTimeMs: Optional; The offset time in milliseconds for the broadcast control action.
            onBehalfOfContentOwner: Optional; Indicates that the request is made on behalf of a content owner.
            onBehalfOfContentOwnerChannel: Optional; The channel owned by the content owner.
            part: Optional; Specifies a comma-separated list of one or more broadcasts resource properties.
            walltime: Optional; An RFC 3339 timestamp that represents the time at which the action takes place.

        Returns:
            The JSON response from the server after controlling the live broadcast.

        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.

        Tags:
            control, live-broadcast, async_job, management
        """
        url = f"{self.base_url}/liveBroadcasts/control"
        query_params = {
            k: v
            for k, v in [
                ("displaySlate", displaySlate),
                ("id", id),
                ("offsetTimeMs", offsetTimeMs),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("onBehalfOfContentOwnerChannel", onBehalfOfContentOwnerChannel),
                ("part", part),
                ("walltime", walltime),
            ]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def transition_live_broadcast(
        self,
        broadcastStatus=None,
        id=None,
        onBehalfOfContentOwner=None,
        onBehalfOfContentOwnerChannel=None,
        part=None,
    ) -> Any:
        """
        Changes a YouTube live broadcast's status (e.g., making it 'live' or 'complete') by posting to the API's transition endpoint. This function alters the broadcast's lifecycle state, distinct from other control actions like binding it to a stream, and returns the API's JSON response.

        Args:
            broadcastStatus: Optional; The status to which the live broadcast should be transitioned.
            id: Optional; The unique identifier of the broadcast that needs to be transitioned.
            onBehalfOfContentOwner: Optional; The YouTube content owner on whose behalf the API request is being made.
            onBehalfOfContentOwnerChannel: Optional; The YouTube channel ID of the channel associated with the specified content owner.
            part: Optional; A comma-separated list of one or more liveBroadcast resource properties that the API response will include.

        Returns:
            The JSON response from the API containing the details of the transitioned live broadcast.

        Raises:
            requests.HTTPError: Raised when the HTTP request to the API fails due to a server error or invalid request.

        Tags:
            transition, live-broadcast, youtube-api, video-management
        """
        url = f"{self.base_url}/liveBroadcasts/transition"
        query_params = {
            k: v
            for k, v in [
                ("broadcastStatus", broadcastStatus),
                ("id", id),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("onBehalfOfContentOwnerChannel", onBehalfOfContentOwnerChannel),
                ("part", part),
            ]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_live_chat_ban(self, id=None) -> Any:
        """
        Deletes a specific YouTube live chat ban using its unique ID. It sends a DELETE request to the `/liveChat/bans` endpoint to revoke the ban, allowing the user to participate in the chat again.

        Args:
            id: Optional; The unique identifier of the live chat ban to delete. If None, no specific ban is targeted.

        Returns:
            The JSON response from the server after deletion, typically containing operation details.

        Raises:
            requests.HTTPError: Raised if the HTTP request fails, indicating server-side issues or invalid parameters.

        Tags:
            delete, management, live-chat, async-job
        """
        url = f"{self.base_url}/liveChat/bans"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_live_chat_message(self, id=None) -> Any:
        """
        Deletes a specific YouTube live chat message identified by its unique ID. This function targets the `/liveChat/messages` endpoint, distinguishing it from `delete_live_chat_bans` and `delete_live_chat_moderators`, which manage different aspects of a live chat.

        Args:
            id: Optional; The identifier of the specific live chat message to be deleted. If not provided, it defaults to None.

        Returns:
            A JSON object containing the server's response to the deletion request. It includes details about the operation's success or failure.

        Raises:
            HTTPError: Raised if the HTTP request to delete the message fails.

        Tags:
            delete, live-chat, message-management
        """
        url = f"{self.base_url}/liveChat/messages"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_live_chat_moderators(self, id=None) -> Any:
        """
        Deletes a specific YouTube live chat moderator using their unique ID. This function sends a DELETE request to the `/liveChat/moderators` API endpoint and returns the server's JSON response, confirming the successful removal or detailing errors. The moderator ID is a required parameter for this action.

        Args:
            id: The ID of the live chat moderator to delete. When None, no deletion occurs (moderator IDs must be explicitly specified).

        Returns:
            Parsed JSON response from the server containing deletion confirmation or error details.

        Raises:
            requests.HTTPError: Raised for unsuccessful HTTP responses (e.g., invalid ID, authorization failure, or server errors).

        Tags:
            delete, moderators, management, live-chat, async_job, ids
        """
        url = f"{self.base_url}/liveChat/moderators"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_videos(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes a specified YouTube video using its unique ID. The operation can be performed on behalf of a content owner by sending an HTTP DELETE request to the `/videos` endpoint. It's distinct from other video functions that only modify or retrieve metadata, like rating or abuse reports.

        Args:
            id: (str, optional): Unique identifier of the video to delete. If omitted, no video ID is specified.
            onBehalfOfContentOwner: (str, optional): Content owner on whose behalf the operation is performed. Defaults to authenticated user.

        Returns:
            (Any): Parsed JSON response from the API including deletion status/errors.

        Raises:
            requests.HTTPError: Raised when the API request fails (e.g., invalid video ID, insufficient permissions).

        Tags:
            delete, video-management, api, async_job
        """
        url = f"{self.base_url}/videos"
        query_params = {
            k: v
            for k, v in [("id", id), ("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_video_ratings(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Retrieves the authenticated user's rating (e.g., 'like', 'dislike') for specified videos. This function fetches existing rating data, distinct from `add_videos_rate` which submits a new rating, and can be performed on behalf of a content owner.

        Args:
            id: Optional; The ID of the video for which the rating is to be retrieved. If None, no specific video ID is used in the request.
            onBehalfOfContentOwner: Optional; Identifies the content owner for whom the request is being made.

        Returns:
            A JSON object containing the video rating information returned by the API.

        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.

        Tags:
            check, video-management
        """
        url = f"{self.base_url}/videos/getRating"
        query_params = {
            k: v
            for k, v in [("id", id), ("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def rate_video(self, id=None, rating=None) -> Any:
        """
        Submits a rating (e.g., 'like', 'dislike') for a video specified by its unique ID. This function sends a POST request to the YouTube API's `/videos/rate` endpoint and returns the server's JSON response upon successful submission.

        Args:
            id: Optional; The unique identifier of the video to rate. If None, the video ID is not included in the request.
            rating: Optional; The rating value to assign to the video. If None, the rating is not included in the request.

        Returns:
            The JSON response from the server after submitting the rating.

        Raises:
            HTTPError: Raised when the server returns an HTTP error status.

        Tags:
            rate, video-management, importance
        """
        url = f"{self.base_url}/videos/rate"
        query_params = {
            k: v for k, v in [("id", id), ("rating", rating)] if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def report_video_for_abuse(self, onBehalfOfContentOwner=None) -> Any:
        """
        Reports a video for abuse via a POST request to the YouTube API. An optional parameter allows a content owner to submit the report on behalf of their account, flagging potentially inappropriate content for review by YouTube.

        Args:
            onBehalfOfContentOwner: Optional; YouTube content owner ID acting as the reporting entity (for partner accounts).

        Returns:
            Dict containing the JSON response from the YouTube API after reporting abuse.

        Raises:
            HTTPError: Raised when the YouTube API request fails, typically due to authentication errors or invalid parameters.

        Tags:
            report, abuse, video, content, api
        """
        url = f"{self.base_url}/videos/reportAbuse"
        query_params = {
            k: v
            for k, v in [("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_channel_watermark(self, channelId=None, onBehalfOfContentOwner=None) -> Any:
        """
        Sets a branding watermark on a specified YouTube channel. The operation targets the channel using its ID and can be executed on behalf of a content owner. This function contrasts with `add_watermarks_unset`, which removes the watermark.

        Args:
            channelId: Optional; The ID of the YouTube channel on which to set the watermark.
            onBehalfOfContentOwner: Optional; The content owner's ID that the request is made on behalf of.

        Returns:
            The JSON response from the API call, which includes details about the watermark setting operation.

        Raises:
            requests.RequestException: Raised if there is an error with the API request, such as connection issues or invalid response status.

        Tags:
            watermark, youtube, management, channel-config
        """
        url = f"{self.base_url}/watermarks/set"
        query_params = {
            k: v
            for k, v in [
                ("channelId", channelId),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
            ]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def unset_channel_watermark(
        self, channelId=None, onBehalfOfContentOwner=None
    ) -> Any:
        """
        Removes the branding watermark for a specified YouTube channel via an API POST request. This operation, the inverse of `add_watermarks_set`, can be executed on behalf of a content owner to unset the channel's current watermark.

        Args:
            channelId: Optional; The unique identifier of the YouTube channel from which to remove watermarks.
            onBehalfOfContentOwner: Optional; The content owner that the request is on behalf of, used by YouTube content partners.

        Returns:
            The JSON response from the YouTube API after attempting to remove the watermarks.

        Raises:
            HTTPError: Raised when there is an error in the HTTP request or if the server returns a status code indicating a client or server error.

        Tags:
            remove, watermark, youtube
        """
        url = f"{self.base_url}/watermarks/unset"
        query_params = {
            k: v
            for k, v in [
                ("channelId", channelId),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
            ]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_activities(
        self,
        channelId=None,
        home=None,
        maxResults=None,
        mine=None,
        pageToken=None,
        part=None,
        publishedAfter=None,
        publishedBefore=None,
        regionCode=None,
    ) -> Any:
        """
        Retrieves a list of YouTube activities, such as video uploads or social posts. Supports filtering by channel, authenticated user's feed, publication date, and region. The function also handles pagination to navigate through large result sets and returns the JSON response from the API.

        Args:
            channelId: The YouTube channel ID to fetch activities from. If None, fetches from multiple sources (depending on other parameters).
            home: If True, retrieves activities from the user's personalized YouTube home feed. Requires authentication if mine is not specified.
            maxResults: Maximum number of items to return in the response list (1-50, default server-side limit).
            mine: If True, retrieves activities from the authenticated user's channel. Requires authentication.
            pageToken: Token to fetch a specific page of results, used for pagination.
            part: Comma-separated list of resource parts to include in the response (e.g., 'snippet,contentDetails').
            publishedAfter: Filter activities published after this datetime (ISO 8601 format).
            publishedBefore: Filter activities published before this datetime (ISO 8601 format).
            regionCode: Return activities viewable in the specified two-letter ISO country code.

        Returns:
            Dictionary containing parsed JSON response with activity data.

        Raises:
            requests.HTTPError: Raised when the API request fails due to invalid parameters, authentication issues, or server errors.

        Tags:
            retrieve, activities, youtube, api-client, pagination, filter, async
        """
        url = f"{self.base_url}/activities"
        query_params = {
            k: v
            for k, v in [
                ("channelId", channelId),
                ("home", home),
                ("maxResults", maxResults),
                ("mine", mine),
                ("pageToken", pageToken),
                ("part", part),
                ("publishedAfter", publishedAfter),
                ("publishedBefore", publishedBefore),
                ("regionCode", regionCode),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def insert_channel_banner(self, channelId=None, onBehalfOfContentOwner=None) -> Any:
        """
        Uploads and sets a new banner image for a specified YouTube channel. This function makes a POST request to the `/channelBanners/insert` endpoint, optionally on behalf of a content owner, and returns details of the newly created banner.

        Args:
            channelId: Optional string specifying the unique identifier of the YouTube channel for banner insertion
            onBehalfOfContentOwner: Optional string indicating the content owner's external ID when acting on their behalf

        Returns:
            JSON object containing the API response with details of the newly inserted channel banner

        Raises:
            HTTPError: Raised when the YouTube Data API request fails (4XX or 5XX status code)

        Tags:
            insert, channel, banner, youtube-api, management, async_job
        """
        url = f"{self.base_url}/channelBanners/insert"
        query_params = {
            k: v
            for k, v in [
                ("channelId", channelId),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
            ]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_channel_sections(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes a YouTube channel section by its unique ID via an API request. The operation can be performed on behalf of a content owner for delegated management, returning a JSON response upon success or raising an HTTPError for failures like invalid IDs or insufficient permissions.

        Args:
            id: Optional string representing the unique identifier of the target channel section. If omitted, no specific deletion occurs (behavior depends on API implementation).
            onBehalfOfContentOwner: Optional string indicating the content owner on whose behalf the request is made.

        Returns:
            JSON-decoded response payload from the API server after deletion attempt.

        Raises:
            requests.HTTPError: Raised for HTTP 4xx/5xx responses from the server during the deletion request.

        Tags:
            delete, channel-section, management
        """
        url = f"{self.base_url}/channelSections"
        query_params = {
            k: v
            for k, v in [("id", id), ("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_channels(
        self,
        categoryId=None,
        forUsername=None,
        hl=None,
        id=None,
        managedByMe=None,
        maxResults=None,
        mine=None,
        mySubscribers=None,
        onBehalfOfContentOwner=None,
        pageToken=None,
        part=None,
    ) -> Any:
        """
        Retrieves channel data from the YouTube API using specific filters like ID, username, or ownership status (`mine`, `managedByMe`). The function supports pagination and localization, returning a JSON object containing details for the targeted channels.

        Args:
            categoryId: Category ID to filter channels.
            forUsername: Username to retrieve channels for.
            hl: Language code for localized output.
            id: List of channel IDs to retrieve.
            managedByMe: Flag to retrieve channels managed by the current user.
            maxResults: Maximum number of results to return.
            mine: Flag to retrieve channels owned by the current user.
            mySubscribers: Flag to retrieve channels subscribed by the current user.
            onBehalfOfContentOwner: Content owner ID to retrieve channels on behalf of.
            pageToken: Token for pagination.
            part: Specified parts of the channel resource to include in the response.

        Returns:
            JSON response containing the requested channels.

        Raises:
            ResponseError: Raised if there is an error in the HTTP response.

        Tags:
            search, youtube, channels, management, important
        """
        url = f"{self.base_url}/channels"
        query_params = {
            k: v
            for k, v in [
                ("categoryId", categoryId),
                ("forUsername", forUsername),
                ("hl", hl),
                ("id", id),
                ("managedByMe", managedByMe),
                ("maxResults", maxResults),
                ("mine", mine),
                ("mySubscribers", mySubscribers),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("pageToken", pageToken),
                ("part", part),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_comment_threads(
        self,
        allThreadsRelatedToChannelId=None,
        channelId=None,
        id=None,
        maxResults=None,
        moderationStatus=None,
        order=None,
        pageToken=None,
        part=None,
        searchTerms=None,
        textFormat=None,
        videoId=None,
    ) -> Any:
        """
        Retrieves YouTube comment threads using filters like channel ID, video ID, or search terms. It supports pagination and sorting, serving as the primary method for fetching comment data, distinct from other functions in the script that moderate or delete individual comments.

        Args:
            allThreadsRelatedToChannelId: Returns all threads associated with the specified channel, including replies
            channelId: Channel ID to filter comment threads
            id: Specific comment thread ID(s) to retrieve
            maxResults: Maximum number of items to return (1-100)
            moderationStatus: Filter by moderation status (e.g., 'heldForReview')
            order: Sort order for results (e.g., 'time', 'relevance')
            pageToken: Pagination token for retrieving specific result pages
            part: Comma-separated list of resource properties to include
            searchTerms: Text search query to filter comments
            textFormat: Formatting for comment text (e.g., 'html', 'plainText')
            videoId: Video ID to filter associated comment threads

        Returns:
            JSON response containing comment thread data and pagination information

        Raises:
            HTTPError: Raised for unsuccessful API requests (4xx/5xx status codes)

        Tags:
            retrieve, comments, pagination, youtube-api, rest, data-fetch
        """
        url = f"{self.base_url}/commentThreads"
        query_params = {
            k: v
            for k, v in [
                ("allThreadsRelatedToChannelId", allThreadsRelatedToChannelId),
                ("channelId", channelId),
                ("id", id),
                ("maxResults", maxResults),
                ("moderationStatus", moderationStatus),
                ("order", order),
                ("pageToken", pageToken),
                ("part", part),
                ("searchTerms", searchTerms),
                ("textFormat", textFormat),
                ("videoId", videoId),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_fanfundingevents(
        self, hl=None, maxResults=None, pageToken=None, part=None
    ) -> Any:
        """
        Fetches a list of fan funding events from the YouTube API for the authenticated user's channel. Supports pagination, localization, and partial responses to retrieve customized event data like Super Chat or Super Stickers based on specified filter criteria and response parts.

        Args:
            hl: Optional; a string representing the language for text values.
            maxResults: Optional; an integer specifying the maximum number of results to return.
            pageToken: Optional; a string token to retrieve a specific page in a paginated set of results.
            part: Optional; a comma-separated list of one or more 'fanFundingEvent' resource properties that the API response will include.

        Returns:
            A JSON-decoded response of the fan funding events data retrieved from the API.

        Raises:
            HTTPError: Raised if the API request returns a status code that indicates an error.

        Tags:
            retrieve, events, fanfunding
        """
        url = f"{self.base_url}/fanFundingEvents"
        query_params = {
            k: v
            for k, v in [
                ("hl", hl),
                ("maxResults", maxResults),
                ("pageToken", pageToken),
                ("part", part),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_guide_categories(self, hl=None, id=None, part=None, regionCode=None) -> Any:
        """
        Retrieves a list of official YouTube guide categories (e.g., Music, Sports). This function queries the `/guideCategories` endpoint, allowing results to be filtered by ID or region and localized for a specific language. These are distinct from the categories assigned to individual videos.

        Args:
            hl: Optional; a string that specifies the language localization.
            id: Optional; a string representing the ID of the guide category.
            part: Optional; a string indicating which parts of the guide category resource to return.
            regionCode: Optional; a string that denotes the region of interest.

        Returns:
            A dictionary containing the JSON response representing guide categories from the service.

        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.

        Tags:
            get, fetch, guide-categories, api-call
        """
        url = f"{self.base_url}/guideCategories"
        query_params = {
            k: v
            for k, v in [
                ("hl", hl),
                ("id", id),
                ("part", part),
                ("regionCode", regionCode),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_i18n_languages(self, hl=None, part=None) -> Any:
        """
        Retrieves a list of supported internationalization (i18n) languages from the YouTube API's `/i18nLanguages` endpoint. It can optionally localize the language names in the response. This function is distinct from `get_regions`, which fetches supported geographical regions.

        Args:
            hl: Optional language code to localize returned language names (e.g., 'en' for English).
            part: Optional comma-separated list of i18nLanguage resource properties to include in response.

        Returns:
            JSON object containing API response with supported languages data.

        Raises:
            HTTPError: Raised for unsuccessful API requests (4XX/5XX status codes).

        Tags:
            fetch, i18n, languages, api-client
        """
        url = f"{self.base_url}/i18nLanguages"
        query_params = {k: v for k, v in [("hl", hl), ("part", part)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_i18n_regions(self, hl=None, part=None) -> Any:
        """
        Fetches a list of geographic regions supported by the YouTube API for content localization. It can localize region names using the 'hl' parameter. This is distinct from get_languages, which retrieves supported languages, not geographic areas.

        Args:
            hl: Optional string representing language code for regional localization.
            part: Optional comma-separated string specifying i18nRegion resource parts to include.

        Returns:
            JSON response containing i18n regions data.

        Raises:
            HTTPError: If the API request fails with a 4XX/5XX status code.

        Tags:
            list, regions, i18n, api
        """
        url = f"{self.base_url}/i18nRegions"
        query_params = {k: v for k, v in [("hl", hl), ("part", part)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_livestreams(
        self, id=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None
    ) -> Any:
        """
        Deletes one or more YouTube livestreams by ID via the `/liveStreams` API endpoint, optionally on behalf of a content owner. This function is distinct from `delete_live_broadcasts`, which targets a different live video resource, and returns the server's JSON response upon successful deletion.

        Args:
            id: Optional; A comma-separated list of YouTube livestream IDs to be deleted.
            onBehalfOfContentOwner: Optional; The YouTube content owner who is the channel owner of the livestream and makes this API call.
            onBehalfOfContentOwnerChannel: Optional; The YouTube channel ID on behalf of which the API call is made.

        Returns:
            A JSON object containing the API's response to the delete request.

        Raises:
            requests.HTTPError: Raised when the HTTP request returns an unsuccessful status code.

        Tags:
            delete, livestream, youtube, api
        """
        url = f"{self.base_url}/liveStreams"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("onBehalfOfContentOwnerChannel", onBehalfOfContentOwnerChannel),
            ]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_playlist_items(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes one or more YouTube playlist items by their unique IDs. The operation can be performed on behalf of a content owner for delegated authorization, sending a DELETE request to the `/playlistItems` endpoint and returning the server's response.

        Args:
            id: Optional; The ID of the playlist item to be deleted.
            onBehalfOfContentOwner: Optional; The content owner on whose behalf the playlist item is being deleted.

        Returns:
            JSON response from the server indicating the result of the deletion operation.

        Raises:
            HTTPError: Raised if the API request fails due to invalid parameters, authorization issues, or server errors.

        Tags:
            delete, playlist-items, management
        """
        url = f"{self.base_url}/playlistItems"
        query_params = {
            k: v
            for k, v in [("id", id), ("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_playlists(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes a YouTube playlist by its unique ID via a DELETE request to the API. The operation can be performed on behalf of a specific content owner for delegated management. This function targets the entire playlist, distinct from `delete_play_list_items` which removes individual videos from a playlist.

        Args:
            id: Optional; A string representing the ID of the playlist to delete. If None, operation details depend on API implementation (not recommended without explicit identifier).
            onBehalfOfContentOwner: Optional; A string representing the content owner on whose behalf the operation is performed. Used for delegated access.

        Returns:
            Dictionary containing the JSON response from the YouTube API after playlist deletion.

        Raises:
            HTTPError: Raised when the API request fails, typically due to invalid permissions, non-existent playlist, or network issues.

        Tags:
            delete, playlists, youtube-api, management
        """
        url = f"{self.base_url}/playlists"
        query_params = {
            k: v
            for k, v in [("id", id), ("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_search(
        self,
        channelId=None,
        channelType=None,
        eventType=None,
        forContentOwner=None,
        forDeveloper=None,
        forMine=None,
        location=None,
        locationRadius=None,
        maxResults=None,
        onBehalfOfContentOwner=None,
        order=None,
        pageToken=None,
        part=None,
        publishedAfter=None,
        publishedBefore=None,
        q=None,
        regionCode=None,
        relatedToVideoId=None,
        relevanceLanguage=None,
        safeSearch=None,
        topicId=None,
        type=None,
        videoCaption=None,
        videoCategoryId=None,
        videoDefinition=None,
        videoDimension=None,
        videoDuration=None,
        videoEmbeddable=None,
        videoLicense=None,
        videoSyndicated=None,
        videoType=None,
    ) -> Any:
        """
        Performs a versatile search on YouTube for videos, channels, or playlists. This function supports extensive filters, including keywords, publication dates, location, and specific video attributes like category or duration, returning a paginated list of matching resources from the YouTube Data API.

        Args:
            channelId: Channel filter for the search.
            channelType: Type of channel to filter by.
            eventType: Type of event to filter by.
            forContentOwner: Whether to search for content owned by the specified content owner.
            forDeveloper: Whether to search for content owned by the developer.
            forMine: Whether to search for the user's videos.
            location: Geographic location to filter results by.
            locationRadius: Radius of the geographic location.
            maxResults: Maximum number of search results to return.
            onBehalfOfContentOwner: Owner ID when acting on behalf of a content owner.
            order: Order in which search results are returned.
            pageToken: Page token for pagination.
            part: Response parts to return.
            publishedAfter: After date to filter by.
            publishedBefore: Before date to filter by.
            q: Search query string.
            regionCode: Region code to filter by.
            relatedToVideoId: Search related videos to the specified ID.
            relevanceLanguage: Language used for relevance.
            safeSearch: Safe search settings.
            topicId: Topic filter.
            type: Type of resource to return.
            videoCaption: Caption filter for videos.
            videoCategoryId: Category of videos.
            videoDefinition: Video definition filter (e.g., 'hd').
            videoDimension: Dimension filter (e.g., '2d', '3d').
            videoDuration: Duration filter for videos.
            videoEmbeddable: Whether videos are embeddable.
            videoLicense: License filter for videos.
            videoSyndicated: Whether videos are syndicated.
            videoType: Type of video (e.g., 'movie', 'episode')

        Returns:
            JSON response containing the search results.

        Raises:
            HTTPError: If the request to the YouTube Data API fails.

        Tags:
            search, youtube-api, video-search, web-api, important
        """
        url = f"{self.base_url}/search"
        query_params = {
            k: v
            for k, v in [
                ("channelId", channelId),
                ("channelType", channelType),
                ("eventType", eventType),
                ("forContentOwner", forContentOwner),
                ("forDeveloper", forDeveloper),
                ("forMine", forMine),
                ("location", location),
                ("locationRadius", locationRadius),
                ("maxResults", maxResults),
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("order", order),
                ("pageToken", pageToken),
                ("part", part),
                ("publishedAfter", publishedAfter),
                ("publishedBefore", publishedBefore),
                ("q", q),
                ("regionCode", regionCode),
                ("relatedToVideoId", relatedToVideoId),
                ("relevanceLanguage", relevanceLanguage),
                ("safeSearch", safeSearch),
                ("topicId", topicId),
                ("type", type),
                ("videoCaption", videoCaption),
                ("videoCategoryId", videoCategoryId),
                ("videoDefinition", videoDefinition),
                ("videoDimension", videoDimension),
                ("videoDuration", videoDuration),
                ("videoEmbeddable", videoEmbeddable),
                ("videoLicense", videoLicense),
                ("videoSyndicated", videoSyndicated),
                ("videoType", videoType),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_sponsors(
        self, filter=None, maxResults=None, pageToken=None, part=None
    ) -> Any:
        """
        Retrieves a list of sponsors for the authenticated user's YouTube channel. This function supports filtering, pagination, and specifying which resource parts to include in the response, allowing for flexible and customized data fetching of sponsor information.

        Args:
            filter: Optional string containing filtering criteria for sponsors.
            maxResults: Optional integer limiting the number of returned sponsors.
            pageToken: Optional token string for paginating to a specific result page.
            part: Optional string specifying which sponsor detail parts to include.

        Returns:
            JSON response containing the list of sponsors (filtered/paginated) as returned by the server.

        Raises:
            requests.HTTPError: If the HTTP request fails or returns a non-200 status code.

        Tags:
            fetch, list, pagination, filter, sponsors, api
        """
        url = f"{self.base_url}/sponsors"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("maxResults", maxResults),
                ("pageToken", pageToken),
                ("part", part),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_subscriptions(self, id=None) -> Any:
        """
        Deletes a specific YouTube channel subscription identified by its unique ID. This function sends a DELETE request to the `/subscriptions` API endpoint and returns the server's JSON response, confirming the operation's success or failure.

        Args:
            id: Optional identifier for a specific subscription to delete (str, int, or None). If None, deletes all subscriptions.

        Returns:
            JSON-formatted response from the API containing deletion results.

        Raises:
            HTTPError: Raised for HTTP request failures (4XX/5XX status codes) during the deletion attempt.

        Tags:
            delete, subscriptions, async-job, management
        """
        url = f"{self.base_url}/subscriptions"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_super_chat_events(
        self, hl=None, maxResults=None, pageToken=None, part=None
    ) -> Any:
        """
        Retrieves a paginated list of Super Chat events from the YouTube Data API. Allows for localization and specifying which resource parts to include in the response. This function is distinct from `get_fanfundingevents`, which fetches a different type of monetary contribution event.

        Args:
            hl: Optional; the language code to select localized resource information.
            maxResults: Optional; the maximum number of items that should be returned in the result set.
            pageToken: Optional; the token to identify a specific page in the result set.
            part: Optional; the parameter specifying which super chat event resource parts to include in the response.

        Returns:
            A JSON object containing the super chat events data returned by the YouTube API.

        Raises:
            RequestException: Raised if there is an issue with the HTTP request, such as network or server errors.

        Tags:
            fetch, youtube-api, async-job
        """
        url = f"{self.base_url}/superChatEvents"
        query_params = {
            k: v
            for k, v in [
                ("hl", hl),
                ("maxResults", maxResults),
                ("pageToken", pageToken),
                ("part", part),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_video_thumbnail(self, onBehalfOfContentOwner=None, videoId=None) -> Any:
        """
        Sets a custom thumbnail for a specified YouTube video via a POST request to the `/thumbnails/set` API endpoint. The operation can be performed on behalf of a content owner for delegated management of video assets.

        Args:
            onBehalfOfContentOwner: Optional; str. The YouTube content owner ID on whose behalf the request is being made.
            videoId: Optional; str. The ID of the video for which the thumbnails are being set.

        Returns:
            dict. The response from the YouTube API as a JSON object, containing details of the updated video thumbnail.

        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.

        Tags:
            thumbnail, youtube-api, video-management, async-job
        """
        url = f"{self.base_url}/thumbnails/set"
        query_params = {
            k: v
            for k, v in [
                ("onBehalfOfContentOwner", onBehalfOfContentOwner),
                ("videoId", videoId),
            ]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_video_abuse_report_reasons(self, hl=None, part=None) -> Any:
        """
        Retrieves a list of valid reasons (e.g., spam, hate speech) for reporting abusive video content. Supports response localization using a language code (`hl`) and allows filtering which parts of the reason resource (e.g., ID, snippet) are returned, providing metadata before submitting a report.

        Args:
            hl: Optional BCP-47 language code for localizing the response (e.g., 'en' or 'fr').
            part: Optional parameter specifying which parts of the abuse report reasons to include in the response (e.g., 'id' or 'snippet').

        Returns:
            A JSON object containing the list of video abuse report reasons, or filtered parts if specified.

        Raises:
            requests.RequestException: Raised if there is a problem with the HTTP request (e.g., network issues or invalid response).

        Tags:
            fetch, management, abuse-report, video-content
        """
        url = f"{self.base_url}/videoAbuseReportReasons"
        query_params = {k: v for k, v in [("hl", hl), ("part", part)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_video_categories(self, hl=None, id=None, part=None, regionCode=None) -> Any:
        """
        Retrieves official YouTube video categories used for classifying uploaded videos, allowing filtering by ID, region, or language. This is distinct from `get_guecategories`, which fetches channel browsing guides, not categories for individual video uploads.

        Args:
            hl: Optional; the language code (e.g., 'en') for localized video category names
            id: Optional; comma-separated list of video category IDs to filter results
            part: Optional; list of properties (e.g., 'snippet') to include in the response
            regionCode: Optional; ISO 3166-1 alpha-2 country code to filter region-specific categories

        Returns:
            Dictionary containing parsed JSON response with video category details

        Raises:
            requests.HTTPError: Raised when the API request fails with a non-success status code

        Tags:
            fetch, video-categories, api-request, json-response
        """
        url = f"{self.base_url}/videoCategories"
        query_params = {
            k: v
            for k, v in [
                ("hl", hl),
                ("id", id),
                ("part", part),
                ("regionCode", regionCode),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_group_items(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes specified items from a YouTube Analytics group via an API request. An item can be targeted by its unique ID, and the action can be performed on behalf of a content owner. This function is distinct from `delete_groups`, which removes the entire group.

        Args:
            id: Optional; A string that identifies the group item to be deleted. If not provided, all group items may be affected depending on other parameters.
            onBehalfOfContentOwner: Optional; A string representing the content owner on whose behalf the request is being made.

        Returns:
            A JSON object containing the response from the deletion request.

        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.

        Tags:
            delete, groupitems, management
        """
        url = f"{self.base_url}/groupItems"
        query_params = {
            k: v
            for k, v in [("id", id), ("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_groups(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes a YouTube group by its ID via an API request, optionally on behalf of a content owner. Unlike `delete_groupitems`, which only removes an item from a group, this function deletes the entire group entity.

        Args:
            id: Optional unique identifier for the group to delete. If None, no specific group targeted.
            onBehalfOfContentOwner: Optional content owner ID for delegated authorization.

        Returns:
            JSON-decoded response indicating operation success/failure.

        Raises:
            requests.exceptions.HTTPError: Raised for invalid requests, authentication failures, or server errors during deletion.

        Tags:
            delete, management, async_job, api
        """
        url = f"{self.base_url}/groups"
        query_params = {
            k: v
            for k, v in [("id", id), ("onBehalfOfContentOwner", onBehalfOfContentOwner)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_analytics_report(
        self,
        currency=None,
        dimensions=None,
        end=None,
        filters=None,
        ids=None,
        include=None,
        max=None,
        metrics=None,
        sort=None,
        start=None,
    ) -> Any:
        """
        Queries the YouTube Analytics API for performance reports, allowing customization via metrics, dimensions, and filters. Unlike `get_jobs_job_reports` which manages bulk report jobs, this function fetches analytical data directly, providing on-demand insights into channel or content performance.

        Args:
            currency: Optional; specifies the currency format for monetary values in the report
            dimensions: Optional; list of dimensions (e.g., 'country', 'device') to include in report breakdowns
            end: Optional; end date (YYYY-MM-DD format) for the report data range
            filters: Optional; conditions to filter report rows (e.g., 'country=US,clicks>100')
            ids: Optional; specific object identifiers (e.g., campaign IDs) to include in the report
            include: Optional; secondary datasets or entities to include in the report output
            max: Optional; maximum number of results to return per pagination batch
            metrics: Optional; list of measurable values to include (e.g., 'clicks', 'conversions')
            sort: Optional; criteria for sorting results (e.g., '-clicks' for descending order)
            start: Optional; start date (YYYY-MM-DD format) for the report data range

        Returns:
            Report data as parsed JSON from the API response

        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to invalid parameters, authentication issues, or server errors

        Tags:
            fetch, report, api, filter, sort, metrics, management
        """
        url = f"{self.base_url}/reports"
        query_params = {
            k: v
            for k, v in [
                ("currency", currency),
                ("dimensions", dimensions),
                ("end", end),
                ("filters", filters),
                ("ids", ids),
                ("include", include),
                ("max", max),
                ("metrics", metrics),
                ("sort", sort),
                ("start", start),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        """
        Returns a list of tool methods available in the class instance.

        Args:
            None: This function does not accept any parameters.

        Returns:
            list: A list containing references to various tool methods associated with job reports, media resources, comments, broadcasts, videos, activities, channels, etc.
        """
        return [
            self.list_job_reports,
            self.get_job_report,
            self.delete_job,
            self.list_jobs,
            self.download_report_media,
            self.get_reporttypes,
            self.delete_captions,
            self.get_transcript_text,
            self.delete_comments,
            self.mark_comment_as_spam,
            self.set_comment_moderation_status,
            self.delete_live_broadcasts,
            self.bind_live_broadcast_to_stream,
            self.control_live_broadcast,
            self.transition_live_broadcast,
            self.delete_live_chat_ban,
            self.delete_live_chat_message,
            self.delete_live_chat_moderators,
            self.delete_videos,
            self.get_video_ratings,
            self.rate_video,
            self.report_video_for_abuse,
            self.set_channel_watermark,
            self.unset_channel_watermark,
            self.get_activities,
            self.insert_channel_banner,
            self.delete_channel_sections,
            self.list_channels,
            self.get_comment_threads,
            self.get_fanfundingevents,
            self.get_guide_categories,
            self.get_i18n_languages,
            self.get_i18n_regions,
            self.delete_livestreams,
            self.delete_playlist_items,
            self.delete_playlists,
            self.get_search,
            self.list_sponsors,
            self.delete_subscriptions,
            self.get_super_chat_events,
            self.set_video_thumbnail,
            self.get_video_abuse_report_reasons,
            self.get_video_categories,
            self.delete_group_items,
            self.delete_groups,
            self.get_analytics_report,
        ]
