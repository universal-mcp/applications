from typing import Any

from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class RocketlaneApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="rocketlane", integration=integration, **kwargs)
        self.base_url = "https://api.rocketlane.com/api"

    def _get_headers(self) -> dict[str, str]:
        """
        Get the headers for Rocketlane API requests.
        Overrides the base class method to use 'api-key'.
        """
        if not self.integration:
            logger.warning(
                "RocketlaneApp: No integration configured, returning empty headers."
            )
            return {}

        credentials = self.integration.get_credentials()

        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )

        if not api_key:
            logger.error("RocketlaneApp: API key not found in integration credentials.")
            return {"Content-Type": "application/json", "Cache-Control": "no-cache"}

        logger.debug("RocketlaneApp: Using 'api-key' for authentication.")
        return {
            "api-key": api_key,  # Correct header name for Rocketlane
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
        }

    def get_time_entry(
        self,
        timeEntryId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get a time entry

        Args:
            timeEntryId (string): timeEntryId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time Tracking
        """
        if timeEntryId is None:
            raise ValueError("Missing required parameter 'timeEntryId'.")
        url = f"{self.base_url}/1.0/time-entries/{timeEntryId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def update_time_entry(
        self,
        timeEntryId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        timeEntryId_body: int | None = None,
        date: str | None = None,
        minutes: int | None = None,
        activityName: str | None = None,
        notes: str | None = None,
        category: dict[str, Any] | None = None,
        billable: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update a time entry

        Args:
            timeEntryId (string): timeEntryId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            timeEntryId_body (integer): The unique, system-generated identifier, which can be used to identify the time entry globally. Example: '201'.
            date (string): Date of the time entry in format YYYY-MM-DD Example: '2023-03-28'.
            minutes (integer): Duration of the time entry in minutes Example: '250'.
            activityName (string): Name of the adhoc activity being performed Example: 'Pre-Sales campaign'.
            notes (string): Notes for the time entry Example: 'Working on API integration'.
            category (object): Category associated with the time entry
            billable (boolean): billable

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time Tracking
        """
        if timeEntryId is None:
            raise ValueError("Missing required parameter 'timeEntryId'.")
        request_body_data = None
        request_body_data = {
            "timeEntryId": timeEntryId_body,
            "date": date,
            "minutes": minutes,
            "activityName": activityName,
            "notes": notes,
            "category": category,
            "billable": billable,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/time-entries/{timeEntryId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def delete_time_entry(self, timeEntryId: str) -> Any:
        """
        Delete a time entry

        Args:
            timeEntryId (string): timeEntryId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time Tracking
        """
        if timeEntryId is None:
            raise ValueError("Missing required parameter 'timeEntryId'.")
        url = f"{self.base_url}/1.0/time-entries/{timeEntryId}"
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

    def get_task(
        self,
        taskId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get task by Id

        Args:
            taskId (string): taskId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        url = f"{self.base_url}/1.0/tasks/{taskId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def update_task(
        self,
        taskId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        taskId_body: int | None = None,
        taskName: str | None = None,
        taskDescription: str | None = None,
        taskPrivateNote: str | None = None,
        startDate: str | None = None,
        dueDate: str | None = None,
        effortInMinutes: int | None = None,
        progress: int | None = None,
        atRisk: bool | None = None,
        type: str | None = None,
        fields: list[dict[str, Any]] | None = None,
        status: dict[str, Any] | None = None,
        externalReferenceId: str | None = None,
        private: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update task by Id

        Args:
            taskId (string): taskId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            taskId_body (integer): The task’s unique, system-generated **identifier**, which can be used to identify the task globally Example: '201'.
            taskName (string): The **name** of the task. Example: 'Kick off'.
            taskDescription (string): The `description` of the task. The description body needs to be in **html** format to avoid any formatting issues in the application. Example: '<p>Schedule Kick off meeting with the stakeholders involved.</p>'.
            taskPrivateNote (string): The `privateNote` for the task is intended exclusively for team members. The note's content should be in `HTML` format to prevent any formatting issues in the application. Example: '<p>Schedule Kick off meeting with the stakeholders involved.</p>'.
            startDate (string): The date when a task starts its execution. It can be empty. The format for the start date is _YYYY-MM-DD_. Example: '2023-03-28'.
            dueDate (string): The date when a task completes its execution. It can be empty. If both `startDate` and `dueDate` are specified for a given task, it is necessary that the latter should be on or after the given `startDate`. The format for the due date is _YYYY-MM-DD_. Example: '2023-03-28'.
            effortInMinutes (integer): The effort is the expected time required to complete the task. The value is determined in minutes. Example: '3000'.
            progress (integer): The task’s progress, if indicated, will be available here and ranges in value from 0 to 100. The task’s status can be used in place of this field, however progress can offer more precise data. Example: '50'.
            atRisk (boolean): Indicates whether the task has been marked as At Risk. This parameter is used to indicate that immediate action is necessary to unblock the task’s execution. Example: 'True'.
            type (string): The type of the task if specified will be available here. There are two options: `MILESTONE` or `TASK`. If a task is not explicitly marked as a milestone, it takes the default value as `TASK`. Milestones refer to critical tasks in the project that include an inbuilt CSAT capability that allows customers to offer CSAT evaluations depending on the task’s execution. Example: 'MILESTONE'.
            fields (array): The custom fields can be set during the task creation with the help of `fields`. The `fieldValue` can be either a string or a number or an array and it has to comply with the type of the field. Refer [examples](https://developer.rocketlane.com/v1.0/docs/custom-fields#examples-of-requests-and-responses-for-assigning-custom-field-values) to know how to assign `fieldValue` based on their `field_type`.
            status (object): The value of the task status can be specified here and this is essential to keep track of it.
            externalReferenceId (string): An externalReferenceId is a unique identifier that links entities or transactions between external systems and Rocketlane, ensuring accurate data correlation and consistency. Example: 'task_8171'.
            private (boolean): This depicts if the task is private or not. Example: 'False'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        request_body_data = None
        request_body_data = {
            "taskId": taskId_body,
            "taskName": taskName,
            "taskDescription": taskDescription,
            "taskPrivateNote": taskPrivateNote,
            "startDate": startDate,
            "dueDate": dueDate,
            "effortInMinutes": effortInMinutes,
            "progress": progress,
            "atRisk": atRisk,
            "type": type,
            "fields": fields,
            "status": status,
            "externalReferenceId": externalReferenceId,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks/{taskId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def delete_task(self, taskId: str) -> Any:
        """
        Delete task by Id

        Args:
            taskId (string): taskId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        url = f"{self.base_url}/1.0/tasks/{taskId}"
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

    def get_space(self, spaceId: str) -> dict[str, Any]:
        """
        Get space by Id

        Args:
            spaceId (string): spaceId

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        if spaceId is None:
            raise ValueError("Missing required parameter 'spaceId'.")
        url = f"{self.base_url}/1.0/spaces/{spaceId}"
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

    def update_space(
        self, spaceId: str, spaceName: str | None = None
    ) -> dict[str, Any]:
        """
        Update space by Id

        Args:
            spaceId (string): spaceId
            spaceName (string): The name of the space. Example: 'Shared space'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        if spaceId is None:
            raise ValueError("Missing required parameter 'spaceId'.")
        request_body_data = None
        request_body_data = {
            "spaceName": spaceName,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/spaces/{spaceId}"
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

    def delete_space(self, spaceId: str) -> Any:
        """
        Delete space by Id

        Args:
            spaceId (string): spaceId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        if spaceId is None:
            raise ValueError("Missing required parameter 'spaceId'.")
        url = f"{self.base_url}/1.0/spaces/{spaceId}"
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

    def get_space_document(self, spaceDocumentId: str) -> dict[str, Any]:
        """
        Get space document by Id

        Args:
            spaceDocumentId (string): spaceDocumentId

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Space Documents
        """
        if spaceDocumentId is None:
            raise ValueError("Missing required parameter 'spaceDocumentId'.")
        url = f"{self.base_url}/1.0/space-documents/{spaceDocumentId}"
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

    def update_space_document(
        self,
        spaceDocumentId: str,
        spaceDocumentId_body: int | None = None,
        spaceDocumentName: str | None = None,
        url: str | None = None,
    ) -> dict[str, Any]:
        """
        Update space document by Id

        Args:
            spaceDocumentId (string): spaceDocumentId
            spaceDocumentId_body (integer): The space document’s unique, system-generated identifier, which can be used to identify the space document globally. Example: '201'.
            spaceDocumentName (string): The name of the space document. Example: 'Sample file'.
            url (string): The url that is embedded in the space document. Example: 'https://www.google.com'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Space Documents
        """
        if spaceDocumentId is None:
            raise ValueError("Missing required parameter 'spaceDocumentId'.")
        request_body_data = None
        request_body_data = {
            "spaceDocumentId": spaceDocumentId_body,
            "spaceDocumentName": spaceDocumentName,
            "url": url,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/space-documents/{spaceDocumentId}"
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

    def delete_space_document(self, spaceDocumentId: str) -> Any:
        """
        Delete space document by Id

        Args:
            spaceDocumentId (string): spaceDocumentId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Space Documents
        """
        if spaceDocumentId is None:
            raise ValueError("Missing required parameter 'spaceDocumentId'.")
        url = f"{self.base_url}/1.0/space-documents/{spaceDocumentId}"
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

    def get_project(
        self,
        projectId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get project by Id

        Args:
            projectId (string): projectId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects, important
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        url = f"{self.base_url}/1.0/projects/{projectId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def update_project(
        self,
        projectId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        projectName: str | None = None,
        startDate: str | None = None,
        dueDate: str | None = None,
        visibility: str | None = None,
        owner: dict[str, Any] | None = None,
        status: dict[str, Any] | None = None,
        fields: list[dict[str, Any]] | None = None,
        annualizedRecurringRevenue: int | None = None,
        projectFee: int | None = None,
        autoAllocation: bool | None = None,
        budgetedHours: float | None = None,
        externalReferenceId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update project by Id

        Args:
            projectId (string): projectId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            projectName (string): The `name` of the project. The name specified will be displayed everywhere else and can be used for filtering purposes. Example: 'Acme onboarding'.
            startDate (string): On this date the project's execution officially begins. If sources (templates) are mentioned in the request, the start date is required. For projects without any defined sources, it may be empty. The format for the start date is _YYYY-MM-DD_. Example: '2023-03-28'.
            dueDate (string): The day on which the project's execution is planned to be completed. The due date is not required and can be left blank. If sources (templates) are included as part of the project creation, the project's due date will be calculated depending on the duration of the specified sources. For projects where both `startDate` and `dueDate` are specified, the latter must be on or after the given `startDate`. The format for the due date is _YYYY-MM-DD_. Example: '2023-03-28'.
            visibility (string): Set visibility parameters to restrict who can see your project. There are two options: `EVERYONE` and `MEMBERS`. Selecting `EVERYONE` allows all team members from your firm to view the project, while selecting `MEMBERS` restricts access to only those team members who have been specifically invited. Example: 'EVERYONE'.
            owner (object): The project owner gets access to everything in the project and can be used to control the activities that happens in the project. Note: Changing the owner can result in `transfer of ownership` from the older member to the specified member. All the access for the older member will be `revoked`.
            status (object): The value of the project status can be specified here and this is essential to keep track of the project. Example: 'In progress'.
            fields (array): The custom fields can be set during the project creation with the help of `fields`. The `fieldValue` can be either a string or a number or an array and it has to comply with the type of the field. Refer [examples](https://developer.rocketlane.com/v1.0/docs/custom-fields#examples-of-requests-and-responses-for-assigning-custom-field-values) to know how to assign `fieldValue` based on their `field_type`.
            annualizedRecurringRevenue (integer): Indicates the value of the recurring revenue of the customer's subscriptions for a single calendar year. Example: '10000'.
            projectFee (integer): The total fee that is charged for the project. Example: '100000'.
            autoAllocation (boolean): The field autoAllocation defines whether Auto Allocation is enabled for the project or not. If auto allocation is enabled, instead of adding it manually, the allocations are computed from the tasks duration, effort and the assignees specified in the project. Example: 'False'.
            budgetedHours (number): Budgeted hours represent the total hours allocated for project execution. This value can be edited at any point throughout the project’s duration. You can enter the budgeted hours in decimal form, including both hours and minutes, with up to two decimal places of precision. Eg: 1.65 hrs = 1h 39m(1.65h * 60m = 99m). Example: '10.5'.
            externalReferenceId (string): An externalReferenceId is a unique identifier that links entities or transactions between external systems and Rocketlane, ensuring accurate data correlation and consistency. Example: 'pr_8171'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects, important
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        request_body_data = None
        request_body_data = {
            "projectName": projectName,
            "startDate": startDate,
            "dueDate": dueDate,
            "visibility": visibility,
            "owner": owner,
            "status": status,
            "fields": fields,
            "annualizedRecurringRevenue": annualizedRecurringRevenue,
            "projectFee": projectFee,
            "autoAllocation": autoAllocation,
            "budgetedHours": budgetedHours,
            "externalReferenceId": externalReferenceId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/projects/{projectId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def delete_project(self, projectId: str) -> Any:
        """
        Delete project by Id

        Args:
            projectId (string): projectId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects, important
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        url = f"{self.base_url}/1.0/projects/{projectId}"
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

    def get_phase(
        self,
        phaseId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get phase by Id

        Args:
            phaseId (string): phaseId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Phases
        """
        if phaseId is None:
            raise ValueError("Missing required parameter 'phaseId'.")
        url = f"{self.base_url}/1.0/phases/{phaseId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def update_phase(
        self,
        phaseId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        phaseName: str | None = None,
        startDate: str | None = None,
        dueDate: str | None = None,
        status: dict[str, Any] | None = None,
        private: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update phase by Id

        Args:
            phaseId (string): phaseId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            phaseName (string): The `name` of the phase. The name specified will be displayed everywhere else and can be used for filtering purposes. Example: 'Go live'.
            startDate (string): On this date the phase's execution officially begins. The format for the start date is _YYYY-MM-DD_. Example: '2023-03-28'.
            dueDate (string): The day on which the phase's execution is planned to be completed. The `dueDate` must be on or after the given `startDate`. The format for the due date is _YYYY-MM-DD_. Example: '2023-03-28'.
            status (object): The value of the phase status can be specified here and this is essential to keep track of the phase.
            private (boolean): Describes the privacy of the phase i.e. if it is private or shared. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Phases
        """
        if phaseId is None:
            raise ValueError("Missing required parameter 'phaseId'.")
        request_body_data = None
        request_body_data = {
            "phaseName": phaseName,
            "startDate": startDate,
            "dueDate": dueDate,
            "status": status,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/phases/{phaseId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def delete_phase(self, phaseId: str) -> Any:
        """
        Delete phase by Id

        Args:
            phaseId (string): phaseId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Phases
        """
        if phaseId is None:
            raise ValueError("Missing required parameter 'phaseId'.")
        url = f"{self.base_url}/1.0/phases/{phaseId}"
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

    def get_field(
        self,
        fieldId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get field by Id

        Args:
            fieldId (string): fieldId
            includeFields (array): This query parameter allows you to specify which field properties should be returned in the response body by selecting from the drop down. To get the relevant field properties, use comma separated values. If this field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the field properties should be returned in the response body. If the field is left blank, the default field properties are returned. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Fields
        """
        if fieldId is None:
            raise ValueError("Missing required parameter 'fieldId'.")
        url = f"{self.base_url}/1.0/fields/{fieldId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def update_field(
        self,
        fieldId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        fieldLabel: str | None = None,
        fieldDescription: str | None = None,
        enabled: bool | None = None,
        private: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update field by Id

        Args:
            fieldId (string): fieldId
            includeFields (array): This query parameter allows you to specify which field properties should be returned in the response body by selecting from the drop down. To get the relevant field properties, use comma separated values. If this field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the field properties should be returned in the response body. If the field is left blank, the default field properties are returned. Example: 'True'.
            fieldLabel (string): The fieldLabel is the name of the field. Example: 'Priority'.
            fieldDescription (string): The description of the field. Example: 'Priority of the bug.'.
            enabled (boolean): This depicts if the field is enabled or not. Only those fields which are enabled will reflect in the account. Example: 'False'.
            private (boolean): This depicts if the field is private or not. Example: 'False'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Fields
        """
        if fieldId is None:
            raise ValueError("Missing required parameter 'fieldId'.")
        request_body_data = None
        request_body_data = {
            "fieldLabel": fieldLabel,
            "fieldDescription": fieldDescription,
            "enabled": enabled,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/fields/{fieldId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def delete_field(self, fieldId: str) -> Any:
        """
        Delete field by Id

        Args:
            fieldId (string): fieldId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Fields
        """
        if fieldId is None:
            raise ValueError("Missing required parameter 'fieldId'.")
        url = f"{self.base_url}/1.0/fields/{fieldId}"
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

    def get_all_timeoffs(
        self,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        startDate_gt: str | None = None,
        startDate_eq: str | None = None,
        startDate_lt: str | None = None,
        startDate_ge: str | None = None,
        startDate_le: str | None = None,
        endDate_gt: str | None = None,
        endDate_eq: str | None = None,
        endDate_lt: str | None = None,
        endDate_ge: str | None = None,
        endDate_le: str | None = None,
        type_eq: list[str] | None = None,
        type_oneOf: list[str] | None = None,
        type_noneOf: list[str] | None = None,
        userId_eq: str | None = None,
        userId_oneOf: str | None = None,
        userId_noneOf: str | None = None,
    ) -> dict[str, Any]:
        """
        Get all time-offs

        Args:
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            startDate_gt (string): Returns responses with start dates greater than the specified date. Example: '2023-03-28'.
            startDate_eq (string): Returns responses with start dates equal to the specified date. Example: '2023-03-28'.
            startDate_lt (string): Returns responses with start dates lesser than the specified date. Example: '2023-03-28'.
            startDate_ge (string): Returns responses with start dates greater than or equal to the specified date. Example: '2023-03-28'.
            startDate_le (string): Returns responses with start dates lesser than or equal to the specified date. Example: '2023-03-28'.
            endDate_gt (string): Returns responses with start dates greater than the specified date. Example: '2023-03-28'.
            endDate_eq (string): Returns responses with start dates equal to the specified date. Example: '2023-03-28'.
            endDate_lt (string): Returns responses with start dates lesser than the specified date. Example: '2023-03-28'.
            endDate_ge (string): Returns responses with start dates greater than or equal to the specified date. Example: '2023-03-28'.
            endDate_le (string): Returns responses with start dates lesser than or equal to the specified date.e. Example: '2023-03-28'.
            type_eq (array): Returns responses with time-offs that exactly match the specified time off type.
            type_oneOf (array): Returns responses with time-offs that matches one of the specified time off type.
            type_noneOf (array): Returns responses with time-offs that matches none of the specified time off type.
            userId_eq (string): Returns responses with time-offs that exactly match the specified user id. Example: '1'.
            userId_oneOf (string): Returns responses with time-offs that matches one of the specified user id. Example: '1,2,3'.
            userId_noneOf (string): Returns responses with time-offs that matches none of the specified user id. Example: '1,2'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time-Offs
        """
        url = f"{self.base_url}/1.0/time-offs"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("startDate.gt", startDate_gt),
                ("startDate.eq", startDate_eq),
                ("startDate.lt", startDate_lt),
                ("startDate.ge", startDate_ge),
                ("startDate.le", startDate_le),
                ("endDate.gt", endDate_gt),
                ("endDate.eq", endDate_eq),
                ("endDate.lt", endDate_lt),
                ("endDate.ge", endDate_ge),
                ("endDate.le", endDate_le),
                ("type.eq", type_eq),
                ("type.oneOf", type_oneOf),
                ("type.noneOf", type_noneOf),
                ("userId.eq", userId_eq),
                ("userId.oneOf", userId_oneOf),
                ("userId.noneOf", userId_noneOf),
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

    def create_timeoff(
        self,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        timeOffId: int | None = None,
        user: dict[str, Any] | None = None,
        note: str | None = None,
        startDate: str | None = None,
        endDate: str | None = None,
        type: str | None = None,
        notifyUsers: dict[str, Any] | None = None,
        durationInMinutes: int | None = None,
    ) -> dict[str, Any]:
        """
        Create a time-off

        Args:
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            timeOffId (integer): The unique `identifier` of the time-off is generated by the system and used to identify the time-off globally. Example: '201'.
            user (object): The time-off user.
            note (string): The note or comment about the time-off. Example: 'Sick leave.'.
            startDate (string): The time-off start date. The format for the start date is _YYYY-MM-DD_. Example: '2023-03-28'.
            endDate (string): The time-off end date. The `endDate` must be on or after the `startDate`, formatted as _YYYY-MM-DD_. Example: '2023-03-28'.
            type (string): The `type` of the time-off. Example: '50'.
            notifyUsers (object): Users to notify about your time off.
            durationInMinutes (integer): The duration of time off is determined by the type selected: if the time off type is `CUSTOM`, the `durationInMinutes` field is `required`. Example: '50'.

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time-Offs
        """
        request_body_data = None
        request_body_data = {
            "timeOffId": timeOffId,
            "user": user,
            "note": note,
            "startDate": startDate,
            "endDate": endDate,
            "type": type,
            "notifyUsers": notifyUsers,
            "durationInMinutes": durationInMinutes,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/time-offs"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def get_all_time_entries(
        self,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: list[str] | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        date_gt: str | None = None,
        date_eq: str | None = None,
        date_lt: str | None = None,
        date_ge: str | None = None,
        date_le: str | None = None,
        project_eq: float | None = None,
        projectId_eq: float | None = None,
        task_eq: float | None = None,
        taskId_eq: float | None = None,
        taskId_oneOf: float | None = None,
        taskId_noneOf: float | None = None,
        projectPhase_eq: float | None = None,
        category_eq: float | None = None,
        user_eq: float | None = None,
        sourceType_eq: str | None = None,
        activityName_eq: str | None = None,
        activityName_cn: str | None = None,
        activityName_nc: str | None = None,
        approvalStatus_eq: str | None = None,
        approvedBy_eq: float | None = None,
        approvedAt_eq: int | None = None,
        approvedAt_gt: int | None = None,
        approvedAt_ge: int | None = None,
        approvedAt_lt: int | None = None,
        approvedAt_le: int | None = None,
        billable_eq: bool | None = None,
        includeDeleted_eq: bool | None = None,
        createdAt_gt: int | None = None,
        createdAt_eq: int | None = None,
        createdAt_lt: int | None = None,
        createdAt_ge: int | None = None,
        createdAt_le: int | None = None,
        updatedAt_gt: int | None = None,
        updatedAt_eq: int | None = None,
        updatedAt_lt: int | None = None,
        updatedAt_ge: int | None = None,
        updatedAt_le: int | None = None,
    ) -> dict[str, Any]:
        """
        Get all time entries

        Args:
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            sortBy (string): You can use the sortBy param to sort the responses by the given field. Valid fields to perform sortBy are: `MINUTES`, `DATE`, `ID` and `BILLABLE`.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            date_gt (string): You can use this param to specify some date and the responses will contain time-entries whose date are greater than the given date. Example: '2023-03-28'.
            date_eq (string): You can use this param to specify some date and the responses will contain exact matches of time-entries that match the given date. Example: '2023-03-28'.
            date_lt (string): You can use this param to specify some date and the responses will contain time-entries whose date are less than the given date. Example: '2023-03-28'.
            date_ge (string): You can use this param to specify some date and the responses will contain time-entries whose date are greater than or equal to the given date. Example: '2023-03-28'.
            date_le (string): You can use this param to specify some date and the responses will contain time-entries whose date are less than or equal to the given date. Example: '2023-03-28'.
            project_eq (number): You can use this param to specify some project Id and the responses will contain exact matches of time-entries that match the given project. Example: '201'.
            projectId_eq (number): You can use this param to specify some project Id and the responses will contain exact matches of time-entries that match the given project. Example: '201'.
            task_eq (number): You can use this param to specify some task Id and the responses will contain exact matches of time-entries that match the given task. Example: '202'.
            taskId_eq (number): You can use this param to specify some task Id and the responses will contain exact matches of time-entries that match the given task. Example: '202'.
            taskId_oneOf (number): You can use this param to provide ids of task and the responses will contain time entries whose time entries that contains the given task ids Example: '202'.
            taskId_noneOf (number): You can use this param to provide ids of task and the responses will contain time entries whose time entries that contains the given task ids Example: '202'.
            projectPhase_eq (number): You can use this param to specify some project phase Id and the responses will contain exact matches of time-entries that match the given phase. Example: '210'.
            category_eq (number): You can use this param to specify some category Id and the responses will contain exact matches of time-entries that match the given category. Example: '5'.
            user_eq (number): You can use this param to specify some user Id and the responses will contain exact matches of time-entries that belong to the user with the given user Id. Example: '5'.
            sourceType_eq (string): You can use this param to specify a source type for the time entries and the responses will contain exact matches of time-entries that have the given source type.
            activityName_eq (string): You can use this param to specify some activity name and the responses will contain exact matches of time-entries that match the given activity name. Example: 'Pre-Sales Campaign'.
            activityName_cn (string): You can use this param to specify some text and the responses will contain time-entries that contain the given text in their activity name. Example: 'Sales'.
            activityName_nc (string): You can use this param to specify some text and the responses will contain time-entries that _DO NOT_ contain the given text in their activity name. Example: 'Sales'.
            approvalStatus_eq (string): You can use this param to specify an approval status for the time entries and the responses will contain exact matches of time-entries that have the given approval type.
            approvedBy_eq (number): You can use this param to specify an approver for the time entries and the response will contain time-entries approved by the given user. Example: '5'.
            approvedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain time entries approved at the given timestamp. Example: '1625164800000'.
            approvedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain time entries approved after the given timestamp. Example: '1625164800000'.
            approvedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain time entries approved at or after the given timestamp. Example: '1625164800000'.
            approvedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain time entries approved before the given timestamp. Example: '1625164800000'.
            approvedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain time entries approved at or before the given timestamp. Example: '1625164800000'.
            billable_eq (boolean): You can use this param to specify the billable flag for the time entries and the responses will contain exact matches of time-entries that have the given billable. Example: 'True'.
            includeDeleted_eq (boolean): You can use this parameter to specify whether responses will include the deleted time entries. Example: 'False'.
            createdAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain time entries whose date are greater than the given time entries created date. Example: '1625164800000'.
            createdAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of time entries that match the given time entries created date. Example: '1625164800000'.
            createdAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain time entries whose date are less than the given time entries created date. Example: '1625164800000'.
            createdAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain time entries whose date are greater than or equal to the given time entries created date. Example: '1625164800000'.
            createdAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain time entries whose date are less than or equal to the given time entries created date. Example: '1625164800000'.
            updatedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain time entries whose date are greater than the given time entries updated date. Example: '1625164800000'.
            updatedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of time entries that match the given time entries updated date. Example: '1625164800000'.
            updatedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain time entries whose date are less than the given time entries updated date. Example: '1625164800000'.
            updatedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain time entries whose date are greater than or equal to the given time entries updated date. Example: '1625164800000'.
            updatedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain time entries whose date are less than or equal to the given time entries updated date. Example: '1625164800000'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time Tracking
        """
        url = f"{self.base_url}/1.0/time-entries"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("date.gt", date_gt),
                ("date.eq", date_eq),
                ("date.lt", date_lt),
                ("date.ge", date_ge),
                ("date.le", date_le),
                ("project.eq", project_eq),
                ("projectId.eq", projectId_eq),
                ("task.eq", task_eq),
                ("taskId.eq", taskId_eq),
                ("taskId.oneOf", taskId_oneOf),
                ("taskId.noneOf", taskId_noneOf),
                ("projectPhase.eq", projectPhase_eq),
                ("category.eq", category_eq),
                ("user.eq", user_eq),
                ("sourceType.eq", sourceType_eq),
                ("activityName.eq", activityName_eq),
                ("activityName.cn", activityName_cn),
                ("activityName.nc", activityName_nc),
                ("approvalStatus.eq", approvalStatus_eq),
                ("approvedBy.eq", approvedBy_eq),
                ("approvedAt.eq", approvedAt_eq),
                ("approvedAt.gt", approvedAt_gt),
                ("approvedAt.ge", approvedAt_ge),
                ("approvedAt.lt", approvedAt_lt),
                ("approvedAt.le", approvedAt_le),
                ("billable.eq", billable_eq),
                ("includeDeleted.eq", includeDeleted_eq),
                ("createdAt.gt", createdAt_gt),
                ("createdAt.eq", createdAt_eq),
                ("createdAt.lt", createdAt_lt),
                ("createdAt.ge", createdAt_ge),
                ("createdAt.le", createdAt_le),
                ("updatedAt.gt", updatedAt_gt),
                ("updatedAt.eq", updatedAt_eq),
                ("updatedAt.lt", updatedAt_lt),
                ("updatedAt.ge", updatedAt_ge),
                ("updatedAt.le", updatedAt_le),
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

    def create_time_entry(
        self,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        timeEntryId: int | None = None,
        date: str | None = None,
        minutes: int | None = None,
        activityName: str | None = None,
        project: dict[str, Any] | None = None,
        task: dict[str, Any] | None = None,
        projectPhase: dict[str, Any] | None = None,
        billable: bool | None = None,
        user: dict[str, Any] | None = None,
        notes: str | None = None,
        category: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create a time entry

        Args:
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            timeEntryId (integer): The unique, system-generated identifier, which can be used to identify the time entry globally. Example: '201'.
            date (string): Date of the time entry in format YYYY-MM-DD Example: '2023-03-28'.
            minutes (integer): Duration of the time entry in minutes Example: '250'.
            activityName (string): Name of the adhoc activity being performed Example: 'Pre-Sales campaign'.
            project (object): Project associated with the time entry
            task (object): Task associated with the time entry
            projectPhase (object): Project phase associated with the time entry
            billable (boolean): Whether the time entry is billable. Defaults to true Example: 'True'.
            user (object): User associated with the time entry
            notes (string): Notes for the time entry Example: 'Working on API integration'.
            category (object): Category associated with the time entry

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time Tracking
        """
        request_body_data = None
        request_body_data = {
            "timeEntryId": timeEntryId,
            "date": date,
            "minutes": minutes,
            "activityName": activityName,
            "project": project,
            "task": task,
            "projectPhase": projectPhase,
            "billable": billable,
            "user": user,
            "notes": notes,
            "category": category,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/time-entries"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def remove_followers_from_task(
        self, taskId: str, members: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Remove followers from a task by Id

        Args:
            taskId (string): taskId
            members (array): The list includes both `team members` and `customers` assigned to the task.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        request_body_data = None
        request_body_data = {
            "members": members,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks/{taskId}/remove-followers"
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

    def remove_dependencies_from_task(
        self, taskId: str, dependencies: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Remove dependencies from a task by Id

        Args:
            taskId (string): taskId
            dependencies (array): Task Dependencies allow you to define relationships between tasks that are dependent on each other. Example: '201'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        request_body_data = None
        request_body_data = {
            "dependencies": dependencies,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks/{taskId}/remove-dependencies"
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

    def remove_assignees_from_task(
        self,
        taskId: str,
        members: list[dict[str, Any]] | None = None,
        placeholders: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Remove assignees from a task by Id

        Args:
            taskId (string): taskId
            members (array): The list includes both `team members` and `customers` assigned to the task.
            placeholders (array):  Rocketlane’s placeholders are associated with roles.  Based on the kind of roles and expertise that are needed to execute a task, placeholders can be added as assignees to templates as well as projects. Eventually, you can resolve placeholders by replacing them with team members according to their availability and role.
        Note: If the project is not built using sources, this value will be ignored but the mappings are retained and can be used in the future

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        request_body_data = None
        request_body_data = {
            "members": members,
            "placeholders": placeholders,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks/{taskId}/remove-assignees"
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

    def move_task_to_given_phase(
        self, taskId: str, phase: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Move a task to the phase by Id

        Args:
            taskId (string): taskId
            phase (object): The phase to which the task will be moved, associating the task with this phase.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        request_body_data = None
        request_body_data = {
            "phase": phase,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks/{taskId}/move-phase"
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

    def add_followers_to_task(
        self, taskId: str, members: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Add followers to a task by Id

        Args:
            taskId (string): taskId
            members (array): The list includes both `team members` and `customers` assigned to the task.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        request_body_data = None
        request_body_data = {
            "members": members,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks/{taskId}/add-followers"
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

    def add_dependencies_to_task(
        self, taskId: str, dependencies: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Add dependencies to a task by Id

        Args:
            taskId (string): taskId
            dependencies (array): Task Dependencies allow you to define relationships between tasks that are dependent on each other. Example: '201'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        request_body_data = None
        request_body_data = {
            "dependencies": dependencies,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks/{taskId}/add-dependencies"
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

    def add_assignee_to_task(
        self,
        taskId: str,
        members: list[dict[str, Any]] | None = None,
        placeholders: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Add assignees to a task by Id

        Args:
            taskId (string): taskId
            members (array): The list includes both `team members` and `customers` assigned to the task.
            placeholders (array):  Rocketlane’s placeholders are associated with roles.  Based on the kind of roles and expertise that are needed to execute a task, placeholders can be added as assignees to templates as well as projects. Eventually, you can resolve placeholders by replacing them with team members according to their availability and role.
        Note: If the project is not built using sources, this value will be ignored but the mappings are retained and can be used in the future

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'.")
        request_body_data = None
        request_body_data = {
            "members": members,
            "placeholders": placeholders,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks/{taskId}/add-assignees"
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

    def get_all_tasks(
        self,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        startDate_gt: str | None = None,
        startDate_eq: str | None = None,
        startDate_lt: str | None = None,
        startDate_ge: str | None = None,
        startDate_le: str | None = None,
        dueDate_gt: str | None = None,
        dueDate_eq: str | None = None,
        dueDate_lt: str | None = None,
        dueDate_ge: str | None = None,
        dueDate_le: str | None = None,
        startDateActual_gt: str | None = None,
        startDateActual_eq: str | None = None,
        startDateActual_lt: str | None = None,
        startDateActual_ge: str | None = None,
        startDateActual_le: str | None = None,
        dueDateActual_gt: str | None = None,
        dueDateActual_eq: str | None = None,
        dueDateActual_lt: str | None = None,
        dueDateActual_ge: str | None = None,
        dueDateActual_le: str | None = None,
        createdAt_gt: int | None = None,
        createdAt_eq: int | None = None,
        createdAt_lt: int | None = None,
        createdAt_ge: int | None = None,
        createdAt_le: int | None = None,
        updatedAt_gt: int | None = None,
        updatedAt_eq: int | None = None,
        updatedAt_lt: int | None = None,
        updatedAt_ge: int | None = None,
        updatedAt_le: int | None = None,
        projectId_eq: float | None = None,
        phaseId_eq: float | None = None,
        taskName_eq: str | None = None,
        taskName_cn: str | None = None,
        taskName_nc: str | None = None,
        effortInMinutes_eq: float | None = None,
        effortInMinutes_gt: float | None = None,
        effortInMinutes_lt: float | None = None,
        progress_eq: float | None = None,
        progress_gt: float | None = None,
        progress_lt: float | None = None,
        includeArchive_eq: bool | None = None,
        task_status_eq: str | None = None,
        task_status_oneOf: str | None = None,
        task_status_noneOf: str | None = None,
        project_status_eq: str | None = None,
        project_status_oneOf: str | None = None,
        project_status_noneOf: str | None = None,
        externalReferenceId_eq: str | None = None,
    ) -> dict[str, Any]:
        """
        Get all tasks

        Args:
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            startDate_gt (string): You can use this param to specify some date and the responses will contain tasks whose date are greater than the given date. Example: '2023-03-28'.
            startDate_eq (string): You can use this param to specify some date and the responses will contain exact matches of tasks that match the given date. Example: '2023-03-28'.
            startDate_lt (string): You can use this param to specify some date and the responses will contain tasks whose date are less than the given date. Example: '2023-03-28'.
            startDate_ge (string): You can use this param to specify some date and the responses will contain tasks whose date are greater than or equal to the given date. Example: '2023-03-28'.
            startDate_le (string): You can use this param to specify some date and the responses will contain tasks whose date are less than or equal to the given date. Example: '2023-03-28'.
            dueDate_gt (string): You can use this param to specify some date and the responses will contain tasks whose date are greater than the given date. Example: '2023-03-28'.
            dueDate_eq (string): You can use this param to specify some date and the responses will contain exact matches of tasks that match the given date. Example: '2023-03-28'.
            dueDate_lt (string): You can use this param to specify some date and the responses will contain tasks whose date are less than the given date. Example: '2023-03-28'.
            dueDate_ge (string): You can use this param to specify some date and the responses will contain tasks whose date are greater than or equal to the given date. Example: '2023-03-28'.
            dueDate_le (string): You can use this param to specify some date and the responses will contain tasks whose date are less than or equal to the given date. Example: '2023-03-28'.
            startDateActual_gt (string): You can use this param to specify some date and the responses will contain tasks whose date are greater than the given date. Example: '2023-03-28'.
            startDateActual_eq (string): You can use this param to specify some date and the responses will contain exact matches of tasks that match the given date. Example: '2023-03-28'.
            startDateActual_lt (string): You can use this param to specify some date and the responses will contain tasks whose date are less than the given date. Example: '2023-03-28'.
            startDateActual_ge (string): You can use this param to specify some date and the responses will contain tasks whose date are greater than or equal to the given date. Example: '2023-03-28'.
            startDateActual_le (string): You can use this param to specify some date and the responses will contain tasks whose date are less than or equal to the given date. Example: '2023-03-28'.
            dueDateActual_gt (string): You can use this param to specify some date and the responses will contain tasks whose date are greater than the given date. Example: '2023-03-28'.
            dueDateActual_eq (string): You can use this param to specify some date and the responses will contain exact matches of tasks that match the given date. Example: '2023-03-28'.
            dueDateActual_lt (string): You can use this param to specify some date and the responses will contain tasks whose date are less than the given date. Example: '2023-03-28'.
            dueDateActual_ge (string): You can use this param to specify some date and the responses will contain tasks whose date are greater than or equal to the given date. Example: '2023-03-28'.
            dueDateActual_le (string): You can use this param to specify some date and the responses will contain tasks whose date are less than or equal to the given date. Example: '2023-03-28'.
            createdAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain tasks whose date are greater than the given tasks created date. Example: '1625164800000'.
            createdAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of tasks that match the given tasks created date. Example: '1625164800000'.
            createdAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain tasks whose date are less than the given tasks created date. Example: '1625164800000'.
            createdAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain tasks whose date are greater than or equal to the given tasks created date. Example: '1625164800000'.
            createdAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain tasks whose date are less than or equal to the given tasks created date. Example: '1625164800000'.
            updatedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain tasks whose date are greater than the given tasks updated date. Example: '1625164800000'.
            updatedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of tasks that match the given tasks updated date. Example: '1625164800000'.
            updatedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain tasks whose date are less than the given tasks updated date. Example: '1625164800000'.
            updatedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain tasks whose date are greater than or equal to the given tasks updated date. Example: '1625164800000'.
            updatedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain tasks whose date are less than or equal to the given tasks updated date. Example: '1625164800000'.
            projectId_eq (number): You can use this param to specify some value as project id and the responses will contain exact matches of tasks that match the given value. Example: '10000'.
            phaseId_eq (number): You can use this param to specify some value as phase id and the responses will contain exact matches of tasks that match the given value. Example: '10000'.
            taskName_eq (string): You can use this param to specify some task name and the responses will contain exact matches of tasks that match the given name. Example: 'Stark Onboarding'.
            taskName_cn (string): You can use this param to specify some task name and the responses will contain matches of tasks that match the given name. Example: 'Stark Onboarding'.
            taskName_nc (string): You can use this param to specify some task name and the responses will not contain matches of tasks that match the given name. Example: 'Stark Onboarding'.
            effortInMinutes_eq (number): You can use this param to specify some value as effort and the responses will contain exact matches of tasks that match the given value. Example: '10000'.
            effortInMinutes_gt (number): You can use this param to specify some value as effort and the responses will contain exact matches of tasks greater than that of the given value. Example: '10000'.
            effortInMinutes_lt (number): You can use this param to specify some value as effort and the responses will contain exact matches of tasks lesser than that of the given value. Example: '10000'.
            progress_eq (number): You can use this param to specify some value as progress and the responses will contain exact matches of tasks that match the given value. Example: '55'.
            progress_gt (number): You can use this param to specify some value as progress and the responses will contain exact matches of tasks greater than that of the given value. Example: '55'.
            progress_lt (number): You can use this param to specify some value as progress and the responses will contain exact matches of tasks lesser than that of the given value. Example: '55'.
            includeArchive_eq (boolean): You can use this parameter to specify whether responses will include the archived tasks. Example: 'False'.
            task_status_eq (string): You can use this param to provide status and the responses will contain tasks that are equal to the given status Example: '1'.
            task_status_oneOf (string): You can use this param to provide statuses and the responses will contain tasks that  contains the given status Example: '1,2'.
            task_status_noneOf (string): You can use this param to provide statuses and the responses will not contain tasks that are equal to the given status Example: '1,2'.
            project_status_eq (string): You can use this param to provide status of project and the responses will contain tasks whose project's status are equal to the given status Example: '1'.
            project_status_oneOf (string): You can use this param to provide statuses of project and the responses will contain tasks whose project's statuses that contains the given status Example: '1,2'.
            project_status_noneOf (string): You can use this param to provide statuses of project and the responses will not contain tasks whose project's statuses are equal to the given status(es) Example: '1,2'.
            externalReferenceId_eq (string): You can use this param to provide external reference id and the responses will contain tasks that are equal to the given id Example: 'task_1818910101'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        url = f"{self.base_url}/1.0/tasks"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("startDate.gt", startDate_gt),
                ("startDate.eq", startDate_eq),
                ("startDate.lt", startDate_lt),
                ("startDate.ge", startDate_ge),
                ("startDate.le", startDate_le),
                ("dueDate.gt", dueDate_gt),
                ("dueDate.eq", dueDate_eq),
                ("dueDate.lt", dueDate_lt),
                ("dueDate.ge", dueDate_ge),
                ("dueDate.le", dueDate_le),
                ("startDateActual.gt", startDateActual_gt),
                ("startDateActual.eq", startDateActual_eq),
                ("startDateActual.lt", startDateActual_lt),
                ("startDateActual.ge", startDateActual_ge),
                ("startDateActual.le", startDateActual_le),
                ("dueDateActual.gt", dueDateActual_gt),
                ("dueDateActual.eq", dueDateActual_eq),
                ("dueDateActual.lt", dueDateActual_lt),
                ("dueDateActual.ge", dueDateActual_ge),
                ("dueDateActual.le", dueDateActual_le),
                ("createdAt.gt", createdAt_gt),
                ("createdAt.eq", createdAt_eq),
                ("createdAt.lt", createdAt_lt),
                ("createdAt.ge", createdAt_ge),
                ("createdAt.le", createdAt_le),
                ("updatedAt.gt", updatedAt_gt),
                ("updatedAt.eq", updatedAt_eq),
                ("updatedAt.lt", updatedAt_lt),
                ("updatedAt.ge", updatedAt_ge),
                ("updatedAt.le", updatedAt_le),
                ("projectId.eq", projectId_eq),
                ("phaseId.eq", phaseId_eq),
                ("taskName.eq", taskName_eq),
                ("taskName.cn", taskName_cn),
                ("taskName.nc", taskName_nc),
                ("effortInMinutes.eq", effortInMinutes_eq),
                ("effortInMinutes.gt", effortInMinutes_gt),
                ("effortInMinutes.lt", effortInMinutes_lt),
                ("progress.eq", progress_eq),
                ("progress.gt", progress_gt),
                ("progress.lt", progress_lt),
                ("includeArchive.eq", includeArchive_eq),
                ("task.status.eq", task_status_eq),
                ("task.status.oneOf", task_status_oneOf),
                ("task.status.noneOf", task_status_noneOf),
                ("project.status.eq", project_status_eq),
                ("project.status.oneOf", project_status_oneOf),
                ("project.status.noneOf", project_status_noneOf),
                ("externalReferenceId.eq", externalReferenceId_eq),
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

    def create_task(
        self,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        taskId: int | None = None,
        taskName: str | None = None,
        taskDescription: str | None = None,
        taskPrivateNote: str | None = None,
        startDate: str | None = None,
        dueDate: str | None = None,
        effortInMinutes: int | None = None,
        progress: int | None = None,
        atRisk: bool | None = None,
        type: str | None = None,
        project: dict[str, Any] | None = None,
        phase: dict[str, Any] | None = None,
        status: dict[str, Any] | None = None,
        fields: list[dict[str, Any]] | None = None,
        assignees: dict[str, Any] | None = None,
        followers: dict[str, Any] | None = None,
        parent: dict[str, Any] | None = None,
        externalReferenceId: str | None = None,
        private: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create a task

        Args:
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            taskId (integer): The task’s unique, system-generated **identifier**, which can be used to identify the task globally Example: '201'.
            taskName (string): The **name** of the task. Example: 'Kick off'.
            taskDescription (string): The `description` of the task. The description body needs to be in **html** format to avoid any formatting issues in the application. Example: '<p>Schedule Kick off meeting with the stakeholders involved.</p>'.
            taskPrivateNote (string): The `privateNote` for the task is intended exclusively for team members. The note's content should be in `HTML` format to prevent any formatting issues in the application. Example: '<p>Schedule Kick off meeting with the stakeholders involved.</p>'.
            startDate (string): The date when a task starts its execution. It can be empty. The format for the start date is _YYYY-MM-DD_. Example: '2023-03-28'.
            dueDate (string): The date when a task completes its execution. It can be empty. If both `startDate` and `dueDate` are specified for a given task, it is necessary that the latter should be on or after the given `startDate`. The format for the due date is _YYYY-MM-DD_. Example: '2023-03-28'.
            effortInMinutes (integer): The effort is the expected time required to complete the task. The value is determined in minutes. Example: '3000'.
            progress (integer): The task’s progress, if indicated, will be available here and ranges in value from 0 to 100. The task’s status can be used in place of this field, however progress can offer more precise data. Example: '50'.
            atRisk (boolean): Indicates whether the task has been marked as At Risk. This parameter is used to indicate that immediate action is necessary to unblock the task’s execution. Example: 'True'.
            type (string): The type of the task if specified will be available here. There are two options: `MILESTONE` or `TASK`. If a task is not explicitly marked as a milestone, it takes the default value as `TASK`. Milestones refer to critical tasks in the project that include an inbuilt CSAT capability that allows customers to offer CSAT evaluations depending on the task’s execution. Example: 'MILESTONE'.
            project (object): The `project` associated with task needs to be specified here and it is mandatory for the task to get created and map accordingly.
            phase (object): The `phase` that needs to be associated with the task can be mentioned here. Note: The `phase` needs to be associated with the `project` and thus failing the task creation process.
            status (object): The value of the task status can be specified here and this is essential to keep track of it.
            fields (array): The custom fields can be set during the task creation with the help of `fields`. The `fieldValue` can be either a string or a number or an array and it has to comply with the type of the field. Refer [examples](https://developer.rocketlane.com/v1.0/docs/custom-fields#examples-of-requests-and-responses-for-assigning-custom-field-values) to know how to assign `fieldValue` based on their `field_type`.
            assignees (object): assignees
            followers (object): The task followers can be either `members` (team members or customers) or `placeholders`.
            parent (object): Parent task id Example: '201'.
            externalReferenceId (string): An externalReferenceId is a unique identifier that links entities or transactions between external systems and Rocketlane, ensuring accurate data correlation and consistency. Example: 'task_8171'.
            private (boolean): This depicts if the task is private or not. Example: 'False'.

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        request_body_data = None
        request_body_data = {
            "taskId": taskId,
            "taskName": taskName,
            "taskDescription": taskDescription,
            "taskPrivateNote": taskPrivateNote,
            "startDate": startDate,
            "dueDate": dueDate,
            "effortInMinutes": effortInMinutes,
            "progress": progress,
            "atRisk": atRisk,
            "type": type,
            "project": project,
            "phase": phase,
            "status": status,
            "fields": fields,
            "assignees": assignees,
            "followers": followers,
            "parent": parent,
            "externalReferenceId": externalReferenceId,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/tasks"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def get_all_spaces(
        self,
        projectId: int,
        pageSize: float | None = None,
        pageToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        spaceName_eq: str | None = None,
        spaceName_cn: str | None = None,
        spaceName_nc: str | None = None,
        createdAt_gt: int | None = None,
        createdAt_eq: int | None = None,
        createdAt_lt: int | None = None,
        createdAt_ge: int | None = None,
        createdAt_le: int | None = None,
        updatedAt_gt: int | None = None,
        updatedAt_eq: int | None = None,
        updatedAt_lt: int | None = None,
        updatedAt_ge: int | None = None,
        updatedAt_le: int | None = None,
    ) -> dict[str, Any]:
        """
        Get all spaces

        Args:
            projectId (integer): You can use this param to specify some value as project id and the responses will contain exact matches of spaces that match the given value. Example: '200'.
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            spaceName_eq (string): You can use this param to specify some space name and the responses will contain exact matches of spaces that match the given name. Example: 'Stark Onboarding'.
            spaceName_cn (string): You can use this param to specify some space name and the responses will contain matches of spaces that match the given name. Example: 'Stark Onboarding'.
            spaceName_nc (string): You can use this param to specify some space name and the responses will not contain matches of spaces that match the given name. Example: 'Stark Onboarding'.
            createdAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain spaces whose date are greater than the given spaces created date. Example: '1625164800000'.
            createdAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of spaces that match the given spaces created date. Example: '1625164800000'.
            createdAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain spaces whose date are less than the given spaces created date. Example: '1625164800000'.
            createdAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain spaces whose date are greater than or equal to the given spaces created date. Example: '1625164800000'.
            createdAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain spaces whose date are less than or equal to the given spaces created date. Example: '1625164800000'.
            updatedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain spaces whose date are greater than the given spaces updated date. Example: '1625164800000'.
            updatedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of spaces that match the given spaces updated date. Example: '1625164800000'.
            updatedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain spaces whose date are less than the given spaces updated date. Example: '1625164800000'.
            updatedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain spaces whose date are greater than or equal to the given spaces updated date. Example: '1625164800000'.
            updatedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain spaces whose date are less than or equal to the given spaces updated date. Example: '1625164800000'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        url = f"{self.base_url}/1.0/spaces"
        query_params = {
            k: v
            for k, v in [
                ("projectId", projectId),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("spaceName.eq", spaceName_eq),
                ("spaceName.cn", spaceName_cn),
                ("spaceName.nc", spaceName_nc),
                ("createdAt.gt", createdAt_gt),
                ("createdAt.eq", createdAt_eq),
                ("createdAt.lt", createdAt_lt),
                ("createdAt.ge", createdAt_ge),
                ("createdAt.le", createdAt_le),
                ("updatedAt.gt", updatedAt_gt),
                ("updatedAt.eq", updatedAt_eq),
                ("updatedAt.lt", updatedAt_lt),
                ("updatedAt.ge", updatedAt_ge),
                ("updatedAt.le", updatedAt_le),
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

    def create_space(
        self,
        spaceId: int | None = None,
        spaceName: str | None = None,
        project: dict[str, Any] | None = None,
        private: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create a space

        Args:
            spaceId (integer): The space’s unique, system-generated identifier, which can be used to identify the space globally. Example: '201'.
            spaceName (string): The name of the space. Example: 'Shared space'.
            project (object): The `project` where the `space` exists.
            private (boolean): Describes the privacy of the space i.e. if it is private or shared. Example: 'True'.

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        request_body_data = None
        request_body_data = {
            "spaceId": spaceId,
            "spaceName": spaceName,
            "project": project,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/spaces"
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

    def get_all_space_documents(
        self,
        projectId: int,
        pageSize: float | None = None,
        pageToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        spaceDocumentName_eq: str | None = None,
        spaceDocumentName_cn: str | None = None,
        spaceDocumentName_nc: str | None = None,
        createdAt_gt: int | None = None,
        createdAt_eq: int | None = None,
        createdAt_lt: int | None = None,
        createdAt_ge: int | None = None,
        createdAt_le: int | None = None,
        updatedAt_gt: int | None = None,
        updatedAt_eq: int | None = None,
        updatedAt_lt: int | None = None,
        updatedAt_ge: int | None = None,
        updatedAt_le: int | None = None,
        spaceId_eq: float | None = None,
    ) -> dict[str, Any]:
        """
        Get all space documents

        Args:
            projectId (integer): You can use this param to specify some value as project id and the responses will contain exact matches of space documents that match the given value. Example: '200'.
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            spaceDocumentName_eq (string): You can use this param to specify some space document name and the responses will contain exact matches of space documents that match the given name. Example: 'Stark Onboarding'.
            spaceDocumentName_cn (string): You can use this param to specify some space document name and the responses will contain matches of space documents that match the given name. Example: 'Stark Onboarding'.
            spaceDocumentName_nc (string): You can use this param to specify some space document name and the responses will not contain matches of space documents that match the given name. Example: 'Stark Onboarding'.
            createdAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain space documents whose date are greater than the given space documents created date. Example: '1625164800000'.
            createdAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of space documents that match the given space documents created date. Example: '1625164800000'.
            createdAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain space documents whose date are less than the given space documents created date. Example: '1625164800000'.
            createdAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain space documents whose date are greater than or equal to the given space documents created date. Example: '1625164800000'.
            createdAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain space documents whose date are less than or equal to the given space documents created date. Example: '1625164800000'.
            updatedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain space documents whose date are greater than the given space documents updated date. Example: '1625164800000'.
            updatedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of space documents that match the given space documents updated date. Example: '1625164800000'.
            updatedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain space documents whose date are less than the given space documents updated date. Example: '1625164800000'.
            updatedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain space documents whose date are greater than or equal to the given space documents updated date. Example: '1625164800000'.
            updatedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain space documents whose date are less than or equal to the given space documents updated date. Example: '1625164800000'.
            spaceId_eq (number): You can use this param to specify some value as space id and the responses will contain exact matches of space documents that match the given value. Example: '10000'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Space Documents
        """
        url = f"{self.base_url}/1.0/space-documents"
        query_params = {
            k: v
            for k, v in [
                ("projectId", projectId),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("spaceDocumentName.eq", spaceDocumentName_eq),
                ("spaceDocumentName.cn", spaceDocumentName_cn),
                ("spaceDocumentName.nc", spaceDocumentName_nc),
                ("createdAt.gt", createdAt_gt),
                ("createdAt.eq", createdAt_eq),
                ("createdAt.lt", createdAt_lt),
                ("createdAt.ge", createdAt_ge),
                ("createdAt.le", createdAt_le),
                ("updatedAt.gt", updatedAt_gt),
                ("updatedAt.eq", updatedAt_eq),
                ("updatedAt.lt", updatedAt_lt),
                ("updatedAt.ge", updatedAt_ge),
                ("updatedAt.le", updatedAt_le),
                ("spaceId.eq", spaceId_eq),
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

    def create_space_document(
        self,
        spaceDocumentId: int | None = None,
        spaceDocumentName: str | None = None,
        space: dict[str, Any] | None = None,
        spaceDocumentType: str | None = None,
        url: str | None = None,
        source: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create a space document

        Args:
            spaceDocumentId (integer): The space document’s unique, system-generated identifier, which can be used to identify the space document globally. Example: '201'.
            spaceDocumentName (string): The name of the space document.By default, the name is 'Untitled'. Example: 'Sample file'.
            space (object): Information about the space to which the space document belongs to.
            spaceDocumentType (string): Defines the type of the space document. This could be a Rocketlane document or an embedded document. Example: 'ROCKETLANE_DOCUMENT'.
            url (string): The url that is embedded in the space document. Example: 'https://www.google.com'.
            source (object): Sources denote the document templates based on which the document is created

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Space Documents
        """
        request_body_data = None
        request_body_data = {
            "spaceDocumentId": spaceDocumentId,
            "spaceDocumentName": spaceDocumentName,
            "space": space,
            "spaceDocumentType": spaceDocumentType,
            "url": url,
            "source": source,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/space-documents"
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

    def unassign_placeholders(
        self, projectId: str, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Un assign placeholders from an user in a project

        Args:
            projectId (string): projectId

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/1.0/projects/{projectId}/unassign-placeholders"
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

    def remove_members(
        self, projectId: str, members: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Remove members from a project

        Args:
            projectId (string): projectId
            members (array): The team members from your organization working on the project.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        request_body_data = None
        request_body_data = {
            "members": members,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/projects/{projectId}/remove-members"
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

    def import_template(
        self, projectId: str, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Import a template to a project

        Args:
            projectId (string): projectId

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/1.0/projects/{projectId}/import-template"
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

    def assign_placeholders(
        self, projectId: str, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Assign placeholders to an user in a project

        Args:
            projectId (string): projectId

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/1.0/projects/{projectId}/assign-placeholders"
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

    def archive_project(self, projectId: str) -> Any:
        """
        Archive project by Id

        Args:
            projectId (string): projectId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        request_body_data = None
        url = f"{self.base_url}/1.0/projects/{projectId}/archive"
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

    def add_members(
        self,
        projectId: str,
        members: list[dict[str, Any]] | None = None,
        customers: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Add members to a project

        Args:
            projectId (string): projectId
            members (array): The project team members.
            customers (array): The project customers.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects, important
        """
        if projectId is None:
            raise ValueError("Missing required parameter 'projectId'.")
        request_body_data = None
        request_body_data = {
            "members": members,
            "customers": customers,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/projects/{projectId}/add-members"
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

    def get_all_projects(
        self,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        startDate_gt: str | None = None,
        startDate_eq: str | None = None,
        startDate_lt: str | None = None,
        startDate_ge: str | None = None,
        startDate_le: str | None = None,
        dueDate_gt: str | None = None,
        dueDate_eq: str | None = None,
        dueDate_lt: str | None = None,
        dueDate_ge: str | None = None,
        dueDate_le: str | None = None,
        startDateActual_gt: str | None = None,
        startDateActual_eq: str | None = None,
        startDateActual_lt: str | None = None,
        startDateActual_ge: str | None = None,
        startDateActual_le: str | None = None,
        dueDateActual_gt: str | None = None,
        dueDateActual_eq: str | None = None,
        dueDateActual_lt: str | None = None,
        dueDateActual_ge: str | None = None,
        dueDateActual_le: str | None = None,
        createdAt_gt: int | None = None,
        createdAt_eq: int | None = None,
        createdAt_lt: int | None = None,
        createdAt_ge: int | None = None,
        createdAt_le: int | None = None,
        updatedAt_gt: int | None = None,
        updatedAt_eq: int | None = None,
        updatedAt_lt: int | None = None,
        updatedAt_ge: int | None = None,
        updatedAt_le: int | None = None,
        annualizedRecurringRevenue_eq: float | None = None,
        annualizedRecurringRevenue_gt: float | None = None,
        annualizedRecurringRevenue_lt: float | None = None,
        projectFee_eq: float | None = None,
        projectFee_gt: float | None = None,
        projectFee_lt: float | None = None,
        customerId_eq: str | None = None,
        customerId_oneOf: str | None = None,
        customerId_noneOf: str | None = None,
        teamMemberId_eq: str | None = None,
        teamMemberId_oneOf: str | None = None,
        teamMemberId_noneOf: str | None = None,
        companyId_eq: str | None = None,
        companyId_oneOf: str | None = None,
        companyId_noneOf: str | None = None,
        projectName_eq: str | None = None,
        projectName_cn: str | None = None,
        projectName_nc: str | None = None,
        inferredProgress_eq: list[str] | None = None,
        contractType_eq: list[str] | None = None,
        contractType_oneOf: list[str] | None = None,
        contractType_noneOf: list[str] | None = None,
        budgetedHours_gt: str | None = None,
        budgetedHours_eq: str | None = None,
        budgetedHours_lt: str | None = None,
        budgetedHours_ge: str | None = None,
        allocatedHours_le: str | None = None,
        allocatedHours_gt: str | None = None,
        allocatedHours_eq: str | None = None,
        allocatedHours_lt: str | None = None,
        allocatedHours_ge: str | None = None,
        customersInvited_gt: str | None = None,
        customersInvited_eq: str | None = None,
        customersInvited_lt: str | None = None,
        customersInvited_ge: str | None = None,
        customersInvited_le: str | None = None,
        customersJoined_gt: str | None = None,
        customersJoined_eq: str | None = None,
        customersJoined_lt: str | None = None,
        customersJoined_ge: str | None = None,
        customersJoined_le: str | None = None,
        includeArchive_eq: bool | None = None,
        status_eq: str | None = None,
        status_oneOf: str | None = None,
        status_noneOf: str | None = None,
        externalReferenceId_eq: str | None = None,
    ) -> dict[str, Any]:
        """
        Get all projects

        Args:
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            sortBy (string): For sorting the responses by the provided field, use the sortBy parameter.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            startDate_gt (string): You can use this param to provide a date and the responses will contain projects whose date are greater than the given start date. Example: '2023-03-28'.
            startDate_eq (string): You can use this param to provide a date and the responses will contain exact matches of projects that match the given start date. Example: '2023-03-28'.
            startDate_lt (string): You can use this param to provide a date and the responses will contain projects whose date are less than the given start date. Example: '2023-03-28'.
            startDate_ge (string): You can use this param to provide a date and the responses will contain projects whose date are greater than or equal to the given start date. Example: '2023-03-28'.
            startDate_le (string): You can use this param to provide a date and the responses will contain projects whose date are less than or equal to the given start date. Example: '2023-03-28'.
            dueDate_gt (string): You can use this param to provide a date and the responses will contain projects whose date are greater than the given due date. Example: '2023-03-28'.
            dueDate_eq (string): You can use this param to provide a date and the responses will contain exact matches of projects that match the given due date. Example: '2023-03-28'.
            dueDate_lt (string): You can use this param to provide a date and the responses will contain projects whose date are less than the given due date. Example: '2023-03-28'.
            dueDate_ge (string): You can use this param to provide a date and the responses will contain projects whose date are greater than or equal to the given due date. Example: '2023-03-28'.
            dueDate_le (string): You can use this param to provide a date and the responses will contain projects whose date are less than or equal to the given due date. Example: '2023-03-28'.
            startDateActual_gt (string): You can use this param to provide a date and the responses will contain projects whose date are greater than the given actual start date. Example: '2023-03-28'.
            startDateActual_eq (string): You can use this param to provide a date and the responses will contain exact matches of projects that match the given actual start date. Example: '2023-03-28'.
            startDateActual_lt (string): You can use this param to provide a date and the responses will contain projects whose date are less than the given actual start date. Example: '2023-03-28'.
            startDateActual_ge (string): You can use this param to provide a date and the responses will contain projects whose date are greater than or equal to the given actual start date. Example: '2023-03-28'.
            startDateActual_le (string): You can use this param to provide a date and the responses will contain projects whose date are less than or equal to the given actual start date. Example: '2023-03-28'.
            dueDateActual_gt (string): You can use this param to provide a date and the responses will contain projects whose date are greater than the given actual due date. Example: '2023-03-28'.
            dueDateActual_eq (string): You can use this param to provide a date and the responses will contain exact matches of projects that match the given actual due date. Example: '2023-03-28'.
            dueDateActual_lt (string): You can use this param to provide a date and the responses will contain projects whose date are less than the given actual due date. Example: '2023-03-28'.
            dueDateActual_ge (string): You can use this param to provide a date and the responses will contain projects whose date are greater than or equal to the given actual due date. Example: '2023-03-28'.
            dueDateActual_le (string): You can use this param to provide a date and the responses will contain projects whose date are less than or equal to the given actual due date. Example: '2023-03-28'.
            createdAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain projects whose date are greater than the given project created date. Example: '1625164800000'.
            createdAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of projects that match the given project created date. Example: '1625164800000'.
            createdAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain projects whose date are less than the given project created date. Example: '1625164800000'.
            createdAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain projects whose date are greater than or equal to the given project created date. Example: '1625164800000'.
            createdAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain projects whose date are less than or equal to the given project created date. Example: '1625164800000'.
            updatedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain projects whose date are greater than the given project updated date. Example: '1625164800000'.
            updatedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of projects that match the given project updated date. Example: '1625164800000'.
            updatedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain projects whose date are less than the given project updated date. Example: '1625164800000'.
            updatedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain projects whose date are greater than or equal to the given project updated date. Example: '1625164800000'.
            updatedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain projects whose date are less than or equal to the given project updated date. Example: '1625164800000'.
            annualizedRecurringRevenue_eq (number): You can use this param to specify some value as ARR and the responses will contain exact matches of projects that match the given value. Example: '10000'.
            annualizedRecurringRevenue_gt (number): You can use this param to specify some value as ARR and the responses will contain exact matches of projects greater than that of the given value. Example: '10000'.
            annualizedRecurringRevenue_lt (number): You can use this param to specify some value as ARR and the responses will contain exact matches of projects lesser than that of the given value. Example: '10000'.
            projectFee_eq (number): You can use this param to specify some value as project fee and the responses will contain exact matches of projects that match the given value. Example: '10000'.
            projectFee_gt (number): You can use this param to specify some value as project fee and the responses will contain matches of projects greater than that of the given value. Example: '10000'.
            projectFee_lt (number): You can use this param to specify some value as project fee and the responses will contain matches of projects lesser than that of the given value. Example: '10000'.
            customerId_eq (string): You can use this param to provide a customer company id and the responses will contain exact matches of projects that match the given customer company id. Example: '1'.
            customerId_oneOf (string): You can use this param to provide customer company ids separated by commas and the responses will contain matches of projects that match any of the given customer company id. Example: '1,2,3'.
            customerId_noneOf (string): You can use this param to provide customer company id separated by commas and the responses will not contain matches of projects that match the given set of customer company id. Example: '1,2,3'.
            teamMemberId_eq (string): You can use this param to provide a team member id and the responses will contain exact matches of projects that match the given team member id. Example: '1'.
            teamMemberId_oneOf (string): You can use this param to provide team member ids separated by commas and the responses will contain matches of projects that match any of the given team member id. Example: '1,2,3'.
            teamMemberId_noneOf (string): You can use this param to provide team member id separated by commas and the responses will not contain matches of projects that match the given set of team member id. Example: '1,2,3'.
            companyId_eq (string): You can use this param to provide a customer company id and the responses will contain exact matches of projects that match the given customer company id. Example: '1'.
            companyId_oneOf (string): You can use this param to provide customer company ids separated by commas and the responses will contain matches of projects that match any of the given customer company id. Example: '1,2,3'.
            companyId_noneOf (string): You can use this param to provide customer company id separated by commas and the responses will not contain matches of projects that match the given set of customer company id. Example: '1,2,3'.
            projectName_eq (string): You can use this param to specify some project name and the responses will contain exact matches of projects that match the given name. Example: 'Stark Onboarding'.
            projectName_cn (string): You can use this param to specify some project name and the responses will contain matches of projects that match the given name. Example: 'Stark Onboarding'.
            projectName_nc (string): You can use this param to specify some project name and the responses will not contain matches of projects that match the given name. Example: 'Stark Onboarding'.
            inferredProgress_eq (array): You can use this param to provide a inferred progress  and the responses will contain exact matches of projects that match the given inferred progress.
            contractType_eq (array): You can use this param to provide a contract type and the responses will contain exact matches of projects that match the given contract type
            contractType_oneOf (array): You can use this param to provide contract types separated by commas and the responses will contain matches of projects that match any of the given contract types.
            contractType_noneOf (array): You can use this param to provide contract types separated by commas and the responses will not contain matches of projects that match the given set of contract types.
            budgetedHours_gt (string): You can use this param to provide a budgeted hour and the responses will contain projects whose budgeted hours are greater than the given budgeted hour. Example: '1'.
            budgetedHours_eq (string): You can use this param to provide a budgeted hour and the responses will contain exact matches of projects that match the given budgeted hour. Example: '2'.
            budgetedHours_lt (string): You can use this param to provide a budgeted hour and the responses will contain projects whose budgeted hours are less than the given budgeted hour. Example: '1'.
            budgetedHours_ge (string): You can use this param to provide a budgeted hour and the responses will contain projects whose budgeted hours are greater than or equal to the given budgeted hour. Example: '2'.
            allocatedHours_le (string): You can use this param to provide a allocated hour and the responses will contain projects whose allocated hours are less than or equal to the given allocated hour. Example: '1'.
            allocatedHours_gt (string): You can use this param to provide a allocated hour and the responses will contain projects whose allocated hours are greater than the given allocated hour. Example: '1'.
            allocatedHours_eq (string): You can use this param to provide a allocated hour and the responses will contain exact matches of projects that match the given allocated hour. Example: '2'.
            allocatedHours_lt (string): You can use this param to provide a allocated hour and the responses will contain projects whose allocated hours are less than the given allocated hour. Example: '1'.
            allocatedHours_ge (string): You can use this param to provide a allocated hour and the responses will contain projects whose allocated hours are greater than or equal to the given allocated hour. Example: '2'.
            customersInvited_gt (string): You can use this param to provide a number and the responses will contain projects that have more customers invited than given number of customers invited. Example: '1'.
            customersInvited_eq (string): You can use this param to provide a number and the responses will contain exact matches of projects that exactly have the given number of customers invited. Example: '2'.
            customersInvited_lt (string): You can use this param to provide a number and the responses will contain projects that have less customers invited than given number of customers invited. Example: '1'.
            customersInvited_ge (string): You can use this param to provide a number and the responses will contain projects that have equal or more customers invited than given number of customers invited. Example: '2'.
            customersInvited_le (string): You can use this param to provide a number and the responses will contain projects that have equal or less customers invited than given number of customers invited. Example: '1'.
            customersJoined_gt (string): You can use this param to provide a number and the responses will contain projects that have more customers joined than given number of customers joined. Example: '1'.
            customersJoined_eq (string): You can use this param to provide a number and the responses will contain exact matches of projects that exactly have the given number of customers joined. Example: '2'.
            customersJoined_lt (string): You can use this param to provide a number and the responses will contain projects that have less customers joined than given number of customers joined. Example: '1'.
            customersJoined_ge (string): You can use this param to provide a number and the responses will contain projects that have equal or more customers joined than given number of customers joined. Example: '2'.
            customersJoined_le (string): You can use this param to provide a number and the responses will contain projects that have equal or less customers joined than given number of customers joined. Example: '1'.
            includeArchive_eq (boolean): You can use this parameter to specify whether responses will include the archived projects. Example: 'False'.
            status_eq (string): You can use this param to provide status and the responses will contain projects that are equal to the given status Example: '1'.
            status_oneOf (string): You can use this param to provide statuses and the responses will contain projects that match one of the given statuses Example: '1,2'.
            status_noneOf (string): You can use this param to provide statuses and the responses will contain projects that matches none of the given statuses Example: '1,2'.
            externalReferenceId_eq (string): You can use this param to provide external reference id and the responses will contain projects that are equal to the given id Example: 'project_181866171876'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        url = f"{self.base_url}/1.0/projects"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("startDate.gt", startDate_gt),
                ("startDate.eq", startDate_eq),
                ("startDate.lt", startDate_lt),
                ("startDate.ge", startDate_ge),
                ("startDate.le", startDate_le),
                ("dueDate.gt", dueDate_gt),
                ("dueDate.eq", dueDate_eq),
                ("dueDate.lt", dueDate_lt),
                ("dueDate.ge", dueDate_ge),
                ("dueDate.le", dueDate_le),
                ("startDateActual.gt", startDateActual_gt),
                ("startDateActual.eq", startDateActual_eq),
                ("startDateActual.lt", startDateActual_lt),
                ("startDateActual.ge", startDateActual_ge),
                ("startDateActual.le", startDateActual_le),
                ("dueDateActual.gt", dueDateActual_gt),
                ("dueDateActual.eq", dueDateActual_eq),
                ("dueDateActual.lt", dueDateActual_lt),
                ("dueDateActual.ge", dueDateActual_ge),
                ("dueDateActual.le", dueDateActual_le),
                ("createdAt.gt", createdAt_gt),
                ("createdAt.eq", createdAt_eq),
                ("createdAt.lt", createdAt_lt),
                ("createdAt.ge", createdAt_ge),
                ("createdAt.le", createdAt_le),
                ("updatedAt.gt", updatedAt_gt),
                ("updatedAt.eq", updatedAt_eq),
                ("updatedAt.lt", updatedAt_lt),
                ("updatedAt.ge", updatedAt_ge),
                ("updatedAt.le", updatedAt_le),
                ("annualizedRecurringRevenue.eq", annualizedRecurringRevenue_eq),
                ("annualizedRecurringRevenue.gt", annualizedRecurringRevenue_gt),
                ("annualizedRecurringRevenue.lt", annualizedRecurringRevenue_lt),
                ("projectFee.eq", projectFee_eq),
                ("projectFee.gt", projectFee_gt),
                ("projectFee.lt", projectFee_lt),
                ("customerId.eq", customerId_eq),
                ("customerId.oneOf", customerId_oneOf),
                ("customerId.noneOf", customerId_noneOf),
                ("teamMemberId.eq", teamMemberId_eq),
                ("teamMemberId.oneOf", teamMemberId_oneOf),
                ("teamMemberId.noneOf", teamMemberId_noneOf),
                ("companyId.eq", companyId_eq),
                ("companyId.oneOf", companyId_oneOf),
                ("companyId.noneOf", companyId_noneOf),
                ("projectName.eq", projectName_eq),
                ("projectName.cn", projectName_cn),
                ("projectName.nc", projectName_nc),
                ("inferredProgress.eq", inferredProgress_eq),
                ("contractType.eq", contractType_eq),
                ("contractType.oneOf", contractType_oneOf),
                ("contractType.noneOf", contractType_noneOf),
                ("budgetedHours.gt", budgetedHours_gt),
                ("budgetedHours.eq", budgetedHours_eq),
                ("budgetedHours.lt", budgetedHours_lt),
                ("budgetedHours.ge", budgetedHours_ge),
                ("allocatedHours.le", allocatedHours_le),
                ("allocatedHours.gt", allocatedHours_gt),
                ("allocatedHours.eq", allocatedHours_eq),
                ("allocatedHours.lt", allocatedHours_lt),
                ("allocatedHours.ge", allocatedHours_ge),
                ("customersInvited.gt", customersInvited_gt),
                ("customersInvited.eq", customersInvited_eq),
                ("customersInvited.lt", customersInvited_lt),
                ("customersInvited.ge", customersInvited_ge),
                ("customersInvited.le", customersInvited_le),
                ("customersJoined.gt", customersJoined_gt),
                ("customersJoined.eq", customersJoined_eq),
                ("customersJoined.lt", customersJoined_lt),
                ("customersJoined.ge", customersJoined_ge),
                ("customersJoined.le", customersJoined_le),
                ("includeArchive.eq", includeArchive_eq),
                ("status.eq", status_eq),
                ("status.oneOf", status_oneOf),
                ("status.noneOf", status_noneOf),
                ("externalReferenceId.eq", externalReferenceId_eq),
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

    def create_project(
        self,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        projectId: int | None = None,
        projectName: str | None = None,
        startDate: str | None = None,
        dueDate: str | None = None,
        visibility: str | None = None,
        owner: dict[str, Any] | None = None,
        teamMembers: dict[str, Any] | None = None,
        status: dict[str, Any] | None = None,
        fields: list[dict[str, Any]] | None = None,
        customer: dict[str, Any] | None = None,
        partners: list[dict[str, Any]] | None = None,
        sources: list[dict[str, Any]] | None = None,
        assignProjectOwner: bool | None = None,
        placeholders: list[dict[str, Any]] | None = None,
        annualizedRecurringRevenue: int | None = None,
        projectFee: int | None = None,
        autoAllocation: bool | None = None,
        autoCreateCompany: bool | None = None,
        budgetedHours: float | None = None,
        financials: dict[str, Any] | None = None,
        currency: str | None = None,
        externalReferenceId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a project

        Args:
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            projectId (integer): The `identifier` of the project is generated by the system and can be used to identify the project globally. Example: '201'.
            projectName (string): The `name` of the project. The name specified will be displayed everywhere else and can be used for filtering purposes. Example: 'Acme onboarding'.
            startDate (string): On this date the project's execution officially begins. If sources (templates) are mentioned in the request, the start date is required. For projects without any defined sources, it may be empty. The format for the start date is _YYYY-MM-DD_. Example: '2023-03-28'.
            dueDate (string): The day on which the project's execution is planned to be completed. The due date is not required and can be left blank. If sources (templates) are included as part of the project creation, the project's due date will be calculated depending on the duration of the specified sources. For projects where both `startDate` and `dueDate` are specified, the latter must be on or after the given `startDate`. The format for the due date is _YYYY-MM-DD_. Example: '2023-03-28'.
            visibility (string): Set visibility parameters to restrict who can see your project. There are two options: `EVERYONE` and `MEMBERS`. Selecting `EVERYONE` allows all team members from your firm to view the project, while selecting `MEMBERS` restricts access to only those team members who have been specifically invited. Example: 'EVERYONE'.
            owner (object): The project owner is mandatory to be specified along with the project creation. The owner gets access to everything in the project and can be used to control the activities that happens in the project. Project owner will receive project invite email based on their notification configuration
            teamMembers (object): The teamMembers field can be used to specify the project members, customers and customerChampion. Once the project is created, an invite will be emailed to all the `teamMembers` specified.
            status (object): The value of the project status can be specified here and this is essential to keep track of the project. Example: 'In progress'.
            fields (array): The custom fields can be set during the project creation with the help of `fields`. The `fieldValue` can be either a string or a number or an array and it has to comply with the type of the field. Refer [examples](https://developer.rocketlane.com/v1.0/docs/custom-fields#examples-of-requests-and-responses-for-assigning-custom-field-values) to know how to assign `fieldValue` based on their `field_type`.
            customer (object): This field is required to identify the `customer` as part of the request. The customer's name is case-sensitive, and an exact match is required for further processing. It should be noted that once the customer information is entered, it cannot be modified during the project's lifespan.
            partners (array): The `partners` field is used to specify partner companies.
            sources (array): Sources denotes the project templates involved in creation/ imported post creation of the `project`.
            assignProjectOwner (boolean): When a project is created, you can use this param to automatically assign any unassigned tasks to the **project owner**. Note: If the project hasn’t been created using sources, this value will be skipped. Example: 'False'.
            placeholders (array): Rocketlane’s placeholders are associated with roles.  Based on the kind of roles and expertise that are needed to execute a task, placeholders can be added as assignees to templates as well as projects. Eventually, you can resolve placeholders by replacing them with team members according to their availability and role.
        Note: If the project is not built using sources, this value will be ignored but the mappings are retained and can be used in the future.
            annualizedRecurringRevenue (integer): Indicates the value of the recurring revenue of the customer's subscriptions for a single calendar year. Example: '10000'.
            projectFee (integer): The total fee that is charged for the project. Example: '100000'.
            autoAllocation (boolean): The field autoAllocation defines whether Auto Allocation is enabled for the project or not. If auto allocation is enabled, instead of adding it manually, the allocations are computed from the tasks duration, effort and the assignees specified in the project. Example: 'False'.
            autoCreateCompany (boolean): The field auto create company defines whether company should be created as part of the project creation. If the field is set to true, then if the company exists we re-use the company and proceed further. Else we will create a new company. Example: 'False'.
            budgetedHours (number): Budgeted hours represent the total hours allocated for project execution. This value can be edited at any point throughout the project’s duration. You can enter the budgeted hours in decimal form, including both hours and minutes, with up to two decimal places of precision. Eg: 1.65 hrs = 1h 39m(1.65h * 60m = 99m). Example: '10.5'.
            financials (object): This section addresses the financial aspects of the projects and the associated fields. Example: '1000'.
            currency (string): The currency for handling the project’s financials. You can only specify a currency for a project that is added at the account level. Please note that the project’s currency cannot to changed once set. Example: 'USD'.
            externalReferenceId (string): An externalReferenceId is a unique identifier that links entities or transactions between external systems and Rocketlane, ensuring accurate data correlation and consistency. Example: 'pr_8171'.

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        request_body_data = None
        request_body_data = {
            "projectId": projectId,
            "projectName": projectName,
            "startDate": startDate,
            "dueDate": dueDate,
            "visibility": visibility,
            "owner": owner,
            "teamMembers": teamMembers,
            "status": status,
            "fields": fields,
            "customer": customer,
            "partners": partners,
            "sources": sources,
            "assignProjectOwner": assignProjectOwner,
            "placeholders": placeholders,
            "annualizedRecurringRevenue": annualizedRecurringRevenue,
            "projectFee": projectFee,
            "autoAllocation": autoAllocation,
            "autoCreateCompany": autoCreateCompany,
            "budgetedHours": budgetedHours,
            "financials": financials,
            "currency": currency,
            "externalReferenceId": externalReferenceId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/projects"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def get_all_phases(
        self,
        projectId: int,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        startDate_gt: str | None = None,
        startDate_eq: str | None = None,
        startDate_lt: str | None = None,
        startDate_ge: str | None = None,
        startDate_le: str | None = None,
        dueDate_gt: str | None = None,
        dueDate_eq: str | None = None,
        dueDate_lt: str | None = None,
        dueDate_ge: str | None = None,
        dueDate_le: str | None = None,
        startDateActual_gt: str | None = None,
        startDateActual_eq: str | None = None,
        startDateActual_lt: str | None = None,
        startDateActual_ge: str | None = None,
        startDateActual_le: str | None = None,
        dueDateActual_gt: str | None = None,
        dueDateActual_eq: str | None = None,
        dueDateActual_lt: str | None = None,
        dueDateActual_ge: str | None = None,
        dueDateActual_le: str | None = None,
        createdAt_gt: int | None = None,
        createdAt_eq: int | None = None,
        createdAt_lt: int | None = None,
        createdAt_ge: int | None = None,
        createdAt_le: int | None = None,
        updatedAt_gt: int | None = None,
        updatedAt_eq: int | None = None,
        updatedAt_lt: int | None = None,
        updatedAt_ge: int | None = None,
        updatedAt_le: int | None = None,
        phaseName_eq: str | None = None,
        phaseName_cn: str | None = None,
        phaseName_nc: str | None = None,
    ) -> dict[str, Any]:
        """
        Get all phases

        Args:
            projectId (integer): The `identifier` of the project is generated by the system and can be used to identify the project globally. Example: '200'.
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            startDate_gt (string): You can use this param to specify some date and the responses will contain phases whose date are greater than the given date. Example: '2023-03-28'.
            startDate_eq (string): You can use this param to specify some date and the responses will contain exact matches of phases that match the given date. Example: '2023-03-28'.
            startDate_lt (string): You can use this param to specify some date and the responses will contain phases whose date are less than the given date. Example: '2023-03-28'.
            startDate_ge (string): You can use this param to specify some date and the responses will contain phases whose date are greater than or equal to the given date. Example: '2023-03-28'.
            startDate_le (string): You can use this param to specify some date and the responses will contain phases whose date are less than or equal to the given date. Example: '2023-03-28'.
            dueDate_gt (string): You can use this param to specify some date and the responses will contain phases whose date are greater than the given date. Example: '2023-03-28'.
            dueDate_eq (string): You can use this param to specify some date and the responses will contain exact matches of phases that match the given date. Example: '2023-03-28'.
            dueDate_lt (string): You can use this param to specify some date and the responses will contain phases whose date are less than the given date. Example: '2023-03-28'.
            dueDate_ge (string): You can use this param to specify some date and the responses will contain phases whose date are greater than or equal to the given date. Example: '2023-03-28'.
            dueDate_le (string): You can use this param to specify some date and the responses will contain phases whose date are less than or equal to the given date. Example: '2023-03-28'.
            startDateActual_gt (string): You can use this param to specify some date and the responses will contain phases whose date are greater than the given date. Example: '2023-03-28'.
            startDateActual_eq (string): You can use this param to specify some date and the responses will contain exact matches of phases that match the given date. Example: '2023-03-28'.
            startDateActual_lt (string): You can use this param to specify some date and the responses will contain phases whose date are less than the given date. Example: '2023-03-28'.
            startDateActual_ge (string): You can use this param to specify some date and the responses will contain phases whose date are greater than or equal to the given date. Example: '2023-03-28'.
            startDateActual_le (string): You can use this param to specify some date and the responses will contain phases whose date are less than or equal to the given date. Example: '2023-03-28'.
            dueDateActual_gt (string): You can use this param to specify some date and the responses will contain phases whose date are greater than the given date. Example: '2023-03-28'.
            dueDateActual_eq (string): You can use this param to specify some date and the responses will contain exact matches of phases that match the given date. Example: '2023-03-28'.
            dueDateActual_lt (string): You can use this param to specify some date and the responses will contain phases whose date are less than the given date. Example: '2023-03-28'.
            dueDateActual_ge (string): You can use this param to specify some date and the responses will contain phases whose date are greater than or equal to the given date. Example: '2023-03-28'.
            dueDateActual_le (string): You can use this param to specify some date and the responses will contain phases whose date are less than or equal to the given date. Example: '2023-03-28'.
            createdAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain phases whose date are greater than the given phases created date. Example: '1625164800000'.
            createdAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of phases that match the given phases created date. Example: '1625164800000'.
            createdAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain phases whose date are less than the given phases created date. Example: '1625164800000'.
            createdAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain phases whose date are greater than or equal to the given phases created date. Example: '1625164800000'.
            createdAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain phases whose date are less than or equal to the given phases created date. Example: '1625164800000'.
            updatedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain phases whose date are greater than the given phases updated date. Example: '1625164800000'.
            updatedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of phases that match the given phases updated date. Example: '1625164800000'.
            updatedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain phases whose date are less than the given phases updated date. Example: '1625164800000'.
            updatedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain phases whose date are greater than or equal to the given phases updated date. Example: '1625164800000'.
            updatedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain phases whose date are less than or equal to the given phases updated date. Example: '1625164800000'.
            phaseName_eq (string): You can use this param to specify some phase name and the responses will contain exact matches of phases that match the given name. Example: 'Stark Onboarding'.
            phaseName_cn (string): You can use this param to specify some phase name and the responses will contain matches of phases that match the given name. Example: 'Stark Onboarding'.
            phaseName_nc (string): You can use this param to specify some phase name and the responses will not contain matches of phases that match the given name. Example: 'Stark Onboarding'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Phases
        """
        url = f"{self.base_url}/1.0/phases"
        query_params = {
            k: v
            for k, v in [
                ("projectId", projectId),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("startDate.gt", startDate_gt),
                ("startDate.eq", startDate_eq),
                ("startDate.lt", startDate_lt),
                ("startDate.ge", startDate_ge),
                ("startDate.le", startDate_le),
                ("dueDate.gt", dueDate_gt),
                ("dueDate.eq", dueDate_eq),
                ("dueDate.lt", dueDate_lt),
                ("dueDate.ge", dueDate_ge),
                ("dueDate.le", dueDate_le),
                ("startDateActual.gt", startDateActual_gt),
                ("startDateActual.eq", startDateActual_eq),
                ("startDateActual.lt", startDateActual_lt),
                ("startDateActual.ge", startDateActual_ge),
                ("startDateActual.le", startDateActual_le),
                ("dueDateActual.gt", dueDateActual_gt),
                ("dueDateActual.eq", dueDateActual_eq),
                ("dueDateActual.lt", dueDateActual_lt),
                ("dueDateActual.ge", dueDateActual_ge),
                ("dueDateActual.le", dueDateActual_le),
                ("createdAt.gt", createdAt_gt),
                ("createdAt.eq", createdAt_eq),
                ("createdAt.lt", createdAt_lt),
                ("createdAt.ge", createdAt_ge),
                ("createdAt.le", createdAt_le),
                ("updatedAt.gt", updatedAt_gt),
                ("updatedAt.eq", updatedAt_eq),
                ("updatedAt.lt", updatedAt_lt),
                ("updatedAt.ge", updatedAt_ge),
                ("updatedAt.le", updatedAt_le),
                ("phaseName.eq", phaseName_eq),
                ("phaseName.cn", phaseName_cn),
                ("phaseName.nc", phaseName_nc),
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

    def create_phase(
        self,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        phaseId: int | None = None,
        phaseName: str | None = None,
        project: dict[str, Any] | None = None,
        startDate: str | None = None,
        dueDate: str | None = None,
        status: dict[str, Any] | None = None,
        private: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create a phase

        Args:
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            phaseId (integer): The `identifier` of the phase is generated by the system and can be used to identify the phase globally. Example: '201'.
            phaseName (string): The `name` of the phase. The name specified will be displayed everywhere else and can be used for filtering purposes. Example: 'Kick off'.
            project (object): The `project` associated with phase needs to be specified here and it is mandatory for the phase to get created and map accordingly.
            startDate (string): On this date the phase's execution officially begins. The start date is required. The format for the start date is _YYYY-MM-DD_. Example: '2023-03-28'.
            dueDate (string): The day on which the phase's execution is planned to be completed. The due date is required and cannot be left blank. The `dueDate` must be on or after the given `startDate`. The format for the due date is _YYYY-MM-DD_. Example: '2023-03-28'.
            status (object): The value of the phase status can be specified here and this is essential to keep track of the phase.
            private (boolean): Describes the privacy of the phase i.e. if it is private or shared. Example: 'True'.

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Phases
        """
        request_body_data = None
        request_body_data = {
            "phaseId": phaseId,
            "phaseName": phaseName,
            "project": project,
            "startDate": startDate,
            "dueDate": dueDate,
            "status": status,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/phases"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def update_field_option(
        self,
        fieldId: str,
        optionValue: int | None = None,
        optionColor: str | None = None,
        optionLabel: str | None = None,
    ) -> dict[str, Any]:
        """
        Update field Option

        Args:
            fieldId (string): fieldId
            optionValue (integer): The optionValue is the unique identifier and is unique for each field. Example: '3'.
            optionColor (string): The optionColor reflects the color of the options for the single or multiple choice field. Example: 'RED'.
            optionLabel (string): The optionLabel reflects the name of the options for the single or multiple choice field. Example: 'High'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Fields
        """
        if fieldId is None:
            raise ValueError("Missing required parameter 'fieldId'.")
        request_body_data = None
        request_body_data = {
            "optionValue": optionValue,
            "optionColor": optionColor,
            "optionLabel": optionLabel,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/fields/{fieldId}/update-option"
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

    def add_field_option(
        self,
        fieldId: str,
        optionColor: str | None = None,
        optionLabel: str | None = None,
    ) -> dict[str, Any]:
        """
        Add field Option

        Args:
            fieldId (string): fieldId
            optionColor (string): The optionColor reflects the color of the options for the single or multiple choice field. Example: 'RED'.
            optionLabel (string): The optionLabel reflects the name of the options for the single or multiple choice field. Example: 'High'.

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Fields
        """
        if fieldId is None:
            raise ValueError("Missing required parameter 'fieldId'.")
        request_body_data = None
        request_body_data = {
            "optionColor": optionColor,
            "optionLabel": optionLabel,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/fields/{fieldId}/add-option"
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

    def get_all_fields(
        self,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        createdAt_gt: int | None = None,
        createdAt_eq: int | None = None,
        createdAt_lt: int | None = None,
        createdAt_ge: int | None = None,
        createdAt_le: int | None = None,
        updatedAt_gt: int | None = None,
        updatedAt_eq: int | None = None,
        updatedAt_lt: int | None = None,
        updatedAt_ge: int | None = None,
        updatedAt_le: int | None = None,
        objectType_eq: str | None = None,
        fieldType_eq: str | None = None,
        enabled_eq: bool | None = None,
        private_eq: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get all fields

        Args:
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (array): This query parameter allows you to specify which field properties should be returned in the response body by selecting from the drop down. To get the relevant field properties, use comma separated values. If this field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the field properties should be returned in the response body. If the field is left blank, the default field properties are returned. Example: 'True'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            createdAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain fields whose date are greater than the given fields created date. Example: '1625164800000'.
            createdAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of fields that match the given fields created date. Example: '1625164800000'.
            createdAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain fields whose date are less than the given fields created date. Example: '1625164800000'.
            createdAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain fields whose date are greater than or equal to the given fields created date. Example: '1625164800000'.
            createdAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain fields whose date are less than or equal to the given fields created date. Example: '1625164800000'.
            updatedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain fields whose date are greater than the given fields updated date. Example: '1625164800000'.
            updatedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of fields that match the given fields updated date. Example: '1625164800000'.
            updatedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain fields whose date are less than the given fields updated date. Example: '1625164800000'.
            updatedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain fields whose date are greater than or equal to the given fields updated date. Example: '1625164800000'.
            updatedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain fields whose date are less than or equal to the given fields updated date. Example: '1625164800000'.
            objectType_eq (string): You can use this param to specify a object type for the fields and the responses will contain exact matches of fields that have the given object type.
            fieldType_eq (string): You can use this param to specify a field type for the fields and the responses will contain exact matches of fields that have the given field type.
            enabled_eq (boolean): You can use this parameter to specify whether responses will contains the enabled or disabled fields. Example: 'True'.
            private_eq (boolean): You can use this parameter to specify whether responses will contains the private or shared fields. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Fields
        """
        url = f"{self.base_url}/1.0/fields"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("createdAt.gt", createdAt_gt),
                ("createdAt.eq", createdAt_eq),
                ("createdAt.lt", createdAt_lt),
                ("createdAt.ge", createdAt_ge),
                ("createdAt.le", createdAt_le),
                ("updatedAt.gt", updatedAt_gt),
                ("updatedAt.eq", updatedAt_eq),
                ("updatedAt.lt", updatedAt_lt),
                ("updatedAt.ge", updatedAt_ge),
                ("updatedAt.le", updatedAt_le),
                ("objectType.eq", objectType_eq),
                ("fieldType.eq", fieldType_eq),
                ("enabled.eq", enabled_eq),
                ("private.eq", private_eq),
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

    def create_field(
        self,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        fieldId: int | None = None,
        fieldLabel: str | None = None,
        fieldDescription: str | None = None,
        fieldType: str | None = None,
        objectType: str | None = None,
        fieldOptions: list[dict[str, Any]] | None = None,
        ratingScale: str | None = None,
        enabled: bool | None = None,
        private: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create a Field

        Args:
            includeFields (array): This query parameter allows you to specify which field properties should be returned in the response body by selecting from the drop down. To get the relevant field properties, use comma separated values. If this field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the field properties should be returned in the response body. If the field is left blank, the default field properties are returned. Example: 'True'.
            fieldId (integer): The field’s unique, system-generated identifier, which can be used to identify the field globally. Example: '201'.
            fieldLabel (string): The fieldLabel is the name of the field. Example: 'Priority'.
            fieldDescription (string): The description of the field. Example: 'Priority of the bug.'.
            fieldType (string): This defines type of the field. Refer [Custom Fields](https://developer.rocketlane.com/v1.0/docs/custom-fields) for further information Example: 'MULTI_LINE_TEXT'.
            objectType (string): This defines type of object that is associated with the field. This could be `TASK`, `PROJECT` or `USER`. Example: 'PROJECT'.
            fieldOptions (array): The fieldOptions params define the value and label for the different options available for `SINGLE_CHOICE` and `MULTIPLE_CHOICE` fields.
            ratingScale (string): The number of stars in the Rating Scale when Field Type is `RATING`. Example: 'THREE'.
            enabled (boolean): This depicts if the field is enabled or not. Only those fields which are enabled will reflect in the account. Example: 'False'.
            private (boolean): This depicts if the field is private or not. Example: 'False'.

        Returns:
            dict[str, Any]: The resource was successfully created in the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Fields, important
        """
        request_body_data = None
        request_body_data = {
            "fieldId": fieldId,
            "fieldLabel": fieldLabel,
            "fieldDescription": fieldDescription,
            "fieldType": fieldType,
            "objectType": objectType,
            "fieldOptions": fieldOptions,
            "ratingScale": ratingScale,
            "enabled": enabled,
            "private": private,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/1.0/fields"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def get_user(
        self,
        userId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get user by Id

        Args:
            userId (string): userId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users, important
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/1.0/users/{userId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def get_all_users(
        self,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        firstName_eq: str | None = None,
        firstName_cn: str | None = None,
        firstName_nc: str | None = None,
        lastName_eq: str | None = None,
        lastName_cn: str | None = None,
        lastName_nc: str | None = None,
        email_eq: str | None = None,
        email_cn: str | None = None,
        email_nc: str | None = None,
        status_eq: list[str] | None = None,
        status_oneOf: list[str] | None = None,
        status_noneOf: list[str] | None = None,
        type_eq: list[str] | None = None,
        type_oneOf: list[str] | None = None,
        roleId_eq: str | None = None,
        roleId_oneOf: str | None = None,
        roleId_noneOf: str | None = None,
        permissionId_eq: str | None = None,
        permissionId_oneOf: str | None = None,
        permissionId_noneOf: str | None = None,
        capacityInMinutes_eq: float | None = None,
        capacityInMinutes_gt: float | None = None,
        capacityInMinutes_ge: float | None = None,
        capacityInMinutes_lt: float | None = None,
        capacityInMinutes_le: float | None = None,
        createdAt_gt: int | None = None,
        createdAt_eq: int | None = None,
        createdAt_lt: int | None = None,
        createdAt_ge: int | None = None,
        createdAt_le: int | None = None,
        updatedAt_gt: int | None = None,
        updatedAt_eq: int | None = None,
        updatedAt_lt: int | None = None,
        updatedAt_ge: int | None = None,
        updatedAt_le: int | None = None,
    ) -> dict[str, Any]:
        """
        Get all users

        Args:
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            firstName_eq (string): You can use this param to specify some user first name and the responses will contain exact matches of users that match the given first name. Example: 'John'.
            firstName_cn (string): You can use this param to specify some user first name and the responses will contain matches of users that match the given first name. Example: 'John'.
            firstName_nc (string): You can use this param to specify some user first name and the responses will not contain matches of users that match the given first name. Example: 'John'.
            lastName_eq (string): You can use this param to specify some user last name and the responses will contain exact matches of users that match the given last ame. Example: 'Doe'.
            lastName_cn (string): You can use this param to specify some user last name and the responses will contain matches of users that match the given last name. Example: 'Doe'.
            lastName_nc (string): You can use this param to specify some user last name and the responses will not contain matches of users that match the given last name. Example: 'Doe'.
            email_eq (string): You can use this param to specify some user email id and the responses will contain exact matches of users that match the given email id. Example: 'johndoe@rocketlane.com'.
            email_cn (string): You can use this param to specify some user email id and the responses will contain matches of users that match the given email id. Example: 'johndoe@rocketlane.com'.
            email_nc (string): You can use this param to specify some user email id and the responses will not contain matches of users that match the given email id. Example: 'johndoe@rocketlane.com'.
            status_eq (array): You can use this param to provide a user status  and the responses will contain exact matches of users that match the given status.
            status_oneOf (array): You can use this param to provide user statuses separated by commas and the responses will contain matches of users that match one of the given user status.
            status_noneOf (array): You can use this param to provide user statuses separated by commas and the responses will contain matches of users that match the none of the given set of user statuses.
            type_eq (array): You can use this param to provide a user type  and the responses will contain exact matches of users that match the given type.
            type_oneOf (array): You can use this param to provide user types separated by commas and the responses will contain matches of users that match the none of the given set of user types.
            roleId_eq (string): You can use this param to provide a role id and the responses will contain exact matches of users that match the given role id. Example: '1'.
            roleId_oneOf (string): You can use this param to provide role ids separated by commas and the responses will contain matches of users that match one of the given role id. Example: '1,2,3'.
            roleId_noneOf (string): You can use this param to provide role id separated by commas and the responses will contain matches of users that match the none of the given set of role id. Example: '1,2,3'.
            permissionId_eq (string): You can use this param to provide a permission id and the responses will contain exact matches of users that match the given permission id. Example: '1'.
            permissionId_oneOf (string): You can use this param to provide permission ids separated by commas and the responses will contain matches of users that match one of the given set of permission id. Example: '1,2,3'.
            permissionId_noneOf (string): You can use this param to provide permission ids separated by commas and the responses will contain matches of users that match the none of the given set of permission id. Example: '1,2,3'.
            capacityInMinutes_eq (number): You can use this param to specify some value as capacity and the responses will contain exact matches of users that match the given value. Example: '2400'.
            capacityInMinutes_gt (number): You can use this param to specify some value as capacity and the responses will contain exact matches of capacity greater than that of the given value. Example: '2400'.
            capacityInMinutes_ge (number): You can use this param to specify some value as capacity and the responses will contain exact matches of capacity greater than or equal to that of the given value. Example: '2400'.
            capacityInMinutes_lt (number): You can use this param to specify some value as capacity and the responses will contain exact matches of capacity lesser than that of the given value. Example: '2400'.
            capacityInMinutes_le (number): You can use this param to specify some value as capacity and the responses will contain exact matches of capacity lesser than or equal to that of the given value. Example: '2400'.
            createdAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain users whose date are greater than the given users created date. Example: '1625164800000'.
            createdAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of users that match the given users created date. Example: '1625164800000'.
            createdAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain users whose date are less than the given users created date. Example: '1625164800000'.
            createdAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain users whose date are greater than or equal to the given users created date. Example: '1625164800000'.
            createdAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain users whose date are less than or equal to the given users created date. Example: '1625164800000'.
            updatedAt_gt (integer): You can use this param to provide an epoch milli value and the responses will contain users whose date are greater than the given users updated date. Example: '1625164800000'.
            updatedAt_eq (integer): You can use this param to provide an epoch milli value and the responses will contain exact matches of users that match the given users updated date. Example: '1625164800000'.
            updatedAt_lt (integer): You can use this param to provide an epoch milli value and the responses will contain users whose date are less than the given users updated date. Example: '1625164800000'.
            updatedAt_ge (integer): You can use this param to provide an epoch milli value and the responses will contain users whose date are greater than or equal to the given users updated date. Example: '1625164800000'.
            updatedAt_le (integer): You can use this param to provide an epoch milli value and the responses will contain users whose date are less than or equal to the given users updated date. Example: '1625164800000'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        url = f"{self.base_url}/1.0/users"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("firstName.eq", firstName_eq),
                ("firstName.cn", firstName_cn),
                ("firstName.nc", firstName_nc),
                ("lastName.eq", lastName_eq),
                ("lastName.cn", lastName_cn),
                ("lastName.nc", lastName_nc),
                ("email.eq", email_eq),
                ("email.cn", email_cn),
                ("email.nc", email_nc),
                ("status.eq", status_eq),
                ("status.oneOf", status_oneOf),
                ("status.noneOf", status_noneOf),
                ("type.eq", type_eq),
                ("type.oneOf", type_oneOf),
                ("roleId.eq", roleId_eq),
                ("roleId.oneOf", roleId_oneOf),
                ("roleId.noneOf", roleId_noneOf),
                ("permissionId.eq", permissionId_eq),
                ("permissionId.oneOf", permissionId_oneOf),
                ("permissionId.noneOf", permissionId_noneOf),
                ("capacityInMinutes.eq", capacityInMinutes_eq),
                ("capacityInMinutes.gt", capacityInMinutes_gt),
                ("capacityInMinutes.ge", capacityInMinutes_ge),
                ("capacityInMinutes.lt", capacityInMinutes_lt),
                ("capacityInMinutes.le", capacityInMinutes_le),
                ("createdAt.gt", createdAt_gt),
                ("createdAt.eq", createdAt_eq),
                ("createdAt.lt", createdAt_lt),
                ("createdAt.ge", createdAt_ge),
                ("createdAt.le", createdAt_le),
                ("updatedAt.gt", updatedAt_gt),
                ("updatedAt.eq", updatedAt_eq),
                ("updatedAt.lt", updatedAt_lt),
                ("updatedAt.ge", updatedAt_ge),
                ("updatedAt.le", updatedAt_le),
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

    def get_timeoff(
        self,
        timeOffId: str,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get time-off by Id

        Args:
            timeOffId (string): timeOffId
            includeFields (array): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time-Offs
        """
        if timeOffId is None:
            raise ValueError("Missing required parameter 'timeOffId'.")
        url = f"{self.base_url}/1.0/time-offs/{timeOffId}"
        query_params = {
            k: v
            for k, v in [
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
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

    def delete_timeoff(self, timeOffId: str) -> Any:
        """
        Delete a time-off

        Args:
            timeOffId (string): timeOffId

        Returns:
            Any: The resource was successfully removed from the database.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time-Offs
        """
        if timeOffId is None:
            raise ValueError("Missing required parameter 'timeOffId'.")
        url = f"{self.base_url}/1.0/time-offs/{timeOffId}"
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

    def search_time_entries(
        self,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: str | None = None,
        includeAllFields: bool | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        date_gt: str | None = None,
        date_eq: str | None = None,
        date_lt: str | None = None,
        date_ge: str | None = None,
        date_le: str | None = None,
        project_eq: float | None = None,
        task_eq: float | None = None,
        projectPhase_eq: float | None = None,
        category_eq: float | None = None,
        user_eq: float | None = None,
        sourceType_eq: str | None = None,
        activityName_eq: str | None = None,
        activityName_cn: str | None = None,
        activityName_nc: str | None = None,
        approvalStatus_eq: str | None = None,
    ) -> dict[str, Any]:
        """
        Search time entries

        Args:
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (string): This query parameter allows you to specify which fields should be returned in the response body by selecting from the drop down. To get the relevant fields, use comma separated values. If the field is left blank, the default properties are returned. Example: 'notes,user'.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field. Valid fields to perform sortBy are: `MINUTES`, `DATE`, `ID` and `BILLABLE`.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            date_gt (string): You can use this param to specify some date and the responses will contain time-entries whose date are greater than the given date. Example: '2023-03-28'.
            date_eq (string): You can use this param to specify some date and the responses will contain exact matches of time-entries that match the given date. Example: '2023-03-28'.
            date_lt (string): You can use this param to specify some date and the responses will contain time-entries whose date are less than the given date. Example: '2023-03-28'.
            date_ge (string): You can use this param to specify some date and the responses will contain time-entries whose date are greater than or equal to the given date. Example: '2023-03-28'.
            date_le (string): You can use this param to specify some date and the responses will contain time-entries whose date are less than or equal to the given date. Example: '2023-03-28'.
            project_eq (number): You can use this param to specify some project Id and the responses will contain exact matches of time-entries that match the given project. Example: '201'.
            task_eq (number): You can use this param to specify some task Id and the responses will contain exact matches of time-entries that match the given task. Example: '202'.
            projectPhase_eq (number): You can use this param to specify some project phase Id and the responses will contain exact matches of time-entries that match the given phase. Example: '210'.
            category_eq (number): You can use this param to specify some category Id and the responses will contain exact matches of time-entries that match the given category. Example: '5'.
            user_eq (number): You can use this param to specify some user Id and the responses will contain exact matches of time-entries that belong to the user with the given user Id. Example: '5'.
            sourceType_eq (string): You can use this param to specify a source type for the time entries and the responses will contain exact matches of time-entries that have the given source type.
            activityName_eq (string): You can use this param to specify some activity name and the responses will contain exact matches of time-entries that match the given activity name. Example: 'Pre-Sales Campaign'.
            activityName_cn (string): You can use this param to specify some text and the responses will contain time-entries that contain the given text in their activity name. Example: 'Sales'.
            activityName_nc (string): You can use this param to specify some text and the responses will contain time-entries that _DO NOT_ contain the given text in their activity name. Example: 'Sales'.
            approvalStatus_eq (string): You can use this param to specify an approval status for the time entries and the responses will contain exact matches of time-entries that have the given approval type.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time Tracking
        """
        url = f"{self.base_url}/1.0/time-entries/search"
        query_params = {
            k: v
            for k, v in [
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("date.gt", date_gt),
                ("date.eq", date_eq),
                ("date.lt", date_lt),
                ("date.ge", date_ge),
                ("date.le", date_le),
                ("project.eq", project_eq),
                ("task.eq", task_eq),
                ("projectPhase.eq", projectPhase_eq),
                ("category.eq", category_eq),
                ("user.eq", user_eq),
                ("sourceType.eq", sourceType_eq),
                ("activityName.eq", activityName_eq),
                ("activityName.cn", activityName_cn),
                ("activityName.nc", activityName_nc),
                ("approvalStatus.eq", approvalStatus_eq),
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

    def get_time_entry_categories(
        self, pageSize: float | None = None, pageToken: str | None = None
    ) -> dict[str, Any]:
        """
        Get time entry categories

        Args:
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Time Tracking
        """
        url = f"{self.base_url}/1.0/time-entries/categories"
        query_params = {
            k: v
            for k, v in [("pageSize", pageSize), ("pageToken", pageToken)]
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

    def get_all_resource_allocations(
        self,
        startDate: str,
        endDate: str,
        pageSize: float | None = None,
        pageToken: str | None = None,
        includeFields: list[str] | None = None,
        includeAllFields: bool | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        match: str | None = None,
        memberId_eq: str | None = None,
        memberId_oneOf: str | None = None,
        memberId_noneOf: str | None = None,
        projectId_eq: str | None = None,
        projectId_oneOf: str | None = None,
        projectId_noneOf: str | None = None,
        placeholderId_eq: str | None = None,
        placeholderId_oneOf: str | None = None,
        placeholderId_noneOf: str | None = None,
    ) -> dict[str, Any]:
        """
        Get all Resource allocations

        Args:
            startDate (string): You can use this parameter to define the start date, and the API response will return all resource allocations that start on or after the specified date. Example: '2023-03-28'.
            endDate (string): You can use this parameter to define an end date, and the API will return allocations that end on or before the specified date. Example: '2023-03-28'.
            pageSize (number): This parameter sets the maximum number of responses to be displayed per page. If the page size is insufficient to accommodate the whole number of responses obtained, the pagination object will include a link to the next page as well as the next page token. If left blank, it defaults to 100. Example: '100'.
            pageToken (string): Use this parameter to specify the pageToken of a page to which you want to navigate. This pageToken can be obtained from a previous request which specified a limit and will only be active for 15 minutes after it is created. Example: '59c12a42-dd10-11ed-afa1-0242ac120002'.
            includeFields (array): Use this query parameter to opt in for fields to be returned in the response body. Use comma separated values to fetch the respective fields. If left blank, default properties are returned.
            includeAllFields (boolean): This query parameter allows you to specify if all the fields should be returned in the response body. If the field is left blank, the default properties are returned. Example: 'True'.
            sortBy (string): You can use the sortBy param to sort the responses by the given field.
            sortOrder (string): The sortOrder param can be used to specify the sorting order, which can be Ascending (ASC) or Descending (DESC). Descending is the default option.
            match (string): You can use the match param to specify if we need to filter the entries using either AND(all) / OR(any). Defaults to AND.
            memberId_eq (string): You can use this parameter to specify a member id, and the API will return allocations that exactly match the given member id. This allows for precise filtering of allocations based on the specified user. Example: '1'.
            memberId_oneOf (string): You can use this parameter to specify multiple member ids, separated by commas, and the API will return allocations that match any of the provided member ids.  Example: '1,2,3'.
            memberId_noneOf (string): You can use this parameter to specify multiple member ids, separated by commas, and the API will return allocations that exclude any of the provided member ids. Example: '1,2,3'.
            projectId_eq (string): You can use this parameter to specify a project id, and the API will return allocations that exactly match the given project id. Example: '1'.
            projectId_oneOf (string): You can use this parameter to specify multiple project ids, separated by commas, and the API will return allocations that match any of the provided project ids. Example: '1,2,3'.
            projectId_noneOf (string): You can use this parameter to specify multiple project ids, separated by commas, and the API will return allocations that exclude any of the provided project ids. Example: '1,2,3'.
            placeholderId_eq (string): You can use this parameter to specify a placeholder id, and the API will return allocations that exactly match the given placeholder id. Example: '1'.
            placeholderId_oneOf (string): You can use this parameter to specify multiple placeholder ids, separated by commas, and the API will return allocations that match any of the provided placeholder ids. Example: '1,2,3'.
            placeholderId_noneOf (string): You can use this parameter to specify multiple placeholder ids, separated by commas, and the API will return allocations that exclude any matching placeholder ids. Example: '1,2,3'.

        Returns:
            dict[str, Any]: The requested action was successfully executed.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Resource Allocations
        """
        url = f"{self.base_url}/1.0/resource-allocations"
        query_params = {
            k: v
            for k, v in [
                ("startDate", startDate),
                ("endDate", endDate),
                ("pageSize", pageSize),
                ("pageToken", pageToken),
                ("includeFields", includeFields),
                ("includeAllFields", includeAllFields),
                ("sortBy", sortBy),
                ("sortOrder", sortOrder),
                ("match", match),
                ("memberId.eq", memberId_eq),
                ("memberId.oneOf", memberId_oneOf),
                ("memberId.noneOf", memberId_noneOf),
                ("projectId.eq", projectId_eq),
                ("projectId.oneOf", projectId_oneOf),
                ("projectId.noneOf", projectId_noneOf),
                ("placeholderId.eq", placeholderId_eq),
                ("placeholderId.oneOf", placeholderId_oneOf),
                ("placeholderId.noneOf", placeholderId_noneOf),
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

    def list_tools(self):
        return [
            self.get_time_entry,
            self.update_time_entry,
            self.delete_time_entry,
            self.get_task,
            self.update_task,
            self.delete_task,
            self.get_space,
            self.update_space,
            self.delete_space,
            self.get_space_document,
            self.update_space_document,
            self.delete_space_document,
            self.get_project,
            self.update_project,
            self.delete_project,
            self.get_phase,
            self.update_phase,
            self.delete_phase,
            self.get_field,
            self.update_field,
            self.delete_field,
            self.get_all_timeoffs,
            self.create_timeoff,
            self.get_all_time_entries,
            self.create_time_entry,
            self.remove_followers_from_task,
            self.remove_dependencies_from_task,
            self.remove_assignees_from_task,
            self.move_task_to_given_phase,
            self.add_followers_to_task,
            self.add_dependencies_to_task,
            self.add_assignee_to_task,
            self.get_all_tasks,
            self.create_task,
            self.get_all_spaces,
            self.create_space,
            self.get_all_space_documents,
            self.create_space_document,
            self.unassign_placeholders,
            self.remove_members,
            self.import_template,
            self.assign_placeholders,
            self.archive_project,
            self.add_members,
            self.get_all_projects,
            self.create_project,
            self.get_all_phases,
            self.create_phase,
            self.update_field_option,
            self.add_field_option,
            self.get_all_fields,
            self.create_field,
            self.get_user,
            self.get_all_users,
            self.get_timeoff,
            self.delete_timeoff,
            self.search_time_entries,
            self.get_time_entry_categories,
            self.get_all_resource_allocations,
        ]
