from typing import Any
from urllib.parse import quote

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class LinkedinApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """

    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="linkedin", integration=integration, **kwargs)
        self.base_url = "https://api.linkedin.com"

    def _get_headers(self):
        if not self.integration:
            raise ValueError("Integration not found")
        credentials = self.integration.get_credentials()
        if "headers" in credentials:
            return credentials["headers"]
        return {
            "Authorization": f"Bearer {credentials['access_token']}",
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json",
            "LinkedIn-Version": "202507",
        }

    def create_post(
        self,
        commentary: str,
        author: str,
        visibility: str = "PUBLIC",
        distribution: dict[str, Any] | None = None,
        lifecycle_state: str = "PUBLISHED",
        is_reshare_disabled: bool = False,
    ) -> dict[str, str]:
        """
        Publishes a new text post to a specified LinkedIn author's feed (person or organization). It allows configuring visibility, distribution, and lifecycle state. Upon success, it returns the unique URN and URL for the new post, distinguishing this creation operation from the update or delete functions.

        Args:
            commentary (str): The user generated commentary for the post. Supports mentions using format "@[Entity Name](urn:li:organization:123456)" and hashtags using "#keyword". Text linking to annotated entities must match the name exactly (case sensitive). For member mentions, partial name matching is supported.
            author (str): The URN of the author creating the post. Use "urn:li:person:{id}" for individual posts or "urn:li:organization:{id}" for company page posts. Example: "urn:li:person:wGgGaX_xbB" or "urn:li:organization:2414183"
            visibility (str): Controls who can view the post. Use "PUBLIC" for posts viewable by anyone on LinkedIn or "CONNECTIONS" for posts viewable by 1st-degree connections only. Defaults to "PUBLIC".
            distribution (dict[str, Any], optional): Distribution settings for the post. If not provided, defaults to {"feedDistribution": "MAIN_FEED", "targetEntities": [], "thirdPartyDistributionChannels": []}. feedDistribution controls where the post appears in feeds, targetEntities specifies entities to target, and thirdPartyDistributionChannels defines external distribution channels.
            lifecycle_state (str): The state of the post. Use "PUBLISHED" for live posts accessible to all entities, "DRAFT" for posts accessible only to author, "PUBLISH_REQUESTED" for posts submitted but processing, or "PUBLISH_FAILED" for posts that failed to publish. Defaults to "PUBLISHED".
            is_reshare_disabled (bool): Whether resharing is disabled by the author. Set to True to prevent other users from resharing this post, or False to allow resharing. Defaults to False.

        Returns:
            dict[str, str]: Dictionary containing the post ID with key "post_id". Example: {"post_id": "urn:li:share:6844785523593134080"}

        Raises:
            ValueError: If required parameters (commentary, author) are missing or if x-restli-id header is not found
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body

        Notes:
            Requires LinkedIn API permissions: w_member_social (for individual posts) or w_organization_social (for company posts). All requests require headers: X-Restli-Protocol-Version: 2.0.0 and LinkedIn-Version: 202507. Rate limits: 150 requests per day per member, 100,000 requests per day per application. The Posts API replaces the deprecated ugcPosts API.

        Tags:
            posts, important
        """
        # Set default distribution if not provided
        if distribution is None:
            distribution = {
                "feedDistribution": "MAIN_FEED",
                "targetEntities": [],
                "thirdPartyDistributionChannels": [],
            }

        request_body_data = {
            "author": author,
            "commentary": commentary,
            "visibility": visibility,
            "distribution": distribution,
            "lifecycleState": lifecycle_state,
            "isReshareDisabledByAuthor": is_reshare_disabled,
        }

        url = f"{self.base_url}/rest/posts"
        query_params = {}

        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
        )

        self._handle_response(response)

        post_id = response.headers.get("x-restli-id")
        if not post_id:
            raise ValueError("x-restli-id header not found in response")

        return {
            "post_urn": post_id,
            "post_url": f"https://www.linkedin.com/feed/update/{post_id}",
        }

    def get_authenticated_user_profile(self) -> dict[str, Any]:
        """
        Retrieves the authenticated user's profile from the LinkedIn `/v2/userinfo` endpoint. Using credentials from the active integration, it returns a dictionary with basic user details like name and email. This function is for fetching user data, distinct from others that create, update, or delete posts.

        Returns:
            dict[str, Any]: Dictionary containing your LinkedIn profile information.

        Raises:
            ValueError: If integration is not found
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body

        Tags:
            profile, info
        """
        url = f"{self.base_url}/v2/userinfo"
        query_params = {}

        response = self._get(
            url,
            params=query_params,
        )

        return self._handle_response(response)

    def delete_post(self, post_urn: str) -> dict[str, str]:
        """
        Deletes a LinkedIn post identified by its unique Uniform Resource Name (URN). This function sends a DELETE request to the API, permanently removing the content. Upon a successful HTTP 204 response, it returns a dictionary confirming the post's deletion status.

        Args:
            post_urn (str): The URN of the post to delete. Can be either a ugcPostUrn (urn:li:ugcPost:{id}) or shareUrn (urn:li:share:{id}).

        Returns:
            dict[str, str]: Dictionary containing the deletion status. Example: {"status": "deleted", "post_urn": "urn:li:share:6844785523593134080"}

        Raises:
            ValueError: If required parameter (post_urn) is missing or if integration is not found
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body


        Tags:
            posts, important
        """
        url = f"{self.base_url}/rest/posts/{quote(post_urn, safe='')}"
        query_params = {}

        response = self._delete(
            url,
            params=query_params,
        )

        if response.status_code == 204:
            return {"status": "deleted", "post_urn": post_urn}
        else:
            return self._handle_response(response)

    def update_post(
        self,
        post_urn: str,
        commentary: str | None = None,
        content_call_to_action_label: str | None = None,
        content_landing_page: str | None = None,
        lifecycle_state: str | None = None,
        ad_context_name: str | None = None,
        ad_context_status: str | None = None,
    ) -> dict[str, str]:
        """
        Modifies an existing LinkedIn post, identified by its URN, by performing a partial update. It selectively changes attributes like commentary or ad context, distinguishing it from `create_post` which creates new content. Returns a confirmation dictionary upon successful completion.

        Args:
            post_urn (str): The URN of the post to update. Can be either a ugcPostUrn (urn:li:ugcPost:{id}) or shareUrn (urn:li:share:{id}).
            commentary (str | None, optional): The user generated commentary of this post in little format.
            content_call_to_action_label (str | None, optional): The call to action label that a member can act on that opens a landing page.
            content_landing_page (str | None, optional): URL of the landing page.
            lifecycle_state (str | None, optional): The state of the content. Can be DRAFT, PUBLISHED, PUBLISH_REQUESTED, or PUBLISH_FAILED.
            ad_context_name (str | None, optional): Update the name of the sponsored content.
            ad_context_status (str | None, optional): Update the status of the sponsored content.

        Returns:
            dict[str, str]: Dictionary containing the update status. Example: {"status": "updated", "post_urn": "urn:li:share:6844785523593134080"}

        Raises:
            ValueError: If required parameter (post_urn) is missing or if integration is not found
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body




        Tags:
            posts, update, important
        """
        url = f"{self.base_url}/rest/posts/{quote(post_urn, safe='')}"
        query_params = {}

        # Build the patch data
        patch_data = {"$set": {}}
        ad_context_data = {}

        if commentary is not None:
            patch_data["$set"]["commentary"] = commentary
        if content_call_to_action_label is not None:
            patch_data["$set"]["contentCallToActionLabel"] = (
                content_call_to_action_label
            )
        if content_landing_page is not None:
            patch_data["$set"]["contentLandingPage"] = content_landing_page
        if lifecycle_state is not None:
            patch_data["$set"]["lifecycleState"] = lifecycle_state

        if ad_context_name is not None or ad_context_status is not None:
            ad_context_data["$set"] = {}
            if ad_context_name is not None:
                ad_context_data["$set"]["dscName"] = ad_context_name
            if ad_context_status is not None:
                ad_context_data["$set"]["dscStatus"] = ad_context_status
            patch_data["adContext"] = ad_context_data

        request_body_data = {"patch": patch_data}

        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
        )

        if response.status_code == 204:
            return {"status": "updated", "post_urn": post_urn}
        else:
            return self._handle_response(response)

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [
            self.create_post,
            self.get_authenticated_user_profile,
            self.delete_post,
            self.update_post,
        ]
