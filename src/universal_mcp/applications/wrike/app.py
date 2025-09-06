from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class WrikeApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        """
        Initializes the OfficialWrikeCollectionV21App with a specified integration and additional keyword arguments.

        Args:
            integration: Integration, optional. The integration instance to associate with this app. Defaults to None.
            **kwargs: Additional keyword arguments passed to the superclass initializer.

        Returns:
            None. This constructor initializes the instance in place.
        """
        super().__init__(name="wrike", integration=integration, **kwargs)
        self.base_url = "https://www.wrike.com/api/v4"

    def get_contacts(self, deleted=None, fields=None, metadata=None) -> Any:
        """
        Retrieves contacts from the server with optional deleted status filtering, field selection, and metadata inclusion.

        Args:
            deleted: Optional[bool]. Filters contacts by deletion status. When None, returns contacts regardless of deletion status.
            fields: Optional[str]. Comma-separated fields to include in each contact's response. Limits returned contact fields.
            metadata: Optional[str]. Comma-separated metadata fields to include in each contact's response.

        Returns:
            JSON-decoded response from server containing contact data, typically as a list or dictionary based on API structure.

        Raises:
            HTTPError: Raised when the server returns a non-success status code, typically due to invalid parameters or server errors.

        Tags:
            retrieve, contacts, filter, api, important
        """
        url = f"{self.base_url}/contacts"
        query_params = {
            k: v
            for k, v in [
                ("deleted", deleted),
                ("fields", fields),
                ("metadata", metadata),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_contacts_by_contactid(self, contactId, fields=None) -> Any:
        """
        Retrieves contact information for a specific contact ID, optionally returning only specified fields.

        Args:
            contactId: The unique identifier of the contact to retrieve. Must not be None.
            fields: Optional; a comma-separated string specifying which fields to include in the response. If None, all fields are returned.

        Returns:
            A JSON-decoded object containing the contact's details as returned by the API.

        Raises:
            ValueError: Raised when the 'contactId' parameter is missing.

        Tags:
            retrieve, contact-management
        """
        if contactId is None:
            raise ValueError("Missing required parameter 'contactId'")
        url = f"{self.base_url}/contacts/{contactId}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_contacts_by_contactid(
        self,
        contactId,
        metadata=None,
        currentBillRate=None,
        currentCostRate=None,
        jobRoleId=None,
        customFields=None,
        fields=None,
    ) -> Any:
        """
        Updates an existing contact using the specified contact ID with provided details including metadata, billing/cost rates, job role, and custom fields.

        Args:
            contactId: The unique identifier of the contact to update (required).
            metadata: Optional dictionary containing metadata for the contact.
            currentBillRate: Optional current billing rate associated with the contact.
            currentCostRate: Optional current cost rate associated with the contact.
            jobRoleId: Optional identifier for the contact's job role.
            customFields: Optional dictionary of custom field values for the contact.
            fields: Optional list of field names to include in the response.

        Returns:
            JSON-decoded response containing updated contact details from the API.

        Raises:
            ValueError: When contactId parameter is not provided.
            requests.HTTPError: When the API request fails due to client (4xx) or server (5xx) errors.

        Tags:
            update, contact, async-job, management
        """
        if contactId is None:
            raise ValueError("Missing required parameter 'contactId'")
        request_body = {
            "metadata": metadata,
            "currentBillRate": currentBillRate,
            "currentCostRate": currentCostRate,
            "jobRoleId": jobRoleId,
            "customFields": customFields,
            "fields": fields,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/contacts/{contactId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_by_userid(self, userId) -> Any:
        """
        Retrieves user information by ID from the API endpoint.

        Args:
            userId: The unique identifier of the user to retrieve (required).

        Returns:
            JSON-decoded dictionary containing user details from the API response.

        Raises:
            ValueError: Raised when userId is None or missing.
            HTTPError: Raised when the API request fails (non-2xx status code).

        Tags:
            retrieve, user-info, api, management
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'")
        url = f"{self.base_url}/users/{userId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_users_by_userid(self, userId, profile=None) -> Any:
        """
        Updates a user's profile information by user ID using a PUT request.

        Args:
            userId: The unique identifier of the user. Must not be None.
            profile: Optional. The profile information to update for the user. If None, no profile data is sent.

        Returns:
            The parsed JSON response from the server after updating the user's information.

        Raises:
            ValueError: Raised when the 'userId' parameter is missing.
            HTTPError: Raised if the HTTP request to the server fails.

        Tags:
            update, user-management
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'")
        request_body = {
            "profile": profile,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/{userId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_groups(
        self, metadata=None, pageSize=None, pageToken=None, fields=None
    ) -> Any:
        """
        Retrieves a list of groups from the API, applying optional filtering and pagination parameters.

        Args:
            metadata: Optional metadata to include or filter by in the group results.
            pageSize: The maximum number of groups to return in the response.
            pageToken: A token identifying the page of results to return, for pagination.
            fields: Selector specifying a subset of fields to include in the response.

        Returns:
            A JSON-compatible object, typically a dictionary containing group information.

        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.

        Tags:
            list, management, important
        """
        url = f"{self.base_url}/groups"
        query_params = {
            k: v
            for k, v in [
                ("metadata", metadata),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("fields", fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_groups(
        self, title, members=None, parent=None, avatar=None, metadata=None
    ) -> Any:
        """
        Creates a new group with the specified title and optional details via a POST request to the groups endpoint.

        Args:
            title: The name of the group to create. This parameter is required.
            members: Optional list of member identifiers to include in the group.
            parent: Optional identifier of the parent group.
            avatar: Optional avatar image or data to associate with the group.
            metadata: Optional dictionary of additional metadata or custom fields for the group.

        Returns:
            A dictionary containing the response data representing the created group.

        Raises:
            ValueError: Raised when the required 'title' parameter is missing.

        Tags:
            create, group-management
        """
        if title is None:
            raise ValueError("Missing required parameter 'title'")
        request_body = {
            "title": title,
            "members": members,
            "parent": parent,
            "avatar": avatar,
            "metadata": metadata,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/groups"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_groups_by_groupid(self, groupId, fields=None) -> Any:
        """
        Retrieves details for a specific group by its group ID, optionally returning only specified fields.

        Args:
            groupId: The unique identifier of the group to retrieve.
            fields: Optional; a comma-separated list of fields to include in the response.

        Returns:
            A dictionary containing the group details as returned by the API.

        Raises:
            ValueError: Raised if the groupId parameter is missing.

        Tags:
            retrieve, group-management, data-fetch
        """
        if groupId is None:
            raise ValueError("Missing required parameter 'groupId'")
        url = f"{self.base_url}/groups/{groupId}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_groups_by_groupid(
        self,
        groupId,
        title=None,
        addMembers=None,
        removeMembers=None,
        addInvitations=None,
        removeInvitations=None,
        parent=None,
        avatar=None,
        metadata=None,
    ) -> Any:
        """
        Updates an existing group by groupId with new properties and membership changes via a PUT request.

        Args:
            groupId: The unique identifier of the group to update. Required.
            title: Optional new title for the group.
            addMembers: Optional list of member identifiers to add to the group.
            removeMembers: Optional list of member identifiers to remove from the group.
            addInvitations: Optional list of invitations to add to the group.
            removeInvitations: Optional list of invitations to remove from the group.
            parent: Optional new parent group identifier for hierarchy changes.
            avatar: Optional new avatar for the group, typically a URL or encoded image data.
            metadata: Optional additional metadata to attach to the group.

        Returns:
            A dict containing the updated group details from the server response.

        Raises:
            ValueError: Raised if the required 'groupId' parameter is missing.

        Tags:
            update, group-management, membership
        """
        if groupId is None:
            raise ValueError("Missing required parameter 'groupId'")
        request_body = {
            "title": title,
            "addMembers": addMembers,
            "removeMembers": removeMembers,
            "addInvitations": addInvitations,
            "removeInvitations": removeInvitations,
            "parent": parent,
            "avatar": avatar,
            "metadata": metadata,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/groups/{groupId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_groups_by_groupid(self, groupId) -> Any:
        """
        Deletes a group resource identified by the provided groupId using an HTTP DELETE request.

        Args:
            groupId: The unique identifier of the group to be deleted.

        Returns:
            The JSON-decoded response from the API after deleting the group.

        Raises:
            ValueError: Raised if the groupId is None.

        Tags:
            delete, group-management, api-call
        """
        if groupId is None:
            raise ValueError("Missing required parameter 'groupId'")
        url = f"{self.base_url}/groups/{groupId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_groups_bulk(self, members) -> Any:
        """
        Updates multiple group memberships in bulk by sending a PUT request with the given member data.

        Args:
            members: List or collection of member data to be processed in bulk. Must not be None.

        Returns:
            Parsed JSON response from the API containing the result of the bulk update operation.

        Raises:
            ValueError: Raised when the required 'members' parameter is missing or None.

        Tags:
            bulk, update, management
        """
        if members is None:
            raise ValueError("Missing required parameter 'members'")
        request_body = {
            "members": members,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/groups_bulk"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_invitations(
        self,
    ) -> Any:
        """
        Retrieves all invitations from the server using a GET request.

        Args:
            None: This function takes no arguments.

        Returns:
            Any: JSON-decoded response containing invitation data.

        Raises:
            requests.HTTPError: Raised if the HTTP request fails (non-2xx status code).

        Tags:
            retrieve, list, invitations, async_job
        """
        url = f"{self.base_url}/invitations"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_invitations(
        self,
        email,
        firstName=None,
        lastName=None,
        role=None,
        external=None,
        subject=None,
        message=None,
        userTypeId=None,
    ) -> Any:
        """
        Sends an invitation email to a user with optional details such as name, role, and custom message.

        Args:
            email: The email address of the user to invite. Required.
            firstName: The first name of the invitee. Optional.
            lastName: The last name of the invitee. Optional.
            role: The role to assign to the invited user. Optional.
            external: Indicates if the invitation is for an external user. Optional.
            subject: Custom subject line for the invitation email. Optional.
            message: Custom message to include in the invitation. Optional.
            userTypeId: The user type identifier to associate with the invitation. Optional.

        Returns:
            The server's parsed JSON response to the invitation request.

        Raises:
            ValueError: Raised if the required 'email' parameter is missing.

        Tags:
            invite, email, invitation, user-management
        """
        if email is None:
            raise ValueError("Missing required parameter 'email'")
        request_body = {
            "email": email,
            "firstName": firstName,
            "lastName": lastName,
            "role": role,
            "external": external,
            "subject": subject,
            "message": message,
            "userTypeId": userTypeId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/invitations"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_invitations_by_invitationid(
        self, invitationId, resend=None, role=None, external=None, userTypeId=None
    ) -> Any:
        """
        Updates an existing invitation by its unique ID with optional parameters, handling conditional updates and API communication.

        Args:
            invitationId: The unique identifier of the invitation to update (required).
            resend: Optional boolean indicating whether to resend the invitation.
            role: Optional role assignment for the invitation recipient.
            external: Optional flag marking the invitation as external/internal.
            userTypeId: Optional identifier specifying the user type for the invitation.

        Returns:
            Dictionary containing the updated invitation resource from the API.

        Raises:
            ValueError: When 'invitationId' is not provided.
            HTTPError: When the API request fails (raised via response.raise_for_status()).

        Tags:
            update, invitation, api, async-job, management
        """
        if invitationId is None:
            raise ValueError("Missing required parameter 'invitationId'")
        request_body = {
            "resend": resend,
            "role": role,
            "external": external,
            "userTypeId": userTypeId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/invitations/{invitationId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_invitations_by_invitationid(self, invitationId) -> Any:
        """
        Deletes a specific invitation using its unique identifier

        Args:
            invitationId: The unique identifier of the invitation to delete (required)

        Returns:
            JSON-decoded response containing the API result after deletion

        Raises:
            ValueError: Raised when invitationId is not provided
            requests.exceptions.HTTPError: Raised for HTTP request failures (e.g., invalid invitation ID or network issues)

        Tags:
            delete, invitation, api, management
        """
        if invitationId is None:
            raise ValueError("Missing required parameter 'invitationId'")
        url = f"{self.base_url}/invitations/{invitationId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_a_ccount(self, fields=None) -> Any:
        """
        Retrieves account information from the API, optionally including only specified fields.

        Args:
            fields: Optional string. A comma-separated string of field names to include in the response. If None, all default fields are returned.

        Returns:
            The JSON-decoded response from the API containing account details.

        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns an unsuccessful status code.

        Tags:
            retrieve, account, api
        """
        url = f"{self.base_url}/account"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_a_ccount(self, metadata=None) -> Any:
        """
        Sends a PUT request to update or create an account with the provided metadata and returns the server response as a JSON object.

        Args:
            metadata: Optional metadata to associate with the account. If provided, included in the request body. Must match the server's expected schema. Defaults to None.

        Returns:
            JSON-decoded Python object representing the server's response from the account API endpoint.

        Raises:
            HTTPError: Raised if the HTTP request fails (e.g., due to invalid metadata format, network issues, or server errors).

        Tags:
            put, account, metadata, async_job
        """
        request_body = {
            "metadata": metadata,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/account"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_workflows(
        self,
    ) -> Any:
        """
        Retrieves all workflows from the server using a GET request.

        Args:
            None: This function takes no arguments

        Returns:
            The parsed JSON response containing the list of workflows.

        Raises:
            requests.RequestException: Raised if there's a problem with the HTTP request to the server.

        Tags:
            list, fetch, workflows, management, important
        """
        url = f"{self.base_url}/workflows"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_workflows(self, name=None, request_body=None) -> Any:
        """
        Creates a new workflow by sending a POST request to the workflows endpoint with optional name and request body.

        Args:
            name: Optional; name of the workflow to create, included as a query parameter if provided.
            request_body: Optional; request body containing workflow details, provided as the data payload for the POST request.

        Returns:
            JSON-decoded response from the server containing details of the created workflow.

        Raises:
            HTTPError: Raised when the server returns a 4XX/5XX status code, indicating a failed request.

        Tags:
            post, create, workflow, async_job, management
        """
        url = f"{self.base_url}/workflows"
        query_params = {k: v for k, v in [("name", name)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_workflows_by_workflowid(
        self, workflowId, name=None, hidden=None, request_body=None
    ) -> Any:
        """
        Updates an existing workflow by workflow ID with optional name, hidden status, and request body data.

        Args:
            workflowId: The unique identifier of the workflow to update. Required.
            name: An optional new name for the workflow. If provided, updates the workflow's name.
            hidden: An optional boolean indicating whether the workflow should be hidden.
            request_body: Optional data to include in the request body when updating the workflow.

        Returns:
            The updated workflow as a JSON-decoded Python object.

        Raises:
            ValueError: Raised when the 'workflowId' parameter is missing.

        Tags:
            update, workflow, management
        """
        if workflowId is None:
            raise ValueError("Missing required parameter 'workflowId'")
        url = f"{self.base_url}/workflows/{workflowId}"
        query_params = {
            k: v for k, v in [("name", name), ("hidden", hidden)] if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_customfields(
        self,
    ) -> Any:
        """
        Retrieves all custom fields from the API and returns them as a parsed JSON object.

        Args:
            None: This function takes no arguments.

        Returns:
            The JSON-decoded response content containing the list of custom fields, typically as a Python dict or list, depending on the API response structure.

        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returned an unsuccessful status code.

        Tags:
            fetch, api_call, data_retrieval
        """
        url = f"{self.base_url}/customfields"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_customfields(
        self,
        title,
        type,
        spaceId=None,
        sharing=None,
        shareds=None,
        settings=None,
        request_body=None,
    ) -> Any:
        """
        Creates a custom field by sending a POST request to the customfields endpoint with the specified parameters.

        Args:
            title: The name of the custom field to be created.
            type: The type of the custom field to be created.
            spaceId: Optional identifier of the space to associate with the custom field.
            sharing: Optional sharing settings for the custom field.
            shareds: Optional users or groups the custom field is shared with.
            settings: Optional additional settings for the custom field in string or JSON format.
            request_body: Optional request body payload to include in the POST request.

        Returns:
            The JSON response data representing the created custom field.

        Raises:
            ValueError: Raised when either 'title' or 'type' is missing.

        Tags:
            create, custom-field, management, api-request
        """
        if title is None:
            raise ValueError("Missing required parameter 'title'")
        if type is None:
            raise ValueError("Missing required parameter 'type'")
        url = f"{self.base_url}/customfields"
        query_params = {
            k: v
            for k, v in [
                ("title", title),
                ("type", type),
                ("spaceId", spaceId),
                ("sharing", sharing),
                ("shareds", shareds),
                ("settings", settings),
            ]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_customfields_by_customfieldid(self, customFieldId) -> Any:
        """
        Retrieves details for a custom field by its unique identifier from the API

        Args:
            customFieldId: The unique identifier of the custom field to retrieve

        Returns:
            A JSON-decoded response containing the custom field details

        Raises:
            ValueError: Raised when the 'customFieldId' parameter is missing or None

        Tags:
            retrieve, api, custom-field
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'")
        url = f"{self.base_url}/customfields/{customFieldId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_customfields_by_customfieldid(
        self,
        customFieldId,
        title=None,
        type=None,
        changeScope=None,
        spaceId=None,
        sharing=None,
        addShareds=None,
        removeShareds=None,
        settings=None,
        addMirrors=None,
        removeMirrors=None,
    ) -> Any:
        """
        Updates a custom field specified by its ID with the provided parameters.

        Args:
            customFieldId: The unique identifier of the custom field to update.
            title: Optional new title for the custom field.
            type: Optional new field type.
            changeScope: Optional scope for tracking or permission changes.
            spaceId: Optional identifier of the space associated with the custom field.
            sharing: Optional sharing configuration or permissions.
            addShareds: Optional list of users or entities to add to the shared list.
            removeShareds: Optional list of users or entities to remove from the shared list.
            settings: Optional dictionary with additional settings for the custom field.
            addMirrors: Optional list of entities to add as mirrors.
            removeMirrors: Optional list of entities to remove as mirrors.

        Returns:
            The server response as a JSON-decoded object containing the updated custom field data.

        Raises:
            ValueError: Raised when the required 'customFieldId' parameter is missing.

        Tags:
            update, custom-field, http-put, management
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'")
        url = f"{self.base_url}/customfields/{customFieldId}"
        query_params = {
            k: v
            for k, v in [
                ("title", title),
                ("type", type),
                ("changeScope", changeScope),
                ("spaceId", spaceId),
                ("sharing", sharing),
                ("addShareds", addShareds),
                ("removeShareds", removeShareds),
                ("settings", settings),
                ("addMirrors", addMirrors),
                ("removeMirrors", removeMirrors),
            ]
            if v is not None
        }
        response = self._put(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_customfields_by_customfieldid(self, customFieldId) -> Any:
        """
        Deletes a custom field resource identified by its custom field ID.

        Args:
            customFieldId: The unique identifier of the custom field to delete.

        Returns:
            The server response as a deserialized JSON object, typically containing the result of the delete operation.

        Raises:
            ValueError: Raised when the 'customFieldId' parameter is missing.

        Tags:
            delete, custom-field, management
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'")
        url = f"{self.base_url}/customfields/{customFieldId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_folders(
        self,
        permalink=None,
        descendants=None,
        metadata=None,
        customFields=None,
        updatedDate=None,
        withInvitations=None,
        project=None,
        deleted=None,
        contractTypes=None,
        plainTextCustomFields=None,
        customItemTypes=None,
        pageSize=None,
        nextPageToken=None,
        fields=None,
    ) -> Any:
        """
        Retrieves a list of folders from the API with support for filtering, pagination, and field selection.

        Args:
            permalink: Filter results by folder permalink.
            descendants: Include descendant folders if True.
            metadata: Filter folders by matching metadata fields.
            customFields: Filter results by custom field values.
            updatedDate: Only return folders updated on or after this date (ISO 8601 format).
            withInvitations: If True, include folders with active invitations.
            project: Filter folders by associated project identifier.
            deleted: Include deleted folders in the response if True.
            contractTypes: Filter folders by contract types.
            plainTextCustomFields: Filter by plain text custom fields.
            customItemTypes: Filter folders by custom item types.
            pageSize: Maximum number of results to return per page.
            nextPageToken: Token to retrieve the next page of results.
            fields: Specify which fields to include in the response.

        Returns:
            A JSON-decoded response from the API containing folder data and related metadata.

        Raises:
            requests.HTTPError: Raised if an HTTP error occurs during the API request.

        Tags:
            retrieve, list, filter, pagination, api-call, folders, metadata
        """
        url = f"{self.base_url}/folders"
        query_params = {
            k: v
            for k, v in [
                ("permalink", permalink),
                ("descendants", descendants),
                ("metadata", metadata),
                ("customFields", customFields),
                ("updatedDate", updatedDate),
                ("withInvitations", withInvitations),
                ("project", project),
                ("deleted", deleted),
                ("contractTypes", contractTypes),
                ("plainTextCustomFields", plainTextCustomFields),
                ("customItemTypes", customItemTypes),
                ("pageSize", pageSize),
                ("nextPageToken", nextPageToken),
                ("fields", fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_folders_by_folderid_folders(
        self,
        folderId,
        permalink=None,
        descendants=None,
        metadata=None,
        customFields=None,
        updatedDate=None,
        withInvitations=None,
        project=None,
        contractTypes=None,
        plainTextCustomFields=None,
        customItemTypes=None,
        pageSize=None,
        nextPageToken=None,
        fields=None,
    ) -> Any:
        """
        Retrieves subfolders of a specified folder, applying optional filters and pagination parameters.

        Args:
            folderId: The unique identifier of the parent folder whose subfolders are to be retrieved. Required.
            permalink: Filter results to subfolders with the specified permalink.
            descendants: If True, include descendant folders recursively in the results.
            metadata: Filter subfolders by associated metadata.
            customFields: Filter subfolders by custom field values.
            updatedDate: Filter subfolders updated on or after the specified date.
            withInvitations: If True, include invitation information with subfolders.
            project: Filter subfolders belonging to a specific project.
            contractTypes: Filter subfolders by contract types.
            plainTextCustomFields: Filter subfolders by plain text custom fields.
            customItemTypes: Filter subfolders by custom item types.
            pageSize: Maximum number of subfolders to return per request, for pagination.
            nextPageToken: Token for retrieving the next page of results.
            fields: Specify fields to include in the response for each folder.

        Returns:
            A JSON object containing the list of subfolders matching the criteria, along with pagination tokens and any requested metadata.

        Raises:
            ValueError: Raised if the required 'folderId' parameter is missing.

        Tags:
            folder-management, list, filter, pagination
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        url = f"{self.base_url}/folders/{folderId}/folders"
        query_params = {
            k: v
            for k, v in [
                ("permalink", permalink),
                ("descendants", descendants),
                ("metadata", metadata),
                ("customFields", customFields),
                ("updatedDate", updatedDate),
                ("withInvitations", withInvitations),
                ("project", project),
                ("contractTypes", contractTypes),
                ("plainTextCustomFields", plainTextCustomFields),
                ("customItemTypes", customItemTypes),
                ("pageSize", pageSize),
                ("nextPageToken", nextPageToken),
                ("fields", fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_folders_by_folderid_folders(
        self,
        folderId,
        title,
        description=None,
        shareds=None,
        metadata=None,
        customFields=None,
        customColumns=None,
        project=None,
        userAccessRoles=None,
        withInvitations=None,
        customItemTypeId=None,
        plainTextCustomFields=None,
        fields=None,
    ) -> Any:
        """
        Creates a new subfolder within a specified folder by folder ID, with configurable attributes such as title, description, sharing, metadata, and permissions.

        Args:
            folderId: The ID of the parent folder in which to create the new subfolder. Required.
            title: The title of the new subfolder. Required.
            description: An optional description for the subfolder.
            shareds: Optional list of user or group IDs to share the subfolder with.
            metadata: Optional metadata to associate with the subfolder.
            customFields: Optional custom fields to set for the subfolder.
            customColumns: Optional custom columns configuration.
            project: Optional project identifier to associate with the subfolder.
            userAccessRoles: Optional list of user access roles to assign to the subfolder.
            withInvitations: If True, send invitations to shared users or groups. Optional.
            customItemTypeId: Optional custom item type identifier for the subfolder.
            plainTextCustomFields: Optional plain text custom fields to set for the subfolder.
            fields: Optional list of specific fields to include in the response.

        Returns:
            The newly created subfolder object as returned by the API.

        Raises:
            ValueError: Raised when either of the required parameters 'folderId' or 'title' is missing.

        Tags:
            create, subfolder, folder, management
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        if title is None:
            raise ValueError("Missing required parameter 'title'")
        request_body = {
            "title": title,
            "description": description,
            "shareds": shareds,
            "metadata": metadata,
            "customFields": customFields,
            "customColumns": customColumns,
            "project": project,
            "userAccessRoles": userAccessRoles,
            "withInvitations": withInvitations,
            "customItemTypeId": customItemTypeId,
            "plainTextCustomFields": plainTextCustomFields,
            "fields": fields,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/folders/{folderId}/folders"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_folders_by_folderid(self, folderId) -> Any:
        """
        Deletes a folder resource identified by its folder ID via an HTTP DELETE request.

        Args:
            folderId: The unique identifier of the folder to delete. Must not be None.

        Returns:
            The parsed JSON response from the server if the deletion is successful.

        Raises:
            ValueError: Raised when the folder ID is missing (i.e., None).
            HTTPError: Raised if the HTTP request fails.

        Tags:
            delete, folders, async_job, management
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        url = f"{self.base_url}/folders/{folderId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_folders_by_folderid(
        self,
        folderId,
        title=None,
        description=None,
        addParents=None,
        removeParents=None,
        addShareds=None,
        removeShareds=None,
        metadata=None,
        restore=None,
        customFields=None,
        customColumns=None,
        clearCustomColumns=None,
        project=None,
        addAccessRoles=None,
        removeAccessRoles=None,
        withInvitations=None,
        convertToCustomItemType=None,
        plainTextCustomFields=None,
        fields=None,
    ) -> Any:
        """
        Updates a folder's properties and relationships using a PUT request, allowing comprehensive modifications including metadata, access roles, and parent associations.

        Args:
            folderId: str. The unique identifier of the folder to update (required).
            title: str, optional. New title for the folder.
            description: str, optional. Updated description of the folder.
            addParents: list or str, optional. Parent folder IDs to add to this folder.
            removeParents: list or str, optional. Parent folder IDs to remove from this folder.
            addShareds: list or str, optional. Accounts to share this folder with.
            removeShareds: list or str, optional. Shared accounts to remove from this folder.
            metadata: dict, optional. Additional metadata to update for the folder.
            restore: bool, optional. Whether to restore a deleted folder.
            customFields: dict, optional. Custom fields and their values to set or update.
            customColumns: dict, optional. Custom columns and their values to set or update.
            clearCustomColumns: list or str, optional. Custom column fields to clear.
            project: str, optional. Associated project identifier for the folder.
            addAccessRoles: list or str, optional. Access role IDs to add to the folder.
            removeAccessRoles: list or str, optional. Access role IDs to remove from the folder.
            withInvitations: bool, optional. Whether to send invitations on access role changes.
            convertToCustomItemType: str, optional. Converts the folder to a specific custom item type.
            plainTextCustomFields: dict, optional. Plain text fields to update.
            fields: str or list, optional. Specific fields to include in the response.

        Returns:
            dict. JSON response containing updated folder information from the API.

        Raises:
            ValueError: Raised when 'folderId' is not provided.
            HTTPError: Raised for HTTP request failures (4XX/5XX status codes).

        Tags:
            update, folder, put-request, async-job, management, metadata, access-control
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        request_body = {
            "title": title,
            "description": description,
            "addParents": addParents,
            "removeParents": removeParents,
            "addShareds": addShareds,
            "removeShareds": removeShareds,
            "metadata": metadata,
            "restore": restore,
            "customFields": customFields,
            "customColumns": customColumns,
            "clearCustomColumns": clearCustomColumns,
            "project": project,
            "addAccessRoles": addAccessRoles,
            "removeAccessRoles": removeAccessRoles,
            "withInvitations": withInvitations,
            "convertToCustomItemType": convertToCustomItemType,
            "plainTextCustomFields": plainTextCustomFields,
            "fields": fields,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/folders/{folderId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks(
        self,
        descendants=None,
        title=None,
        status=None,
        importance=None,
        startDate=None,
        dueDate=None,
        scheduledDate=None,
        createdDate=None,
        updatedDate=None,
        completedDate=None,
        authors=None,
        responsibles=None,
        responsiblePlaceholders=None,
        permalink=None,
        type=None,
        limit=None,
        sortField=None,
        sortOrder=None,
        subTasks=None,
        pageSize=None,
        nextPageToken=None,
        metadata=None,
        customField=None,
        customFields=None,
        customStatuses=None,
        withInvitations=None,
        billingTypes=None,
        plainTextCustomFields=None,
        customItemTypes=None,
        fields=None,
    ) -> Any:
        """
        Retrieves tasks from the API with optional filtering, sorting, pagination, and field selection parameters.

        Args:
            descendants: Optional; filter tasks by descendant items or folders.
            title: Optional; filter tasks by title.
            status: Optional; filter tasks by their status.
            importance: Optional; filter tasks by importance level.
            startDate: Optional; filter tasks by their start date.
            dueDate: Optional; filter tasks by due date.
            scheduledDate: Optional; filter tasks by scheduled date.
            createdDate: Optional; filter tasks by creation date.
            updatedDate: Optional; filter tasks by last updated date.
            completedDate: Optional; filter tasks by completion date.
            authors: Optional; filter tasks by author(s).
            responsibles: Optional; filter tasks by responsible user(s).
            responsiblePlaceholders: Optional; filter by responsible placeholders.
            permalink: Optional; filter tasks by their permalink.
            type: Optional; filter tasks by type.
            limit: Optional; limit the number of returned tasks.
            sortField: Optional; field to sort the tasks by.
            sortOrder: Optional; sort order ('asc' or 'desc').
            subTasks: Optional; filter tasks by whether they are sub-tasks.
            pageSize: Optional; number of tasks per page.
            nextPageToken: Optional; token for retrieving the next page of results.
            metadata: Optional; include or filter by metadata.
            customField: Optional; filter by a specific custom field.
            customFields: Optional; filter tasks by custom fields.
            customStatuses: Optional; filter tasks by custom workflow statuses.
            withInvitations: Optional; include tasks with invitations.
            billingTypes: Optional; filter tasks by billing types.
            plainTextCustomFields: Optional; specify if custom fields should be plain text.
            customItemTypes: Optional; filter by custom item types.
            fields: Optional; select specific fields to include in the result.

        Returns:
            The JSON-decoded API response containing a list of tasks and related metadata.

        Raises:
            requests.exceptions.HTTPError: Raised when the API request returns an unsuccessful status code.

        Tags:
            list, filter, api_call, async_job_support, management
        """
        url = f"{self.base_url}/tasks"
        query_params = {
            k: v
            for k, v in [
                ("descendants", descendants),
                ("title", title),
                ("status", status),
                ("importance", importance),
                ("startDate", startDate),
                ("dueDate", dueDate),
                ("scheduledDate", scheduledDate),
                ("createdDate", createdDate),
                ("updatedDate", updatedDate),
                ("completedDate", completedDate),
                ("authors", authors),
                ("responsibles", responsibles),
                ("responsiblePlaceholders", responsiblePlaceholders),
                ("permalink", permalink),
                ("type", type),
                ("limit", limit),
                ("sortField", sortField),
                ("sortOrder", sortOrder),
                ("subTasks", subTasks),
                ("pageSize", pageSize),
                ("nextPageToken", nextPageToken),
                ("metadata", metadata),
                ("customField", customField),
                ("customFields", customFields),
                ("customStatuses", customStatuses),
                ("withInvitations", withInvitations),
                ("billingTypes", billingTypes),
                ("plainTextCustomFields", plainTextCustomFields),
                ("customItemTypes", customItemTypes),
                ("fields", fields),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_by_taskid(self, taskId, fields=None) -> Any:
        """
        Retrieves a task by its ID from the remote service, optionally returning only specified fields.

        Args:
            taskId: The unique identifier of the task to retrieve.
            fields: Optional. A comma-separated string specifying which fields to include in the response. If None, all available fields are returned.

        Returns:
            The JSON-decoded response data containing task details, as returned by the remote API.

        Raises:
            ValueError: Raised when the required 'taskId' parameter is missing.

        Tags:
            task, retrieve, api, management
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'")
        url = f"{self.base_url}/tasks/{taskId}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_tasks_by_taskid(
        self,
        taskId,
        title=None,
        description=None,
        status=None,
        importance=None,
        dates=None,
        addParents=None,
        removeParents=None,
        addShareds=None,
        removeShareds=None,
        addResponsibles=None,
        removeResponsibles=None,
        addResponsiblePlaceholders=None,
        removeResponsiblePlaceholders=None,
        addFollowers=None,
        follow=None,
        priorityBefore=None,
        priorityAfter=None,
        addSuperTasks=None,
        removeSuperTasks=None,
        metadata=None,
        customFields=None,
        customStatus=None,
        restore=None,
        effortAllocation=None,
        billingType=None,
        withInvitations=None,
        convertToCustomItemType=None,
        plainTextCustomFields=None,
        fields=None,
    ) -> Any:
        """
        Updates a task's properties and relationships by ID, returning the updated task data.

        Args:
            taskId: The unique identifier of the task to update (required).
            title: The new title for the task.
            description: The new description for the task.
            status: The new status identifier for the task.
            importance: The importance level identifier to assign.
            dates: Dictionary containing task date updates (e.g., due date, start date).
            addParents: List of parent task IDs to add to this task.
            removeParents: List of parent task IDs to remove from this task.
            addShareds: List of user IDs to add as shared users.
            removeShareds: List of user IDs to remove from shared users.
            addResponsibles: List of user IDs to add as responsible users.
            removeResponsibles: List of user IDs to remove from responsible users.
            addResponsiblePlaceholders: Placeholder IDs to add to responsible users.
            removeResponsiblePlaceholders: Placeholder IDs to remove from responsible users.
            addFollowers: User IDs to add as followers.
            follow: If True/False, follows or unfollows the task.
            priorityBefore: Task ID before which to prioritize this task.
            priorityAfter: Task ID after which to prioritize this task.
            addSuperTasks: Task IDs to add as super tasks.
            removeSuperTasks: Task IDs to remove from super tasks.
            metadata: Arbitrary metadata key-value pairs to associate.
            customFields: List of custom field update objects.
            customStatus: Custom status identifier to apply.
            restore: If True, restores a deleted task.
            effortAllocation: Effort allocation data objects.
            billingType: Billing type identifier to set.
            withInvitations: If True, sends invitations to new shared/responsible users.
            convertToCustomItemType: Identifier to convert task to custom item type.
            plainTextCustomFields: Plain text values for custom fields.
            fields: List of fields to include in the response.

        Returns:
            Dictionary containing updated task details from the server response.

        Raises:
            ValueError: When taskId parameter is not provided.
            HTTPError: When the API request fails (e.g., invalid parameters or server errors).

        Tags:
            update, task-management, async, api, rest, batch
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'")
        request_body = {
            "title": title,
            "description": description,
            "status": status,
            "importance": importance,
            "dates": dates,
            "addParents": addParents,
            "removeParents": removeParents,
            "addShareds": addShareds,
            "removeShareds": removeShareds,
            "addResponsibles": addResponsibles,
            "removeResponsibles": removeResponsibles,
            "addResponsiblePlaceholders": addResponsiblePlaceholders,
            "removeResponsiblePlaceholders": removeResponsiblePlaceholders,
            "addFollowers": addFollowers,
            "follow": follow,
            "priorityBefore": priorityBefore,
            "priorityAfter": priorityAfter,
            "addSuperTasks": addSuperTasks,
            "removeSuperTasks": removeSuperTasks,
            "metadata": metadata,
            "customFields": customFields,
            "customStatus": customStatus,
            "restore": restore,
            "effortAllocation": effortAllocation,
            "billingType": billingType,
            "withInvitations": withInvitations,
            "convertToCustomItemType": convertToCustomItemType,
            "plainTextCustomFields": plainTextCustomFields,
            "fields": fields,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{taskId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tasks_by_taskid(self, taskId) -> Any:
        """
        Deletes a task identified by the given task ID via an HTTP DELETE request and returns the response as a JSON object.

        Args:
            taskId: The unique identifier of the task to be deleted. Must not be None.

        Returns:
            A JSON object containing the API response to the delete operation.

        Raises:
            ValueError: Raised when the required parameter 'taskId' is None.
            HTTPError: Raised if the HTTP DELETE request fails (e.g., invalid task ID or server error).

        Tags:
            delete, http, async_job, management
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'")
        url = f"{self.base_url}/tasks/{taskId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_folders_by_folderid_tasks(
        self,
        folderId,
        title,
        description=None,
        status=None,
        importance=None,
        dates=None,
        shareds=None,
        parents=None,
        responsibles=None,
        responsiblePlaceholders=None,
        followers=None,
        follow=None,
        priorityBefore=None,
        priorityAfter=None,
        superTasks=None,
        metadata=None,
        customFields=None,
        customStatus=None,
        effortAllocation=None,
        billingType=None,
        withInvitations=None,
        customItemTypeId=None,
        plainTextCustomFields=None,
        fields=None,
    ) -> Any:
        """
        Creates a new task in a specified folder with configurable attributes including title, description, assignments, and custom fields.

        Args:
            folderId: str or int. Required ID of the folder where the task is created.
            title: str. Required title of the task.
            description: str, optional. Detailed task description.
            status: str, optional. Task status (e.g., 'active', 'completed').
            importance: str or int, optional. Importance level of the task.
            dates: dict or list, optional. Date-related details (e.g., start/due dates).
            shareds: list, optional. Users to share the task with.
            parents: list, optional. Parent task IDs if this is a subtask.
            responsibles: list, optional. Users responsible for the task.
            responsiblePlaceholders: list, optional. Placeholder users assigned as responsible.
            followers: list, optional. Users to follow task updates.
            follow: bool, optional. Whether the current user should follow the task.
            priorityBefore: str or int, optional. ID of task to prioritize before.
            priorityAfter: str or int, optional. ID of task to prioritize after.
            superTasks: list, optional. IDs of super tasks this task belongs to.
            metadata: dict, optional. Arbitrary metadata attached to the task.
            customFields: dict or list, optional. Custom field values.
            customStatus: str, optional. Custom status value.
            effortAllocation: dict or list, optional. Effort allocation details.
            billingType: str, optional. Billing details/type.
            withInvitations: bool, optional. Send invitations to added users.
            customItemTypeId: str or int, optional. Custom item type identifier.
            plainTextCustomFields: dict or list, optional. Plain text custom fields.
            fields: list or str, optional. Fields to include in the API response.

        Returns:
            dict. JSON response containing details of the created task.

        Raises:
            ValueError: If 'folderId' or 'title' parameters are missing.
            HTTPError: If the API request fails (via response.raise_for_status()).

        Tags:
            create, task-management, async-job, api-integration
        """
        if folderId is None:
            raise ValueError("Missing required parameter 'folderId'")
        if title is None:
            raise ValueError("Missing required parameter 'title'")
        request_body = {
            "title": title,
            "description": description,
            "status": status,
            "importance": importance,
            "dates": dates,
            "shareds": shareds,
            "parents": parents,
            "responsibles": responsibles,
            "responsiblePlaceholders": responsiblePlaceholders,
            "followers": followers,
            "follow": follow,
            "priorityBefore": priorityBefore,
            "priorityAfter": priorityAfter,
            "superTasks": superTasks,
            "metadata": metadata,
            "customFields": customFields,
            "customStatus": customStatus,
            "effortAllocation": effortAllocation,
            "billingType": billingType,
            "withInvitations": withInvitations,
            "customItemTypeId": customItemTypeId,
            "plainTextCustomFields": plainTextCustomFields,
            "fields": fields,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/folders/{folderId}/tasks"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_contacts,
            self.get_contacts_by_contactid,
            self.put_contacts_by_contactid,
            self.get_users_by_userid,
            self.put_users_by_userid,
            self.get_groups,
            self.post_groups,
            self.get_groups_by_groupid,
            self.put_groups_by_groupid,
            self.delete_groups_by_groupid,
            self.put_groups_bulk,
            self.get_invitations,
            self.post_invitations,
            self.put_invitations_by_invitationid,
            self.delete_invitations_by_invitationid,
            self.get_a_ccount,
            self.put_a_ccount,
            self.get_workflows,
            self.post_workflows,
            self.put_workflows_by_workflowid,
            self.get_customfields,
            self.post_customfields,
            self.get_customfields_by_customfieldid,
            self.put_customfields_by_customfieldid,
            self.delete_customfields_by_customfieldid,
            self.get_folders,
            self.get_folders_by_folderid_folders,
            self.post_folders_by_folderid_folders,
            self.delete_folders_by_folderid,
            self.put_folders_by_folderid,
            self.get_tasks,
            self.get_tasks_by_taskid,
            self.put_tasks_by_taskid,
            self.delete_tasks_by_taskid,
            self.post_folders_by_folderid_tasks,
        ]
