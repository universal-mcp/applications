from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class TrelloApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="trello", integration=integration, **kwargs)
        self.base_url = "https://api.trello.com/1"

    def get_actions_id(
        self,
        id: str,
        display: bool | None = None,
        entities: bool | None = None,
        fields: str | None = None,
        member: bool | None = None,
        member_fields: str | None = None,
        memberCreator: bool | None = None,
        memberCreator_fields: str | None = None,
    ) -> Any:
        """
        Get an Action

        Args:
            id (string): id
            display (boolean): Determines whether the results should include a visible response or not; defaults to true if not specified.
            entities (boolean): A boolean flag indicating whether to include entities in the response.
            fields (string): `all` or a comma-separated list of action [fields](/cloud/trello/guides/rest-api/object-definitions/#action-object)
            member (boolean): Include this boolean query parameter to filter the action response based on membership status; defaults to true.
            member_fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
            memberCreator (boolean): Whether to include the member object for the creator of the action
            memberCreator_fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            actions, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{id}"
        query_params = {
            k: v
            for k, v in [
                ("display", display),
                ("entities", entities),
                ("fields", fields),
                ("member", member),
                ("member_fields", member_fields),
                ("memberCreator", memberCreator),
                ("memberCreator_fields", memberCreator_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_actions_id(self, id: str, text: str) -> Any:
        """
        Update an Action

        Args:
            id (string): id
            text (string): The new text for the comment

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/actions/{id}"
        query_params = {k: v for k, v in [("text", text)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_actions_id(self, id: str) -> Any:
        """
        Delete an Action

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_actions_id_field(self, id: str, field: str) -> dict[str, Any]:
        """
        Get a specific field on an Action

        Args:
            id (string): id
            field (string): field

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        url = f"{self.base_url}/actions/{id}/{field}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_actions_id_board(
        self, id: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get the Board for an Action

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of board fields

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{id}/board"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_actions_id_card(self, id: str, fields: str | None = None) -> dict[str, Any]:
        """
        Get the Card for an Action

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of card fields

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{id}/card"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_actions_id_list(self, id: str, fields: str | None = None) -> dict[str, Any]:
        """
        Get the List for an Action

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of list fields

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{id}/list"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_actions_id_member(
        self, id: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get the Member of an Action

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of member fields

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{id}/member"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_actions_id_membercreator(
        self, id: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get the Member Creator of an Action

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of member fields

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{id}/memberCreator"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_actions_id_organization(
        self, id: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get the Organization of an Action

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of organization fields

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{id}/organization"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_actions_id_text(self, id: str, value: str) -> Any:
        """
        Update a Comment Action

        Args:
            id (string): id
            value (string): The new text for the comment

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/actions/{id}/text"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_actions_idaction_reactions(
        self, idAction: str, member: bool | None = None, emoji: bool | None = None
    ) -> Any:
        """
        Get Action's Reactions

        Args:
            idAction (string): idAction
            member (boolean): Whether to load the member as a nested resource. See [Members Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#members-nested-resource)
            emoji (boolean): Whether to load the emoji as a nested resource.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idAction is None:
            raise ValueError("Missing required parameter 'idAction'.")
        url = f"{self.base_url}/actions/{idAction}/reactions"
        query_params = {
            k: v for k, v in [("member", member), ("emoji", emoji)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_reaction_to_action(
        self,
        idAction: str,
        shortName: str | None = None,
        skinVariation: str | None = None,
        native: str | None = None,
        unified: str | None = None,
    ) -> Any:
        """
        Create Reaction for Action

        Args:
            idAction (string): idAction
            shortName (string): The primary `shortName` of the emoji to add. See [/emoji](#emoji)
            skinVariation (string): The `skinVariation` of the emoji to add. See [/emoji](#emoji)
            native (string): The emoji to add as a native unicode emoji. See [/emoji](#emoji)
            unified (string): The `unified` value of the emoji to add. See [/emoji](#emoji)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idAction is None:
            raise ValueError("Missing required parameter 'idAction'.")
        request_body_data = None
        request_body_data = {
            "shortName": shortName,
            "skinVariation": skinVariation,
            "native": native,
            "unified": unified,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/actions/{idAction}/reactions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_action_reaction_by_id(
        self,
        idAction: str,
        id: str,
        member: bool | None = None,
        emoji: bool | None = None,
    ) -> Any:
        """
        Get Action's Reaction

        Args:
            idAction (string): idAction
            id (string): id
            member (boolean): Whether to load the member as a nested resource. See [Members Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#members-nested-resource)
            emoji (boolean): Whether to load the emoji as a nested resource.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idAction is None:
            raise ValueError("Missing required parameter 'idAction'.")
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{idAction}/reactions/{id}"
        query_params = {
            k: v for k, v in [("member", member), ("emoji", emoji)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_reaction_by_id_action(self, idAction: str, id: str) -> Any:
        """
        Delete Action's Reaction

        Args:
            idAction (string): idAction
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idAction is None:
            raise ValueError("Missing required parameter 'idAction'.")
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/actions/{idAction}/reactions/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_action_reactions_summary(self, idAction: str) -> Any:
        """
        List Action's summary of Reactions

        Args:
            idAction (string): idAction

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idAction is None:
            raise ValueError("Missing required parameter 'idAction'.")
        url = f"{self.base_url}/actions/{idAction}/reactionsSummary"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def applications_key_compliance(self, key: str) -> Any:
        """
        Get Application's compliance data

        Args:
            key (string): key

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if key is None:
            raise ValueError("Missing required parameter 'key'.")
        url = f"{self.base_url}/applications/{key}/compliance"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_batch(self, urls: str) -> Any:
        """
        Batch Requests

        Args:
            urls (string): A list of API routes. Maximum of 10 routes allowed. The routes should begin with a forward slash and should not include the API version number - e.g. "urls=/members/trello,/cards/[cardId]"

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        url = f"{self.base_url}/batch"
        query_params = {k: v for k, v in [("urls", urls)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_memberships(
        self,
        id: str,
        filter: str | None = None,
        activity: bool | None = None,
        orgMemberType: bool | None = None,
        member: bool | None = None,
        member_fields: str | None = None,
    ) -> dict[str, Any]:
        """
        Get Memberships of a Board

        Args:
            id (string): id
            filter (string): One of `admins`, `all`, `none`, `normal`
            activity (boolean): Works for premium organizations only.
            orgMemberType (boolean): Shows the type of member to the org the user is. For instance, an org admin will have a `orgMemberType` of `admin`.
            member (boolean): Determines whether to include a [nested member object](/cloud/trello/guides/rest-api/nested-resources/).
            member_fields (string): Fields to show if `member=true`. Valid values: [nested member resource fields](/cloud/trello/guides/rest-api/nested-resources/).

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/memberships"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("activity", activity),
                ("orgMemberType", orgMemberType),
                ("member", member),
                ("member_fields", member_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id(
        self,
        id: str,
        actions: str | None = None,
        boardStars: str | None = None,
        cards: str | None = None,
        card_pluginData: bool | None = None,
        checklists: str | None = None,
        customFields: bool | None = None,
        fields: str | None = None,
        labels: str | None = None,
        lists: str | None = None,
        members: str | None = None,
        memberships: str | None = None,
        pluginData: bool | None = None,
        organization: bool | None = None,
        organization_pluginData: bool | None = None,
        myPrefs: bool | None = None,
        tags: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get a Board

        Args:
            id (string): id
            actions (string): This is a nested resource. Read more about actions as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/).
            boardStars (string): Valid values are one of: `mine` or `none`.
            cards (string): This is a nested resource. Read more about cards as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/).
            card_pluginData (boolean): Use with the `cards` param to include card pluginData with the response
            checklists (string): This is a nested resource. Read more about checklists as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/).
            customFields (boolean): This is a nested resource. Read more about custom fields as nested resources [here](#custom-fields-nested-resource).
            fields (string): The fields of the board to be included in the response. Valid values: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url
            labels (string): This is a nested resource. Read more about labels as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/).
            lists (string): This is a nested resource. Read more about lists as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/).
            members (string): This is a nested resource. Read more about members as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/).
            memberships (string): This is a nested resource. Read more about memberships as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/).
            pluginData (boolean): Determines whether the pluginData for this board should be returned. Valid values: true or false.
            organization (boolean): This is a nested resource. Read more about organizations as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/).
            organization_pluginData (boolean): Use with the `organization` param to include organization pluginData with the response
            myPrefs (boolean): Indicates whether to include the current user’s preferences for the specified board (default is false).
            tags (boolean): Also known as collections, tags, refer to the collection(s) that a Board belongs to.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}"
        query_params = {
            k: v
            for k, v in [
                ("actions", actions),
                ("boardStars", boardStars),
                ("cards", cards),
                ("card_pluginData", card_pluginData),
                ("checklists", checklists),
                ("customFields", customFields),
                ("fields", fields),
                ("labels", labels),
                ("lists", lists),
                ("members", members),
                ("memberships", memberships),
                ("pluginData", pluginData),
                ("organization", organization),
                ("organization_pluginData", organization_pluginData),
                ("myPrefs", myPrefs),
                ("tags", tags),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_boards_id(
        self,
        id: str,
        name: str | None = None,
        desc: str | None = None,
        closed: bool | None = None,
        subscribed: str | None = None,
        idOrganization: str | None = None,
        prefs_permissionLevel: str | None = None,
        prefs_selfJoin: bool | None = None,
        prefs_cardCovers: bool | None = None,
        prefs_hideVotes: bool | None = None,
        prefs_invitations: str | None = None,
        prefs_voting: str | None = None,
        prefs_comments: str | None = None,
        prefs_background: str | None = None,
        prefs_cardAging: str | None = None,
        prefs_calendarFeedEnabled: bool | None = None,
        labelNames_green: str | None = None,
        labelNames_yellow: str | None = None,
        labelNames_orange: str | None = None,
        labelNames_red: str | None = None,
        labelNames_purple: str | None = None,
        labelNames_blue: str | None = None,
    ) -> Any:
        """
        Update a Board

        Args:
            id (string): id
            name (string): The new name for the board. 1 to 16384 characters long.
            desc (string): A new description for the board, 0 to 16384 characters long
            closed (boolean): Whether the board is closed
            subscribed (string): Whether the acting user is subscribed to the board Example: '5abbe4b7ddc1b351ef961414'.
            idOrganization (string): The id of the Workspace the board should be moved to
            prefs_permissionLevel (string): One of: org, private, public
            prefs_selfJoin (boolean): Whether Workspace members can join the board themselves
            prefs_cardCovers (boolean): Whether card covers should be displayed on this board
            prefs_hideVotes (boolean): Determines whether the Voting Power-Up should hide who voted on cards or not.
            prefs_invitations (string): Who can invite people to this board. One of: admins, members
            prefs_voting (string): Who can vote on this board. One of disabled, members, observers, org, public
            prefs_comments (string): Who can comment on cards on this board. One of: disabled, members, observers, org, public
            prefs_background (string): The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey
            prefs_cardAging (string): One of: pirate, regular
            prefs_calendarFeedEnabled (boolean): Determines whether the calendar feed is enabled or not.
            labelNames_green (string): Name for the green label. 1 to 16384 characters long
            labelNames_yellow (string): Name for the yellow label. 1 to 16384 characters long
            labelNames_orange (string): Name for the orange label. 1 to 16384 characters long
            labelNames_red (string): Name for the red label. 1 to 16384 characters long
            labelNames_purple (string): Name for the purple label. 1 to 16384 characters long
            labelNames_blue (string): Name for the blue label. 1 to 16384 characters long

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("desc", desc),
                ("closed", closed),
                ("subscribed", subscribed),
                ("idOrganization", idOrganization),
                ("prefs/permissionLevel", prefs_permissionLevel),
                ("prefs/selfJoin", prefs_selfJoin),
                ("prefs/cardCovers", prefs_cardCovers),
                ("prefs/hideVotes", prefs_hideVotes),
                ("prefs/invitations", prefs_invitations),
                ("prefs/voting", prefs_voting),
                ("prefs/comments", prefs_comments),
                ("prefs/background", prefs_background),
                ("prefs/cardAging", prefs_cardAging),
                ("prefs/calendarFeedEnabled", prefs_calendarFeedEnabled),
                ("labelNames/green", labelNames_green),
                ("labelNames/yellow", labelNames_yellow),
                ("labelNames/orange", labelNames_orange),
                ("labelNames/red", labelNames_red),
                ("labelNames/purple", labelNames_purple),
                ("labelNames/blue", labelNames_blue),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_boards_id(self, id: str) -> Any:
        """
        Delete a Board

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_field(self, id: str, field: str) -> Any:
        """
        Get a field on a Board

        Args:
            id (string): id
            field (string): field

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        url = f"{self.base_url}/boards/{id}/{field}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_actions(
        self,
        boardId: str,
        fields: dict[str, Any] | None = None,
        filter: str | None = None,
        format: str | None = None,
        idModels: str | None = None,
        limit: float | None = None,
        member: bool | None = None,
        member_fields: str | None = None,
        memberCreator: bool | None = None,
        memberCreator_fields: str | None = None,
        page: float | None = None,
        reactions: bool | None = None,
        before: str | None = None,
        since: str | None = None,
    ) -> Any:
        """
        Get Actions of a Board

        Args:
            boardId (string): boardId
            fields (object): The fields to be returned for the Actions. [See Action fields here](/cloud/trello/guides/rest-api/object-definitions/#action-object).
            filter (string): A comma-separated list of [action types](/cloud/trello/guides/rest-api/action-types/).
            format (string): The format of the returned Actions. Either list or count.
            idModels (string): A comma-separated list of idModels. Only actions related to these models will be returned.
            limit (number): The limit of the number of responses, between 0 and 1000.
            member (boolean): Whether to return the member object for each action.
            member_fields (string): The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) to return.
            memberCreator (boolean): Whether to return the memberCreator object for each action.
            memberCreator_fields (string): The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) creator to return
            page (number): The page of results for actions.
            reactions (boolean): Whether to show reactions on comments or not.
            before (string): A date string in the form of YYYY-MM-DDThh:mm:ssZ or a mongo object ID. Only objects created before this date will be returned.
            since (string): A date string in the form of YYYY-MM-DDThh:mm:ssZ or a mongo object ID. Only objects created since this date will be returned.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if boardId is None:
            raise ValueError("Missing required parameter 'boardId'.")
        url = f"{self.base_url}/boards/{boardId}/actions"
        query_params = {
            k: v
            for k, v in [
                ("fields", fields),
                ("filter", filter),
                ("format", format),
                ("idModels", idModels),
                ("limit", limit),
                ("member", member),
                ("member_fields", member_fields),
                ("memberCreator", memberCreator),
                ("memberCreator_fields", memberCreator_fields),
                ("page", page),
                ("reactions", reactions),
                ("before", before),
                ("since", since),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_boardstars(
        self, boardId: str, filter: str | None = None
    ) -> list[Any]:
        """
        Get boardStars on a Board

        Args:
            boardId (string): boardId
            filter (string): Valid values: mine, none

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if boardId is None:
            raise ValueError("Missing required parameter 'boardId'.")
        url = f"{self.base_url}/boards/{boardId}/boardStars"
        query_params = {k: v for k, v in [("filter", filter)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def boards_id_checklists(self, id: str) -> Any:
        """
        Get Checklists on a Board

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/checklists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_cards(self, id: str) -> Any:
        """
        Get Cards on a Board

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/cards"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_cards_filter(self, id: str, filter: str) -> Any:
        """
        Get filtered Cards on a Board

        Args:
            id (string): id
            filter (string): filter

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if filter is None:
            raise ValueError("Missing required parameter 'filter'.")
        url = f"{self.base_url}/boards/{id}/cards/{filter}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_customfields(self, id: str) -> list[Any]:
        """
        Get Custom Fields for Board

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/customFields"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_labels(
        self,
        id: str,
        fields: dict[str, Any] | None = None,
        limit: int | None = None,
    ) -> Any:
        """
        Get Labels on a Board

        Args:
            id (string): id
            fields (object): The fields to be returned for the Labels.
            limit (integer): The number of Labels to be returned.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/labels"
        query_params = {
            k: v for k, v in [("fields", fields), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_boards_id_labels(self, id: str, name: str, color: str) -> Any:
        """
        Create a Label on a Board

        Args:
            id (string): id
            name (string): The name of the label to be created. 1 to 16384 characters long.
            color (string): Sets the color of the new label. Valid values are a label color or `null`.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/labels"
        query_params = {
            k: v for k, v in [("name", name), ("color", color)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_lists(
        self,
        id: str,
        cards: str | None = None,
        card_fields: str | None = None,
        filter: str | None = None,
        fields: str | None = None,
    ) -> list[Any]:
        """
        Get Lists on a Board

        Args:
            id (string): id
            cards (string): Filter to apply to Cards.
            card_fields (string): `all` or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/#card-object)
            filter (string): Filter to apply to Lists
            fields (string): `all` or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/lists"
        query_params = {
            k: v
            for k, v in [
                ("cards", cards),
                ("card_fields", card_fields),
                ("filter", filter),
                ("fields", fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_boards_id_lists(
        self, id: str, name: str, pos: str | None = None
    ) -> dict[str, Any]:
        """
        Create a List on a Board

        Args:
            id (string): id
            name (string): The name of the list to be created. 1 to 16384 characters long.
            pos (string): Determines the position of the list. Valid values: `top`, `bottom`, or a positive number.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/lists"
        query_params = {
            k: v for k, v in [("name", name), ("pos", pos)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_lists_filter(self, id: str, filter: str) -> Any:
        """
        Get filtered Lists on a Board

        Args:
            id (string): id
            filter (string): filter

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if filter is None:
            raise ValueError("Missing required parameter 'filter'.")
        url = f"{self.base_url}/boards/{id}/lists/{filter}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_members(self, id: str) -> Any:
        """
        Get the Members of a Board

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/members"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_boards_id_members(
        self,
        id: str,
        email: str,
        type: str | None = None,
        fullName: str | None = None,
    ) -> Any:
        """
        Invite Member to Board via email

        Args:
            id (string): id
            email (string): The email address of a user to add as a member of the board.
            type (string): Valid values: admin, normal, observer. Determines what type of member the user being added should be of the board.
            fullName (string): The full name of the user to as a member of the board. Must have a length of at least 1 and cannot begin nor end with a space.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "fullName": fullName,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/boards/{id}/members"
        query_params = {
            k: v for k, v in [("email", email), ("type", type)] if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_boards_id_members_idmember(
        self,
        id: str,
        idMember: str,
        type: str,
        allowBillableGuest: bool | None = None,
    ) -> Any:
        """
        Add a Member to a Board

        Args:
            id (string): id
            idMember (string): idMember
            type (string): One of: admin, normal, observer. Determines the type of member this user will be on the board.
            allowBillableGuest (boolean): Optional param that allows organization admins to add multi-board guests onto a board.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/members/{idMember}"
        query_params = {
            k: v
            for k, v in [("type", type), ("allowBillableGuest", allowBillableGuest)]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def boardsidmembersidmember(self, id: str, idMember: str) -> Any:
        """
        Remove Member from Board

        Args:
            id (string): id
            idMember (string): idMember

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        url = f"{self.base_url}/boards/{id}/members/{idMember}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_membership(
        self, id: str, idMembership: str, type: str, member_fields: str | None = None
    ) -> Any:
        """
        Update Membership of Member on a Board

        Args:
            id (string): id
            idMembership (string): idMembership
            type (string): One of: admin, normal, observer. Determines the type of member that this membership will be to this board.
            member_fields (string): Valid values: all, avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMembership is None:
            raise ValueError("Missing required parameter 'idMembership'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/memberships/{idMembership}"
        query_params = {
            k: v
            for k, v in [("type", type), ("member_fields", member_fields)]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_board_email_position(self, id: str, value: str) -> Any:
        """
        Update emailPosition Pref on a Board

        Args:
            id (string): id
            value (string): Valid values: bottom, top. Determines the position of the email address.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/myPrefs/emailPosition"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_board_my_prefs_id_email_list(self, id: str, value: str) -> Any:
        """
        Update idEmailList Pref on a Board

        Args:
            id (string): id
            value (string): The id of an email list. Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/myPrefs/idEmailList"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_board_sidebar_pref(self, id: str, value: bool) -> Any:
        """
        Update showSidebar Pref on a Board

        Args:
            id (string): id
            value (boolean): Determines whether to show the side bar.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/myPrefs/showSidebar"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_board_sidebar_act_pref(self, id: str, value: bool) -> Any:
        """
        Update showSidebarActivity Pref on a Board

        Args:
            id (string): id
            value (boolean): Determines whether to show sidebar activity.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/myPrefs/showSidebarActivity"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_board_sidebar_actions(self, id: str, value: bool) -> Any:
        """
        Update showSidebarBoardActions Pref on a Board

        Args:
            id (string): id
            value (boolean): Determines whether to show the sidebar board actions.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/myPrefs/showSidebarBoardActions"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_board_prefs_show_members(self, id: str, value: bool) -> Any:
        """
        Update showSidebarMembers Pref on a Board

        Args:
            id (string): id
            value (boolean): Determines whether to show members of the board in the sidebar.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/myPrefs/showSidebarMembers"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_boards(
        self,
        name: str,
        defaultLabels: bool | None = None,
        defaultLists: bool | None = None,
        desc: str | None = None,
        idOrganization: str | None = None,
        idBoardSource: str | None = None,
        keepFromSource: str | None = None,
        powerUps: str | None = None,
        prefs_permissionLevel: str | None = None,
        prefs_voting: str | None = None,
        prefs_comments: str | None = None,
        prefs_invitations: str | None = None,
        prefs_selfJoin: bool | None = None,
        prefs_cardCovers: bool | None = None,
        prefs_background: str | None = None,
        prefs_cardAging: str | None = None,
    ) -> Any:
        """
        Create a Board

        Args:
            name (string): The new name for the board. 1 to 16384 characters long.
            defaultLabels (boolean): Determines whether to use the default set of labels.
            defaultLists (boolean): Determines whether to add the default set of lists to a board (To Do, Doing, Done). It is ignored if `idBoardSource` is provided.
            desc (string): A new description for the board, 0 to 16384 characters long
            idOrganization (string): The id or name of the Workspace the board should belong to. Example: '5abbe4b7ddc1b351ef961414'.
            idBoardSource (string): The id of a board to copy into the new board. Example: '5abbe4b7ddc1b351ef961414'.
            keepFromSource (string): To keep cards from the original board pass in the value `cards`
            powerUps (string): The Power-Ups that should be enabled on the new board. One of: `all`, `calendar`, `cardAging`, `recap`, `voting`.
            prefs_permissionLevel (string): The permissions level of the board. One of: `org`, `private`, `public`.
            prefs_voting (string): Who can vote on this board. One of `disabled`, `members`, `observers`, `org`, `public`.
            prefs_comments (string): Who can comment on cards on this board. One of: `disabled`, `members`, `observers`, `org`, `public`.
            prefs_invitations (string): Determines what types of members can invite users to join. One of: `admins`, `members`.
            prefs_selfJoin (boolean): Determines whether users can join the boards themselves or whether they have to be invited.
            prefs_cardCovers (boolean): Determines whether card covers are enabled.
            prefs_background (string): The id of a custom background or one of: `blue`, `orange`, `green`, `red`, `purple`, `pink`, `lime`, `sky`, `grey`.
            prefs_cardAging (string): Determines the type of card aging that should take place on the board if card aging is enabled. One of: `pirate`, `regular`.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/boards/"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("defaultLabels", defaultLabels),
                ("defaultLists", defaultLists),
                ("desc", desc),
                ("idOrganization", idOrganization),
                ("idBoardSource", idBoardSource),
                ("keepFromSource", keepFromSource),
                ("powerUps", powerUps),
                ("prefs_permissionLevel", prefs_permissionLevel),
                ("prefs_voting", prefs_voting),
                ("prefs_comments", prefs_comments),
                ("prefs_invitations", prefs_invitations),
                ("prefs_selfJoin", prefs_selfJoin),
                ("prefs_cardCovers", prefs_cardCovers),
                ("prefs_background", prefs_background),
                ("prefs_cardAging", prefs_cardAging),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def generate_calendar_key(self, id: str) -> Any:
        """
        Create a calendarKey for a Board

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/calendarKey/generate"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def generate_board_email_key(self, id: str) -> Any:
        """
        Create a emailKey for a Board

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/emailKey/generate"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_boards_id_idtags(self, id: str, value: str) -> Any:
        """
        Create a Tag for a Board

        Args:
            id (string): id
            value (string): The id of a tag from the organization to which this board belongs. Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/idTags"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_boards_id_markedasviewed(self, id: str) -> Any:
        """
        Mark Board as viewed

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/markedAsViewed"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_boards_id_boardplugins(self, id: str) -> list[Any]:
        """
        Get Enabled Power-Ups on Board

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/boardPlugins"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_boards_id_boardplugins(self, id: str, idPlugin: str | None = None) -> Any:
        """
        Enable a Power-Up on a Board

        Args:
            id (string): id
            idPlugin (string): The ID of the Power-Up to enable Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/boards/{id}/boardPlugins"
        query_params = {k: v for k, v in [("idPlugin", idPlugin)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_boards_id_boardplugins(self, id: str, idPlugin: str) -> Any:
        """
        Disable a Power-Up on a Board

        Args:
            id (string): id
            idPlugin (string): idPlugin

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idPlugin is None:
            raise ValueError("Missing required parameter 'idPlugin'.")
        url = f"{self.base_url}/boards/{id}/boardPlugins/{idPlugin}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_board_id_plugins(
        self, id: str, filter: str | None = None
    ) -> dict[str, Any]:
        """
        Get Power-Ups on a Board

        Args:
            id (string): id
            filter (string): One of: `enabled` or `available`

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/boards/{id}/plugins"
        query_params = {k: v for k, v in [("filter", filter)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_cards(
        self,
        idList: str,
        name: str | None = None,
        desc: str | None = None,
        pos: Any | None = None,
        due: str | None = None,
        start: str | None = None,
        dueComplete: bool | None = None,
        idMembers: list[Any] | None = None,
        idLabels: list[Any] | None = None,
        urlSource: str | None = None,
        fileSource: bytes | None = None,
        mimeType: str | None = None,
        idCardSource: str | None = None,
        keepFromSource: str | None = None,
        address: str | None = None,
        locationName: str | None = None,
        coordinates: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a new Card

        Args:
            idList (string): The ID of the list the card should be created in Example: '5abbe4b7ddc1b351ef961414'.
            name (string): The name for the card
            desc (string): The description for the card
            pos (string): The position of the new card. `top`, `bottom`, or a positive float
            due (string): A due date for the card
            start (string): The start date of a card, or `null`
            dueComplete (boolean): Whether the status of the card is complete
            idMembers (array): Comma-separated list of member IDs to add to the card
            idLabels (array): Comma-separated list of label IDs to add to the card
            urlSource (string): A URL starting with ` or ` The URL will be attached to the card upon creation.
            fileSource (string): Optional query parameter specifying the source file for the operation.
            mimeType (string): The mimeType of the attachment. Max length 256
            idCardSource (string): The ID of a card to copy into the new card Example: '5abbe4b7ddc1b351ef961414'.
            keepFromSource (string): If using `idCardSource` you can specify which properties to copy over. `all` or comma-separated list of: `attachments,checklists,customFields,comments,due,start,labels,members,start,stickers`
            address (string): For use with/by the Map View
            locationName (string): For use with/by the Map View
            coordinates (string): For use with/by the Map View. Should take the form latitude,longitude

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/cards"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("desc", desc),
                ("pos", pos),
                ("due", due),
                ("start", start),
                ("dueComplete", dueComplete),
                ("idList", idList),
                ("idMembers", idMembers),
                ("idLabels", idLabels),
                ("urlSource", urlSource),
                ("fileSource", fileSource),
                ("mimeType", mimeType),
                ("idCardSource", idCardSource),
                ("keepFromSource", keepFromSource),
                ("address", address),
                ("locationName", locationName),
                ("coordinates", coordinates),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id(
        self,
        id: str,
        fields: str | None = None,
        actions: str | None = None,
        attachments: str | None = None,
        attachment_fields: str | None = None,
        members: bool | None = None,
        member_fields: str | None = None,
        membersVoted: bool | None = None,
        memberVoted_fields: str | None = None,
        checkItemStates: bool | None = None,
        checklists: str | None = None,
        checklist_fields: str | None = None,
        board: bool | None = None,
        board_fields: str | None = None,
        list: bool | None = None,
        pluginData: bool | None = None,
        stickers: bool | None = None,
        sticker_fields: str | None = None,
        customFieldItems: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get a Card

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `badges, checkItemStates, closed, dateLastActivity, desc, descData, due, start, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl, url`
            actions (string): See the [Actions Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#actions-nested-resource)
            attachments (string): `true`, `false`, or `cover`
            attachment_fields (string): `all` or a comma-separated list of attachment [fields](/cloud/trello/guides/rest-api/object-definitions/)
            members (boolean): Whether to return member objects for members on the card
            member_fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `avatarHash, fullName, initials, username`
            membersVoted (boolean): Whether to return member objects for members who voted on the card
            memberVoted_fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `avatarHash, fullName, initials, username`
            checkItemStates (boolean): Optional boolean parameter to indicate whether to check the states of items associated with the card.
            checklists (string): Whether to return the checklists on the card. `all` or `none`
            checklist_fields (string): `all` or a comma-separated list of `idBoard,idCard,name,pos`
            board (boolean): Whether to return the board object the card is on
            board_fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object). **Defaults**: `name, desc, descData, closed, idOrganization, pinned, url, prefs`
            list (boolean): See the [Lists Nested Resource](/cloud/trello/guides/rest-api/nested-resources/)
            pluginData (boolean): Whether to include pluginData on the card with the response
            stickers (boolean): Whether to include sticker models with the response
            sticker_fields (string): `all` or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/)
            customFieldItems (boolean): Whether to include the customFieldItems

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields", fields),
                ("actions", actions),
                ("attachments", attachments),
                ("attachment_fields", attachment_fields),
                ("members", members),
                ("member_fields", member_fields),
                ("membersVoted", membersVoted),
                ("memberVoted_fields", memberVoted_fields),
                ("checkItemStates", checkItemStates),
                ("checklists", checklists),
                ("checklist_fields", checklist_fields),
                ("board", board),
                ("board_fields", board_fields),
                ("list", list),
                ("pluginData", pluginData),
                ("stickers", stickers),
                ("sticker_fields", sticker_fields),
                ("customFieldItems", customFieldItems),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_cards_id(
        self,
        id: str,
        name: str | None = None,
        desc: str | None = None,
        closed: bool | None = None,
        idMembers: str | None = None,
        idAttachmentCover: str | None = None,
        idList: str | None = None,
        idLabels: str | None = None,
        idBoard: str | None = None,
        pos: Any | None = None,
        due: str | None = None,
        start: str | None = None,
        dueComplete: bool | None = None,
        subscribed: bool | None = None,
        address: str | None = None,
        locationName: str | None = None,
        coordinates: str | None = None,
        cover: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update a Card

        Args:
            id (string): id
            name (string): The new name for the card
            desc (string): The new description for the card
            closed (boolean): Whether the card should be archived (closed: true)
            idMembers (string): Comma-separated list of member IDs Example: '5abbe4b7ddc1b351ef961414'.
            idAttachmentCover (string): The ID of the image attachment the card should use as its cover, or null for none Example: '5abbe4b7ddc1b351ef961414'.
            idList (string): The ID of the list the card should be in Example: '5abbe4b7ddc1b351ef961414'.
            idLabels (string): Comma-separated list of label IDs Example: '5abbe4b7ddc1b351ef961414'.
            idBoard (string): The ID of the board the card should be on Example: '5abbe4b7ddc1b351ef961414'.
            pos (string): The position of the card in its list. `top`, `bottom`, or a positive float
            due (string): When the card is due, or `null`
            start (string): The start date of a card, or `null`
            dueComplete (boolean): Whether the status of the card is complete
            subscribed (boolean): Whether the member is should be subscribed to the card
            address (string): For use with/by the Map View
            locationName (string): For use with/by the Map View
            coordinates (string): For use with/by the Map View. Should be latitude,longitude
            cover (object): Updates the card's cover | Option | Values | About | |--------|--------|-------| | color | `pink`, `yellow`, `lime`, `blue`, `black`, `orange`, `red`, `purple`, `sky`, `green` | Makes the cover a solid color . | | brightness | `dark`, `light` | Determines whether the text on the cover should be dark or light. | url | An unsplash URL: | Used if making an image the cover. Only Unsplash URLs work. | idAttachment | ID of an attachment on the card | Used if setting an attached image as the cover. | | size | `normal`, `full` | Determines whether to show the card name on the cover, or below it. | `brightness` can be sent alongside any of the other parameters, but all of the other parameters are mutually exclusive; you can not have the cover be a `color` and an `idAttachment` at the same time. On the brightness options, setting it to light will make the text on the card cover dark: ![](/cloud/trello/images/rest/cards/cover-brightness-dark.png) And vice versa, setting it to dark will make the text on the card cover light: ![](/cloud/trello/images/rest/cards/cover-brightness-light.png)

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("desc", desc),
                ("closed", closed),
                ("idMembers", idMembers),
                ("idAttachmentCover", idAttachmentCover),
                ("idList", idList),
                ("idLabels", idLabels),
                ("idBoard", idBoard),
                ("pos", pos),
                ("due", due),
                ("start", start),
                ("dueComplete", dueComplete),
                ("subscribed", subscribed),
                ("address", address),
                ("locationName", locationName),
                ("coordinates", coordinates),
                ("cover", cover),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_cards_id(self, id: str) -> Any:
        """
        Delete a Card

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_field(self, id: str, field: str) -> dict[str, Any]:
        """
        Get a field on a Card

        Args:
            id (string): id
            field (string): field

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        url = f"{self.base_url}/cards/{id}/{field}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_actions(
        self, id: str, filter: str | None = None, page: float | None = None
    ) -> list[Any]:
        """
        Get Actions on a Card

        Args:
            id (string): id
            filter (string): A comma-separated list of [action types](
            page (number): The page of results for actions. Each page of results has 50 actions.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/actions"
        query_params = {
            k: v for k, v in [("filter", filter), ("page", page)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_attachments(
        self, id: str, fields: str | None = None, filter: str | None = None
    ) -> list[Any]:
        """
        Get Attachments on a Card

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of attachment [fields](/cloud/trello/guides/rest-api/object-definitions/)
            filter (string): Use `cover` to restrict to just the cover attachment

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/attachments"
        query_params = {
            k: v for k, v in [("fields", fields), ("filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_cards_id_attachments(
        self,
        id: str,
        name: str | None = None,
        file: bytes | None = None,
        mimeType: str | None = None,
        url: str | None = None,
        setCover: bool | None = None,
    ) -> list[Any]:
        """
        Create Attachment On Card

        Args:
            id (string): id
            name (string): The name of the attachment. Max length 256.
            file (string): The file to attach, as multipart/form-data
            mimeType (string): The mimeType of the attachment. Max length 256
            url (string): A URL to attach. Must start with ` or `
            setCover (boolean): Determines whether to use the new attachment as a cover for the Card.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("file", file),
                ("mimeType", mimeType),
                ("url", url),
                ("setCover", setCover),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_attachment_by_id(
        self, id: str, idAttachment: str, fields: list[Any] | None = None
    ) -> list[Any]:
        """
        Get an Attachment on a Card

        Args:
            id (string): id
            idAttachment (string): idAttachment
            fields (array): The Attachment fields to be included in the response.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idAttachment is None:
            raise ValueError("Missing required parameter 'idAttachment'.")
        url = f"{self.base_url}/cards/{id}/attachments/{idAttachment}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_attachment_by_id(self, id: str, idAttachment: str) -> Any:
        """
        Delete an Attachment on a Card

        Args:
            id (string): id
            idAttachment (string): idAttachment

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idAttachment is None:
            raise ValueError("Missing required parameter 'idAttachment'.")
        url = f"{self.base_url}/cards/{id}/attachments/{idAttachment}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_board(self, id: str, fields: str | None = None) -> Any:
        """
        Get the Board the Card is on

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/board"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_checkitemstates(self, id: str, fields: str | None = None) -> Any:
        """
        Get checkItems on a Card

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of: `idCheckItem`, `state`

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/checkItemStates"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_checklists(
        self,
        id: str,
        checkItems: str | None = None,
        checkItem_fields: str | None = None,
        filter: str | None = None,
        fields: str | None = None,
    ) -> Any:
        """
        Get Checklists on a Card

        Args:
            id (string): id
            checkItems (string): `all` or `none`
            checkItem_fields (string): `all` or a comma-separated list of: `name,nameData,pos,state,type,due,dueReminder,idMember`
            filter (string): `all` or `none`
            fields (string): `all` or a comma-separated list of: `idBoard,idCard,name,pos`

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/checklists"
        query_params = {
            k: v
            for k, v in [
                ("checkItems", checkItems),
                ("checkItem_fields", checkItem_fields),
                ("filter", filter),
                ("fields", fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_cards_id_checklists(
        self,
        id: str,
        name: str | None = None,
        idChecklistSource: str | None = None,
        pos: str | None = None,
    ) -> Any:
        """
        Create Checklist on a Card

        Args:
            id (string): id
            name (string): The name of the checklist
            idChecklistSource (string): The ID of a source checklist to copy into the new one Example: '5abbe4b7ddc1b351ef961414'.
            pos (string): The position of the checklist on the card. One of: `top`, `bottom`, or a positive number.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/checklists"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("idChecklistSource", idChecklistSource),
                ("pos", pos),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def check_card_item(
        self, id: str, idCheckItem: str, fields: str | None = None
    ) -> Any:
        """
        Get checkItem on a Card

        Args:
            id (string): id
            idCheckItem (string): idCheckItem
            fields (string): `all` or a comma-separated list of `name,nameData,pos,state,type,due,dueReminder,idMember`

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            card, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idCheckItem is None:
            raise ValueError("Missing required parameter 'idCheckItem'.")
        url = f"{self.base_url}/cards/{id}/checkItem/{idCheckItem}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_card_check_item(
        self,
        id: str,
        idCheckItem: str,
        name: str | None = None,
        state: str | None = None,
        idChecklist: str | None = None,
        pos: Any | None = None,
        due: str | None = None,
        dueReminder: float | None = None,
        idMember: str | None = None,
    ) -> Any:
        """
        Update a checkItem on a Card

        Args:
            id (string): id
            idCheckItem (string): idCheckItem
            name (string): The new name for the checklist item
            state (string): One of: `complete`, `incomplete`
            idChecklist (string): The ID of the checklist this item is in Example: '5abbe4b7ddc1b351ef961414'.
            pos (string): `top`, `bottom`, or a positive float
            due (string): A due date for the checkitem
            dueReminder (number): A dueReminder for the due date on the checkitem
            idMember (string): The ID of the member to remove from the card Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idCheckItem is None:
            raise ValueError("Missing required parameter 'idCheckItem'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/checkItem/{idCheckItem}"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("state", state),
                ("idChecklist", idChecklist),
                ("pos", pos),
                ("due", due),
                ("dueReminder", dueReminder),
                ("idMember", idMember),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_card_check_item(self, id: str, idCheckItem: str) -> Any:
        """
        Delete checkItem on a Card

        Args:
            id (string): id
            idCheckItem (string): idCheckItem

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idCheckItem is None:
            raise ValueError("Missing required parameter 'idCheckItem'.")
        url = f"{self.base_url}/cards/{id}/checkItem/{idCheckItem}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_list(self, id: str, fields: str | None = None) -> Any:
        """
        Get the List of a Card

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/list"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_members(self, id: str, fields: str | None = None) -> Any:
        """
        Get the Members of a Card

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/members"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_membersvoted(self, id: str, fields: str | None = None) -> Any:
        """
        Get Members who have voted on a Card

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/membersVoted"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def cardsidmembersvoted(self, id: str, value: str) -> Any:
        """
        Add Member vote to Card

        Args:
            id (string): id
            value (string): The ID of the member to vote 'yes' on the card Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/membersVoted"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_plugindata(self, id: str) -> Any:
        """
        Get pluginData on a Card

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/pluginData"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_stickers(self, id: str, fields: str | None = None) -> Any:
        """
        Get Stickers on a Card

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/stickers"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_cards_id_stickers(
        self,
        id: str,
        image: str,
        top: float,
        left: float,
        zIndex: int,
        rotate: float | None = None,
    ) -> Any:
        """
        Add a Sticker to a Card

        Args:
            id (string): id
            image (string): For custom stickers, the id of the sticker. For default stickers, the string identifier (like 'taco-cool', see below)
            top (number): The top position of the sticker, from -60 to 100
            left (number): The left position of the sticker, from -60 to 100
            zIndex (integer): The z-index of the sticker
            rotate (number): The rotation of the sticker

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/stickers"
        query_params = {
            k: v
            for k, v in [
                ("image", image),
                ("top", top),
                ("left", left),
                ("zIndex", zIndex),
                ("rotate", rotate),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_card_sticker(
        self, id: str, idSticker: str, fields: str | None = None
    ) -> Any:
        """
        Get a Sticker on a Card

        Args:
            id (string): id
            idSticker (string): idSticker
            fields (string): `all` or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idSticker is None:
            raise ValueError("Missing required parameter 'idSticker'.")
        url = f"{self.base_url}/cards/{id}/stickers/{idSticker}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_sticker_by_id(self, id: str, idSticker: str) -> Any:
        """
        Delete a Sticker on a Card

        Args:
            id (string): id
            idSticker (string): idSticker

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idSticker is None:
            raise ValueError("Missing required parameter 'idSticker'.")
        url = f"{self.base_url}/cards/{id}/stickers/{idSticker}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_card_sticker_by_id_sticker(
        self,
        id: str,
        idSticker: str,
        top: float,
        left: float,
        zIndex: int,
        rotate: float | None = None,
    ) -> Any:
        """
        Update a Sticker on a Card

        Args:
            id (string): id
            idSticker (string): idSticker
            top (number): The top position of the sticker, from -60 to 100
            left (number): The left position of the sticker, from -60 to 100
            zIndex (integer): The z-index of the sticker
            rotate (number): The rotation of the sticker

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idSticker is None:
            raise ValueError("Missing required parameter 'idSticker'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/stickers/{idSticker}"
        query_params = {
            k: v
            for k, v in [
                ("top", top),
                ("left", left),
                ("zIndex", zIndex),
                ("rotate", rotate),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_card_action_comment(self, id: str, idAction: str, text: str) -> Any:
        """
        Update Comment Action on a Card

        Args:
            id (string): id
            idAction (string): idAction
            text (string): The new text for the comment

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idAction is None:
            raise ValueError("Missing required parameter 'idAction'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/actions/{idAction}/comments"
        query_params = {k: v for k, v in [("text", text)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_comment_action(self, id: str, idAction: str) -> Any:
        """
        Delete a comment on a Card

        Args:
            id (string): id
            idAction (string): idAction

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idAction is None:
            raise ValueError("Missing required parameter 'idAction'.")
        url = f"{self.base_url}/cards/{id}/actions/{idAction}/comments"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_card_custom_field_item(
        self,
        idCard: str,
        idCustomField: str,
        value: dict[str, Any] | None = None,
        idValue: str | None = None,
    ) -> Any:
        """
        Update Custom Field item on Card

        Args:
            idCard (string): idCard
            idCustomField (string): idCustomField
            value (object): An object containing the key and value to set for the card's Custom Field value. The key used to set the value should match the type of Custom Field defined.
            idValue (string): idValue Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idCard is None:
            raise ValueError("Missing required parameter 'idCard'.")
        if idCustomField is None:
            raise ValueError("Missing required parameter 'idCustomField'.")
        request_body_data = None
        request_body_data = {
            "value": value,
            "idValue": idValue,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/cards/{idCard}/customField/{idCustomField}/item"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_cards_idcard_customfields(
        self, idCard: str, customFieldItems: list[dict[str, Any]] | None = None
    ) -> Any:
        """
        Update Multiple Custom Field items on Card

        Args:
            idCard (string): idCard
            customFieldItems (array): An array of objects containing the custom field ID, key and value, and ID of list type option.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idCard is None:
            raise ValueError("Missing required parameter 'idCard'.")
        request_body_data = None
        request_body_data = {
            "customFieldItems": customFieldItems,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/cards/{idCard}/customFields"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_cards_id_customfielditems(self, id: str) -> list[Any]:
        """
        Get Custom Field Items for a Card

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/cards/{id}/customFieldItems"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_cards_id_actions_comments(self, id: str, text: str) -> dict[str, Any]:
        """
        Add a new comment to a Card

        Args:
            id (string): id
            text (string): The comment

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/actions/comments"
        query_params = {k: v for k, v in [("text", text)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_cards_id_idlabels(self, id: str, value: str | None = None) -> Any:
        """
        Add a Label to a Card

        Args:
            id (string): id
            value (string): The ID of the label to add Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/idLabels"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_cards_id_idmembers(self, id: str, value: str | None = None) -> Any:
        """
        Add a Member to a Card

        Args:
            id (string): id
            value (string): The ID of the Member to add to the card Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/idMembers"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_cards_id_labels(self, id: str, color: str, name: str | None = None) -> Any:
        """
        Create a new Label on a Card

        Args:
            id (string): id
            color (string): A valid label color or `null`. See [labels](/cloud/trello/guides/rest-api/object-definitions/)
            name (string): A name for the label

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/labels"
        query_params = {
            k: v for k, v in [("color", color), ("name", name)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def mark_notifications_read(self, id: str) -> Any:
        """
        Mark a Card's Notifications as read

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{id}/markAssociatedNotificationsRead"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_card_id_label_by_id(self, id: str, idLabel: str) -> Any:
        """
        Remove a Label from a Card

        Args:
            id (string): id
            idLabel (string): idLabel

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idLabel is None:
            raise ValueError("Missing required parameter 'idLabel'.")
        url = f"{self.base_url}/cards/{id}/idLabels/{idLabel}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_id_idmembers_idmember(self, id: str, idMember: str) -> Any:
        """
        Remove a Member from a Card

        Args:
            id (string): id
            idMember (string): idMember

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        url = f"{self.base_url}/cards/{id}/idMembers/{idMember}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_card_voter(self, id: str, idMember: str) -> Any:
        """
        Remove a Member's Vote on a Card

        Args:
            id (string): id
            idMember (string): idMember

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        url = f"{self.base_url}/cards/{id}/membersVoted/{idMember}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_check_item(
        self, idCard: str, idChecklist: str, idCheckItem: str, pos: Any | None = None
    ) -> dict[str, Any]:
        """
        Update Checkitem on Checklist on Card

        Args:
            idCard (string): idCard
            idChecklist (string): idChecklist
            idCheckItem (string): idCheckItem
            pos (string): `top`, `bottom`, or a positive float

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idCard is None:
            raise ValueError("Missing required parameter 'idCard'.")
        if idChecklist is None:
            raise ValueError("Missing required parameter 'idChecklist'.")
        if idCheckItem is None:
            raise ValueError("Missing required parameter 'idCheckItem'.")
        request_body_data = None
        url = f"{self.base_url}/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}"
        query_params = {k: v for k, v in [("pos", pos)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_checklist_by_id(self, id: str, idChecklist: str) -> Any:
        """
        Delete a Checklist on a Card

        Args:
            id (string): id
            idChecklist (string): idChecklist

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idChecklist is None:
            raise ValueError("Missing required parameter 'idChecklist'.")
        url = f"{self.base_url}/cards/{id}/checklists/{idChecklist}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_checklists(
        self,
        idCard: str,
        name: str | None = None,
        pos: Any | None = None,
        idChecklistSource: str | None = None,
    ) -> Any:
        """
        Create a Checklist

        Args:
            idCard (string): The ID of the Card that the checklist should be added to. Example: '5abbe4b7ddc1b351ef961414'.
            name (string): The name of the checklist. Should be a string of length 1 to 16384.
            pos (string): The position of the checklist on the card. One of: `top`, `bottom`, or a positive number.
            idChecklistSource (string): The ID of a checklist to copy into the new checklist. Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/checklists"
        query_params = {
            k: v
            for k, v in [
                ("idCard", idCard),
                ("name", name),
                ("pos", pos),
                ("idChecklistSource", idChecklistSource),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_checklists_id(
        self,
        id: str,
        cards: str | None = None,
        checkItems: str | None = None,
        checkItem_fields: str | None = None,
        fields: str | None = None,
    ) -> Any:
        """
        Get a Checklist

        Args:
            id (string): id
            cards (string): Valid values: `all`, `closed`, `none`, `open`, `visible`. Cards is a nested resource. The additional query params available are documented at [Cards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#cards-nested-resource).
            checkItems (string): The check items on the list to return. One of: `all`, `none`.
            checkItem_fields (string): The fields on the checkItem to return if checkItems are being returned. `all` or a comma-separated list of: `name`, `nameData`, `pos`, `state`, `type`, `due`, `dueReminder`, `idMember`
            fields (string): `all` or a comma-separated list of checklist [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/checklists/{id}"
        query_params = {
            k: v
            for k, v in [
                ("cards", cards),
                ("checkItems", checkItems),
                ("checkItem_fields", checkItem_fields),
                ("fields", fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_checlists_id(
        self, id: str, name: str | None = None, pos: Any | None = None
    ) -> Any:
        """
        Update a Checklist

        Args:
            id (string): id
            name (string): Name of the new checklist being created. Should be length of 1 to 16384.
            pos (string): Determines the position of the checklist on the card. One of: `top`, `bottom`, or a positive number.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/checklists/{id}"
        query_params = {
            k: v for k, v in [("name", name), ("pos", pos)] if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_checklists_id(self, id: str) -> Any:
        """
        Delete a Checklist

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/checklists/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_checklists_id_field(self, id: str, field: str) -> Any:
        """
        Get field on a Checklist

        Args:
            id (string): id
            field (string): field

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        url = f"{self.base_url}/checklists/{id}/{field}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_checklists_id_field(self, id: str, field: str, value: Any) -> Any:
        """
        Update field on a Checklist

        Args:
            id (string): id
            field (string): field
            value (string): The value to change the checklist name to. Should be a string of length 1 to 16384.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        request_body_data = None
        url = f"{self.base_url}/checklists/{id}/{field}"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_checklists_id_board(self, id: str, fields: str | None = None) -> Any:
        """
        Get the Board the Checklist is on

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/checklists/{id}/board"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_checklists_id_cards(self, id: str) -> Any:
        """
        Get the Card a Checklist is on

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/checklists/{id}/cards"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_checklists_id_checkitems(
        self, id: str, filter: str | None = None, fields: str | None = None
    ) -> Any:
        """
        Get Checkitems on a Checklist

        Args:
            id (string): id
            filter (string): One of: `all`, `none`.
            fields (string): One of: `all`, `name`, `nameData`, `pos`, `state`,`type`, `due`, `dueReminder`, `idMember`.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/checklists/{id}/checkItems"
        query_params = {
            k: v for k, v in [("filter", filter), ("fields", fields)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_checklists_id_checkitems(
        self,
        id: str,
        name: str,
        pos: Any | None = None,
        checked: bool | None = None,
        due: str | None = None,
        dueReminder: float | None = None,
        idMember: str | None = None,
    ) -> Any:
        """
        Create Checkitem on Checklist

        Args:
            id (string): id
            name (string): The name of the new check item on the checklist. Should be a string of length 1 to 16384.
            pos (string): The position of the check item in the checklist. One of: `top`, `bottom`, or a positive number.
            checked (boolean): Determines whether the check item is already checked when created.
            due (string): A due date for the checkitem
            dueReminder (number): A dueReminder for the due date on the checkitem
            idMember (string): An ID of a member resource. Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/checklists/{id}/checkItems"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("pos", pos),
                ("checked", checked),
                ("due", due),
                ("dueReminder", dueReminder),
                ("idMember", idMember),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_check_item_detail(
        self, id: str, idCheckItem: str, fields: str | None = None
    ) -> Any:
        """
        Get a Checkitem on a Checklist

        Args:
            id (string): id
            idCheckItem (string): idCheckItem
            fields (string): One of: `all`, `name`, `nameData`, `pos`, `state`, `type`, `due`, `dueReminder`, `idMember`,.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idCheckItem is None:
            raise ValueError("Missing required parameter 'idCheckItem'.")
        url = f"{self.base_url}/checklists/{id}/checkItems/{idCheckItem}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_checklist_item_by_id(self, id: str, idCheckItem: str) -> Any:
        """
        Delete Checkitem from Checklist

        Args:
            id (string): id
            idCheckItem (string): idCheckItem

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idCheckItem is None:
            raise ValueError("Missing required parameter 'idCheckItem'.")
        url = f"{self.base_url}/checklists/{id}/checkItems/{idCheckItem}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_customfields(
        self,
        idModel: str | None = None,
        modelType: str | None = None,
        name: str | None = None,
        type: str | None = None,
        options: str | None = None,
        pos: Any | None = None,
        display_cardFront: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create a new Custom Field on a Board

        Args:
            idModel (string): idModel Example: '5abbe4b7ddc1b351ef961414'.
            modelType (string): The type of model that the Custom Field is being defined on. This should always be `board`.
            name (string): The name of the Custom Field
            type (string): The type of Custom Field to create.
            options (string): If the type is `checkbox`
            pos (string): pos
            display_cardFront (boolean): Whether this Custom Field should be shown on the front of Cards

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        request_body_data = {
            "idModel": idModel,
            "modelType": modelType,
            "name": name,
            "type": type,
            "options": options,
            "pos": pos,
            "display_cardFront": display_cardFront,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/customFields"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_customfields_id(self, id: str) -> dict[str, Any]:
        """
        Get a Custom Field

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/customFields/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_customfields_id(
        self,
        id: str,
        name: str | None = None,
        pos: Any | None = None,
        display_cardFront: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update a Custom Field definition

        Args:
            id (string): id
            name (string): The name of the Custom Field
            pos (string): pos
            display_cardFront (boolean): Whether to display this custom field on the front of cards

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "pos": pos,
            "display/cardFront": display_cardFront,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/customFields/{id}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_customfields_id(self, id: str) -> Any:
        """
        Delete a Custom Field definition

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/customFields/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_customfields_id_options(self, id: str) -> Any:
        """
        Add Option to Custom Field dropdown

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/customFields/{id}/options"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_customfields_id_options(self, id: str) -> Any:
        """
        Get Options of Custom Field drop down

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/customFields/{id}/options"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_custom_field_option_by_id(self, id: str, idCustomFieldOption: str) -> Any:
        """
        Get Option of Custom Field dropdown

        Args:
            id (string): id
            idCustomFieldOption (string): idCustomFieldOption

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idCustomFieldOption is None:
            raise ValueError("Missing required parameter 'idCustomFieldOption'.")
        url = f"{self.base_url}/customFields/{id}/options/{idCustomFieldOption}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_custom_field_option(self, id: str, idCustomFieldOption: str) -> Any:
        """
        Delete Option of Custom Field dropdown

        Args:
            id (string): id
            idCustomFieldOption (string): idCustomFieldOption

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idCustomFieldOption is None:
            raise ValueError("Missing required parameter 'idCustomFieldOption'.")
        url = f"{self.base_url}/customFields/{id}/options/{idCustomFieldOption}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def emoji(
        self, locale: str | None = None, spritesheets: bool | None = None
    ) -> dict[str, Any]:
        """
        List available Emoji

        Args:
            locale (string): The locale to return emoji descriptions and names in. Defaults to the logged in member's locale.
            spritesheets (boolean): `true` to return spritesheet URLs in the response

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        url = f"{self.base_url}/emoji"
        query_params = {
            k: v
            for k, v in [("locale", locale), ("spritesheets", spritesheets)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_enterprises_id(
        self,
        id: str,
        fields: str | None = None,
        members: str | None = None,
        member_fields: str | None = None,
        member_filter: str | None = None,
        member_sort: str | None = None,
        member_sortBy: str | None = None,
        member_sortOrder: str | None = None,
        member_startIndex: int | None = None,
        member_count: int | None = None,
        organizations: str | None = None,
        organization_fields: str | None = None,
        organization_paid_accounts: bool | None = None,
        organization_memberships: str | None = None,
    ) -> dict[str, Any]:
        """
        Get an Enterprise

        Args:
            id (string): id
            fields (string): Comma-separated list of: `id`, `name`, `displayName`, `prefs`, `ssoActivationFailed`, `idAdmins`, `idMembers` (Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. Read the SCIM documentation [here]() for more information on filtering), `idOrganizations`, `products`, `userTypes`, `idMembers`, `idOrganizations`
            members (string): One of: `none`, `normal`, `admins`, `owners`, `all`
            member_fields (string): One of: `avatarHash`, `fullName`, `initials`, `username`
            member_filter (string): Pass a [SCIM-style query](/cloud/trello/scim/) to filter members. This takes precedence over the all/normal/admins value of members. If any of the member_* args are set, the member array will be paginated.
            member_sort (string): This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value prefixed by a `-` to sort descending. If no `-` is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data.
            member_sortBy (string): Deprecated: Please use member_sort. This parameter expects a [SCIM-style sorting value](/cloud/trello/scim/). Note that the members array returned will be paginated if `members` is `normal` or `admins`. Pagination can be controlled with `member_startIndex`, etc, and the API response's header will contain the total count and pagination state.
            member_sortOrder (string): Deprecated: Please use member_sort. One of: `ascending`, `descending`, `asc`, `desc`
            member_startIndex (integer): Any integer between 0 and 100.
            member_count (integer): 0 to 100
            organizations (string): One of: `none`, `members`, `public`, `all`
            organization_fields (string): Any valid value that the [nested organization field resource]() accepts.
            organization_paid_accounts (boolean): Whether or not to include paid account information in the returned workspace objects
            organization_memberships (string): Comma-seperated list of: `me`, `normal`, `admin`, `active`, `deactivated`

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/enterprises/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields", fields),
                ("members", members),
                ("member_fields", member_fields),
                ("member_filter", member_filter),
                ("member_sort", member_sort),
                ("member_sortBy", member_sortBy),
                ("member_sortOrder", member_sortOrder),
                ("member_startIndex", member_startIndex),
                ("member_count", member_count),
                ("organizations", organizations),
                ("organization_fields", organization_fields),
                ("organization_paid_accounts", organization_paid_accounts),
                ("organization_memberships", organization_memberships),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_enterprises_id_auditlog(self, id: str) -> list[Any]:
        """
        Get auditlog data for an Enterprise

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/enterprises/{id}/auditlog"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_enterprises_id_admins(
        self, id: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get Enterprise admin Members

        Args:
            id (string): id
            fields (string): Any valid value that the [nested member field resource]() accepts.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/enterprises/{id}/admins"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_enterprises_id_signupurl(
        self,
        id: str,
        authenticate: bool | None = None,
        confirmationAccepted: bool | None = None,
        returnUrl: str | None = None,
        tosAccepted: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get signupUrl for Enterprise

        Args:
            id (string): id
            authenticate (boolean): Optional boolean parameter to specify whether authentication should be performed during the signup process.
            confirmationAccepted (boolean): Indicates whether the user has accepted the confirmation; defaults to false if not specified.
            returnUrl (string): Any valid URL.
            tosAccepted (boolean): Designates whether the user has seen/consented to the Trello ToS prior to being redirected to the enterprise signup page/their IdP.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/enterprises/{id}/signupUrl"
        query_params = {
            k: v
            for k, v in [
                ("authenticate", authenticate),
                ("confirmationAccepted", confirmationAccepted),
                ("returnUrl", returnUrl),
                ("tosAccepted", tosAccepted),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_users_id(
        self,
        id: str,
        licensed: bool | None = None,
        deactivated: bool | None = None,
        collaborator: bool | None = None,
        managed: bool | None = None,
        admin: bool | None = None,
        activeSince: str | None = None,
        inactiveSince: str | None = None,
        search: str | None = None,
        cursor: str | None = None,
    ) -> list[Any]:
        """
        Get Users of an Enterprise

        Args:
            id (string): id
            licensed (boolean): When true, returns members who possess a license for the corresponding Trello Enterprise; when false, returns members who do not. If unspecified, both licensed and unlicensed members will be returned.
            deactivated (boolean): When true, returns members who have been deactivated for the corresponding Trello Enterprise; when false, returns members who have not. If unspecified, both active and deactivated members will be returned.
            collaborator (boolean): When true, returns members who are guests on one or more boards in the corresponding Trello Enterprise (but do not possess a license); when false, returns members who are not. If unspecified, both guests and non-guests will be returned.
            managed (boolean): When true, returns members who are managed by the corresponding Trello Enterprise; when false, returns members who are not. If unspecified, both managed and unmanaged members will be returned.
            admin (boolean): When true, returns members who are administrators of the corresponding Trello Enterprise; when false, returns members who are not. If unspecified, both admin and non-admin members will be returned.
            activeSince (string): Returns only Trello users active since this date (inclusive).
            inactiveSince (string): Returns only Trello users active since this date (inclusive).
            search (string): Returns members with email address or full name that start with the search value.
            cursor (string): Cursor to return next set of results, use cursor returned in the response to query the next batch.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/enterprises/{id}/members/query"
        query_params = {
            k: v
            for k, v in [
                ("licensed", licensed),
                ("deactivated", deactivated),
                ("collaborator", collaborator),
                ("managed", managed),
                ("admin", admin),
                ("activeSince", activeSince),
                ("inactiveSince", inactiveSince),
                ("search", search),
                ("cursor", cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_enterprises_id_members(
        self,
        id: str,
        fields: str | None = None,
        filter: str | None = None,
        sort: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        startIndex: int | None = None,
        count: str | None = None,
        organization_fields: str | None = None,
        board_fields: str | None = None,
    ) -> list[Any]:
        """
        Get Members of Enterprise

        Args:
            id (string): id
            fields (string): A comma-seperated list of valid [member fields](/cloud/trello/guides/rest-api/object-definitions/#member-object).
            filter (string): Pass a [SCIM-style query](/cloud/trello/scim/) to filter members. This takes precedence over the all/normal/admins value of members. If any of the below member_* args are set, the member array will be paginated.
            sort (string): This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value prefixed by a `-` to sort descending. If no `-` is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data.
            sortBy (string): Deprecated: Please use `sort` instead. This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value. Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data.
            sortOrder (string): Deprecated: Please use `sort` instead. One of: `ascending`, `descending`, `asc`, `desc`.
            startIndex (integer): Any integer between 0 and 9999.
            count (string): [SCIM-style filter](/cloud/trello/scim/).
            organization_fields (string): Any valid value that the [nested organization field resource](/cloud/trello/guides/rest-api/nested-resources/) accepts.
            board_fields (string): Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/enterprises/{id}/members"
        query_params = {
            k: v
            for k, v in [
                ("fields", fields),
                ("filter", filter),
                ("sort", sort),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("startIndex", startIndex),
                ("count", count),
                ("organization_fields", organization_fields),
                ("board_fields", board_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_member_details(
        self,
        id: str,
        idMember: str,
        fields: str | None = None,
        organization_fields: str | None = None,
        board_fields: str | None = None,
    ) -> dict[str, Any]:
        """
        Get a Member of Enterprise

        Args:
            id (string): id
            idMember (string): idMember
            fields (string): A comma separated list of any valid values that the [nested member field resource]() accepts.
            organization_fields (string): Any valid value that the [nested organization field resource](/cloud/trello/guides/rest-api/nested-resources/) accepts.
            board_fields (string): Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        url = f"{self.base_url}/enterprises/{id}/members/{idMember}"
        query_params = {
            k: v
            for k, v in [
                ("fields", fields),
                ("organization_fields", organization_fields),
                ("board_fields", board_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organization_transfer(self, id: str, idOrganization: str) -> dict[str, Any]:
        """
        Get whether an organization can be transferred to an enterprise.

        Args:
            id (string): id
            idOrganization (string): idOrganization

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idOrganization is None:
            raise ValueError("Missing required parameter 'idOrganization'.")
        url = f"{self.base_url}/enterprises/{id}/transferrable/organization/{idOrganization}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_enterprise_transferrables_by_org_ids(
        self, id: str, idOrganizations: str
    ) -> list[Any]:
        """
        Get a bulk list of organizations that can be transferred to an enterprise.

        Args:
            id (string): id
            idOrganizations (string): idOrganizations

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idOrganizations is None:
            raise ValueError("Missing required parameter 'idOrganizations'.")
        url = f"{self.base_url}/enterprises/{id}/transferrable/bulk/{idOrganizations}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def bulk_join_enterprise_requests(self, id: str, idOrganizations: list[Any]) -> Any:
        """
        Decline enterpriseJoinRequests from one organization or a bulk list of organizations.

        Args:
            id (string): id
            idOrganizations (array): An array of IDs of an Organization resource.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/enterprises/${id}/enterpriseJoinRequest/bulk"
        query_params = {
            k: v for k, v in [("idOrganizations", idOrganizations)] if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_claimable_orgs(
        self,
        id: str,
        limit: int | None = None,
        cursor: str | None = None,
        name: str | None = None,
        activeSince: str | None = None,
        inactiveSince: str | None = None,
    ) -> dict[str, Any]:
        """
        Get ClaimableOrganizations of an Enterprise

        Args:
            id (string): id
            limit (integer): Limits the number of workspaces to be sorted
            cursor (string): Specifies the sort order to return matching documents
            name (string): Name of the enterprise to retrieve workspaces for
            activeSince (string): Date in YYYY-MM-DD format indicating the date to search up to for activeness of workspace
            inactiveSince (string): Date in YYYY-MM-DD format indicating the date to search up to for inactiveness of workspace

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/enterprises/{id}/claimableOrganizations"
        query_params = {
            k: v
            for k, v in [
                ("limit", limit),
                ("cursor", cursor),
                ("name", name),
                ("activeSince", activeSince),
                ("inactiveSince", inactiveSince),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_pending_organizations(
        self,
        id: str,
        activeSince: str | None = None,
        inactiveSince: str | None = None,
    ) -> list[Any]:
        """
        Get PendingOrganizations of an Enterprise

        Args:
            id (string): id
            activeSince (string): Date in YYYY-MM-DD format indicating the date to search up to for activeness of workspace
            inactiveSince (string): Date in YYYY-MM-DD format indicating the date to search up to for inactiveness of workspace

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/enterprises/{id}/pendingOrganizations"
        query_params = {
            k: v
            for k, v in [("activeSince", activeSince), ("inactiveSince", inactiveSince)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_enterprises_id_tokens(self, id: str, expiration: str | None = None) -> Any:
        """
        Create an auth Token for an Enterprise.

        Args:
            id (string): id
            expiration (string): One of: `1hour`, `1day`, `30days`, `never`

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/enterprises/{id}/tokens"
        query_params = {k: v for k, v in [("expiration", expiration)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_enterprise_organizations_by_id(
        self, id: str, idOrganization: str
    ) -> list[Any]:
        """
        Transfer an Organization to an Enterprise.

        Args:
            id (string): id
            idOrganization (string): ID of Organization to be transferred to Enterprise.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/enterprises/{id}/organizations"
        query_params = {
            k: v for k, v in [("idOrganization", idOrganization)] if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_enterprise_member_licensed(
        self, id: str, idMember: str, value: bool
    ) -> dict[str, Any]:
        """
        Update a Member's licensed status

        Args:
            id (string): id
            idMember (string): idMember
            value (boolean): Boolean value to determine whether the user should be given an Enterprise license (true) or not (false).

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        request_body_data = None
        url = f"{self.base_url}/enterprises/{id}/members/{idMember}/licensed"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def deactivate_member(
        self,
        id: str,
        idMember: str,
        value: bool,
        fields: str | None = None,
        organization_fields: str | None = None,
        board_fields: str | None = None,
    ) -> Any:
        """
        Deactivate a Member of an Enterprise.

        Args:
            id (string): id
            idMember (string): idMember
            value (boolean): Determines whether the user is deactivated or not.
            fields (string): A comma separated list of any valid values that the [nested member field resource]() accepts.
            organization_fields (string): Any valid value that the [nested organization resource](/cloud/trello/guides/rest-api/nested-resources/) accepts.
            board_fields (string): Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        request_body_data = None
        url = f"{self.base_url}/enterprises/{id}/members/{idMember}/deactivated"
        query_params = {
            k: v
            for k, v in [
                ("value", value),
                ("fields", fields),
                ("organization_fields", organization_fields),
                ("board_fields", board_fields),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_admin_member(self, id: str, idMember: str) -> Any:
        """
        Update Member to be admin of Enterprise

        Args:
            id (string): id
            idMember (string): idMember

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        request_body_data = None
        url = f"{self.base_url}/enterprises/{id}/admins/{idMember}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_enterprise_admin_by_id(self, id: str, idMember: str) -> Any:
        """
        Remove a Member as admin from Enterprise.

        Args:
            id (string): id
            idMember (string): idMember

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        url = f"{self.base_url}/enterprises/{id}/admins/{idMember}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_organization_by_id_and_org_id(self, id: str, idOrg: str) -> Any:
        """
        Delete an Organization from an Enterprise.

        Args:
            id (string): id
            idOrg (string): idOrg

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idOrg is None:
            raise ValueError("Missing required parameter 'idOrg'.")
        url = f"{self.base_url}/enterprises/{id}/organizations/{idOrg}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_bulk_organizations_by_ids(self, id: str, idOrganizations: str) -> Any:
        """
        Bulk accept a set of organizations to an Enterprise.

        Args:
            id (string): id
            idOrganizations (string): idOrganizations

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idOrganizations is None:
            raise ValueError("Missing required parameter 'idOrganizations'.")
        url = f"{self.base_url}/enterprises/{id}/organizations/bulk/{idOrganizations}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_labels_id(self, id: str, fields: str | None = None) -> Any:
        """
        Get a Label

        Args:
            id (string): id
            fields (string): all or a comma-separated list of [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/labels/{id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_labels_id(
        self, id: str, name: str | None = None, color: str | None = None
    ) -> Any:
        """
        Update a Label

        Args:
            id (string): id
            name (string): The new name for the label
            color (string): The new color for the label. See: [fields](/cloud/trello/guides/rest-api/object-definitions/) for color options

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/labels/{id}"
        query_params = {
            k: v for k, v in [("name", name), ("color", color)] if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_labels_id(self, id: str) -> Any:
        """
        Delete a Label

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/labels/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_labels_id_field(self, id: str, field: str, value: str) -> Any:
        """
        Update a field on a label

        Args:
            id (string): id
            field (string): field
            value (string): The new value for the field. Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        request_body_data = None
        url = f"{self.base_url}/labels/{id}/{field}"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_labels(self, name: str, color: str, idBoard: str) -> Any:
        """
        Create a Label

        Args:
            name (string): Name for the label
            color (string): The color for the label.
            idBoard (string): The ID of the Board to create the Label on.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/labels"
        query_params = {
            k: v
            for k, v in [("name", name), ("color", color), ("idBoard", idBoard)]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_lists_id(self, id: str, fields: str | None = None) -> Any:
        """
        Get a List

        Args:
            id (string): id
            fields (string): `all` or a comma separated list of List field names.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/lists/{id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_lists_id(
        self,
        id: str,
        name: str | None = None,
        closed: bool | None = None,
        idBoard: str | None = None,
        pos: Any | None = None,
        subscribed: bool | None = None,
    ) -> Any:
        """
        Update a List

        Args:
            id (string): id
            name (string): New name for the list
            closed (boolean): Whether the list should be closed (archived)
            idBoard (string): ID of a board the list should be moved to Example: '5abbe4b7ddc1b351ef961414'.
            pos (string): New position for the list: `top`, `bottom`, or a positive floating point number
            subscribed (boolean): Whether the active member is subscribed to this list

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/lists/{id}"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("closed", closed),
                ("idBoard", idBoard),
                ("pos", pos),
                ("subscribed", subscribed),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_lists(
        self,
        name: str,
        idBoard: str,
        idListSource: str | None = None,
        pos: Any | None = None,
    ) -> Any:
        """
        Create a new List

        Args:
            name (string): Name for the list
            idBoard (string): The long ID of the board the list should be created on Example: '5abbe4b7ddc1b351ef961414'.
            idListSource (string): ID of the List to copy into the new List Example: '5abbe4b7ddc1b351ef961414'.
            pos (string): Position of the list. `top`, `bottom`, or a positive floating point number

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/lists"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("idBoard", idBoard),
                ("idListSource", idListSource),
                ("pos", pos),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_lists_id_archiveallcards(self, id: str) -> Any:
        """
        Archive all Cards in List

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/lists/{id}/archiveAllCards"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_lists_id_moveallcards(self, id: str, idBoard: str, idList: str) -> Any:
        """
        Move all Cards in List

        Args:
            id (string): id
            idBoard (string): The ID of the board the cards should be moved to Example: '5abbe4b7ddc1b351ef961414'.
            idList (string): The ID of the list that the cards should be moved to Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/lists/{id}/moveAllCards"
        query_params = {
            k: v for k, v in [("idBoard", idBoard), ("idList", idList)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_lists_id_closed(self, id: str, value: str | None = None) -> Any:
        """
        Archive or unarchive a list

        Args:
            id (string): id
            value (string): Set to true to close (archive) the list Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/lists/{id}/closed"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_id_idboard(self, id: str, value: str) -> Any:
        """
        Move List to Board

        Args:
            id (string): id
            value (string): The ID of the board to move the list to Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/lists/{id}/idBoard"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_lists_id_field(self, id: str, field: str, value: Any | None = None) -> Any:
        """
        Update a field on a List

        Args:
            id (string): id
            field (string): field
            value (string): The new value for the field

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        request_body_data = None
        url = f"{self.base_url}/lists/{id}/{field}"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_lists_id_actions(self, id: str, filter: str | None = None) -> Any:
        """
        Get Actions for a List

        Args:
            id (string): id
            filter (string): A comma-separated list of [action types](

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/lists/{id}/actions"
        query_params = {k: v for k, v in [("filter", filter)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_lists_id_board(self, id: str, fields: str | None = None) -> Any:
        """
        Get the Board a List is on

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/lists/{id}/board"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_lists_id_cards(self, id: str) -> list[Any]:
        """
        Get Cards in a List

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/lists/{id}/cards"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id(
        self,
        id: str,
        actions: str | None = None,
        boards: str | None = None,
        boardBackgrounds: str | None = None,
        boardsInvited: str | None = None,
        boardsInvited_fields: str | None = None,
        boardStars: bool | None = None,
        cards: str | None = None,
        customBoardBackgrounds: str | None = None,
        customEmoji: str | None = None,
        customStickers: str | None = None,
        fields: str | None = None,
        notifications: str | None = None,
        organizations: str | None = None,
        organization_fields: str | None = None,
        organization_paid_account: bool | None = None,
        organizationsInvited: str | None = None,
        organizationsInvited_fields: str | None = None,
        paid_account: bool | None = None,
        savedSearches: bool | None = None,
        tokens: str | None = None,
    ) -> Any:
        """
        Get a Member

        Args:
            id (string): id
            actions (string): See the [Actions Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#actions-nested-resource)
            boards (string): See the [Boards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#boards-nested-resource)
            boardBackgrounds (string): One of: `all`, `custom`, `default`, `none`, `premium`
            boardsInvited (string): `all` or a comma-separated list of: closed, members, open, organization, pinned, public, starred, unpinned
            boardsInvited_fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/)
            boardStars (boolean): Whether to return the boardStars or not
            cards (string): See the [Cards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#cards-nested-resource) for additional options
            customBoardBackgrounds (string): `all` or `none`
            customEmoji (string): `all` or `none`
            customStickers (string): `all` or `none`
            fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
            notifications (string): See the [Notifications Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#notifications-nested-resource)
            organizations (string): One of: `all`, `members`, `none`, `public`
            organization_fields (string): `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)
            organization_paid_account (boolean): Whether or not to include paid account information in the returned workspace object
            organizationsInvited (string): One of: `all`, `members`, `none`, `public`
            organizationsInvited_fields (string): `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)
            paid_account (boolean): Whether or not to include paid account information in the returned member object
            savedSearches (boolean): Indicates whether to include saved searches in the response for the specified member.
            tokens (string): `all` or `none`

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}"
        query_params = {
            k: v
            for k, v in [
                ("actions", actions),
                ("boards", boards),
                ("boardBackgrounds", boardBackgrounds),
                ("boardsInvited", boardsInvited),
                ("boardsInvited_fields", boardsInvited_fields),
                ("boardStars", boardStars),
                ("cards", cards),
                ("customBoardBackgrounds", customBoardBackgrounds),
                ("customEmoji", customEmoji),
                ("customStickers", customStickers),
                ("fields", fields),
                ("notifications", notifications),
                ("organizations", organizations),
                ("organization_fields", organization_fields),
                ("organization_paid_account", organization_paid_account),
                ("organizationsInvited", organizationsInvited),
                ("organizationsInvited_fields", organizationsInvited_fields),
                ("paid_account", paid_account),
                ("savedSearches", savedSearches),
                ("tokens", tokens),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_members_id(
        self,
        id: str,
        fullName: str | None = None,
        initials: str | None = None,
        username: str | None = None,
        bio: str | None = None,
        avatarSource: str | None = None,
        prefs_colorBlind: bool | None = None,
        prefs_locale: str | None = None,
        prefs_minutesBetweenSummaries: int | None = None,
    ) -> Any:
        """
        Update a Member

        Args:
            id (string): id
            fullName (string): New name for the member. Cannot begin or end with a space.
            initials (string): New initials for the member. 1-4 characters long.
            username (string): New username for the member. At least 3 characters long, only lowercase letters, underscores, and numbers. Must be unique.
            bio (string): Provides a brief biography for the member, included as an optional string in the query parameter.
            avatarSource (string): One of: `gravatar`, `none`, `upload`
            prefs_colorBlind (boolean): Indicates whether the member's preferences should accommodate color blindness by adjusting visual elements, with true enabling colorblind-friendly settings.
            prefs_locale (string): Optional query parameter specifying the preferred locale for the member, allowing language or region-specific preferences to be set during the update.
            prefs_minutesBetweenSummaries (integer): `-1` for disabled, `1`, or `60`

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fullName", fullName),
                ("initials", initials),
                ("username", username),
                ("bio", bio),
                ("avatarSource", avatarSource),
                ("prefs/colorBlind", prefs_colorBlind),
                ("prefs/locale", prefs_locale),
                ("prefs/minutesBetweenSummaries", prefs_minutesBetweenSummaries),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_field(self, id: str, field: str) -> Any:
        """
        Get a field on a Member

        Args:
            id (string): id
            field (string): field

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        url = f"{self.base_url}/members/{id}/{field}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_actions(self, id: str, filter: str | None = None) -> list[Any]:
        """
        Get a Member's Actions

        Args:
            id (string): id
            filter (string): A comma-separated list of [action types](

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/actions"
        query_params = {k: v for k, v in [("filter", filter)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_board_backgrounds_by_id(
        self, id: str, filter: str | None = None
    ) -> list[Any]:
        """
        Get Member's custom Board backgrounds

        Args:
            id (string): id
            filter (string): One of: `all`, `custom`, `default`, `none`, `premium`

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/boardBackgrounds"
        query_params = {k: v for k, v in [("filter", filter)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def create_board_background(self, id: str, file: bytes) -> list[Any]:
        """
        Upload new boardBackground for Member

        Args:
            id (string): id
            file (string): Specifies the file to be uploaded as a board background for the member, provided as a query parameter in the POST request.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/boardBackgrounds"
        query_params = {k: v for k, v in [("file", file)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_member_board_backgrounds(
        self, id: str, idBackground: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get a boardBackground of a Member

        Args:
            id (string): id
            idBackground (string): idBackground
            fields (string): `all` or a comma-separated list of: `brightness`, `fullSizeUrl`, `scaled`, `tile`

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idBackground is None:
            raise ValueError("Missing required parameter 'idBackground'.")
        url = f"{self.base_url}/members/{id}/boardBackgrounds/{idBackground}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_board_background(
        self,
        id: str,
        idBackground: str,
        brightness: str | None = None,
        tile: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update a Member's custom Board background

        Args:
            id (string): id
            idBackground (string): idBackground
            brightness (string): One of: `dark`, `light`, `unknown`
            tile (boolean): Whether the background should be tiled

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idBackground is None:
            raise ValueError("Missing required parameter 'idBackground'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/boardBackgrounds/{idBackground}"
        query_params = {
            k: v
            for k, v in [("brightness", brightness), ("tile", tile)]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_board_background_by_id(self, id: str, idBackground: str) -> Any:
        """
        Delete a Member's custom Board background

        Args:
            id (string): id
            idBackground (string): idBackground

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idBackground is None:
            raise ValueError("Missing required parameter 'idBackground'.")
        url = f"{self.base_url}/members/{id}/boardBackgrounds/{idBackground}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_boardstars(self, id: str) -> Any:
        """
        Get a Member's boardStars

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/boardStars"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_members_id_boardstars(self, id: str, idBoard: str, pos: Any) -> list[Any]:
        """
        Create Star for Board

        Args:
            id (string): id
            idBoard (string): The ID of the board to star Example: '5abbe4b7ddc1b351ef961414'.
            pos (string): The position of the newly starred board. `top`, `bottom`, or a positive float.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/boardStars"
        query_params = {
            k: v for k, v in [("idBoard", idBoard), ("pos", pos)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_board_star_by_id(self, id: str, idStar: str) -> dict[str, Any]:
        """
        Get a boardStar of Member

        Args:
            id (string): id
            idStar (string): idStar

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idStar is None:
            raise ValueError("Missing required parameter 'idStar'.")
        url = f"{self.base_url}/members/{id}/boardStars/{idStar}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_board_star_position(
        self, id: str, idStar: str, pos: Any | None = None
    ) -> Any:
        """
        Update the position of a boardStar of Member

        Args:
            id (string): id
            idStar (string): idStar
            pos (string): New position for the starred board. `top`, `bottom`, or a positive float.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idStar is None:
            raise ValueError("Missing required parameter 'idStar'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/boardStars/{idStar}"
        query_params = {k: v for k, v in [("pos", pos)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_board_star(self, id: str, idStar: str) -> Any:
        """
        Delete Star for Board

        Args:
            id (string): id
            idStar (string): idStar

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idStar is None:
            raise ValueError("Missing required parameter 'idStar'.")
        url = f"{self.base_url}/members/{id}/boardStars/{idStar}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_boards(
        self,
        id: str,
        filter: str | None = None,
        fields: str | None = None,
        lists: str | None = None,
        organization: bool | None = None,
        organization_fields: str | None = None,
    ) -> list[Any]:
        """
        Get Boards that Member belongs to

        Args:
            id (string): id
            filter (string): `all` or a comma-separated list of: `closed`, `members`, `open`, `organization`, `public`, `starred`
            fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/)
            lists (string): Which lists to include with the boards. One of: `all`, `closed`, `none`, `open`
            organization (boolean): Whether to include the Organization object with the Boards
            organization_fields (string): `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/boards"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("fields", fields),
                ("lists", lists),
                ("organization", organization),
                ("organization_fields", organization_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_boardsinvited(
        self, id: str, fields: str | None = None
    ) -> list[Any]:
        """
        Get Boards the Member has been invited to

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/boardsInvited"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_cards(self, id: str, filter: str | None = None) -> list[Any]:
        """
        Get Cards the Member is on

        Args:
            id (string): id
            filter (string): One of: `all`, `closed`, `complete`, `incomplete`, `none`, `open`, `visible`

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/cards"
        query_params = {k: v for k, v in [("filter", filter)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_custom_board_backgrounds_by_id(self, id: str) -> list[Any]:
        """
        Get a Member's custom Board Backgrounds

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/customBoardBackgrounds"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def set_custom_board_backgrounds(self, id: str, file: bytes) -> dict[str, Any]:
        """
        Create a new custom Board Background

        Args:
            id (string): id
            file (string): The file query parameter is required and specifies the identifier or filename of the custom board background to be processed, uploaded, or associated with the member.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/customBoardBackgrounds"
        query_params = {k: v for k, v in [("file", file)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_custom_board_backgrounds_by_id_back(
        self, id: str, idBackground: str
    ) -> dict[str, Any]:
        """
        Get custom Board Background of Member

        Args:
            id (string): id
            idBackground (string): idBackground

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idBackground is None:
            raise ValueError("Missing required parameter 'idBackground'.")
        url = f"{self.base_url}/members/{id}/customBoardBackgrounds/{idBackground}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_member_custom_board_background(
        self,
        id: str,
        idBackground: str,
        brightness: str | None = None,
        tile: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update custom Board Background of Member

        Args:
            id (string): id
            idBackground (string): idBackground
            brightness (string): One of: `dark`, `light`, `unknown`
            tile (boolean): Whether to tile the background

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idBackground is None:
            raise ValueError("Missing required parameter 'idBackground'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/customBoardBackgrounds/{idBackground}"
        query_params = {
            k: v
            for k, v in [("brightness", brightness), ("tile", tile)]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_custom_background_by_id(self, id: str, idBackground: str) -> Any:
        """
        Delete custom Board Background of Member

        Args:
            id (string): id
            idBackground (string): idBackground

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idBackground is None:
            raise ValueError("Missing required parameter 'idBackground'.")
        url = f"{self.base_url}/members/{id}/customBoardBackgrounds/{idBackground}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_customemoji(self, id: str) -> list[Any]:
        """
        Get a Member's customEmojis

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/customEmoji"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_members_id_customemoji(
        self, id: str, file: bytes, name: str
    ) -> dict[str, Any]:
        """
        Create custom Emoji for Member

        Args:
            id (string): id
            file (string): The file parameter in the query is a required string representing the custom emoji file to be uploaded for the specified member.
            name (string): Name for the emoji. 2 - 64 characters

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/customEmoji"
        query_params = {
            k: v for k, v in [("file", file), ("name", name)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def membersidcustomemojiidemoji(
        self, id: str, idEmoji: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get a Member's custom Emoji

        Args:
            id (string): id
            idEmoji (string): idEmoji
            fields (string): `all` or a comma-separated list of `name`, `url`

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idEmoji is None:
            raise ValueError("Missing required parameter 'idEmoji'.")
        url = f"{self.base_url}/members/{id}/customEmoji/{idEmoji}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_customstickers(self, id: str) -> list[Any]:
        """
        Get Member's custom Stickers

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/customStickers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_members_id_customstickers(self, id: str, file: bytes) -> dict[str, Any]:
        """
        Create custom Sticker for Member

        Args:
            id (string): id
            file (string): Required file identifier or path as a string, used to specify the file associated with the custom sticker for the member.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/customStickers"
        query_params = {k: v for k, v in [("file", file)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_member_custom_sticker_by_id(
        self, id: str, idSticker: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get a Member's custom Sticker

        Args:
            id (string): id
            idSticker (string): idSticker
            fields (string): `all` or a comma-separated list of `scaled`, `url`

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idSticker is None:
            raise ValueError("Missing required parameter 'idSticker'.")
        url = f"{self.base_url}/members/{id}/customStickers/{idSticker}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_member_custom_sticker_by_id(self, id: str, idSticker: str) -> Any:
        """
        Delete a Member's custom Sticker

        Args:
            id (string): id
            idSticker (string): idSticker

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idSticker is None:
            raise ValueError("Missing required parameter 'idSticker'.")
        url = f"{self.base_url}/members/{id}/customStickers/{idSticker}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_notifications(
        self,
        id: str,
        entities: bool | None = None,
        display: bool | None = None,
        filter: str | None = None,
        read_filter: str | None = None,
        fields: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        before: str | None = None,
        since: str | None = None,
        memberCreator: bool | None = None,
        memberCreator_fields: str | None = None,
    ) -> list[Any]:
        """
        Get Member's Notifications

        Args:
            id (string): id
            entities (boolean): Optional boolean query parameter indicating whether to include entities in the response, defaulting to false.
            display (boolean): Determines if notifications should be displayed for the member (defaults to false).
            filter (string): Optional string parameter to filter notifications for the specified member, defaulting to "all" if not provided.
            read_filter (string): One of: `all`, `read`, `unread`
            fields (string): `all` or a comma-separated list of notification [fields](/cloud/trello/guides/rest-api/object-definitions/)
            limit (integer): Max 1000
            page (integer): Max 100
            before (string): A notification ID
            since (string): A notification ID
            memberCreator (boolean): Filter notifications to only include those created by the member specified by the {id} when set to true; defaults to true if not provided.
            memberCreator_fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/notifications"
        query_params = {
            k: v
            for k, v in [
                ("entities", entities),
                ("display", display),
                ("filter", filter),
                ("read_filter", read_filter),
                ("fields", fields),
                ("limit", limit),
                ("page", page),
                ("before", before),
                ("since", since),
                ("memberCreator", memberCreator),
                ("memberCreator_fields", memberCreator_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_organizations(
        self,
        id: str,
        filter: str | None = None,
        fields: str | None = None,
        paid_account: bool | None = None,
    ) -> list[Any]:
        """
        Get Member's Organizations

        Args:
            id (string): id
            filter (string): One of: `all`, `members`, `none`, `public` (Note: `members` filters to only private Workspaces)
            fields (string): `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)
            paid_account (boolean): Whether or not to include paid account information in the returned workspace object

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/organizations"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("fields", fields),
                ("paid_account", paid_account),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_member_organizations_invited(
        self, id: str, fields: str | None = None
    ) -> list[Any]:
        """
        Get Organizations a Member has been invited to

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/organizationsInvited"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_savedsearches(self, id: str) -> list[Any]:
        """
        Get Member's saved searched

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/savedSearches"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_members_id_savedsearches(
        self, id: str, name: str, query: str, pos: Any
    ) -> dict[str, Any]:
        """
        Create saved Search for Member

        Args:
            id (string): id
            name (string): The name for the saved search
            query (string): The search query
            pos (string): The position of the saved search. `top`, `bottom`, or a positive float.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/savedSearches"
        query_params = {
            k: v
            for k, v in [("name", name), ("query", query), ("pos", pos)]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_saved_searches_by_id(self, id: str, idSearch: str) -> dict[str, Any]:
        """
        Get a saved search

        Args:
            id (string): id
            idSearch (string): idSearch

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idSearch is None:
            raise ValueError("Missing required parameter 'idSearch'.")
        url = f"{self.base_url}/members/{id}/savedSearches/{idSearch}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_member_saved_search(
        self,
        id: str,
        idSearch: str,
        name: str | None = None,
        query: str | None = None,
        pos: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a saved search

        Args:
            id (string): id
            idSearch (string): idSearch
            name (string): The new name for the saved search
            query (string): The new search query
            pos (string): New position for saves search. `top`, `bottom`, or a positive float.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idSearch is None:
            raise ValueError("Missing required parameter 'idSearch'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/savedSearches/{idSearch}"
        query_params = {
            k: v
            for k, v in [("name", name), ("query", query), ("pos", pos)]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_saved_search(self, id: str, idSearch: str) -> Any:
        """
        Delete a saved search

        Args:
            id (string): id
            idSearch (string): idSearch

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idSearch is None:
            raise ValueError("Missing required parameter 'idSearch'.")
        url = f"{self.base_url}/members/{id}/savedSearches/{idSearch}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_members_id_tokens(self, id: str, webhooks: bool | None = None) -> list[Any]:
        """
        Get Member's Tokens

        Args:
            id (string): id
            webhooks (boolean): Whether to include webhooks

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/tokens"
        query_params = {k: v for k, v in [("webhooks", webhooks)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def membersidavatar(self, id: str, file: bytes) -> Any:
        """
        Create Avatar for Member

        Args:
            id (string): id
            file (string): The "file" parameter specifies the file to upload as a string, required for the avatar upload operation.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/avatar"
        query_params = {k: v for k, v in [("file", file)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_member_one_time_messages_dismissed(self, id: str, value: str) -> Any:
        """
        Dismiss a message for Member

        Args:
            id (string): id
            value (string): The message to dismiss Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/oneTimeMessagesDismissed"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_member_notifications_channel_settings(self, id: str) -> list[Any]:
        """
        Get a Member's notification channel settings

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/members/{id}/notificationsChannelSettings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_notification_channel_settings(
        self, id: str, channel: str, blockedKeys: Any
    ) -> Any:
        """
        Update blocked notification keys of Member on a channel

        Args:
            id (string): id
            channel (string): channel Example: 'email'.
            blockedKeys (string): Blocked key or array of blocked keys.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "channel": channel,
            "blockedKeys": blockedKeys,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/members/{id}/notificationsChannelSettings"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_member_notification_channel_settings(self, id: str, channel: str) -> Any:
        """
        Get blocked notification keys of Member on this channel

        Args:
            id (string): id
            channel (string): channel

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if channel is None:
            raise ValueError("Missing required parameter 'channel'.")
        url = f"{self.base_url}/members/{id}/notificationsChannelSettings/{channel}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_member_notification_channel_settings(
        self, id: str, channel: str, blockedKeys: Any
    ) -> Any:
        """
        Update blocked notification keys of Member on a channel

        Args:
            id (string): id
            channel (string): channel
            blockedKeys (string): Singular key or array of notification keys

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if channel is None:
            raise ValueError("Missing required parameter 'channel'.")
        request_body_data = None
        request_body_data = {
            "blockedKeys": blockedKeys,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/members/{id}/notificationsChannelSettings/{channel}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_notification_settings(
        self, id: str, channel: str, blockedKeys: str
    ) -> Any:
        """
        Update blocked notification keys of Member on a channel

        Args:
            id (string): id
            channel (string): channel
            blockedKeys (string): blockedKeys

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if channel is None:
            raise ValueError("Missing required parameter 'channel'.")
        if blockedKeys is None:
            raise ValueError("Missing required parameter 'blockedKeys'.")
        request_body_data = None
        url = f"{self.base_url}/members/{id}/notificationsChannelSettings/{channel}/{blockedKeys}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_notifications_id(
        self,
        id: str,
        board: bool | None = None,
        board_fields: str | None = None,
        card: bool | None = None,
        card_fields: str | None = None,
        display: bool | None = None,
        entities: bool | None = None,
        fields: str | None = None,
        list: bool | None = None,
        member: bool | None = None,
        member_fields: str | None = None,
        memberCreator: bool | None = None,
        memberCreator_fields: str | None = None,
        organization: bool | None = None,
        organization_fields: str | None = None,
    ) -> Any:
        """
        Get a Notification

        Args:
            id (string): id
            board (boolean): Whether to include the board object
            board_fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/)
            card (boolean): Whether to include the card object
            card_fields (string): `all` or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/)
            display (boolean): Whether to include the display object with the results
            entities (boolean): Whether to include the entities object with the results
            fields (string): `all` or a comma-separated list of notification [fields](/cloud/trello/guides/rest-api/object-definitions/)
            list (boolean): Whether to include the list object
            member (boolean): Whether to include the member object
            member_fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
            memberCreator (boolean): Whether to include the member object of the creator
            memberCreator_fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
            organization (boolean): Whether to include the organization object
            organization_fields (string): `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/notifications/{id}"
        query_params = {
            k: v
            for k, v in [
                ("board", board),
                ("board_fields", board_fields),
                ("card", card),
                ("card_fields", card_fields),
                ("display", display),
                ("entities", entities),
                ("fields", fields),
                ("list", list),
                ("member", member),
                ("member_fields", member_fields),
                ("memberCreator", memberCreator),
                ("memberCreator_fields", memberCreator_fields),
                ("organization", organization),
                ("organization_fields", organization_fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_notifications_id(self, id: str, unread: bool | None = None) -> Any:
        """
        Update a Notification's read status

        Args:
            id (string): id
            unread (boolean): Whether the notification should be marked as read or not

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/notifications/{id}"
        query_params = {k: v for k, v in [("unread", unread)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_notifications_id_field(self, id: str, field: str) -> Any:
        """
        Get a field of a Notification

        Args:
            id (string): id
            field (string): field

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        url = f"{self.base_url}/notifications/{id}/{field}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_notifications_all_read(
        self, read: bool | None = None, ids: list[str] | None = None
    ) -> Any:
        """
        Mark all Notifications as read

        Args:
            read (boolean): Boolean to specify whether to mark as read or unread (defaults to `true`, marking as read)
            ids (array): A comma-seperated list of IDs. Allows specifying an array of notification IDs to change the read state for. This will become useful as we add grouping of notifications to the UI, with a single button to mark all notifications in the group as read/unread.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/notifications/all/read"
        query_params = {
            k: v for k, v in [("read", read), ("ids", ids)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_notifications_id_unread(self, id: str, value: str | None = None) -> Any:
        """
        Update Notification's read status

        Args:
            id (string): id
            value (string): The "value" query parameter optionally specifies the new unread status as a string for the notification identified by {id}.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/notifications/{id}/unread"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_notifications_id_board(self, id: str, fields: str | None = None) -> Any:
        """
        Get the Board a Notification is on

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of board[fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/notifications/{id}/board"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_notifications_id_card(self, id: str, fields: str | None = None) -> Any:
        """
        Get the Card a Notification is on

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/notifications/{id}/card"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_notifications_id_list(self, id: str, fields: str | None = None) -> Any:
        """
        Get the List a Notification is on

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/notifications/{id}/list"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def notificationsidmember(self, id: str, fields: str | None = None) -> Any:
        """
        Get the Member a Notification is about (not the creator)

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/notifications/{id}/member"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_member_creator_details(self, id: str, fields: str | None = None) -> Any:
        """
        Get the Member who created the Notification

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/notifications/{id}/memberCreator"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_notification_org(self, id: str, fields: str | None = None) -> Any:
        """
        Get a Notification's associated Organization

        Args:
            id (string): id
            fields (string): `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/notifications/{id}/organization"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_organizations(
        self,
        displayName: str,
        desc: str | None = None,
        name: str | None = None,
        website: str | None = None,
    ) -> Any:
        """
        Create a new Organization

        Args:
            displayName (string): The name to display for the Organization
            desc (string): The description for the organizations
            name (string): A string with a length of at least 3. Only lowercase letters, underscores, and numbers are allowed. If the name contains invalid characters, they will be removed. If the name conflicts with an existing name, a new name will be substituted.
            website (string): A URL starting with ` or `

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/organizations"
        query_params = {
            k: v
            for k, v in [
                ("displayName", displayName),
                ("desc", desc),
                ("name", name),
                ("website", website),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organizations_id(self, id: str) -> dict[str, Any]:
        """
        Get an Organization

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_organizations_id(
        self,
        id: str,
        name: str | None = None,
        displayName: str | None = None,
        desc: str | None = None,
        website: str | None = None,
        prefs_associatedDomain: str | None = None,
        prefs_externalMembersDisabled: bool | None = None,
        prefs_googleAppsVersion: int | None = None,
        prefs_boardVisibilityRestrict_org: str | None = None,
        prefs_boardVisibilityRestrict_private: str | None = None,
        prefs_boardVisibilityRestrict_public: str | None = None,
        prefs_orgInviteRestrict: str | None = None,
        prefs_permissionLevel: str | None = None,
    ) -> dict[str, Any]:
        """
        Update an Organization

        Args:
            id (string): id
            name (string): A new name for the organization. At least 3 lowercase letters, underscores, and numbers. Must be unique
            displayName (string): A new displayName for the organization. Must be at least 1 character long and not begin or end with a space.
            desc (string): A new description for the organization
            website (string): A URL starting with ` ` or `null`
            prefs_associatedDomain (string): The Google Apps domain to link this org to.
            prefs_externalMembersDisabled (boolean): Whether non-workspace members can be added to boards inside the Workspace
            prefs_googleAppsVersion (integer): `1` or `2`
            prefs_boardVisibilityRestrict_org (string): Who on the Workspace can make Workspace visible boards. One of `admin`, `none`, `org`
            prefs_boardVisibilityRestrict_private (string): Who can make private boards. One of: `admin`, `none`, `org`
            prefs_boardVisibilityRestrict_public (string): Who on the Workspace can make public boards. One of: `admin`, `none`, `org`
            prefs_orgInviteRestrict (string): An email address with optional wildcard characters. (E.g. `subdomain.*.trello.com`)
            prefs_permissionLevel (string): Whether the Workspace page is publicly visible. One of: `private`, `public`

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/organizations/{id}"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("displayName", displayName),
                ("desc", desc),
                ("website", website),
                ("prefs/associatedDomain", prefs_associatedDomain),
                ("prefs/externalMembersDisabled", prefs_externalMembersDisabled),
                ("prefs/googleAppsVersion", prefs_googleAppsVersion),
                (
                    "prefs/boardVisibilityRestrict/org",
                    prefs_boardVisibilityRestrict_org,
                ),
                (
                    "prefs/boardVisibilityRestrict/private",
                    prefs_boardVisibilityRestrict_private,
                ),
                (
                    "prefs/boardVisibilityRestrict/public",
                    prefs_boardVisibilityRestrict_public,
                ),
                ("prefs/orgInviteRestrict", prefs_orgInviteRestrict),
                ("prefs/permissionLevel", prefs_permissionLevel),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_organizations_id(self, id: str) -> Any:
        """
        Delete an Organization

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organizations_id_field(self, id: str, field: str) -> dict[str, Any]:
        """
        Get field on Organization

        Args:
            id (string): id
            field (string): field

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        url = f"{self.base_url}/organizations/{id}/{field}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organizations_id_actions(self, id: str) -> list[Any]:
        """
        Get Actions for Organization

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/actions"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organizations_id_boards(
        self, id: str, filter: str | None = None, fields: str | None = None
    ) -> list[Any]:
        """
        Get Boards in an Organization

        Args:
            id (string): id
            filter (string): `all` or a comma-separated list of: `open`, `closed`, `members`, `organization`, `public`
            fields (string): `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/)

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/boards"
        query_params = {
            k: v for k, v in [("filter", filter), ("fields", fields)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_organizations_id_exports(
        self, id: str, attachments: bool | None = None
    ) -> dict[str, Any]:
        """
        Create Export for Organizations

        Args:
            id (string): id
            attachments (boolean): Whether the CSV should include attachments or not.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/organizations/{id}/exports"
        query_params = {
            k: v for k, v in [("attachments", attachments)] if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organizations_id_exports(self, id: str) -> list[Any]:
        """
        Retrieve Organization's Exports

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/exports"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organizations_id_members(self, id: str) -> list[Any]:
        """
        Get the Members of an Organization

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/members"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_organizations_id_members(
        self, id: str, email: str, fullName: str, type: str | None = None
    ) -> Any:
        """
        Update an Organization's Members

        Args:
            id (string): id
            email (string): An email address
            fullName (string): Name for the member, at least 1 character not beginning or ending with a space
            type (string): One of: `admin`, `normal`

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/organizations/{id}/members"
        query_params = {
            k: v
            for k, v in [("email", email), ("fullName", fullName), ("type", type)]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organization_memberships(
        self, id: str, filter: str | None = None, member: bool | None = None
    ) -> list[Any]:
        """
        Get Memberships of an Organization

        Args:
            id (string): id
            filter (string): `all` or a comma-separated list of: `active`, `admin`, `deactivated`, `me`, `normal`
            member (boolean): Whether to include the Member objects with the Memberships

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/memberships"
        query_params = {
            k: v for k, v in [("filter", filter), ("member", member)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_membership_details(
        self, id: str, idMembership: str, member: bool | None = None
    ) -> Any:
        """
        Get a Membership of an Organization

        Args:
            id (string): id
            idMembership (string): idMembership
            member (boolean): Whether to include the Member object in the response

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMembership is None:
            raise ValueError("Missing required parameter 'idMembership'.")
        url = f"{self.base_url}/organizations/{id}/memberships/{idMembership}"
        query_params = {k: v for k, v in [("member", member)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organization_plugin_data_by_id(self, id: str) -> list[Any]:
        """
        Get the pluginData Scoped to Organization

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/pluginData"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_organizations_id_tags(self, id: str) -> list[Any]:
        """
        Get Tags of an Organization

        Args:
            id (string): id

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_organizations_id_tags(self, id: str) -> Any:
        """
        Create a Tag in Organization

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/organizations/{id}/tags"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_member_type(self, id: str, idMember: str, type: str) -> Any:
        """
        Update a Member of an Organization

        Args:
            id (string): id
            idMember (string): idMember
            type (string): One of: `admin`, `normal`

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        request_body_data = None
        url = f"{self.base_url}/organizations/{id}/members/{idMember}"
        query_params = {k: v for k, v in [("type", type)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def remove_organization_member(self, id: str, idMember: str) -> Any:
        """
        Remove a Member from an Organization

        Args:
            id (string): id
            idMember (string): idMember

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        url = f"{self.base_url}/organizations/{id}/members/{idMember}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def deactivate_member_org(self, id: str, idMember: str, value: bool) -> Any:
        """
        Deactivate or reactivate a member of an Organization

        Args:
            id (string): id
            idMember (string): idMember
            value (boolean): Indicates whether the member is deactivated, with `true` deactivating the member and `false` reactivating them.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        request_body_data = None
        url = f"{self.base_url}/organizations/{id}/members/{idMember}/deactivated"
        query_params = {k: v for k, v in [("value", value)] if v is not None}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_organizations_id_logo(self, id: str, file: bytes | None = None) -> Any:
        """
        Update logo for an Organization

        Args:
            id (string): id
            file (string): Image file for the logo

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/organizations/{id}/logo"
        query_params = {k: v for k, v in [("file", file)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_organizations_id_logo(self, id: str) -> Any:
        """
        Delete Logo for Organization

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/logo"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_organization_member_all(self, id: str, idMember: str) -> Any:
        """
        Remove a Member from an Organization and all Organization Boards

        Args:
            id (string): id
            idMember (string): idMember

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idMember is None:
            raise ValueError("Missing required parameter 'idMember'.")
        url = f"{self.base_url}/organizations/{id}/members/{idMember}/all"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_associated_domain(self, id: str) -> Any:
        """
        Remove the associated Google Apps domain from a Workspace

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/prefs/associatedDomain"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_org_invite_restrict_by_id(self, id: str) -> Any:
        """
        Delete the email domain restriction on who can be invited to the Workspace

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/organizations/{id}/prefs/orgInviteRestrict"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_organization_tag_by_id_tag(self, id: str, idTag: str) -> Any:
        """
        Delete an Organization's Tag

        Args:
            id (string): id
            idTag (string): idTag

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idTag is None:
            raise ValueError("Missing required parameter 'idTag'.")
        url = f"{self.base_url}/organizations/{id}/tags/{idTag}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_guests_by_board(self, id: str, idBoard: str) -> Any:
        """
        Get Organizations new billable guests

        Args:
            id (string): id
            idBoard (string): idBoard

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if idBoard is None:
            raise ValueError("Missing required parameter 'idBoard'.")
        url = f"{self.base_url}/organizations/{id}/newBillableGuests/{idBoard}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_plugins_id(self, id: str) -> dict[str, Any]:
        """
        Get a Plugin

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/plugins/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_plugins_id(self, id: str) -> dict[str, Any]:
        """
        Update a Plugin

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/plugins/{id}/"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_plugins_idplugin_listing(
        self,
        idPlugin: str,
        description: str | None = None,
        locale: str | None = None,
        overview: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a Listing for Plugin

        Args:
            idPlugin (string): idPlugin
            description (string): The description to show for the given locale
            locale (string): The locale that this listing should be displayed for.
            overview (string): The overview to show for the given locale.
            name (string): The name to use for the given locale.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idPlugin is None:
            raise ValueError("Missing required parameter 'idPlugin'.")
        request_body_data = None
        request_body_data = {
            "description": description,
            "locale": locale,
            "overview": overview,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/plugins/{idPlugin}/listing"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_member_privacy_compliance(self, id: str) -> Any:
        """
        Get Plugin's Member privacy compliance

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/plugins/{id}/compliance/memberPrivacy"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def update_plugin_listing(
        self,
        idPlugin: str,
        idListing: str,
        description: str | None = None,
        locale: str | None = None,
        overview: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Updating Plugin's Listing

        Args:
            idPlugin (string): idPlugin
            idListing (string): idListing
            description (string): The description to show for the given locale
            locale (string): The locale that this listing should be displayed for.
            overview (string): The overview to show for the given locale.
            name (string): The name to use for the given locale.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if idPlugin is None:
            raise ValueError("Missing required parameter 'idPlugin'.")
        if idListing is None:
            raise ValueError("Missing required parameter 'idListing'.")
        request_body_data = None
        request_body_data = {
            "description": description,
            "locale": locale,
            "overview": overview,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/plugins/{idPlugin}/listings/{idListing}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_search(
        self,
        query: str,
        idBoards: Any | None = None,
        idOrganizations: str | None = None,
        idCards: str | None = None,
        modelTypes: str | None = None,
        board_fields: str | None = None,
        boards_limit: int | None = None,
        board_organization: bool | None = None,
        card_fields: str | None = None,
        cards_limit: int | None = None,
        cards_page: float | None = None,
        card_board: bool | None = None,
        card_list: bool | None = None,
        card_members: bool | None = None,
        card_stickers: bool | None = None,
        card_attachments: str | None = None,
        organization_fields: str | None = None,
        organizations_limit: int | None = None,
        member_fields: str | None = None,
        members_limit: int | None = None,
        partial: bool | None = None,
    ) -> list[Any]:
        """
        Search Trello

        Args:
            query (string): The search query with a length of 1 to 16384 characters
            idBoards (string): `mine` or a comma-separated list of Board IDs
            idOrganizations (string): A comma-separated list of Organization IDs
            idCards (string): A comma-separated list of Card IDs
            modelTypes (string): What type or types of Trello objects you want to search. all or a comma-separated list of: `actions`, `boards`, `cards`, `members`, `organizations`
            board_fields (string): all or a comma-separated list of: `closed`, `dateLastActivity`, `dateLastView`, `desc`, `descData`, `idOrganization`, `invitations`, `invited`, `labelNames`, `memberships`, `name`, `pinned`, `powerUps`, `prefs`, `shortLink`, `shortUrl`, `starred`, `subscribed`, `url`
            boards_limit (integer): The maximum number of boards returned. Maximum: 1000
            board_organization (boolean): Whether to include the parent organization with board results
            card_fields (string): all or a comma-separated list of: `badges`, `checkItemStates`, `closed`, `dateLastActivity`, `desc`, `descData`, `due`, `idAttachmentCover`, `idBoard`, `idChecklists`, `idLabels`, `idList`, `idMembers`, `idMembersVoted`, `idShort`, `labels`, `manualCoverAttachment`, `name`, `pos`, `shortLink`, `shortUrl`, `subscribed`, `url`
            cards_limit (integer): The maximum number of cards to return. Maximum: 1000
            cards_page (number): The page of results for cards. Maximum: 100
            card_board (boolean): Whether to include the parent board with card results
            card_list (boolean): Whether to include the parent list with card results
            card_members (boolean): Whether to include member objects with card results
            card_stickers (boolean): Whether to include sticker objects with card results
            card_attachments (string): Whether to include attachment objects with card results. A boolean value (true or false) or cover for only card cover attachments.
            organization_fields (string): all or a comma-separated list of billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url, website
            organizations_limit (integer): The maximum number of Workspaces to return. Maximum 1000
            member_fields (string): all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username
            members_limit (integer): The maximum number of members to return. Maximum 1000
            partial (boolean): By default, Trello searches for each word in your query against exactly matching words within Member content. Specifying partial to be true means that we will look for content that starts with any of the words in your query. If you are looking for a Card titled "My Development Status Report", by default you would need to search for "Development". If you have partial enabled, you will be able to search for "dev" but not "velopment".

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Search, important
        """
        url = f"{self.base_url}/search"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("idBoards", idBoards),
                ("idOrganizations", idOrganizations),
                ("idCards", idCards),
                ("modelTypes", modelTypes),
                ("board_fields", board_fields),
                ("boards_limit", boards_limit),
                ("board_organization", board_organization),
                ("card_fields", card_fields),
                ("cards_limit", cards_limit),
                ("cards_page", cards_page),
                ("card_board", card_board),
                ("card_list", card_list),
                ("card_members", card_members),
                ("card_stickers", card_stickers),
                ("card_attachments", card_attachments),
                ("organization_fields", organization_fields),
                ("organizations_limit", organizations_limit),
                ("member_fields", member_fields),
                ("members_limit", members_limit),
                ("partial", partial),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_search_members(
        self,
        query: str,
        limit: int | None = None,
        idBoard: str | None = None,
        idOrganization: str | None = None,
        onlyOrgMembers: bool | None = None,
    ) -> list[Any]:
        """
        Search for Members

        Args:
            query (string): Search query 1 to 16384 characters long
            limit (integer): The maximum number of results to return. Maximum of 20.
            idBoard (string): Optional parameter to filter search results by a specific board ID. Example: '5abbe4b7ddc1b351ef961414'.
            idOrganization (string): The optional query parameter to filter members by the ID of their organization. Example: '5abbe4b7ddc1b351ef961414'.
            onlyOrgMembers (boolean): A boolean flag indicating whether to return only members of the organization; defaults to false.

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        url = f"{self.base_url}/search/members/"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("limit", limit),
                ("idBoard", idBoard),
                ("idOrganization", idOrganization),
                ("onlyOrgMembers", onlyOrgMembers),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_tokens_token(
        self, token: str, fields: str | None = None, webhooks: bool | None = None
    ) -> dict[str, Any]:
        """
        Get a Token

        Args:
            token (string): token
            fields (string): `all` or a comma-separated list of `dateCreated`, `dateExpires`, `idMember`, `identifier`, `permissions`
            webhooks (boolean): Determines whether to include webhooks.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'.")
        url = f"{self.base_url}/tokens/{token}"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("webhooks", webhooks)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_tokens_token_member(
        self, token: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Get Token's Member

        Args:
            token (string): token
            fields (string): `all` or a comma-separated list of valid fields for [Member Object](/cloud/trello/guides/rest-api/object-definitions/).

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'.")
        url = f"{self.base_url}/tokens/{token}/member"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_tokens_token_webhooks(self, token: str) -> list[Any]:
        """
        Get Webhooks for Token

        Args:
            token (string): token

        Returns:
            list[Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'.")
        url = f"{self.base_url}/tokens/{token}/webhooks"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_tokens_token_webhooks(
        self,
        token: str,
        callbackURL: str,
        idModel: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        """
        Create Webhooks for Token

        Args:
            token (string): token
            callbackURL (string): The URL that the webhook should POST information to.
            idModel (string): ID of the object to create a webhook on. Example: '5abbe4b7ddc1b351ef961414'.
            description (string): A description to be displayed when retrieving information about the webhook.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'.")
        request_body_data = None
        url = f"{self.base_url}/tokens/{token}/webhooks"
        query_params = {
            k: v
            for k, v in [
                ("description", description),
                ("callbackURL", callbackURL),
                ("idModel", idModel),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_webhook_by_id(self, token: str, idWebhook: str) -> dict[str, Any]:
        """
        Get a Webhook belonging to a Token

        Args:
            token (string): token
            idWebhook (string): idWebhook

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'.")
        if idWebhook is None:
            raise ValueError("Missing required parameter 'idWebhook'.")
        url = f"{self.base_url}/tokens/{token}/webhooks/{idWebhook}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_webhook_by_id(self, token: str, idWebhook: str) -> Any:
        """
        Delete a Webhook created by Token

        Args:
            token (string): token
            idWebhook (string): idWebhook

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'.")
        if idWebhook is None:
            raise ValueError("Missing required parameter 'idWebhook'.")
        url = f"{self.base_url}/tokens/{token}/webhooks/{idWebhook}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def tokenstokenwebhooks(
        self,
        token: str,
        idWebhook: str,
        description: str | None = None,
        callbackURL: str | None = None,
        idModel: str | None = None,
    ) -> Any:
        """
        Update a Webhook created by Token

        Args:
            token (string): token
            idWebhook (string): idWebhook
            description (string): A description to be displayed when retrieving information about the webhook.
            callbackURL (string): The URL that the webhook should `POST` information to.
            idModel (string): ID of the object that the webhook is on. Example: '5abbe4b7ddc1b351ef961414'.

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'.")
        if idWebhook is None:
            raise ValueError("Missing required parameter 'idWebhook'.")
        request_body_data = None
        url = f"{self.base_url}/tokens/{token}/webhooks/{idWebhook}"
        query_params = {
            k: v
            for k, v in [
                ("description", description),
                ("callbackURL", callbackURL),
                ("idModel", idModel),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_token(self, token: str) -> Any:
        """
        Delete a Token

        Args:
            token (string): token

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if token is None:
            raise ValueError("Missing required parameter 'token'.")
        url = f"{self.base_url}/tokens/{token}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_webhooks(
        self,
        callbackURL: str,
        idModel: str,
        description: str | None = None,
        active: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create a Webhook

        Args:
            callbackURL (string): A valid URL that is reachable with a `HEAD` and `POST` request.
            idModel (string): ID of the model to be monitored Example: '5abbe4b7ddc1b351ef961414'.
            description (string): A string with a length from `0` to `16384`.
            active (boolean): Determines whether the webhook is active and sending `POST` requests.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/webhooks/"
        query_params = {
            k: v
            for k, v in [
                ("description", description),
                ("callbackURL", callbackURL),
                ("idModel", idModel),
                ("active", active),
            ]
            if v is not None
        }
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_webhooks_id(self, id: str) -> dict[str, Any]:
        """
        Get a Webhook

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/webhooks/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_webhooks_id(
        self,
        id: str,
        description: str | None = None,
        callbackURL: str | None = None,
        idModel: str | None = None,
        active: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update a Webhook

        Args:
            id (string): id
            description (string): A string with a length from `0` to `16384`.
            callbackURL (string): A valid URL that is reachable with a `HEAD` and `POST` request.
            idModel (string): ID of the model to be monitored Example: '5abbe4b7ddc1b351ef961414'.
            active (boolean): Determines whether the webhook is active and sending `POST` requests.

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/webhooks/{id}"
        query_params = {
            k: v
            for k, v in [
                ("description", description),
                ("callbackURL", callbackURL),
                ("idModel", idModel),
                ("active", active),
            ]
            if v is not None
        }
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_webhooks_id(self, id: str) -> Any:
        """
        Delete a Webhook

        Args:
            id (string): id

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/webhooks/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def webhooksidfield(self, id: str, field: str) -> Any:
        """
        Get a field on a Webhook

        Args:
            id (string): id
            field (string): field

        Returns:
            Any: Success

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        if field is None:
            raise ValueError("Missing required parameter 'field'.")
        url = f"{self.base_url}/webhooks/{id}/{field}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_tools(self):
        return [
            self.get_actions_id,
            self.put_actions_id,
            self.delete_actions_id,
            self.get_actions_id_field,
            self.get_actions_id_board,
            self.get_actions_id_card,
            self.get_actions_id_list,
            self.get_actions_id_member,
            self.get_actions_id_membercreator,
            self.get_actions_id_organization,
            self.put_actions_id_text,
            self.get_actions_idaction_reactions,
            self.create_reaction_to_action,
            self.get_action_reaction_by_id,
            self.delete_reaction_by_id_action,
            self.get_action_reactions_summary,
            self.applications_key_compliance,
            self.get_batch,
            self.get_boards_id_memberships,
            self.get_boards_id,
            self.put_boards_id,
            self.delete_boards_id,
            self.get_boards_id_field,
            self.get_boards_id_actions,
            self.get_boards_id_boardstars,
            self.boards_id_checklists,
            self.get_boards_id_cards,
            self.get_boards_id_cards_filter,
            self.get_boards_id_customfields,
            self.get_boards_id_labels,
            self.post_boards_id_labels,
            self.get_boards_id_lists,
            self.post_boards_id_lists,
            self.get_boards_id_lists_filter,
            self.get_boards_id_members,
            self.put_boards_id_members,
            self.put_boards_id_members_idmember,
            self.boardsidmembersidmember,
            self.update_membership,
            self.update_board_email_position,
            self.update_board_my_prefs_id_email_list,
            self.update_board_sidebar_pref,
            self.update_board_sidebar_act_pref,
            self.update_board_sidebar_actions,
            self.update_board_prefs_show_members,
            self.post_boards,
            self.generate_calendar_key,
            self.generate_board_email_key,
            self.post_boards_id_idtags,
            self.post_boards_id_markedasviewed,
            self.get_boards_id_boardplugins,
            self.post_boards_id_boardplugins,
            self.delete_boards_id_boardplugins,
            self.get_board_id_plugins,
            self.post_cards,
            self.get_cards_id,
            self.put_cards_id,
            self.delete_cards_id,
            self.get_cards_id_field,
            self.get_cards_id_actions,
            self.get_cards_id_attachments,
            self.post_cards_id_attachments,
            self.get_attachment_by_id,
            self.delete_attachment_by_id,
            self.get_cards_id_board,
            self.get_cards_id_checkitemstates,
            self.get_cards_id_checklists,
            self.post_cards_id_checklists,
            self.check_card_item,
            self.update_card_check_item,
            self.delete_card_check_item,
            self.get_cards_id_list,
            self.get_cards_id_members,
            self.get_cards_id_membersvoted,
            self.cardsidmembersvoted,
            self.get_cards_id_plugindata,
            self.get_cards_id_stickers,
            self.post_cards_id_stickers,
            self.get_card_sticker,
            self.delete_sticker_by_id,
            self.update_card_sticker_by_id_sticker,
            self.update_card_action_comment,
            self.delete_comment_action,
            self.update_card_custom_field_item,
            self.put_cards_idcard_customfields,
            self.get_cards_id_customfielditems,
            self.post_cards_id_actions_comments,
            self.post_cards_id_idlabels,
            self.post_cards_id_idmembers,
            self.post_cards_id_labels,
            self.mark_notifications_read,
            self.delete_card_id_label_by_id,
            self.delete_id_idmembers_idmember,
            self.delete_card_voter,
            self.update_check_item,
            self.delete_checklist_by_id,
            self.post_checklists,
            self.get_checklists_id,
            self.put_checlists_id,
            self.delete_checklists_id,
            self.get_checklists_id_field,
            self.put_checklists_id_field,
            self.get_checklists_id_board,
            self.get_checklists_id_cards,
            self.get_checklists_id_checkitems,
            self.post_checklists_id_checkitems,
            self.get_check_item_detail,
            self.delete_checklist_item_by_id,
            self.post_customfields,
            self.get_customfields_id,
            self.put_customfields_id,
            self.delete_customfields_id,
            self.get_customfields_id_options,
            self.post_customfields_id_options,
            self.get_custom_field_option_by_id,
            self.delete_custom_field_option,
            self.emoji,
            self.get_enterprises_id,
            self.get_enterprises_id_auditlog,
            self.get_enterprises_id_admins,
            self.get_enterprises_id_signupurl,
            self.get_users_id,
            self.get_enterprises_id_members,
            self.get_member_details,
            self.get_organization_transfer,
            self.list_enterprise_transferrables_by_org_ids,
            self.bulk_join_enterprise_requests,
            self.list_claimable_orgs,
            self.get_pending_organizations,
            self.post_enterprises_id_tokens,
            self.put_enterprise_organizations_by_id,
            self.update_enterprise_member_licensed,
            self.deactivate_member,
            self.update_admin_member,
            self.delete_enterprise_admin_by_id,
            self.delete_organization_by_id_and_org_id,
            self.get_bulk_organizations_by_ids,
            self.get_labels_id,
            self.put_labels_id,
            self.delete_labels_id,
            self.put_labels_id_field,
            self.post_labels,
            self.get_lists_id,
            self.put_lists_id,
            self.post_lists,
            self.post_lists_id_archiveallcards,
            self.post_lists_id_moveallcards,
            self.put_lists_id_closed,
            self.put_id_idboard,
            self.put_lists_id_field,
            self.get_lists_id_actions,
            self.get_lists_id_board,
            self.get_lists_id_cards,
            self.get_members_id,
            self.put_members_id,
            self.get_members_id_field,
            self.get_members_id_actions,
            self.get_board_backgrounds_by_id,
            self.create_board_background,
            self.get_member_board_backgrounds,
            self.update_board_background,
            self.delete_board_background_by_id,
            self.get_members_id_boardstars,
            self.post_members_id_boardstars,
            self.get_board_star_by_id,
            self.update_board_star_position,
            self.delete_board_star,
            self.get_members_id_boards,
            self.get_members_id_boardsinvited,
            self.get_members_id_cards,
            self.get_custom_board_backgrounds_by_id,
            self.set_custom_board_backgrounds,
            self.get_custom_board_backgrounds_by_id_back,
            self.update_member_custom_board_background,
            self.delete_custom_background_by_id,
            self.get_members_id_customemoji,
            self.post_members_id_customemoji,
            self.membersidcustomemojiidemoji,
            self.get_members_id_customstickers,
            self.post_members_id_customstickers,
            self.get_member_custom_sticker_by_id,
            self.delete_member_custom_sticker_by_id,
            self.get_members_id_notifications,
            self.get_members_id_organizations,
            self.get_member_organizations_invited,
            self.get_members_id_savedsearches,
            self.post_members_id_savedsearches,
            self.get_saved_searches_by_id,
            self.update_member_saved_search,
            self.delete_saved_search,
            self.get_members_id_tokens,
            self.membersidavatar,
            self.post_member_one_time_messages_dismissed,
            self.get_member_notifications_channel_settings,
            self.update_notification_channel_settings,
            self.get_member_notification_channel_settings,
            self.update_member_notification_channel_settings,
            self.update_notification_settings,
            self.get_notifications_id,
            self.put_notifications_id,
            self.get_notifications_id_field,
            self.post_notifications_all_read,
            self.put_notifications_id_unread,
            self.get_notifications_id_board,
            self.get_notifications_id_card,
            self.get_notifications_id_list,
            self.notificationsidmember,
            self.get_member_creator_details,
            self.get_notification_org,
            self.post_organizations,
            self.get_organizations_id,
            self.put_organizations_id,
            self.delete_organizations_id,
            self.get_organizations_id_field,
            self.get_organizations_id_actions,
            self.get_organizations_id_boards,
            self.post_organizations_id_exports,
            self.get_organizations_id_exports,
            self.get_organizations_id_members,
            self.put_organizations_id_members,
            self.get_organization_memberships,
            self.get_membership_details,
            self.get_organization_plugin_data_by_id,
            self.get_organizations_id_tags,
            self.post_organizations_id_tags,
            self.update_member_type,
            self.remove_organization_member,
            self.deactivate_member_org,
            self.post_organizations_id_logo,
            self.delete_organizations_id_logo,
            self.delete_organization_member_all,
            self.delete_associated_domain,
            self.delete_org_invite_restrict_by_id,
            self.delete_organization_tag_by_id_tag,
            self.get_guests_by_board,
            self.get_plugins_id,
            self.put_plugins_id,
            self.post_plugins_idplugin_listing,
            self.get_member_privacy_compliance,
            self.update_plugin_listing,
            self.get_search,
            self.get_search_members,
            self.get_tokens_token,
            self.get_tokens_token_member,
            self.get_tokens_token_webhooks,
            self.post_tokens_token_webhooks,
            self.get_webhook_by_id,
            self.delete_webhook_by_id,
            self.tokenstokenwebhooks,
            self.delete_token,
            self.post_webhooks,
            self.get_webhooks_id,
            self.put_webhooks_id,
            self.delete_webhooks_id,
            self.webhooksidfield,
        ]
