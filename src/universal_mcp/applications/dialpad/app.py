from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class DialpadApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="dialpad", integration=integration, **kwargs)
        self.base_url = "https://dialpad.com/api/v2"

    def accesscontrolpolicies_assign(
        self, id, target_id=None, target_type=None, user_id=None
    ) -> dict[str, Any]:
        """
        Assigns an access control policy to a target entity using the provided policy ID and returns a success status.

        Args:
            id (string): id
            target_id (integer): Required if the policy is associated with a target (Office or Contact Center). Not required for a company level policy.
            target_type (string): Policy permissions applied at this target level. Defaults to company target type.
            user_id (integer): The user's id to be assigned to the policy.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            accesscontrolpolicies
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "target_id": target_id,
            "target_type": target_type,
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/accesscontrolpolicies/{id}/assign"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def accesscontrolpolicies_list(self, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of access control policies using the "GET" method, optionally paginating results with a cursor parameter.

        Args:
            cursor (string): A token that marks the current position in the paginated list, used to fetch the next page of access control policies.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            accesscontrolpolicies
        """
        url = f"{self.base_url}/api/v2/accesscontrolpolicies"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def accesscontrolpolicies_create(
        self,
        description=None,
        name=None,
        owner_id=None,
        permission_sets=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Creates a new access control policy using JSON data and returns a successful response upon completion.

        Args:
            description (string): [single-line only]

        Optional description for the policy. Max 200 characters.
            name (string): [single-line only]

        A human-readable display name for the policy. Max 50 characters.
            owner_id (integer): Owner for this policy i.e company admin.
            permission_sets (array): List of permission associated with this policy.
            target_type (string): Policy permissions applied at this target level. Defaults to company target type.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            accesscontrolpolicies
        """
        request_body = {
            "description": description,
            "name": name,
            "owner_id": owner_id,
            "permission_sets": permission_sets,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/accesscontrolpolicies"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def accesscontrolpolicies_delete(self, id) -> dict[str, Any]:
        """
        Deletes the specified access control policy identified by the provided ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            accesscontrolpolicies
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/accesscontrolpolicies/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def accesscontrolpolicies_get(self, id) -> dict[str, Any]:
        """
        Retrieves a specific access control policy by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            accesscontrolpolicies
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/accesscontrolpolicies/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def accesscontrolpolicies_update(
        self,
        id,
        description=None,
        name=None,
        permission_sets=None,
        state=None,
        user_id=None,
    ) -> dict[str, Any]:
        """
        Partially updates an existing access control policy by its ID using a JSON payload.

        Args:
            id (string): id
            description (string): [single-line only]

        Optional description for the policy.
            name (string): [single-line only]

        A human-readable display name for the policy.
            permission_sets (array): List of permission associated with this policy.
            state (string): Restore a deleted policy.
            user_id (integer): user id updating this policy. Must be a company admin

        Returns:
            dict[str, Any]: A successful response

        Tags:
            accesscontrolpolicies
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "description": description,
            "name": name,
            "permission_sets": permission_sets,
            "state": state,
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/accesscontrolpolicies/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def accesscontrolpolicies_assignments(self, id, cursor=None) -> dict[str, Any]:
        """
        Retrieves the assignments of an access control policy identified by the specified ID.

        Args:
            id (string): id
            cursor (string): A string token used to fetch the next page of results in cursor-based pagination, enabling efficient retrieval of large or changing datasets by marking the position in the result set.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            accesscontrolpolicies
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/accesscontrolpolicies/{id}/assignments"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def accesscontrolpolicies_unassign(
        self, id, target_id=None, target_type=None, unassign_all=None, user_id=None
    ) -> dict[str, Any]:
        """
        Unassigns an access control policy from a specified ID using a POST request, allowing for the removal of policy assignments based on the provided ID.

        Args:
            id (string): id
            target_id (integer): Required if the policy is associated with a target (Office or Contact Center). Not required for a company level policy or if unassign_all is True.
            target_type (string): Policy permissions applied at this target level. Defaults to company target type.
            unassign_all (boolean): Unassign all associated target groups from the user for a policy.
            user_id (integer): The user's id to be assigned to the policy.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            accesscontrolpolicies
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "target_id": target_id,
            "target_type": target_type,
            "unassign_all": unassign_all,
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/accesscontrolpolicies/{id}/unassign"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def app_settings_get(self, target_id=None, target_type=None) -> dict[str, Any]:
        """
        Retrieves application settings using the provided target ID and type from version 2 of the API.

        Args:
            target_id (integer): Optional integer query parameter to specify the target ID for filtering or retrieving specific app settings.
            target_type (string): Optional query parameter to specify the type of target entity, with allowed values including callcenter, callrouter, channel, coachinggroup, coachingteam, department, office, room, staffgroup, unknown, or user.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            app
        """
        url = f"{self.base_url}/api/v2/app/settings"
        query_params = {
            k: v
            for k, v in [("target_id", target_id), ("target_type", target_type)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def blockednumbers_add(self, numbers=None) -> Any:
        """
        Adds a phone number to the blocked numbers list using a JSON-formatted request body and returns a success status.

        Args:
            numbers (array): A list of E164 formatted numbers.

        Returns:
            Any: A successful response

        Tags:
            blockednumbers
        """
        request_body = {
            "numbers": numbers,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/blockednumbers/add"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def blockednumbers_get(self, number) -> dict[str, Any]:
        """
        Retrieves information about a specific blocked number identified by the given number parameter.

        Args:
            number (string): number

        Returns:
            dict[str, Any]: A successful response

        Tags:
            blockednumbers
        """
        if number is None:
            raise ValueError("Missing required parameter 'number'")
        url = f"{self.base_url}/api/v2/blockednumbers/{number}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def blockednumbers_remove(self, numbers=None) -> Any:
        """
        Removes a blocked number using the POST method, sending data in JSON format to the defined API endpoint and returns a status response.

        Args:
            numbers (array): A list of E164 formatted numbers.

        Returns:
            Any: A successful response

        Tags:
            blockednumbers
        """
        request_body = {
            "numbers": numbers,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/blockednumbers/remove"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def blockednumbers_list(self, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of blocked numbers using the provided cursor for pagination.

        Args:
            cursor (string): A string token used to fetch the next or previous page of results in cursor-based pagination, allowing for stable pagination through large datasets.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            blockednumbers
        """
        url = f"{self.base_url}/api/v2/blockednumbers"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_participants_add(self, id, participant=None) -> dict[str, Any]:
        """
        Adds participants to a call using the provided call ID.

        Args:
            id (string): id
            participant (string): New member of the call to add. Can be a number or a Target. In case of a target, it must have a primary number assigned.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            call
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "participant": participant,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/call/{id}/participants/add"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_get_call_info(self, id) -> dict[str, Any]:
        """
        Retrieves details of a call resource by its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            call
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/call/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_initiate_ivr_call(
        self,
        custom_data=None,
        outbound_caller_id=None,
        phone_number=None,
        target_id=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Initiates an outbound call to ring an IVR workflow by sending a POST request and returns a confirmation upon success[1].

        Args:
            custom_data (string): Extra data to associate with the call. This will be passed through to any subscribed call events.
            outbound_caller_id (string): The e164-formatted number shown to the call recipient (or "blocked").
            phone_number (string): The e164-formatted number to call.
            target_id (integer): The ID of a group that will be used to initiate the call.
            target_type (string): The type of a group that will be used to initiate the call.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            call
        """
        request_body = {
            "custom_data": custom_data,
            "outbound_caller_id": outbound_caller_id,
            "phone_number": phone_number,
            "target_id": target_id,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/call/initiate_ivr_call"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_list(
        self,
        cursor=None,
        started_after=None,
        started_before=None,
        target_id=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of calls using the provided query parameters for filtering by cursor, start time, end time, target ID, and target type, and returns the results.

        Args:
            cursor (string): A token or unique identifier used to fetch the next or previous page of results in a paginated response, allowing incremental traversal of the dataset.
            started_after (integer): Returns only calls that began after the specified Unix timestamp.
            started_before (integer): Optional integer parameter to filter calls that started before a specified timestamp.
            target_id (integer): Optional target ID to be used for the operation, specified as an integer value.
            target_type (string): Optional query parameter specifying the type of target for the call, with valid values including "callcenter," "callrouter," "channel," "coachinggroup," "coachingteam," "department," "office," "room," "staffgroup," "unknown," and "user."

        Returns:
            dict[str, Any]: A successful response

        Tags:
            call
        """
        url = f"{self.base_url}/api/v2/call"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("started_after", started_after),
                ("started_before", started_before),
                ("target_id", target_id),
                ("target_type", target_type),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_call(
        self,
        custom_data=None,
        device_id=None,
        group_id=None,
        group_type=None,
        is_consult=None,
        outbound_caller_id=None,
        phone_number=None,
        user_id=None,
    ) -> dict[str, Any]:
        """
        Initiates a call using a JSON payload and returns a successful response upon completion.

        Args:
            custom_data (string): Extra data to associate with the call. This will be passed through to any subscribed call events.
            device_id (string): The device's id.
            group_id (integer): The ID of a group that will be used to initiate the call.
            group_type (string): The type of a group that will be used to initiate the call.
            is_consult (boolean): Enables the creation of a second call. If there is an ongoing call, it puts it on hold.
            outbound_caller_id (string): The e164-formatted number shown to the call recipient (or "blocked").

        If set to "blocked", the recipient will receive a call from "unknown caller". The number can be the caller's number, or the caller's group number if the group is provided, or the caller's company reserved number.
            phone_number (string): The e164-formatted number to call.
            user_id (integer): The id of the user who should make the outbound call.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            call
        """
        request_body = {
            "custom_data": custom_data,
            "device_id": device_id,
            "group_id": group_id,
            "group_type": group_type,
            "is_consult": is_consult,
            "outbound_caller_id": outbound_caller_id,
            "phone_number": phone_number,
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/call"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_transfer_call(
        self, id, custom_data=None, to=None, transfer_state=None
    ) -> dict[str, Any]:
        """
        Transfers a call identified by the provided ID using the POST method, sending the request body in JSON format.

        Args:
            id (string): id
            custom_data (string): Extra data to associate with the call. This will be passed through to any subscribed call events.
            to (string): Destination of the call that will be transfer. It can be a single option between a number,
        an existing call or a target
            transfer_state (string): The state which the call should take when it's transferred to.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            call
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "custom_data": custom_data,
            "to": to,
            "transfer_state": transfer_state,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/call/{id}/transfer"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_unpark(self, id, user_id=None) -> dict[str, Any]:
        """
        Unparks a call with the specified ID using the POST method.

        Args:
            id (string): id
            user_id (integer): The id of the user who should unpark the call.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            call
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/call/{id}/unpark"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_actions_hangup(self, id) -> Any:
        """
        Hangs up a call with the specified ID using the PUT method.

        Args:
            id (string): id

        Returns:
            Any: A successful response

        Tags:
            call
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/call/{id}/actions/hangup"
        query_params = {}
        response = self._put(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_put_call_labels(self, id, labels=None) -> dict[str, Any]:
        """
        Updates the labels of a call with the specified ID using the provided JSON data.

        Args:
            id (string): id
            labels (array): The list of labels to attach to the call

        Returns:
            dict[str, Any]: A successful response

        Tags:
            call
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "labels": labels,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/call/{id}/labels"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_callback(self, call_center_id=None, phone_number=None) -> dict[str, Any]:
        """
        Registers a callback endpoint using a POST request to the "/api/v2/callback" path, accepting a JSON payload in the request body, and returns a successful response upon registration.

        Args:
            call_center_id (integer): The ID of a call center that will be used to fulfill the callback.
            phone_number (string): The e164-formatted number to call back

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callback
        """
        request_body = {
            "call_center_id": call_center_id,
            "phone_number": phone_number,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callback"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_validate_callback(
        self, call_center_id=None, phone_number=None
    ) -> dict[str, Any]:
        """
        Validates a callback using the provided JSON data and returns a success response if the validation is successful.

        Args:
            call_center_id (integer): The ID of a call center that will be used to fulfill the callback.
            phone_number (string): The e164-formatted number to call back

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callback
        """
        request_body = {
            "call_center_id": call_center_id,
            "phone_number": phone_number,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callback/validate"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_listall(
        self, cursor=None, office_id=None, name_search=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of call centers using the specified query parameters, such as cursor for pagination, office_id for filtering by office, and name_search for searching by name.

        Args:
            cursor (string): The cursor query parameter is an optional string used for cursor-based pagination to specify the position in the dataset from which to continue fetching the next page of results.
            office_id (integer): Optional integer parameter to filter call centers by a specific office ID.
            name_search (string): Filters call centers by name using partial string matching (case-insensitive unless otherwise specified).

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        url = f"{self.base_url}/api/v2/callcenters"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("office_id", office_id),
                ("name_search", name_search),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_create(
        self,
        advanced_settings=None,
        alerts=None,
        friday_hours=None,
        group_description=None,
        hold_queue=None,
        hours_on=None,
        monday_hours=None,
        name=None,
        office_id=None,
        ring_seconds=None,
        routing_options=None,
        saturday_hours=None,
        sunday_hours=None,
        thursday_hours=None,
        tuesday_hours=None,
        voice_intelligence=None,
        wednesday_hours=None,
    ) -> dict[str, Any]:
        """
        Creates a new call center resource using JSON data and returns a successful response upon completion.

        Args:
            advanced_settings (object): advanced_settings
            alerts (object): alerts
            friday_hours (array): The Friday hours of operation. Default value is ["08:00", "18:00"].
            group_description (string): The description of the call center. Max 256 characters.
            hold_queue (object): hold_queue
            hours_on (boolean): The time frame when the call center wants to receive calls. Default value is false, which means the call center will always take calls (24/7).
            monday_hours (array): The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].
            name (string): [single-line only]

        The name of the call center. Max 100 characters.
            office_id (integer): The id of the office to which the call center belongs..
            ring_seconds (integer): The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds. Default is 30 seconds.
            routing_options (object): routing_options
            saturday_hours (array): The Saturday hours of operation. Default is empty array.
            sunday_hours (array): The Sunday hours of operation. Default is empty array.
            thursday_hours (array): The Thursday hours of operation. Default value is ["08:00", "18:00"].
            tuesday_hours (array): The Tuesday hours of operation. Default value is ["08:00", "18:00"].
            voice_intelligence (object): voice_intelligence
            wednesday_hours (array): The Wednesday hours of operation. Default value is ["08:00", "18:00"].

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        request_body = {
            "advanced_settings": advanced_settings,
            "alerts": alerts,
            "friday_hours": friday_hours,
            "group_description": group_description,
            "hold_queue": hold_queue,
            "hours_on": hours_on,
            "monday_hours": monday_hours,
            "name": name,
            "office_id": office_id,
            "ring_seconds": ring_seconds,
            "routing_options": routing_options,
            "saturday_hours": saturday_hours,
            "sunday_hours": sunday_hours,
            "thursday_hours": thursday_hours,
            "tuesday_hours": tuesday_hours,
            "voice_intelligence": voice_intelligence,
            "wednesday_hours": wednesday_hours,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callcenters"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_delete(self, id) -> dict[str, Any]:
        """
        Deletes a call center identified by the specified ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callcenters/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_get(self, id) -> dict[str, Any]:
        """
        Retrieves details for the specified call center identified by its unique ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callcenters/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_update(
        self,
        id,
        advanced_settings=None,
        alerts=None,
        friday_hours=None,
        group_description=None,
        hold_queue=None,
        hours_on=None,
        monday_hours=None,
        name=None,
        ring_seconds=None,
        routing_options=None,
        saturday_hours=None,
        sunday_hours=None,
        thursday_hours=None,
        tuesday_hours=None,
        voice_intelligence=None,
        wednesday_hours=None,
    ) -> dict[str, Any]:
        """
        Updates partial properties of the call center resource identified by the given ID using a JSON Patch document.

        Args:
            id (string): id
            advanced_settings (object): advanced_settings
            alerts (object): alerts
            friday_hours (array): The Friday hours of operation. Default value is ["08:00", "18:00"].
            group_description (string): The description of the call center. Max 256 characters.
            hold_queue (object): hold_queue
            hours_on (boolean): The time frame when the call center wants to receive calls. Default value is false, which means the call center will always take calls (24/7).
            monday_hours (array): The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].
            name (string): [single-line only]

        The name of the call center. Max 100 characters.
            ring_seconds (integer): The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds. Default is 30 seconds.
            routing_options (object): routing_options
            saturday_hours (array): The Saturday hours of operation. Default is empty array.
            sunday_hours (array): The Sunday hours of operation. Default is empty array.
            thursday_hours (array): The Thursday hours of operation. Default value is ["08:00", "18:00"].
            tuesday_hours (array): The Tuesday hours of operation. Default value is ["08:00", "18:00"].
            voice_intelligence (object): voice_intelligence
            wednesday_hours (array): The Wednesday hours of operation. Default value is ["08:00", "18:00"].

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "advanced_settings": advanced_settings,
            "alerts": alerts,
            "friday_hours": friday_hours,
            "group_description": group_description,
            "hold_queue": hold_queue,
            "hours_on": hours_on,
            "monday_hours": monday_hours,
            "name": name,
            "ring_seconds": ring_seconds,
            "routing_options": routing_options,
            "saturday_hours": saturday_hours,
            "sunday_hours": sunday_hours,
            "thursday_hours": thursday_hours,
            "tuesday_hours": tuesday_hours,
            "voice_intelligence": voice_intelligence,
            "wednesday_hours": wednesday_hours,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callcenters/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_status(self, id) -> dict[str, Any]:
        """
        Retrieves the status of a call center identified by the provided ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callcenters/{id}/status"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_operators_get_dutystatus(self, id) -> dict[str, Any]:
        """
        Retrieves the duty status of a specific call center operator identified by the provided ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callcenters/operators/{id}/dutystatus"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_operators_dutystatus(
        self, id, duty_status_reason=None, on_duty=None
    ) -> dict[str, Any]:
        """
        Updates the duty status of a call center operator with the specified ID using the PATCH method and returns a 200 OK response upon success.

        Args:
            id (string): id
            duty_status_reason (string): [single-line only]

        A description of this status.
            on_duty (boolean): True if this status message indicates an "on-duty" status.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "duty_status_reason": duty_status_reason,
            "on_duty": on_duty,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callcenters/operators/{id}/dutystatus"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_operators_get_skilllevel(
        self, call_center_id, user_id
    ) -> dict[str, Any]:
        """
        Retrieves the skill information for a specific operator associated with a given call center.

        Args:
            call_center_id (string): call_center_id
            user_id (string): user_id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if call_center_id is None:
            raise ValueError("Missing required parameter 'call_center_id'")
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'")
        url = f"{self.base_url}/api/v2/callcenters/{call_center_id}/operators/{user_id}/skill"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_operators_skilllevel(
        self, call_center_id, user_id, skill_level=None
    ) -> dict[str, Any]:
        """
        Updates the skill information for a specific operator in a call center using the PATCH method, requiring a JSON payload with the updated details.

        Args:
            call_center_id (string): call_center_id
            user_id (string): user_id
            skill_level (integer): New skill level to set the operator in the call center. It must be an integer value between 0 and 100.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if call_center_id is None:
            raise ValueError("Missing required parameter 'call_center_id'")
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'")
        request_body = {
            "skill_level": skill_level,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callcenters/{call_center_id}/operators/{user_id}/skill"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_operators_delete(self, id, user_id=None) -> dict[str, Any]:
        """
        Deletes an operator associated with a specific call center identified by the provided ID.

        Args:
            id (string): id
            user_id (integer): ID of the operator to remove.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callcenters/{id}/operators"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_operators_get(self, id) -> dict[str, Any]:
        """
        Retrieves the list of operators associated with the specified call center by its ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callcenters/{id}/operators"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_operators_post(
        self,
        id,
        keep_paid_numbers=None,
        license_type=None,
        role=None,
        skill_level=None,
        user_id=None,
    ) -> dict[str, Any]:
        """
        Adds a new operator to the call center specified by the given ID using a JSON request body.

        Args:
            id (string): id
            keep_paid_numbers (boolean): Whether or not to keep phone numbers when switching to a support license.

        Note: Phone numbers require additional number licenses under a support license.
            license_type (string): The type of license to assign to the new operator if a license is required.
        (`agents` or `lite_support_agents`). Defaults to `agents`
            role (string): The role the user should assume.
            skill_level (integer): Skill level of the operator. Integer value in range 1 - 100. Default 100.
            user_id (integer): The ID of the user.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callcenters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "keep_paid_numbers": keep_paid_numbers,
            "license_type": license_type,
            "role": role,
            "skill_level": skill_level,
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callcenters/{id}/operators"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def calllabel_list(self, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of call labels, optionally limited by the specified number of results.

        Args:
            limit (integer): The maximum number of call labels to return in the response, specified as an integer to limit the result set size.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            calllabels
        """
        url = f"{self.base_url}/api/v2/calllabels"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_review_share_link_create(
        self, call_id=None, privacy=None
    ) -> dict[str, Any]:
        """
        Creates a shareable link for a call review, returning the generated link upon successful creation.

        Args:
            call_id (integer): The call's id.
            privacy (string): The privacy state of the recording share link, 'company' will be set as default.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callreviewsharelink
        """
        request_body = {
            "call_id": call_id,
            "privacy": privacy,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callreviewsharelink"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_review_share_link_delete(self, id) -> dict[str, Any]:
        """
        Deletes a call review share link identified by the provided ID using the DELETE method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callreviewsharelink
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callreviewsharelink/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_review_share_link_get(self, id) -> dict[str, Any]:
        """
        Retrieves a share link for a call review by its ID using the Dialpad API.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callreviewsharelink
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callreviewsharelink/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_review_share_link_update(self, id, privacy=None) -> dict[str, Any]:
        """
        Updates a call review share link for the specified ID using the provided JSON data.

        Args:
            id (string): id
            privacy (string): The privacy state of the recording share link

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callreviewsharelink
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "privacy": privacy,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callreviewsharelink/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def callrouters_list(self, cursor=None, office_id=None) -> dict[str, Any]:
        """
        Retrieves a list of call routers, optionally filtered by office ID and paginated using a cursor.

        Args:
            cursor (string): A string parameter used for cursor-based pagination, allowing incremental data retrieval by specifying a unique identifier or token to mark the position in the dataset.
            office_id (integer): Specifies the unique office identifier to filter call routers by office; only routers associated with the specified office will be returned in the response.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callrouters
        """
        url = f"{self.base_url}/api/v2/callrouters"
        query_params = {
            k: v
            for k, v in [("cursor", cursor), ("office_id", office_id)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callrouters_create(
        self,
        default_target_id=None,
        default_target_type=None,
        enabled=None,
        name=None,
        office_id=None,
        routing_url=None,
        secret=None,
    ) -> dict[str, Any]:
        """
        Creates a new call router configuration using the provided JSON data and returns a successful response upon completion.

        Args:
            default_target_id (integer): The ID of the target that should be used as a fallback destination for calls if the call router is disabled or fails.
            default_target_type (string): The entity type of the default target.
            enabled (boolean): If set to False, the call router will skip the routing url and instead forward calls straight to the default target.
            name (string): [single-line only]

        A human-readable display name for the router.
            office_id (integer): The ID of the office to which this router belongs.
            routing_url (string): The URL that should be used to drive call routing decisions.
            secret (string): [single-line only]

        The call router's signature secret. This is a plain text string that you should generate with a minimum length of 32 characters.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callrouters
        """
        request_body = {
            "default_target_id": default_target_id,
            "default_target_type": default_target_type,
            "enabled": enabled,
            "name": name,
            "office_id": office_id,
            "routing_url": routing_url,
            "secret": secret,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callrouters"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def callrouters_delete(self, id) -> Any:
        """
        Deletes a call router identified by the provided ID from the system.

        Args:
            id (string): id

        Returns:
            Any: A successful response

        Tags:
            callrouters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callrouters/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callrouters_get(self, id) -> dict[str, Any]:
        """
        Retrieves details for a specific call router identified by its unique ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callrouters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/callrouters/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callrouters_update(
        self,
        id,
        default_target_id=None,
        default_target_type=None,
        enabled=None,
        name=None,
        office_id=None,
        reset_error_count=None,
        routing_url=None,
        secret=None,
    ) -> dict[str, Any]:
        """
        Updates a call router with a specified ID using partial modifications via a JSON Patch document.

        Args:
            id (string): id
            default_target_id (integer): The ID of the target that should be used as a fallback destination for calls if the call router is disabled or fails.
            default_target_type (string): The entity type of the default target.
            enabled (boolean): If set to False, the call router will skip the routing url and instead forward calls straight to the default target.
            name (string): [single-line only]

        A human-readable display name for the router.
            office_id (integer): The ID of the office to which this router belongs.
            reset_error_count (boolean): Sets the auto-disablement routing error count back to zero.

        Call routers maintain a count of the number of errors that have occured within the past hour, and automatically become disabled when that count exceeds 10.

        Setting enabled to true via the API will not reset that count, which means that the router will likely become disabled again after one more error. In most cases, this will be useful for testing fixes in your routing API, but in some circumstances it may be desirable to reset that counter.
            routing_url (string): The URL that should be used to drive call routing decisions.
            secret (string): [single-line only]

        The call router's signature secret. This is a plain text string that you should generate with a minimum length of 32 characters.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callrouters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "default_target_id": default_target_id,
            "default_target_type": default_target_type,
            "enabled": enabled,
            "name": name,
            "office_id": office_id,
            "reset_error_count": reset_error_count,
            "routing_url": routing_url,
            "secret": secret,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callrouters/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_assign_call_router_number_post(
        self, id, area_code=None, number=None, primary=None
    ) -> dict[str, Any]:
        """
        Assigns a phone number to a call router with the specified ID using the provided JSON data.

        Args:
            id (string): id
            area_code (string): An area code in which to find an available phone number for assignment.
            number (string): A phone number to assign. (e164-formatted)
            primary (boolean): A boolean indicating whether this should become the primary phone number.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            callrouters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "area_code": area_code,
            "number": number,
            "primary": primary,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/callrouters/{id}/assign_number"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_delete(self, id) -> Any:
        """
        Deletes the channel identified by the specified ID and returns a status response confirming the deletion.

        Args:
            id (string): id

        Returns:
            Any: A successful response

        Tags:
            channels
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/channels/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_get(self, id) -> dict[str, Any]:
        """
        Retrieves information about a specific channel by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            channels
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/channels/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_list(self, cursor=None, state=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of channels, optionally filtered by state, using the provided cursor for pagination.

        Args:
            cursor (string): Optional string parameter used for cursor-based pagination, specifying the position from which to retrieve the next set of results.
            state (string): An optional string parameter indicating the state of the channels to be retrieved.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            channels
        """
        url = f"{self.base_url}/api/v2/channels"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("state", state)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_post(
        self, description=None, name=None, privacy_type=None, user_id=None
    ) -> dict[str, Any]:
        """
        Creates a new channel by submitting channel details in JSON format.

        Args:
            description (string): The description of the channel.
            name (string): [single-line only]

        The name of the channel.
            privacy_type (string): The privacy type of the channel.
            user_id (integer): The ID of the user who owns the channel. Just for company level API key.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            channels
        """
        request_body = {
            "description": description,
            "name": name,
            "privacy_type": privacy_type,
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/channels"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_members_delete(self, id, user_id=None) -> Any:
        """
        Removes a member from a channel specified by the given ID using the DELETE method.

        Args:
            id (string): id
            user_id (integer): The user id.

        Returns:
            Any: A successful response

        Tags:
            channels
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/channels/{id}/members"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_members_list(self, id, cursor=None) -> dict[str, Any]:
        """
        Get a list of members in a specific channel, optionally paginated using a cursor.

        Args:
            id (string): id
            cursor (string): An opaque token used for cursor-based pagination, indicating the position from which to fetch the next set of members in the channel.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            channels
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/channels/{id}/members"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_members_post(self, id, user_id=None) -> dict[str, Any]:
        """
        Adds a member to a channel specified by the provided ID using the provided JSON data.

        Args:
            id (string): id
            user_id (integer): The user id.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            channels
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/channels/{id}/members"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def coaching_team_members_get(self, id) -> dict[str, Any]:
        """
        Retrieves the members of a coaching team identified by the provided ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            coachingteams
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/coachingteams/{id}/members"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def coaching_team_members_add(
        self, id, member_id=None, role=None
    ) -> dict[str, Any]:
        """
        Adds a new member to a coaching team identified by the provided ID using the POST method and returns a status message.

        Args:
            id (string): id
            member_id (string): The id of the user added to the coaching team.
            role (string): The role of the user added.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            coachingteams
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "member_id": member_id,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/coachingteams/{id}/members"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def coaching_team_get(self, id) -> dict[str, Any]:
        """
        Retrieves information about a coaching team specified by its identifier using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            coachingteams
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/coachingteams/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def coaching_team_listall(self, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of coaching teams using the GET method, optionally allowing pagination with a cursor query parameter.

        Args:
            cursor (string): An opaque string token used for cursor-based pagination, indicating the starting point for retrieving the next set of results from the coaching teams list.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            coachingteams
        """
        url = f"{self.base_url}/api/v2/coachingteams"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def company_get(self) -> dict[str, Any]:
        """
        Retrieves company data using the "GET" method at the "/api/v2/company" endpoint and returns the response.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            company
        """
        url = f"{self.base_url}/api/v2/company"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def company_sms_opt_out(
        self, id, opt_out_state, a2p_campaign_id=None, cursor=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of SMS opt-out information for a specified company, filtered by optional parameters such as a2p campaign ID and cursor, with a required opt-out state parameter.

        Args:
            id (string): id
            opt_out_state (string): The "opt_out_state" parameter specifies the opt-out status of SMS messages, required for filtering results, with possible values being "opted_out" or "opted_back_in".
            a2p_campaign_id (integer): Optional integer parameter to filter SMS opt-out records by a specific A2P campaign ID.
            cursor (string): An opaque string used for cursor-based pagination, indicating the position in the dataset from which to retrieve the next page of SMS opt-out records.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            company
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/company/{id}/smsoptout"
        query_params = {
            k: v
            for k, v in [
                ("a2p_campaign_id", a2p_campaign_id),
                ("cursor", cursor),
                ("opt_out_state", opt_out_state),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def conference_rooms_list(self, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of conference rooms using the "GET" method, optionally paginating results with a query parameter cursor, secured by either an API key in the URL or a Bearer token.

        Args:
            cursor (string): Optional string parameter used for cursor pagination, indicating the position to start fetching data from in the list of conference rooms.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            conference
        """
        url = f"{self.base_url}/api/v2/conference/rooms"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def conference_meetings_list(self, cursor=None, room_id=None) -> dict[str, Any]:
        """
        Retrieves a list of meetings for a conference, allowing optional filtering by room ID and pagination using a cursor.

        Args:
            cursor (string): A unique string identifier used for cursor-based pagination to fetch the next or previous set of meetings, allowing incremental data retrieval.
            room_id (string): Specifies the unique identifier of the room to filter meetings for; if omitted, all rooms are considered.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            conference
        """
        url = f"{self.base_url}/api/v2/conference/meetings"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("room_id", room_id)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def contacts_delete(self, id) -> dict[str, Any]:
        """
        Deletes a specific contact by ID and removes all associated list memberships for that contact.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            contacts
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/contacts/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def contacts_get(self, id) -> dict[str, Any]:
        """
        Retrieves detailed information for a specific contact identified by the given ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            contacts
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/contacts/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def contacts_update(
        self,
        id,
        company_name=None,
        emails=None,
        extension=None,
        first_name=None,
        job_title=None,
        last_name=None,
        phones=None,
        trunk_group=None,
        urls=None,
    ) -> dict[str, Any]:
        """
        Partially updates the contact resource identified by the given ID with the provided JSON data.

        Args:
            id (string): id
            company_name (string): [single-line only]

        The contact's company name.
            emails (array): The contact's emails.

        The first email in the list is the contact's primary email.
            extension (string): The contact's extension number.
            first_name (string): [single-line only]

        The contact's first name.
            job_title (string): [single-line only]

        The contact's job title.
            last_name (string): [single-line only]

        The contact's last name.
            phones (array): The contact's phone numbers.

        The phone number must be in e164 format. The first number in the list is the contact's primary phone.
            trunk_group (string): [Deprecated]
            urls (array): A list of websites associated with or belonging to this contact.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            contacts
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "company_name": company_name,
            "emails": emails,
            "extension": extension,
            "first_name": first_name,
            "job_title": job_title,
            "last_name": last_name,
            "phones": phones,
            "trunk_group": trunk_group,
            "urls": urls,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/contacts/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def contacts_list(
        self, cursor=None, include_local=None, owner_id=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of contacts, optionally filtered by owner and local inclusion status.

        Args:
            cursor (string): Specifies the opaque token or unique identifier used to retrieve the next or previous page of contacts in cursor-based pagination; include this value to continue fetching results from where the previous page ended.
            include_local (boolean): Optional boolean parameter to include local contacts in the response.
            owner_id (string): Optional string parameter to filter contacts by the ID of their owner.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            contacts
        """
        url = f"{self.base_url}/api/v2/contacts"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("include_local", include_local),
                ("owner_id", owner_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def contacts_create(
        self,
        company_name=None,
        emails=None,
        extension=None,
        first_name=None,
        job_title=None,
        last_name=None,
        owner_id=None,
        phones=None,
        trunk_group=None,
        urls=None,
    ) -> dict[str, Any]:
        """
        Creates or updates one or multiple contacts by submitting their data in JSON format to the server.

        Args:
            company_name (string): [single-line only]

        The contact's company name.
            emails (array): The contact's emails.

        The first email in the list is the contact's primary email.
            extension (string): The contact's extension number.
            first_name (string): [single-line only]

        The contact's first name.
            job_title (string): [single-line only]

        The contact's job title.
            last_name (string): [single-line only]

        The contact's last name.
            owner_id (string): The id of the user who will own this contact.

        If provided, a local contact will be created for this user. Otherwise, the contact will be created as a shared contact in your company.
            phones (array): The contact's phone numbers.

        The phone number must be in e164 format. The first number in the list is the contact's primary phone.
            trunk_group (string): [Deprecated]
            urls (array): A list of websites associated with or belonging to this contact.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            contacts
        """
        request_body = {
            "company_name": company_name,
            "emails": emails,
            "extension": extension,
            "first_name": first_name,
            "job_title": job_title,
            "last_name": last_name,
            "owner_id": owner_id,
            "phones": phones,
            "trunk_group": trunk_group,
            "urls": urls,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/contacts"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def contacts_create_with_uid(
        self,
        company_name=None,
        emails=None,
        extension=None,
        first_name=None,
        job_title=None,
        last_name=None,
        phones=None,
        trunk_group=None,
        uid=None,
        urls=None,
    ) -> dict[str, Any]:
        """
        Updates or replaces the entire contact resource at the specified path with the provided request data, returning a status code on success.

        Args:
            company_name (string): [single-line only]

        The contact's company name.
            emails (array): The contact's emails.

        The first email in the list is the contact's primary email.
            extension (string): The contact's extension number.
            first_name (string): [single-line only]

        The contact's first name.
            job_title (string): [single-line only]

        The contact's job title.
            last_name (string): [single-line only]

        The contact's last name.
            phones (array): The contact's phone numbers.

        The phone number must be in e164 format. The first number in the list is the contact's primary phone.
            trunk_group (string): [Deprecated]
            uid (string): The unique id to be included as part of the contact's generated id.
            urls (array): A list of websites associated with or belonging to this contact.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            contacts
        """
        request_body = {
            "company_name": company_name,
            "emails": emails,
            "extension": extension,
            "first_name": first_name,
            "job_title": job_title,
            "last_name": last_name,
            "phones": phones,
            "trunk_group": trunk_group,
            "uid": uid,
            "urls": urls,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/contacts"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def ivr_delete(
        self, target_type, target_id, ivr_type, ivr_id=None, select_option=None
    ) -> dict[str, Any]:
        """
        Deletes a specific customer IVR configuration based on the target type, target ID, and IVR type using the provided JSON payload.

        Args:
            target_type (string): target_type
            target_id (string): target_id
            ivr_type (string): ivr_type
            ivr_id (integer): The id of the ivr that you want to use for the ivr type.
            select_option (string): For call center auto call recording only. Set ivr for inbound or outbound. Default is both.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            customivrs
        """
        if target_type is None:
            raise ValueError("Missing required parameter 'target_type'")
        if target_id is None:
            raise ValueError("Missing required parameter 'target_id'")
        if ivr_type is None:
            raise ValueError("Missing required parameter 'ivr_type'")
        request_body = {
            "ivr_id": ivr_id,
            "select_option": select_option,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/customivrs/{target_type}/{target_id}/{ivr_type}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def ivr_update(
        self, target_type, target_id, ivr_type, ivr_id=None, select_option=None
    ) -> dict[str, Any]:
        """
        Modifies a custom IVR configuration using the PATCH method by updating specific properties for a target identified by type, ID, and IVR type.

        Args:
            target_type (string): target_type
            target_id (string): target_id
            ivr_type (string): ivr_type
            ivr_id (integer): The id of the ivr that you want to use for the ivr type.
            select_option (string): For call center auto call recording only. Set ivr for inbound or outbound. Default is both.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            customivrs
        """
        if target_type is None:
            raise ValueError("Missing required parameter 'target_type'")
        if target_id is None:
            raise ValueError("Missing required parameter 'target_id'")
        if ivr_type is None:
            raise ValueError("Missing required parameter 'ivr_type'")
        request_body = {
            "ivr_id": ivr_id,
            "select_option": select_option,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/customivrs/{target_type}/{target_id}/{ivr_type}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def custom_ivrs_get(self, target_type, target_id, cursor=None) -> dict[str, Any]:
        """
        Retrieves custom IVR data based on the specified target type and ID, with optional pagination using a cursor.

        Args:
            target_type (string): Specifies the type of target for the custom IVR, with possible values including callcenter, callrouter, channel, coachinggroup, coachingteam, department, office, room, staffgroup, unknown, or user.
            target_id (integer): target_id is a required integer query parameter specifying the unique identifier of the target resource to retrieve custom IVR details.
            cursor (string): **cursor**: An optional string parameter used for cursor-based pagination, indicating the position in the dataset from which to retrieve the next set of results.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            customivrs, important
        """
        url = f"{self.base_url}/api/v2/customivrs"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("target_type", target_type),
                ("target_id", target_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def ivr_create(
        self,
        description=None,
        file=None,
        ivr_type=None,
        name=None,
        target_id=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Creates a new custom IVR entry via API and returns a confirmation upon success.

        Args:
            description (string): [single-line only]

        The description of the new IVR. Max 256 characters.
            file (string): An MP3 audio file. The file needs to be Base64-encoded.
            ivr_type (string): Type of IVR.
            name (string): [single-line only]

        The name of the new IVR. Max 100 characters.
            target_id (integer): The ID of the target to which you want to assign this IVR.
            target_type (string): The type of the target to which you want to assign this IVR.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            customivrs
        """
        request_body = {
            "description": description,
            "file": file,
            "ivr_type": ivr_type,
            "name": name,
            "target_id": target_id,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/customivrs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def ivr_details_update(self, ivr_id, description=None, name=None) -> dict[str, Any]:
        """
        Updates a custom IVR configuration identified by the `ivr_id` using partial modifications specified in the JSON request body.

        Args:
            ivr_id (string): ivr_id
            description (string): [single-line only]

        The description of the IVR.
            name (string): [single-line only]

        The name of this IVR.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            customivrs
        """
        if ivr_id is None:
            raise ValueError("Missing required parameter 'ivr_id'")
        request_body = {
            "description": description,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/customivrs/{ivr_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_delete(self, id) -> dict[str, Any]:
        """
        Deletes the department identified by the specified ID from the system.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            departments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/departments/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_get(self, id) -> dict[str, Any]:
        """
        Retrieves detailed information for a department by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            departments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/departments/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_update(
        self,
        id,
        auto_call_recording=None,
        friday_hours=None,
        group_description=None,
        hold_queue=None,
        hours_on=None,
        monday_hours=None,
        name=None,
        ring_seconds=None,
        routing_options=None,
        saturday_hours=None,
        sunday_hours=None,
        thursday_hours=None,
        tuesday_hours=None,
        voice_intelligence=None,
        wednesday_hours=None,
    ) -> dict[str, Any]:
        """
        Updates a department partially using the provided JSON data at the specified department ID.

        Args:
            id (string): id
            auto_call_recording (boolean): Whether or not automatically record all calls of this department. Default is False.
            friday_hours (array): The Friday hours of operation. Default value is ["08:00", "18:00"].
            group_description (string): The description of the department. Max 256 characters.
            hold_queue (object): hold_queue
            hours_on (boolean): The time frame when the department wants to receive calls. Default value is false, which means the call center will always take calls (24/7).
            monday_hours (array): The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].
            name (string): [single-line only]

        The name of the department. Max 100 characters.
            ring_seconds (integer): The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds. Default is 30 seconds.
            routing_options (object): routing_options
            saturday_hours (array): The Saturday hours of operation. Default is empty array.
            sunday_hours (array): The Sunday hours of operation. Default is empty array.
            thursday_hours (array): The Thursday hours of operation. Default value is ["08:00", "18:00"].
            tuesday_hours (array): The Tuesday hours of operation. Default value is ["08:00", "18:00"].
            voice_intelligence (object): voice_intelligence
            wednesday_hours (array): The Wednesday hours of operation. Default value is ["08:00", "18:00"].

        Returns:
            dict[str, Any]: A successful response

        Tags:
            departments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "auto_call_recording": auto_call_recording,
            "friday_hours": friday_hours,
            "group_description": group_description,
            "hold_queue": hold_queue,
            "hours_on": hours_on,
            "monday_hours": monday_hours,
            "name": name,
            "ring_seconds": ring_seconds,
            "routing_options": routing_options,
            "saturday_hours": saturday_hours,
            "sunday_hours": sunday_hours,
            "thursday_hours": thursday_hours,
            "tuesday_hours": tuesday_hours,
            "voice_intelligence": voice_intelligence,
            "wednesday_hours": wednesday_hours,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/departments/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_listall(
        self, cursor=None, office_id=None, name_search=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of departments, optionally filtered by office ID or name, and supports pagination via cursor.

        Args:
            cursor (string): An opaque string used for cursor-based pagination, indicating the position in the list of results from which to fetch the next set of data.
            office_id (integer): An optional integer parameter specifying the office ID for filtering department results.
            name_search (string): Optional string parameter to search for departments by name.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            departments
        """
        url = f"{self.base_url}/api/v2/departments"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("office_id", office_id),
                ("name_search", name_search),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_create(
        self,
        auto_call_recording=None,
        friday_hours=None,
        group_description=None,
        hold_queue=None,
        hours_on=None,
        monday_hours=None,
        name=None,
        office_id=None,
        ring_seconds=None,
        routing_options=None,
        saturday_hours=None,
        sunday_hours=None,
        thursday_hours=None,
        tuesday_hours=None,
        voice_intelligence=None,
        wednesday_hours=None,
    ) -> dict[str, Any]:
        """
        Creates a new department resource using the provided JSON data and returns a successful response if the operation is completed.

        Args:
            auto_call_recording (boolean): Whether or not automatically record all calls of this department. Default is False.
            friday_hours (array): The Friday hours of operation. Default value is ["08:00", "18:00"].
            group_description (string): The description of the department. Max 256 characters.
            hold_queue (object): hold_queue
            hours_on (boolean): The time frame when the department wants to receive calls. Default value is false, which means the call center will always take calls (24/7).
            monday_hours (array): The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].
            name (string): [single-line only]

        The name of the department. Max 100 characters.
            office_id (integer): The id of the office to which the department belongs..
            ring_seconds (integer): The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds. Default is 30 seconds.
            routing_options (object): routing_options
            saturday_hours (array): The Saturday hours of operation. Default is empty array.
            sunday_hours (array): The Sunday hours of operation. Default is empty array.
            thursday_hours (array): The Thursday hours of operation. Default value is ["08:00", "18:00"].
            tuesday_hours (array): The Tuesday hours of operation. Default value is ["08:00", "18:00"].
            voice_intelligence (object): voice_intelligence
            wednesday_hours (array): The Wednesday hours of operation. Default value is ["08:00", "18:00"].

        Returns:
            dict[str, Any]: A successful response

        Tags:
            departments
        """
        request_body = {
            "auto_call_recording": auto_call_recording,
            "friday_hours": friday_hours,
            "group_description": group_description,
            "hold_queue": hold_queue,
            "hours_on": hours_on,
            "monday_hours": monday_hours,
            "name": name,
            "office_id": office_id,
            "ring_seconds": ring_seconds,
            "routing_options": routing_options,
            "saturday_hours": saturday_hours,
            "sunday_hours": sunday_hours,
            "thursday_hours": thursday_hours,
            "tuesday_hours": tuesday_hours,
            "voice_intelligence": voice_intelligence,
            "wednesday_hours": wednesday_hours,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/departments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_operators_delete(
        self, id, operator_id=None, operator_type=None
    ) -> dict[str, Any]:
        """
        Deletes a department operator by ID using the specified API endpoint and returns a status message.

        Args:
            id (string): id
            operator_id (integer): ID of the operator to remove.
            operator_type (string): Type of the operator to remove (`user` or `room`).

        Returns:
            dict[str, Any]: A successful response

        Tags:
            departments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "operator_id": operator_id,
            "operator_type": operator_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/departments/{id}/operators"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_operators_get(self, id) -> dict[str, Any]:
        """
        Retrieves information about operators associated with a specific department by department ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            departments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/departments/{id}/operators"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_operators_post(
        self, id, operator_id=None, operator_type=None, role=None
    ) -> dict[str, Any]:
        """
        Creates a new operator for the specified department and returns a successful status on completion.

        Args:
            id (string): id
            operator_id (integer): ID of the operator to add.
            operator_type (string): Type of the operator to add. (`user` or `room`)
            role (string): The role of the new operator. (`operator` or `admin`)

        Returns:
            dict[str, Any]: A successful response

        Tags:
            departments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "operator_id": operator_id,
            "operator_type": operator_type,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/departments/{id}/operators"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def faxline_create(self, line=None, target=None) -> dict[str, Any]:
        """
        Creates a new fax line resource using the provided JSON data and returns a successful response upon creation.

        Args:
            line (string): Line to assign.
            target (object): target

        Returns:
            dict[str, Any]: A successful response

        Tags:
            faxline
        """
        request_body = {
            "line": line,
            "target": target,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/faxline"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_assign_number_post(
        self, number, primary=None, target_id=None, target_type=None
    ) -> dict[str, Any]:
        """
        Assigns a specified number to a resource by sending a POST request with the number as a path parameter and the assignment details in the request body.

        Args:
            number (string): number
            primary (boolean): A boolean indicating whether this should become the target's primary phone number.
            target_id (integer): The ID of the target to reassign this number to.
            target_type (string): The type of the target.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            numbers
        """
        if number is None:
            raise ValueError("Missing required parameter 'number'")
        request_body = {
            "primary": primary,
            "target_id": target_id,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/numbers/{number}/assign"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_assign_target_number_post(
        self,
        area_code=None,
        number=None,
        primary=None,
        target_id=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Assigns numbers using a JSON payload in the request body via the "POST" method and returns a successful response upon completion.

        Args:
            area_code (string): An area code in which to find an available phone number for assignment.
            number (string): A phone number to assign. (e164-formatted)
            primary (boolean): A boolean indicating whether this should become the target's primary phone number.
            target_id (integer): The ID of the target to reassign this number to.
            target_type (string): The type of the target.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            numbers
        """
        request_body = {
            "area_code": area_code,
            "number": number,
            "primary": primary,
            "target_id": target_id,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/numbers/assign"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_delete(self, number, release=None) -> dict[str, Any]:
        """
        Deletes a number resource identified by the path parameter "number" and optionally considers the "release" status if specified in the query.

        Args:
            number (string): number
            release (boolean): Optional boolean parameter indicating whether to release resources associated with the number during deletion.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            numbers
        """
        if number is None:
            raise ValueError("Missing required parameter 'number'")
        url = f"{self.base_url}/api/v2/numbers/{number}"
        query_params = {k: v for k, v in [("release", release)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_get(self, number) -> dict[str, Any]:
        """
        Retrieves information for a specific number using the provided number identifier.

        Args:
            number (string): number

        Returns:
            dict[str, Any]: A successful response

        Tags:
            numbers
        """
        if number is None:
            raise ValueError("Missing required parameter 'number'")
        url = f"{self.base_url}/api/v2/numbers/{number}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_list(self, cursor=None, status=None) -> dict[str, Any]:
        """
        Retrieves a list of numbers with optional filtering by status and supports pagination using a cursor parameter.

        Args:
            cursor (string): An opaque string token used for cursor-based pagination, allowing clients to retrieve the next page of data by including this value in the request.
            status (string): Optional query parameter to filter results by the status of the numbers.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            numbers
        """
        url = f"{self.base_url}/api/v2/numbers"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("status", status)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def format_post(self, country_code=None, number=None) -> dict[str, Any]:
        """
        Formats a given number according to the specified country code and returns the formatted result.

        Args:
            country_code (string): Optional country code as a string to specify the country for number formatting.
            number (string): An optional string parameter used to specify a number for formatting purposes in the request.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            numbers
        """
        url = f"{self.base_url}/api/v2/numbers/format"
        query_params = {
            k: v
            for k, v in [("country_code", country_code), ("number", number)]
            if v is not None
        }
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def oauth2_authorize_get(
        self,
        redirect_uri,
        client_id,
        code_challenge_method=None,
        code_challenge=None,
        scope=None,
        response_type=None,
        state=None,
    ) -> Any:
        """
        Initiates the OAuth 2.0 authorization code flow by redirecting the user to authenticate and grant permissions, then redirects back to the specified callback URL with an authorization code or error.

        Args:
            redirect_uri (string): The URL to which the authorization server will redirect the user after authentication; must exactly match one of the registered redirect URIs for the client.
            client_id (string): The `client_id` parameter is a required string that identifies the client application making the authorization request to the OAuth 2.0 authorization server.
            code_challenge_method (string): The "code_challenge_method" parameter specifies the method used to derive the code challenge, with supported values being "S256" for SHA-256 hashing and "plain" for no hashing.
            code_challenge (string): The `code_challenge` parameter is a base64url-encoded string used in the Proof Key for Code Exchange (PKCE) flow to ensure secure authorization code exchange, sent in the authorization request to prevent authorization code interception attacks.
            scope (string): Specifies the permissions (as a space-separated list of OAuth 2.0 scopes) that the client requests from the user during authorization; each scope defines a level of access to protected resources[2][5][3].
            response_type (string): Specifies the type of response expected from the authorization server, with the value "code" indicating an authorization code grant is expected.
            state (string): An opaque value used by the client to maintain state between the request and callback, helping to prevent cross-site request forgery and allowing restoration of the application state after authentication.

        Returns:
            Any: A successful response

        Tags:
            oauth2
        """
        url = f"{self.base_url}/oauth2/authorize"
        query_params = {
            k: v
            for k, v in [
                ("code_challenge_method", code_challenge_method),
                ("code_challenge", code_challenge),
                ("scope", scope),
                ("response_type", response_type),
                ("redirect_uri", redirect_uri),
                ("client_id", client_id),
                ("state", state),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def oauth2_deauthorize_post(self) -> Any:
        """
        Revokes OAuth 2.0 access tokens associated with the client or user, returning a successful response with no content.

        Returns:
            Any: A successful response

        Tags:
            oauth2
        """
        url = f"{self.base_url}/oauth2/deauthorize"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

        """
        Requests an access token and optionally a refresh token using OAuth 2.0 by exchanging credentials or codes, typically in flows like authorization code, client credentials, or refresh token.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            oauth2
        """
        url = f"{self.base_url}/oauth2/token"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def plan_get(self, office_id) -> dict[str, Any]:
        """
        Retrieves the plan details for a specified office identified by its office_id.

        Args:
            office_id (string): office_id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if office_id is None:
            raise ValueError("Missing required parameter 'office_id'")
        url = f"{self.base_url}/api/v2/offices/{office_id}/plan"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def callcenters_list(self, office_id, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of call centers associated with a specific office, supporting pagination via a cursor parameter.

        Args:
            office_id (string): office_id
            cursor (string): A string token used to fetch the next or previous page of call center records after a specific position in the results list.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if office_id is None:
            raise ValueError("Missing required parameter 'office_id'")
        url = f"{self.base_url}/api/v2/offices/{office_id}/callcenters"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def coaching_team_list(self, office_id, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of teams associated with a specific office, identified by the office ID provided in the path, with optional pagination using the cursor query parameter.

        Args:
            office_id (string): office_id
            cursor (string): A unique identifier used for cursor-based pagination to fetch the next page of teams data, typically based on a timestamp or other unique criteria.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if office_id is None:
            raise ValueError("Missing required parameter 'office_id'")
        url = f"{self.base_url}/api/v2/offices/{office_id}/teams"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def departments_list(self, office_id, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of departments associated with a specific office identified by the provided office ID.

        Args:
            office_id (string): office_id
            cursor (string): A unique identifier or token provided by the server that marks the position in the paginated list of departments, enabling retrieval of the next or previous set of results when making subsequent API requests.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if office_id is None:
            raise ValueError("Missing required parameter 'office_id'")
        url = f"{self.base_url}/api/v2/offices/{office_id}/departments"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_assign_office_number_post(
        self, id, area_code=None, number=None, primary=None
    ) -> dict[str, Any]:
        """
        Assigns a phone number to an office identified by the specified ID using a JSON request body.

        Args:
            id (string): id
            area_code (string): An area code in which to find an available phone number for assignment.
            number (string): A phone number to assign. (e164-formatted)
            primary (boolean): A boolean indicating whether this should become the primary phone number.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "area_code": area_code,
            "number": number,
            "primary": primary,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/offices/{id}/assign_number"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_office_unassign_number_post(self, id, number=None) -> dict[str, Any]:
        """
        Unassigns a phone number from an office using the POST method by specifying the office ID in the path and providing additional details in the JSON request body.

        Args:
            id (string): id
            number (string): A phone number to unassign. (e164-formatted)

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "number": number,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/offices/{id}/unassign_number"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_e911_get(self, id) -> dict[str, Any]:
        """
        Retrieves Enhanced 911 (E911) information for a specific office identified by the provided office ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/offices/{id}/e911"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_e911_update(
        self,
        id,
        address=None,
        address2=None,
        city=None,
        country=None,
        state=None,
        update_all=None,
        use_validated_option=None,
        zip=None,
    ) -> dict[str, Any]:
        """
        Updates or replaces the E911 configuration for the specified office using the provided data in the request body.

        Args:
            id (string): id
            address (string): [single-line only]

        Line 1 of the new E911 address.
            address2 (string): [single-line only]

        Line 2 of the new E911 address.
            city (string): [single-line only]

        City of the new E911 address.
            country (string): Country of the new E911 address.
            state (string): [single-line only]

        State or Province of the new E911 address.
            update_all (boolean): Update E911 for all users in this office.
            use_validated_option (boolean): Whether to use the validated address option from our service.
            zip (string): [single-line only]

        Zip code of the new E911 address.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "address": address,
            "address2": address2,
            "city": city,
            "country": country,
            "state": state,
            "update_all": update_all,
            "use_validated_option": use_validated_option,
            "zip": zip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/offices/{id}/e911"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def plan_available_licenses_get(self, office_id) -> dict[str, Any]:
        """
        Retrieves the available licenses for a specific office identified by its ID.

        Args:
            office_id (string): office_id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if office_id is None:
            raise ValueError("Missing required parameter 'office_id'")
        url = f"{self.base_url}/api/v2/offices/{office_id}/available_licenses"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_offdutystatuses_get(self, id) -> dict[str, Any]:
        """
        Retrieves a list of off-duty statuses for the specified office, identified by its ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/offices/{id}/offdutystatuses"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_get(self, id) -> dict[str, Any]:
        """
        Retrieves details about a specific office by ID using the API.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/offices/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_list(self, cursor=None, active_only=None) -> dict[str, Any]:
        """
        Retrieves a list of offices, optionally filtering by active status and supporting pagination with a cursor parameter.

        Args:
            cursor (string): A token representing the current position in the dataset, used to fetch the next or previous page of results in cursor-based pagination.
            active_only (boolean): If set to true, returns only active offices; if omitted or false, returns all offices regardless of status.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        url = f"{self.base_url}/api/v2/offices"
        query_params = {
            k: v
            for k, v in [("cursor", cursor), ("active_only", active_only)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_create(
        self,
        annual_commit_monthly_billing=None,
        auto_call_recording=None,
        billing_address=None,
        billing_contact=None,
        country=None,
        currency=None,
        e911_address=None,
        first_action=None,
        friday_hours=None,
        group_description=None,
        hours_on=None,
        international_enabled=None,
        invoiced=None,
        mainline_number=None,
        monday_hours=None,
        name=None,
        no_operators_action=None,
        plan_period=None,
        ring_seconds=None,
        routing_options=None,
        saturday_hours=None,
        sunday_hours=None,
        thursday_hours=None,
        timezone=None,
        tuesday_hours=None,
        unified_billing=None,
        use_same_address=None,
        voice_intelligence=None,
        wednesday_hours=None,
    ) -> dict[str, Any]:
        """
        Creates a new office using the provided JSON data in the request body.

        Args:
            annual_commit_monthly_billing (boolean): A flag indicating if the primary office's plan is categorized as annual commit monthly billing.
            auto_call_recording (boolean): Whether or not automatically record all calls of this office. Default is False.
            billing_address (object): billing_address
            billing_contact (object): billing_contact
            country (string): The office country.
            currency (string): The office's billing currency.
            e911_address (object): e911_address
            first_action (string): The desired action when the office receives a call.
            friday_hours (array): The Friday hours of operation. Default value is ["08:00", "18:00"].
            group_description (string): The description of the office. Max 256 characters.
            hours_on (boolean): The time frame when the office wants to receive calls. Default value is false, which means the office will always take calls (24/7).
            international_enabled (boolean): A flag indicating if the primary office is able to make international phone calls.
            invoiced (boolean): A flag indicating if the payment will be paid by invoice.
            mainline_number (string): The mainline of the office.
            monday_hours (array): The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].
            name (string): [single-line only]

        The office name.
            no_operators_action (string): The action to take if there is no one available to answer calls.
            plan_period (string): The frequency at which the company will be billed.
            ring_seconds (integer): The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds.
            routing_options (object): routing_options
            saturday_hours (array): The Saturday hours of operation. Default is empty array.
            sunday_hours (array): The Sunday hours of operation. Default is empty array.
            thursday_hours (array): The Thursday hours of operation. Default value is ["08:00", "18:00"].
            timezone (string): Timezone using a tz database name.
            tuesday_hours (array): The Tuesday hours of operation. Default value is ["08:00", "18:00"].
            unified_billing (boolean): A flag indicating if to send a unified invoice.
            use_same_address (boolean): A flag indicating if the billing address and the emergency address are the same.
            voice_intelligence (object): voice_intelligence
            wednesday_hours (array): The Wednesday hours of operation. Default value is ["08:00", "18:00"].

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        request_body = {
            "annual_commit_monthly_billing": annual_commit_monthly_billing,
            "auto_call_recording": auto_call_recording,
            "billing_address": billing_address,
            "billing_contact": billing_contact,
            "country": country,
            "currency": currency,
            "e911_address": e911_address,
            "first_action": first_action,
            "friday_hours": friday_hours,
            "group_description": group_description,
            "hours_on": hours_on,
            "international_enabled": international_enabled,
            "invoiced": invoiced,
            "mainline_number": mainline_number,
            "monday_hours": monday_hours,
            "name": name,
            "no_operators_action": no_operators_action,
            "plan_period": plan_period,
            "ring_seconds": ring_seconds,
            "routing_options": routing_options,
            "saturday_hours": saturday_hours,
            "sunday_hours": sunday_hours,
            "thursday_hours": thursday_hours,
            "timezone": timezone,
            "tuesday_hours": tuesday_hours,
            "unified_billing": unified_billing,
            "use_same_address": use_same_address,
            "voice_intelligence": voice_intelligence,
            "wednesday_hours": wednesday_hours,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/offices"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_operators_delete(
        self, id, operator_id=None, operator_type=None
    ) -> dict[str, Any]:
        """
        Deletes the specified operator(s) associated with the office whose ID is provided in the path, returning a success status upon completion.

        Args:
            id (string): id
            operator_id (integer): ID of the operator to remove.
            operator_type (string): Type of the operator to remove (`user` or `room`).

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "operator_id": operator_id,
            "operator_type": operator_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/offices/{id}/operators"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_operators_get(self, id) -> dict[str, Any]:
        """
        Get the list of operators associated with the specified office by its ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/offices/{id}/operators"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def offices_operators_post(
        self, id, operator_id=None, operator_type=None, role=None
    ) -> dict[str, Any]:
        """
        Creates a new operator resource within the specified office using the provided data and returns a success status.

        Args:
            id (string): id
            operator_id (integer): ID of the operator to add.
            operator_type (string): Type of the operator to add. (`user` or `room`)
            role (string): The role of the new operator. (`operator` or `admin`)

        Returns:
            dict[str, Any]: A successful response

        Tags:
            offices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "operator_id": operator_id,
            "operator_type": operator_type,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/offices/{id}/operators"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def recording_share_link_create(
        self, privacy=None, recording_id=None, recording_type=None
    ) -> dict[str, Any]:
        """
        Creates a recording share link by accepting JSON input and returns a success response upon completion.

        Args:
            privacy (string): The privacy state of the recording share link.
            recording_id (string): The recording entity's ID.
            recording_type (string): The type of the recording entity shared via the link.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            recordingsharelink
        """
        request_body = {
            "privacy": privacy,
            "recording_id": recording_id,
            "recording_type": recording_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/recordingsharelink"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def recording_share_link_delete(self, id) -> dict[str, Any]:
        """
        Deletes the recording share link identified by the specified ID and returns a confirmation upon successful completion.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            recordingsharelink
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/recordingsharelink/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def recording_share_link_get(self, id) -> dict[str, Any]:
        """
        Retrieves a recording share link by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            recordingsharelink
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/recordingsharelink/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def recording_share_link_update(self, id, privacy=None) -> dict[str, Any]:
        """
        Updates or replaces the recording share link resource identified by the given ID with the provided data.

        Args:
            id (string): id
            privacy (string): The privacy state of the recording share link.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            recordingsharelink
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "privacy": privacy,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/recordingsharelink/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_assign_room_number_post(
        self, id, area_code=None, number=None, primary=None
    ) -> dict[str, Any]:
        """
        Assigns a number to the specified room and returns a success status.

        Args:
            id (string): id
            area_code (string): An area code in which to find an available phone number for assignment.
            number (string): A phone number to assign. (e164-formatted)
            primary (boolean): A boolean indicating whether this should become the primary phone number.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "area_code": area_code,
            "number": number,
            "primary": primary,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/rooms/{id}/assign_number"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_room_unassign_number_post(self, id, number=None) -> dict[str, Any]:
        """
        Unassigns a phone number from a room using the API and returns a success status.

        Args:
            id (string): id
            number (string): A phone number to unassign. (e164-formatted)

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "number": number,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/rooms/{id}/unassign_number"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def rooms_delete(self, id) -> dict[str, Any]:
        """
        Deletes a room by its ID and returns a successful response.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/rooms/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def rooms_get(self, id) -> dict[str, Any]:
        """
        Retrieves details of a specific room identified by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/rooms/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def rooms_patch(self, id, name=None, phone_numbers=None) -> dict[str, Any]:
        """
        Updates a room with the specified ID by partially modifying its properties using the provided JSON payload.

        Args:
            id (string): id
            name (string): [single-line only]

        The name of the room.
            phone_numbers (array): A list of all phone numbers assigned to the room.

        Numbers can be re-ordered or removed from this list to unassign them.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "name": name,
            "phone_numbers": phone_numbers,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/rooms/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def rooms_list(self, cursor=None, office_id=None) -> dict[str, Any]:
        """
        Retrieves a list of rooms, optionally filtered by office ID, using the provided cursor for pagination.

        Args:
            cursor (string): An opaque string used for cursor-based pagination to specify the position in the dataset, allowing for incremental fetching of data in a specific order.
            office_id (integer): Optional integer parameter to filter rooms by the specified office ID.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        url = f"{self.base_url}/api/v2/rooms"
        query_params = {
            k: v
            for k, v in [("cursor", cursor), ("office_id", office_id)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def rooms_post(self, name=None, office_id=None) -> dict[str, Any]:
        """
        Creates a new room resource and returns a success response upon completion.

        Args:
            name (string): [single-line only]

        The name of the room.
            office_id (integer): The office in which this room resides.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        request_body = {
            "name": name,
            "office_id": office_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/rooms"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deskphones_rooms_create_international_pin(
        self, customer_ref=None
    ) -> dict[str, Any]:
        """
        Creates an international PIN for a room and returns the result.

        Args:
            customer_ref (string): [single-line only]

        An identifier to be printed in the usage summary. Typically used for identifying the person who requested the PIN.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        request_body = {
            "customer_ref": customer_ref,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/rooms/international_pin"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deskphones_rooms_delete(self, parent_id, id) -> Any:
        """
        Deletes a deskphone with the specified ID from a room with the given parent ID using the DELETE method.

        Args:
            parent_id (string): parent_id
            id (string): id

        Returns:
            Any: A successful response

        Tags:
            rooms
        """
        if parent_id is None:
            raise ValueError("Missing required parameter 'parent_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/rooms/{parent_id}/deskphones/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deskphones_rooms_get(self, parent_id, id) -> dict[str, Any]:
        """
        Retrieves details of a specific desk phone identified by `{id}` within a room associated with `{parent_id}`.

        Args:
            parent_id (string): parent_id
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        if parent_id is None:
            raise ValueError("Missing required parameter 'parent_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/rooms/{parent_id}/deskphones/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deskphones_rooms_list(self, parent_id) -> dict[str, Any]:
        """
        Retrieves a list of desk phones associated with a specific room, identified by the parent ID.

        Args:
            parent_id (string): parent_id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            rooms
        """
        if parent_id is None:
            raise ValueError("Missing required parameter 'parent_id'")
        url = f"{self.base_url}/api/v2/rooms/{parent_id}/deskphones"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_reports_delete(self, id) -> dict[str, Any]:
        """
        Deletes a schedule report by ID using the DELETE method, returning a successful response if the operation is completed.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            schedulereports
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/schedulereports/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_reports_get(self, id) -> dict[str, Any]:
        """
        Retrieves a scheduled report by its ID using the "GET" method, returning details or results of the specified report.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            schedulereports
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/schedulereports/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_reports_update(
        self,
        id,
        at=None,
        coaching_group=None,
        enabled=None,
        endpoint_id=None,
        frequency=None,
        name=None,
        on_day=None,
        report_type=None,
        target_id=None,
        target_type=None,
        timezone=None,
    ) -> dict[str, Any]:
        """
        Updates a scheduled report by modifying specific properties of the resource identified by the provided ID using a JSON payload.

        Args:
            id (string): id
            at (integer): Hour of the day when the report will execute considering the frequency and timezones between 0 and 23  e.g. 10 will be 10:00 am.
            coaching_group (boolean): Whether the the statistics should be for trainees of the coach group with the given target_id.
            enabled (boolean): Whether or not this schedule reports event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully.
            frequency (string): How often the report will execute.
            name (string): [single-line only]

        The name of the schedule reports.
            on_day (integer): The day of the week or month when the report will execute considering the frequency. daily=0, weekly=0-6, monthly=0-30.
            report_type (string): The type of report that will be generated.
            target_id (integer): The target's id.
            target_type (string): Target's type.
            timezone (string): Timezone using a tz database name.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            schedulereports
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "at": at,
            "coaching_group": coaching_group,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
            "frequency": frequency,
            "name": name,
            "on_day": on_day,
            "report_type": report_type,
            "target_id": target_id,
            "target_type": target_type,
            "timezone": timezone,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/schedulereports/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_reports_list(self, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of scheduled reports, optionally paginated by a cursor, and returns them in response.

        Args:
            cursor (string): An opaque string used for cursor-based pagination to retrieve the next page of data, typically based on a unique identifier or timestamp.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            schedulereports
        """
        url = f"{self.base_url}/api/v2/schedulereports"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_reports_create(
        self,
        at=None,
        coaching_group=None,
        enabled=None,
        endpoint_id=None,
        frequency=None,
        name=None,
        on_day=None,
        report_type=None,
        target_id=None,
        target_type=None,
        timezone=None,
    ) -> dict[str, Any]:
        """
        Schedules reports for retrieval using the POST method, sending a JSON request to configure the reporting parameters.

        Args:
            at (integer): Hour of the day when the report will execute considering the frequency and timezones between 0 and 23  e.g. 10 will be 10:00 am.
            coaching_group (boolean): Whether the the statistics should be for trainees of the coach group with the given target_id.
            enabled (boolean): Whether or not this schedule reports event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully.
            frequency (string): How often the report will execute.
            name (string): [single-line only]

        The name of the schedule reports.
            on_day (integer): The day of the week or month when the report will execute considering the frequency. daily=0, weekly=0-6, monthly=0-30.
            report_type (string): The type of report that will be generated.
            target_id (integer): The target's id.
            target_type (string): Target's type.
            timezone (string): Timezone using a tz database name.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            schedulereports
        """
        request_body = {
            "at": at,
            "coaching_group": coaching_group,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
            "frequency": frequency,
            "name": name,
            "on_day": on_day,
            "report_type": report_type,
            "target_id": target_id,
            "target_type": target_type,
            "timezone": timezone,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/schedulereports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sms_send(
        self,
        channel_hashtag=None,
        from_number=None,
        infer_country_code=None,
        media=None,
        sender_group_id=None,
        sender_group_type=None,
        text=None,
        to_numbers=None,
        user_id=None,
    ) -> dict[str, Any]:
        """
        Sends an SMS message using the provided JSON data in the request body and returns a status message upon successful execution.

        Args:
            channel_hashtag (string): [single-line only]

        The hashtag of the channel which should receive the SMS.
            from_number (string): The number of who sending the SMS. The number must be assigned to user or a user group. It will override user_id and sender_group_id.
            infer_country_code (boolean): If true, to_numbers will be assumed to be from the specified user's country, and the E164 format requirement will be relaxed.
            media (string): Base64-encoded media attachment (will cause the message to be sent as MMS).
            sender_group_id (integer): The ID of an office, department, or call center that the User should send the message on behalf of.
            sender_group_type (string): The sender group's type (i.e. office, department, or callcenter).
            text (string): The contents of the message that should be sent.
            to_numbers (array): Up to 10 E164-formatted phone numbers who should receive the SMS.
            user_id (integer): The ID of the user who should be the sender of the SMS.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            sms
        """
        request_body = {
            "channel_hashtag": channel_hashtag,
            "from_number": from_number,
            "infer_country_code": infer_country_code,
            "media": media,
            "sender_group_id": sender_group_id,
            "sender_group_type": sender_group_type,
            "text": text,
            "to_numbers": to_numbers,
            "user_id": user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/sms"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def stats_get(self, id) -> dict[str, Any]:
        """
        Retrieves statistics for the specified resource identified by the provided ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            stats
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/stats/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def stats_create(
        self,
        coaching_group=None,
        coaching_team=None,
        days_ago_end=None,
        days_ago_start=None,
        export_type=None,
        group_by=None,
        is_today=None,
        office_id=None,
        stat_type=None,
        target_id=None,
        target_type=None,
        timezone=None,
    ) -> dict[str, Any]:
        """
        Submits statistical data via a POST request to the "/api/v2/stats" endpoint and expects a successful (200) response upon completion.

        Args:
            coaching_group (boolean): Whether or not the the statistics should be for trainees of the coach group with the given target_id.
            coaching_team (boolean): Whether or not the the statistics should be for trainees of the coach team with the given target_id.
            days_ago_end (integer): End of the date range to get statistics for.

        This is the number of days to look back relative to the current day. Used in conjunction with days_ago_start to specify a range.
            days_ago_start (integer): Start of the date range to get statistics for.

        This is the number of days to look back relative to the current day. Used in conjunction with days_ago_end to specify a range.
            export_type (string): Whether to return aggregated statistics (stats), or individual rows for each record (records).

        NOTE: For stat_type "csat" or "dispositions", only "records" is supported.
            group_by (string): This param is only applicable when the stat_type is specified as call. For call stats, group calls by user per day (default), get total metrics by day, or break down by department and call center (office only).
            is_today (boolean): Whether or not the statistics are for the current day.

        NOTE: days_ago_start and days_ago_end are ignored if this is passed in.
            office_id (integer): ID of the office to get statistics for.

        If a target_id and target_type are passed in this value is ignored and instead the target is used.
            stat_type (string): The type of statistics to be returned.

        NOTE: if the value is "csat" or "dispositions", target_id and target_type must be specified.
            target_id (integer): The target's id.
            target_type (string): Target's type.
            timezone (string): Timezone using a tz database name.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            stats
        """
        request_body = {
            "coaching_group": coaching_group,
            "coaching_team": coaching_team,
            "days_ago_end": days_ago_end,
            "days_ago_start": days_ago_start,
            "export_type": export_type,
            "group_by": group_by,
            "is_today": is_today,
            "office_id": office_id,
            "stat_type": stat_type,
            "target_id": target_id,
            "target_type": target_type,
            "timezone": timezone,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/stats"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_agent_status_event_subscription_list(
        self, cursor=None
    ) -> dict[str, Any]:
        """
        Retrieves the current status of agent subscriptions, optionally paginated using a cursor parameter.

        Args:
            cursor (string): A unique identifier used in cursor-based pagination to fetch data incrementally, specifying the position from which to retrieve the next set of results.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        url = f"{self.base_url}/api/v2/subscriptions/agent_status"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_agent_status_event_subscription_create(
        self, agent_type=None, enabled=None, endpoint_id=None
    ) -> dict[str, Any]:
        """
        Updates the agent status for a subscription using JSON data and returns a successful response.

        Args:
            agent_type (string): The agent type this event subscription subscribes to.
            enabled (boolean): Whether or not the this agent status event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        request_body = {
            "agent_type": agent_type,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/agent_status"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_agent_status_event_subscription_delete(self, id) -> dict[str, Any]:
        """
        Deletes an agent status event subscription by its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/agent_status/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_agent_status_event_subscription_get(self, id) -> dict[str, Any]:
        """
        Retrieves the status information of a subscription agent identified by the given ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/agent_status/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_agent_status_event_subscription_update(
        self, id, agent_type=None, enabled=None, endpoint_id=None
    ) -> dict[str, Any]:
        """
        Updates the status of a specific agent subscription using a JSON payload.

        Args:
            id (string): id
            agent_type (string): The agent type this event subscription subscribes to.
            enabled (boolean): Whether or not the this agent status event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,
        please provide a valid webhook ID here.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "agent_type": agent_type,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/agent_status/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_call_event_subscription_list(
        self, cursor=None, target_type=None, target_id=None
    ) -> dict[str, Any]:
        """
        Retrieves information about a call subscription using optional parameters for cursor, target type, and target ID.

        Args:
            cursor (string): An opaque string used for cursor-based pagination, indicating the position in the dataset to fetch the next page of subscriptions.
            target_type (string): **target_type**: Optional string parameter to specify the type of subscription target, such as callcenter, callrouter, channel, coachinggroup, coachingteam, department, office, room, staffgroup, user, or unknown.
            target_id (integer): An optional integer parameter that specifies the target ID for filtering subscriptions during the call operation.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        url = f"{self.base_url}/api/v2/subscriptions/call"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("target_type", target_type),
                ("target_id", target_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_call_event_subscription_create(
        self,
        call_states=None,
        enabled=None,
        endpoint_id=None,
        group_calls_only=None,
        target_id=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Subscribes a user to a call notification service using a JSON payload and returns a success response upon successful subscription.

        Args:
            call_states (array): The call event subscription's list of call states.
            enabled (boolean): Whether or not the call event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully.
            group_calls_only (boolean): Call event subscription for group calls only.
            target_id (integer): The ID of the specific target for which events should be sent.
            target_type (string): The target type.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        request_body = {
            "call_states": call_states,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
            "group_calls_only": group_calls_only,
            "target_id": target_id,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/call"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_call_event_subscription_delete(self, id) -> dict[str, Any]:
        """
        Cancels a subscription identified by the provided ID using the DELETE method, preventing future charges and updating the subscription status to canceled.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/call/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_call_event_subscription_get(self, id) -> dict[str, Any]:
        """
        Retrieves the subscription details identified by the specified subscription ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/call/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_call_event_subscription_update(
        self,
        id,
        call_states=None,
        enabled=None,
        endpoint_id=None,
        group_calls_only=None,
        target_id=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Partially updates a subscription identified by the provided ID using the PATCH method, allowing for selective modification of specific fields in the subscription resource.

        Args:
            id (string): id
            call_states (array): The call event subscription's list of call states.
            enabled (boolean): Whether or not the call event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,
        please provide a valid webhook ID here.
            group_calls_only (boolean): Call event subscription for group calls only.
            target_id (integer): The ID of the specific target for which events should be sent.
            target_type (string): The target type.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "call_states": call_states,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
            "group_calls_only": group_calls_only,
            "target_id": target_id,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/call/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_change_log_event_subscription_list(self, cursor=None) -> dict[str, Any]:
        """
        Retrieves a changelog of subscription updates using the "GET" method, optionally filtering results by a specified cursor, and authenticates via either an API key or Bearer token.

        Args:
            cursor (string): Used for cursor-based pagination, this string parameter specifies a unique identifier to fetch the next page of changelog data.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        url = f"{self.base_url}/api/v2/subscriptions/changelog"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_change_log_event_subscription_create(
        self, enabled=None, endpoint_id=None
    ) -> dict[str, Any]:
        """
        Submits a subscription changelog entry by posting JSON data and returns a 200 response if successful, with authentication handled via API key or bearer token.

        Args:
            enabled (boolean): Whether or not the this change log event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        request_body = {
            "enabled": enabled,
            "endpoint_id": endpoint_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/changelog"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_change_log_event_subscription_delete(self, id) -> dict[str, Any]:
        """
        Deletes a specific changelog entry identified by the provided ID using the "DELETE" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/changelog/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_change_log_event_subscription_get(self, id) -> dict[str, Any]:
        """
        Retrieves the changelog for a specific subscription with the given ID using a GET request, requiring either an API key in the URL or a Bearer token for authentication.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/changelog/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_change_log_event_subscription_update(
        self, id, enabled=None, endpoint_id=None
    ) -> dict[str, Any]:
        """
        Updates a specific changelog subscription by modifying its properties using a JSON patch document, and returns a status message indicating the success of the operation.

        Args:
            id (string): id
            enabled (boolean): Whether or not the change log event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,
        please provide a valid webhook ID here.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "enabled": enabled,
            "endpoint_id": endpoint_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/changelog/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_contact_event_subscription_list(self, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of contact details for subscriptions, allowing pagination via a cursor parameter.

        Args:
            cursor (string): An opaque token used for cursor-based pagination to retrieve the next page of results, typically set to a unique identifier like a timestamp or record ID.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        url = f"{self.base_url}/api/v2/subscriptions/contact"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_contact_event_subscription_create(
        self, contact_type=None, enabled=None, endpoint_id=None
    ) -> dict[str, Any]:
        """
        Creates a new contact subscription using the provided JSON data and returns a successful response.

        Args:
            contact_type (string): The contact type this event subscription subscribes to.
            enabled (boolean): Whether or not the contact event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        request_body = {
            "contact_type": contact_type,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/contact"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_contact_event_subscription_delete(self, id) -> dict[str, Any]:
        """
        Deletes a subscription associated with a specific contact ID, removing the subscription from the system and preventing future charges.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/contact/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_contact_event_subscription_get(self, id) -> dict[str, Any]:
        """
        Retrieves a subscription associated with a specific contact by their ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/contact/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_contact_event_subscription_update(
        self, id, contact_type=None, enabled=None, endpoint_id=None
    ) -> dict[str, Any]:
        """
        Modifies a specific subscription contact by ID using a JSON patch document to update its properties.

        Args:
            id (string): id
            contact_type (string): The contact type this event subscription subscribes to.
            enabled (boolean): Whether or not the contact event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,
        please provide a valid webhook ID here.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "contact_type": contact_type,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/contact/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_sms_event_subscription_list(
        self, cursor=None, target_type=None, target_id=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of SMS subscriptions, optionally filtered by cursor, target type, and target ID.

        Args:
            cursor (string): An opaque token used for cursor-based pagination, specifying the position from which to fetch the next set of results in a paginated list of SMS subscriptions.
            target_type (string): Optional string parameter to specify the target type for subscriptions, with allowed values being callcenter, callrouter, channel, coachinggroup, coachingteam, department, office, room, staffgroup, unknown, or user.
            target_id (integer): Optional integer parameter specifying the target ID for filtering or identifying specific subscriptions in the SMS-related query.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        url = f"{self.base_url}/api/v2/subscriptions/sms"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("target_type", target_type),
                ("target_id", target_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_sms_event_subscription_create(
        self,
        direction=None,
        enabled=None,
        endpoint_id=None,
        include_internal=None,
        status=None,
        target_id=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Sends a subscription request for SMS notifications by creating an SMS subscription.

        Args:
            direction (string): The SMS direction this event subscription subscribes to.
            enabled (boolean): Whether or not the SMS event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully.
            include_internal (boolean): Whether or not to trigger SMS events for SMS sent between two users from the same company.
            status (boolean): Whether or not to update on each SMS delivery status.
            target_id (integer): The ID of the specific target for which events should be sent.
            target_type (string): The target's type.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        request_body = {
            "direction": direction,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
            "include_internal": include_internal,
            "status": status,
            "target_id": target_id,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/sms"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_sms_event_subscription_delete(self, id) -> dict[str, Any]:
        """
        Cancels an SMS subscription by its ID using the DELETE method, removing future charges and updating the subscription status to reflect cancellation.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/sms/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_sms_event_subscription_get(self, id) -> dict[str, Any]:
        """
        Retrieves the details of a specific SMS subscription identified by the provided subscription ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/subscriptions/sms/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_sms_event_subscription_update(
        self,
        id,
        direction=None,
        enabled=None,
        endpoint_id=None,
        include_internal=None,
        status=None,
        target_id=None,
        target_type=None,
    ) -> dict[str, Any]:
        """
        Updates an SMS subscription identified by its ID, modifying specific properties using JSON Patch operations.

        Args:
            id (string): id
            direction (string): The SMS direction this event subscription subscribes to.
            enabled (boolean): Whether or not the SMS event subscription is enabled.
            endpoint_id (integer): The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,
        please provide a valid webhook ID here.
            include_internal (boolean): Whether or not to trigger SMS events for SMS sent between two users from the same company.
            status (boolean): Whether or not to update on each SMS delivery status.
            target_id (integer): The ID of the specific target for which events should be sent.
            target_type (string): The target's type.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "direction": direction,
            "enabled": enabled,
            "endpoint_id": endpoint_id,
            "include_internal": include_internal,
            "status": status,
            "target_id": target_id,
            "target_type": target_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/subscriptions/sms/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def transcripts_get(self, call_id) -> dict[str, Any]:
        """
        Retrieves a transcript for a specific call identified by the call ID using the GET method.

        Args:
            call_id (string): call_id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            transcripts
        """
        if call_id is None:
            raise ValueError("Missing required parameter 'call_id'")
        url = f"{self.base_url}/api/v2/transcripts/{call_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def transcripts_get_url(self, call_id) -> dict[str, Any]:
        """
        Retrieves the URL for a transcript associated with a specific call ID using the GET method.

        Args:
            call_id (string): call_id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            transcripts
        """
        if call_id is None:
            raise ValueError("Missing required parameter 'call_id'")
        url = f"{self.base_url}/api/v2/transcripts/{call_id}/url"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def userdevices_get(self, id) -> dict[str, Any]:
        """
        Retrieves details about a user device specified by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            userdevices
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/userdevices/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def userdevices_list(self, cursor=None, user_id=None) -> dict[str, Any]:
        """
        Retrieves a list of user devices, optionally filtered by a user ID or a cursor for pagination.

        Args:
            cursor (string): A string value used as a pointer to fetch the next or previous paginated set of user devices, enabling efficient traversal through large datasets without numeric offsets.
            user_id (string): Specifies the unique identifier of the user for filtering the devices returned in the query.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            userdevices
        """
        url = f"{self.base_url}/api/v2/userdevices"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("user_id", user_id)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_initiate_call(
        self,
        id,
        custom_data=None,
        group_id=None,
        group_type=None,
        outbound_caller_id=None,
        phone_number=None,
    ) -> dict[str, Any]:
        """
        Initiates a call for a user identified by the provided ID using the POST method, sending JSON data in the request body.

        Args:
            id (string): id
            custom_data (string): Extra data to associate with the call. This will be passed through to any subscribed call events.
            group_id (integer): The ID of a group that will be used to initiate the call.
            group_type (string): The type of a group that will be used to initiate the call.
            outbound_caller_id (string): The e164-formatted number shown to the call recipient (or "blocked").

        If set to "blocked", the recipient will receive a call from "unknown caller". The number can be the caller's number, or the caller's group number if the group is provided,
        or the caller's company reserved number.
            phone_number (string): The e164-formatted number to call.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "custom_data": custom_data,
            "group_id": group_id,
            "group_type": group_type,
            "outbound_caller_id": outbound_caller_id,
            "phone_number": phone_number,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/initiate_call"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_update_active_call(
        self, id, is_recording=None, play_message=None, recording_type=None
    ) -> dict[str, Any]:
        """
        Updates the active call status for a user with the specified ID using the PATCH method and returns a status message.

        Args:
            id (string): id
            is_recording (boolean): Whether or not recording should be enabled.
            play_message (boolean): Whether or not to play a message to indicate the call is being recorded (or recording has stopped).
            recording_type (string): Whether or not to toggle recording for the operator call (personal recording),
        the group call (department recording), or both.

        Only applicable for group calls (call centers, departments, etc.)

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "is_recording": is_recording,
            "play_message": play_message,
            "recording_type": recording_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/activecall"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_toggle_call_vi(self, id, enable_vi=None) -> dict[str, Any]:
        """
        Toggles the "vi" setting for a user with the specified ID using the PATCH method.

        Args:
            id (string): id
            enable_vi (boolean): Whether or not call vi should be enabled.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "enable_vi": enable_vi,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/togglevi"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def caller_id_users_get(self, id) -> dict[str, Any]:
        """
        Retrieves the caller ID information for a user identified by the provided ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/users/{id}/caller_id"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def caller_id_users_post(self, id, caller_id=None) -> dict[str, Any]:
        """
        Updates the caller ID for a user with the specified ID using a JSON payload and returns a successful response upon completion.

        Args:
            id (string): id
            caller_id (string): Phone number (e164 formatted) that will be defined as a Caller ID for the target. Use 'blocked' to block the Caller ID.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "caller_id": caller_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/caller_id"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deskphones_users_delete(self, parent_id, id) -> Any:
        """
        Deletes a specific deskphone associated with a user identified by the parent ID and deskphone ID using the DELETE method.

        Args:
            parent_id (string): parent_id
            id (string): id

        Returns:
            Any: A successful response

        Tags:
            users
        """
        if parent_id is None:
            raise ValueError("Missing required parameter 'parent_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/users/{parent_id}/deskphones/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deskphones_users_get(self, parent_id, id) -> dict[str, Any]:
        """
        Retrieves details of a specific desk phone associated with a user, identified by the parent ID and desk phone ID.

        Args:
            parent_id (string): parent_id
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if parent_id is None:
            raise ValueError("Missing required parameter 'parent_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/users/{parent_id}/deskphones/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deskphones_users_list(self, parent_id) -> dict[str, Any]:
        """
        Retrieves a list of desk phones associated with a specific parent ID.

        Args:
            parent_id (string): parent_id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if parent_id is None:
            raise ValueError("Missing required parameter 'parent_id'")
        url = f"{self.base_url}/api/v2/users/{parent_id}/deskphones"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_assign_user_number_post(
        self, id, area_code=None, number=None, primary=None
    ) -> dict[str, Any]:
        """
        Assigns a number to the user identified by the given ID using a POST request with JSON payload and returns a 200 status on success.

        Args:
            id (string): id
            area_code (string): An area code in which to find an available phone number for assignment.
            number (string): A phone number to assign. (e164-formatted)
            primary (boolean): A boolean indicating whether this should become the primary phone number.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "area_code": area_code,
            "number": number,
            "primary": primary,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/assign_number"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def numbers_user_unassign_number_post(self, id, number=None) -> dict[str, Any]:
        """
        Unassigns a phone number from a user using the POST method by providing the user ID in the path and the necessary details in the JSON request body.

        Args:
            id (string): id
            number (string): A phone number to unassign. (e164-formatted)

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "number": number,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/unassign_number"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_toggle_dnd(
        self, id, do_not_disturb=None, group_id=None, group_type=None
    ) -> dict[str, Any]:
        """
        Toggles the DND status for a user with the specified ID using the PATCH method, accepting a JSON payload.

        Args:
            id (string): id
            do_not_disturb (boolean): Determines if DND is ON or OFF.
            group_id (integer): The ID of the group which the user's DND status will be updated for.
            group_type (string): The type of the group which the user's DND status will be updated for.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "do_not_disturb": do_not_disturb,
            "group_id": group_id,
            "group_type": group_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/togglednd"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_e911_get(self, id) -> dict[str, Any]:
        """
        Retrieves the Enhanced 911 (E911) information for a specific user identified by their ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/users/{id}/e911"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_e911_update(
        self,
        id,
        address=None,
        address2=None,
        city=None,
        country=None,
        state=None,
        use_validated_option=None,
        zip=None,
    ) -> dict[str, Any]:
        """
        Updates the E911 (Enhanced 911) location information for a user identified by the specified ID.

        Args:
            id (string): id
            address (string): [single-line only]

        Line 1 of the new E911 address.
            address2 (string): [single-line only]

        Line 2 of the new E911 address.
            city (string): [single-line only]

        City of the new E911 address.
            country (string): Country of the new E911 address.
            state (string): [single-line only]

        State or Province of the new E911 address.
            use_validated_option (boolean): Whether to use the validated address option from our service.
            zip (string): [single-line only]

        Zip of the new E911 address.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "address": address,
            "address2": address2,
            "city": city,
            "country": country,
            "state": state,
            "use_validated_option": use_validated_option,
            "zip": zip,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/e911"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_personas_get(self, id) -> dict[str, Any]:
        """
        Retrieves the personas associated with a user identified by the provided `{id}` parameter using the `GET` method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/users/{id}/personas"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def screen_pop_initiate(self, id, screen_pop_uri=None) -> dict[str, Any]:
        """
        Triggers a screen pop for the specified user by their ID, requiring a JSON request body, and returns a success status upon completion.

        Args:
            id (string): id
            screen_pop_uri (string): The screen pop's url.

        Most Url should start with scheme name such as http or https. Be aware that url with userinfo subcomponent, such as
        "https://username:password@www.example.com" is not supported for security reasons. Launching native apps is also supported through a format such as "customuri://domain.com"

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "screen_pop_uri": screen_pop_uri,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/screenpop"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_delete(self, id) -> dict[str, Any]:
        """
        Deletes a user with the specified ID from the system, potentially removing associated data and roles.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/users/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_get(self, id) -> dict[str, Any]:
        """
        Retrieves the details of a specific user identified by the provided ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/users/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_update(
        self,
        id,
        admin_office_ids=None,
        emails=None,
        extension=None,
        first_name=None,
        forwarding_numbers=None,
        is_super_admin=None,
        job_title=None,
        keep_paid_numbers=None,
        last_name=None,
        license=None,
        office_id=None,
        phone_numbers=None,
        presence_status=None,
        state=None,
    ) -> dict[str, Any]:
        """
        Partially updates the user identified by the given ID with the specified JSON data and returns a success response.

        Args:
            id (string): id
            admin_office_ids (array): The list of admin office IDs.

        This is used to set the user as an office admin for the offices with the provided IDs.
            emails (array): The user's emails.

        This can be used to add, remove, or re-order emails. The first email in the list is the user's primary email.
            extension (string): The user's new extension number.

        Extensions are optional in Dialpad and turned off by default. If you want extensions please contact support to enable them.
            first_name (string): [single-line only]

        The user's first name.
            forwarding_numbers (array): A list of phone numbers that should be dialed in addition to the user's Dialpad number(s)
        upon receiving a call.
            is_super_admin (boolean): Whether or not the user is a super admin. (company level administrator)
            job_title (string): [single-line only]

        The user's job title.
            keep_paid_numbers (boolean): Whether or not to keep phone numbers when switching to a support license.

        Note: Phone numbers require additional number licenses under a support license.
            last_name (string): [single-line only]

        The user's last name.
            license (string): The user's license type.

        Changing this affects billing for the user. For a Sell license, specify the type as `agents`. For a Support license, specify the type as `support`.
            office_id (integer): The user's office id.

        If provided, the user will be moved to this office. For international offices, the user must not have phone numbers assigned. Once the transfer is complete, your admin can add the phone numbers via the user assign number API. Only supported on paid accounts and there must be enough licenses to transfer the user to the destination office.
            phone_numbers (array): A list of the phone number(s) assigned to this user.

        This can be used to re-order or remove numbers. To assign a new number, use the assign number API instead.
            presence_status (object): presence_status
            state (string): The user's state.

        This is used to suspend or re-activate a user.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "admin_office_ids": admin_office_ids,
            "emails": emails,
            "extension": extension,
            "first_name": first_name,
            "forwarding_numbers": forwarding_numbers,
            "is_super_admin": is_super_admin,
            "job_title": job_title,
            "keep_paid_numbers": keep_paid_numbers,
            "last_name": last_name,
            "license": license,
            "office_id": office_id,
            "phone_numbers": phone_numbers,
            "presence_status": presence_status,
            "state": state,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_list(
        self, cursor=None, state=None, company_admin=None, email=None, number=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of users with optional filtering by cursor, state, company admin status, email, or number using the "/api/v2/users" GET endpoint.

        Args:
            cursor (string): A string token used to fetch the next page of users after the specified cursor in paginated results.
            state (string): Filters users by their account state, accepting values: active, all, cancelled, deleted, pending, or suspended.
            company_admin (boolean): Filters the user list to only include users who are company administrators if set to true.
            email (string): Optional query parameter to filter users by email address.
            number (string): An optional string parameter to specify a custom number for filtering or querying users.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        url = f"{self.base_url}/api/v2/users"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("state", state),
                ("company_admin", company_admin),
                ("email", email),
                ("number", number),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_create(
        self,
        auto_assign=None,
        email=None,
        first_name=None,
        last_name=None,
        license=None,
        office_id=None,
    ) -> dict[str, Any]:
        """
        Creates a new user resource using JSON data and returns a success response with a status code of 200 OK.

        Args:
            auto_assign (boolean): If set to true, a number will be automatically assigned.
            email (string): The user's email.
            first_name (string): [single-line only]

        The user's first name.
            last_name (string): [single-line only]

        The user's last name.
            license (string): The user's license type. This affects billing for the user.
            office_id (integer): The user's office id.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users, important
        """
        request_body = {
            "auto_assign": auto_assign,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "license": license,
            "office_id": office_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_move_office_patch(self, id, office_id=None) -> dict[str, Any]:
        """
        Updates the office location of a user with the specified ID using a JSON payload.

        Args:
            id (string): id
            office_id (integer): The user's office id. When provided, the user will be moved to this office.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "office_id": office_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/move_office"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_update_status(
        self, id, expiration=None, status_message=None
    ) -> dict[str, Any]:
        """
        Updates the status of a user with the specified ID using the PATCH method.

        Args:
            id (string): id
            expiration (integer): The expiration of this status. None for no expiration.
            status_message (string): The status message for the user.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "expiration": expiration,
            "status_message": status_message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/users/{id}/status"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhooks_list(self, cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of webhooks, optionally supporting pagination with a cursor query parameter.

        Args:
            cursor (string): A string value representing a cursor used to fetch the next page of webhook records in a paginated response.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            webhooks
        """
        url = f"{self.base_url}/api/v2/webhooks"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhooks_create(self, hook_url=None, secret=None) -> dict[str, Any]:
        """
        Creates a new webhook endpoint that sends HTTP notifications in response to specified events.

        Args:
            hook_url (string): The webhook's URL. Triggered events will be sent to the url provided here.
            secret (string): [single-line only]

        Webhook's signature secret that's used to confirm the validity of the request.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            webhooks
        """
        request_body = {
            "hook_url": hook_url,
            "secret": secret,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/webhooks"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhooks_delete(self, id) -> dict[str, Any]:
        """
        Deletes the webhook with the specified ID and returns a success status.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            webhooks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/webhooks/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhooks_get(self, id) -> dict[str, Any]:
        """
        Retrieves details of a webhook by its ID using the "GET" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            webhooks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/webhooks/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_update(self, id, hook_url=None, secret=None) -> dict[str, Any]:
        """
        Updates a specific webhook resource by its ID using a partial payload sent via PATCH.

        Args:
            id (string): id
            hook_url (string): The webhook's URL. Triggered events will be sent to the url provided here.
            secret (string): [single-line only]

        Webhook's signature secret that's used to confirm the validity of the request.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            webhooks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "hook_url": hook_url,
            "secret": secret,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/webhooks/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def websockets_list(self, cursor=None) -> dict[str, Any]:
        """
        Establishes a WebSocket connection at "/api/v2/websockets" using the GET method, allowing optional specification of a cursor for resuming data consumption.

        Args:
            cursor (string): An opaque token used for cursor-based pagination, allowing retrieval of data in a specific order by marking the position in the dataset.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            websockets
        """
        url = f"{self.base_url}/api/v2/websockets"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def websockets_create(self, secret=None) -> dict[str, Any]:
        """
        Establishes a WebSocket connection using the POST method to the "/api/v2/websockets" endpoint, accepting JSON data in the request body.

        Args:
            secret (string): [single-line only]

        Websocket's signature secret that's used to confirm the validity of the request.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            websockets
        """
        request_body = {
            "secret": secret,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/websockets"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def websockets_delete(self, id) -> dict[str, Any]:
        """
        Deletes a WebSocket by its ID, specified in the path, using the "DELETE" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            websockets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/websockets/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def websockets_get(self, id) -> dict[str, Any]:
        """
        Retrieves details for a specific WebSocket connection identified by its integer ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A successful response

        Tags:
            websockets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/v2/websockets/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def websockets_update(self, id, secret=None) -> dict[str, Any]:
        """
        Updates the WebSocket connection resource identified by the specified ID using a JSON-formatted patch request.

        Args:
            id (string): id
            secret (string): [single-line only]

        Websocket's signature secret that's used to confirm the validity of the request.

        Returns:
            dict[str, Any]: A successful response

        Tags:
            websockets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "secret": secret,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/v2/websockets/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.accesscontrolpolicies_assign,
            self.accesscontrolpolicies_list,
            self.accesscontrolpolicies_create,
            self.accesscontrolpolicies_delete,
            self.accesscontrolpolicies_get,
            self.accesscontrolpolicies_update,
            self.accesscontrolpolicies_assignments,
            self.accesscontrolpolicies_unassign,
            self.app_settings_get,
            self.blockednumbers_add,
            self.blockednumbers_get,
            self.blockednumbers_remove,
            self.blockednumbers_list,
            self.call_participants_add,
            self.call_get_call_info,
            self.call_initiate_ivr_call,
            self.call_list,
            self.call_call,
            self.call_transfer_call,
            self.call_unpark,
            self.call_actions_hangup,
            self.call_put_call_labels,
            self.call_callback,
            self.call_validate_callback,
            self.callcenters_listall,
            self.callcenters_create,
            self.callcenters_delete,
            self.callcenters_get,
            self.callcenters_update,
            self.callcenters_status,
            self.callcenters_operators_get_dutystatus,
            self.callcenters_operators_dutystatus,
            self.callcenters_operators_get_skilllevel,
            self.callcenters_operators_skilllevel,
            self.callcenters_operators_delete,
            self.callcenters_operators_get,
            self.callcenters_operators_post,
            self.calllabel_list,
            self.call_review_share_link_create,
            self.call_review_share_link_delete,
            self.call_review_share_link_get,
            self.call_review_share_link_update,
            self.callrouters_list,
            self.callrouters_create,
            self.callrouters_delete,
            self.callrouters_get,
            self.callrouters_update,
            self.numbers_assign_call_router_number_post,
            self.channels_delete,
            self.channels_get,
            self.channels_list,
            self.channels_post,
            self.channels_members_delete,
            self.channels_members_list,
            self.channels_members_post,
            self.coaching_team_members_get,
            self.coaching_team_members_add,
            self.coaching_team_get,
            self.coaching_team_listall,
            self.company_get,
            self.company_sms_opt_out,
            self.conference_rooms_list,
            self.conference_meetings_list,
            self.contacts_delete,
            self.contacts_get,
            self.contacts_update,
            self.contacts_list,
            self.contacts_create,
            self.contacts_create_with_uid,
            self.ivr_delete,
            self.ivr_update,
            self.custom_ivrs_get,
            self.ivr_create,
            self.ivr_details_update,
            self.departments_delete,
            self.departments_get,
            self.departments_update,
            self.departments_listall,
            self.departments_create,
            self.departments_operators_delete,
            self.departments_operators_get,
            self.departments_operators_post,
            self.faxline_create,
            self.numbers_assign_number_post,
            self.numbers_assign_target_number_post,
            self.numbers_delete,
            self.numbers_get,
            self.numbers_list,
            self.format_post,
            self.oauth2_authorize_get,
            self.oauth2_deauthorize_post,
            self.plan_get,
            self.callcenters_list,
            self.coaching_team_list,
            self.departments_list,
            self.numbers_assign_office_number_post,
            self.numbers_office_unassign_number_post,
            self.offices_e911_get,
            self.offices_e911_update,
            self.plan_available_licenses_get,
            self.offices_offdutystatuses_get,
            self.offices_get,
            self.offices_list,
            self.offices_create,
            self.offices_operators_delete,
            self.offices_operators_get,
            self.offices_operators_post,
            self.recording_share_link_create,
            self.recording_share_link_delete,
            self.recording_share_link_get,
            self.recording_share_link_update,
            self.numbers_assign_room_number_post,
            self.numbers_room_unassign_number_post,
            self.rooms_delete,
            self.rooms_get,
            self.rooms_patch,
            self.rooms_list,
            self.rooms_post,
            self.deskphones_rooms_create_international_pin,
            self.deskphones_rooms_delete,
            self.deskphones_rooms_get,
            self.deskphones_rooms_list,
            self.schedule_reports_delete,
            self.schedule_reports_get,
            self.schedule_reports_update,
            self.schedule_reports_list,
            self.schedule_reports_create,
            self.sms_send,
            self.stats_get,
            self.stats_create,
            self.webhook_agent_status_event_subscription_list,
            self.webhook_agent_status_event_subscription_create,
            self.webhook_agent_status_event_subscription_delete,
            self.webhook_agent_status_event_subscription_get,
            self.webhook_agent_status_event_subscription_update,
            self.webhook_call_event_subscription_list,
            self.webhook_call_event_subscription_create,
            self.webhook_call_event_subscription_delete,
            self.webhook_call_event_subscription_get,
            self.webhook_call_event_subscription_update,
            self.webhook_change_log_event_subscription_list,
            self.webhook_change_log_event_subscription_create,
            self.webhook_change_log_event_subscription_delete,
            self.webhook_change_log_event_subscription_get,
            self.webhook_change_log_event_subscription_update,
            self.webhook_contact_event_subscription_list,
            self.webhook_contact_event_subscription_create,
            self.webhook_contact_event_subscription_delete,
            self.webhook_contact_event_subscription_get,
            self.webhook_contact_event_subscription_update,
            self.webhook_sms_event_subscription_list,
            self.webhook_sms_event_subscription_create,
            self.webhook_sms_event_subscription_delete,
            self.webhook_sms_event_subscription_get,
            self.webhook_sms_event_subscription_update,
            self.transcripts_get,
            self.transcripts_get_url,
            self.userdevices_get,
            self.userdevices_list,
            self.users_initiate_call,
            self.users_update_active_call,
            self.users_toggle_call_vi,
            self.caller_id_users_get,
            self.caller_id_users_post,
            self.deskphones_users_delete,
            self.deskphones_users_get,
            self.deskphones_users_list,
            self.numbers_assign_user_number_post,
            self.numbers_user_unassign_number_post,
            self.users_toggle_dnd,
            self.users_e911_get,
            self.users_e911_update,
            self.users_personas_get,
            self.screen_pop_initiate,
            self.users_delete,
            self.users_get,
            self.users_update,
            self.users_list,
            self.users_create,
            self.users_move_office_patch,
            self.users_update_status,
            self.webhooks_list,
            self.webhooks_create,
            self.webhooks_delete,
            self.webhooks_get,
            self.webhook_update,
            self.websockets_list,
            self.websockets_create,
            self.websockets_delete,
            self.websockets_get,
            self.websockets_update,
        ]
