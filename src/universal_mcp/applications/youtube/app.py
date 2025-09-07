from typing import Any

from youtube_transcript_api import YouTubeTranscriptApi

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class YoutubeApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
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

    def get_jobs_job_reports(
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
        Retrieves job reports for a specified job based on provided filters and parameters.

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

    def get_jobs_job_reports_report(
        self, jobId, reportId, onBehalfOfContentOwner=None
    ) -> Any:
        """
        Retrieves a specific report associated with a job using the provided job and report identifiers.

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

    def delete_jobs_job(self, jobId, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes a job with the specified ID, optionally acting on behalf of a content owner.

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

    def get_jobs(
        self,
        includeSystemManaged=None,
        onBehalfOfContentOwner=None,
        pageSize=None,
        pageToken=None,
    ) -> Any:
        """
        Retrieves a list of jobs from the server with optional filtering by query parameters.

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

    def get_media_resource_name(self, resourceName) -> Any:
        """
        Retrieves a media resource by name and returns its JSON representation.

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
        Retrieves a paginated list of report types from the API with optional filtering.

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
        Deletes specified captions from a YouTube resource and returns the API response.

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

    def get_captions(self, video_id: str) -> str:
        """
        Retrieves the captions text for a specified video ID on youtube

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
            api = YouTubeTranscriptApi()
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
        Deletes a comment or comments from the server based on the specified ID.

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

    def add_comments_mark_as_spam(self, id=None) -> Any:
        """
        Marks a comment as spam by sending a POST request to the API endpoint.

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

    def add_comments_set_moderation_status(
        self, banAuthor=None, id=None, moderationStatus=None
    ) -> Any:
        """
        Sets the moderation status for a comment and optionally bans the author through a POST request to a defined endpoint.

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
        Deletes specified live broadcasts using query parameters to filter requests.

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

    def add_live_broadcasts_bind(
        self,
        id=None,
        onBehalfOfContentOwner=None,
        onBehalfOfContentOwnerChannel=None,
        part=None,
        streamId=None,
    ) -> Any:
        """
        Binds a live broadcast to a stream on YouTube, using specified parameters for authentication and identification.

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

    def add_live_broadcasts_control(
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
        Controls a live broadcast by sending a POST request with specified parameters.

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

    def add_live_broadcasts_transition(
        self,
        broadcastStatus=None,
        id=None,
        onBehalfOfContentOwner=None,
        onBehalfOfContentOwnerChannel=None,
        part=None,
    ) -> Any:
        """
        Transitions a live broadcast to a specified status for a given broadcast ID via API.

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

    def delete_live_chat_bans(self, id=None) -> Any:
        """
        Deletes a live chat ban identified by the specified ID from the server.

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

    def delete_live_chat_messages(self, id=None) -> Any:
        """
        Deletes live chat messages based on the specified message ID.

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
        Deletes a live chat moderator by ID using the specified endpoint.

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
        Deletes specified videos from a video platform using API endpoints.

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

    def get_videos_get_rating(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Retrieves the rating of a video using its ID and optional content owner specification.

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

    def add_videos_rate(self, id=None, rating=None) -> Any:
        """
        Submits a rating for a video on the server using the provided video ID and rating value.

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

    def add_videos_report_abuse(self, onBehalfOfContentOwner=None) -> Any:
        """
        Sends an abuse report for videos via the YouTube API, typically used to flag inappropriate content.

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

    def add_watermarks_set(self, channelId=None, onBehalfOfContentOwner=None) -> Any:
        """
        Sets watermarks on a specified YouTube channel using optional content owner credentials.

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

    def add_watermarks_unset(self, channelId=None, onBehalfOfContentOwner=None) -> Any:
        """
        Removes watermarks from a YouTube channel specified by channel ID.

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
        Retrieve YouTube channel activities based on specified filters and parameters.

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

    def add_channel_banners_insert(
        self, channelId=None, onBehalfOfContentOwner=None
    ) -> Any:
        """
        Inserts a new channel banner for a YouTube channel using the YouTube Data API.

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
        Deletes one or more channel sections from the specified platform using the provided identifiers.

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

    def get_channels(
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
        Retrieves YouTube channels based on specified parameters.

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
        Retrieve YouTube comment threads based on specified filters and pagination parameters.

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
        Retrieves fan funding events based on specified filter criteria.

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

    def get_guecategories(self, hl=None, id=None, part=None, regionCode=None) -> Any:
        """
        Fetches guide categories from a remote service based on specified parameters.

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

    def get_languages(self, hl=None, part=None) -> Any:
        """
        Fetches a list of supported languages from the internationalization API, returning localized names when specified.

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

    def get_regions(self, hl=None, part=None) -> Any:
        """
        Retrieves a list of i18n regions from an API endpoint.

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
        Deletes a YouTube livestream resource using the YouTube Data API with optional filtering parameters.

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

    def delete_play_list_items(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes playlist items identified by the given ID or on behalf of the specified content owner.

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
        Deletes playlists via the YouTube Data API based on specified criteria.

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
        Submits a search query to the YouTube Data API with optional filters.

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

    def get_sponsors(
        self, filter=None, maxResults=None, pageToken=None, part=None
    ) -> Any:
        """
        Fetches a list of sponsors from a server with optional filtering and pagination.

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
        Deletes one or all subscriptions by sending a DELETE request to the API endpoint.

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

    def get_superchatevents(
        self, hl=None, maxResults=None, pageToken=None, part=None
    ) -> Any:
        """
        Fetches a list of super chat events from the YouTube API with optional filtering parameters.

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

    def add_thumbnails_set(self, onBehalfOfContentOwner=None, videoId=None) -> Any:
        """
        Sets a thumbnail for a specified video on behalf of a content owner using the YouTube API.

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
        Fetches video abuse report reasons with optional localization and response filtering.

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

    def get_veocategories(self, hl=None, id=None, part=None, regionCode=None) -> Any:
        """
        Fetches video categories from an external API using specified query parameters and returns the parsed JSON response.

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

    def delete_groupitems(self, id=None, onBehalfOfContentOwner=None) -> Any:
        """
        Deletes group items based on the provided parameters.

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
        Deletes specified groups via API, optionally on behalf of a content owner.

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

    def get_reports(
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
        Fetches and returns report data based on specified filtering, sorting, and range criteria.

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
            self.get_jobs_job_reports,
            self.get_jobs_job_reports_report,
            self.delete_jobs_job,
            self.get_jobs,
            self.get_media_resource_name,
            self.get_reporttypes,
            self.delete_captions,
            self.get_captions,
            self.delete_comments,
            self.add_comments_mark_as_spam,
            self.add_comments_set_moderation_status,
            self.delete_live_broadcasts,
            self.add_live_broadcasts_bind,
            self.add_live_broadcasts_control,
            self.add_live_broadcasts_transition,
            self.delete_live_chat_bans,
            self.delete_live_chat_messages,
            self.delete_live_chat_moderators,
            self.delete_videos,
            self.get_videos_get_rating,
            self.add_videos_rate,
            self.add_videos_report_abuse,
            self.add_watermarks_set,
            self.add_watermarks_unset,
            self.get_activities,
            self.add_channel_banners_insert,
            self.delete_channel_sections,
            self.get_channels,
            self.get_comment_threads,
            self.get_fanfundingevents,
            self.get_guecategories,
            self.get_languages,
            self.get_regions,
            self.delete_livestreams,
            self.delete_play_list_items,
            self.delete_playlists,
            self.get_search,
            self.get_sponsors,
            self.delete_subscriptions,
            self.get_superchatevents,
            self.add_thumbnails_set,
            self.get_video_abuse_report_reasons,
            self.get_veocategories,
            self.delete_groupitems,
            self.delete_groups,
            self.get_reports,
        ]
